"""Daily: ingest -> rank -> extract -> writer."""
import asyncio
import json
import re
from datetime import date
from pathlib import Path

from . import dashboard, extract, gap, ingest, rank, record, writer

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / "state"

REL_RE = re.compile(r"^\s*(?:-\s*)?(\d+(?:\.\d+)?)\s*(?:/10)?\s*(?:—|-|:)?")

MAX_ATTEMPTS = 3


def _item_id(it):
    """Return stable queue id: openalex_id else slug-prefixed title."""
    return it.get("openalex_id") or ("slug:" + writer.slugify(it.get("title") or "untitled"))


def _queue_entry(item, scope, window, attempts):
    """Build pending entry dict with id, scope, window, attempts, item."""
    return {"id": _item_id(item), "scope": scope, "window": window, "attempts": attempts, "item": item}


def _process_one(it, thesis, backfill):
    """Extract, parse, and write one item, return (path, rec, body)."""
    abstract = it.get("abstract") or it["title"]  # ponytail: title-only, full abstract when OpenAlex abstract_inverted_index wired
    body = extract.extract(thesis, it["title"], abstract)
    rec = record.parse(body)
    rec.update({"title": it["title"], "year": it.get("year"), "body": body,
                "relevance": parse_relevance(body, it.get("score", 0) * 10)})
    if it.get("doi") and record._is_empty(rec.get("doi")):
        rec["doi"] = it["doi"]
    if record.validate(rec):
        rec["body"] += "\n\n#needs-review"
    return writer.write_record(rec, force=not backfill), rec, body


def parse_relevance(body, fallback):
    """Parse 0-10 relevance from extract body, fallback to rank score."""
    for line in body.split("## Relevance Score")[-1].splitlines():
        m = REL_RE.match(line)
        if m:
            return float(m.group(1))
    return fallback


def report_path(scope="ivn"):
    """Resolve state/<scope>-report.json path."""
    return STATE / f"{scope}-report.json"


def records_path(scope="ivn"):
    """Resolve state/<scope>-records.json path."""
    return STATE / f"{scope}-records.json"


def write_report(scope, report):
    """Write read-only per-scope run report JSON."""
    dest = report_path(scope)
    dest.parent.mkdir(exist_ok=True)
    dest.write_text(json.dumps(report, indent=2))
    return dest


