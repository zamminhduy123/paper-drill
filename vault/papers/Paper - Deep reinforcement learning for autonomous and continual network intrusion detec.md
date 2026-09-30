---
title: "Deep reinforcement learning for autonomous and continual network intrusion detection"
year: 2026
doi: "https://doi.org/10.1016/j.jisa.2026.104594"
relevance_score: 9.649
type: paper
---
# Deep reinforcement learning for autonomous and continual network intrusion detection

Novelty

Autonomous end-to-end NIDS combining deep RL–guided continual learning with clustering-based emerging-pattern detection/labeling and CGAN-based CL data generation, removing manual labeling and repeated fine-tuning while mitigating catastrophic forgetting.

Methodology

Two-layer architecture: (1) emerging-pattern detection and labeling via clustering to group/label novel traffic patterns; (2) conditional GAN (CGAN) generating CL-related data for detected patterns to support balanced retraining without catastrophic forgetting. A deep RL agent guides the ML-based NID classifier through continual learning by deciding when to adapt and how much retraining data to use from different sources. Evaluated on four widely used NIDS datasets with ablation studies.

Explicit Limitations

Not stated by authors in provided text.

Future Work

Not stated by authors in provided text.

Concept Hubs

[[Concept - Continual Learning]]
[[Concept - Catastrophic Forgetting]]
[[Concept - Deep Learning Intrusion Detection]]
[[Concept - Generative Adaptive Detection]]
[[Concept - Unsupervised Intrusion Detection]]

Relevance Score

Not stated.

Monitoring Transfer

Monitoring problem: detecting novel attacks, zero-day attacks, and evolving benign traffic in enterprise/internet networks. Signal: network traffic patterns and classifier outputs over time. Uncertainty method: deep RL agent decides when to adapt and how much retraining data to use from different sources; clustering labels novel patterns. Resulting action: continual fine-tuning/retraining of the ML-based NID classifier with CGAN-generated data. Evaluation setting: four widely used NIDS datasets, including ablation studies, with source code on GitHub.

Transfer to IVN: the RL-guided continual learning controller could govern when and how much to retrain an in-vehicle NIDS classifier as CAN/CAN FD traffic behavior drifts with firmware updates, new ECUs, or novel injection attacks. Transfer may fail because in-vehicle traffic is highly deterministic and periodic, so clustering may mislabel normal scheduling jitter as novel patterns, and the RL agent's adaptation triggers would fire on benign timing variation rather than genuine attacks.

doi: not stated
source_link: https://github.com/hanisami/nids_continual_learning
text_kind: abstract
monitoring_problem: detecting novel and zero-day attacks plus evolving benign traffic patterns in enterprise/internet networks
signal: network traffic patterns and ML-based NID classifier outputs
uncertainty_method: deep RL agent deciding when to adapt and how much retraining data to use, with clustering for emerging-pattern detection and labeling
action: continual learning/fine-tuning of the NID classifier using CGAN-generated retraining data
eval_setting: four widely used NIDS datasets with ablation studies
limitation_author: not stated
limitation_inference: RL adaptation may be slow and clustering labels may be unreliable for highly deterministic periodic traffic
limitation_unknown: GARDIAN performance under real-time latency constraints and adversarial evasion is not stated
support_passage: GARDIAN integrates a deep RL agent that guides the ML-based NID classifier through the CL process by deciding when to adapt and how much retraining data to use from different sources.
transfer_ivn: RL-guided continual learning controller for retraining in-vehicle NIDS under traffic drift
transfer_risk: deterministic periodic CAN traffic may be mislabeled as novel, triggering unnecessary retraining

Autonomous end-to-end NIDS combining deep RL–guided continual learning with clustering-based emerging-pattern detection/labeling and CGAN-based CL data generation, removing manual labeling and repeated fine-tuning while mitigating catastrophic forgetting.

Two-layer architecture: (1) emerging-pattern detection and labeling via clustering to group/label novel traffic patterns; (2) conditional GAN (CGAN) generating CL-related data for detected patterns to support balanced retraining without catastrophic forgetting. A deep RL agent guides the ML-based NID classifier through continual learning by deciding when to adapt and how much retraining data to use from different sources. Evaluated on four widely used NIDS datasets with ablation studies.

