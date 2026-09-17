"""Gap: DeepSeek-web ideas with Qwen fallback (1 call/day)."""
import re
import textwrap
from datetime import date
from pathlib import Path

from . import deepseek_web, extract, rank


def build_prompt(thesis, limitations, datasets):
    """Build gap-ideas prompt constrained to scope datasets."""
    lims = "\n".join(f"- {x}" for x in limitations)
    names = ", ".join(datasets)
    return (
        f"Thesis: {thesis}\nExplicit limitations:\n{lims}\n"
        f"Propose concrete research splits using only these datasets: {names}.\n"
        f"Use no other dataset names."
    )


async def run(limitations, thesis=None, datasets=None):
    """Ask DeepSeek-web, fall back to Qwen on any failure."""
    if thesis is None or datasets is None:
        cfg = rank.load_cfg()
        thesis = thesis or cfg["seeds"]["thesis_statements"][0]
        datasets = datasets or cfg["seeds"]["datasets"]
    prompt = build_prompt(thesis, limitations, datasets)
    try:
        return await deepseek_web.ask(prompt, timeout=300)
    except Exception:
        return extract.chat(prompt, timeout=300)


def save(text, path=None):
    """Write ideas note, return path."""
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
    dest = Path(path) if path else Path(__file__).resolve().parent.parent / "vault" / "ideas" / f"{date.today().isoformat()}.md"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(text.strip() + "\n")
    return dest
