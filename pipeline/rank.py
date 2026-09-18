"""Rank: zembed-1 cosine thesis<->title, sorted top-N."""
import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SCOPES = ROOT / "config" / "scopes"
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


def gap(pos, neg):
    """Gap = pos_min - neg_max, want >0.05 for clean split."""
    return float(min(pos) - max(neg))  # pos_min - neg_max, want >0.05


def rank(items, thesis, model, threshold=0.80, keep=20):
    """Score items, flag above_edge, return top-N sorted desc."""
    scores = score(thesis, [i.get("title") for i in items], model)
    out = [{**i, "score": round(float(s), 4), "above_edge": float(s) >= threshold}
           for i, s in zip(items, scores)]
    return sorted(out, key=lambda d: d["score"], reverse=True)[:keep]


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
