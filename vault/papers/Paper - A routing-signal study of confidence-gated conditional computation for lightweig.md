---
title: "A routing-signal study of confidence-gated conditional computation for lightweight IoT intrusion detection"
year: 2026
doi: "https://doi.org/10.12688/openreseurope.24532.1"
relevance_score: 9.0
type: paper
---
# A routing-signal study of confidence-gated conditional computation for lightweight IoT intrusion detection

## Novelty
Systematic study of which confidence signal should drive escalation in a dual-path lightweight IoT intrusion detection system, comparing MSP, entropy, margin, energy, temperature-scaled confidence, latent norm, learned routing, and ensemble disagreement under matched cost.

## Methodology
A tiny PCA-compressed MLP fast path is gated to a heavier MLP or gradient-boosted-tree model using routing signals. The study evaluates temperature scaling, leakage-free thresholding, tiny-ensemble disagreement, robustness, latency, model size, statistical significance, and cross-dataset transfer on ACI-IoT-2023, TabularIoTAttacks-2024, and CICIoT2023.

## Explicit Limitations
A fixed threshold does not transfer across datasets, with escalation rates swinging from 1% to 55%. On CICIoT2023, routing cannot reach heavy-model performance even at large budgets because the tiny model is confidently wrong on high-volume DoS attacks. Learned routing and ensemble signals do not close the oracle gap.

## Future Work
Identify confident errors within high-confidence classes rather than relying only on better routing signals. Set gates by budget and explore stronger heavy backbones to improve efficiency and close the oracle gap.

## Concept Hubs
[[Concept - IoT Intrusion Detection]] [[Concept - Lightweight Detection]] [[Concept - Edge AI Inference]] [[Concept - Threshold Control]] [[Concept - Cross-Dataset Evaluation]]

## Relevance Score
9/10

## Monitoring Transfer
Monitoring problem: detect IoT network intrusions at edge gateways under tight compute and memory budgets. Signal: MSP, entropy, margin, energy, temperature-scaled confidence, latent norm, learned router, ensemble disagreement. Uncertainty method: confidence-gated conditional computation with MSP and temperature scaling. Resulting action: route most flows to a tiny model and escalate uncertain flows to a heavier model under a fixed budget. Evaluation setting: three IoT intrusion detection benchmarks with matched cost, robustness, latency, model size, statistical significance, and cross-dataset transfer. IVN transfer: apply MSP-gated tiny/heavy routing to in-vehicle network intrusion detection at a gateway or ECU edge, escalating uncertain CAN/DoIP flows to a heavier detector. Failure risk: vehicle traffic is protocol-specific and highly periodic, so confidence thresholds calibrated on IoT datasets may misroute or miss confident errors.

doi:
not stated
source_link:
not stated
text_kind:
abstract
monitoring_problem:
detect IoT network intrusions at edge gateways under tight compute and memory budgets
signal:
MSP, predictive entropy, margin, energy, temperature-scaled confidence, latent norm, learned router, tiny-ensemble disagreement
uncertainty_method:
confidence-gated conditional computation with MSP and temperature-scaled calibration
action:
route most flows to a tiny model and escalate uncertain flows to a heavier model under a fixed budget
eval_setting:
ACI-IoT-2023, TabularIoTAttacks-2024, CICIoT2023 with matched cost, robustness, latency, model size, statistical significance, and cross-dataset transfer
limitation_author:
fixed threshold does not transfer across datasets; oracle gap on CICIoT2023 because tiny model is confidently wrong on high-volume DoS floods; learned router only marginally improves MSP
limitation_inference:
confidence-based routing may fail when errors are high-confidence; budget alone may not close the oracle gap
limitation_unknown:
not stated
support_passage:
A fixed threshold does not transfer across datasets, its escalation rate swinging from 1 % to 55 % .
transfer_ivn:
apply MSP-gated tiny/heavy routing to in-vehicle network intrusion detection at a gateway or ECU edge, escalating uncertain CAN/DoIP flows to a heavier detector
transfer_risk:
vehicle traffic is protocol-specific and highly periodic, so confidence thresholds calibrated on IoT datasets may misroute or miss confident errors

#needs-review

## Record Fields
doi: https://doi.org/10.12688/openreseurope.24532.1
source_link: not stated
text_kind: abstract
monitoring_problem: detect IoT network intrusions at edge gateways under tight compute and memory budgets. Signal: MSP, entropy, margin, energy, temperature-scaled confidence, latent norm, learned router, ensemble disagreement. Uncertainty method: confidence-gated conditional computation with MSP and temperature scaling. Resulting action: route most flows to a tiny model and escalate uncertain flows to a heavier model under a fixed budget. Evaluation setting: three IoT intrusion detection benchmarks with matched cost, robustness, latency, model size, statistical significance, and cross-dataset transfer. IVN transfer: apply MSP-gated tiny/heavy routing to in-vehicle network intrusion detection at a gateway or ECU edge, escalating uncertain CAN/DoIP flows to a heavier detector. Failure risk: vehicle traffic is protocol-specific and highly periodic, so confidence thresholds calibrated on IoT datasets may misroute or miss confident errors.
signal: MSP, predictive entropy, margin, energy, temperature-scaled confidence, latent norm, learned router, tiny-ensemble disagreement
uncertainty_method: confidence-gated conditional computation with MSP and temperature-scaled calibration
action: route most flows to a tiny model and escalate uncertain flows to a heavier model under a fixed budget
eval_setting: ACI-IoT-2023, TabularIoTAttacks-2024, CICIoT2023 with matched cost, robustness, latency, model size, statistical significance, and cross-dataset transfer
limitation_author: fixed threshold does not transfer across datasets; oracle gap on CICIoT2023 because tiny model is confidently wrong on high-volume DoS floods; learned router only marginally improves MSP
limitation_inference: confidence-based routing may fail when errors are high-confidence; budget alone may not close the oracle gap
limitation_unknown: not stated
support_passage: A fixed threshold does not transfer across datasets, its escalation rate swinging from 1 % to 55 % .
transfer_ivn: apply MSP-gated tiny/heavy routing to in-vehicle network intrusion detection at a gateway or ECU edge, escalating uncertain CAN/DoIP flows to a heavier detector
transfer_risk: vehicle traffic is protocol-specific and highly periodic, so confidence thresholds calibrated on IoT datasets may misroute or miss confident errors
