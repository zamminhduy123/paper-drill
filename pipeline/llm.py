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


async def arun(prompt: str, timeout: int = 300) -> str:
    """Try glm, deepseek, then local chat with same prompt, return first good text."""
    try:
        text = await glm_web.ask(prompt, timeout=timeout)
        if _ok(text):
            return text
    except Exception:
        pass
    try:
        text = await deepseek_web.ask(prompt, timeout=timeout)
        if _ok(text):
            return text
    except Exception:
        pass
    try:
        from .extract import chat
        text = chat(prompt, timeout=timeout)
        if _ok(text):
            return text
    except Exception:
        pass
    raise RuntimeError("all LLM rungs failed or returned busy text")


def run(prompt: str, timeout: int = 300) -> str:
    """Run async chain from sync contexts, return first good text."""
    return asyncio.run(arun(prompt, timeout=timeout))
