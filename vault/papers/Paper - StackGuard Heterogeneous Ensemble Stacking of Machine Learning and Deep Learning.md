---
title: "StackGuard: Heterogeneous Ensemble Stacking of Machine Learning and Deep Learning Paradigms for Industrial IoT Intrusion Detection"
year: 2026
doi: "10.1109/eSmarTA70636.2026.11652363"
relevance_score: 9.731
type: paper
---
# StackGuard: Heterogeneous Ensemble Stacking of Machine Learning and Deep Learning Paradigms for Industrial IoT Intrusion Detection

Novelty

The paper introduces StackGuard, a triple hybrid stacking architecture that jointly integrates Random Forest, CNN, and DNN as heterogeneous base learners with a Random Forest meta-classifier trained on held-out prediction probabilities, addressing a gap where prior IIoT IDS work evaluated these paradigms only in isolation or pairwise combinations. It further contributes a two-level data-splitting strategy that separates base and meta training subsets to prevent data leakage and ensure unbiased meta-classifier training, alongside a six-configuration ablation study on the X-IIoTID benchmark.

Methodology

The authors formulate intrusion detection as a binary classification problem (Normal=0, Attack=1) decomposed into a two-stage stacking procedure: ŷ = f_meta(f_RF(x), f_CNN(x), f_DNN(x)), where f_RF, f_CNN, and f_DNN produce attack-class probabilities and f_meta is a Random Forest meta-classifier trained on their concatenated outputs. Experiments use the X-IIoTID dataset (>800,000 records, 73 numerical features after preprocessing, binary target "class3", 80/20 train/test split, 164,167 test samples). Preprocessing involves four steps: feature removal (timestamps, IP addresses to prevent identity-based leakage), one-hot categorical encoding (protocol, service, state), missing value imputation (zero), and StandardScaler feature scaling fit on train only. A rigorous two-level data-splitting strategy separates base and meta training subsets via stratified sub-split. Evaluation spans six model configurations: Decision Tree, Logistic Regression, Random Forest, CNN, DNN, and a two-stage CNN–RF hybrid, compared against state-of-the-art IIoT IDS methods including CNN–LSTM (98.84%). Threshold optimization at τ*=0.53 refines the precision–recall trade-off.

Explicit Limitations

The provided text is truncated and does not contain a dedicated limitations section. The abstract and introduction do not explicitly state limitations of the proposed StackGuard framework. The related work notes that CNN and DNN architectures "require substantial computational resources and large-scale training data," and that traditional ML approaches "depend heavily on manual feature selection and degrade under class imbalance and distributional shift," but these are characterizations of prior paradigms rather than explicitly acknowledged limitations of StackGuard itself. No author-stated limitations are present in the available text.

Future Work

Not stated in the provided text. The conclusion (Section V) is referenced in the paper organization but its content is not included in the truncated output.

Concept Hubs

[[Concept - Stacking Ensemble]]
[[Concept - Heterogeneous Base Learners]]
[[Concept - Data Leakage Prevention]]
[[Concept - Meta-Classifier]]
[[Concept - IIoT Intrusion Detection]]

Relevance Score

Not stated

Monitoring Transfer

Monitoring problem: Cyberattacks targeting Industrial IoT environments, including DoS/DDoS, malware, ransomware, MITM, and unauthorized access, exploiting weaknesses such as heterogeneous devices and limited resources. Signal: Network traffic records containing packet statistics, byte counts, connection duration, and system activity indicators from the X-IIoTID dataset (>800,000 records, 73 numerical features). Uncertainty method: Stacking-based meta-learning where RF, CNN, and DNN base learners produce attack-class probabilities, and a Random Forest meta-classifier trained on held-out prediction probabilities produces the final decision; threshold optimization at τ*=0.53 refines the precision–recall trade-off. Resulting action: Binary classification of each network traffic record as Normal (0) or Attack (1), enabling intrusion detection in IIoT environments. Evaluation setting: X-IIoTID benchmark dataset with 80/20 train/test split (164,167 test samples), two-level data-splitting separating base and meta training subsets, six model configurations ablated (Decision Tree, Logistic Regression, Random Forest, CNN, DNN, CNN–RF hybrid), compared against state-of-the-art including CNN–LSTM (98.84%), achieving 99.76% accuracy, precision 0.9984, recall 0.9967, F1-score 0.9975, ROC-AUC 0.9999.

