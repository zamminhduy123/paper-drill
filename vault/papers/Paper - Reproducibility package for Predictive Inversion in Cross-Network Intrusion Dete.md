---
title: "Reproducibility package for: Predictive Inversion in Cross-Network Intrusion Detection"
year: 2026
doi: "https://doi.org/10.5281/zenodo.21699335"
relevance_score: 9.0
type: paper
---
# Reproducibility package for: Predictive Inversion in Cross-Network Intrusion Detection

## Novelty
Identifies predictive score-ordering inversion in cross-network intrusion detection and evaluates small-budget label-acquisition strategies for repairing inverted detectors.

## Methodology
Leakage-free experiment pipeline using NetFlow-v2 benchmark data, six directed source-to-target transfers, four label-acquisition strategies, four label budgets, three classifier families, 18 seeds, and paired Wilcoxon signed-rank significance analysis.

## Explicit Limitations
Not stated. Inferred: evaluation is limited to the tested NetFlow-v2 benchmark pairs, label budgets, classifier families, and seed count.

## Future Work
not stated

## Concept Hubs
[[Concept - Deep Learning Intrusion Detection]] [[Concept - Cross-Dataset Evaluation]] [[Concept - Intrusion Detection]] [[Concept - Network Traffic Analysis]] [[Concept - Data Leakage Prevention]]

## Relevance Score
9/10

## Monitoring Transfer
doi:
not stated
source_link:
not stated
text_kind:
reproducibility package
monitoring_problem:
cross-network intrusion detector score-ordering inversion on a target network
signal:
detector score ordering
uncertainty_method:
not stated
action:
acquire a small number of target labels to repair the detector
eval_setting:
six directed source-target transfers, four label budgets, three classifier families, 18 seeds, NetFlow-v2 benchmark
limitation_author:
not stated
limitation_inference:
limited to the tested NetFlow-v2 benchmark pairs, label budgets, classifier families, and seed count
limitation_unknown:
not stated
support_passage:
A network intrusion detector trained on one network can have its score ordering invert on another network (target AUROC below 0.5), even when the same detector scores near 0.99 in-domain.
transfer_ivn:
apply cross-network score-inversion detection and targeted label acquisition to in-vehicle network intrusion detectors when source-to-target score ordering degrades
transfer_risk:
IVN traffic is more heterogeneous and safety-critical, and limited labeled target data may not repair inverted detectors if source-target domains differ strongly

#needs-review

## Record Fields
doi: https://doi.org/10.5281/zenodo.21699335
source_link: not stated
text_kind: abstract
monitoring_problem: cross-network intrusion detector score-ordering inversion on a target network
signal: detector score ordering
uncertainty_method: not stated
action: acquire a small number of target labels to repair the detector
eval_setting: six directed source-target transfers, four label budgets, three classifier families, 18 seeds, NetFlow-v2 benchmark
limitation_author: not stated
limitation_inference: limited to the tested NetFlow-v2 benchmark pairs, label budgets, classifier families, and seed count
limitation_unknown: not stated
support_passage: A network intrusion detector trained on one network can have its score ordering invert on another network (target AUROC below 0.5), even when the same detector scores near 0.99 in-domain.
transfer_ivn: apply cross-network score-inversion detection and targeted label acquisition to in-vehicle network intrusion detectors when source-to-target score ordering degrades
transfer_risk: IVN traffic is more heterogeneous and safety-critical, and limited labeled target data may not repair inverted detectors if source-target domains differ strongly