Not stated by authors in provided text.

Not stated by authors in provided text.

[[Concept - Continual Learning]]
[[Concept - Catastrophic Forgetting]]
[[Concept - Deep Learning Intrusion Detection]]
[[Concept - Generative Adaptive Detection]]
[[Concept - Unsupervised Intrusion Detection]]

Not stated.

Monitoring problem: detecting novel attacks, zero-day attacks, and evolving benign traffic in enterprise/internet networks. Signal: network traffic patterns and classifier outputs over time. Uncertainty method: deep RL agent decides when to adapt and how much retraining data to use from different sources; clustering labels novel patterns. Resulting action: continual fine-tuning/retraining of the ML-based NID classifier with CGAN-generated data. Evaluation setting: four widely used NIDS datasets, including ablation studies, with source code on GitHub.

Transfer to IVN: the RL-guided continual learning controller could govern when and how much to retrain an in-vehicle NIDS classifier as CAN/CAN FD traffic behavior drifts with firmware updates, new ECUs, or novel injection attacks. Transfer may fail because in-vehicle traffic is highly deterministic and periodic, so clustering may mislabel normal scheduling jitter as novel patterns, and the RL agent's adaptation triggers would fire on benign timing variation rather than genuine attacks.

doi: not stated
source_link: https://github.com/hanisami/nids_continual_learning
text_kind: abstract
monitoring_problem: detecting novel and zero-day attacks plus evolving benign traffic patterns in enterprise/internet networks
signal: network traffic patterns and ML-based NID classifier outputs
uncertainty_method: deep RL agent deciding when to adapt and how much retraining data to use, with clustering for emerging-pattern detection and labeling
action: continual learning/fine-tuning of the NID classifier using CGAN-generated retraining data
eval_setting: four widely used NIDS datasets with ablation studies
limitation_author: not stated
limitation_inference: RL adaptation may be slow and clustering labels may be unreliable for highly deterministic periodic traffic
limitation_unknown: GARDIAN performance under real-time latency constraints and adversarial evasion is not stated
support_passage: GARDIAN integrates a deep RL agent that guides the ML-based NID classifier through the CL process by deciding when to adapt and how much retraining data to use from different sources.
transfer_ivn: RL-guided continual learning controller for retraining in-vehicle NIDS under traffic drift
transfer_risk: deterministic periodic CAN traffic may be mislabeled as novel, triggering unnecessary retraining

#needs-review

## Record Fields
doi: https://doi.org/10.1016/j.jisa.2026.104594
source_link: https://github.com/hanisami/nids_continual_learning
text_kind: abstract
monitoring_problem: detecting novel attacks, zero-day attacks, and evolving benign traffic in enterprise/internet networks. Signal: network traffic patterns and classifier outputs over time. Uncertainty method: deep RL agent decides when to adapt and how much retraining data to use from different sources; clustering labels novel patterns. Resulting action: continual fine-tuning/retraining of the ML-based NID classifier with CGAN-generated data. Evaluation setting: four widely used NIDS datasets, including ablation studies, with source code on GitHub.
signal: network traffic patterns and ML-based NID classifier outputs
uncertainty_method: deep RL agent deciding when to adapt and how much retraining data to use, with clustering for emerging-pattern detection and labeling
action: continual learning/fine-tuning of the NID classifier using CGAN-generated retraining data
eval_setting: four widely used NIDS datasets with ablation studies
limitation_author: not stated
limitation_inference: RL adaptation may be slow and clustering labels may be unreliable for highly deterministic periodic traffic
limitation_unknown: GARDIAN performance under real-time latency constraints and adversarial evasion is not stated
support_passage: GARDIAN integrates a deep RL agent that guides the ML-based NID classifier through the CL process by deciding when to adapt and how much retraining data to use from different sources.
transfer_ivn: RL-guided continual learning controller for retraining in-vehicle NIDS under traffic drift
transfer_risk: deterministic periodic CAN traffic may be mislabeled as novel, triggering unnecessary retraining
