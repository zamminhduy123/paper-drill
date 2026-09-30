---
title: "Sequential submodular feature-sample selection for lightweight and update-efficient IoT intrusion detection"
year: 2026
doi: "https://doi.org/10.1038/s41598-026-66614-x"
relevance_score: 4.0
type: paper
---
# Sequential submodular feature-sample selection for lightweight and update-efficient IoT intrusion detection

Novelty

Sequential two-stage framework (SSFSS) that jointly optimizes feature space (LA-CGFS, label-conditioned facility location) and sample space (geometry-aware coreset selection), with a proven constant-factor approximation guarantee via submodularity, rather than treating dimensionality reduction and data pruning as isolated tasks.

Methodology

Feature selection as a label-aware facility location problem maximizing coverage across class manifolds (no synthetic oversampling); geometry-aware coreset selection minimizing coverage error in the reduced space; submodular diminishing-returns property yields approximation guarantee; evaluated on RT-IoT2022, Edge-IIoTset, CICIoT2023 with four ERM classifiers (kernel logistic regression, kernel SVM, kernel ridge, softmax regression); measured training speedup, peak RAM, accuracy, macro-F1, balanced accuracy.

Explicit Limitations

Not stated.

Future Work

Not stated.

Concept Hubs

[[Concept - IoT Intrusion Detection]]
[[Concept - Lightweight Detection]]
[[Concept - Edge Security]]
[[Concept - Coreset Selection]]
[[Concept - Submodular Optimization]]

Relevance Score

4

Monitoring Transfer

Monitoring problem: detecting intrusions in resource-constrained IoT traffic under evolving attack patterns requiring on-device retraining.
Signal: high-dimensional traffic features and large labeled traffic corpora.
Uncertainty method: submodular coverage bounds and approximation guarantee; empirical accuracy/F1 across classifiers and datasets.
Resulting action: select reduced feature subset and coreset, then retrain lightweight classifier.
Evaluation setting: offline benchmark evaluation on RT-IoT2022, Edge-IIoTset, CICIoT2023 with four differentiable ERM classifiers, measuring speedup, RAM, accuracy, macro-F1, balanced accuracy.

doi: not stated
source_link: not stated
text_kind: abstract
monitoring_problem: intrusion detection in resource-constrained IoT networks with evolving traffic and attacks requiring frequent retraining
signal: high-dimensional traffic features and large labeled traffic corpora
uncertainty_method: submodular approximation guarantee with coverage-based bounds and empirical classifier metrics
action: sequential feature and sample selection followed by lightweight classifier retraining
eval_setting: offline benchmarks RT-IoT2022, Edge-IIoTset, CICIoT2023 across four differentiable ERM classifiers
limitation_author: not stated
limitation_inference: evaluation is offline and benchmark-based, so on-device deployment, streaming traffic, and real hardware constraints are not demonstrated
limitation_unknown: exact speedup factors, RAM figures, and whether results hold under concept drift or adversarial evasion
support_passage: Extensive evaluation on the RT-IoT2022, Edge-IIoTset, and CICIoT2023 datasets demonstrates that SSFSS reduces the feature space to 20 features and the training set to as little as 5% of the original samples
transfer_ivn: apply submodular feature-sample selection to CAN/IVN traffic so in-vehicle IDS can be retrained on constrained ECU hardware
transfer_risk: CAN frames lack the rich feature dimensionality and label structure of IoT flow datasets, so coverage-based selection may discard rare but safety-critical attack signatures

Sequential two-stage framework (SSFSS) that jointly optimizes feature space (LA-CGFS, label-conditioned facility location) and sample space (geometry-aware coreset selection), with a proven constant-factor approximation guarantee via submodularity, rather than treating dimensionality reduction and data pruning as isolated tasks.

