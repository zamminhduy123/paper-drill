---
title: "FPGA validated RISC V system on chip with a custom systolic array accelerator for edge AI inference"
year: 2026
doi: "https://doi.org/10.1007/s44163-026-02003-7"
relevance_score: 5.11
type: paper
---
# FPGA validated RISC V system on chip with a custom systolic array accelerator for edge AI inference

Novelty

A complete FPGA-validated RISC-V SoC that pairs a five-stage RV32IM processor with a custom 4×4 output-stationary systolic MAC array, using memory-mapped registers instead of custom opcodes so existing toolchains stay unmodified. It targets the low-cost Artix-7 XC7A35T without an embedded ARM host and combines plain Verilog source, DMA-driven operand/result movement, and a closed-form performance model that matches measured results.

Methodology

An AXI4 crossbar connects the RV32IM core and the systolic accelerator; a scatter–gather DMA engine moves operand tiles and results while the processor handles control. Processing elements take INT8 quantised inputs sign-extended to 18 bits to fit the DSP48E1 multiplier port, with 64-bit accumulators to prevent overflow across a full tile. A 4×4 matrix multiply completes in 320 ns at 100 MHz (1.16 GOPS compute-phase throughput); the systolic compute phase is 3N−1 = 11 cycles (110 ns). Validation used Vivado XSim simulation and on-board runs on a Digilent Basys 3. Post-place-and-route: 39.5% LUTs (8214/20,800), 17.8% DSP48E1 (16/90), 16.0% BRAM (8/50), 148 mW total on-chip power, 7.86 GOPS/W compute-phase efficiency. Two propositions are formally proved: output-stationary scheduling reduces computation cycles by Θ(N²/3) versus naïve unblocked sequential CPU execution, and gives a factor-N reduction in weight-memory reads under the same baseline.

Explicit Limitations

Power, DMA-overlap, and sustained-throughput figures are estimates from Vivado post-implementation analysis and the analytical performance model, not direct on-board measurements. Functional correctness is validated on physical silicon, but those quantitative metrics are not measured on hardware.

Future Work

Not stated.

Concept Hubs

[[Concept - TinyML Systems]]
[[Concept - Energy-Aware Inference]]
[[Concept - Embedded Systems]]
[[Concept - Real-Time Telemetry]]
[[Concept - Open Architecture]]

Relevance Score

Not stated.

Monitoring Transfer

Monitoring problem: Running deep-learning inference on resource-constrained edge hardware where latency and memory traffic must both be cut, not traded off.
Signal: Compute-phase throughput (GOPS), end-to-end tile latency (ns), compute-phase efficiency (GOPS/W), and post-implementation resource utilisation (LUT, DSP48E1, BRAM).
Uncertainty method: Formal proof of two scheduling propositions plus cross-checking of a closed-form analytical performance model against XSim simulation and on-board measured numbers.
Action: Instantiate a memory-mapped systolic-array accelerator alongside a RISC-V core with DMA-driven tiling, rather than extending the ISA with custom opcodes, so existing toolchains need no modification.
Eval setting: Vivado XSim simulation and on-board runs on a Digilent Basys 3 board with a Xilinx Artix-7 XC7A35T, benchmarked on 4×4 matrix multiply at 100 MHz.

