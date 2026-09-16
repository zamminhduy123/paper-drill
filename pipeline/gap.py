"""Gap: DeepSeek-web ideas with Qwen fallback (1 call/day)."""
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
    dest = Path(path) if path else Path(__file__).resolve().parent.parent / "vault" / "ideas" / f"{date.today().isoformat()}.md"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(text.strip() + "\n")
    return dest
