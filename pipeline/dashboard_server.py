"""Dashboard server: localhost-only vault browser reusing dashboard.py data (stdlib only)."""
import html
import json
import re
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, quote, urlparse

from pipeline.dashboard import CONCEPTS, IDEAS, PAPERS, SCOPES, _meta

ROOT = Path(__file__).resolve().parent.parent
LINK_RE = re.compile(r"\[\[(.+?)\]\]")
CSS = "body{font-family:sans-serif;max-width:900px;margin:2em auto;padding:0 1em;line-height:1.55}table{border-collapse:collapse;width:100%}td,th{border:1px solid #ccc;padding:.2em .5em;text-align:left}th{background:#f4f4f4}li{margin:.25em 0}nav a{margin-right:1em}pre{background:#f4f4f4;padding:1em;overflow:auto}"
NAV = '<nav><a href="/">overview</a><a href="/papers">papers</a><a href="/ideas">ideas</a></nav>'


def page(title, body):
    """Wrap body HTML in a minimal page shell."""
    t = html.escape(title)
    return f"<!doctype html><html><head><meta charset=utf-8><title>{t}</title><style>{CSS}</style></head><body>{NAV}<h1>{t}</h1>{body}</body></html>"


def md(text):
    """Render note Markdown-ish: lists, tables, bold, escaped HTML, [[links]], #/## headers."""
    def inline(s):
        """Apply [[links]] and **bold** to already-escaped text."""
        s = LINK_RE.sub(lambda m: f'<a href="/paper?slug={quote(m.group(1))}">{m.group(1)}</a>' if m.group(1).startswith("Paper - ") else f"<b>{m.group(1)}</b>", s)
        return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    text = html.escape(text)
    if text.startswith("---"):
        text = text.split("---", 2)[-1]
    lines, out, i, in_ul, in_ol = text.splitlines(), [], 0, False, False
    def close():
        """Close any open list tags and return the closers."""
        nonlocal in_ul, in_ol
        s = ("</ul>" if in_ul else "") + ("</ol>" if in_ol else "")
        in_ul, in_ol = False, False
        return s
    while i < len(lines):
        s = lines[i].strip()
        if s == "---":
            out.append(close() + "<hr>")
            i += 1
            continue
        if not s.strip(" -"):
            out.append(close())
            i += 1
            continue
        if "|" in s and i + 1 < len(lines) and "---" in lines[i + 1]:
            head = [inline(c.strip()) for c in s.strip().strip("|").split("|")]
            out.append(close() + "<table><tr>" + "".join(f"<th>{c}</th>" for c in head) + "</tr>")
            i += 2
            while i < len(lines) and "|" in lines[i] and lines[i].strip():
                cells = [inline(c.strip()) for c in lines[i].strip().strip("|").split("|")]
                out.append("<tr>" + "".join(f"<td>{c}</td>" for c in cells) + "</tr>")
                i += 1
            out.append("</table>")
            continue
        if s.startswith("## "):
            out.append(close() + f"<h2>{inline(s[3:])}</h2>")
        elif s.startswith("# "):
            out.append(close() + f"<h1>{inline(s[2:])}</h1>")
        elif m := re.match(r"[*\-]\s+(.*)", s):
            pre = ("</ol>" if in_ol else "") + ("<ul>" if not in_ul else "")
            out.append(pre + f"<li>{inline(m.group(1))}</li>")
            in_ul, in_ol = True, False
        elif m := re.match(r"\d+\.\s+(.*)", s):
            pre = ("</ul>" if in_ul else "") + ("<ol>" if not in_ol else "")
            out.append(pre + f"<li>{inline(m.group(1))}</li>")
            in_ul, in_ol = False, True
        else:
            out.append(close() + (f"<p>{inline(s)}</p>" if s.strip(" -") else ""))
        i += 1
    return "".join(out) + close()


def papers():
    """Load paper metas sorted by score desc (reuses dashboard._meta)."""
    return sorted((_meta(p) for p in PAPERS.glob("*.md") if p.is_file()), key=lambda d: d["score"], reverse=True)


def find_note(slug):
    """Find a paper/idea note by stem or title substring, case-insensitive."""
    q, notes = slug.lower(), sorted(list(PAPERS.glob("*.md")) + list(IDEAS.glob("*.md")))
    for p in notes:  # ponytail: exact stem first, substring fallback for short slugs
        if q in (p.stem.lower(), p.stem.lower().replace("paper - ", "")):
            return p
    return next((p for p in notes if q in p.stem.lower()), None)


