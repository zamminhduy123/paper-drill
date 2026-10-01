"""Gap: DeepSeek-web ideas with Qwen fallback (1 call/day)."""
import json
import re
import textwrap
from datetime import date
from pathlib import Path

from . import llm, rank, writer

ROOT = Path(__file__).resolve().parent.parent

LIM_RE = re.compile(r"## Explicit Limitations\s*(.*?)(?=\n## |\Z)", re.S)

CARD_FIELDS = ("Question", "Evidence", "Transfer", "Experiment", "Value")
CARD_METRICS = ("false alarms/hour", "detection delay", "accepted-error rate", "review workload", "post-shift performance")
CARD_NOVELTY = ("unchecked", "overlaps prior work", "specific difference")


def _card_slug(rec):
    """Slugify one card record title for vault [[Paper - X]] links."""
    return writer.slugify((rec or {}).get("title") or "untitled")


def _card_evidence(rec):
    """Render one record with author/inference/unknown labels preserved."""
    rec = rec or {}
    slug = _card_slug(rec)
    lines = [f"- title: {rec.get('title', 'not stated')}", f"- note: [[Paper - {slug}]]"]
    for f in ("monitoring_problem", "signal", "uncertainty_method", "action", "eval_setting",
              "limitation_author", "limitation_inference", "limitation_unknown",
              "support_passage", "transfer_ivn", "transfer_risk"):
        lines.append(f"- {f} (record label, do not relabel): {rec.get(f, 'not stated')}")
    return "\n".join(lines)


def build_card_prompt(records):
    """Build one disprovable candidate-card prompt from labeled records."""
    records = [r for r in (records or []) if r]
    slugs = [s for s in (_card_slug(r) for r in records)
             if (writer.PAPERS / f"Paper - {s}.md").exists()]
    allowed = ", ".join(f"[[Paper - {s}]]" for s in slugs) or "(none verified: use plain titles, no [[...]] links)"
    ev = "\n\n".join(_card_evidence(r) for r in records) or "(no records)"
    metrics = ", ".join(CARD_METRICS)
    novelty = ", ".join(CARD_NOVELTY)
    return (
        "Write exactly ONE candidate card with these EXACT sections, in order:\n"
        "## Question\n## Evidence\n## Transfer\n## Experiment\n## Value\n"
        "## Question: one disprovable claim (falsifiable, single sentence first).\n"
        "## Evidence: three labeled bullets: supporting papers, conflicting papers, unknown. "
        "Use only record labels below; never present inference as author-stated; write \"not stated\" when absent. "
        "Label thin/speculative parts as speculative.\n"
        "## Transfer: source field -> mechanism -> IVN problem, one line each.\n"
        "## Experiment: data, baseline, shift-or-failure condition, comparison.\n"
        f"## Value: one measurement from [{metrics}], the job skill it improves, feasibility, "
        f"and exactly one novelty line `Novelty status: <one of {novelty}>`.\n"
        f"Link rules: only these verified links may appear: {allowed}. "
        "Never invent [[Paper - X]] links; reuse record labels verbatim.\n"
        f"Records:\n{ev}\n"
    )


def _top_card_records(scopes, limit=3):
    """Load records files across scopes, return top-N by relevance desc."""
    all_recs = []
    for scope in scopes or []:
        try:
            recs = json.loads((ROOT / "state" / f"{scope}-records.json").read_text())
        except (OSError, ValueError):
            continue  # ponytail: missing/corrupt records file, skip scope
        all_recs.extend([r for r in (recs or []) if r])
    all_recs.sort(key=lambda r: float((r or {}).get("relevance", 0) or 0), reverse=True)
    return all_recs[:max(0, limit)]


async def cards_run(scopes=("ivn", "iot-ids", "nids")):
    """Generate <=3 candidate cards from top records, save via save(), return paths."""
    top = _top_card_records(scopes, limit=3)
    if not top:
        print("cards_run: no records, skipping"); return []
    today = date.today().isoformat()
    paths = []
    for i, rec in enumerate(top, 1):
        prompt = build_card_prompt([rec])
        text = await llm.arun(prompt, timeout=300)
        paths.append(save(text, path=ROOT / "vault" / "ideas" / f"card-{today}-{i}.md",
                          papers=[_card_slug(rec)]))
    return paths


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
    parts.append("Every section title MUST start with ##. Never repeat any section; output each section once.")
    return "\n".join(parts)


def records_lims(scope):
    """Load limitation_author/inference from state records, empty when absent."""
    try:
        recs = json.loads((ROOT / "state" / f"{scope}-records.json").read_text())
    except (OSError, ValueError):
        return []
    out = []
    for r in recs or []:
        for k in ("limitation_author", "limitation_inference"):
            v = str((r or {}).get(k, "") or "").strip()
            if v and v.lower() not in ("not stated", "not stated in abstract", "none", ""):
                out.append(v)
    return out


async def cross_run(scopes=("ivn", "iot-ids", "nids")):
    """Run one cross-scope gap prompt and save ideas note, return path."""
    sections, datasets, papers, concepts = {}, [], [], []
    for scope in scopes:
        try:
            items = json.loads(rank.state_paths(scope)[1].read_text())[:5]
        except (OSError, ValueError):
            continue  # ponytail: missing/corrupt ranked state, skip scope
        datasets.extend(rank.load_cfg(scope)["seeds"]["datasets"])
        lims = records_lims(scope) or []
        for it in items:
            slug = writer.slugify(it["title"])
            papers.append(slug)
            note = ROOT / "vault" / "papers" / f"Paper - {slug}.md"
            if not note.exists():
                continue
            body = note.read_text()
            if not lims:
                lims.extend(m.group(1).strip() for m in LIM_RE.finditer(body) if m.group(1).strip())
            concepts.extend(writer.HUB_RE.findall(body))
        sections[scope] = lims
    if not any(sections.values()):
        print("cross_run: no new limitations, skipping"); return None
    thesis = "Transfer proven methods across network intrusion domains (ivn, iot-ids, nids): apply Method X from one domain to Problem Y in another."
    prompt = build_cross_prompt(sections, thesis, list(dict.fromkeys(datasets)))
    ideas = await llm.arun(prompt, timeout=300)
    return save(ideas, path=ROOT / "vault" / "ideas" / f"cross-{date.today().isoformat()}.md", papers=papers, concepts=concepts)


CROSS_TITLES = ("Transfer Hypotheses", "Cross-Domain Transfer Proposals", "Claims Audit",
                "Research Splits", "IVN →", "IoT-IDS →", "NIDS →")


def _clean(text):
    """Cut a duplicated tail and promote bare cross-note section titles to ## headings."""
    def key(ln):
        """Reduce a line to bare wording so a bullet copy and a plain copy compare equal."""
        return re.sub(r"\s+", " ", re.sub(r"^[#*+\-\d. ]+", "", ln)).strip().lower()

    seen, lines = {}, []  # ponytail: exact-wording dedup, misses paraphrased copies
    for i, ln in enumerate(text.splitlines()):
        k = key(ln)
        if k:
            if k in seen and i - seen[k] >= 5:
                break
            seen.setdefault(k, i)
        lines.append(ln)
    out, secs = [], False
    for ln in lines:
        if ln.startswith("#"):
            secs = False
        elif not re.match(r"^[#*+-]", ln) and ln.startswith(CROSS_TITLES):
            ln, secs = "## " + ln, True
        elif secs and re.match(r"^\d+\. ", ln):
            ln = "**" + ln.split(". ", 1)[1].rstrip(".") + "**"
        out.append(ln)
    return "\n".join(out)


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
    else:
        text = _clean(text)
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
