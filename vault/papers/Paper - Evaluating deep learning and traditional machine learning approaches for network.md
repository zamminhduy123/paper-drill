---
title: "Evaluating deep learning and traditional machine learning approaches for network intrusion detection"
year: 2026
doi: "https://doi.org/10.14457/tu.the.2025.519"
relevance_score: 9.674
type: paper
---
# Evaluating deep learning and traditional machine learning approaches for network intrusion detection

Novelty

Systematic evaluation of traditional ML, DL, and hybrid DL variants (RF, DT, SVM, KNN, DNN, CNN, LSTM, CNN-LSTM, AE-LSTM) across two structurally distinct flow-based tabular benchmarks (CIC-IDS2017, BCCC-CIC-IDS-2017) under four data-balancing pipelines (P1_None, P2_SMOTE, P3_SMOTE_Tomek, P4_RUS_50) with Stratified 5-Fold Cross-Validation and leakage-safe preprocessing confined to training partitions. Demonstrates that tree-based ensembles (Random Forest) outperform heavier deep learning architectures on flat engineered flow features, evidencing diminishing returns from model complexity in tabular NIDS.

Methodology

* Two flow-based tabular benchmarks: CIC-IDS2017 and BCCC-CIC-IDS-2017.

* Four data-balancing pipelines: P1_None, P2_SMOTE, P3_SMOTE_Tomek, P4_RUS_50.

* Stratified 5-Fold Cross-Validation with preprocessing strictly confined to training partition to prevent data leakage.

* Model matrix: Random Forest, Decision Tree, SVM, KNN, DNN, CNN, LSTM, CNN-LSTM, AE-LSTM.

* Comparative assessment of accuracy, equilibrium metrics, and training efficiency.

Explicit Limitations

* Evaluated only on tabular flow-based features, not raw packet or payload data.

* Reliance on existing datasets (CIC-IDS2017, BCCC-CIC-IDS-2017) noted as an obstacle in current research.

* Deep learning variants incurred extreme computational costs without exceeding baseline thresholds.

* Diminishing returns observed for model complexity in tabular NIDS settings.

* Class imbalance remains a structural challenge (highly skewed distributions favoring benign traffic).

Future Work

Not stated.

Concept Hubs

[[Concept - Deep Learning Intrusion Detection]]
[[Concept - Anomaly Detection]]
[[Concept - Data Leakage Prevention]]
[[Concept - SMOTE Oversampling]]
[[Concept - Benchmark Stress Testing]]

Relevance Score

Not stated.

Monitoring Transfer

Monitoring problem: Network intrusion detection under highly skewed traffic distributions, outdated datasets, and heavy neural processing overhead.
Signal: Flow-based tabular network traffic features from CIC-IDS2017 and BCCC-CIC-IDS-2017.
Uncertainty method: Comparative evaluation across ML/DL/hybrid architectures and four data-balancing pipelines with cross-validation.
Action: Selection of Random Forest as the most viable operational strategy for tabular NIDS.
Evaluation setting: Stratified 5-Fold Cross-Validation on two flow-based tabular benchmarks.

Transfer to IVN: Tree-based ensemble detection (e.g., Random Forest) applied to in-vehicle network flow features for intrusion detection.

Transfer risk: Flow-based tabular benchmarks (CIC-IDS2017, BCCC-CIC-IDS-2017) lack CAN bus timing, priority arbitration, and physical signal semantics, so benign traffic distributions and attack signatures may not align with IVN characteristics.

doi: not stated
source_link: not stated
text_kind: not stated
monitoring_problem: Network intrusion detection under highly skewed traffic distributions, outdated datasets, and heavy neural processing overhead
signal: Flow-based tabular network traffic features from CIC-IDS2017 and BCCC-CIC-IDS-2017
uncertainty_method: Comparative evaluation across ML/DL/hybrid architectures and four data-balancing pipelines with Stratified 5-Fold Cross-Validation
action: Selection of Random Forest as the most viable operational strategy for tabular NIDS
eval_setting: Stratified 5-Fold Cross-Validation on two flow-based tabular benchmarks (CIC-IDS2017, BCCC-CIC-IDS-2017)
limitation_author: Not stated
limitation_inference: Evaluation restricted to tabular flow features and legacy datasets; no raw packet, payload, or IVN-specific signal validation
limitation_unknown: Whether findings generalize to non-tabular, time-series, or in-vehicle network domains
support_passage: Empirical outcomes indicate that for flat, engineered flow features, Random Forest outpaces competing architectures by delivering the highest equilibrium between metric accuracy and training efficiency.
transfer_ivn: Tree-based ensemble detection (e.g., Random Forest) applied to in-vehicle network flow features for intrusion detection
transfer_risk: Flow-based tabular benchmarks lack CAN bus timing, priority arbitration, and physical signal semantics, so benign traffic distributions and attack signatures may not align with IVN characteristics

Systematic evaluation of traditional ML, DL, and hybrid DL variants (RF, DT, SVM, KNN, DNN, CNN, LSTM, CNN-LSTM, AE-LSTM) across two structurally distinct flow-based tabular benchmarks (CIC-IDS2017, BCCC-CIC-IDS-2017) under four data-balancing pipelines (P1_None, P2_SMOTE, P3_SMOTE_Tomek, P4_RUS_50) with Stratified 5-Fold Cross-Validation and leakage-safe preprocessing confined to training partitions. Demonstrates that tree-based ensembles (Random Forest) outperform heavier deep learning architectures on flat engineered flow features, evidencing diminishing returns from model complexity in tabular NIDS.

