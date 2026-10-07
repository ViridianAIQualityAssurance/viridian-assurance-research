# Viridian Assurance Research

Independent technical studies on experimental validity, evaluator behaviour, provenance, comparability, and the limits of claims made from AI evaluation evidence.

Viridian Assurance examines a narrower question than ordinary model evaluation: **what does the available evidence actually justify claiming?**

This repository contains public technical notes, frozen analysis plans, result summaries, and reproducibility material produced by Viridian. It is intended to make the evidential basis of published findings inspectable rather than asking readers to rely on a headline result.

## Technical notes

| Note | Study | Result |
| --- | --- | --- |
| 001 | Position sensitivity in pairwise LLM-as-a-judge evaluation | Published on the Viridian website |
| 002 | [Evaluator Contract Stability](studies/002-evaluator-contract-stability/) | 0/20 winner-label disagreements under the tested equivalent rubric formulations |
| 003 | [Presentation / Serialization Sensitivity](studies/003-presentation-serialization-sensitivity/) | 0/20 winner-label disagreements under the tested boundary-wrapper perturbations |

## Interpretation

Notes 002 and 003 reuse the same frozen 20-prompt candidate sample from the parent position-sensitivity study. They are **not independent replications of candidate generation**.

The completed follow-up runs also contain an important execution limitation: the preregistered protocols requested fresh isolated judge contexts for each condition, but the completed judgments were performed by the same GPT-5.6 Sol judge within one conversation at the user's request. Shared judge state may increase cross-condition consistency and bias disagreement rates downward. This deviation is disclosed in each study directory and must travel with any citation of the results.

The maximum defensible conclusion from these two follow-ups is therefore narrow:

> In this single-judge execution on the fixed 20-prompt sample, neither the tested semantically equivalent rubric reformulations nor the tested response-boundary serialization changed any pairwise winner decision.

These studies do **not** establish a general 0% sensitivity rate for LLM judges.

## Evidence standard

Viridian separates:

- observed result from interpretation;
- absence of evidence from evidence of absence;
- model/evaluator identity from substantive outcome;
- descriptive findings from causal claims;
- preregistered endpoints from post-hoc observations;
- protocol-compliant evidence from evidence affected by deviations.

Where a limitation changes the maximum defensible claim, it is reported rather than hidden.

## Repository structure

```text
studies/
  002-evaluator-contract-stability/
  003-presentation-serialization-sensitivity/
```

Each study directory includes the public study note, frozen analysis plan, analysis summary, execution note, and integrity metadata.

## Viridian Assurance

Independent experimental assurance for AI systems.

https://viridianassurance.com

> We do not sell certainty. We show you exactly what the evidence can justify.
