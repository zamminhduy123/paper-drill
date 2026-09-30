---
title: "XKG-IDS: Symbolic Graph Learning for Intrinsically Explainable IoT Intrusion Detection"
year: 2026
doi: "10.1007/978-3-032-34377-2_18"
relevance_score: 9.661
type: paper
---
# XKG-IDS: Symbolic Graph Learning for Intrinsically Explainable IoT Intrusion Detection

Novelty

Combines graph neural networks with Kolmogorov-Arnold Network (KAN) layers for IoT intrusion detection, representing traffic as temporal flow graphs. The learnable B-spline functions in KAN layers provide intrinsic interpretability through feature importance, per-sample explanations, spline patterns, and symbolic rules.

Methodology

IoT traffic is represented as temporal flow graphs to capture relationships between network flows. The framework integrates graph neural networks with Kolmogorov-Arnold Network layers whose learnable B-spline functions enable interpretable outputs. Evaluated on 12-class RT-IoT2022 dataset using five-fold cross-validation.

Explicit Limitations

Not stated in available abstract. The paper is behind a paywall, and no explicit limitations are mentioned in the accessible portion.

Future Work

Not stated in available abstract.

Concept Hubs

[[Concept - IoT Intrusion Detection]]
[[Concept - Symbolic Graph Learning]]
[[Concept - Kolmogorov-Arnold Networks]]
[[Concept - Graph Neural Networks]]
[[Concept - Intrinsic Explainability]]

Relevance Score

High relevance to the thesis topic. The paper directly addresses deep learning methods for IoT network intrusion detection, with explicit focus on explainability—a dimension often underexplored in prior IoT IDS work.

Monitoring Transfer

Monitoring problem, signal, uncertainty method, resulting action, evaluation setting.

Monitoring problem: Real-time detection of network intrusions in IoT environments where model decisions must be interpretable for security analysts.

Signal: Graph-structured network flow representations with per-sample feature importance scores and symbolic rules derived from B-spline functions.

Uncertainty method: Not explicitly stated; the model produces deterministic accuracy metrics (97.89% ± 0.47 across folds).

Action: Flag detected intrusions for analyst review, with explanations provided through symbolic rules and feature importance to support triage.

Evaluation setting: Five-fold cross-validation on the 12-class RT-IoT2022 dataset, achieving best fold accuracy of 98.43% and macro F1-score of 92.43%.

One transfer to IVN and one reason the transfer may fail.

Transfer to IVN: The symbolic graph learning approach could be adapted for in-vehicle network intrusion detection by representing CAN bus messages as temporal flow graphs and using KAN layers for interpretable attack classification.

Transfer risk: IVN traffic has fundamentally different characteristics from IoT networks—CAN messages are broadcast-based with strict timing constraints and fixed message IDs, whereas IoT traffic involves diverse protocols and endpoint relationships. The graph construction and feature engineering that work for IoT flow relationships may not capture the deterministic, periodic nature of CAN communication, potentially degrading detection performance.

Exact Field Lines

doi:10.1007/978-3-032-34377-2_18
source_link: https://dl.acm.org/doi/abs/10.1007/978-3-032-34377-2_18
text_kind:abstract
monitoring_problem:real-time IoT network intrusion detection requiring interpretable model decisions
signal:graph-structured network flow representations; per-sample feature importance; spline patterns; symbolic rules
uncertainty_method:not stated
action:flag detected intrusions with explanations for analyst review
eval_setting:five-fold cross-validation on 12-class RT-IoT2022 dataset
limitation_author:not stated
limitation_inference:paywalled full text; no explicit limitations in abstract; symbolic rule interpretability may trade off detection latency in real-time settings
limitation_unknown:computational overhead of KAN layers; generalizability to other IoT datasets; robustness to adversarial evasion
support_passage:Intrusion detection in Internet of Things (IoT) environments needs models that are accurate, reliable, and easy to interpret. This study presents XKG-IDS, a graph-based intrusion detection framework that combines graph neural networks with Kolmogorov-Arnold Network (KAN) layers. The model represents IoT traffic as temporal flow graphs to capture relationships between network flows. The KAN layers use learnable B-spline functions, which make the model interpretable by providing feature importance, per-sample explanations, spline patterns, and symbolic rules. Experiments on the 12-class RT-IoT2022 dataset show that XKG-IDS achieves a mean accuracy of 97.89% ± 0.47 across five folds, with the best fold reaching 98.43% accuracy and 92.43% macro F1-score.
transfer_ivn:represent CAN bus messages as temporal flow graphs with KAN layers for interpretable attack classification
transfer_risk:CAN bus deterministic broadcast communication with fixed message IDs differs fundamentally from IoT flow relationships, degrading graph construction efficacy

Combines graph neural networks with Kolmogorov-Arnold Network (KAN) layers for IoT intrusion detection, representing traffic as temporal flow graphs. The learnable B-spline functions in KAN layers provide intrinsic interpretability through feature importance, per-sample explanations, spline patterns, and symbolic rules.

IoT traffic is represented as temporal flow graphs to capture relationships between network flows. The framework integrates graph neural networks with Kolmogorov-Arnold Network layers whose learnable B-spline functions enable interpretable outputs. Evaluated on 12-class RT-IoT2022 dataset using five-fold cross-validation.

Not stated in available abstract. The paper is behind a paywall, and no explicit limitations are mentioned in the accessible portion.

Not stated in available abstract.

