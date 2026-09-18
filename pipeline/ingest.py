"""Ingest: OpenAlex /works newest-first, dedupe on openalex_id."""
import json
import time
from datetime import date
from pathlib import Path

import requests
import yaml

ROOT = Path(__file__).resolve().parent.parent
SCOPES = ROOT / "config" / "scopes"
STATE = ROOT / "state"
API = "https://api.openalex.org/works"

def cfg_path(scope="ivn"):
    """Resolve config/scopes/<scope>.yaml path."""
    return SCOPES / f"{scope}.yaml"


def load_cfg(scope="ivn"):
    """Load scope yaml (keywords, dates, limits)."""
    return yaml.safe_load(cfg_path(scope).read_text())

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


def state_paths(scope="ivn"):
    """Resolve per-scope (latest, seen, cursor) state paths."""
    return (STATE / f"{scope}-latest.json", STATE / f"{scope}-seen.json", STATE / f"{scope}-cursor.txt")


def load_seen(scope="ivn"):
    """Load seen {id: date} map, empty dict when missing."""
    seen = state_paths(scope)[1]
    return json.loads(seen.read_text()) if seen.exists() else {}


def save_seen(seen, scope="ivn"):
    """Persist seen {id: date} map to state/<scope>-seen.json."""
    dest = state_paths(scope)[1]
    dest.parent.mkdir(exist_ok=True)
    dest.write_text(json.dumps(seen, indent=2))


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


def ingest(limit=50, per_page=50, mode="new", frm=None, to=None, scope="ivn"):
    """Fetch OpenAlex window, drop seen IDs, save seen, advance cursor."""
    cfg = load_cfg(scope)
    out_path, _, cursor_path = state_paths(scope)
    ox = cfg["sources"]["openalex"]
    q = "|".join(f'"{k}"' for k in cfg["seeds"]["keywords"])
    if mode == "backfill":
        filt = f"from_publication_date:{frm},to_publication_date:{to},title-and-abstract.search:{q}"
    else:
        start = cursor_path.read_text().strip() if cursor_path.exists() else ox["from_publication_date"]
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
    store = load_seen(scope)
    today = date.today().isoformat()
    fresh = []
    for it in out:
        keys = keys_of(it)
        if any(k in store for k in keys):
            continue
        fresh.append(it)
        for k in keys:
            store[k] = today
    save_seen(store, scope)
    if mode == "new":
        cursor_path.parent.mkdir(exist_ok=True)
        cursor_path.write_text(today)
    return fresh


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("limit", nargs="?", type=int, default=None)
    p.add_argument("--scope", default="ivn")
    a = p.parse_args()
    n = a.limit or load_cfg(a.scope)["limits"]["per_run"]
    assert n > 0, "limit must be positive"
    items = ingest(limit=n, scope=a.scope)
    assert isinstance(items, list), "ingest must return list"
    assert len(items) == len({i["openalex_id"] for i in items}), "dedupe broken"
    for w in items[:5]:  # eyeball check
        print(f"{w['year']} | {w['title']}")
    out_path = state_paths(a.scope)[0]
    out_path.parent.mkdir(exist_ok=True)
    out_path.write_text(json.dumps(items, indent=2))
    # TODO: publisher_fetch hook (config sources.publisher_fetch)
