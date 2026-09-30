---
title: "DriveShield: attention-based hybrid neural network for intrusion detection in automotive controller area networks"
year: 2026
doi: "https://doi.org/10.11591/ijai.v15.i3.pp2618-2632"
relevance_score: 8.064
type: paper
---
# DriveShield: attention-based hybrid neural network for intrusion detection in automotive controller area networks

Novelty

First IDS to combine GRU, CNN, and LSTM with an attention mechanism for in-vehicle network intrusion detection; validated across two public datasets (OTIDS, HCRL) with strong generalization.

Methodology

Systematic pre-processing pipeline: feature engineering, SMOTE for class balancing, and normalization. Hybrid neural architecture of GRU + CNN + LSTM augmented with an attention mechanism. Validated on OTIDS and HCRL car hacking datasets.

Explicit Limitations

Future work needed on lower-frequency attacks (via unsupervised learning) and real-world deployment trials; no other explicit limitations stated by authors.

Future Work

Study performance on lower-frequency attacks through unsupervised learning methods; conduct real-world deployment trials.

Concept Hubs

[[Concept - CAN Intrusion Detection]]
[[Concept - Deep Learning Intrusion Detection]]
[[Concept - SMOTE Oversampling]]
[[Concept - In-Vehicle Network Security]]
[[Concept - Real-Time Attack Defense]]

Relevance Score

Not stated

Monitoring Transfer

Monitoring problem, signal, uncertainty method, resulting action, evaluation setting.

Transfer

One transfer to IVN and one reason the transfer may fail.

doi: not stated
source_link: not stated
text_kind: research abstract
monitoring_problem: cyberattacks on automotive controller area networks due to increasing connected technology
signal: CAN bus traffic features (engineered from OTIDS and HCRL datasets)
uncertainty_method: attention mechanism weighting of significant features; SMOTE for class imbalance
action: real-time intrusion detection and attack classification
eval_setting: OTIDS and HCRL car hacking datasets; accuracy and F1-score metrics
limitation_author: lower-frequency attacks not addressed; real-world deployment trials not yet conducted
limitation_inference: reliance on two public datasets may not capture full diversity of real vehicle network traffic and attack variants
limitation_unknown: computational overhead and latency of GRU-CNN-LSTM-attention model on resource-constrained automotive ECUs
support_passage: This paper presents DriveShield, a novel real-time intrusion detection system (IDS) that is the first to combine gated recurrent units (GRU), convolutional neural networks (CNN), and long short-term memory (LSTM) with an attention mechanism.
transfer_ivn: attention-based hybrid sequence modeling transfers to CAN traffic by weighting salient temporal features for attack discrimination
transfer_risk: attention weights may overfit dataset-specific attack signatures, reducing detection of lower-frequency or novel attacks in real vehicles

First IDS to combine GRU, CNN, and LSTM with an attention mechanism for in-vehicle network intrusion detection; validated across two public datasets (OTIDS, HCRL) with strong generalization.

Systematic pre-processing pipeline: feature engineering, SMOTE for class balancing, and normalization. Hybrid neural architecture of GRU + CNN + LSTM augmented with an attention mechanism. Validated on OTIDS and HCRL car hacking datasets.

Future work needed on lower-frequency attacks (via unsupervised learning) and real-world deployment trials; no other explicit limitations stated by authors.

Study performance on lower-frequency attacks through unsupervised learning methods; conduct real-world deployment trials.

[[Concept - CAN Intrusion Detection]]
[[Concept - Deep Learning Intrusion Detection]]
[[Concept - SMOTE Oversampling]]
[[Concept - In-Vehicle Network Security]]
[[Concept - Real-Time Attack Defense]]

Not stated

Monitoring problem, signal, uncertainty method, resulting action, evaluation setting.

One transfer to IVN and one reason the transfer may fail.

doi: not stated
source_link: not stated
text_kind: research abstract
monitoring_problem: cyberattacks on automotive controller area networks due to increasing connected technology
signal: CAN bus traffic features (engineered from OTIDS and HCRL datasets)
uncertainty_method: attention mechanism weighting of significant features; SMOTE for class imbalance
action: real-time intrusion detection and attack classification
eval_setting: OTIDS and HCRL car hacking datasets; accuracy and F1-score metrics
limitation_author: lower-frequency attacks not addressed; real-world deployment trials not yet conducted
limitation_inference: reliance on two public datasets may not capture full diversity of real vehicle network traffic and attack variants
limitation_unknown: computational overhead and latency of GRU-CNN-LSTM-attention model on resource-constrained automotive ECUs
support_passage: This paper presents DriveShield, a novel real-time intrusion detection system (IDS) that is the first to combine gated recurrent units (GRU), convolutional neural networks (CNN), and long short-term memory (LSTM) with an attention mechanism.
transfer_ivn: attention-based hybrid sequence modeling transfers to CAN traffic by weighting salient temporal features for attack discrimination
transfer_risk: attention weights may overfit dataset-specific attack signatures, reducing detection of lower-frequency or novel attacks in real vehicles

#needs-review

## Record Fields
doi: https://doi.org/10.11591/ijai.v15.i3.pp2618-2632
source_link: not stated
text_kind: abstract
monitoring_problem: cyberattacks on automotive controller area networks due to increasing connected technology
signal: CAN bus traffic features (engineered from OTIDS and HCRL datasets)
uncertainty_method: attention mechanism weighting of significant features; SMOTE for class imbalance
action: real-time intrusion detection and attack classification
eval_setting: OTIDS and HCRL car hacking datasets; accuracy and F1-score metrics
limitation_author: lower-frequency attacks not addressed; real-world deployment trials not yet conducted
limitation_inference: reliance on two public datasets may not capture full diversity of real vehicle network traffic and attack variants
limitation_unknown: computational overhead and latency of GRU-CNN-LSTM-attention model on resource-constrained automotive ECUs
support_passage: This paper presents DriveShield, a novel real-time intrusion detection system (IDS) that is the first to combine gated recurrent units (GRU), convolutional neural networks (CNN), and long short-term memory (LSTM) with an attention mechanism.
transfer_ivn: attention-based hybrid sequence modeling transfers to CAN traffic by weighting salient temporal features for attack discrimination
transfer_risk: attention weights may overfit dataset-specific attack signatures, reducing detection of lower-frequency or novel attacks in real vehicles
