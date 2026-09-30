---
title: "DMR-HDM: Data augmentation method based on Dual-Modal Representation and Hierarchical Diffusion Model for network intrusion detection"
year: 2026
doi: "https://doi.org/10.1016/j.jnca.2026.104566"
relevance_score: 6.0
type: paper
---
# DMR-HDM: Data augmentation method based on Dual-Modal Representation and Hierarchical Diffusion Model for network intrusion detection

Novelty

A dual-modal representation combined with a hierarchical diffusion model for data augmentation in network intrusion detection, addressing class imbalance by generating high-fidelity synthetic traffic samples.

Methodology

Data augmentation via Dual-Modal Representation (DMR) and Hierarchical Diffusion Model (HDM); learns joint feature distributions across modalities and generates synthetic intrusion samples hierarchically.

Explicit Limitations

Not stated in the provided title/abstract.

Future Work

Not stated in the provided title/abstract.

Concept Hubs

[[Concept - Diffusion Model Detection]]
[[Concept - Minority Class Augmentation]]
[[Concept - Deep Learning Intrusion Detection]]
[[Concept - Network Traffic Dynamics]]
[[Concept - Generative Adaptive Detection]]

Relevance Score

6

Monitoring Transfer

Monitoring problem: detecting network intrusions under severe class imbalance and evolving attack distributions. Signal: raw network traffic features across dual modalities. Uncertainty method: hierarchical diffusion generative modeling of feature distributions. Resulting action: synthetic sample augmentation to rebalance and enrich training data. Evaluation setting: enterprise/internet network intrusion detection benchmarks.

Transfer to IVN: dual-modal hierarchical diffusion augmentation could generate synthetic in-vehicle CAN/automotive Ethernet intrusion samples to relieve scarce attack data for in-vehicle network intrusion detection. Reason transfer may fail: IVN traffic has strict physical/timing semantics and deterministic scheduling, so diffusion-generated samples may violate CAN FD timing and signal constraints, producing unrealistic artifacts that harm detection.

doi: not stated
source_link: not stated
text_kind: title and abstract
monitoring_problem: network intrusion detection under class imbalance and evolving attacks
signal: dual-modal network traffic representations
uncertainty_method: hierarchical diffusion model
action: data augmentation with synthetic intrusion samples
eval_setting: enterprise/internet network intrusion detection
limitation_author: not stated
limitation_inference: generative fidelity and computational cost of hierarchical diffusion may limit real-time deployment
limitation_unknown: quantitative gains, dataset scope, and complexity overhead
support_passage: We study the application of deep learning methods into areas of enterprise/internet network intrusion detection
transfer_ivn: synthetic CAN/automotive Ethernet intrusion sample generation for in-vehicle network intrusion detection
transfer_risk: generated samples may violate physical/timing semantics of in-vehicle network traffic

A dual-modal representation combined with a hierarchical diffusion model for data augmentation in network intrusion detection, addressing class imbalance by generating high-fidelity synthetic traffic samples.

Data augmentation via Dual-Modal Representation (DMR) and Hierarchical Diffusion Model (HDM); learns joint feature distributions across modalities and generates synthetic intrusion samples hierarchically.

Not stated in the provided title/abstract.

Not stated in the provided title/abstract.

[[Concept - Diffusion Model Detection]]
[[Concept - Minority Class Augmentation]]
[[Concept - Deep Learning Intrusion Detection]]
[[Concept - Network Traffic Dynamics]]
[[Concept - Generative Adaptive Detection]]

6

Monitoring problem: detecting network intrusions under severe class imbalance and evolving attack distributions. Signal: raw network traffic features across dual modalities. Uncertainty method: hierarchical diffusion generative modeling of feature distributions. Resulting action: synthetic sample augmentation to rebalance and enrich training data. Evaluation setting: enterprise/internet network intrusion detection benchmarks.

Transfer to IVN: dual-modal hierarchical diffusion augmentation could generate synthetic in-vehicle CAN/automotive Ethernet intrusion samples to relieve scarce attack data for in-vehicle network intrusion detection. Reason transfer may fail: IVN traffic has strict physical/timing semantics and deterministic scheduling, so diffusion-generated samples may violate CAN FD timing and signal constraints, producing unrealistic artifacts that harm detection.

doi: not stated
source_link: not stated
text_kind: title and abstract
monitoring_problem: network intrusion detection under class imbalance and evolving attacks
signal: dual-modal network traffic representations
uncertainty_method: hierarchical diffusion model
action: data augmentation with synthetic intrusion samples
eval_setting: enterprise/internet network intrusion detection
limitation_author: not stated
limitation_inference: generative fidelity and computational cost of hierarchical diffusion may limit real-time deployment
limitation_unknown: quantitative gains, dataset scope, and complexity overhead
support_passage: We study the application of deep learning methods into areas of enterprise/internet network intrusion detection
transfer_ivn: synthetic CAN/automotive Ethernet intrusion sample generation for in-vehicle network intrusion detection
transfer_risk: generated samples may violate physical/timing semantics of in-vehicle network traffic

#needs-review

## Record Fields
doi: https://doi.org/10.1016/j.jnca.2026.104566
source_link: not stated
text_kind: abstract
monitoring_problem: detecting network intrusions under severe class imbalance and evolving attack distributions. Signal: raw network traffic features across dual modalities. Uncertainty method: hierarchical diffusion generative modeling of feature distributions. Resulting action: synthetic sample augmentation to rebalance and enrich training data. Evaluation setting: enterprise/internet network intrusion detection benchmarks.
signal: dual-modal network traffic representations
uncertainty_method: hierarchical diffusion model
action: data augmentation with synthetic intrusion samples
eval_setting: enterprise/internet network intrusion detection
limitation_author: not stated
limitation_inference: generative fidelity and computational cost of hierarchical diffusion may limit real-time deployment
limitation_unknown: quantitative gains, dataset scope, and complexity overhead
support_passage: We study the application of deep learning methods into areas of enterprise/internet network intrusion detection
transfer_ivn: synthetic CAN/automotive Ethernet intrusion sample generation for in-vehicle network intrusion detection
transfer_risk: generated samples may violate physical/timing semantics of in-vehicle network traffic
