---
title: "BOSE: A Bayesian-Optimized Stacked Ensemble Framework for Explainable Fine-Grained Industrial IoT Intrusion Detection"
year: 2026
doi: "https://doi.org/10.3390/app16167919"
relevance_score: 9.581
type: paper
---
# BOSE: A Bayesian-Optimized Stacked Ensemble Framework for Explainable Fine-Grained Industrial IoT Intrusion Detection

Novelty

BOSE introduces a Bayesian-optimized stacked ensemble for 50-class fine-grained IIoT intrusion detection that jointly targets accuracy, CPU-level deployment cost, and interpretability. Its distinguishing elements are hybrid feature selection (84→46 features), leakage-free Out-of-Fold meta-feature generation, and a dual-level SHAP scheme that explains both feature-level contributions and ensemble-level decisions.

Methodology

* Hybrid feature selection reduces the original 84-feature space to 46 informative features.

* Bayesian Optimization tunes hyperparameters for the ensemble base and meta models.

* Out-of-Fold (OOF) stacking with leakage-free meta-feature generation supports reliable meta-learning.

* Dual-level SHAP explainability covers feature-level attribution and ensemble-level decision explanation.

* Evaluation on the 50-class DataSense benchmark over ten independent runs, with Macro-F1, inference latency, throughput, runtime memory, and model size reported under a workstation CPU configuration.

Explicit Limitations

* Evaluation is restricted to the 50-class DataSense benchmark.

* Deployment feasibility is demonstrated only for CPU-based inference under the evaluated workstation configuration.

* Suitability for industrial edge gateways and industrial PCs is stated as potential rather than validated.

* Comparisons with recent hierarchical multi-stage frameworks are described as competitive rather than superior, since those are not directly comparable under the same end-to-end setting.

Future Work

Not stated.

Concept Hubs

[[Concept - IIoT Intrusion Detection]], [[Concept - Stacking Ensemble]], [[Concept - Bayesian Optimization]], [[Concept - Data Leakage Prevention]], [[Concept - Edge Security]]

Relevance Score

High. The paper addresses deep-learning-based intrusion detection for IoT/IIoT networks with an emphasis on fine-grained classification, deployment cost, and explainability, which aligns directly with the stated thesis on applying deep learning to IoT network intrusion detection.

Monitoring Transfer

monitoring_problem: Sophisticated cyberattacks in IIoT environments requiring intrusion detection that balances accuracy, deployment cost, and interpretability.
signal: Network traffic features from the DataSense benchmark, reduced from 84 to 46 informative features.
uncertainty_method: Bayesian Optimization for hyperparameter configuration; dual-level SHAP for model transparency.
action: Classify traffic into 50 fine-grained intrusion classes via a Bayesian-optimized stacked ensemble.
eval_setting: 50-class DataSense benchmark, ten independent runs, CPU-based workstation inference; Macro-F1, latency, throughput, memory, and model size reported.
limitation_author: Evaluation limited to DataSense; edge/industrial PC applicability framed as potential; hierarchical comparisons not directly comparable.
limitation_inference: Generalization to other IIoT datasets, hardware platforms, and attack distributions is unverified; SHAP explanations add interpretability but not causal validation.
limitation_unknown: Cross-dataset performance, adversarial robustness, concept drift behavior, and real-world deployment latency under production traffic are not reported.
support_passage: Experimental results on the 50-class DataSense benchmark show that BOSE achieves a Macro-F1 score of 88.43% over ten independent runs, outperforming all directly comparable baseline models evaluated under the same end-to-end 50-class classification setting while remaining competitive with recent hierarchical multi-stage frameworks.
transfer_ivn: The leakage-free OOF stacking and Bayesian-optimized ensemble pipeline could be adapted to in-vehicle network intrusion detection, where multi-class attack classification and SHAP-based explanation of ensemble decisions would aid automotive security monitoring under tight compute budgets.
transfer_risk: IVN traffic differs fundamentally from IIoT traffic in timing determinism, protocol semantics, and feature stability, so the 46-feature selection and class structure may not transfer without re-derivation, and latency constraints on CAN/CAN FD gateways are stricter than the reported 0.1421 ms workstation inference.