def counts(scope, kind):
    """Count entries in one state/<scope>-<kind>.json, '?' when missing."""
    try:
        return len(json.loads((ROOT / "state" / f"{scope}-{kind}.json").read_text()))
    except Exception:
        return "?"


def tbl(rows):
    """Render rows as a plain HTML table."""
    return "<table>" + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</table>"


def overview():
    """Render / overview: counts, state, hubs, warnings, cron tail."""
    ps, hubs = papers(), {}
    for d in ps:
        for h in dict.fromkeys(x.strip() for x in d["hubs"] if x.strip()):
            hubs[h] = hubs.get(h, 0) + 1
    warns = [f'no hubs: {d["title"]}' for d in ps if not d["hubs"]] + [f'low score ({d["score"]}): {d["title"]}' for d in ps if d["score"] < 4]
    try:
        tail = "\n".join((ROOT / "cron.log").read_text(errors="ignore").splitlines()[-20:])
    except Exception:
        tail = "no cron.log yet"
    scopes = sorted(q.stem for q in SCOPES.glob("*.yaml"))
    return page("overview", f"<p>{len(ps)} papers, {len(list(CONCEPTS.glob('*.md')))} concepts, {len(list(IDEAS.glob('*.md')))} ideas</p>"
        + "<h2>per-scope state</h2>" + tbl([(s, counts(s, "seen"), counts(s, "ranked")) for s in scopes])
        + "<h2>concept hubs</h2>" + tbl(sorted(hubs.items()))
        + "<h2>warnings</h2>" + tbl([(w,) for w in warns] or [("(none)",)])
        + f"<h2>cron.log tail</h2><pre>{html.escape(tail)}</pre>")


def paper_table(sort):
    """Render /papers table sorted by score/title/year with links to /paper."""
    key = {"title": lambda d: d["title"], "year": lambda d: d["year"]}.get(sort, lambda d: -d["score"])
    rows = "".join(f'<tr><td><a href="/paper?slug={quote(d["title"])}">{html.escape(d["title"])}</a></td><td>{d["year"]}</td><td>{d["score"]}</td></tr>' for d in sorted(papers(), key=key))
    return page("papers", '<p>sort: <a href="/papers?sort=score">score</a> <a href="/papers?sort=title">title</a> <a href="/papers?sort=year">year</a></p><table><tr><th>title</th><th>year</th><th>score</th></tr>' + rows + "</table>")


def note(path, slug):
    """Render one note via md(), or 404 when the slug is unknown."""
    return (200, page(path.stem, md(path.read_text(errors="ignore")))) if path and path.is_file() else (404, page("not found", f"<p>no note for slug {html.escape(slug)}</p>"))


class H(BaseHTTPRequestHandler):
    """Route GET to overview/papers/paper/ideas, localhost-only by bind addr."""

    def do_GET(self):
        """Parse path and dispatch to the matching view."""
        u, q = urlparse(self.path), parse_qs(urlparse(self.path).query)
        code, body = 200, ""
        if u.path == "/":
            body = overview()
        elif u.path == "/papers":
            body = paper_table(q.get("sort", ["score"])[0])
        elif u.path == "/paper":
            code, body = note(find_note(q.get("slug", [""])[0]), q.get("slug", [""])[0])
        elif u.path == "/ideas" and q.get("file"):
            code, body = note(ROOT / "vault" / "ideas" / q["file"][0], q["file"][0])
        elif u.path == "/ideas":
            body = page("ideas", "<ul>" + "".join(f'<li><a href="/ideas?file={quote(p.name)}">{html.escape(p.name)}</a></li>' for p in sorted(IDEAS.glob("*.md"))) + "</ul>")
        else:
            code, body = 404, page("not found", "<p>unknown route</p>")
        raw = body.encode()
        self.send_response(code)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def log_message(self, *a):
        """Silence default request logging (dash.log stays clean)."""


if __name__ == "__main__":
    with ThreadingHTTPServer(("127.0.0.1", 8080), H) as srv:  # ponytail: localhost bind is the auth, no campus exposure
        print("serving http://127.0.0.1:8080")
        srv.serve_forever()
