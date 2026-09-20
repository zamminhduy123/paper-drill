"""Dashboard: vault awareness with zero infra (plain Markdown)."""
import re
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAPERS, IDEAS, CONCEPTS = ROOT / "vault" / "papers", ROOT / "vault" / "ideas", ROOT / "vault" / "concepts"
SCOPES, DEST = ROOT / "config" / "scopes", ROOT / "vault" / "Dashboard.md"
HUB_RE, DATE_RE = re.compile(r"\[\[Concept - (.+?)\]\]"), re.compile(r"(20\d\d-\d\d-\d\d)")
TITLE_RE, YEAR_RE, SCORE_RE = re.compile(r'^title:\s*"?(.*?)"?\s*$', re.M), re.compile(r"^year:\s*(\d{4})?", re.M), re.compile(r"^relevance_score:\s*([\d.]+)?", re.M)


def _meta(p):
    """Parse frontmatter title/year/score plus hubs and mtime date."""
    t = p.read_text(errors="ignore")
    ti = (TITLE_RE.search(t) or [None, p.stem]).group(1)
    y = (YEAR_RE.search(t) or [None, None]).group(1) or "?"
    s = (SCORE_RE.search(t) or [None, "0"]).group(1) or 0
    return {"title": ti, "year": y, "score": float(s), "hubs": HUB_RE.findall(t), "day": datetime.fromtimestamp(p.stat().st_mtime).date().isoformat()}


def build():
    """Scan vault, write Dashboard.md with 4 plain tables, return path."""
    papers = sorted((_meta(p) for p in PAPERS.glob("*.md") if p.is_file()), key=lambda d: d["score"], reverse=True)
    counts = {}
    for d in papers:
        for h in dict.fromkeys(x.strip() for x in d["hubs"] if x.strip()):
            counts[h] = counts.get(h, 0) + 1
    for c in CONCEPTS.glob("*.md"):
        counts.setdefault(c.stem.replace("Concept - ", ""), 0)
    ideas = []
    for p in IDEAS.glob("*.md"):
        m = DATE_RE.search(p.name)
        dt = m.group(1) if m else datetime.fromtimestamp(p.stat().st_mtime).date().isoformat()
        sc = p.name[: m.start()].rstrip("-_ ") if m else "unknown" or "unknown"
        ideas.append((dt, sc or "unknown", p.name, p.read_text(errors="ignore").count("[[Paper - ")))
    ideas.sort(reverse=True)
    scopes = [q.stem for q in SCOPES.glob("*.yaml")]
    fresh = {sc for dt, sc, _, _ in ideas if len(dt) == 10 and (date.today() - date.fromisoformat(dt)).days <= 7} if ideas else set()
    warns = ["- no hubs: " + t for t in [d["title"] for d in papers if not d["hubs"]]]
    warns += [f"- low score (<4): {d['title']} ({d['score']})" for d in papers if d["score"] < 4]
    warns += ["- stale scope (no notes this week): " + s for s in scopes if s not in fresh]
    L = [f"# Dashboard\n_updated {date.today().isoformat()} · {len(papers)} papers, {len(counts)} hubs, {len(ideas)} ideas_\n",
         "## New papers (by day, score desc)\n| date | title | year | score |\n|---|---|---|---|\n"]
    L += [f"| {d['day']} | {d['title']} | {d['year']} | {d['score']} |" for d in papers] or ["_none_"]
    L += ["\n## Concept hubs (papers using each hub)\n| hub | papers | flag |\n|---|---|---|\n"]
    L += [f"| {h} | {n} | {'single-use' if n == 1 else 'unused' if n == 0 else ''} |" for h, n in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))] or ["_none_"]
    L += ["\n## Ideas (date, scope, linked papers)\n| date | scope | file | linked papers |\n|---|---|---|---|\n"]
    L += [f"| {dt} | {sc} | {fn} | {n} |" for dt, sc, fn, n in ideas] or ["_none_"]
    L += ["\n## Warnings\n"] + (warns or ["- none"])
    L += ['\n```dataview\nTABLE year, relevance_score FROM "papers" SORT relevance_score DESC\n```']
    DEST.write_text("\n".join(L) + "\n")
    return DEST