One transfer to IVN: The heterogeneous stacking paradigm combining Random Forest, CNN, and DNN base learners with a meta-classifier could be adapted to in-vehicle network intrusion detection, where CAN bus traffic records (analogous to IIoT network traffic records) could be classified as normal or attack, with the meta-classifier learning to combine complementary strengths of tree-based methods on structured tabular CAN features and deep learning methods on temporal/sequential CAN signal patterns.

One reason the transfer may fail: CAN bus networks have fundamentally different characteristics from IIoT networks, including extremely constrained message sizes (8 bytes typical), hard real-time requirements, deterministic broadcast communication without IP addresses or protocols, and a much smaller feature space, which may render the 73-feature preprocessing pipeline and the computational overhead of a triple-model stacking ensemble impractical for resource-constrained in-vehicle electronic control units.

doi: 10.1109/eSmarTA70636.2026.11652363
source_link: Not stated
text_kind: Conference paper (2026 6th International Conference on Emerging Smart Technologies and Applications, eSmarTA)
monitoring_problem: Cyberattacks targeting Industrial IoT environments (DoS/DDoS, malware, ransomware, MITM, unauthorized access) exploiting heterogeneous devices and limited resources, where signature-based IDS fail against zero-day and adaptive threats
signal: Network traffic records from X-IIoTID dataset (>800,000 records, 73 numerical features after preprocessing) containing packet statistics, byte counts, connection duration, and system activity indicators
uncertainty_method: Stacking ensemble with Random Forest, CNN, and DNN base learners producing attack-class probabilities, combined by a Random Forest meta-classifier trained on held-out prediction probabilities; threshold optimization at τ =0.53; two-level data-splitting to prevent data leakage
action: Binary classification of each network traffic record as Normal (0) or Attack (1) for IIoT intrusion detection
eval_setting: X-IIoTID benchmark dataset, 80/20 train/test split (164,167 test samples), six model configurations ablated (Decision Tree, Logistic Regression, Random Forest, CNN, DNN, CNN–RF hybrid), compared against state-of-the-art including CNN–LSTM (98.84%), achieving 99.76% accuracy, precision 0.9984, recall 0.9967, F1-score 0.9975, ROC-AUC 0.9999
limitation_author: Not stated
limitation_inference: The triple-model stacking architecture with a meta-classifier introduces substantial computational overhead and latency, which may be impractical for resource-constrained IIoT edge devices; the study evaluates on a single benchmark dataset (X-IIoTID) without cross-dataset validation, raising generalizability concerns; the binary classification formulation collapses multi-class attack types into a single "Attack" category, losing granularity for threat-specific response
limitation_unknown: Whether the two-level data-splitting strategy introduces sufficient meta-training data after stratified sub-splitting of the training set; the exact computational cost and inference latency of the full StackGuard pipeline; performance under concept drift or adversarial evasion targeting the stacking ensemble; whether threshold τ =0.53 is dataset-specific or generalizable
support_passage: "StackGuard achieves 99.76% accuracy, precision of 0.9984, recall of 0.9967, F1-score of 0.9975, and ROC-AUC of 0.9999, surpassing all evaluated baselines by at least 0.92 percentage points. Threshold optimization at τ* = 0.53 further refines the precision–recall trade-off, yielding a peak F1-score of 0.9979."
transfer_ivn: Heterogeneous stacking of Random Forest, CNN, and DNN base learners with a meta-classifier could be adapted to CAN bus intrusion detection, where tree-based methods capture structured tabular CAN ID/feature patterns and deep learning captures temporal signal sequences, with the meta-classifier combining complementary strengths
transfer_risk: CAN bus networks have fundamentally different characteristics from IIoT networks—extremely constrained 8-byte messages, hard real-time requirements, deterministic broadcast communication without IP addresses or protocols, and much smaller feature space—which may render the 73-feature preprocessing pipeline and triple-model stacking computational overhead impractical for resource-constrained in-vehicle ECUs

