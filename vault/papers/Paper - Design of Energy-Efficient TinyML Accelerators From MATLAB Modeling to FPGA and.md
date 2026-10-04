---
title: "Design of Energy-Efficient TinyML Accelerators: From MATLAB Modeling to FPGA and Embedded Deployment"
year: 2026
doi: "10.1109/ICCMC69250.2026.11625074"
relevance_score: 92.0
type: paper
---
# Design of Energy-Efficient TinyML Accelerators: From MATLAB Modeling to FPGA and Embedded Deployment

## Novelty
The paper proposes an end-to-end Algorithm-to-Bitstream TinyML workflow that couples MATLAB quantization-aware CNN design, Verilog RTL accelerator synthesis, Xilinx Artix-7 FPGA verification, and STM32F407 virtual-prototyping power profiling with DVFS.

## Methodology
The authors design a shallow INT8 CNN for MNIST under STM32F407 memory constraints, apply asymmetric affine quantization and batch-normalization folding, generate Verilog RTL using MATLAB Deep Learning HDL Toolbox, verify the accelerator on a Xilinx Artix-7 FPGA, and evaluate system-level power behavior on an STM32F407 virtual prototype using DVFS.

## Explicit Limitations
not stated

## Future Work
not stated

## Concept Hubs
[[Concept - Edge AI Inference]] [[Concept - Energy-Aware Inference]] [[Concept - TinyML Systems]] [[Concept - Resource-Constrained Edge]]

## Relevance Score
92

## Monitoring Transfer
doi: 10.1109/ICCMC69250.2026.11625074
source_link: not stated
text_kind: conference paper
monitoring_problem: energy consumption during edge TinyML inference
signal: power profile and idle operating states
uncertainty_method: not stated
action: apply DVFS to reduce power during idle states
eval_setting: Xilinx Artix-7 FPGA RTL/HIL and STM32F407 virtual prototyping on MNIST
limitation_author: not stated
limitation_inference: STM32 power profiling uses virtual prototyping; evaluation is limited to MNIST; DVFS is assessed for idle states
limitation_unknown: not stated
support_passage: Dynamic Voltage and Frequency Scaling (DVFS) effectively reduces power consumption during idle operating states.
transfer_ivn: deploy an INT8 CNN accelerator with DVFS on an in-vehicle ECU or FPGA for low-power network anomaly monitoring
transfer_risk: automotive IVN real-time safety, temperature, and certification constraints may invalidate virtual power profiling and latency assumptions

#needs-review

## Record Fields
doi: 10.1109/ICCMC69250.2026.11625074
source_link: not stated
text_kind: fulltext
monitoring_problem: energy consumption during edge TinyML inference
signal: power profile and idle operating states
uncertainty_method: not stated
action: apply DVFS to reduce power during idle states
eval_setting: Xilinx Artix-7 FPGA RTL/HIL and STM32F407 virtual prototyping on MNIST
limitation_author: not stated
limitation_inference: STM32 power profiling uses virtual prototyping; evaluation is limited to MNIST; DVFS is assessed for idle states
limitation_unknown: not stated
support_passage: Dynamic Voltage and Frequency Scaling (DVFS) effectively reduces power consumption during idle operating states.
transfer_ivn: deploy an INT8 CNN accelerator with DVFS on an in-vehicle ECU or FPGA for low-power network anomaly monitoring
transfer_risk: automotive IVN real-time safety, temperature, and certification constraints may invalidate virtual power profiling and latency assumptions
