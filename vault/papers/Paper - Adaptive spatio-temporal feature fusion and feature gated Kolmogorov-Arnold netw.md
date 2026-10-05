---
title: "Adaptive spatio-temporal feature fusion and feature gated Kolmogorov-Arnold networks for intrusion detection"
year: 2026
doi: "https://doi.org/10.1016/j.asoc.2026.116046"
relevance_score: 0.95
type: paper
---
# Adaptive spatio-temporal feature fusion and feature gated Kolmogorov-Arnold networks for intrusion detection

## Novelty
Proposes adaptive spatio-temporal feature fusion with fusion-level gating, feature interaction, and adaptive fusion weighting, combined with a feature-gated Kolmogorov-Arnold network classifier for intrusion detection.

## Methodology
The method uses an ASTFF module to adaptively fuse spatio-temporal traffic features and an FG-KAN module with decision-level gating and KAN-based nonlinear classification. It is evaluated on CICIDS2017, CSE-CICIDS2018, and CICIoV2024 using accuracy and F1 score.

## Explicit Limitations
Not stated in the provided abstract.

## Future Work
Not stated.

## Concept Hubs
[[Concept - Kolmogorov-Arnold Networks]], [[Concept - Deep Learning Intrusion Detection]], [[Concept - Network Traffic Analysis]], [[Concept - Cross-Dataset Evaluation]], [[Concept - In-Vehicle Network Security]]

## Relevance Score
0.95

## Monitoring Transfer
doi: not stated
source_link: not stated
text_kind: research paper abstract
monitoring_problem: detecting network intrusions in enterprise, internet, and IoV traffic
signal: spatio-temporal network traffic features fused by ASTFF
uncertainty_method: not stated
action: classify traffic as benign or attack
eval_setting: CICIDS2017, CSE-CICIDS2018, CICIoV2024; accuracy and F1 score
limitation_author: not stated
limitation_inference: generalization to unseen domains and real-time constrained deployment is not fully validated
limitation_unknown: not stated
support_passage: experiments were conducted on CICIDS2017, CSE-CICIDS2018, and CICIoV2024, achieving accuracy rates of 99.86%, 99.97%, and 99.65% and F1 scores of 94.57%, 99.97%, and 97.43%
transfer_ivn: apply ASTFF and FG-KAN to in-vehicle network traffic monitoring for intrusion detection
transfer_risk: IoV and enterprise traffic patterns may differ from in-vehicle network dynamics, reducing transfer performance without domain adaptation

#needs-review

## Record Fields
doi: https://doi.org/10.1016/j.asoc.2026.116046
source_link: not stated
text_kind: abstract
monitoring_problem: detecting network intrusions in enterprise, internet, and IoV traffic
signal: spatio-temporal network traffic features fused by ASTFF
uncertainty_method: not stated
action: classify traffic as benign or attack
eval_setting: CICIDS2017, CSE-CICIDS2018, CICIoV2024; accuracy and F1 score
limitation_author: not stated
limitation_inference: generalization to unseen domains and real-time constrained deployment is not fully validated
limitation_unknown: not stated
support_passage: experiments were conducted on CICIDS2017, CSE-CICIDS2018, and CICIoV2024, achieving accuracy rates of 99.86%, 99.97%, and 99.65% and F1 scores of 94.57%, 99.97%, and 97.43%
transfer_ivn: apply ASTFF and FG-KAN to in-vehicle network traffic monitoring for intrusion detection
transfer_risk: IoV and enterprise traffic patterns may differ from in-vehicle network dynamics, reducing transfer performance without domain adaptation
