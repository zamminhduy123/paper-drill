"""Gap: DeepSeek-web ideas with Qwen fallback (1 call/day)."""
import json
import re
import textwrap
from datetime import date
from pathlib import Path

from . import llm, rank, writer

ROOT = Path(__file__).resolve().parent.parent

LIM_RE = re.compile(r"## Explicit Limitations\s*(.*?)(?=\n## |\Z)", re.S)


def build_prompt(thesis, limitations, datasets):
    """Build gap-ideas prompt constrained to scope datasets."""
    lims = "\n".join(f"- {x}" for x in limitations if x and x.strip())
    names = ", ".join(datasets)
    return (
        f"Thesis: {thesis}\nExplicit limitations:\n{lims}\n"
        f"Propose concrete research splits using only these datasets: {names}.\n"
        f"Use no other dataset names.\n"
        "For each claim output exactly three labeled parts: Author-stated (quote or \"not stated in abstract\"), Inference (model's, mark as such), Proposed experiment.\n"
        "Never present inference as author-stated; write \"not stated\" when absent.\n"
        "Format: use ## for section titles, - for bullets, 1. for numbered steps,\n"
        "and GitHub pipe tables (| col |) with a --- separator row for any tabular data.\n"
        "Never use space-aligned tables."
    )


async def run(limitations, thesis=None, datasets=None):
    """Ask GLM-web, fall back to DeepSeek-web, then Qwen."""
    limitations = [l.strip() for l in (limitations or []) if l and l.strip()]
    if thesis is None or datasets is None:
        cfg = rank.load_cfg()
        thesis = thesis or cfg["seeds"]["thesis_statements"][0]
        datasets = datasets or cfg["seeds"]["datasets"]
    prompt = build_prompt(thesis, limitations, datasets)
    return await llm.arun(prompt, timeout=300)


def build_cross_prompt(sections, thesis, datasets):
    """Build one cross-scope gap prompt with scope-labeled limitations."""
    parts = [f"Thesis: {thesis}"]
    for scope, lims in sections.items():
        clean = [x.strip() for x in (lims or []) if x and x.strip()]
        parts.append(f"Scope {scope} limitations:\n" + "\n".join(f"- {x}" for x in clean))
    names = ", ".join(datasets)
    parts.append("Propose concrete ideas shaped as `Method X from Scope A -> Problem Y in Scope B`.")
    parts.append(f"Propose concrete research splits using only these datasets: {names}.\nUse no other dataset names.")
    parts.append("For each claim output exactly three labeled parts: Author-stated (quote or \"not stated in abstract\"), Inference (model's, mark as such), Proposed experiment.")
    parts.append("Never present inference as author-stated; write \"not stated\" when absent.")
    parts.append("Format: use ## for section titles, - for bullets, 1. for numbered steps,\nand GitHub pipe tables (| col |) with a --- separator row for any tabular data.\nNever use space-aligned tables.")
    return "\n".join(parts)


async def cross_run(scopes=("ivn", "iot-ids", "nids")):
    """Run one cross-scope gap prompt and save ideas note, return path."""
    sections, datasets, papers, concepts = {}, [], [], []
    for scope in scopes:
        try:
            items = json.loads(rank.state_paths(scope)[1].read_text())[:5]
        except (OSError, ValueError):
            continue  # ponytail: missing/corrupt ranked state, skip scope
        datasets.extend(rank.load_cfg(scope)["seeds"]["datasets"])
        lims = []
        for it in items:
            slug = writer.slugify(it["title"])
            papers.append(slug)
            note = ROOT / "vault" / "papers" / f"Paper - {slug}.md"
            if not note.exists():
                continue
            body = note.read_text()
            lims.extend(m.group(1).strip() for m in LIM_RE.finditer(body) if m.group(1).strip())
            concepts.extend(writer.HUB_RE.findall(body))
        sections[scope] = lims
    if not any(sections.values()):
        print("cross_run: no new limitations, skipping"); return None
    thesis = "Transfer proven methods across network intrusion domains (ivn, iot-ids, nids): apply Method X from one domain to Problem Y in another."
    prompt = build_cross_prompt(sections, thesis, list(dict.fromkeys(datasets)))
    ideas = await llm.arun(prompt, timeout=300)
    return save(ideas, path=ROOT / "vault" / "ideas" / f"cross-{date.today().isoformat()}.md", papers=papers, concepts=concepts)


def save(text, path=None, papers=None, concepts=None):
    """Write ideas note, return path."""
    papers = list(dict.fromkeys(papers or []))
    concepts = list(dict.fromkeys(concepts or []))
    text = textwrap.dedent(text)
    lines = [ln.rstrip() for ln in text.splitlines()]
    lines = [ln.lstrip() if ln.strip() else "" for ln in lines]
    lines = [ln for ln in lines if not re.match(r"^\s*-\s*\d+\s*$", ln)]
    text = "\n".join(lines)
    if "Summary of Splits" in text:
        head, tail = text.split("Summary of Splits", 1)
        keep = []
        for ln in tail.splitlines():
            s = ln.strip()
            if s.startswith("Based on ") or s.startswith("Datasets:"):
                break
            keep.append(ln)
        text = head + "Summary of Splits" + "\n".join(keep)
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    text = text.strip()
    if papers:
        present = [p for p in papers if (writer.PAPERS / f"Paper - {p}.md").exists()]
        absent = [p for p in papers if not (writer.PAPERS / f"Paper - {p}.md").exists()]
        if present:
            text += "\n\n## Linked Papers\n" + "\n".join(f"[[Paper - {p}]]" for p in present)
        if absent:
            text += "\n\n## To investigate (notes absent)\n" + "\n".join(f"- {p}" for p in absent)
    if concepts:
        text += "\n\n## Linked Concepts\n" + "\n".join(f"[[Concept - {c}]]" for c in concepts)
    dest = Path(path) if path else Path(__file__).resolve().parent.parent / "vault" / "ideas" / f"{date.today().isoformat()}.md"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(text.strip() + "\n")
    return dest