doi: not stated
source_link: not stated
text_kind: research paper (abstract)
monitoring_problem: deep-learning inference on constrained edge hardware needing simultaneous reduction of latency and memory traffic
signal: compute-phase throughput in GOPS, end-to-end tile latency in ns, GOPS/W efficiency, LUT/DSP/BRAM utilisation, on-chip power
uncertainty_method: formal proof of scheduling propositions; closed-form analytical performance model matched against simulation and measured results
action: memory-mapped systolic-array accelerator coupled to RISC-V via AXI4 crossbar with scatter–gather DMA, avoiding custom opcodes
eval_setting: Vivado XSim simulation and on-board Digilent Basys 3 (Artix-7 XC7A35T) runs at 100 MHz on 4×4 matrix multiply
limitation_author: power, DMA-overlap, and sustained-throughput figures are estimates from Vivado post-implementation analysis and the analytical model rather than direct on-board measurement
limitation_inference: no comparison against other RISC-V accelerator baselines on the same device; no sustained end-to-end throughput measurement under real workloads; only a 4×4 matrix multiply is reported
limitation_unknown: whether sustained throughput and power hold under continuous real inference workloads; behaviour beyond the 4×4 tile size
support_passage: Both Vivado XSim simulation and on-board runs confirm that a 4×4 matrix multiply finishes in 320 ns at 100 MHz, giving a compute-phase throughput of 1.16 GOPS.
transfer_ivn: a memory-mapped, DMA-driven accelerator with an unmodified toolchain and a closed-form latency/energy model could be repurposed as an in-vehicle network edge inference node for real-time CAN or V2X traffic classification on low-cost FPGAs
transfer_risk: the design is validated only on 4×4 matrix multiply with estimated power and sustained-throughput figures, so in-vehicle workloads with irregular or streaming traffic patterns may not achieve the modelled latency and energy on the Artix-7

A complete FPGA-validated RISC-V SoC that pairs a five-stage RV32IM processor with a custom 4×4 output-stationary systolic MAC array, using memory-mapped registers instead of custom opcodes so existing toolchains stay unmodified. It targets the low-cost Artix-7 XC7A35T without an embedded ARM host and combines plain Verilog source, DMA-driven operand/result movement, and a closed-form performance model that matches measured results.

An AXI4 crossbar connects the RV32IM core and the systolic accelerator; a scatter–gather DMA engine moves operand tiles and results while the processor handles control. Processing elements take INT8 quantised inputs sign-extended to 18 bits to fit the DSP48E1 multiplier port, with 64-bit accumulators to prevent overflow across a full tile. A 4×4 matrix multiply completes in 320 ns at 100 MHz (1.16 GOPS compute-phase throughput); the systolic compute phase is 3N−1 = 11 cycles (110 ns). Validation used Vivado XSim simulation and on-board runs on a Digilent Basys 3. Post-place-and-route: 39.5% LUTs (8214/20,800), 17.8% DSP48E1 (16/90), 16.0% BRAM (8/50), 148 mW total on-chip power, 7.86 GOPS/W compute-phase efficiency. Two propositions are formally proved: output-stationary scheduling reduces computation cycles by Θ(N²/3) versus naïve unblocked sequential CPU execution, and gives a factor-N reduction in weight-memory reads under the same baseline.

Power, DMA-overlap, and sustained-throughput figures are estimates from Vivado post-implementation analysis and the analytical performance model, not direct on-board measurements. Functional correctness is validated on physical silicon, but those quantitative metrics are not measured on hardware.

Not stated.

[[Concept - TinyML Systems]]
[[Concept - Energy-Aware Inference]]
[[Concept - Embedded Systems]]
[[Concept - Real-Time Telemetry]]
[[Concept - Open Architecture]]

Not stated.

Monitoring problem: Running deep-learning inference on resource-constrained edge hardware where latency and memory traffic must both be cut, not traded off.
Signal: Compute-phase throughput (GOPS), end-to-end tile latency (ns), compute-phase efficiency (GOPS/W), and post-implementation resource utilisation (LUT, DSP48E1, BRAM).
Uncertainty method: Formal proof of two scheduling propositions plus cross-checking of a closed-form analytical performance model against XSim simulation and on-board measured numbers.
Action: Instantiate a memory-mapped systolic-array accelerator alongside a RISC-V core with DMA-driven tiling, rather than extending the ISA with custom opcodes, so existing toolchains need no modification.
Eval setting: Vivado XSim simulation and on-board runs on a Digilent Basys 3 board with a Xilinx Artix-7 XC7A35T, benchmarked on 4×4 matrix multiply at 100 MHz.

