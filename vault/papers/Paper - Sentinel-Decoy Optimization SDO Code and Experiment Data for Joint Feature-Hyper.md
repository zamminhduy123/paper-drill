---
title: "Sentinel-Decoy Optimization (SDO): Code and Experiment Data for Joint Feature-Hyperparameter Optimization and Adaptive Network Intrusion Detection"
year: 2026
doi: "https://doi.org/10.5281/zenodo.23007715"
relevance_score: 94.0
type: paper
---
# Sentinel-Decoy Optimization (SDO): Code and Experiment Data for Joint Feature-Hyperparameter Optimization and Adaptive Network Intrusion Detection

## Novelty
- Proposes Sentinel-Decoy Optimization (SDO), a differential-evolution-style metaheuristic that uses decoy-guided perturbations, threat memory, and an adaptive decoy ratio to maintain search diversity.
- Combines feature selection and hyperparameter co-optimization for a feature-masked neural-network intrusion detector.
- Adds an entropy-triggered online adaptation framework that uses prediction uncertainty as a boundary-pressure signal and performs warm-started re-optimization when drift or novel attack behavior is detected.

## Methodology
- Implements SDO and baseline optimizers PSO, GWO, and WOA on six shifted/rotated benchmark functions.
- Includes ablations isolating decoys, threat memory, and adaptive decoy ratio.
- Builds a joint feature-selection and hyperparameter co-optimization pipeline for a feature-masked neural-network intrusion detector.
- Evaluates the detector on UNSW-NB15, CIC-IDS2017, and CIC-IoT2023.
- Uses entropy-triggered monitoring of prediction uncertainty and warm-started re-optimization for drift or novel attack behavior.
- Applies paired Wilcoxon signed-rank testing, Holm-Bonferroni correction, and Friedman ranking across repeated runs.

## Explicit Limitations
- Raw third-party datasets are not redistributed in the repository.
- DOI is to be added once assigned.

## Future Work
not stated

## Concept Hubs
[[Concept - Deep Learning Intrusion Detection]]
[[Concept - Feature Selection]]
[[Concept - Anomaly Detection]]
[[Concept - Continual Learning]]
[[Concept - Network Traffic Analysis]]

## Relevance Score
94

## Monitoring Transfer
Monitoring problem: detecting drift or novel attack behavior in streaming network traffic.
Signal: prediction uncertainty as a boundary-pressure signal.
Uncertainty method: entropy-triggered online adaptation.
Resulting action: warm-started re-optimization of feature selection and hyperparameters.
Evaluation setting: UNSW-NB15, CIC-IDS2017, and CIC-IoT2023 with repeated-run statistical testing.
Transfer to IVN: apply entropy-triggered re-optimization to in-vehicle network intrusion detection by monitoring prediction uncertainty and adapting detector features/hyperparameters for novel in-vehicle attacks.
Transfer risk: IVN traffic is highly structured, latency-sensitive, and resource-constrained, so entropy-based triggers and re-optimization may be too slow or noisy for real-time CAN/IVN deployment.

doi: not stated
source_link: not stated
text_kind: repository
monitoring_problem: detecting drift or novel attack behavior in streaming network traffic
signal: prediction uncertainty as a boundary-pressure signal
uncertainty_method: entropy-triggered online adaptation
action: warm-started re-optimization of feature selection and hyperparameters
eval_setting: UNSW-NB15, CIC-IDS2017, and CIC-IoT2023 with repeated-run statistical testing
limitation_author: Raw third-party datasets are not redistributed here; DOI to be added once assigned
limitation_inference: No methodological limitations are stated in the abstract
limitation_unknown: not stated
support_passage: An entropy-triggered online adaptation framework that monitors prediction uncertainty as a boundary-pressure signal and performs warm-started re-optimization when drift or novel attack behavior is detected.
transfer_ivn: Apply entropy-triggered re-optimization to in-vehicle network intrusion detection by monitoring prediction uncertainty and adapting detector features/hyperparameters for novel in-vehicle attacks.
transfer_risk: IVN traffic is highly structured, latency-sensitive, and resource-constrained, so entropy-based triggers and re-optimization may be too slow or noisy for real-time CAN/IVN deployment.

#needs-review

## Record Fields
doi: https://doi.org/10.5281/zenodo.23007715
source_link: not stated
text_kind: abstract
monitoring_problem: detecting drift or novel attack behavior in streaming network traffic.
signal: prediction uncertainty as a boundary-pressure signal.
uncertainty_method: entropy-triggered online adaptation.
action: warm-started re-optimization of feature selection and hyperparameters
eval_setting: UNSW-NB15, CIC-IDS2017, and CIC-IoT2023 with repeated-run statistical testing
limitation_author: Raw third-party datasets are not redistributed here; DOI to be added once assigned
limitation_inference: No methodological limitations are stated in the abstract
limitation_unknown: not stated
support_passage: An entropy-triggered online adaptation framework that monitors prediction uncertainty as a boundary-pressure signal and performs warm-started re-optimization when drift or novel attack behavior is detected.
transfer_ivn: Apply entropy-triggered re-optimization to in-vehicle network intrusion detection by monitoring prediction uncertainty and adapting detector features/hyperparameters for novel in-vehicle attacks.
transfer_risk: IVN traffic is highly structured, latency-sensitive, and resource-constrained, so entropy-based triggers and re-optimization may be too slow or noisy for real-time CAN/IVN deployment.
