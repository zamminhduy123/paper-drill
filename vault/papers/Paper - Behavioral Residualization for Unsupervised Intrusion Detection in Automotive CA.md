---
title: "Behavioral Residualization for Unsupervised Intrusion Detection in Automotive CAN Networks"
year: 2026
doi: "https://doi.org/10.48550/arxiv.2608.05548"
relevance_score: 8.205
type: paper
---
# Behavioral Residualization for Unsupervised Intrusion Detection in Automotive CAN Networks

Novelty

* Introduces per-ID behavioral residualization, a CAN-specific representation that extracts fourteen temporal, protocol, and payload features from sliding windows and residualizes them against each arbitration ID's normal baseline.

* Central claim: the representation, rather than any individual detector, drives performance gains across six unsupervised detectors and two datasets.

* Explicitly quantifies coverage boundaries via two failure modes (novel-ID flooding and cross-ID fuzzing).

Methodology

* Extract 14 temporal, protocol, and payload features from sliding windows on CAN traffic.

* Residualize features against each arbitration ID's normal baseline (per-ID behavioral residualization).

* Evaluate six unsupervised detectors across two datasets (HCRL and ROAD) using five seeds.

* Measure mean F1 improvement from residualization (21/24 on HCRL, 30/36 on ROAD) and recall/ROC-AUC on ROAD targeted signal-manipulation attacks.

Explicit Limitations

* Novel-ID flooding (HCRL DoS, F1 = 0.02).

* Cross-ID fuzzing (ROAD, F1 = 0.27).

* These define the measured coverage boundary of the proposed representation.

Future Work

* Not stated.

Concept Hubs

* [[Concept - Behavioral Residualization]]

* [[Concept - Unsupervised Intrusion Detection]]

* [[Concept - In-Vehicle Network Security]]

* [[Concept - CAN Network Anomaly Detection]]

* [[Concept - Deep Learning Intrusion Detection]]

Relevance Score

* Not stated.

Monitoring Transfer

Monitoring problem, signal, uncertainty method, resulting action, evaluation setting. One transfer to IVN and one reason the transfer may fail.

* monitoring_problem: Intrusion detection in automotive CAN networks where attackers reuse legitimate arbitration IDs, defeating presence-based features.

* signal: Fourteen temporal, protocol, and payload features extracted from sliding windows and residualized against each arbitration ID's normal baseline.

* uncertainty_method: Unsupervised detectors (six evaluated) operating on residualized per-ID behavioral representations.

* action: Flag anomalous CAN frames as intrusions for defense-in-depth.

* eval_setting: Six unsupervised detectors, two datasets (HCRL and ROAD), five seeds; recall >= 0.99 with high ROC-AUC on ROAD targeted signal-manipulation attacks.

* limitation_author: Novel-ID flooding (HCRL DoS, F1 = 0.02) and cross-ID fuzzing (ROAD, F1 = 0.27) define the measured coverage boundary.

* limitation_inference: Residualization assumes stable per-ID normal baselines; attacks that introduce new IDs or blur ID boundaries fall outside the representation's coverage.

* limitation_unknown: Whether residualization generalizes to other vehicle bus protocols or real-time deployment constraints is not stated.

* support_passage: "We present per-ID behavioral residualization, a CAN-specific representation that extracts fourteen temporal, protocol, and payload features from sliding windows and residualizes them against each arbitration ID's normal baseline."

* transfer_ivn: Per-ID residualization can be applied to CAN traffic monitoring in production vehicles to detect ID-reuse attacks that bypass presence-based detectors.

* transfer_risk: Transfer may fail if the target vehicle's per-ID baselines drift or if attackers introduce novel IDs, since these are the quantified failure modes.

doi: not stated
source_link: not stated
text_kind: not stated
monitoring_problem: Intrusion detection in automotive CAN networks where attackers reuse legitimate arbitration IDs.
signal: Fourteen temporal, protocol, and payload features from sliding windows residualized against each arbitration ID's normal baseline.
uncertainty_method: Unsupervised detectors operating on residualized per-ID behavioral representations.
action: Flag anomalous CAN frames as intrusions for defense-in-depth.
eval_setting: Six unsupervised detectors, HCRL and ROAD datasets, five seeds; recall >= 0.99 with high ROC-AUC on ROAD targeted signal-manipulation attacks.
limitation_author: Novel-ID flooding (HCRL DoS, F1 = 0.02) and cross-ID fuzzing (ROAD, F1 = 0.27).
limitation_inference: Residualization assumes stable per-ID normal baselines and fails when attacks introduce new IDs or blur ID boundaries.
limitation_unknown: Generalization to other bus protocols and real-time deployment constraints.
support_passage: We present per-ID behavioral residualization, a CAN-specific representation that extracts fourteen temporal, protocol, and payload features from sliding windows and residualizes them against each arbitration ID's normal baseline.
transfer_ivn: Per-ID residualization can be applied to CAN traffic monitoring in production vehicles to detect ID-reuse attacks that bypass presence-based detectors.
transfer_risk: Transfer may fail if the target vehicle's per-ID baselines drift or if attackers introduce novel IDs, since these are the quantified failure modes.

Introduces per-ID behavioral residualization, a CAN-specific representation that extracts fourteen temporal, protocol, and payload features from sliding windows and residualizes them against each arbitration ID's normal baseline.

Central claim: the representation, rather than any individual detector, drives performance gains across six unsupervised detectors and two datasets.

Explicitly quantifies coverage boundaries via two failure modes (novel-ID flooding and cross-ID fuzzing).

