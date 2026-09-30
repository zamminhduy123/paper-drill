---
title: "conformal prediction for network intrusion detection"
year: 2026
doi: "https://doi.org/10.5281/zenodo.21781544"
relevance_score: 2.0
type: paper
---
# conformal prediction for network intrusion detection

Novelty

Conformal prediction provides distribution-free coverage guarantees for intrusion detection, wrapping existing deep learning backbones as a post-hoc calibration layer rather than replacing them - 2 . Unlike point-prediction accuracy metrics, conformal prediction converts softmax outputs into coverage-calibrated prediction sets with a statistical guarantee that the true label is included with probability 1 − α - 2 - 4 . Recent advances extend this to adversarial settings via attack-orbit invariance, selecting scored representations where attacker-controlled feature perturbations become the identity map, achieving exact rather than bounded coverage guarantees - 4 . Adaptive conformal inference addresses non-exchangeability through online threshold updates, enabling valid coverage under concept drift - 11 .

Methodology

Split conformal prediction computes nonconformity scores on a held-out calibration set, then selects a threshold q̂ such that prediction sets C(x) = {y : s(x,y) ≤ q̂} satisfy Pr[y ∉ C(x)] ≤ α - 1 . For intrusion detection, the nonconformity score is typically based on the softmax probability of the true class or margin-based measures - 2 . Weighted conformal prediction under covariate shift reweights calibration scores to account for distributional differences between training and deployment traffic - 4 . Adaptive conformal inference updates the quantile online using gradient-based updates to the miscoverage rate, maintaining coverage under temporal distribution shifts - 11 . Conformal risk control generalizes the framework to arbitrary monotone loss functions beyond classification error - 1 .

Explicit Limitations

Conformal prediction provides marginal coverage, not conditional coverage—a 90% guarantee holds on average across all predictions but may fail systematically for specific subgroups or minority attack classes - 17 . The exchangeability assumption underlying split conformal prediction is violated under distribution shift; deploying a calibrated checkpoint on a different dataset's traffic drives single-step miscoverage to 100% even at 78% top-1 accuracy - 1 . Prediction set efficiency degrades under distribution shift, with empty prediction sets becoming a stark label-free symptom of exchangeability violation - 1 . Conformal pseudo-labels for online model updating show inconsistent performance across datasets and models, with greater drift magnitude reducing improvement - 11 . The calibration set requirement reduces data available for training, which is particularly problematic when attack samples are scarce - 17 .

Future Work

Extending conformal prediction to multi-protocol in-vehicle network settings spanning CAN, Ethernet, and V2X interfaces remains an architectural direction rather than an empirically validated component - 5 . Developing adaptive calibration mechanisms that maintain coverage under adversarial manipulation without requiring matched-perturbation calibration sets - 4 . Exploring the reduction of correct prediction rejection when conformal layers filter uncertain samples, balancing coverage guarantees against operational throughput - 16 . Investigating class-conditional conformal methods to provide subgroup-level coverage guarantees for rare attack families - 17 . Integrating conformal prediction with sequential detection frameworks like CUSUM for joint coverage and latency optimization under real-time constraints - 3 .

Concept Hubs

[[Concept - Deep Learning Intrusion Detection]]
[[Concept - Anomaly Detection]]
[[Concept - Threshold Control]]
[[Concept - Context-Specific Outliers]]
[[Concept - Network Traffic Dynamics]]

Relevance Score

High

Monitoring Transfer

Monitoring problem: Distribution shift between calibration and deployment traffic causes silent coverage loss, where the detector remains confident but prediction sets no longer contain the true label at the promised rate.

Signal: Empty or inflated prediction sets at inference time—a label-free symptom available without ground truth - 1 .

Uncertainty method: Split conformal prediction with nonconformity scores based on model softmax outputs - 1 - 2 .

Resulting action: Flag traffic for analyst review or model recalibration when prediction set size exceeds a threshold, or when empty sets indicate severe exchangeability violation.

Evaluation setting: CIC-IDS2017/2018 and CICIoT2023 benchmarks; cross-dataset deployment of fine-tuned checkpoints to measure coverage degradation under real distribution shift - 1 - 2 .

Transfer to IVN: CAN bus intrusion detection using conformal prediction on recurrent plot CNN features, where the HCRL Car-Hacking dataset provides a natural calibration and evaluation setting - 19 .

