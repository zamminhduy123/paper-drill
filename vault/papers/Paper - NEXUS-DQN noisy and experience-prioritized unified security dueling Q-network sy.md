---
title: "NEXUS-DQN★: noisy and experience-prioritized unified security dueling Q-network system for intelligent and optimized network traffic intrusion detection"
year: 2026
doi: "https://doi.org/10.1007/s10586-026-06526-7"
relevance_score: 9.609
type: paper
---
# NEXUS-DQN★: noisy and experience-prioritized unified security dueling Q-network system for intelligent and optimized network traffic intrusion detection

Novelty

The paper proposes NEXUS-DQN★, a dueling deep Q-network system that unifies noisy exploration and experience prioritization for network traffic intrusion detection. Novelty lies in combining noisy networks with prioritized experience replay inside a dueling Q architecture, rather than treating exploration and sampling efficiency separately.

Methodology

Deep reinforcement learning for intrusion detection: dueling Q-network architecture, noisy parameter layers for exploration, experience-prioritized replay for sample efficiency, applied to enterprise/internet network traffic classification. Not stated: exact datasets, feature engineering, training schedule, baselines.

Explicit Limitations

Not stated in the provided title and abstract.

Future Work

Not stated in the provided title and abstract.

Concept Hubs

[[Concept - Deep Learning Intrusion Detection]]
[[Concept - Network Traffic Dynamics]]
[[Concept - Real-Time Attack Defense]]
[[Concept - Anomaly Detection]]
[[Concept - Edge Security]]

Relevance Score

Not stated

Monitoring Transfer

Monitoring problem: detecting intrusions in enterprise/internet network traffic. Signal: network traffic features/flow statistics. Uncertainty method: noisy network parameter exploration within dueling Q-learning. Action: classify traffic as intrusive or benign and trigger defense response. Evaluation setting: not stated; presumably benchmark or enterprise network traffic datasets. Transfer to IVN: the dueling DQN with noisy exploration and prioritized replay could be adapted to CAN/automotive intrusion detection where sequential decision-making over traffic frames matters. Transfer risk: enterprise traffic statistics and label semantics differ substantially from CAN frame timing and signal-level behavior, so learned policies may not generalize.

doi: not stated
source_link: not stated
text_kind: title and abstract only
monitoring_problem: enterprise and internet network intrusion detection
signal: network traffic data
uncertainty_method: noisy networks with dueling Q-learning
action: intrusion detection decision for network traffic
eval_setting: not stated
limitation_author: not stated
limitation_inference: evaluation datasets, baselines, and computational cost are unspecified
limitation_unknown: dataset, benchmark, and deployment constraints
support_passage: We study the application of deep learning methods into areas of enterprise/internet network intrusion detection
transfer_ivn: dueling DQN with noisy exploration and prioritized replay could support sequential CAN intrusion detection decisions
transfer_risk: enterprise traffic distributions and label semantics differ from in-vehicle CAN frame behavior

The paper proposes NEXUS-DQN★, a dueling deep Q-network system that unifies noisy exploration and experience prioritization for network traffic intrusion detection. Novelty lies in combining noisy networks with prioritized experience replay inside a dueling Q architecture, rather than treating exploration and sampling efficiency separately.

Deep reinforcement learning for intrusion detection: dueling Q-network architecture, noisy parameter layers for exploration, experience-prioritized replay for sample efficiency, applied to enterprise/internet network traffic classification. Not stated: exact datasets, feature engineering, training schedule, baselines.

Not stated in the provided title and abstract.

Not stated in the provided title and abstract.

[[Concept - Deep Learning Intrusion Detection]]
[[Concept - Network Traffic Dynamics]]
[[Concept - Real-Time Attack Defense]]
[[Concept - Anomaly Detection]]
[[Concept - Edge Security]]

Not stated

Monitoring problem: detecting intrusions in enterprise/internet network traffic. Signal: network traffic features/flow statistics. Uncertainty method: noisy network parameter exploration within dueling Q-learning. Action: classify traffic as intrusive or benign and trigger defense response. Evaluation setting: not stated; presumably benchmark or enterprise network traffic datasets. Transfer to IVN: the dueling DQN with noisy exploration and prioritized replay could be adapted to CAN/automotive intrusion detection where sequential decision-making over traffic frames matters. Transfer risk: enterprise traffic statistics and label semantics differ substantially from CAN frame timing and signal-level behavior, so learned policies may not generalize.

doi: not stated
source_link: not stated
text_kind: title and abstract only
monitoring_problem: enterprise and internet network intrusion detection
signal: network traffic data
uncertainty_method: noisy networks with dueling Q-learning
action: intrusion detection decision for network traffic
eval_setting: not stated
limitation_author: not stated
limitation_inference: evaluation datasets, baselines, and computational cost are unspecified
limitation_unknown: dataset, benchmark, and deployment constraints
support_passage: We study the application of deep learning methods into areas of enterprise/internet network intrusion detection
transfer_ivn: dueling DQN with noisy exploration and prioritized replay could support sequential CAN intrusion detection decisions
transfer_risk: enterprise traffic distributions and label semantics differ from in-vehicle CAN frame behavior

#needs-review

## Record Fields
doi: https://doi.org/10.1007/s10586-026-06526-7
source_link: not stated
text_kind: abstract
monitoring_problem: detecting intrusions in enterprise/internet network traffic. Signal: network traffic features/flow statistics. Uncertainty method: noisy network parameter exploration within dueling Q-learning. Action: classify traffic as intrusive or benign and trigger defense response. Evaluation setting: not stated; presumably benchmark or enterprise network traffic datasets. Transfer to IVN: the dueling DQN with noisy exploration and prioritized replay could be adapted to CAN/automotive intrusion detection where sequential decision-making over traffic frames matters. Transfer risk: enterprise traffic statistics and label semantics differ substantially from CAN frame timing and signal-level behavior, so learned policies may not generalize.
signal: network traffic data
uncertainty_method: noisy networks with dueling Q-learning
action: intrusion detection decision for network traffic
eval_setting: not stated
limitation_author: not stated
limitation_inference: evaluation datasets, baselines, and computational cost are unspecified
limitation_unknown: dataset, benchmark, and deployment constraints
support_passage: We study the application of deep learning methods into areas of enterprise/internet network intrusion detection
transfer_ivn: dueling DQN with noisy exploration and prioritized replay could support sequential CAN intrusion detection decisions
transfer_risk: enterprise traffic distributions and label semantics differ from in-vehicle CAN frame behavior
