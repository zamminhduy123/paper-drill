---
title: "Regime-Aware Deployment Validity of Flow-Based IDS"
year: 2026
doi: "https://doi.org/10.55525/tjst.1957896"
relevance_score: 8.0
type: paper
---
# Regime-Aware Deployment Validity of Flow-Based IDS

## Novelty
- Proposes a regime-aware deployment-validity evaluation protocol for flow-based IDS under temporal shift, attack-family novelty, and combined shift.
- Shows that near-perfect random-split benchmark performance can coexist with severe failures in future, family-novel, and combined-shift regimes.
- Compares flow-only, context-only, selected-context, and full-context XGBoost variants to isolate the effect of graph-derived context on transfer.

## Methodology
- Evaluates XGBoost IDS variants on CICIDS2017 and UNSW-NB15 using flow features and graph-derived context features.
- Uses regime composition, ablations, bootstrap confidence intervals, five-seed sensitivity for corrected family holdouts, diagnostic score distributions, precision-recall analyses, and approximate runtime.
- Tests random split, future/temporal regimes, family-novel holdouts, combined shift, and a record-disjoint UNSW-NB15 Generic/Exploits holdout.

## Explicit Limitations
- Not stated as a formal limitations section.
- Author-stated caveats: high random-split performance does not establish deployment readiness; temporal evaluation can mislead when attack-family structure is not separated; graph-context transfer varies by feature set and operating regime.
- Inferred limitations: Friday botnet distribution shift and the botnet-family holdout remain severe failures, with zero F1 and recall for several feature sets; full context can reduce transfer.

## Future Work
- Not stated.

## Concept Hubs
[[Concept - Intrusion Detection]] [[Concept - Network Traffic Analysis]] [[Concept - Cross-Dataset Evaluation]] [[Concept - Benchmark Stress Testing]] [[Concept - Context-Specific Outliers]]

## Relevance Score
8/10

## Monitoring Transfer
Monitoring problem: Determine whether a flow-based IDS remains valid when traffic regimes, attack families, and temporal distributions shift.
Signal: Flow features, graph-derived context features, diagnostic score distributions, precision-recall, F1, and recall.
Uncertainty method: Bootstrap confidence intervals and five-seed sensitivity for corrected family holdouts.
Resulting action: Select or reject IDS variants and context features by regime-specific performance, flag botnet-shift and family-novel failures, and avoid deployment decisions based only on random-split scores.
Evaluation setting: CICIDS2017 and UNSW-NB15 random split, future/temporal, family-novel, combined shift, and record-disjoint Generic/Exploits holdout.
Transfer to IVN: Apply the same regime-aware flow/context evaluation to in-vehicle network traffic, using ECU/DoIP/CAN flow features and context features to detect OOD attack families and temporal drift.
Transfer risk: Internet/enterprise graph-derived context may not transfer to constrained, protocol-specific IVN traffic, and IVN anomalies may be subtle or safety-critical, causing the same zero-recall failures under family-novel or botnet-like shift.

doi: not stated
source_link: not stated
text_kind: abstract
monitoring_problem: Determine whether a flow-based IDS remains valid under traffic regime shifts, novel attack families, and combined distributional change.
signal: Flow features, graph-derived context features, diagnostic score distributions, precision-recall, F1, and recall.
uncertainty_method: Bootstrap confidence intervals and five-seed sensitivity for corrected family holdouts.
action: Select or reject IDS variants and context features by regime-specific performance and flag severe botnet-shift and family-novel failures.
eval_setting: CICIDS2017 and UNSW-NB15 random split, future/temporal, family-novel, combined shift, and record-disjoint Generic/Exploits holdout.
limitation_author: not stated
limitation_inference: Friday botnet distribution shift and botnet-family holdout remain severe failures, with zero F1 and recall for several feature sets; full context can reduce transfer.
limitation_unknown: not stated
support_passage: The results demonstrate that high random-split performance does not establish deployment readiness; temporal evaluation can also mislead when attack-family structure is not separated, and graph-context transfer varies by feature set and operating regime.
transfer_ivn: Apply regime-aware flow/context IDS evaluation to in-vehicle network traffic using ECU/DoIP/CAN flow features and context features to detect OOD attack families and temporal drift.
transfer_risk: Internet/enterprise graph-derived context may not transfer to constrained, protocol-specific IVN traffic, and IVN anomalies may be subtle or safety-critical, causing zero-recall failures under family-novel or botnet-like shift.

#needs-review

## Record Fields
doi: https://doi.org/10.55525/tjst.1957896
source_link: not stated
text_kind: abstract
monitoring_problem: Determine whether a flow-based IDS remains valid when traffic regimes, attack families, and temporal distributions shift.
signal: Flow features, graph-derived context features, diagnostic score distributions, precision-recall, F1, and recall.
uncertainty_method: Bootstrap confidence intervals and five-seed sensitivity for corrected family holdouts.
action: Select or reject IDS variants and context features by regime-specific performance and flag severe botnet-shift and family-novel failures.
eval_setting: CICIDS2017 and UNSW-NB15 random split, future/temporal, family-novel, combined shift, and record-disjoint Generic/Exploits holdout.
limitation_author: not stated
limitation_inference: Friday botnet distribution shift and botnet-family holdout remain severe failures, with zero F1 and recall for several feature sets; full context can reduce transfer.
limitation_unknown: not stated
support_passage: The results demonstrate that high random-split performance does not establish deployment readiness; temporal evaluation can also mislead when attack-family structure is not separated, and graph-context transfer varies by feature set and operating regime.
transfer_ivn: Apply regime-aware flow/context IDS evaluation to in-vehicle network traffic using ECU/DoIP/CAN flow features and context features to detect OOD attack families and temporal drift.
transfer_risk: Internet/enterprise graph-derived context may not transfer to constrained, protocol-specific IVN traffic, and IVN anomalies may be subtle or safety-critical, causing the same zero-recall failures under family-novel or botnet-like shift.
