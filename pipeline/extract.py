"""Extract: novelty, method, limitations, future work, concept hubs via Qwen (v2 locked)."""
import os
import requests

PROMPT = """You extract structured research info. Return Markdown with exactly these headings.
Thesis: {thesis}
Title: {title}
Abstract: {abstract}

Output:
## Novelty (2 bullets)
## Methodology (3 bullets)
## Explicit Limitations (bullets, quote if stated)
## Future Work (bullets)
## Concept Hubs (exactly 3-5, each MUST match [[Concept - <2-4 word noun>]], reuse existing names verbatim when possible, no other prefix)
## Relevance Score (0-10 + reason; 0-3 off-topic, 4-6 tangential, 7-8 related, 9-10 direct; be strict)
"""

def chat(prompt: str, base_url: str | None = None, model: str | None = None) -> str:
    """POST one chat completion to llama.cpp OpenAI-compatible endpoint."""
    base_url = base_url or os.environ.get("LLAMA_BASE_URL", "http://localhost:8080/v1")
    model = model or os.environ.get("LLAMA_MODEL", "Swift-Qwen3.8-27B-Q4_K_M")
    r = requests.post(
        f"{base_url}/chat/completions",
        json={"model": model, "messages": [{"role": "user", "content": prompt}],
              "temperature": 0.2, "max_tokens": 1200},
        timeout=300,
    )
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]

def extract(thesis: str, title: str, abstract: str) -> str:
    """Run locked v2 prompt, return structured Markdown block."""
    return chat(PROMPT.format(thesis=thesis, title=title, abstract=abstract))
