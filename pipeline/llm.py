"""LLM chain with content-level busy detection and fallback."""
import asyncio
import re

from . import deepseek_web, glm_web

BUSY_RE = re.compile(r"at capacity|server is busy|try again later|overloaded|rate limit exceeded", re.I)


def _ok(text) -> bool:
    """Return True when text is non-empty and not a busy notice."""
    if not text or not str(text).strip():
        return False
    return not BUSY_RE.search(str(text))


def _scrub(msg) -> str:
    """Redact bearer/token secrets and truncate message to 100 chars."""
    s = re.sub(r"(?i)(bearer\s+[^\s'\";]+|token\s*[:=]\s*[^\s'\";,]+)", "[redacted]", str(msg))
    return s[:100]


async def arun(prompt: str, timeout: int = 600, thinking: bool = True) -> str:
    """Try deepseek, glm, then local chat with same prompt, return first good text."""
    fails = []
    try:
        text = await deepseek_web.ask(prompt, timeout=timeout, thinking=thinking)
        if _ok(text):
            return text
        fails.append("deepseek: busy-text")
    except Exception as e:
        fails.append(f"deepseek: {type(e).__name__}({_scrub(e)})")
    try:
        text = await glm_web.ask(prompt, timeout=timeout, thinking=thinking)
        if _ok(text):
            return text
        fails.append("glm: busy-text")
    except Exception as e:
        fails.append(f"glm: {type(e).__name__}({_scrub(e)})")
    try:
        from .extract import chat
        text = chat(prompt, timeout=timeout)
        if _ok(text):
            return text
        fails.append("qwen: busy-text")
    except Exception as e:
        fails.append(f"qwen: {type(e).__name__}({_scrub(e)})")
    raise RuntimeError(f"all LLM rungs failed: {'; '.join(fails)}")


def run(prompt: str, timeout: int = 600, thinking: bool = True) -> str:
    """Run async chain from sync contexts, return first good text."""
    return asyncio.run(arun(prompt, timeout=timeout, thinking=thinking))
