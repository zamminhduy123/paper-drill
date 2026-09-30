---
title: "kvsambasivarao/Dataset-repository: Multi-Class Severity-Annotated Controller Area Network (CAN) Dataset for Intrusion Detection"
year: 2026
doi: "https://doi.org/10.5281/zenodo.21503517"
relevance_score: 3.6919999999999997
type: paper
---
# kvsambasivarao/Dataset-repository: Multi-Class Severity-Annotated Controller Area Network (CAN) Dataset for Intrusion Detection

Novelty

A simulated CAN bus dataset that combines normal traffic with nine representative cyberattack categories, and uniquely annotates every frame with a four-level severity class (Low, Medium, High, Critical), enabling joint intrusion detection and attack severity/risk prioritization.

Methodology

Insights were integrated from multiple publicly available CAN intrusion detection datasets, and representative attack scenarios from the literature were incorporated to build a research-grade simulated CAN bus dataset. Normal CAN traffic is combined with nine representative cyberattack categories; each frame receives both an attack label and a four-level severity annotation. The dataset is released publicly via a GitHub repository commit for reproducible benchmarking of machine learning and deep learning models for intrusion detection, attack classification, and cyber-risk prioritization.

Explicit Limitations

* CAN IDs, message formats, and communication characteristics vary considerably across vehicle manufacturers and models, so a single real-world dataset cannot represent all possible CAN traffic patterns.

* The dataset is simulated and intended to capture structure, behavior, and characteristics of CAN communication under normal and malicious conditions rather than replicate any specific manufacturer's proprietary CAN database.

* Intended exclusively for academic research, benchmarking, algorithm development, and educational purposes.

Future Work

Not stated.

Concept Hubs

[[Concept - CAN Intrusion Detection]]
[[Concept - In-Vehicle Network Security]]
[[Concept - Deep Learning Intrusion Detection]]
[[Concept - Benchmark Stress Testing]]
[[Concept - Multi-Agent Security Evaluation]]

Relevance Score

High — the dataset directly targets in-vehicle network intrusion detection with multi-class attack and severity labels for training and evaluating deep learning models.

Monitoring Transfer

The dataset frames CAN traffic monitoring as a classification problem: each frame is a signal to be labeled as normal or one of nine attacks and assigned a severity level, with evaluation as benchmarking of ML/DL intrusion detection, attack classification, and risk prioritization. Transfer to IVN is direct because the dataset is itself CAN bus data for in-vehicle networks. The transfer may fail because the simulated traffic is not tied to any specific manufacturer's proprietary CAN database, so CAN ID and message-format distributions may not match real vehicle deployments.

doi: not stated
source_link: https://github.com/kvsambasivarao/Dataset-repository/commit/f274293fa9fc89b8e733a79d368f44fb00aa5293
text_kind: dataset description
monitoring_problem: intrusion detection and attack severity assessment in in-vehicle CAN networks
signal: CAN frames with CAN IDs and message formats
uncertainty_method: not stated
action: attack detection, attack classification, and cyber-risk prioritization
eval_setting: benchmarking of machine learning and deep learning models on a simulated CAN bus dataset with nine attack categories and four severity levels
limitation_author: simulated dataset cannot replicate any specific vehicle manufacturer's proprietary CAN database; CAN characteristics vary across manufacturers and models
limitation_inference: simulated CAN ID and message-format distributions may not generalize to real vehicle deployments
limitation_unknown: exact simulation fidelity, attack injection parameters, and class balance are not described
support_passage: The dataset includes normal CAN traffic together with Nine representative cyberattack categories commonly investigated in automotive security research. In addition to attack labels, each CAN frame is annotated with a four-level severity classification (Low, Medium, High, and Critical), enabling both attack detection and attack severity assessment.
transfer_ivn: dataset is native CAN bus data for in-vehicle networks, directly usable for IVN intrusion detection research
transfer_risk: simulated traffic not tied to any manufacturer's proprietary CAN database may not match real CAN ID and message-format distributions

A simulated CAN bus dataset that combines normal traffic with nine representative cyberattack categories, and uniquely annotates every frame with a four-level severity class (Low, Medium, High, Critical), enabling joint intrusion detection and attack severity/risk prioritization.

