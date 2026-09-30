---
title: "XP-IDS: an explainable hybrid CNN–XGBoost framework for IoT intrusion detection"
year: 2026
doi: "https://doi.org/10.1038/s41598-026-63304-6"
relevance_score: 9.594000000000001
type: paper
---
# XP-IDS: an explainable hybrid CNN–XGBoost framework for IoT intrusion detection

Novelty

Hybrid architecture combining stacked CNNs for feature extraction with XGBoost classification, applied to IoT intrusion detection on the CIC IoT-DIAD 2024 dataset, with SHAP-based interpretability and a handcrafted feature taxonomy (strategic, time-based, IP-based).

Methodology

Three categories of handcrafted features are extracted: (i) strategic-based features capturing protocol semantics and flow behavior, (ii) time-based features representing sequential relationships and traffic evolution, and (iii) IP-based features characterizing packet-flow communication among IoT endpoints. Stacked CNNs extract feature representations, which are forwarded to an Extreme Gradient Boosting classifier for final prediction. SHAP provides interpretability and overall feature importance. Evaluated on the CIC IoT-DIAD 2024 dataset against multiple baselines.

Explicit Limitations

Not stated by authors.

Future Work

Not stated.

Concept Hubs

[[Concept - IoT Intrusion Detection]]
[[Concept - Deep Learning Intrusion Detection]]
[[Concept - Edge Security]]
[[Concept - Intrinsic Explainability]]
[[Concept - Network Traffic Dynamics]]

doi: not stated
source_link: not stated
text_kind: research paper
monitoring_problem: Detecting anomalous and intrusive network activity in resource-constrained, poorly protected IoT environments
signal: Handcrafted network traffic features (strategic-based, time-based, IP-based) from IoT packet flows
uncertainty_method: SHAP (SHapley Additive exPlanation) for interpretability of model decisions and feature importance
action: Classify traffic as normal or attack and flag intrusions for mitigation
eval_setting: CIC IoT-DIAD 2024 dataset, compared against multiple baseline approaches
limitation_author: not stated
limitation_inference: No explicit limitations stated; potential concerns include dataset-specific evaluation, unclear edge-deployment latency/energy costs, and SHAP overhead on low-power devices
limitation_unknown: Generalization to unseen IoT datasets and real-world deployment constraints; computational cost on edge hardware
support_passage: Using the CIC IoT-DIAD 2024 dataset, XP-IDS learns from three categories of handcrafted features: (i) strategic-based features... (ii) time-based features... (iii) IP-based features... Feature representations extracted through stacked Convolutional Neural Networks are subsequently forwarded to an Extreme Gradient Boosting classifier for final prediction. In addition, SHapley Additive exPlanation (SHAP) is utilized to provide interpretability
transfer_ivn: The hybrid CNN–XGBoost pipeline with SHAP interpretability could be adapted to in-vehicle network intrusion detection using CAN traffic features (e.g., timing, ID-based, and payload-derived features) fed to the same stacked CNN plus gradient boosting classifier
transfer_risk: CAN bus traffic differs fundamentally from IoT IP-based traffic in protocol structure, feature semantics, and timing behavior, so handcrafted feature categories (strategic, time-based, IP-based) may not map cleanly and could degrade detection performance without redesign

Hybrid architecture combining stacked CNNs for feature extraction with XGBoost classification, applied to IoT intrusion detection on the CIC IoT-DIAD 2024 dataset, with SHAP-based interpretability and a handcrafted feature taxonomy (strategic, time-based, IP-based).

Three categories of handcrafted features are extracted: (i) strategic-based features capturing protocol semantics and flow behavior, (ii) time-based features representing sequential relationships and traffic evolution, and (iii) IP-based features characterizing packet-flow communication among IoT endpoints. Stacked CNNs extract feature representations, which are forwarded to an Extreme Gradient Boosting classifier for final prediction. SHAP provides interpretability and overall feature importance. Evaluated on the CIC IoT-DIAD 2024 dataset against multiple baselines.