The paper introduces StackGuard, a triple hybrid stacking architecture that jointly integrates Random Forest, CNN, and DNN as heterogeneous base learners with a Random Forest meta-classifier trained on held-out prediction probabilities, addressing a gap where prior IIoT IDS work evaluated these paradigms only in isolation or pairwise combinations. It further contributes a two-level data-splitting strategy that separates base and meta training subsets to prevent data leakage and ensure unbiased meta-classifier training, alongside a six-configuration ablation study on the X-IIoTID benchmark.

The authors formulate intrusion detection as a binary classification problem (Normal=0, Attack=1) decomposed into a two-stage stacking procedure: ŷ = f_meta(f_RF(x), f_CNN(x), f_DNN(x)), where f_RF, f_CNN, and f_DNN produce attack-class probabilities and f_meta is a Random Forest meta-classifier trained on their concatenated outputs. Experiments use the X-IIoTID dataset (>800,000 records, 73 numerical features after preprocessing, binary target "class3", 80/20 train/test split, 164,167 test samples). Preprocessing involves four steps: feature removal (timestamps, IP addresses to prevent identity-based leakage), one-hot categorical encoding (protocol, service, state), missing value imputation (zero), and StandardScaler feature scaling fit on train only. A rigorous two-level data-splitting strategy separates base and meta training subsets via stratified sub-split. Evaluation spans six model configurations: Decision Tree, Logistic Regression, Random Forest, CNN, DNN, and a two-stage CNN–RF hybrid, compared against state-of-the-art IIoT IDS methods including CNN–LSTM (98.84%). Threshold optimization at τ*=0.53 refines the precision–recall trade-off.

The provided text is truncated and does not contain a dedicated limitations section. The abstract and introduction do not explicitly state limitations of the proposed StackGuard framework. The related work notes that CNN and DNN architectures "require substantial computational resources and large-scale training data," and that traditional ML approaches "depend heavily on manual feature selection and degrade under class imbalance and distributional shift," but these are characterizations of prior paradigms rather than explicitly acknowledged limitations of StackGuard itself. No author-stated limitations are present in the available text.

Not stated in the provided text. The conclusion (Section V) is referenced in the paper organization but its content is not included in the truncated output.

[[Concept - Stacking Ensemble]]
[[Concept - Heterogeneous Base Learners]]
[[Concept - Data Leakage Prevention]]
[[Concept - Meta-Classifier]]
[[Concept - IIoT Intrusion Detection]]

Not stated

Monitoring problem: Cyberattacks targeting Industrial IoT environments, including DoS/DDoS, malware, ransomware, MITM, and unauthorized access, exploiting weaknesses such as heterogeneous devices and limited resources. Signal: Network traffic records containing packet statistics, byte counts, connection duration, and system activity indicators from the X-IIoTID dataset (>800,000 records, 73 numerical features). Uncertainty method: Stacking-based meta-learning where RF, CNN, and DNN base learners produce attack-class probabilities, and a Random Forest meta-classifier trained on held-out prediction probabilities produces the final decision; threshold optimization at τ*=0.53 refines the precision–recall trade-off. Resulting action: Binary classification of each network traffic record as Normal (0) or Attack (1), enabling intrusion detection in IIoT environments. Evaluation setting: X-IIoTID benchmark dataset with 80/20 train/test split (164,167 test samples), two-level data-splitting separating base and meta training subsets, six model configurations ablated (Decision Tree, Logistic Regression, Random Forest, CNN, DNN, CNN–RF hybrid), compared against state-of-the-art including CNN–LSTM (98.84%), achieving 99.76% accuracy, precision 0.9984, recall 0.9967, F1-score 0.9975, ROC-AUC 0.9999.

