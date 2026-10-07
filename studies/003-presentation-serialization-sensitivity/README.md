# Technical Note 003 — Presentation / Serialization Sensitivity

## Question

For the same 20 prompts, exact substantive candidate response strings, and fixed A/B orientation inherited from the parent position-sensitivity study, does adding a standardized, semantically inert boundary wrapper to one candidate change pairwise judge decisions?

[View the combined 002–003 v1 release](https://github.com/ViridianAIQualityAssurance/viridian-assurance-research/releases/tag/studies-002-003-v1)

The wrapper was:

    <<<BEGIN CANDIDATE RESPONSE>>>
    <unchanged response text>
    <<<END CANDIDATE RESPONSE>>>

No character inside the original response text was edited, removed, normalized, or reordered.

## Conditions

- **P0** — neither response wrapped.
- **PA** — Response A only wrapped.
- **PB** — Response B only wrapped.
- **PAB** — both responses wrapped.

All four conditions used the same original frozen pairwise rubric.

## Result

Across this completed execution:

- PA vs P0: **0/20 disagreements**
- PB vs P0: **0/20 disagreements**
- PAB vs P0: **0/20 disagreements**
- Classification: **20/20 CONTENT_STABLE**
- Every condition produced **15 Qwen wins, 5 K2 wins, 0 ties**
- Mean reported confidence: **0.920**
- Median reported confidence: **0.960**

## Maximum defensible claim

> In this single-judge execution on this fixed 20-prompt sample, the tested response-boundary serialization did not change any pairwise winner decision.

This does **not** establish a general 0% presentation-sensitivity rate.

## Protocol deviation

The frozen plan required a fresh isolated judge context for every condition. At the user's explicit request, all conditions were judged by the same GPT-5.6 Sol instance in one conversation. Shared context may increase cross-condition consistency and bias disagreement rates downward.

Accordingly, this completed run should be treated as an **exploratory/operational execution of the frozen protocol**, not a clean confirmatory test of between-context presentation sensitivity.

## Study materials

- [Frozen analysis plan](analysis_plan.md)
- [Analysis summary](analysis_summary.md)
- [Judge execution note](judge_execution_note.md)
- [Integrity record](integrity.md)
- [Parent study — Technical Note 001](../001-position-sensitivity/)
- [Technical Note 002 — Evaluator Contract Stability](../002-evaluator-contract-stability/)
