---
title: "Evaluating False Alarm and Missing Attacks in CAN IDS"
year: 2026
doi: "https://doi.org/10.48550/arxiv.2602.02781"
relevance_score: 0.95
type: paper
---
# Evaluating False Alarm and Missing Attacks in CAN IDS

## Novelty
Systematic adversarial evaluation of CAN IDS using protocol-compliant payload-level FGSM BIM and PGD perturbations on the ROAD dataset, comparing shallow and DNN detectors for false alarms and missed attacks.

## Methodology
Train and test four shallow learning models and a DNN on the ROAD dataset, apply FGSM BIM and PGD payload perturbations to benign and malicious CAN frames, and measure false alarm and missed attack rates.

## Explicit Limitations
not stated

## Future Work
adversarial robustness evaluation in safety-critical automotive IDS

## Concept Hubs
[[Concept - CAN Intrusion Detection]]
[[Concept - Deep Learning Intrusion Detection]]
[[Concept - In-Vehicle Network Security]]
[[Concept - Benchmark Stress Testing]]

## Relevance Score
0.95

## Monitoring Transfer
doi: not stated
source_link: not stated
text_kind: abstract
monitoring_problem: detect malicious CAN frames and avoid false alarms under adversarial perturbations
signal: CAN frame payload features
uncertainty_method: not stated
action: flag malicious CAN frame
eval_setting: ROAD dataset with benign and malicious CAN frames under FGSM BIM and PGD payload-level perturbations
limitation_author: not stated
limitation_inference: single ROAD dataset and payload-level perturbations only
limitation_unknown: not stated
support_passage: Using protocol-compliant, payload-level perturbations generated via FGSM, BIM and PGD, we evaluate adversarial effects on both benign and malicious CAN frames.
transfer_ivn: use adversarial payload-level stress testing to evaluate IVN IDS false alarms and missed attacks
transfer_risk: real IVN traffic and ECU timing may differ from the ROAD dataset and payload-only attacks

#needs-review

## Record Fields
doi: https://doi.org/10.48550/arxiv.2602.02781
source_link: not stated
text_kind: abstract
monitoring_problem: detect malicious CAN frames and avoid false alarms under adversarial perturbations
signal: CAN frame payload features
uncertainty_method: not stated
action: flag malicious CAN frame
eval_setting: ROAD dataset with benign and malicious CAN frames under FGSM BIM and PGD payload-level perturbations
limitation_author: not stated
limitation_inference: single ROAD dataset and payload-level perturbations only
limitation_unknown: not stated
support_passage: Using protocol-compliant, payload-level perturbations generated via FGSM, BIM and PGD, we evaluate adversarial effects on both benign and malicious CAN frames.
transfer_ivn: use adversarial payload-level stress testing to evaluate IVN IDS false alarms and missed attacks
transfer_risk: real IVN traffic and ECU timing may differ from the ROAD dataset and payload-only attacks
