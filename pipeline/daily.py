"""Daily: ingest -> rank -> extract -> writer."""
import asyncio
import re

from . import extract, gap, ingest, rank, writer

REL_RE = re.compile(r"^\s*(?:-\s*)?(\d+(?:\.\d+)?)\s*(?:/10)?\s*(?:—|-|:)?")


def parse_relevance(body, fallback):
    """Parse 0-10 relevance from extract body, fallback to rank score."""
    for line in body.split("## Relevance Score")[-1].splitlines():
        m = REL_RE.match(line)
        if m:
            return float(m.group(1))
    return fallback


def run(backfill=False, frm=None, to=None):
    """Run ingest-rank-extract-write for top-5, return written paths."""
    cfg = rank.load_cfg()
    thesis = cfg["seeds"]["thesis_statements"][0]
    items = ingest.ingest(limit=cfg["limits"]["per_run"], mode="backfill" if backfill else "new", frm=frm, to=to)
    model = rank.load_model()
    ranked = rank.rank(items, thesis, model, threshold=cfg["thresholds"]["semantic_edge"], keep=cfg["limits"]["keep"])
    paths, seen, bodies = [], set(), []
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
            continue
        paths.append(writer.write_paper(it["title"], it.get("year"), it.get("doi") or "", parse_relevance(body, it["score"] * 10), body, force=not backfill))
        bodies.append(body)
    if paths:
        try:  # ponytail: 1 gap call/day, never break daily on failure
            lims = [m.group(1).strip() for b in bodies for m in re.finditer(r"## Explicit Limitations\s*(.*?)(?=\n## |\Z)", b, re.S) if m.group(1).strip()]
            ideas = asyncio.run(gap.run(lims, thesis, cfg["seeds"]["datasets"]))
            papers = [writer.slugify(it["title"]) for it in ranked[:5]]
            concepts = list(dict.fromkeys(h for b in bodies for h in writer.HUB_RE.findall(b)))
            print(gap.save(ideas, papers=papers, concepts=concepts))
        except Exception:
            pass
    return paths


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--backfill", action="store_true")
    p.add_argument("--from", dest="frm", default=None)
    p.add_argument("--to", dest="to", default=None)
    a = p.parse_args()
    for pth in run(backfill=a.backfill, frm=a.frm, to=a.to):
        print(pth)
