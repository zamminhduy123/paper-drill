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
    """Run ingest-rank-extract-write for top-5, return written paths."""
    cfg = rank.load_cfg(scope)
    thesis = cfg["seeds"]["thesis_statements"][0]
    threshold = cfg["thresholds"]["semantic_edge"]
    items = ingest.ingest(limit=cfg["limits"]["per_run"], mode="backfill" if backfill else "new", frm=frm, to=to, scope=scope)
    counts = dict(getattr(ingest, "last_counts", {}) or {"available": len(items), "examined": len(items)})
    if not counts.get("examined"):
        counts = {"available": counts.get("available", len(items)), "examined": len(items)}
    found = len(items)
    model = rank.load_model(scope=scope)
    ranked = rank.rank(items, thesis, model, threshold=threshold, keep=cfg["limits"]["keep"])
    stats = dict(getattr(rank, "last_stats", None) or {"threshold": threshold, "above": len(ranked), "below": found - len(ranked)})
    rank.state_paths(scope)[1].write_text(json.dumps(ranked, indent=2))
    report = {"scope": scope, "date": date.today().isoformat(), "found": found, "selected": len(ranked),
              "processed": 0, "failed": 0, "failed_ids": [], "threshold": stats.get("threshold", threshold),
              "above_threshold": stats.get("above", len(ranked)), "below_threshold": stats.get("below", max(0, found - len(ranked))),
              "available": counts.get("available", found), "examined": counts.get("examined", found),
              "selection_reason": f"score >= {stats.get('threshold', threshold)}"}
    if not ranked:
        write_report(scope, report)
        return []
    paths, seen, bodies, failed_ids, recs = [], set(), [], [], []
    store = ingest.load_seen(scope)
    today = date.today().isoformat()
    for it in ranked:
        if len(paths) >= min(cfg["limits"]["keep"], 5):
            break
        slug = writer.slugify(it["title"])
        if slug in seen:  # ponytail: OpenAlex double-indexes same title, backfill from ranked
            continue
        seen.add(slug)
        if backfill and (writer.PAPERS / f"Paper - {slug}.md").exists():
            continue
        abstract = it.get("abstract") or it["title"]  # ponytail: title-only, full abstract when OpenAlex abstract_inverted_index wired
        try:
            body = extract.extract(thesis, it["title"], abstract)
        except Exception as e:  # ponytail: skip paper, never overwrite good note with stub
            print(f"skip {slug}: extract failed: {e}")
            failed_ids.append(it.get("openalex_id") or slug)
            continue
        rec = record.parse(body)
        # fill metadata from ingest item, flag thin records
        rec.update({"title": it["title"], "year": it.get("year"), "body": body,
                    "relevance": parse_relevance(body, it["score"] * 10)})
        if it.get("doi") and record._is_empty(rec.get("doi")):
            rec["doi"] = it["doi"]
        if record.validate(rec):
            rec["body"] += "\n\n#needs-review"
        paths.append(writer.write_record(rec, force=not backfill))
        recs.append(rec)
        bodies.append(body)
        for k in ingest.keys_of(it):
            store[k] = today
    if paths:
        ingest.save_seen(store, scope)
        records_path(scope).write_text(json.dumps(recs, indent=2))
        try:  # ponytail: 1 gap call/day, never break daily on failure
            lims = [m.group(1).strip() for b in bodies for m in re.finditer(r"## Explicit Limitations\s*(.*?)(?=\n## |\Z)", b, re.S) if m.group(1).strip()]
            ideas = asyncio.run(gap.run(lims, thesis, cfg["seeds"]["datasets"]))
            papers = [writer.slugify(it["title"]) for it in ranked[:5]]
            concepts = list(dict.fromkeys(h for b in bodies for h in writer.HUB_RE.findall(b)))
            print(gap.save(ideas, path=ROOT / "vault" / "ideas" / f"{scope}-{date.today().isoformat()}.md", papers=papers, concepts=concepts))
        except Exception:
            pass
    try:  # ponytail: dashboard never breaks daily
        dashboard.build()
    except Exception:
        pass
    report.update({"selected": len(ranked), "processed": len(paths), "failed": len(failed_ids), "failed_ids": failed_ids})
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