One transfer to IVN: The heterogeneous stacking paradigm combining Random Forest, CNN, and DNN base learners with a meta-classifier could be adapted to in-vehicle network intrusion detection, where CAN bus traffic records (analogous to IIoT network traffic records) could be classified as normal or attack, with the meta-classifier learning to combine complementary strengths of tree-based methods on structured tabular CAN features and deep learning methods on temporal/sequential CAN signal patterns.

One reason the transfer may fail: CAN bus networks have fundamentally different characteristics from IIoT networks, including extremely constrained message sizes (8 bytes typical), hard real-time requirements, deterministic broadcast communication without IP addresses or protocols, and a much smaller feature space, which may render the 73-feature preprocessing pipeline and the computational overhead of a triple-model stacking ensemble impractical for resource-constrained in-vehicle electronic control units.

doi: 10.1109/eSmarTA70636.2026.11652363
source_link: Not stated
text_kind: Conference paper (2026 6th International Conference on Emerging Smart Technologies and Applications, eSmarTA)
monitoring_problem: Cyberattacks targeting Industrial IoT environments (DoS/DDoS, malware, ransomware, MITM, unauthorized access) exploiting heterogeneous devices and limited resources, where signature-based IDS fail against zero-day and adaptive threats
signal: Network traffic records from X-IIoTID dataset (>800,000 records, 73 numerical features after preprocessing) containing packet statistics, byte counts, connection duration, and system activity indicators
uncertainty_method: Stacking ensemble with Random Forest, CNN, and DNN base learners producing attack-class probabilities, combined by a Random Forest meta-classifier trained on held-out prediction probabilities; threshold optimization at τ =0.53; two-level data-splitting to prevent data leakage
action: Binary classification of each network traffic record as Normal (0) or Attack (1) for IIoT intrusion detection
eval_setting: X-IIoTID benchmark dataset, 80/20 train/test split (164,167 test samples), six model configurations ablated (Decision Tree, Logistic Regression, Random Forest, CNN, DNN, CNN–RF hybrid), compared against state-of-the-art including CNN–LSTM (98.84%), achieving 99.76% accuracy, precision 0.9984, recall 0.9967, F1-score 0.9975, ROC-AUC 0.9999
limitation_author: Not stated
limitation_inference: The triple-model stacking architecture with a meta-classifier introduces substantial computational overhead and latency, which may be impractical for resource-constrained IIoT edge devices; the study evaluates on a single benchmark dataset (X-IIoTID) without cross-dataset validation, raising generalizability concerns; the binary classification formulation collapses multi-class attack types into a single "Attack" category, losing granularity for threat-specific response
limitation_unknown: Whether the two-level data-splitting strategy introduces sufficient meta-training data after stratified sub-splitting of the training set; the exact computational cost and inference latency of the full StackGuard pipeline; performance under concept drift or adversarial evasion targeting the stacking ensemble; whether threshold τ =0.53 is dataset-specific or generalizable
support_passage: "StackGuard achieves 99.76% accuracy, precision of 0.9984, recall of 0.9967, F1-score of 0.9975, and ROC-AUC of 0.9999, surpassing all evaluated baselines by at least 0.92 percentage points. Threshold optimization at τ* = 0.53 further refines the precision–recall trade-off, yielding a peak F1-score of 0.9979."
transfer_ivn: Heterogeneous stacking of Random Forest, CNN, and DNN base learners with a meta-classifier could be adapted to CAN bus intrusion detection, where tree-based methods capture structured tabular CAN ID/feature patterns and deep learning captures temporal signal sequences, with the meta-classifier combining complementary strengths
transfer_risk: CAN bus networks have fundamentally different characteristics from IIoT networks—extremely constrained 8-byte messages, hard real-time requirements, deterministic broadcast communication without IP addresses or protocols, and much smaller feature space—which may render the 73-feature preprocessing pipeline and triple-model stacking computational overhead impractical for resource-constrained in-vehicle ECUs

#needs-review