doi: not stated
source_link: not stated
text_kind: research paper (abstract)
monitoring_problem: deep-learning inference on constrained edge hardware needing simultaneous reduction of latency and memory traffic
signal: compute-phase throughput in GOPS, end-to-end tile latency in ns, GOPS/W efficiency, LUT/DSP/BRAM utilisation, on-chip power
uncertainty_method: formal proof of scheduling propositions; closed-form analytical performance model matched against simulation and measured results
action: memory-mapped systolic-array accelerator coupled to RISC-V via AXI4 crossbar with scatter–gather DMA, avoiding custom opcodes
eval_setting: Vivado XSim simulation and on-board Digilent Basys 3 (Artix-7 XC7A35T) runs at 100 MHz on 4×4 matrix multiply
limitation_author: power, DMA-overlap, and sustained-throughput figures are estimates from Vivado post-implementation analysis and the analytical model rather than direct on-board measurement
limitation_inference: no comparison against other RISC-V accelerator baselines on the same device; no sustained end-to-end throughput measurement under real workloads; only a 4×4 matrix multiply is reported
limitation_unknown: whether sustained throughput and power hold under continuous real inference workloads; behaviour beyond the 4×4 tile size
support_passage: Both Vivado XSim simulation and on-board runs confirm that a 4×4 matrix multiply finishes in 320 ns at 100 MHz, giving a compute-phase throughput of 1.16 GOPS.
transfer_ivn: a memory-mapped, DMA-driven accelerator with an unmodified toolchain and a closed-form latency/energy model could be repurposed as an in-vehicle network edge inference node for real-time CAN or V2X traffic classification on low-cost FPGAs
transfer_risk: the design is validated only on 4×4 matrix multiply with estimated power and sustained-throughput figures, so in-vehicle workloads with irregular or streaming traffic patterns may not achieve the modelled latency and energy on the Artix-7

#needs-review

## Record Fields
doi: https://doi.org/10.1007/s44163-026-02003-7
source_link: not stated
text_kind: abstract
monitoring_problem: Running deep-learning inference on resource-constrained edge hardware where latency and memory traffic must both be cut, not traded off.
signal: Compute-phase throughput (GOPS), end-to-end tile latency (ns), compute-phase efficiency (GOPS/W), and post-implementation resource utilisation (LUT, DSP48E1, BRAM).
uncertainty_method: Formal proof of two scheduling propositions plus cross-checking of a closed-form analytical performance model against XSim simulation and on-board measured numbers.
action: Instantiate a memory-mapped systolic-array accelerator alongside a RISC-V core with DMA-driven tiling, rather than extending the ISA with custom opcodes, so existing toolchains need no modification.
eval_setting: Vivado XSim simulation and on-board runs on a Digilent Basys 3 board with a Xilinx Artix-7 XC7A35T, benchmarked on 4×4 matrix multiply at 100 MHz.
limitation_author: power, DMA-overlap, and sustained-throughput figures are estimates from Vivado post-implementation analysis and the analytical model rather than direct on-board measurement
limitation_inference: no comparison against other RISC-V accelerator baselines on the same device; no sustained end-to-end throughput measurement under real workloads; only a 4×4 matrix multiply is reported
limitation_unknown: whether sustained throughput and power hold under continuous real inference workloads; behaviour beyond the 4×4 tile size
support_passage: Both Vivado XSim simulation and on-board runs confirm that a 4×4 matrix multiply finishes in 320 ns at 100 MHz, giving a compute-phase throughput of 1.16 GOPS.
transfer_ivn: a memory-mapped, DMA-driven accelerator with an unmodified toolchain and a closed-form latency/energy model could be repurposed as an in-vehicle network edge inference node for real-time CAN or V2X traffic classification on low-cost FPGAs
transfer_risk: the design is validated only on 4×4 matrix multiply with estimated power and sustained-throughput figures, so in-vehicle workloads with irregular or streaming traffic patterns may not achieve the modelled latency and energy on the Artix-7
