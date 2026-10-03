---
title: "AutoHack-Benchmark: A Physically Verified Multi-Bus CAN Dataset for Intrusion Detection System Evaluation"
year: 2026
doi: "https://doi.org/10.5281/zenodo.19676891"
relevance_score: 0.55
type: paper
---
# AutoHack-Benchmark: A Physically Verified Multi-Bus CAN Dataset for Intrusion Detection System Evaluation

## Novelty
A physically verified multi-bus CAN benchmark artifact for IDS evaluation, with preprocessing, feature extraction, and reproducible single-bus/multi-bus experiments using tree-based baselines.

## Methodology
Preprocessing pipeline, feature extraction scripts, and experimental code evaluate IDSs in single-bus and multi-bus settings using Random Forest and XGBoost baselines.

## Explicit Limitations
not stated

## Future Work
not stated

## Concept Hubs
[[Concept - CAN Intrusion Detection]] [[Concept - Benchmark Stress Testing]] [[Concept - In-Vehicle Network Security]] [[Concept - Feature Selection]]

## Relevance Score
0.55

## Monitoring Transfer
doi: not stated
source_link: not stated
text_kind: benchmark code
monitoring_problem: Detect intrusions in automotive CAN bus traffic
signal: CAN message features from single-bus and multi-bus traffic
uncertainty_method: not stated
action: classify traffic as normal or intrusive for IDS evaluation
eval_setting: single-bus and multi-bus analysis on AutoHack dataset
limitation_author: not stated
limitation_inference: benchmark emphasizes tree-based baselines rather than deep learning IDSs
limitation_unknown: not stated
support_passage: This benchmark code is designed to support the evaluation of automotive CAN Intrusion Detection Systems (IDSs) using the AutoHack dataset. It provides the preprocessing pipeline, feature extraction scripts, and experimental code used to reproduce the benchmark results reported in the paper. The code supports multiple evaluation settings, including single-bus and multi-bus analysis, and includes implementations based on tree-based baseline models such as Random Forest and XGBoost.
transfer_ivn: Use the AutoHack multi-bus preprocessing and evaluation pipeline to benchmark deep learning IDSs on in-vehicle CAN traffic
transfer_risk: The benchmark is centered on tree-based baselines and physically verified CAN data, so results may not transfer to deep learning models requiring different feature representations or unknown attacks

#needs-review

## Record Fields
doi: https://doi.org/10.5281/zenodo.19676891
source_link: not stated
text_kind: abstract
monitoring_problem: Detect intrusions in automotive CAN bus traffic
signal: CAN message features from single-bus and multi-bus traffic
uncertainty_method: not stated
action: classify traffic as normal or intrusive for IDS evaluation
eval_setting: single-bus and multi-bus analysis on AutoHack dataset
limitation_author: not stated
limitation_inference: benchmark emphasizes tree-based baselines rather than deep learning IDSs
limitation_unknown: not stated
support_passage: This benchmark code is designed to support the evaluation of automotive CAN Intrusion Detection Systems (IDSs) using the AutoHack dataset. It provides the preprocessing pipeline, feature extraction scripts, and experimental code used to reproduce the benchmark results reported in the paper. The code supports multiple evaluation settings, including single-bus and multi-bus analysis, and includes implementations based on tree-based baseline models such as Random Forest and XGBoost.
transfer_ivn: Use the AutoHack multi-bus preprocessing and evaluation pipeline to benchmark deep learning IDSs on in-vehicle CAN traffic
transfer_risk: The benchmark is centered on tree-based baselines and physically verified CAN data, so results may not transfer to deep learning models requiring different feature representations or unknown attacks
