"""GLM-web minimal client (chat.z.ai, stable semantic hooks, token-only)."""
import os
from asyncio import sleep
from time import time

LOGIN_URL = "https://chat.z.ai/"
TEXTBOX_CSS = '.messageInputContainer textarea'
SEND_CSS = '.sendMessageButton'


async def launch(headless=True):
    """Start zendriver browser on Z.ai chat, best-effort CF bypass."""
    import zendriver
    kwargs = {"headless": headless}
    if os.environ.get("BROWSER_PATH"):
        kwargs["browser_executable_path"] = os.environ["BROWSER_PATH"]
    browser = await zendriver.start(**kwargs)
    await browser.get(LOGIN_URL)
    try:
        await browser.main_tab.verify_cf()
    except Exception:
        pass  # no challenge presented
    return browser


async def login_token(browser, token=None):
    """Login via localStorage token, wait for chat box or raise."""
    token = token or os.environ.get("GLM_TOKEN")
    assert token, "export GLM_TOKEN first"
    await browser.main_tab.evaluate(
        f"localStorage.setItem('token', '{token}')",
        await_promise=True, return_by_value=True,
    )
    await browser.main_tab.reload()
    await sleep(4)
    await browser.main_tab.select(TEXTBOX_CSS, timeout=15)


def _scrape(html):
    """Extract markdown-ish assistant blocks as text."""
    from bs4 import BeautifulSoup
    from inscriptis import get_text
    soup = BeautifulSoup(html, "html.parser")
    blocks = soup.find_all(class_=lambda c: c and "markdown" in c.lower())
    if blocks:
        return "\n\n".join(get_text(str(b)).strip() for b in blocks)
    return ""


async def send_message(browser, message, timeout=180):
    """Send message, wait for stable response text, return it."""
    box = await browser.main_tab.select(TEXTBOX_CSS, timeout=15)
    await box.send_keys(message)
    send = await browser.main_tab.select(SEND_CSS, timeout=15)
    await send.click()
    end, last, stable_since = time() + timeout, "", time()
    while time() < end:
        await sleep(3)
        html = await browser.main_tab.evaluate(
            "document.documentElement.outerHTML", await_promise=True, return_by_value=True,
        )
        text = _scrape(html)
        if text and text != last:
            last, stable_since = text, time()
        if last and time() - stable_since > 9:
            return last
    raise TimeoutError("no stable response in timeout")


async def ask(message, token=None, timeout=180):
    """One-shot: launch, login, ask, close, return text."""
    browser = await launch()
    try:
        await login_token(browser, token)
        return await send_message(browser, message, timeout)
    finally:
        try:
            browser.stop()
        except Exception:
            pass
