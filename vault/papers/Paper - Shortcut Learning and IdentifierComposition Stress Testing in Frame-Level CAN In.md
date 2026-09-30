---
title: "Shortcut Learning and Identifier/Composition Stress Testing in Frame-Level CAN Intrusion Detection"
year: 2026
doi: "https://doi.org/10.5281/zenodo.21536764"
relevance_score: 4.5040000000000004
type: paper
---
# Shortcut Learning and Identifier/Composition Stress Testing in Frame-Level CAN Intrusion Detection

Novelty

This work audits shortcut learning in frame-level CAN intrusion detection rather than proposing a new detector, using corrected reconstructions of the CAR-Hacking and Survival datasets to expose identifier and composition artifacts. It combines fixed-identifier lookup controls, feature ablations, split-scheme contrasts, identifier/composition stress tests, cross-corpus transfer diagnostics, and a bounded temporal-convolutional-network sanity check.

Methodology

Frame-level CAN intrusion detection is evaluated on corrected reconstructions of CAR-Hacking and Survival logs. The study runs fixed-identifier lookup controls, timing and payload feature ablations, chronological versus random-frame splits, identifier/composition stress tests, cross-corpus transfer diagnostics, and a bounded temporal-convolutional-network sanity check. Code, processed-result artifacts, validation tests, generated tables, and reproducibility materials are packaged for verification, but third-party raw datasets are not redistributed; full reconstruction and model refitting require obtaining the original logs separately per the README and data manifests.

Explicit Limitations

Raw CAR-Hacking and Survival logs are not redistributed, so full dataset reconstruction and model refitting depend on users obtaining the original logs separately. The study is an audit of shortcut learning rather than a deployed detection system, and the temporal-convolutional-network check is bounded rather than an exhaustive architecture search.

Future Work

Not stated.

Concept Hubs

[[Concept - CAN Intrusion Detection]], [[Concept - Shortcut Learning]], [[Concept - Benchmark Stress Testing]], [[Concept - Data Leakage Prevention]], [[Concept - In-Vehicle Network Security]]

Relevance Score

Not stated.

Monitoring Transfer

Monitoring problem: frame-level CAN intrusion detection under shortcut learning and identifier/composition stress. Signal: CAN frame identifiers, timing, and payload features. Uncertainty method: fixed-identifier lookup controls, feature ablations, split-scheme contrasts, identifier/composition stress tests, cross-corpus transfer diagnostics, and a bounded temporal-convolutional-network sanity check. Action: audit and stress-test detector behavior. Evaluation setting: corrected reconstructions of CAR-Hacking and Survival datasets. Transfer to IVN: frame-level CAN ID and composition stress testing transfers directly to in-vehicle network intrusion detection benchmarking. Transfer risk: shortcut learning may cause detectors to rely on identifier artifacts that do not generalize across vehicle architectures or driving conditions.

doi: Not stated
source_link: Not stated
text_kind: repository/software record
monitoring_problem: frame-level CAN intrusion detection under shortcut learning and identifier/composition stress
signal: CAN frame identifiers, timing, and payload features
uncertainty_method: fixed-identifier lookup controls, feature ablations, chronological and random-frame splits, identifier/composition stress tests, cross-corpus transfer diagnostics, bounded temporal-convolutional-network sanity check
action: audit and stress-test detector behavior
eval_setting: corrected reconstructions of CAR-Hacking and Survival datasets
limitation_author: Full dataset reconstruction and model refitting require users to obtain the original CAR-Hacking and Survival logs separately; raw datasets are not redistributed
limitation_inference: The temporal-convolutional-network check is bounded and does not exhaustively cover detector architectures or deployment conditions
limitation_unknown: Not stated
support_passage: This study audits shortcut learning in frame-level Controller Area Network intrusion detection using corrected reconstructions of the CAR-Hacking and Survival datasets. It evaluates fixed-identifier lookup controls, timing and payload feature ablations, chronological and random-frame splits, identifier/composition stress tests, cross-corpus transfer diagnostics, and a bounded temporal-convolutional-network sanity check.
transfer_ivn: Frame-level CAN identifier and composition stress testing transfers directly to in-vehicle network intrusion detection benchmarking
transfer_risk: Shortcut learning may cause detectors to rely on identifier artifacts that do not generalize across vehicle architectures or driving conditions

This work audits shortcut learning in frame-level CAN intrusion detection rather than proposing a new detector, using corrected reconstructions of the CAR-Hacking and Survival datasets to expose identifier and composition artifacts. It combines fixed-identifier lookup controls, feature ablations, split-scheme contrasts, identifier/composition stress tests, cross-corpus transfer diagnostics, and a bounded temporal-convolutional-network sanity check.

Frame-level CAN intrusion detection is evaluated on corrected reconstructions of CAR-Hacking and Survival logs. The study runs fixed-identifier lookup controls, timing and payload feature ablations, chronological versus random-frame splits, identifier/composition stress tests, cross-corpus transfer diagnostics, and a bounded temporal-convolutional-network sanity check. Code, processed-result artifacts, validation tests, generated tables, and reproducibility materials are packaged for verification, but third-party raw datasets are not redistributed; full reconstruction and model refitting require obtaining the original logs separately per the README and data manifests.