[[Concept - IoT Intrusion Detection]]
[[Concept - Symbolic Graph Learning]]
[[Concept - Kolmogorov-Arnold Networks]]
[[Concept - Graph Neural Networks]]
[[Concept - Intrinsic Explainability]]

High relevance to the thesis topic. The paper directly addresses deep learning methods for IoT network intrusion detection, with explicit focus on explainability—a dimension often underexplored in prior IoT IDS work.

Monitoring problem, signal, uncertainty method, resulting action, evaluation setting.

Monitoring problem: Real-time detection of network intrusions in IoT environments where model decisions must be interpretable for security analysts.

Signal: Graph-structured network flow representations with per-sample feature importance scores and symbolic rules derived from B-spline functions.

Uncertainty method: Not explicitly stated; the model produces deterministic accuracy metrics (97.89% ± 0.47 across folds).

Action: Flag detected intrusions for analyst review, with explanations provided through symbolic rules and feature importance to support triage.

Evaluation setting: Five-fold cross-validation on the 12-class RT-IoT2022 dataset, achieving best fold accuracy of 98.43% and macro F1-score of 92.43%.

One transfer to IVN and one reason the transfer may fail.

Transfer to IVN: The symbolic graph learning approach could be adapted for in-vehicle network intrusion detection by representing CAN bus messages as temporal flow graphs and using KAN layers for interpretable attack classification.

Transfer risk: IVN traffic has fundamentally different characteristics from IoT networks—CAN messages are broadcast-based with strict timing constraints and fixed message IDs, whereas IoT traffic involves diverse protocols and endpoint relationships. The graph construction and feature engineering that work for IoT flow relationships may not capture the deterministic, periodic nature of CAN communication, potentially degrading detection performance.

doi:10.1007/978-3-032-34377-2_18
source_link: https://dl.acm.org/doi/abs/10.1007/978-3-032-34377-2_18
text_kind:abstract
monitoring_problem:real-time IoT network intrusion detection requiring interpretable model decisions
signal:graph-structured network flow representations; per-sample feature importance; spline patterns; symbolic rules
uncertainty_method:not stated
action:flag detected intrusions with explanations for analyst review
eval_setting:five-fold cross-validation on 12-class RT-IoT2022 dataset
limitation_author:not stated
limitation_inference:paywalled full text; no explicit limitations in abstract; symbolic rule interpretability may trade off detection latency in real-time settings
limitation_unknown:computational overhead of KAN layers; generalizability to other IoT datasets; robustness to adversarial evasion
support_passage:Intrusion detection in Internet of Things (IoT) environments needs models that are accurate, reliable, and easy to interpret. This study presents XKG-IDS, a graph-based intrusion detection framework that combines graph neural networks with Kolmogorov-Arnold Network (KAN) layers. The model represents IoT traffic as temporal flow graphs to capture relationships between network flows. The KAN layers use learnable B-spline functions, which make the model interpretable by providing feature importance, per-sample explanations, spline patterns, and symbolic rules. Experiments on the 12-class RT-IoT2022 dataset show that XKG-IDS achieves a mean accuracy of 97.89% ± 0.47 across five folds, with the best fold reaching 98.43% accuracy and 92.43% macro F1-score.
transfer_ivn:represent CAN bus messages as temporal flow graphs with KAN layers for interpretable attack classification
transfer_risk:CAN bus deterministic broadcast communication with fixed message IDs differs fundamentally from IoT flow relationships, degrading graph construction efficacy

#needs-review

## Record Fields
doi: 10.1007/978-3-032-34377-2_18
source_link: https://dl.acm.org/doi/abs/10.1007/978-3-032-34377-2_18
text_kind: abstract
monitoring_problem: Real-time detection of network intrusions in IoT environments where model decisions must be interpretable for security analysts.
signal: Graph-structured network flow representations with per-sample feature importance scores and symbolic rules derived from B-spline functions.
uncertainty_method: Not explicitly stated; the model produces deterministic accuracy metrics (97.89% ± 0.47 across folds).
action: Flag detected intrusions for analyst review, with explanations provided through symbolic rules and feature importance to support triage.
eval_setting: five-fold cross-validation on 12-class RT-IoT2022 dataset
limitation_author: not stated
limitation_inference: paywalled full text; no explicit limitations in abstract; symbolic rule interpretability may trade off detection latency in real-time settings
limitation_unknown: computational overhead of KAN layers; generalizability to other IoT datasets; robustness to adversarial evasion
support_passage: Intrusion detection in Internet of Things (IoT) environments needs models that are accurate, reliable, and easy to interpret. This study presents XKG-IDS, a graph-based intrusion detection framework that combines graph neural networks with Kolmogorov-Arnold Network (KAN) layers. The model represents IoT traffic as temporal flow graphs to capture relationships between network flows. The KAN layers use learnable B-spline functions, which make the model interpretable by providing feature importance, per-sample explanations, spline patterns, and symbolic rules. Experiments on the 12-class RT-IoT2022 dataset show that XKG-IDS achieves a mean accuracy of 97.89% ± 0.47 across five folds, with the best fold reaching 98.43% accuracy and 92.43% macro F1-score.
transfer_ivn: represent CAN bus messages as temporal flow graphs with KAN layers for interpretable attack classification
transfer_risk: IVN traffic has fundamentally different characteristics from IoT networks—CAN messages are broadcast-based with strict timing constraints and fixed message IDs, whereas IoT traffic involves diverse protocols and endpoint relationships. The graph construction and feature engineering that work for IoT flow relationships may not capture the deterministic, periodic nature of CAN communication, potentially degrading detection performance.