Two flow-based tabular benchmarks: CIC-IDS2017 and BCCC-CIC-IDS-2017.

Four data-balancing pipelines: P1_None, P2_SMOTE, P3_SMOTE_Tomek, P4_RUS_50.

Stratified 5-Fold Cross-Validation with preprocessing strictly confined to training partition to prevent data leakage.

Model matrix: Random Forest, Decision Tree, SVM, KNN, DNN, CNN, LSTM, CNN-LSTM, AE-LSTM.

Comparative assessment of accuracy, equilibrium metrics, and training efficiency.

Evaluated only on tabular flow-based features, not raw packet or payload data.

Reliance on existing datasets (CIC-IDS2017, BCCC-CIC-IDS-2017) noted as an obstacle in current research.

Deep learning variants incurred extreme computational costs without exceeding baseline thresholds.

Diminishing returns observed for model complexity in tabular NIDS settings.

Class imbalance remains a structural challenge (highly skewed distributions favoring benign traffic).

Not stated.

[[Concept - Deep Learning Intrusion Detection]]
[[Concept - Anomaly Detection]]
[[Concept - Data Leakage Prevention]]
[[Concept - SMOTE Oversampling]]
[[Concept - Benchmark Stress Testing]]

Not stated.

Monitoring problem: Network intrusion detection under highly skewed traffic distributions, outdated datasets, and heavy neural processing overhead.
Signal: Flow-based tabular network traffic features from CIC-IDS2017 and BCCC-CIC-IDS-2017.
Uncertainty method: Comparative evaluation across ML/DL/hybrid architectures and four data-balancing pipelines with cross-validation.
Action: Selection of Random Forest as the most viable operational strategy for tabular NIDS.
Evaluation setting: Stratified 5-Fold Cross-Validation on two flow-based tabular benchmarks.

Transfer to IVN: Tree-based ensemble detection (e.g., Random Forest) applied to in-vehicle network flow features for intrusion detection.

Transfer risk: Flow-based tabular benchmarks (CIC-IDS2017, BCCC-CIC-IDS-2017) lack CAN bus timing, priority arbitration, and physical signal semantics, so benign traffic distributions and attack signatures may not align with IVN characteristics.

doi: not stated
source_link: not stated
text_kind: not stated
monitoring_problem: Network intrusion detection under highly skewed traffic distributions, outdated datasets, and heavy neural processing overhead
signal: Flow-based tabular network traffic features from CIC-IDS2017 and BCCC-CIC-IDS-2017
uncertainty_method: Comparative evaluation across ML/DL/hybrid architectures and four data-balancing pipelines with Stratified 5-Fold Cross-Validation
action: Selection of Random Forest as the most viable operational strategy for tabular NIDS
eval_setting: Stratified 5-Fold Cross-Validation on two flow-based tabular benchmarks (CIC-IDS2017, BCCC-CIC-IDS-2017)
limitation_author: Not stated
limitation_inference: Evaluation restricted to tabular flow features and legacy datasets; no raw packet, payload, or IVN-specific signal validation
limitation_unknown: Whether findings generalize to non-tabular, time-series, or in-vehicle network domains
support_passage: Empirical outcomes indicate that for flat, engineered flow features, Random Forest outpaces competing architectures by delivering the highest equilibrium between metric accuracy and training efficiency.
transfer_ivn: Tree-based ensemble detection (e.g., Random Forest) applied to in-vehicle network flow features for intrusion detection
transfer_risk: Flow-based tabular benchmarks lack CAN bus timing, priority arbitration, and physical signal semantics, so benign traffic distributions and attack signatures may not align with IVN characteristics

#needs-review

## Record Fields
doi: https://doi.org/10.14457/tu.the.2025.519
source_link: not stated
text_kind: abstract
monitoring_problem: Network intrusion detection under highly skewed traffic distributions, outdated datasets, and heavy neural processing overhead.
signal: Flow-based tabular network traffic features from CIC-IDS2017 and BCCC-CIC-IDS-2017.
uncertainty_method: Comparative evaluation across ML/DL/hybrid architectures and four data-balancing pipelines with cross-validation.
action: Selection of Random Forest as the most viable operational strategy for tabular NIDS.
eval_setting: Stratified 5-Fold Cross-Validation on two flow-based tabular benchmarks (CIC-IDS2017, BCCC-CIC-IDS-2017)
limitation_author: Not stated
limitation_inference: Evaluation restricted to tabular flow features and legacy datasets; no raw packet, payload, or IVN-specific signal validation
limitation_unknown: Whether findings generalize to non-tabular, time-series, or in-vehicle network domains
support_passage: Empirical outcomes indicate that for flat, engineered flow features, Random Forest outpaces competing architectures by delivering the highest equilibrium between metric accuracy and training efficiency.
transfer_ivn: Tree-based ensemble detection (e.g., Random Forest) applied to in-vehicle network flow features for intrusion detection
transfer_risk: Flow-based tabular benchmarks (CIC-IDS2017, BCCC-CIC-IDS-2017) lack CAN bus timing, priority arbitration, and physical signal semantics, so benign traffic distributions and attack signatures may not align with IVN characteristics.
