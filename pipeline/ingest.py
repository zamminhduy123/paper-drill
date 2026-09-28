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

last_counts = {"available": 0, "examined": 0}

RESULTS_CAP = 500

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


def pending_path(scope="ivn"):
    """Resolve state/<scope>-pending.json durable retry queue path."""
    return STATE / f"{scope}-pending.json"


def load_pending(scope="ivn"):
    """Load pending retry queue, empty list when missing."""
    p = pending_path(scope)
    return json.loads(p.read_text()) if p.exists() else []


def save_pending(pending, scope="ivn"):
    """Persist pending retry queue to state/<scope>-pending.json."""
    dest = pending_path(scope)
    dest.parent.mkdir(exist_ok=True)
    dest.write_text(json.dumps(pending, indent=2))


def current_window(scope="ivn"):
    """Return current fetch window start (cursor or config default)."""
    _, _, cursor_path = state_paths(scope)
    if cursor_path.exists():
        return cursor_path.read_text().strip()
    return load_cfg(scope)["sources"]["openalex"]["from_publication_date"]


def advance_cursor(scope="ivn", value=None):
    """Advance date cursor to value (today default), creating state dir."""
    _, _, cursor_path = state_paths(scope)
    cursor_path.parent.mkdir(exist_ok=True)
    cursor_path.write_text(value or date.today().isoformat())


def fetch_path(scope="ivn"):
    """Resolve state/<scope>-fetch.json resume offset path."""
    return STATE / f"{scope}-fetch.json"


def load_fetch(scope="ivn"):
    """Load fetch resume {window, offset, available}, empty dict when missing."""
    p = fetch_path(scope)
    try:
        d = json.loads(p.read_text()) if p.exists() else {}
    except Exception:
        return {}
    return d if isinstance(d, dict) else {}


def save_fetch(scope, window, offset, available):
    """Persist fetch resume {window, offset, available} to state file."""
    dest = fetch_path(scope)
    dest.parent.mkdir(exist_ok=True)
    dest.write_text(json.dumps({"window": window, "offset": offset, "available": available}))


def fetch_complete(scope, window):
    """Return True when stored offset covers available for window."""
    d = load_fetch(scope)
    if d.get("window") != window:
        return False
    try:
        return int(d.get("offset") or 0) >= int(d.get("available") or 0)
    except (TypeError, ValueError):
        return False


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


def ingest_with_counts(limit=50, per_page=50, mode="new", frm=None, to=None, scope="ivn"):
    """Fetch window page resuming at stored offset up to cap, return (fresh, counts)."""
    global last_counts
    cfg = load_cfg(scope)
    _, _, cursor_path = state_paths(scope)
    ox = cfg["sources"]["openalex"]
    q = "|".join(f'"{k}"' for k in cfg["seeds"]["keywords"])
    if mode == "backfill":
        filt = f"from_publication_date:{frm},to_publication_date:{to},title-and-abstract.search:{q}"
        window = f"{frm}:{to}"
    else:
        start = cursor_path.read_text().strip() if cursor_path.exists() else ox["from_publication_date"]
        filt = f"from_publication_date:{start},title-and-abstract.search:{q}"
        window = start
    prev = load_fetch(scope)
    start_offset = int(prev.get("offset") or 0) if prev.get("window") == window else 0
    try:
        known = int(prev.get("available") or 0) if prev.get("window") == window else 0
    except (TypeError, ValueError):
        known = 0
    available, examined = known, 0
    seen, out = set(), []
    page = start_offset // per_page + 1
    skip = start_offset % per_page
    first = True
    while examined < RESULTS_CAP and (available == 0 or start_offset + examined < available):
        params = {"filter": filt, "sort": "publication_date:desc", "per-page": per_page, "page": page, "mailto": ox["mailto"]}
        data = fetch(params) or {}
        if first:
            first = False
            try:
                available = int((data.get("meta") or {}).get("count") or known or 0)
            except (TypeError, ValueError):
                available = known
        raw = data.get("results") or []
        if not raw:
            break
        results = raw[skip:] if skip else raw
        skip = 0
        if not results:
            if len(raw) < per_page:
                break
            page += 1
            continue
        for w in results:
            if examined >= RESULTS_CAP:
                break
            if available and start_offset + examined >= available:
                break
            examined += 1
            oid = w.get("id")
            if oid in seen:
                continue
            seen.add(oid)
            out.append({"openalex_id": oid, "title": w.get("title"), "year": w.get("publication_year"), "doi": w.get("doi"), "abstract": inv_to_text(w.get("abstract_inverted_index")) or w.get("title")})
        if len(raw) < per_page:
            break
        page += 1
    new_offset = start_offset + examined
    save_fetch(scope, window, new_offset, available)
    store = load_seen(scope)
    fresh = []
    for it in out:
        keys = keys_of(it)
        if any(k in store for k in keys):
            continue
        fresh.append(it)
    # ponytail: never advance cursor here, daily.py advances only when offset covered and pending empty
    last_counts = {"available": available, "examined": examined, "offset": new_offset}
    ingest.last_counts = last_counts
    return fresh, dict(last_counts)


def ingest(limit=50, per_page=50, mode="new", frm=None, to=None, scope="ivn"):
    """Fetch OpenAlex window, drop seen IDs, return items only."""
    items, _ = ingest_with_counts(limit=limit, per_page=per_page, mode=mode, frm=frm, to=to, scope=scope)
    return items


ingest.last_counts = {"available": 0, "examined": 0}


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
