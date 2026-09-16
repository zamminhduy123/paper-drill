"""Ingest: OpenAlex /works newest-first, dedupe on openalex_id."""
import json
import sys
import time
from pathlib import Path

import requests
import yaml

ROOT = Path(__file__).resolve().parent.parent
CFG = ROOT / "config" / "scope.yaml"
OUT = ROOT / "state" / "latest.json"
API = "https://api.openalex.org/works"

def load_cfg():
    """Load scope.yaml (keywords, dates, limits)."""
    return yaml.safe_load(CFG.read_text())

def fetch(params, timeout=30):
    """GET OpenAlex with one retry on failure."""
    try:
        r = requests.get(API, params=params, timeout=timeout)
        r.raise_for_status()
        return r.json()
    except Exception:
        time.sleep(2)  # retry 1x
        r = requests.get(API, params=params, timeout=timeout)
        r.raise_for_status()
        return r.json()

def inv_to_text(inv):
    """Join OpenAlex abstract_inverted_index to plain text."""
    pos = {i: tok for tok, idxs in (inv or {}).items() for i in idxs}
    return " ".join(pos[i] for i in sorted(pos))


def ingest(limit=50, per_page=50):
    """Fetch newest OpenAlex works, dedupe on openalex_id."""
    cfg = load_cfg()
    ox = cfg["sources"]["openalex"]
    q = "|".join(f'"{k}"' for k in cfg["seeds"]["keywords"])
    params = {
        "filter": f"from_publication_date:{ox['from_publication_date']},title-and-abstract.search:{q}",
        "sort": "publication_date:desc",
        "per-page": per_page,
        "mailto": ox["mailto"],
    }
    data = fetch(params).get("results", [])[:limit]
    seen, out = set(), []
    for w in data:
        oid = w.get("id")
        if oid in seen:
            continue
        seen.add(oid)
        out.append({"openalex_id": oid, "title": w.get("title"), "year": w.get("publication_year"), "doi": w.get("doi"), "abstract": inv_to_text(w.get("abstract_inverted_index")) or w.get("title")})
    return out


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