## Record Fields
doi: 10.1109/eSmarTA70636.2026.11652363
source_link: Not stated
text_kind: fulltext
monitoring_problem: Cyberattacks targeting Industrial IoT environments, including DoS/DDoS, malware, ransomware, MITM, and unauthorized access, exploiting weaknesses such as heterogeneous devices and limited resources. Signal: Network traffic records containing packet statistics, byte counts, connection duration, and system activity indicators from the X-IIoTID dataset (>800,000 records, 73 numerical features). Uncertainty method: Stacking-based meta-learning where RF, CNN, and DNN base learners produce attack-class probabilities, and a Random Forest meta-classifier trained on held-out prediction probabilities produces the final decision; threshold optimization at τ*=0.53 refines the precision–recall trade-off. Resulting action: Binary classification of each network traffic record as Normal (0) or Attack (1), enabling intrusion detection in IIoT environments. Evaluation setting: X-IIoTID benchmark dataset with 80/20 train/test split (164,167 test samples), two-level data-splitting separating base and meta training subsets, six model configurations ablated (Decision Tree, Logistic Regression, Random Forest, CNN, DNN, CNN–RF hybrid), compared against state-of-the-art including CNN–LSTM (98.84%), achieving 99.76% accuracy, precision 0.9984, recall 0.9967, F1-score 0.9975, ROC-AUC 0.9999.
signal: Network traffic records from X-IIoTID dataset (>800,000 records, 73 numerical features after preprocessing) containing packet statistics, byte counts, connection duration, and system activity indicators
uncertainty_method: Stacking ensemble with Random Forest, CNN, and DNN base learners producing attack-class probabilities, combined by a Random Forest meta-classifier trained on held-out prediction probabilities; threshold optimization at τ =0.53; two-level data-splitting to prevent data leakage
action: Binary classification of each network traffic record as Normal (0) or Attack (1) for IIoT intrusion detection
eval_setting: X-IIoTID benchmark dataset, 80/20 train/test split (164,167 test samples), six model configurations ablated (Decision Tree, Logistic Regression, Random Forest, CNN, DNN, CNN–RF hybrid), compared against state-of-the-art including CNN–LSTM (98.84%), achieving 99.76% accuracy, precision 0.9984, recall 0.9967, F1-score 0.9975, ROC-AUC 0.9999
limitation_author: Not stated
limitation_inference: The triple-model stacking architecture with a meta-classifier introduces substantial computational overhead and latency, which may be impractical for resource-constrained IIoT edge devices; the study evaluates on a single benchmark dataset (X-IIoTID) without cross-dataset validation, raising generalizability concerns; the binary classification formulation collapses multi-class attack types into a single "Attack" category, losing granularity for threat-specific response
limitation_unknown: Whether the two-level data-splitting strategy introduces sufficient meta-training data after stratified sub-splitting of the training set; the exact computational cost and inference latency of the full StackGuard pipeline; performance under concept drift or adversarial evasion targeting the stacking ensemble; whether threshold τ =0.53 is dataset-specific or generalizable
support_passage: "StackGuard achieves 99.76% accuracy, precision of 0.9984, recall of 0.9967, F1-score of 0.9975, and ROC-AUC of 0.9999, surpassing all evaluated baselines by at least 0.92 percentage points. Threshold optimization at τ* = 0.53 further refines the precision–recall trade-off, yielding a peak F1-score of 0.9979."
transfer_ivn: Heterogeneous stacking of Random Forest, CNN, and DNN base learners with a meta-classifier could be adapted to CAN bus intrusion detection, where tree-based methods capture structured tabular CAN ID/feature patterns and deep learning captures temporal signal sequences, with the meta-classifier combining complementary strengths
transfer_risk: CAN bus networks have fundamentally different characteristics from IIoT networks—extremely constrained 8-byte messages, hard real-time requirements, deterministic broadcast communication without IP addresses or protocols, and much smaller feature space—which may render the 73-feature preprocessing pipeline and triple-model stacking computational overhead impractical for resource-constrained in-vehicle ECUs
