"""Fulltext: campus-session PDF fetch + pypdf text, cached (requests + stdlib)."""
import re
from io import BytesIO
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "state" / "pdfs"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"


def _session():
    """Return Session with browser UA for publisher cookie flow."""
    s = requests.Session()
    s.headers.update({"User-Agent": UA})
    return s


def _is_pdf(resp):
    """Return True when response looks like a PDF payload."""
    ct = (resp.headers.get("Content-Type") or "").lower()
    return resp.status_code == 200 and "pdf" in ct and (resp.content or b"")[:5] == b"%PDF-"


def fetch_ieee(doc_id_or_doi):
    """Fetch IEEE PDF via page-cookies then stampPDF, return bytes or None."""
    token = str(doc_id_or_doi or "").strip()
    if not token:
        return None
    try:
        s = _session()
        if re.fullmatch(r"\d+", token):
            arn, referer = token, f"https://ieeexplore.ieee.org/document/{token}/"
            s.get(referer, timeout=30)
        else:
            doi = re.sub(r"^(https?://(dx\.)?doi\.org/|doi:)", "", token).strip()
            page = s.get(f"https://doi.org/{doi}", timeout=30)
            m = re.search(r"/document/(\d+)", page.url or "")
            if not m:
                return None
            arn, referer = m.group(1), page.url
        r = s.get(f"https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber={arn}&ref=",
                  headers={"Referer": referer}, timeout=60)
        return r.content if _is_pdf(r) else None
    except Exception:
        return None


def fetch_elsevier(doi):
    """Attempt Elsevier pdfft via article-page session, return bytes or None."""
    token = str(doi or "").strip()
    if not token:
        return None
    try:
        s = _session()
        doi = re.sub(r"^(https?://(dx\.)?doi\.org/|doi:)", "", token).strip()
        page = s.get(f"https://doi.org/{doi}", timeout=30)
        url = page.url or ""
        if "sciencedirect" not in url:
            return None
        r = s.get(url.rstrip("/") + "/pdfft?isDTMRedir=true&download=true",
                  headers={"Referer": url}, timeout=60)
        return r.content if _is_pdf(r) else None
    except Exception:
        return None


def pdf_text(pdf_bytes, max_chars=12000):
    """Extract text from PDF bytes, truncated to max_chars."""
    try:
        from pypdf import PdfReader
        reader = PdfReader(BytesIO(pdf_bytes or b""))
        text = "\n".join((p.extract_text() or "") for p in reader.pages).strip()
    except Exception:
        return ""
    if len(text) > max_chars:
        return text[:max_chars] + "\n[truncated]"
    return text


def get_text(item):
    """Return cached fulltext or fetch once, else empty string."""
    from .writer import slugify
    item = item or {}
    slug = slugify(item.get("title") or "untitled")
    dest = CACHE / f"{slug}.txt"
    try:
        if dest.exists():
            return dest.read_text()
    except Exception:
        pass
    doi = str(item.get("doi") or "").strip()
    pdf = None
    try:
        if "10.1109" in doi:
            pdf = fetch_ieee(doi)
        elif "10.1016" in doi:
            pdf = fetch_elsevier(doi)
        elif doi:
            pdf = fetch_ieee(doi) or fetch_elsevier(doi)
    except Exception:
        pdf = None
    if not pdf:
        return ""
    text = pdf_text(pdf)
    if not text:
        return ""
    try:
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(text)
    except Exception:
        pass
    return text
