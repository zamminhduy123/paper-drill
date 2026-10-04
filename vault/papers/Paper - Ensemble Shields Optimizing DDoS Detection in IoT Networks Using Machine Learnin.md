---
title: "Ensemble Shields: Optimizing DDoS Detection in IoT Networks Using Machine Learning"
year: 2026
doi: "https://doi.org/10.3390/app16199607"
relevance_score: 6.0
type: paper
---
# Ensemble Shields: Optimizing DDoS Detection in IoT Networks Using Machine Learning

## Novelty
The paper proposes two optimized ensemble methods for DDoS detection in IoT networks: OESA-4, a stacking ensemble using a meta-learner, and OEVA-4, a weighted soft-voting ensemble. Both combine four supervised classifiers: KNN, Random Forest, XGBoost, and Decision Tree.

## Methodology
The study evaluates OESA-4 and OEVA-4 on a subset of the CIC-DDoS2019 dataset containing 325,965 occurrences. OESA-4 combines base learner outputs through a meta-learner, while OEVA-4 assigns different weights to base learners using weighted soft voting. Performance is assessed using a single split and stratified five-fold cross-validation.

## Explicit Limitations
not stated

## Future Work
not stated

## Concept Hubs
[[Concept - Stacking Ensemble]] [[Concept - Heterogeneous Base Learners]] [[Concept - Meta-Classifier]] [[Concept - IoT Intrusion Detection]] [[Concept - Intrusion Detection]]

## Relevance Score
6/10

## Monitoring Transfer
doi:
not stated
source_link:
not stated
text_kind:
abstract
monitoring_problem:
DDoS attack detection in IoT network traffic
signal:
network traffic occurrences from the CIC-DDoS2019 subset
uncertainty_method:
not stated
action:
classify traffic as DDoS attack type
eval_setting:
single split and stratified five-fold cross-validation on 325,965 occurrences
limitation_author:
not stated
limitation_inference:
evaluation uses one supervised dataset subset and reports accuracy without uncertainty calibration or real-time deployment constraints
limitation_unknown:
not stated
support_passage:
The results show that the proposed OESA-4 and OEVA-4 demonstrated reliable performance with accuracies of 99.87% and 99.73%, respectively, on a single split, whereas stratified five-fold cross-validation resulted in mean accuracies of 99.51% ± 0.08% for OESA-4 and 99.28% ± 0.11% for OEVA-4 respectively.
transfer_ivn:
apply OESA-4 and OEVA-4 ensembles to in-vehicle network traffic to detect DDoS-like flooding attacks
transfer_risk:
IVN traffic is protocol-specific and safety-critical, so IoT DDoS features and ensemble weights may not generalize and may cause false alarms

#needs-review

## Record Fields
doi: https://doi.org/10.3390/app16199607
source_link: not stated
text_kind: abstract
monitoring_problem: DDoS attack detection in IoT network traffic
signal: network traffic occurrences from the CIC-DDoS2019 subset
uncertainty_method: not stated
action: classify traffic as DDoS attack type
eval_setting: single split and stratified five-fold cross-validation on 325,965 occurrences
limitation_author: not stated
limitation_inference: evaluation uses one supervised dataset subset and reports accuracy without uncertainty calibration or real-time deployment constraints
limitation_unknown: not stated
support_passage: The results show that the proposed OESA-4 and OEVA-4 demonstrated reliable performance with accuracies of 99.87% and 99.73%, respectively, on a single split, whereas stratified five-fold cross-validation resulted in mean accuracies of 99.51% ± 0.08% for OESA-4 and 99.28% ± 0.11% for OEVA-4 respectively.
transfer_ivn: apply OESA-4 and OEVA-4 ensembles to in-vehicle network traffic to detect DDoS-like flooding attacks
transfer_risk: IVN traffic is protocol-specific and safety-critical, so IoT DDoS features and ensemble weights may not generalize and may cause false alarms
