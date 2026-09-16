"""Writer: paper md + concept stubs (stdlib only)."""
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAPERS = ROOT / "vault" / "papers"
CONCEPTS = ROOT / "vault" / "concepts"
HUB_RE = re.compile(r"\[\[Concept - (.+?)\]\]")


def slugify(title: str) -> str:
    """ASCII slug (80 chars) for vault filename."""
    ascii_ = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode()
    s = re.sub(r"[^A-Za-z0-9 _-]+", "", ascii_).strip()
    s = re.sub(r"\s+", " ", s)[:80].strip()
    return s or "untitled"


def write_paper(title, year, doi, relevance, body, force=False) -> Path:
    """Write paper note + missing concept stubs, return path."""
    PAPERS.mkdir(parents=True, exist_ok=True)
    CONCEPTS.mkdir(parents=True, exist_ok=True)
    dest = PAPERS / f"Paper - {slugify(title)}.md"
    if dest.exists() and not force:
        raise FileExistsError(f"{dest} exists (use force=True to overwrite)")
    hubs = HUB_RE.findall(body)
    text = (
        "---\n"
        f'title: "{title}"\n'
        f"year: {year}\n"
        f'doi: "{doi}"\n'
        f"relevance_score: {relevance}\n"
        "type: paper\n"
        "---\n"
        f"# {title}\n\n{body.strip()}\n"
    )
    dest.write_text(text)
    for h in dict.fromkeys(h.strip() for h in hubs if h.strip()):
        stub = CONCEPTS / f"Concept - {h}.md"
        if not stub.exists():
            stub.write_text(f"# Concept - {h}\nHub for {h}.\n")
    return dest


def check() -> Path:
    """Self-check: fixture note + 2 hubs resolve."""
    body = (
        "## Novelty\n- fixture\n## Methodology\n- fixture\n"
        "## Explicit Limitations\n- fixture\n## Future Work\n- fixture\n"
        "## Concept Hubs\n- [[Concept - Selfcheck Hub A]]\n- [[Concept - Selfcheck Hub B]]\n"
        "## Relevance Score\n9.0 fixture\n"
    )
    dest = write_paper("Writer Selfcheck", 2024, "", 9.0, body, force=True)
    text = dest.read_text()
    assert "[[Concept - Selfcheck Hub A]]" in text and "[[Concept - Selfcheck Hub B]]" in text
    for h in ("Selfcheck Hub A", "Selfcheck Hub B"):
        assert (CONCEPTS / f"Concept - {h}.md").exists(), h
    print(f"ok: {dest.relative_to(ROOT)} + 2 hubs resolve")
    return dest


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "check":
        check()
    else:
        sys.exit("usage: python -m pipeline.writer check")
