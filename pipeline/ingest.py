"""Ingest: OpenAlex /works newest-first, dedupe on openalex_id."""
import json
import sys
import time
from datetime import date
from pathlib import Path

import requests
import yaml

ROOT = Path(__file__).resolve().parent.parent
CFG = ROOT / "config" / "scope.yaml"
OUT = ROOT / "state" / "latest.json"
SEEN = ROOT / "state" / "seen.json"
CURSOR = ROOT / "state" / "cursor.txt"
API = "https://api.openalex.org/works"

def load_cfg():
    """Load scope.yaml (keywords, dates, limits)."""
    return yaml.safe_load(CFG.read_text())

def fetch(params, timeout=30):
    """GET OpenAlex with 3 retries, backoff honoring Retry-After."""
    r = None
    for attempt in range(4):
        try:
            r = requests.get(API, params=params, timeout=timeout)
            r.raise_for_status()
            return r.json()
        except Exception:
            if attempt == 3:
                raise
            try:
                raw = r.headers.get("Retry-After") if r is not None else None
            except Exception:
                raw = None
            try:
                wait = int(raw) or 2**attempt
            except (TypeError, ValueError):
                wait = 2**attempt
            time.sleep(min(60, wait))

def inv_to_text(inv):
    """Join OpenAlex abstract_inverted_index to plain text."""
    pos = {i: tok for tok, idxs in (inv or {}).items() for i in idxs}
    return " ".join(pos[i] for i in sorted(pos))


def load_seen():
    """Load seen {id: date} map, empty dict when missing."""
    return json.loads(SEEN.read_text()) if SEEN.exists() else {}


def save_seen(seen):
    """Persist seen {id: date} map to state/seen.json."""
    SEEN.parent.mkdir(exist_ok=True)
    SEEN.write_text(json.dumps(seen, indent=2))


def keys_of(item):
    """Return dedupe keys: openalex_id, else doi, else title slug."""
    keys = []
    if item.get("openalex_id"):
        keys.append(item["openalex_id"])
    if item.get("doi"):
        keys.append(item["doi"].lower().strip())
    if not keys:
        try:
            from .writer import slugify
        except ImportError:
            from pipeline.writer import slugify
        keys.append("slug:" + slugify(item.get("title") or "untitled"))
    return keys


def ingest(limit=50, per_page=50, mode="new", frm=None, to=None):
    """Fetch OpenAlex window, drop seen IDs, save seen, advance cursor."""
    cfg = load_cfg()
    ox = cfg["sources"]["openalex"]
    q = "|".join(f'"{k}"' for k in cfg["seeds"]["keywords"])
    if mode == "backfill":
        filt = f"from_publication_date:{frm},to_publication_date:{to},title-and-abstract.search:{q}"
    else:
        start = CURSOR.read_text().strip() if CURSOR.exists() else ox["from_publication_date"]
        filt = f"from_publication_date:{start},title-and-abstract.search:{q}"
    params = {"filter": filt, "sort": "publication_date:desc", "per-page": per_page, "mailto": ox["mailto"]}
    data = fetch(params).get("results", [])[:limit]
    seen, out = set(), []
    for w in data:
        oid = w.get("id")
        if oid in seen:
            continue
        seen.add(oid)
        out.append({"openalex_id": oid, "title": w.get("title"), "year": w.get("publication_year"), "doi": w.get("doi"), "abstract": inv_to_text(w.get("abstract_inverted_index")) or w.get("title")})
    store = load_seen()
    today = date.today().isoformat()
    fresh = []
    for it in out:
        keys = keys_of(it)
        if any(k in store for k in keys):
            continue
        fresh.append(it)
        for k in keys:
            store[k] = today
    save_seen(store)
    if mode == "new":
        CURSOR.parent.mkdir(exist_ok=True)
        CURSOR.write_text(today)
    return fresh


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else load_cfg()["limits"]["per_run"]
    assert n > 0, "limit must be positive"
    items = ingest(limit=n)
    assert isinstance(items, list), "ingest must return list"
    assert len(items) == len({i["openalex_id"] for i in items}), "dedupe broken"
    for w in items[:5]:  # eyeball check
        print(f"{w['year']} | {w['title']}")
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(items, indent=2))
    # TODO: publisher_fetch hook (config sources.publisher_fetch)