Extract 14 temporal, protocol, and payload features from sliding windows on CAN traffic.

Residualize features against each arbitration ID's normal baseline (per-ID behavioral residualization).

Evaluate six unsupervised detectors across two datasets (HCRL and ROAD) using five seeds.

Measure mean F1 improvement from residualization (21/24 on HCRL, 30/36 on ROAD) and recall/ROC-AUC on ROAD targeted signal-manipulation attacks.

Novel-ID flooding (HCRL DoS, F1 = 0.02).

Cross-ID fuzzing (ROAD, F1 = 0.27).

These define the measured coverage boundary of the proposed representation.

Not stated.

[[Concept - Behavioral Residualization]]

[[Concept - Unsupervised Intrusion Detection]]

[[Concept - In-Vehicle Network Security]]

[[Concept - CAN Network Anomaly Detection]]

[[Concept - Deep Learning Intrusion Detection]]

Not stated.

Monitoring problem, signal, uncertainty method, resulting action, evaluation setting. One transfer to IVN and one reason the transfer may fail.

monitoring_problem: Intrusion detection in automotive CAN networks where attackers reuse legitimate arbitration IDs, defeating presence-based features.

signal: Fourteen temporal, protocol, and payload features extracted from sliding windows and residualized against each arbitration ID's normal baseline.

uncertainty_method: Unsupervised detectors (six evaluated) operating on residualized per-ID behavioral representations.

action: Flag anomalous CAN frames as intrusions for defense-in-depth.

eval_setting: Six unsupervised detectors, two datasets (HCRL and ROAD), five seeds; recall >= 0.99 with high ROC-AUC on ROAD targeted signal-manipulation attacks.

limitation_author: Novel-ID flooding (HCRL DoS, F1 = 0.02) and cross-ID fuzzing (ROAD, F1 = 0.27) define the measured coverage boundary.

limitation_inference: Residualization assumes stable per-ID normal baselines; attacks that introduce new IDs or blur ID boundaries fall outside the representation's coverage.

limitation_unknown: Whether residualization generalizes to other vehicle bus protocols or real-time deployment constraints is not stated.

support_passage: "We present per-ID behavioral residualization, a CAN-specific representation that extracts fourteen temporal, protocol, and payload features from sliding windows and residualizes them against each arbitration ID's normal baseline."

transfer_ivn: Per-ID residualization can be applied to CAN traffic monitoring in production vehicles to detect ID-reuse attacks that bypass presence-based detectors.

transfer_risk: Transfer may fail if the target vehicle's per-ID baselines drift or if attackers introduce novel IDs, since these are the quantified failure modes.

doi: not stated
source_link: not stated
text_kind: not stated
monitoring_problem: Intrusion detection in automotive CAN networks where attackers reuse legitimate arbitration IDs.
signal: Fourteen temporal, protocol, and payload features from sliding windows residualized against each arbitration ID's normal baseline.
uncertainty_method: Unsupervised detectors operating on residualized per-ID behavioral representations.
action: Flag anomalous CAN frames as intrusions for defense-in-depth.
eval_setting: Six unsupervised detectors, HCRL and ROAD datasets, five seeds; recall >= 0.99 with high ROC-AUC on ROAD targeted signal-manipulation attacks.
limitation_author: Novel-ID flooding (HCRL DoS, F1 = 0.02) and cross-ID fuzzing (ROAD, F1 = 0.27).
limitation_inference: Residualization assumes stable per-ID normal baselines and fails when attacks introduce new IDs or blur ID boundaries.
limitation_unknown: Generalization to other bus protocols and real-time deployment constraints.
support_passage: We present per-ID behavioral residualization, a CAN-specific representation that extracts fourteen temporal, protocol, and payload features from sliding windows and residualizes them against each arbitration ID's normal baseline.
transfer_ivn: Per-ID residualization can be applied to CAN traffic monitoring in production vehicles to detect ID-reuse attacks that bypass presence-based detectors.
transfer_risk: Transfer may fail if the target vehicle's per-ID baselines drift or if attackers introduce novel IDs, since these are the quantified failure modes.

#needs-review

## Record Fields
doi: https://doi.org/10.48550/arxiv.2608.05548
source_link: not stated
text_kind: abstract
monitoring_problem: Intrusion detection in automotive CAN networks where attackers reuse legitimate arbitration IDs.
signal: Fourteen temporal, protocol, and payload features from sliding windows residualized against each arbitration ID's normal baseline.
uncertainty_method: Unsupervised detectors operating on residualized per-ID behavioral representations.
action: Flag anomalous CAN frames as intrusions for defense-in-depth.
eval_setting: Six unsupervised detectors, HCRL and ROAD datasets, five seeds; recall >= 0.99 with high ROC-AUC on ROAD targeted signal-manipulation attacks.
limitation_author: Novel-ID flooding (HCRL DoS, F1 = 0.02) and cross-ID fuzzing (ROAD, F1 = 0.27).
limitation_inference: Residualization assumes stable per-ID normal baselines and fails when attacks introduce new IDs or blur ID boundaries.
limitation_unknown: Generalization to other bus protocols and real-time deployment constraints.
support_passage: We present per-ID behavioral residualization, a CAN-specific representation that extracts fourteen temporal, protocol, and payload features from sliding windows and residualizes them against each arbitration ID's normal baseline.
transfer_ivn: Per-ID residualization can be applied to CAN traffic monitoring in production vehicles to detect ID-reuse attacks that bypass presence-based detectors.
transfer_risk: Transfer may fail if the target vehicle's per-ID baselines drift or if attackers introduce novel IDs, since these are the quantified failure modes.