Not stated by authors.

Not stated.

[[Concept - IoT Intrusion Detection]]
[[Concept - Deep Learning Intrusion Detection]]
[[Concept - Edge Security]]
[[Concept - Intrinsic Explainability]]
[[Concept - Network Traffic Dynamics]]

doi: not stated
source_link: not stated
text_kind: research paper
monitoring_problem: Detecting anomalous and intrusive network activity in resource-constrained, poorly protected IoT environments
signal: Handcrafted network traffic features (strategic-based, time-based, IP-based) from IoT packet flows
uncertainty_method: SHAP (SHapley Additive exPlanation) for interpretability of model decisions and feature importance
action: Classify traffic as normal or attack and flag intrusions for mitigation
eval_setting: CIC IoT-DIAD 2024 dataset, compared against multiple baseline approaches
limitation_author: not stated
limitation_inference: No explicit limitations stated; potential concerns include dataset-specific evaluation, unclear edge-deployment latency/energy costs, and SHAP overhead on low-power devices
limitation_unknown: Generalization to unseen IoT datasets and real-world deployment constraints; computational cost on edge hardware
support_passage: Using the CIC IoT-DIAD 2024 dataset, XP-IDS learns from three categories of handcrafted features: (i) strategic-based features... (ii) time-based features... (iii) IP-based features... Feature representations extracted through stacked Convolutional Neural Networks are subsequently forwarded to an Extreme Gradient Boosting classifier for final prediction. In addition, SHapley Additive exPlanation (SHAP) is utilized to provide interpretability
transfer_ivn: The hybrid CNN–XGBoost pipeline with SHAP interpretability could be adapted to in-vehicle network intrusion detection using CAN traffic features (e.g., timing, ID-based, and payload-derived features) fed to the same stacked CNN plus gradient boosting classifier
transfer_risk: CAN bus traffic differs fundamentally from IoT IP-based traffic in protocol structure, feature semantics, and timing behavior, so handcrafted feature categories (strategic, time-based, IP-based) may not map cleanly and could degrade detection performance without redesign

#needs-review

## Record Fields
doi: https://doi.org/10.1038/s41598-026-63304-6
source_link: not stated
text_kind: abstract
monitoring_problem: Detecting anomalous and intrusive network activity in resource-constrained, poorly protected IoT environments
signal: Handcrafted network traffic features (strategic-based, time-based, IP-based) from IoT packet flows
uncertainty_method: SHAP (SHapley Additive exPlanation) for interpretability of model decisions and feature importance
action: Classify traffic as normal or attack and flag intrusions for mitigation
eval_setting: CIC IoT-DIAD 2024 dataset, compared against multiple baseline approaches
limitation_author: not stated
limitation_inference: No explicit limitations stated; potential concerns include dataset-specific evaluation, unclear edge-deployment latency/energy costs, and SHAP overhead on low-power devices
limitation_unknown: Generalization to unseen IoT datasets and real-world deployment constraints; computational cost on edge hardware
support_passage: Using the CIC IoT-DIAD 2024 dataset, XP-IDS learns from three categories of handcrafted features: (i) strategic-based features... (ii) time-based features... (iii) IP-based features... Feature representations extracted through stacked Convolutional Neural Networks are subsequently forwarded to an Extreme Gradient Boosting classifier for final prediction. In addition, SHapley Additive exPlanation (SHAP) is utilized to provide interpretability
transfer_ivn: The hybrid CNN–XGBoost pipeline with SHAP interpretability could be adapted to in-vehicle network intrusion detection using CAN traffic features (e.g., timing, ID-based, and payload-derived features) fed to the same stacked CNN plus gradient boosting classifier
transfer_risk: CAN bus traffic differs fundamentally from IoT IP-based traffic in protocol structure, feature semantics, and timing behavior, so handcrafted feature categories (strategic, time-based, IP-based) may not map cleanly and could degrade detection performance without redesign