doi: not stated
source_link: not stated
text_kind: abstract
monitoring_problem: Sophisticated cyberattacks in IIoT environments requiring intrusion detection balancing accuracy, deployment cost, and interpretability.
signal: Network traffic features from the DataSense benchmark, reduced from 84 to 46 informative features.
uncertainty_method: Bayesian Optimization for hyperparameters; dual-level SHAP explainability.
action: 50-class fine-grained intrusion classification via Bayesian-optimized stacked ensemble with leakage-free OOF stacking.
eval_setting: 50-class DataSense benchmark, ten independent runs, CPU-based workstation inference; Macro-F1, latency, throughput, memory, and model size.
limitation_author: Evaluation limited to DataSense; edge/industrial PC applicability stated as potential; hierarchical framework comparisons not directly comparable.
limitation_inference: Generalization to other IIoT datasets and hardware is unverified; SHAP provides transparency but not causal validation.
limitation_unknown: Cross-dataset performance, adversarial robustness, concept drift, and production deployment latency are not reported.
support_passage: Experimental results on the 50-class DataSense benchmark show that BOSE achieves a Macro-F1 score of 88.43% over ten independent runs, outperforming all directly comparable baseline models evaluated under the same end-to-end 50-class classification setting while remaining competitive with recent hierarchical multi-stage frameworks.
transfer_ivn: Leakage-free OOF stacking and Bayesian-optimized ensembling could support multi-class IVN attack detection with SHAP-based explanation under constrained automotive compute.
transfer_risk: IVN traffic differs in timing determinism, protocol semantics, and feature stability, so feature selection and class structure may not transfer, and CAN/CAN FD latency budgets are stricter than the reported workstation inference.

BOSE introduces a Bayesian-optimized stacked ensemble for 50-class fine-grained IIoT intrusion detection that jointly targets accuracy, CPU-level deployment cost, and interpretability. Its distinguishing elements are hybrid feature selection (84→46 features), leakage-free Out-of-Fold meta-feature generation, and a dual-level SHAP scheme that explains both feature-level contributions and ensemble-level decisions.

Hybrid feature selection reduces the original 84-feature space to 46 informative features.

Bayesian Optimization tunes hyperparameters for the ensemble base and meta models.

Out-of-Fold (OOF) stacking with leakage-free meta-feature generation supports reliable meta-learning.

Dual-level SHAP explainability covers feature-level attribution and ensemble-level decision explanation.

Evaluation on the 50-class DataSense benchmark over ten independent runs, with Macro-F1, inference latency, throughput, runtime memory, and model size reported under a workstation CPU configuration.

Evaluation is restricted to the 50-class DataSense benchmark.

Deployment feasibility is demonstrated only for CPU-based inference under the evaluated workstation configuration.

Suitability for industrial edge gateways and industrial PCs is stated as potential rather than validated.

Comparisons with recent hierarchical multi-stage frameworks are described as competitive rather than superior, since those are not directly comparable under the same end-to-end setting.

Not stated.

[[Concept - IIoT Intrusion Detection]], [[Concept - Stacking Ensemble]], [[Concept - Bayesian Optimization]], [[Concept - Data Leakage Prevention]], [[Concept - Edge Security]]

High. The paper addresses deep-learning-based intrusion detection for IoT/IIoT networks with an emphasis on fine-grained classification, deployment cost, and explainability, which aligns directly with the stated thesis on applying deep learning to IoT network intrusion detection.

monitoring_problem: Sophisticated cyberattacks in IIoT environments requiring intrusion detection that balances accuracy, deployment cost, and interpretability.
signal: Network traffic features from the DataSense benchmark, reduced from 84 to 46 informative features.
uncertainty_method: Bayesian Optimization for hyperparameter configuration; dual-level SHAP for model transparency.
action: Classify traffic into 50 fine-grained intrusion classes via a Bayesian-optimized stacked ensemble.
eval_setting: 50-class DataSense benchmark, ten independent runs, CPU-based workstation inference; Macro-F1, latency, throughput, memory, and model size reported.
limitation_author: Evaluation limited to DataSense; edge/industrial PC applicability framed as potential; hierarchical comparisons not directly comparable.
limitation_inference: Generalization to other IIoT datasets, hardware platforms, and attack distributions is unverified; SHAP explanations add interpretability but not causal validation.
limitation_unknown: Cross-dataset performance, adversarial robustness, concept drift behavior, and real-world deployment latency under production traffic are not reported.
support_passage: Experimental results on the 50-class DataSense benchmark show that BOSE achieves a Macro-F1 score of 88.43% over ten independent runs, outperforming all directly comparable baseline models evaluated under the same end-to-end 50-class classification setting while remaining competitive with recent hierarchical multi-stage frameworks.
transfer_ivn: The leakage-free OOF stacking and Bayesian-optimized ensemble pipeline could be adapted to in-vehicle network intrusion detection, where multi-class attack classification and SHAP-based explanation of ensemble decisions would aid automotive security monitoring under tight compute budgets.
transfer_risk: IVN traffic differs fundamentally from IIoT traffic in timing determinism, protocol semantics, and feature stability, so the 46-feature selection and class structure may not transfer without re-derivation, and latency constraints on CAN/CAN FD gateways are stricter than the reported 0.1421 ms workstation inference.