Transfer risk: CAN traffic exhibits deterministic scheduling and physical-layer constraints that violate exchangeability in ways distinct from Ethernet/IP traffic—the calibration distribution may not represent attack variants that emerge from bus-specific vulnerabilities, causing coverage guarantees to fail silently in the safety-critical setting.

doi: not stated
source_link: https://inass.org/wp-content/uploads/2026/05/2026083128-2.pdf
text_kind: research article
monitoring_problem: Silent coverage loss under distribution shift between calibration and deployment traffic
signal: Empty or inflated prediction sets at inference time
uncertainty_method: Split conformal prediction with softmax-based nonconformity scores
action: Flag for review or recalibration when prediction sets exceed size threshold
eval_setting: CIC-IDS2017/2018, CICIoT2023 benchmarks with cross-dataset shift evaluation
limitation_author: Marginal coverage does not guarantee conditional coverage for subgroups or minority classes; exchangeability violation under shift causes 100% miscoverage
limitation_inference: IVN CAN bus traffic violates exchangeability due to deterministic scheduling and physical constraints
limitation_unknown: Whether adaptive conformal methods maintain coverage under adversarial manipulation of CAN frames
support_passage: Deploying a stage's own fine-tuned checkpoint on a different dataset's real traffic drives single-step miscoverage to 100% in all 12 tested cells, even at 78% top-1 accuracy
transfer_ivn: CAN bus intrusion detection with conformal prediction on recurrent plot CNN features
transfer_risk: CAN-specific attack variants and deterministic bus scheduling may violate exchangeability differently than IP traffic, causing coverage guarantees to fail silently

Conformal prediction provides distribution-free coverage guarantees for intrusion detection, wrapping existing deep learning backbones as a post-hoc calibration layer rather than replacing them - 2 . Unlike point-prediction accuracy metrics, conformal prediction converts softmax outputs into coverage-calibrated prediction sets with a statistical guarantee that the true label is included with probability 1 − α - 2 - 4 . Recent advances extend this to adversarial settings via attack-orbit invariance, selecting scored representations where attacker-controlled feature perturbations become the identity map, achieving exact rather than bounded coverage guarantees - 4 . Adaptive conformal inference addresses non-exchangeability through online threshold updates, enabling valid coverage under concept drift - 11 .

- 2

- 2

- 4

- 4

- 11

Split conformal prediction computes nonconformity scores on a held-out calibration set, then selects a threshold q̂ such that prediction sets C(x) = {y : s(x,y) ≤ q̂} satisfy Pr[y ∉ C(x)] ≤ α - 1 . For intrusion detection, the nonconformity score is typically based on the softmax probability of the true class or margin-based measures - 2 . Weighted conformal prediction under covariate shift reweights calibration scores to account for distributional differences between training and deployment traffic - 4 . Adaptive conformal inference updates the quantile online using gradient-based updates to the miscoverage rate, maintaining coverage under temporal distribution shifts - 11 . Conformal risk control generalizes the framework to arbitrary monotone loss functions beyond classification error - 1 .

- 1

- 2

- 4

- 11

- 1

Conformal prediction provides marginal coverage, not conditional coverage—a 90% guarantee holds on average across all predictions but may fail systematically for specific subgroups or minority attack classes - 17 . The exchangeability assumption underlying split conformal prediction is violated under distribution shift; deploying a calibrated checkpoint on a different dataset's traffic drives single-step miscoverage to 100% even at 78% top-1 accuracy - 1 . Prediction set efficiency degrades under distribution shift, with empty prediction sets becoming a stark label-free symptom of exchangeability violation - 1 . Conformal pseudo-labels for online model updating show inconsistent performance across datasets and models, with greater drift magnitude reducing improvement - 11 . The calibration set requirement reduces data available for training, which is particularly problematic when attack samples are scarce - 17 .

- 17

- 1

- 1

- 11

- 17

Extending conformal prediction to multi-protocol in-vehicle network settings spanning CAN, Ethernet, and V2X interfaces remains an architectural direction rather than an empirically validated component - 5 . Developing adaptive calibration mechanisms that maintain coverage under adversarial manipulation without requiring matched-perturbation calibration sets - 4 . Exploring the reduction of correct prediction rejection when conformal layers filter uncertain samples, balancing coverage guarantees against operational throughput - 16 . Investigating class-conditional conformal methods to provide subgroup-level coverage guarantees for rare attack families - 17 . Integrating conformal prediction with sequential detection frameworks like CUSUM for joint coverage and latency optimization under real-time constraints - 3 .

- 5

- 4

- 16

- 17

- 3

