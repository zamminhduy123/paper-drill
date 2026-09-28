"""Rank: zembed-1 cosine thesis<->title, sorted top-N."""
import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SCOPES = ROOT / "config" / "scopes"
LENSES = ROOT / "config" / "lenses"
STATE = ROOT / "state"

# ponytail: 4 pos + 3 neg from notebooks/02-shootout.ipynb, enough to judge separation
POS = ["Knowledge distillation GNN Transformer to tiny ECU student <10K params for CAN IDS",
       "Small language models MiniLM DistilBERT convert CAN traffic to tokens for intrusion detection",
       "Open-set few-shot cross-dataset CAN IDS Car-Hacking to CIC-IoV-2024",
       "Vision Transformer on CAN image recurrence plots for intrusion detection"]
NEG = ["HairCLIP text image hair editing StyleGAN",
       "AlphaFold protein 3D structure prediction",
       "LLM summarization of legal contracts"]
CHECK_THESIS = "deep learning for in-vehicle CAN intrusion detection"

last_stats = {"threshold": 0.0, "above": 0, "below": 0}


def cfg_path(scope="ivn"):
    """Resolve config/scopes/<scope>.yaml path."""
    return SCOPES / f"{scope}.yaml"


def load_cfg(scope="ivn"):
    """Load scope yaml (model, thresholds, keep)."""
    return yaml.safe_load(cfg_path(scope).read_text())


def state_paths(scope="ivn"):
    """Resolve per-scope (latest, ranked) state paths."""
    return (STATE / f"{scope}-latest.json", STATE / f"{scope}-ranked.json")


def load_model(name=None, scope="ivn"):
    """Load zembed model on CPU (never touch driver)."""
    from sentence_transformers import SentenceTransformer
    name = name or load_cfg(scope)["models"]["embed_model"]
    return SentenceTransformer(name, trust_remote_code=True, device="cpu")  # CPU-safe, never touch driver


def score(thesis, texts, model):
    """Cosine thesis vs texts with query:/passage: prefixes."""
    q = model.encode(["query: " + thesis], normalize_embeddings=True)
    p = model.encode(["passage: " + (t or "") for t in texts], normalize_embeddings=True)
    return (p @ q.T).ravel().tolist()


def load_lens(name="monitoring"):
    """Load lens yaml mechanisms with probes and transfer targets."""
    return yaml.safe_load((LENSES / f"{name}.yaml").read_text())


def mechanism_fit(items, mechanisms, model):
    """Max cosine title vs any probe, return per-item (best name, best score)."""
    titles = [(i.get("title") or "") for i in items]
    names = [""] * len(items)
    scores = [0.0] * len(items)
    for mech_name, mech in (mechanisms or {}).items():
        for probe in (mech.get("probes", []) if isinstance(mech, dict) else []):
            for idx, v in enumerate(score(probe, titles, model)):
                if float(v) > scores[idx]:
                    names[idx] = mech_name
                    scores[idx] = round(float(v), 4)
    return list(zip(names, scores))


def gap(pos, neg):
    """Gap = pos_min - neg_max, want >0.05 for clean split."""
    return float(min(pos) - max(neg))  # pos_min - neg_max, want >0.05


def rank_with_stats(items, thesis, model, threshold=0.80, keep=20, lens="monitoring", mechanism_threshold=None):
    """Score thesis + mechanism, admit thesis>=thr OR mech>=mech_thr, sort by max desc."""
    global last_stats
    if not items:
        last_stats = {"threshold": threshold, "above": 0, "below": 0, "mechanism_admits": 0}
        rank.last_stats = last_stats
        return [], dict(last_stats)
    scores = score(thesis, [i.get("title") for i in items], model)
    lens_cfg = {}
    try:
        lens_cfg = load_lens(lens) or {}
        fits = mechanism_fit(items, lens_cfg.get("mechanisms", {}), model)
    except Exception:
        fits = [("", 0.0)] * len(items)  # ponytail: lens optional, thesis gate never breaks
    if mechanism_threshold is None:
        try:
            mechanism_threshold = float((lens_cfg.get("thresholds") or {}).get(
                "mechanism_edge", lens_cfg.get("mechanism_threshold", threshold)))
        except Exception:
            mechanism_threshold = threshold  # ponytail: absent lens key, reuse thesis threshold
    above = sum(1 for s in scores if float(s) >= threshold)
    below = len(items) - above
    out = []
    for i, s, f in zip(items, scores, fits):
        thesis_ok = float(s) >= threshold
        mech_ok = float(f[1]) >= mechanism_threshold
        if thesis_ok or mech_ok:
            out.append({**i, "score": round(float(s), 4), "above_edge": thesis_ok,
                        "mechanism_best": f[0], "mechanism_score": f[1],
                        "selection_reason": "thesis" if thesis_ok else "mechanism"})
    ranked = sorted(out, key=lambda d: max(d["score"], d["mechanism_score"]), reverse=True)[:keep]
    mech_in_top = sum(1 for d in ranked if d["selection_reason"] == "mechanism")
    if mech_in_top < 3:
        seen = {id(d) for d in ranked}
        pool = sorted((d for d in out if id(d) not in seen and d["selection_reason"] == "mechanism"),
                      key=lambda d: d["mechanism_score"], reverse=True)[:3 - mech_in_top]
        for d in pool:
            d["selection_reason"] = "mechanism-quota"
        if pool:
            thesis_idx = sorted((i for i, d in enumerate(ranked) if d["selection_reason"] == "thesis"), reverse=True)[:len(pool)]
            drop = set(thesis_idx)
            ranked = [d for i, d in enumerate(ranked) if i not in drop] + pool
            ranked = sorted(ranked, key=lambda d: max(d["score"], d["mechanism_score"]), reverse=True)[:keep]
    assert len(ranked) <= keep
    last_stats = {"threshold": threshold, "above": above, "below": below,
                  "mechanism_admits": sum(1 for d in ranked if d["selection_reason"] in ("mechanism", "mechanism-quota"))}
    rank.last_stats = last_stats
    return ranked, dict(last_stats)


def rank(items, thesis, model, threshold=0.80, keep=20, lens="monitoring", mechanism_threshold=None):
    """Score items, admit by thesis or mechanism threshold, return top-N sorted desc."""
    ranked, _ = rank_with_stats(items, thesis, model, threshold=threshold, keep=keep, lens=lens,
                                mechanism_threshold=mechanism_threshold)
    return ranked


rank.last_stats = {"threshold": 0.0, "above": 0, "below": 0}


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--scope", default="ivn")
    a = p.parse_args()
    m = load_model(scope=a.scope)
    g = gap(score(CHECK_THESIS, POS, m), score(CHECK_THESIS, NEG, m))
    assert g > 0.05, f"separation collapsed: gap={g:.3f}"
    print(f"self-check gap={g:.3f} ok")
    cfg = load_cfg(a.scope)
    thesis = cfg["seeds"]["thesis_statements"][0]
    in_path, out_path = state_paths(a.scope)
    items = json.loads(in_path.read_text())
    ranked = rank(items, thesis, m, threshold=cfg["thresholds"]["semantic_edge"], keep=cfg["limits"]["keep"])
    out_path.write_text(json.dumps(ranked, indent=2))
    for r in ranked[:5]:
        print(f"{r['score']:.3f} | {r.get('title')}")