doi: not stated
source_link: not stated
text_kind: abstract
monitoring_problem: Sophisticated cyberattacks in IIoT environments requiring intrusion detection balancing accuracy, deployment cost, and interpretability.
signal: Network traffic features from the DataSense benchmark, reduced from 84 to 46 informative features.
uncertainty_method: Bayesian Optimization for hyperparameters; dual-level SHAP explainability.
action: 50-class fine-grained intrusion classification via Bayesian-optimized stacked ensemble with leakage-free OOF stacking.
eval_setting: 50-class DataSense benchmark, ten independent runs, CPU-based workstation inference; Macro-F1, latency, throughput, memory, and model size.
limitation_author: Evaluation limited to DataSense; edge/industrial PC applicability stated as potential; hierarchical framework comparisons not directly comparable.
limitation_inference: Generalization to other IIoT datasets and hardware is unverified; SHAP provides transparency but not causal validation.
limitation_unknown: Cross-dataset performance, adversarial robustness, concept drift, and production deployment latency are not reported.
support_passage: Experimental results on the 50-class DataSense benchmark show that BOSE achieves a Macro-F1 score of 88.43% over ten independent runs, outperforming all directly comparable baseline models evaluated under the same end-to-end 50-class classification setting while remaining competitive with recent hierarchical multi-stage frameworks.
transfer_ivn: Leakage-free OOF stacking and Bayesian-optimized ensembling could support multi-class IVN attack detection with SHAP-based explanation under constrained automotive compute.
transfer_risk: IVN traffic differs in timing determinism, protocol semantics, and feature stability, so feature selection and class structure may not transfer, and CAN/CAN FD latency budgets are stricter than the reported workstation inference.

#needs-review

## Record Fields
doi: https://doi.org/10.3390/app16167919
source_link: not stated
text_kind: abstract
monitoring_problem: Sophisticated cyberattacks in IIoT environments requiring intrusion detection that balances accuracy, deployment cost, and interpretability.
signal: Network traffic features from the DataSense benchmark, reduced from 84 to 46 informative features.
uncertainty_method: Bayesian Optimization for hyperparameter configuration; dual-level SHAP for model transparency.
action: Classify traffic into 50 fine-grained intrusion classes via a Bayesian-optimized stacked ensemble.
eval_setting: 50-class DataSense benchmark, ten independent runs, CPU-based workstation inference; Macro-F1, latency, throughput, memory, and model size reported.
limitation_author: Evaluation limited to DataSense; edge/industrial PC applicability framed as potential; hierarchical comparisons not directly comparable.
limitation_inference: Generalization to other IIoT datasets, hardware platforms, and attack distributions is unverified; SHAP explanations add interpretability but not causal validation.
limitation_unknown: Cross-dataset performance, adversarial robustness, concept drift behavior, and real-world deployment latency under production traffic are not reported.
support_passage: Experimental results on the 50-class DataSense benchmark show that BOSE achieves a Macro-F1 score of 88.43% over ten independent runs, outperforming all directly comparable baseline models evaluated under the same end-to-end 50-class classification setting while remaining competitive with recent hierarchical multi-stage frameworks.
transfer_ivn: The leakage-free OOF stacking and Bayesian-optimized ensemble pipeline could be adapted to in-vehicle network intrusion detection, where multi-class attack classification and SHAP-based explanation of ensemble decisions would aid automotive security monitoring under tight compute budgets.
transfer_risk: IVN traffic differs fundamentally from IIoT traffic in timing determinism, protocol semantics, and feature stability, so the 46-feature selection and class structure may not transfer without re-derivation, and latency constraints on CAN/CAN FD gateways are stricter than the reported 0.1421 ms workstation inference.
