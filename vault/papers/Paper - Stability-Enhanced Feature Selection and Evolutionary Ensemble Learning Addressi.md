---
title: "Stability-Enhanced Feature Selection and Evolutionary Ensemble Learning: Addressing Adversarial Attacks in IoT Intrusion Detection"
year: 2026
doi: "https://doi.org/10.26599/tst.2026.9010058"
relevance_score: 0.85
type: paper
---
# Stability-Enhanced Feature Selection and Evolutionary Ensemble Learning: Addressing Adversarial Attacks in IoT Intrusion Detection

## Novelty
A secure IoT intrusion detection framework that combines stability-enhanced RFECV feature selection across multiple models with CMA-ES-optimized weighted ensemble learning to mitigate adversarial feature injection.

## Methodology
RFECV with cross-validation across multiple models, stability analysis of selected features, weighted ensemble learning, CMA-ES optimization of ensemble weights, and evaluation on UNSW-NB15 and TON-IoT.

## Explicit Limitations
not stated

## Future Work
not stated

## Concept Hubs
[[Concept - Feature Selection]]
[[Concept - IoT Intrusion Detection]]
[[Concept - Deep Learning Intrusion Detection]]
[[Concept - Heterogeneous Base Learners]]
[[Concept - Cross-Dataset Evaluation]]

## Relevance Score
0.85

## Monitoring Transfer
doi:
not stated
source_link:
not stated
text_kind:
abstract
monitoring_problem:
adversarial feature injection corrupting training data and feature selection in IoT intrusion detection
signal:
stable feature subsets across RFECV models and ensemble classification performance
uncertainty_method:
stability analysis of RFECV feature selection
action:
retain stable features and train a CMA-ES-optimized weighted ensemble classifier
eval_setting:
UNSW-NB15 and TON-IoT benchmark datasets
limitation_author:
not stated
limitation_inference:
the abstract does not discuss computational cost, real-time deployment, scalability, or generalization beyond the two evaluated datasets
limitation_unknown:
not stated
support_passage:
we propose a secure framework that applies recursive feature elimination with cross-validation (RFECV) across multiple models, followed by stability analysis to ensure robust feature selection. Additionally, we enhance the classification accuracy of ML-based IDSs through a weighted ensemble learning approach optimized using the Covariance Matrix Adaptation Evolution Strategy (CMA-ES). Extensive experiments on two benchmark IoT intrusion detection datasets, namely UNSW-NB15 and TON-IoT
transfer_ivn:
Apply stable RFECV feature selection and CMA-ES-optimized weighted ensemble learning to in-vehicle network intrusion detection, using feature stability and ensemble outputs to flag adversarial feature injection in vehicle telemetry
transfer_risk:
Vehicle networks impose stricter real-time, resource, and protocol-specific constraints, so RFECV and CMA-ES may be too computationally heavy and feature stability may not generalize

#needs-review

## Record Fields
doi: https://doi.org/10.26599/tst.2026.9010058
source_link: not stated
text_kind: abstract
monitoring_problem: adversarial feature injection corrupting training data and feature selection in IoT intrusion detection
signal: stable feature subsets across RFECV models and ensemble classification performance
uncertainty_method: stability analysis of RFECV feature selection
action: retain stable features and train a CMA-ES-optimized weighted ensemble classifier
eval_setting: UNSW-NB15 and TON-IoT benchmark datasets
limitation_author: not stated
limitation_inference: the abstract does not discuss computational cost, real-time deployment, scalability, or generalization beyond the two evaluated datasets
limitation_unknown: not stated
support_passage: we propose a secure framework that applies recursive feature elimination with cross-validation (RFECV) across multiple models, followed by stability analysis to ensure robust feature selection. Additionally, we enhance the classification accuracy of ML-based IDSs through a weighted ensemble learning approach optimized using the Covariance Matrix Adaptation Evolution Strategy (CMA-ES). Extensive experiments on two benchmark IoT intrusion detection datasets, namely UNSW-NB15 and TON-IoT
transfer_ivn: Apply stable RFECV feature selection and CMA-ES-optimized weighted ensemble learning to in-vehicle network intrusion detection, using feature stability and ensemble outputs to flag adversarial feature injection in vehicle telemetry
transfer_risk: Vehicle networks impose stricter real-time, resource, and protocol-specific constraints, so RFECV and CMA-ES may be too computationally heavy and feature stability may not generalize