def run(scope="ivn", backfill=False, frm=None, to=None):
    """Run pending-retries then ingest-rank-extract-write with overflow queued, return paths."""
    cfg = rank.load_cfg(scope)
    thesis = cfg["seeds"]["thesis_statements"][0]
    threshold = cfg["thresholds"]["semantic_edge"]
    window = frm or ingest.current_window(scope)
    model = rank.load_model(scope=scope)
    store = ingest.load_seen(scope)
    today = date.today().isoformat()
    paths, seen, bodies, failed_ids, recs = [], set(), [], [], []
    still_pending, dead_ids, dead_reasons = [], [], {}
    extract_budget = min(cfg["limits"]["keep"], 5)
    pending_processed, fresh_processed, tried = 0, 0, 0
    pending_list = ingest.load_pending(scope)
    for idx, entry in enumerate(pending_list):
        if tried >= extract_budget:  # ponytail: budget is total, remainder stays queued untouched
            still_pending.extend(pending_list[idx:])
            break
        it = entry.get("item") or {}
        attempts = int(entry.get("attempts") or 0) + 1
        slug = writer.slugify(it.get("title") or entry.get("id") or "untitled")
        if slug in seen:  # ponytail: same title twice in queue, first wins
            continue
        seen.add(slug)
        if backfill and (writer.PAPERS / f"Paper - {slug}.md").exists():
            continue
        try:
            path, rec, body = _process_one(it, thesis, backfill)
        except Exception as e:  # ponytail: failure = queued, never a stub note
            print(f"skip {slug}: retry failed: {e}")
            tried += 1
            failed_ids.append(entry.get("id"))
            if attempts >= MAX_ATTEMPTS:
                dead_ids.append(entry.get("id"))
                dead_reasons[entry.get("id")] = str(e)[:200]
            else:
                still_pending.append(_queue_entry(it, scope, entry.get("window", window), attempts))
            continue
        tried += 1
        pending_processed += 1
        paths.append(path)
        recs.append(rec)
        bodies.append(body)
        for k in ingest.keys_of(it):
            store[k] = today
    items = ingest.ingest(limit=cfg["limits"]["per_run"], mode="backfill" if backfill else "new", frm=frm, to=to, scope=scope)
    counts = dict(getattr(ingest, "last_counts", {}) or {"available": len(items), "examined": len(items)})
    if not counts.get("examined"):
        counts = {"available": counts.get("available", len(items)), "examined": len(items)}
    found = len(items)
    ranked = rank.rank(items, thesis, model, threshold=threshold, keep=cfg["limits"]["keep"])
    stats = dict(getattr(rank, "last_stats", None) or {"threshold": threshold, "above": len(ranked), "below": found - len(ranked)})
    rank.state_paths(scope)[1].write_text(json.dumps(ranked, indent=2))
    report = {"scope": scope, "date": today, "found": found, "selected": len(ranked),
              "processed": 0, "failed": 0, "failed_ids": [], "threshold": stats.get("threshold", threshold),
              "above_threshold": stats.get("above", len(ranked)), "below_threshold": stats.get("below", max(0, found - len(ranked))),
              "available": counts.get("available", found), "examined": counts.get("examined", found),
              "selection_reason": f"score >= {stats.get('threshold', threshold)}"}
    queued_ids = {e["id"] for e in still_pending}
    for it in ranked:
        if _item_id(it) in queued_ids:
            continue
        slug = writer.slugify(it["title"])
        if slug in seen:  # ponytail: OpenAlex double-indexes same title, backfill from ranked
            continue
        seen.add(slug)
        if backfill and (writer.PAPERS / f"Paper - {slug}.md").exists():
            continue
        if tried >= extract_budget:  # ponytail: budget caps cost, overflow queues unprocessed, never dropped
            still_pending.append(_queue_entry(it, scope, window, 0))
            queued_ids.add(_item_id(it))
            continue
        try:
            path, rec, body = _process_one(it, thesis, backfill)
        except Exception as e:  # ponytail: skip paper, never overwrite good note with stub
            print(f"skip {slug}: extract failed: {e}")
            tried += 1
            failed_ids.append(_item_id(it))
            still_pending.append(_queue_entry(it, scope, window, 1))
            queued_ids.add(_item_id(it))
            continue
        tried += 1
        fresh_processed += 1
        paths.append(path)
        recs.append(rec)
        bodies.append(body)
        for k in ingest.keys_of(it):
            store[k] = today
    if paths:
        ingest.save_seen(store, scope)
        records_path(scope).write_text(json.dumps(recs, indent=2))
        try:  # ponytail: 1 gap call/day, never break daily on failure
            scopes = (scope,)
            card_paths = asyncio.run(gap.cards_run(scopes))
            if not card_paths:
                print("skip ideas: no records/thin evidence, no card written")
            else:
                for cp in card_paths:
                    print(cp)
        except Exception:
            pass
    ingest.save_pending(still_pending, scope)
    if not backfill and not still_pending and ingest.fetch_complete(scope, window):
        ingest.advance_cursor(scope, today)
    try:  # ponytail: dashboard never breaks daily
        dashboard.build()
    except Exception:
        pass
    report.update({"selected": len(ranked), "processed": len(paths), "failed": len(failed_ids), "failed_ids": failed_ids,
                   "pending": len(still_pending), "pending_ids": [e["id"] for e in still_pending],
                   "pending_processed": pending_processed, "fresh_processed": fresh_processed,
                   "dead": len(dead_ids), "dead_ids": dead_ids, "dead_reasons": dead_reasons})
    write_report(scope, report)
    if failed_ids:
        print(f"SCOPE-FAILED {scope} failed={len(failed_ids)} processed={len(paths)} selected={len(ranked)}")
    return paths


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--scope", default="ivn")
    p.add_argument("--backfill", action="store_true")
    p.add_argument("--from", dest="frm", default=None)
    p.add_argument("--to", dest="to", default=None)
    p.add_argument("--cross", action="store_true")
    a = p.parse_args()
    if a.cross:
        print(asyncio.run(gap.cross_run()))
        try:  # ponytail: dashboard never breaks daily
            dashboard.build()
        except Exception:
            pass
    else:
        paths = run(scope=a.scope, backfill=a.backfill, frm=a.frm, to=a.to)
        for pth in paths:
            print(pth)
        try:
            failed = (json.loads(report_path(a.scope).read_text()) or {}).get("failed", 0)
        except Exception:
            failed = 0
        if failed:
            print(f"SCOPE-FAILED {a.scope} failed={failed}")
            raise SystemExit(1)