Feature selection as a label-aware facility location problem maximizing coverage across class manifolds (no synthetic oversampling); geometry-aware coreset selection minimizing coverage error in the reduced space; submodular diminishing-returns property yields approximation guarantee; evaluated on RT-IoT2022, Edge-IIoTset, CICIoT2023 with four ERM classifiers (kernel logistic regression, kernel SVM, kernel ridge, softmax regression); measured training speedup, peak RAM, accuracy, macro-F1, balanced accuracy.

Not stated.

Not stated.

[[Concept - IoT Intrusion Detection]]
[[Concept - Lightweight Detection]]
[[Concept - Edge Security]]
[[Concept - Coreset Selection]]
[[Concept - Submodular Optimization]]

4

Monitoring problem: detecting intrusions in resource-constrained IoT traffic under evolving attack patterns requiring on-device retraining.
Signal: high-dimensional traffic features and large labeled traffic corpora.
Uncertainty method: submodular coverage bounds and approximation guarantee; empirical accuracy/F1 across classifiers and datasets.
Resulting action: select reduced feature subset and coreset, then retrain lightweight classifier.
Evaluation setting: offline benchmark evaluation on RT-IoT2022, Edge-IIoTset, CICIoT2023 with four differentiable ERM classifiers, measuring speedup, RAM, accuracy, macro-F1, balanced accuracy.

doi: not stated
source_link: not stated
text_kind: abstract
monitoring_problem: intrusion detection in resource-constrained IoT networks with evolving traffic and attacks requiring frequent retraining
signal: high-dimensional traffic features and large labeled traffic corpora
uncertainty_method: submodular approximation guarantee with coverage-based bounds and empirical classifier metrics
action: sequential feature and sample selection followed by lightweight classifier retraining
eval_setting: offline benchmarks RT-IoT2022, Edge-IIoTset, CICIoT2023 across four differentiable ERM classifiers
limitation_author: not stated
limitation_inference: evaluation is offline and benchmark-based, so on-device deployment, streaming traffic, and real hardware constraints are not demonstrated
limitation_unknown: exact speedup factors, RAM figures, and whether results hold under concept drift or adversarial evasion
support_passage: Extensive evaluation on the RT-IoT2022, Edge-IIoTset, and CICIoT2023 datasets demonstrates that SSFSS reduces the feature space to 20 features and the training set to as little as 5% of the original samples
transfer_ivn: apply submodular feature-sample selection to CAN/IVN traffic so in-vehicle IDS can be retrained on constrained ECU hardware
transfer_risk: CAN frames lack the rich feature dimensionality and label structure of IoT flow datasets, so coverage-based selection may discard rare but safety-critical attack signatures

#needs-review

## Record Fields
doi: https://doi.org/10.1038/s41598-026-66614-x
source_link: not stated
text_kind: abstract
monitoring_problem: detecting intrusions in resource-constrained IoT traffic under evolving attack patterns requiring on-device retraining.
signal: high-dimensional traffic features and large labeled traffic corpora.
uncertainty_method: submodular coverage bounds and approximation guarantee; empirical accuracy/F1 across classifiers and datasets.
action: sequential feature and sample selection followed by lightweight classifier retraining
eval_setting: offline benchmarks RT-IoT2022, Edge-IIoTset, CICIoT2023 across four differentiable ERM classifiers
limitation_author: not stated
limitation_inference: evaluation is offline and benchmark-based, so on-device deployment, streaming traffic, and real hardware constraints are not demonstrated
limitation_unknown: exact speedup factors, RAM figures, and whether results hold under concept drift or adversarial evasion
support_passage: Extensive evaluation on the RT-IoT2022, Edge-IIoTset, and CICIoT2023 datasets demonstrates that SSFSS reduces the feature space to 20 features and the training set to as little as 5% of the original samples
transfer_ivn: apply submodular feature-sample selection to CAN/IVN traffic so in-vehicle IDS can be retrained on constrained ECU hardware
transfer_risk: CAN frames lack the rich feature dimensionality and label structure of IoT flow datasets, so coverage-based selection may discard rare but safety-critical attack signatures
