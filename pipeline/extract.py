"""Extract: novelty, method, limitations, future work, concept hubs via Qwen (v2 locked)."""
import os
from pathlib import Path
import requests
from dotenv import load_dotenv
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

PROMPT = """You extract structured research info. Return Markdown with exactly these headings.
Thesis: {thesis}
Title: {title}
Abstract: {abstract}

Output:
## Novelty
## Methodology
## Explicit Limitations
## Future Work
## Concept Hubs
## Relevance Score
3-5 hubs as [[Concept - Name]], 2-4 word noun, reuse names, never output angle brackets.
"""

def chat(
    prompt: str, 
    base_url: str | None = None, 
    model: str | None = None,
    api_key: str | None = None,
    temperature: float = 0.2,
    max_tokens: int | None = None,
    timeout: int = 300
) -> str:
    """POST one chat completion to llama.cpp OpenAI-compatible endpoint."""
    base_url = (base_url or os.environ.get("LLAMA_BASE_URL", "http://localhost:8080/v1")).rstrip("/")
    api_key = api_key or os.environ.get("LLAMA_API_KEY")
    model = model or os.environ.get("LLAMA_MODEL", "ukisai/Swift-Qwen3.8-27B-GGUF")
    headers = {
        "Content-Type": "application/json",
        "ngrok-skip-browser-warning": "true"
    }
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": temperature,
    }
    if max_tokens is not None:
        payload["max_tokens"] = max_tokens
    response = requests.post(
        f"{base_url}/chat/completions",
        headers=headers,
        json=payload,
        timeout=timeout,
    )
    response.raise_for_status()
    message = response.json()["choices"][0]["message"]
    # Return content, or fallback to reasoning_content if content is empty/None
    return message.get("content") or message.get("reasoning_content") or ""

def existing_hubs() -> list:
    """List existing concept hub names from vault stems."""
    d = Path(__file__).resolve().parent.parent / "vault" / "concepts"
    if not d.exists():
        return []
    return sorted(h for p in d.glob("Concept - *.md") for h in [p.name[len("Concept - "):-len(".md")]] if "<" not in h and ">" not in h)


def extract(thesis: str, title: str, abstract: str) -> str:
    """Run locked v2 prompt, return structured Markdown block."""
    hubs = existing_hubs()
    extra = f"\nExisting hubs: {', '.join(hubs)}\nReuse an existing hub verbatim when it fits; create a new one only when nothing fits.\n"
    return chat(PROMPT.format(thesis=thesis, title=title, abstract=abstract) + extra)


if __name__ == "__main__":
    print(chat("test"))