[[Concept - Deep Learning Intrusion Detection]]
[[Concept - Anomaly Detection]]
[[Concept - Threshold Control]]
[[Concept - Context-Specific Outliers]]
[[Concept - Network Traffic Dynamics]]

High

Monitoring problem: Distribution shift between calibration and deployment traffic causes silent coverage loss, where the detector remains confident but prediction sets no longer contain the true label at the promised rate.

Signal: Empty or inflated prediction sets at inference time—a label-free symptom available without ground truth - 1 .

- 1

Uncertainty method: Split conformal prediction with nonconformity scores based on model softmax outputs - 1 - 2 .

- 1

- 2

Resulting action: Flag traffic for analyst review or model recalibration when prediction set size exceeds a threshold, or when empty sets indicate severe exchangeability violation.

Evaluation setting: CIC-IDS2017/2018 and CICIoT2023 benchmarks; cross-dataset deployment of fine-tuned checkpoints to measure coverage degradation under real distribution shift - 1 - 2 .

- 1

- 2

Transfer to IVN: CAN bus intrusion detection using conformal prediction on recurrent plot CNN features, where the HCRL Car-Hacking dataset provides a natural calibration and evaluation setting - 19 .

- 19

Transfer risk: CAN traffic exhibits deterministic scheduling and physical-layer constraints that violate exchangeability in ways distinct from Ethernet/IP traffic—the calibration distribution may not represent attack variants that emerge from bus-specific vulnerabilities, causing coverage guarantees to fail silently in the safety-critical setting.

doi: not stated
source_link: https://inass.org/wp-content/uploads/2026/05/2026083128-2.pdf
text_kind: research article
monitoring_problem: Silent coverage loss under distribution shift between calibration and deployment traffic
signal: Empty or inflated prediction sets at inference time
uncertainty_method: Split conformal prediction with softmax-based nonconformity scores
action: Flag for review or recalibration when prediction sets exceed size threshold
eval_setting: CIC-IDS2017/2018, CICIoT2023 benchmarks with cross-dataset shift evaluation
limitation_author: Marginal coverage does not guarantee conditional coverage for subgroups or minority classes; exchangeability violation under shift causes 100% miscoverage
limitation_inference: IVN CAN bus traffic violates exchangeability due to deterministic scheduling and physical constraints
limitation_unknown: Whether adaptive conformal methods maintain coverage under adversarial manipulation of CAN frames
support_passage: Deploying a stage's own fine-tuned checkpoint on a different dataset's real traffic drives single-step miscoverage to 100% in all 12 tested cells, even at 78% top-1 accuracy
transfer_ivn: CAN bus intrusion detection with conformal prediction on recurrent plot CNN features
transfer_risk: CAN-specific attack variants and deterministic bus scheduling may violate exchangeability differently than IP traffic, causing coverage guarantees to fail silently

## Record Fields
doi: https://doi.org/10.5281/zenodo.21781544
source_link: https://inass.org/wp-content/uploads/2026/05/2026083128-2.pdf
text_kind: abstract
monitoring_problem: Distribution shift between calibration and deployment traffic causes silent coverage loss, where the detector remains confident but prediction sets no longer contain the true label at the promised rate.
signal: Empty or inflated prediction sets at inference time—a label-free symptom available without ground truth - 1 .
uncertainty_method: Split conformal prediction with nonconformity scores based on model softmax outputs - 1 - 2 .
action: Flag for review or recalibration when prediction sets exceed size threshold
eval_setting: CIC-IDS2017/2018, CICIoT2023 benchmarks with cross-dataset shift evaluation
limitation_author: Marginal coverage does not guarantee conditional coverage for subgroups or minority classes; exchangeability violation under shift causes 100% miscoverage
limitation_inference: IVN CAN bus traffic violates exchangeability due to deterministic scheduling and physical constraints
limitation_unknown: Whether adaptive conformal methods maintain coverage under adversarial manipulation of CAN frames
support_passage: Deploying a stage's own fine-tuned checkpoint on a different dataset's real traffic drives single-step miscoverage to 100% in all 12 tested cells, even at 78% top-1 accuracy
transfer_ivn: CAN bus intrusion detection with conformal prediction on recurrent plot CNN features
transfer_risk: CAN traffic exhibits deterministic scheduling and physical-layer constraints that violate exchangeability in ways distinct from Ethernet/IP traffic—the calibration distribution may not represent attack variants that emerge from bus-specific vulnerabilities, causing coverage guarantees to fail silently in the safety-critical setting.
