---
title: "A rule-based label harmonization framework for cross-dataset IoT intrusion detection"
year: 2026
doi: "https://doi.org/10.1016/j.iot.2026.102030"
relevance_score: 9.0
type: paper
---
# A rule-based label harmonization framework for cross-dataset IoT intrusion detection

## Novelty
Rule-based label harmonization framework for cross-dataset IoT intrusion detection using Zeek standardized flow features and MITRE ATT&CK/CAPEC behavioral semantics, replacing manual relabeling and enabling unified dataset training.

## Methodology
Systematic cross-dataset evaluation of intrusion detection models on CIC-IoT-2023, IoT-23, and IoTID20; comparison of same-dataset, cross-dataset, and unified training settings; rule-based behavioral labeling from Zeek flow features and MITRE ATT&CK/CAPEC semantics; proof-of-concept evaluation in three smart-home environments.

## Explicit Limitations
- Cross-dataset testing caused sharp performance degradation, with average F1 below 0.50 except for Multi-Layer Perceptron.
- Unified-dataset results depend on consistent labeling for reliable cross-dataset evaluation.

## Future Work
not stated

## Concept Hubs
[[Concept - Cross-Dataset Evaluation]]
[[Concept - IoT Intrusion Detection]]
[[Concept - Deep Learning Intrusion Detection]]
[[Concept - Network Traffic Analysis]]
[[Concept - Dataset Bias]]

## Relevance Score
9/10

## Monitoring Transfer
doi: not stated
source_link: not stated
text_kind: abstract
monitoring_problem: IoT IDS cross-dataset generalization under heterogeneous labels and domain shift
signal: Zeek standardized flow features
uncertainty_method: not stated
action: rule-based label harmonization and unified dataset training
eval_setting: same-dataset, cross-dataset, and unified training evaluation on CIC-IoT-2023, IoT-23, IoTID20, plus smart-home proof of concept
limitation_author: consistent labeling remains essential for reliable cross-dataset evaluation
limitation_inference: cross-dataset F1 collapse indicates label and domain heterogeneity, not only model weakness
limitation_unknown: not stated
support_passage: performance degraded sharply when models trained on one dataset were tested on a different one (average F1 below 0.50 except for Multi-Layer Perceptron
transfer_ivn: Harmonize IVN intrusion datasets using standardized vehicle-network features and MITRE ATT&CK/CAPEC behavioral labels
transfer_risk: IVN protocol semantics and timing differ from IoT traffic, so Zeek flow features and IoT labels may not map cleanly

#needs-review

## Record Fields
doi: https://doi.org/10.1016/j.iot.2026.102030
source_link: not stated
text_kind: abstract
monitoring_problem: IoT IDS cross-dataset generalization under heterogeneous labels and domain shift
signal: Zeek standardized flow features
uncertainty_method: not stated
action: rule-based label harmonization and unified dataset training
eval_setting: same-dataset, cross-dataset, and unified training evaluation on CIC-IoT-2023, IoT-23, IoTID20, plus smart-home proof of concept
limitation_author: consistent labeling remains essential for reliable cross-dataset evaluation
limitation_inference: cross-dataset F1 collapse indicates label and domain heterogeneity, not only model weakness
limitation_unknown: not stated
support_passage: performance degraded sharply when models trained on one dataset were tested on a different one (average F1 below 0.50 except for Multi-Layer Perceptron
transfer_ivn: Harmonize IVN intrusion datasets using standardized vehicle-network features and MITRE ATT&CK/CAPEC behavioral labels
transfer_risk: IVN protocol semantics and timing differ from IoT traffic, so Zeek flow features and IoT labels may not map cleanly
