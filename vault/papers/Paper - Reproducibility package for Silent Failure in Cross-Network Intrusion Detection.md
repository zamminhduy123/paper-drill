---
title: "Reproducibility package for: Silent Failure in Cross-Network Intrusion Detection — Label-Efficient Canary Monitoring under Rare Attacks"
year: 2026
doi: "https://doi.org/10.5281/zenodo.21927881"
relevance_score: 0.85
type: paper
---
# Reproducibility package for: Silent Failure in Cross-Network Intrusion Detection — Label-Efficient Canary Monitoring under Rare Attacks

## Novelty
Reproducibility package for silent failure in cross-network intrusion detection, focusing on label-efficient canary monitoring under rare attacks, with a pre-registered replication on a second target network and seed-paired bootstrap analysis with invariant selftests.

## Methodology
Full experimental pipeline with per-draw logs across fourteen deployment conditions and four label budgets, label-free signal evaluation, two controlled prevalence sweeps on distinct target networks, an adapted active-testing baseline, fixed seeds, self-test invariant checks, pre-registration, 2,400 per-draw records for the NF-ToN-IoT-v2 sweep, and a seed-paired bootstrap analysis script with 13 invariant selftests.

## Explicit Limitations
Benchmark datasets are not redistributed. The replication returned the registered outcome (C), and the corresponding claim in the manuscript was lowered accordingly.

## Future Work
not stated

## Concept Hubs
[[Concept - Deep Learning Intrusion Detection]] [[Concept - Cross-Dataset Evaluation]] [[Concept - Class Imbalance]] [[Concept - Network Traffic Analysis]]

## Relevance Score
0.85

## Monitoring Transfer
doi:
not stated
source_link:
not stated
text_kind:
reproducibility package
monitoring_problem:
silent failure in deployed cross-network intrusion detection under rare attacks
signal:
small labeled sample of target traffic
uncertainty_method:
seed-paired bootstrap analysis
action:
lower the corresponding claim in the manuscript
eval_setting:
fourteen deployment conditions, four label budgets, two controlled prevalence sweeps on distinct target networks, NF-ToN-IoT-v2 sweep
limitation_author:
benchmark datasets are not redistributed
limitation_inference:
replication returned registered outcome C and the claim was lowered
limitation_unknown:
not stated
support_passage:
diagnose whether a deployed network intrusion detector still works, using a small labeled sample of target traffic
transfer_ivn:
use label-efficient canary monitoring with bootstrap uncertainty to detect silent failure of in-vehicle network intrusion detectors
transfer_risk:
IVN traffic, attack rarity, and domain shift may differ enough that target-traffic labels and prevalence sweeps do not transfer

#needs-review

## Record Fields
doi: https://doi.org/10.5281/zenodo.21927881
source_link: not stated
text_kind: abstract
monitoring_problem: silent failure in deployed cross-network intrusion detection under rare attacks
signal: small labeled sample of target traffic
uncertainty_method: seed-paired bootstrap analysis
action: lower the corresponding claim in the manuscript
eval_setting: fourteen deployment conditions, four label budgets, two controlled prevalence sweeps on distinct target networks, NF-ToN-IoT-v2 sweep
limitation_author: benchmark datasets are not redistributed
limitation_inference: replication returned registered outcome C and the claim was lowered
limitation_unknown: not stated
support_passage: diagnose whether a deployed network intrusion detector still works, using a small labeled sample of target traffic
transfer_ivn: use label-efficient canary monitoring with bootstrap uncertainty to detect silent failure of in-vehicle network intrusion detectors
transfer_risk: IVN traffic, attack rarity, and domain shift may differ enough that target-traffic labels and prevalence sweeps do not transfer
