---
title: "Relational Modeling for Automotive Cybersecurity: Structural Transition and Graph Topology-Based CAN Intrusion Detection"
year: 2026
doi: "https://doi.org/10.20944/preprints202603.1899.v1"
relevance_score: 0.6
type: paper
---
# Relational Modeling for Automotive Cybersecurity: Structural Transition and Graph Topology-Based CAN Intrusion Detection

## Novelty
The paper proposes a lightweight CAN intrusion detection approach that combines statistical traffic descriptors, structural identifier transition features, and graph topology representations to capture relational dependencies between CAN messages. It shows that relational features improve robustness across attack types, especially when statistical features fail under cross-attack transfer.

## Methodology
The authors build a CAN intrusion detection system using CAN communication windows. Features include statistical traffic descriptors, structural identifier transition features, and graph topology representations. They evaluate the approach on the HCRL Car-Hacking and ROAD datasets using multiple machine learning classifiers, including logistic regression, support vector machines, random forests, gradient boosting, decision trees, and k-nearest neighbors.

## Explicit Limitations
Statistical features are highly effective for DoS attacks but nearly useless for spoofing attacks such as RPM manipulation when the model is trained on DoS attacks. Decision tree classifiers exhibited instability when combined with hybrid feature representations.

## Future Work
not stated

## Concept Hubs
[[Concept - CAN Intrusion Detection]]
[[Concept - In-Vehicle Network Security]]
[[Concept - Network Traffic Analysis]]
[[Concept - Lightweight Detection]]
[[Concept - Cross-Dataset Evaluation]]

## Relevance Score
0.6

## Monitoring Transfer
doi: not stated
source_link: not stated
text_kind: abstract
monitoring_problem: detect CAN intrusions robustly across DoS and spoofing attacks
signal: statistical traffic descriptors, structural identifier transition features, and graph topology representations of CAN communication windows
uncertainty_method: not stated
action: classify CAN traffic as normal or malicious
eval_setting: HCRL Car-Hacking and ROAD datasets; cross-attack transfer from DoS-trained models to spoofing/RPM manipulation; multiple classifiers
limitation_author: statistical features are nearly useless for spoofing attacks when training data is based on DoS attacks; decision tree classifiers exhibited instability with hybrid features
limitation_inference: graph topology construction and relational feature extraction may be vehicle-specific and may not scale to larger or heterogeneous IVN topologies
limitation_unknown: not stated
support_passage: "structural transition features and graph topology representations provide consistently high levels of detection effectiveness across all types of attacks tested"
transfer_ivn: apply relational CAN message transition and graph topology features to IVN intrusion detection for cross-attack generalization
transfer_risk: graph topology and identifier transition features may be vehicle-specific and degrade when CAN topology, message IDs, or attack distributions shift

#needs-review

## Record Fields
doi: https://doi.org/10.20944/preprints202603.1899.v1
source_link: not stated
text_kind: abstract
monitoring_problem: detect CAN intrusions robustly across DoS and spoofing attacks
signal: statistical traffic descriptors, structural identifier transition features, and graph topology representations of CAN communication windows
uncertainty_method: not stated
action: classify CAN traffic as normal or malicious
eval_setting: HCRL Car-Hacking and ROAD datasets; cross-attack transfer from DoS-trained models to spoofing/RPM manipulation; multiple classifiers
limitation_author: statistical features are nearly useless for spoofing attacks when training data is based on DoS attacks; decision tree classifiers exhibited instability with hybrid features
limitation_inference: graph topology construction and relational feature extraction may be vehicle-specific and may not scale to larger or heterogeneous IVN topologies
limitation_unknown: not stated
support_passage: "structural transition features and graph topology representations provide consistently high levels of detection effectiveness across all types of attacks tested"
transfer_ivn: apply relational CAN message transition and graph topology features to IVN intrusion detection for cross-attack generalization
transfer_risk: graph topology and identifier transition features may be vehicle-specific and degrade when CAN topology, message IDs, or attack distributions shift
