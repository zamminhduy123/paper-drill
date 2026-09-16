"""Rank: zembed-1 cosine thesis<->title, sorted top-N."""
import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CFG = ROOT / "config" / "scope.yaml"
IN = ROOT / "state" / "latest.json"
OUT = ROOT / "state" / "ranked.json"

# ponytail: 4 pos + 3 neg from notebooks/02-shootout.ipynb, enough to judge separation
POS = ["Knowledge distillation GNN Transformer to tiny ECU student <10K params for CAN IDS",
       "Small language models MiniLM DistilBERT convert CAN traffic to tokens for intrusion detection",
       "Open-set few-shot cross-dataset CAN IDS Car-Hacking to CIC-IoV-2024",
       "Vision Transformer on CAN image recurrence plots for intrusion detection"]
NEG = ["HairCLIP text image hair editing StyleGAN",
       "AlphaFold protein 3D structure prediction",
       "LLM summarization of legal contracts"]
CHECK_THESIS = "deep learning for in-vehicle CAN intrusion detection"


def load_cfg():
    """Load scope.yaml (model, thresholds, keep)."""
    return yaml.safe_load(CFG.read_text())


def load_model(name=None):
    """Load zembed model on CPU (never touch driver)."""
    from sentence_transformers import SentenceTransformer
    name = name or load_cfg()["models"]["embed_model"]
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
    m = load_model()
    g = gap(score(CHECK_THESIS, POS, m), score(CHECK_THESIS, NEG, m))
    assert g > 0.05, f"separation collapsed: gap={g:.3f}"
    print(f"self-check gap={g:.3f} ok")
    cfg = load_cfg()
    thesis = cfg["seeds"]["thesis_statements"][0]
    items = json.loads(IN.read_text())
    ranked = rank(items, thesis, m, threshold=cfg["thresholds"]["semantic_edge"], keep=cfg["limits"]["keep"])
    OUT.write_text(json.dumps(ranked, indent=2))
    for r in ranked[:5]:
        print(f"{r['score']:.3f} | {r.get('title')}")