Raw CAR-Hacking and Survival logs are not redistributed, so full dataset reconstruction and model refitting depend on users obtaining the original logs separately. The study is an audit of shortcut learning rather than a deployed detection system, and the temporal-convolutional-network check is bounded rather than an exhaustive architecture search.

Not stated.

[[Concept - CAN Intrusion Detection]], [[Concept - Shortcut Learning]], [[Concept - Benchmark Stress Testing]], [[Concept - Data Leakage Prevention]], [[Concept - In-Vehicle Network Security]]

Not stated.

Monitoring problem: frame-level CAN intrusion detection under shortcut learning and identifier/composition stress. Signal: CAN frame identifiers, timing, and payload features. Uncertainty method: fixed-identifier lookup controls, feature ablations, split-scheme contrasts, identifier/composition stress tests, cross-corpus transfer diagnostics, and a bounded temporal-convolutional-network sanity check. Action: audit and stress-test detector behavior. Evaluation setting: corrected reconstructions of CAR-Hacking and Survival datasets. Transfer to IVN: frame-level CAN ID and composition stress testing transfers directly to in-vehicle network intrusion detection benchmarking. Transfer risk: shortcut learning may cause detectors to rely on identifier artifacts that do not generalize across vehicle architectures or driving conditions.

doi: Not stated
source_link: Not stated
text_kind: repository/software record
monitoring_problem: frame-level CAN intrusion detection under shortcut learning and identifier/composition stress
signal: CAN frame identifiers, timing, and payload features
uncertainty_method: fixed-identifier lookup controls, feature ablations, chronological and random-frame splits, identifier/composition stress tests, cross-corpus transfer diagnostics, bounded temporal-convolutional-network sanity check
action: audit and stress-test detector behavior
eval_setting: corrected reconstructions of CAR-Hacking and Survival datasets
limitation_author: Full dataset reconstruction and model refitting require users to obtain the original CAR-Hacking and Survival logs separately; raw datasets are not redistributed
limitation_inference: The temporal-convolutional-network check is bounded and does not exhaustively cover detector architectures or deployment conditions
limitation_unknown: Not stated
support_passage: This study audits shortcut learning in frame-level Controller Area Network intrusion detection using corrected reconstructions of the CAR-Hacking and Survival datasets. It evaluates fixed-identifier lookup controls, timing and payload feature ablations, chronological and random-frame splits, identifier/composition stress tests, cross-corpus transfer diagnostics, and a bounded temporal-convolutional-network sanity check.
transfer_ivn: Frame-level CAN identifier and composition stress testing transfers directly to in-vehicle network intrusion detection benchmarking
transfer_risk: Shortcut learning may cause detectors to rely on identifier artifacts that do not generalize across vehicle architectures or driving conditions

#needs-review

## Record Fields
doi: https://doi.org/10.5281/zenodo.21536764
source_link: Not stated
text_kind: abstract
monitoring_problem: frame-level CAN intrusion detection under shortcut learning and identifier/composition stress. Signal: CAN frame identifiers, timing, and payload features. Uncertainty method: fixed-identifier lookup controls, feature ablations, split-scheme contrasts, identifier/composition stress tests, cross-corpus transfer diagnostics, and a bounded temporal-convolutional-network sanity check. Action: audit and stress-test detector behavior. Evaluation setting: corrected reconstructions of CAR-Hacking and Survival datasets. Transfer to IVN: frame-level CAN ID and composition stress testing transfers directly to in-vehicle network intrusion detection benchmarking. Transfer risk: shortcut learning may cause detectors to rely on identifier artifacts that do not generalize across vehicle architectures or driving conditions.
signal: CAN frame identifiers, timing, and payload features
uncertainty_method: fixed-identifier lookup controls, feature ablations, chronological and random-frame splits, identifier/composition stress tests, cross-corpus transfer diagnostics, bounded temporal-convolutional-network sanity check
action: audit and stress-test detector behavior
eval_setting: corrected reconstructions of CAR-Hacking and Survival datasets
limitation_author: Full dataset reconstruction and model refitting require users to obtain the original CAR-Hacking and Survival logs separately; raw datasets are not redistributed
limitation_inference: The temporal-convolutional-network check is bounded and does not exhaustively cover detector architectures or deployment conditions
limitation_unknown: Not stated
support_passage: This study audits shortcut learning in frame-level Controller Area Network intrusion detection using corrected reconstructions of the CAR-Hacking and Survival datasets. It evaluates fixed-identifier lookup controls, timing and payload feature ablations, chronological and random-frame splits, identifier/composition stress tests, cross-corpus transfer diagnostics, and a bounded temporal-convolutional-network sanity check.
transfer_ivn: Frame-level CAN identifier and composition stress testing transfers directly to in-vehicle network intrusion detection benchmarking
transfer_risk: Shortcut learning may cause detectors to rely on identifier artifacts that do not generalize across vehicle architectures or driving conditions
