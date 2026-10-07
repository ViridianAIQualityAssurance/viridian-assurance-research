# Technical Note 002 — Evaluator Contract Stability

## Question

For the same 20 prompts, exact candidate response texts, and fixed A/B orientation inherited from the parent position-sensitivity study, do pairwise winner labels change when the rubric is reformulated without intentionally changing its substantive criteria?

[View the combined 002–003 v1 release](https://github.com/ViridianAIQualityAssurance/viridian-assurance-research/releases/tag/studies-002-003-v1)

## Conditions

- **R0A** — original frozen rubric.
- **R0B** — exact same rubric and response orientation/text, with independently shuffled item order.
- **R1** — same six criteria and decision/output rules, criteria reordered.
- **R2** — same six criteria and decision/output rules, compactly restated.

No candidate generation was repeated.

## Result

Across this completed execution:

- R0B vs R0A: **0/20 disagreements**
- R1 vs R0A: **0/20 disagreements**
- R2 vs R0A: **0/20 disagreements**
- Every condition produced **15 Qwen wins, 5 K2 wins, 0 ties**
- Mean reported confidence: **0.920**
- Median reported confidence: **0.960**

## Maximum defensible claim

> In this single-judge execution on this fixed 20-prompt sample, the tested semantically equivalent rubric reformulations did not change any pairwise winner decision.

This does **not** establish that equivalent rubric reformulations generally have zero effect.

## Protocol deviation

The frozen plan required a fresh isolated judge context for every condition. At the user's explicit request, all conditions were judged by the same GPT-5.6 Sol instance in one conversation. Shared context may increase cross-condition consistency and bias disagreement rates downward.

Accordingly, this completed run should be treated as an **exploratory/operational execution of the frozen protocol**, not a clean confirmatory test of between-context evaluator instability.

## Study materials

- [Frozen analysis plan](analysis_plan.md)
- [Analysis summary](analysis_summary.md)
- [Judge execution note](judge_execution_note.md)
- [Integrity record](integrity.md)
- [Parent study — Technical Note 001](../001-position-sensitivity/)
- [Technical Note 003 — Presentation / Serialization Sensitivity](../003-presentation-serialization-sensitivity/)
