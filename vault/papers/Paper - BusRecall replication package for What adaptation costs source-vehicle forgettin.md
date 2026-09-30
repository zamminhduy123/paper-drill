---
title: "BusRecall: replication package for "What adaptation costs: source-vehicle forgetting in cross-vehicle CAN intrusion detection""
year: 2026
doi: "https://doi.org/10.5281/zenodo.21889099"
relevance_score: 4.0
type: paper
---
# BusRecall: replication package for "What adaptation costs: source-vehicle forgetting in cross-vehicle CAN intrusion detection"

Novelty

The replication package provides code and result files for the first systematic study of catastrophic forgetting in cross-vehicle CAN intrusion detection, quantifying source-vehicle forgetting when adapting detectors to a new vehicle and comparing continual-learning remedies across all 24 task orders on two independent corpora.

Methodology

Reproduces every table and figure of the paper: (1) the cross-vehicle collapse and its three controls, (2) a continual-learning comparison over all 24 task orders on can-train-and-test and the ORNL ROAD dataset, (3) a diagnostic measurement of the distillation teacher on the target vehicle, and (4) a memory-budget curve. The two public datasets are not redistributed; the README supplies their DOIs and the cache-building pipeline.

Explicit Limitations

Datasets are public and not redistributed, so reproduction depends on external access and the documented cache pipeline; the package scope is limited to the paper's tables and figures.

Future Work

Not stated.

Concept Hubs

[[Concept - CAN Intrusion Detection]]
[[Concept - Cross-Vehicle Transfer Learning]]
[[Concept - Continual Learning]]
[[Concept - Catastrophic Forgetting]]
[[Concept - Knowledge Distillation]]

Relevance Score

4

Monitoring Transfer

Monitoring problem, signal, uncertainty method, resulting action, evaluation setting. One transfer to IVN and one reason the transfer may fail.

doi: not stated
source_link: not stated
text_kind: replication package
monitoring_problem: source-vehicle forgetting when a CAN intrusion detector is adapted to a new vehicle
signal: CAN bus traffic from source and target vehicles
uncertainty_method: not stated
action: adapt intrusion detection models across vehicles and apply continual-learning remedies
eval_setting: all 24 task orders on two independent corpora, can-train-and-test and the ORNL ROAD dataset
limitation_author: datasets are public and not redistributed; README gives DOIs and cache-building pipeline
limitation_inference: reproduction requires external dataset access and correct execution of the cache pipeline
limitation_unknown: not stated
support_passage: The package reproduces every table and figure in the paper: the cross-vehicle collapse and its three controls, the continual-learning comparison over all 24 task orders on two independent corpora.
transfer_ivn: cross-vehicle CAN intrusion detection is an in-vehicle network security task, so forgetting-aware adaptation transfers directly to IVN monitoring
transfer_risk: vehicle-specific signal distributions can make learned intrusion cues vehicle-bound, so adaptation may erase source-vehicle knowledge and fail on the original vehicle

The replication package provides code and result files for the first systematic study of catastrophic forgetting in cross-vehicle CAN intrusion detection, quantifying source-vehicle forgetting when adapting detectors to a new vehicle and comparing continual-learning remedies across all 24 task orders on two independent corpora.

Reproduces every table and figure of the paper: (1) the cross-vehicle collapse and its three controls, (2) a continual-learning comparison over all 24 task orders on can-train-and-test and the ORNL ROAD dataset, (3) a diagnostic measurement of the distillation teacher on the target vehicle, and (4) a memory-budget curve. The two public datasets are not redistributed; the README supplies their DOIs and the cache-building pipeline.

Datasets are public and not redistributed, so reproduction depends on external access and the documented cache pipeline; the package scope is limited to the paper's tables and figures.

Not stated.

[[Concept - CAN Intrusion Detection]]
[[Concept - Cross-Vehicle Transfer Learning]]
[[Concept - Continual Learning]]
[[Concept - Catastrophic Forgetting]]
[[Concept - Knowledge Distillation]]

4

Monitoring problem, signal, uncertainty method, resulting action, evaluation setting. One transfer to IVN and one reason the transfer may fail.

doi: not stated
source_link: not stated
text_kind: replication package
monitoring_problem: source-vehicle forgetting when a CAN intrusion detector is adapted to a new vehicle
signal: CAN bus traffic from source and target vehicles
uncertainty_method: not stated
action: adapt intrusion detection models across vehicles and apply continual-learning remedies
eval_setting: all 24 task orders on two independent corpora, can-train-and-test and the ORNL ROAD dataset
limitation_author: datasets are public and not redistributed; README gives DOIs and cache-building pipeline
limitation_inference: reproduction requires external dataset access and correct execution of the cache pipeline
limitation_unknown: not stated
support_passage: The package reproduces every table and figure in the paper: the cross-vehicle collapse and its three controls, the continual-learning comparison over all 24 task orders on two independent corpora.
transfer_ivn: cross-vehicle CAN intrusion detection is an in-vehicle network security task, so forgetting-aware adaptation transfers directly to IVN monitoring
transfer_risk: vehicle-specific signal distributions can make learned intrusion cues vehicle-bound, so adaptation may erase source-vehicle knowledge and fail on the original vehicle

#needs-review

## Record Fields
doi: https://doi.org/10.5281/zenodo.21889099
source_link: not stated
text_kind: abstract
monitoring_problem: source-vehicle forgetting when a CAN intrusion detector is adapted to a new vehicle
signal: CAN bus traffic from source and target vehicles
uncertainty_method: not stated
action: adapt intrusion detection models across vehicles and apply continual-learning remedies
eval_setting: all 24 task orders on two independent corpora, can-train-and-test and the ORNL ROAD dataset
limitation_author: datasets are public and not redistributed; README gives DOIs and cache-building pipeline
limitation_inference: reproduction requires external dataset access and correct execution of the cache pipeline
limitation_unknown: not stated
support_passage: The package reproduces every table and figure in the paper: the cross-vehicle collapse and its three controls, the continual-learning comparison over all 24 task orders on two independent corpora.
transfer_ivn: cross-vehicle CAN intrusion detection is an in-vehicle network security task, so forgetting-aware adaptation transfers directly to IVN monitoring
transfer_risk: vehicle-specific signal distributions can make learned intrusion cues vehicle-bound, so adaptation may erase source-vehicle knowledge and fail on the original vehicle
