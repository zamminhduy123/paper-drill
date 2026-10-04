---
title: "Opening the Black Box: Cross-Model Explainability Analysis of Deep Learning-Engineered Features in IoT Intrusion Detection"
year: 2026
doi: "10.1109/CoDIT70676.2026.11631031"
relevance_score: 0.95
type: paper
---
# Opening the Black Box: Cross-Model Explainability Analysis of Deep Learning-Engineered Features in IoT Intrusion Detection

## Novelty
- Cross-model explainability analysis of a hybrid deep learning intrusion detection system using SHAP, LIME, and gradient-based methods.
- Quantifies that 32 deep learning-engineered features contribute 93.7% of predictive power, while 46 original network features contribute 6.3%.
- Reports 82.2% Spearman correlation between tree-based and neural network explanations as cross-model validation.
- Introduces attack fingerprinting for eight attack types and concentration analysis showing that 13 deep learning features capture 80% of cumulative importance.

## Methodology
- Uses the CIC-IoT-2023 dataset with 46 original network features and eight traffic categories.
- Stage 1 extracts 32 deep learning-engineered features using an ensemble of Autoencoder, LSTM, and CNN.
- Stage 2 concatenates the 32 engineered features with the 46 original features into a 78-dimensional representation and classifies traffic with XGBoost.
- Applies SHAP TreeExplainer, LIME, and gradient-based explanation methods, then performs cross-model validation, attack fingerprinting, and importance concentration analysis.

## Explicit Limitations
- Not stated in the provided excerpt.
- The authors note that without explainability, models may learn spurious correlations that can fail under distribution shift or adversarial manipulation.

## Future Work
- Not stated in the provided excerpt.

## Concept Hubs
[[Concept - Explainable Intrusion Detection]]
[[Concept - Deep Learning Intrusion Detection]]
[[Concept - IoT Intrusion Detection]]
[[Concept - Network Traffic Analysis]]

## Relevance Score
0.95

## Monitoring Transfer
monitoring_problem: Detect and explain IoT network intrusion alerts across eight traffic categories.
signal: 78-dimensional fused vector of 46 original network features and 32 deep learning-engineered features from Autoencoder, LSTM, and CNN.
uncertainty_method: Cross-model explanation agreement using SHAP TreeExplainer, LIME, gradient-based methods, and Spearman correlation between tree and neural explanations.
action: Classify traffic as benign or attack and provide feature attributions and attack fingerprints for analyst response.
eval_setting: CIC-IoT-2023 dataset with over 46 million flows from 105 heterogeneous IoT devices and eight attack or benign categories.
limitation_author: The model may learn spurious correlations that can fail under distribution shift or adversarial manipulation.
limitation_inference: Explainability analysis does not by itself establish robustness, generalization, or production deployment readiness.
limitation_unknown: Not stated in the provided excerpt.
support_passage: Without explainability, we cannot verify that the model has learned meaningful security-relevant patterns rather than spurious correlations that may fail under distribution shift or adversarial manipulation.
transfer_ivn: Apply the explainable hybrid deep learning and XGBoost intrusion detection pipeline to in-vehicle network traffic, using SHAP and LIME to explain intrusion alerts for CAN or DoIP anomalies.
transfer_risk: IoT traffic features and attack distributions may not match in-vehicle network dynamics, and real-time in-vehicle constraints may limit deep feature extraction and explanation latency.
doi: 10.1109/CoDIT70676.2026.11631031
source_link: not stated
text_kind: conference_paper

#needs-review

## Record Fields
doi: 10.1109/CoDIT70676.2026.11631031
source_link: not stated
text_kind: fulltext
monitoring_problem: Detect and explain IoT network intrusion alerts across eight traffic categories.
signal: 78-dimensional fused vector of 46 original network features and 32 deep learning-engineered features from Autoencoder, LSTM, and CNN.
uncertainty_method: Cross-model explanation agreement using SHAP TreeExplainer, LIME, gradient-based methods, and Spearman correlation between tree and neural explanations.
action: Classify traffic as benign or attack and provide feature attributions and attack fingerprints for analyst response.
eval_setting: CIC-IoT-2023 dataset with over 46 million flows from 105 heterogeneous IoT devices and eight attack or benign categories.
limitation_author: The model may learn spurious correlations that can fail under distribution shift or adversarial manipulation.
limitation_inference: Explainability analysis does not by itself establish robustness, generalization, or production deployment readiness.
limitation_unknown: Not stated in the provided excerpt.
support_passage: Without explainability, we cannot verify that the model has learned meaningful security-relevant patterns rather than spurious correlations that may fail under distribution shift or adversarial manipulation.
transfer_ivn: Apply the explainable hybrid deep learning and XGBoost intrusion detection pipeline to in-vehicle network traffic, using SHAP and LIME to explain intrusion alerts for CAN or DoIP anomalies.
transfer_risk: IoT traffic features and attack distributions may not match in-vehicle network dynamics, and real-time in-vehicle constraints may limit deep feature extraction and explanation latency.
