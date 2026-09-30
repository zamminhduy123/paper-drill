---
title: "On the Instance Hardness as a Decision Criterion in TinyML Systems"
year: 2026
doi: "https://doi.org/10.48550/arxiv.2608.29913"
relevance_score: 7.65
type: paper
---
# On the Instance Hardness as a Decision Criterion in TinyML Systems

Novelty

Applies tree depth prune instance hardness method to TinyML systems, using instance hardness as a decision criterion for threshold control; demonstrates that energy consumption can be adjusted with limited classification quality changes.

Methodology

Tree depth prune instance hardness method applied to TinyML inference; threshold control used to adjust classification accuracy, thereby influencing computational complexity and energy consumption for inference; presented as preliminary work-in-progress with initial results as proof of concept.

Explicit Limitations

Preliminary findings only; work in progress; initial results serve as proof of concept.

Future Work

Not stated.

Concept Hubs

[[Concept - Instance Hardness]]
[[Concept - TinyML Systems]]
[[Concept - Tree Depth Pruning]]
[[Concept - Energy-Aware Inference]]
[[Concept - Threshold Control]]

Relevance Score

Not stated.

Monitoring Transfer

Monitoring problem: Energy consumption and computational cost of inference on resource-constrained edge devices.
Signal: Instance hardness of samples under tree depth prune method.
Uncertainty method: Threshold control over instance hardness criterion.
Resulting action: Adjust classification threshold to trade off accuracy against computational complexity and energy consumption.
Evaluation setting: TinyML systems on devices with limited memory and computing resources; preliminary proof-of-concept results.

One transfer to IVN: Energy-aware threshold control could be adapted to in-vehicle network intrusion detection nodes, adjusting detection thresholds to manage compute/energy budgets on constrained automotive ECUs.
One reason the transfer may fail: Instance hardness distributions and energy-accuracy trade-offs in TinyML classification may not hold for high-speed, streaming CAN traffic where attack instances are rare and latency constraints are strict.

doi: not stated
source_link: not stated
text_kind: research abstract
monitoring_problem: Energy consumption and computational cost of AI inference on resource-constrained edge devices
signal: Instance hardness of samples under tree depth prune method
uncertainty_method: Threshold control over instance hardness criterion
action: Adjust classification threshold to trade off accuracy against computational complexity and energy consumption
eval_setting: TinyML systems on devices with limited memory and computing resources; preliminary proof-of-concept results
limitation_author: Preliminary findings; work in progress; initial results as proof of concept
limitation_inference: No quantitative results, datasets, or baselines reported; energy-accuracy trade-off magnitude unknown
limitation_unknown: Dataset, model architecture, hardware platform, and evaluation metrics not stated
support_passage: The results indicate that threshold control can change energy consumption with limited classification quality changes. This method allows us to adjust classification accuracy, thereby influencing computational complexity and energy consumption for inference.
transfer_ivn: Energy-aware threshold control could be adapted to in-vehicle network intrusion detection nodes, adjusting detection thresholds to manage compute/energy budgets on constrained automotive ECUs
transfer_risk: Instance hardness distributions and energy-accuracy trade-offs in TinyML classification may not hold for high-speed, streaming CAN traffic where attack instances are rare and latency constraints are strict

Applies tree depth prune instance hardness method to TinyML systems, using instance hardness as a decision criterion for threshold control; demonstrates that energy consumption can be adjusted with limited classification quality changes.

Tree depth prune instance hardness method applied to TinyML inference; threshold control used to adjust classification accuracy, thereby influencing computational complexity and energy consumption for inference; presented as preliminary work-in-progress with initial results as proof of concept.

Preliminary findings only; work in progress; initial results serve as proof of concept.

Not stated.

[[Concept - Instance Hardness]]
[[Concept - TinyML Systems]]
[[Concept - Tree Depth Pruning]]
[[Concept - Energy-Aware Inference]]
[[Concept - Threshold Control]]

Not stated.

Monitoring problem: Energy consumption and computational cost of inference on resource-constrained edge devices.
Signal: Instance hardness of samples under tree depth prune method.
Uncertainty method: Threshold control over instance hardness criterion.
Resulting action: Adjust classification threshold to trade off accuracy against computational complexity and energy consumption.
Evaluation setting: TinyML systems on devices with limited memory and computing resources; preliminary proof-of-concept results.

One transfer to IVN: Energy-aware threshold control could be adapted to in-vehicle network intrusion detection nodes, adjusting detection thresholds to manage compute/energy budgets on constrained automotive ECUs.
One reason the transfer may fail: Instance hardness distributions and energy-accuracy trade-offs in TinyML classification may not hold for high-speed, streaming CAN traffic where attack instances are rare and latency constraints are strict.

doi: not stated
source_link: not stated
text_kind: research abstract
monitoring_problem: Energy consumption and computational cost of AI inference on resource-constrained edge devices
signal: Instance hardness of samples under tree depth prune method
uncertainty_method: Threshold control over instance hardness criterion
action: Adjust classification threshold to trade off accuracy against computational complexity and energy consumption
eval_setting: TinyML systems on devices with limited memory and computing resources; preliminary proof-of-concept results
limitation_author: Preliminary findings; work in progress; initial results as proof of concept
limitation_inference: No quantitative results, datasets, or baselines reported; energy-accuracy trade-off magnitude unknown
limitation_unknown: Dataset, model architecture, hardware platform, and evaluation metrics not stated
support_passage: The results indicate that threshold control can change energy consumption with limited classification quality changes. This method allows us to adjust classification accuracy, thereby influencing computational complexity and energy consumption for inference.
transfer_ivn: Energy-aware threshold control could be adapted to in-vehicle network intrusion detection nodes, adjusting detection thresholds to manage compute/energy budgets on constrained automotive ECUs
transfer_risk: Instance hardness distributions and energy-accuracy trade-offs in TinyML classification may not hold for high-speed, streaming CAN traffic where attack instances are rare and latency constraints are strict

#needs-review

## Record Fields
doi: https://doi.org/10.48550/arxiv.2608.29913
source_link: not stated
text_kind: abstract
monitoring_problem: Energy consumption and computational cost of inference on resource-constrained edge devices.
signal: Instance hardness of samples under tree depth prune method.
uncertainty_method: Threshold control over instance hardness criterion.
action: Adjust classification threshold to trade off accuracy against computational complexity and energy consumption
eval_setting: TinyML systems on devices with limited memory and computing resources; preliminary proof-of-concept results
limitation_author: Preliminary findings; work in progress; initial results as proof of concept
limitation_inference: No quantitative results, datasets, or baselines reported; energy-accuracy trade-off magnitude unknown
limitation_unknown: Dataset, model architecture, hardware platform, and evaluation metrics not stated
support_passage: The results indicate that threshold control can change energy consumption with limited classification quality changes. This method allows us to adjust classification accuracy, thereby influencing computational complexity and energy consumption for inference.
transfer_ivn: Energy-aware threshold control could be adapted to in-vehicle network intrusion detection nodes, adjusting detection thresholds to manage compute/energy budgets on constrained automotive ECUs
transfer_risk: Instance hardness distributions and energy-accuracy trade-offs in TinyML classification may not hold for high-speed, streaming CAN traffic where attack instances are rare and latency constraints are strict
