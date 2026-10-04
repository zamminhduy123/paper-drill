---
title: "RPPFL: Random Projection-Based Personalized Federated Learning for IoT Intrusion Detection"
year: 2026
doi: "10.1109/COMPSAC69091.2026.00462"
relevance_score: 0.95
type: paper
---
# RPPFL: Random Projection-Based Personalized Federated Learning for IoT Intrusion Detection

## Novelty
The paper proposes RPPFL, a Random Projection-Based Personalized Federated Learning framework for IoT intrusion detection. Its novelty is combining lightweight random projection at IoT devices for privacy and overhead reduction with personalized federated learning at fog nodes for non-IID data, and evaluating privacy resilience using a cGAN-based reconstruction attack.

## Methodology
RPPFL applies random projection to IoT device data before federated training, reducing dimensionality, communication cost, and privacy exposure. Personalized federated learning is performed at the fog layer, using a FedProx-style proximal term to keep local models close to the global model while adapting to heterogeneous non-IID data. A conditional GAN-based attack is introduced to test whether original training data can be reconstructed from projected representations. Experiments are conducted on the RT-IoT 2022 and CIC-IoT 2023 datasets.

## Explicit Limitations
Not stated in the provided excerpt for the proposed RPPFL framework. The excerpt notes limitations of existing FL-based IDS, including performance limitations, high computation and communication overhead, and potential privacy attacks.

## Future Work
Not stated in the provided excerpt.

## Concept Hubs
[[Concept - IoT Intrusion Detection]]
[[Concept - Privacy-Preserving Learning]]
[[Concept - Deep Learning Intrusion Detection]]
[[Concept - Edge AI Inference]]

## Relevance Score
0.95

## Monitoring Transfer
monitoring_problem: IoT network intrusion detection under distributed non-IID data and privacy constraints
signal: projected IoT traffic feature vectors
uncertainty_method: not stated
action: train personalized federated intrusion detection model at fog layer and flag intrusions
eval_setting: RT-IoT 2022 and CIC-IoT 2023 datasets
doi: 10.1109/COMPSAC69091.2026.00462
source_link: https://doi.org/10.1109/COMPSAC69091.2026.00462
text_kind: conference paper
limitation_author: not stated
limitation_inference: cGAN attack evaluates only reconstruction from projected representations and does not cover all federated privacy attacks
limitation_unknown: not stated
support_passage: Experimental results on the RT-IoT 2022 and CIC-IoT 2023 datasets demonstrate that RPPFL provides high detection accuracy (above 95.0%) while preserving data privacy and reducing computation and communication overhead
transfer_ivn: Apply RPPFL to in-vehicle networks by projecting vehicle traffic at edge nodes and training personalized federated intrusion detection at a gateway
transfer_risk: Vehicle network real-time latency and protocol-specific traffic may make random projection and federated aggregation too slow or less effective

#needs-review

## Record Fields
doi: 10.1109/COMPSAC69091.2026.00462
source_link: https://doi.org/10.1109/COMPSAC69091.2026.00462
text_kind: fulltext
monitoring_problem: IoT network intrusion detection under distributed non-IID data and privacy constraints
signal: projected IoT traffic feature vectors
uncertainty_method: not stated
action: train personalized federated intrusion detection model at fog layer and flag intrusions
eval_setting: RT-IoT 2022 and CIC-IoT 2023 datasets
limitation_author: not stated
limitation_inference: cGAN attack evaluates only reconstruction from projected representations and does not cover all federated privacy attacks
limitation_unknown: not stated
support_passage: Experimental results on the RT-IoT 2022 and CIC-IoT 2023 datasets demonstrate that RPPFL provides high detection accuracy (above 95.0%) while preserving data privacy and reducing computation and communication overhead
transfer_ivn: Apply RPPFL to in-vehicle networks by projecting vehicle traffic at edge nodes and training personalized federated intrusion detection at a gateway
transfer_risk: Vehicle network real-time latency and protocol-specific traffic may make random projection and federated aggregation too slow or less effective