Insights were integrated from multiple publicly available CAN intrusion detection datasets, and representative attack scenarios from the literature were incorporated to build a research-grade simulated CAN bus dataset. Normal CAN traffic is combined with nine representative cyberattack categories; each frame receives both an attack label and a four-level severity annotation. The dataset is released publicly via a GitHub repository commit for reproducible benchmarking of machine learning and deep learning models for intrusion detection, attack classification, and cyber-risk prioritization.

CAN IDs, message formats, and communication characteristics vary considerably across vehicle manufacturers and models, so a single real-world dataset cannot represent all possible CAN traffic patterns.

The dataset is simulated and intended to capture structure, behavior, and characteristics of CAN communication under normal and malicious conditions rather than replicate any specific manufacturer's proprietary CAN database.

Intended exclusively for academic research, benchmarking, algorithm development, and educational purposes.

Not stated.

[[Concept - CAN Intrusion Detection]]
[[Concept - In-Vehicle Network Security]]
[[Concept - Deep Learning Intrusion Detection]]
[[Concept - Benchmark Stress Testing]]
[[Concept - Multi-Agent Security Evaluation]]

High — the dataset directly targets in-vehicle network intrusion detection with multi-class attack and severity labels for training and evaluating deep learning models.

The dataset frames CAN traffic monitoring as a classification problem: each frame is a signal to be labeled as normal or one of nine attacks and assigned a severity level, with evaluation as benchmarking of ML/DL intrusion detection, attack classification, and risk prioritization. Transfer to IVN is direct because the dataset is itself CAN bus data for in-vehicle networks. The transfer may fail because the simulated traffic is not tied to any specific manufacturer's proprietary CAN database, so CAN ID and message-format distributions may not match real vehicle deployments.

doi: not stated
source_link: https://github.com/kvsambasivarao/Dataset-repository/commit/f274293fa9fc89b8e733a79d368f44fb00aa5293
text_kind: dataset description
monitoring_problem: intrusion detection and attack severity assessment in in-vehicle CAN networks
signal: CAN frames with CAN IDs and message formats
uncertainty_method: not stated
action: attack detection, attack classification, and cyber-risk prioritization
eval_setting: benchmarking of machine learning and deep learning models on a simulated CAN bus dataset with nine attack categories and four severity levels
limitation_author: simulated dataset cannot replicate any specific vehicle manufacturer's proprietary CAN database; CAN characteristics vary across manufacturers and models
limitation_inference: simulated CAN ID and message-format distributions may not generalize to real vehicle deployments
limitation_unknown: exact simulation fidelity, attack injection parameters, and class balance are not described
support_passage: The dataset includes normal CAN traffic together with Nine representative cyberattack categories commonly investigated in automotive security research. In addition to attack labels, each CAN frame is annotated with a four-level severity classification (Low, Medium, High, and Critical), enabling both attack detection and attack severity assessment.
transfer_ivn: dataset is native CAN bus data for in-vehicle networks, directly usable for IVN intrusion detection research
transfer_risk: simulated traffic not tied to any manufacturer's proprietary CAN database may not match real CAN ID and message-format distributions

#needs-review

## Record Fields
doi: https://doi.org/10.5281/zenodo.21503517
source_link: https://github.com/kvsambasivarao/Dataset-repository/commit/f274293fa9fc89b8e733a79d368f44fb00aa5293
text_kind: abstract
monitoring_problem: intrusion detection and attack severity assessment in in-vehicle CAN networks
signal: CAN frames with CAN IDs and message formats
uncertainty_method: not stated
action: attack detection, attack classification, and cyber-risk prioritization
eval_setting: benchmarking of machine learning and deep learning models on a simulated CAN bus dataset with nine attack categories and four severity levels
limitation_author: simulated dataset cannot replicate any specific vehicle manufacturer's proprietary CAN database; CAN characteristics vary across manufacturers and models
limitation_inference: simulated CAN ID and message-format distributions may not generalize to real vehicle deployments
limitation_unknown: exact simulation fidelity, attack injection parameters, and class balance are not described
support_passage: The dataset includes normal CAN traffic together with Nine representative cyberattack categories commonly investigated in automotive security research. In addition to attack labels, each CAN frame is annotated with a four-level severity classification (Low, Medium, High, and Critical), enabling both attack detection and attack severity assessment.
transfer_ivn: dataset is native CAN bus data for in-vehicle networks, directly usable for IVN intrusion detection research
transfer_risk: simulated traffic not tied to any manufacturer's proprietary CAN database may not match real CAN ID and message-format distributions
