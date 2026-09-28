"""Record: parse extract Markdown into stable evidence dict (stdlib only)."""
import re

FIELDS = ["doi", "source_link", "text_kind", "monitoring_problem", "signal",
          "uncertainty_method", "action", "eval_setting", "limitation_author",
          "limitation_inference", "limitation_unknown", "support_passage",
          "transfer_ivn", "transfer_risk"]

EMPTY = {"", "not stated", "not stated in abstract", "none", "n/a", "unknown", "-"}


def _is_empty(v) -> bool:
    """Check if a record value counts as missing."""
    return str(v or "").strip().lower() in EMPTY


def _find(body: str, field: str) -> str:
    """Extract one `field: value` line, return 'not stated' when absent."""
    pat = field.replace("_", r"[\s_\-]*")
    m = re.search(rf"(?im)^\s*{pat}\s*:\s*(.+?)\s*$", body or "")
    return m.group(1).strip() if m and m.group(1).strip() else "not stated"


def parse(body: str) -> dict:
    """Parse extract Markdown into {field: value} dict, never inventing values."""
    return {f: _find(body, f) for f in FIELDS}


def validate(rec: dict) -> list:
    """List missing fields; flag needs-review when limitations+passage all empty."""
    missing = [f for f in FIELDS if _is_empty((rec or {}).get(f))]
    lims_empty = all(_is_empty((rec or {}).get(f)) for f in ("limitation_author", "limitation_inference", "limitation_unknown"))
    if lims_empty and _is_empty((rec or {}).get("support_passage")) and "needs-review" not in missing:
        missing.append("needs-review")
    return missing
