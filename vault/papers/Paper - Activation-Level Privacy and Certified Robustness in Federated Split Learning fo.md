---
title: "Activation-Level Privacy and Certified Robustness in Federated Split Learning for IoT Intrusion Detection"
year: 2026
doi: "https://doi.org/10.1051/epjconf/202638100035/pdf"
relevance_score: 0.95
type: paper
---
# Activation-Level Privacy and Certified Robustness in Federated Split Learning for IoT Intrusion Detection

## Novelty
SplitFed-DP moves Gaussian differential privacy from high-dimensional full-encoder gradients to low-dimensional cut-layer activations in federated split learning, and shows that the same Gaussian release also provides a certified l2-robustness guarantee via randomized smoothing.

## Methodology
A federated split-learning pipeline is trained for IoT intrusion detection with a dual guarantee: Rényi differential privacy is audited on a low-dimensional activation release at the cut layer, and the same release is interpreted as a randomized-smoothing operator to certify l2-robustness. The approach is evaluated on TON-IoT and Bot-IoT against gradient-level DP-SGD and non-private federated baselines.

## Explicit Limitations
not stated

## Future Work
not stated

## Concept Hubs
[[Concept - IoT Intrusion Detection]]
[[Concept - Privacy-Preserving Learning]]
[[Concept - Deep Learning Intrusion Detection]]
[[Concept - Federated Split Learning]]
[[Concept - Certified Robustness]]

## Relevance Score
0.95

## Monitoring Transfer
doi: not stated
source_link: not stated
text_kind: abstract
monitoring_problem: protect client training records in federated IoT intrusion detection under non-IID label-scarce traffic
signal: low-dimensional cut-layer activation with Gaussian release
uncertainty_method: Rényi differential privacy and randomized smoothing certified l2 robustness
action: train and certify a federated split intrusion detector
eval_setting: TON-IoT and Bot-IoT executed runs against DP-SGD and non-private federated baselines
limitation_author: not stated
limitation_inference: residual utility gap to oracle and only a large majority of inputs certified
limitation_unknown: not stated
support_passage: closes about two-thirds of the DP-SGD-to-oracle utility gap and certifies a large majority of inputs at non-trivial radii
transfer_ivn: apply activation-level DP split learning to in-vehicle network intrusion detection to protect vehicle data and certify robustness
transfer_risk: IVN traffic may be more heterogeneous and safety-critical, reducing utility or certification coverage

#needs-review

## Record Fields
doi: https://doi.org/10.1051/epjconf/202638100035/pdf
source_link: not stated
text_kind: abstract
monitoring_problem: protect client training records in federated IoT intrusion detection under non-IID label-scarce traffic
signal: low-dimensional cut-layer activation with Gaussian release
uncertainty_method: Rényi differential privacy and randomized smoothing certified l2 robustness
action: train and certify a federated split intrusion detector
eval_setting: TON-IoT and Bot-IoT executed runs against DP-SGD and non-private federated baselines
limitation_author: not stated
limitation_inference: residual utility gap to oracle and only a large majority of inputs certified
limitation_unknown: not stated
support_passage: closes about two-thirds of the DP-SGD-to-oracle utility gap and certifies a large majority of inputs at non-trivial radii
transfer_ivn: apply activation-level DP split learning to in-vehicle network intrusion detection to protect vehicle data and certify robustness
transfer_risk: IVN traffic may be more heterogeneous and safety-critical, reducing utility or certification coverage
