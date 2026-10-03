---
title: "HTPI: A New Head–Tail Population Initialization for Feature Selection Stability in IoT IDSs with Post Hoc Explainable AI Analysis"
year: 2026
doi: "https://doi.org/10.3390/s26165207"
relevance_score: 7.0
type: paper
---
# HTPI: A New Head–Tail Population Initialization for Feature Selection Stability in IoT IDSs with Post Hoc Explainable AI Analysis

## Novelty
The paper introduces Head-Tail Population Initialization (HTPI), a feature-importance-guided initialization strategy for improving cross-run stability of stochastic metaheuristic feature selection in IoT intrusion detection. HTPI is integrated into AHGA-SA as an incremental extension that changes only initialization and reinitialization, and the study adds post hoc explainable AI analysis of selected Head and Tail feature groups.

## Methodology
HTPI splits candidate features into Head and Tail groups using feature-importance scores. Candidate feature subsets are initialized by prioritizing Head features and sampling Tail features with importance-based weights. The method is embedded in Adaptive Hybrid Genetic Algorithm-Simulated Annealing as HTPI-AHGA-SA. Experiments use eight IoT-oriented IDS datasets, 50 runs per configuration, paired seeds across methods, Nogueira stability, Holm correction, 95% leave-one-run-out jackknife confidence intervals, F1 Macro comparisons, and post hoc permutation-importance XAI on three representative datasets.

## Explicit Limitations
The abstract reports that all absolute differences in dataset-level mean F1 Macro remained below 0.003, formal equivalence at that margin was supported for six datasets, dataset-specific security-metric trade-offs remained, and XAI analysis was performed on three representative datasets.

## Future Work
not stated

## Concept Hubs
[[Concept - Feature Selection]]
[[Concept - IoT Intrusion Detection]]
[[Concept - Explainable Intrusion Detection]]
[[Concept - Cross-Dataset Evaluation]]

## Relevance Score
7/10

## Monitoring Transfer
doi:
not stated
source_link:
not stated
text_kind:
abstract
monitoring_problem:
unstable feature-subset selection across repeated runs in IoT intrusion detection
signal:
Nogueira stability of selected feature subsets
uncertainty_method:
95% leave-one-run-out jackknife confidence intervals
action:
initialize and reinitialize candidate feature subsets by prioritizing Head features and importance-weighted Tail sampling
eval_setting:
eight IoT-oriented IDS datasets with 50 runs per configuration and paired seeds
limitation_author:
F1 Macro differences below 0.003, formal equivalence supported for six datasets, dataset-specific security-metric trade-offs remained, XAI limited to three representative datasets
limitation_inference:
stability is characterized under a fixed data partition, so cross-run stability may not imply generalization to new data
limitation_unknown:
not stated
support_passage:
significantly higher Nogueira stability under HTPI-AHGA-SA on all datasets after Holm correction, with non-overlapping 95% leave-one-run-out jackknife confidence intervals in every case
transfer_ivn:
apply HTPI-guided initialization to feature selection for in-vehicle network intrusion detection to stabilize selected IVN traffic features across repeated training runs
transfer_risk:
IVN feature importance may be less stable due to protocol-specific dynamics and class imbalance, weakening Head and Tail prioritization

#needs-review

## Record Fields
doi: https://doi.org/10.3390/s26165207
source_link: not stated
text_kind: abstract
monitoring_problem: unstable feature-subset selection across repeated runs in IoT intrusion detection
signal: Nogueira stability of selected feature subsets
uncertainty_method: 95% leave-one-run-out jackknife confidence intervals
action: initialize and reinitialize candidate feature subsets by prioritizing Head features and importance-weighted Tail sampling
eval_setting: eight IoT-oriented IDS datasets with 50 runs per configuration and paired seeds
limitation_author: F1 Macro differences below 0.003, formal equivalence supported for six datasets, dataset-specific security-metric trade-offs remained, XAI limited to three representative datasets
limitation_inference: stability is characterized under a fixed data partition, so cross-run stability may not imply generalization to new data
limitation_unknown: not stated
support_passage: significantly higher Nogueira stability under HTPI-AHGA-SA on all datasets after Holm correction, with non-overlapping 95% leave-one-run-out jackknife confidence intervals in every case
transfer_ivn: apply HTPI-guided initialization to feature selection for in-vehicle network intrusion detection to stabilize selected IVN traffic features across repeated training runs
transfer_risk: IVN feature importance may be less stable due to protocol-specific dynamics and class imbalance, weakening Head and Tail prioritization
