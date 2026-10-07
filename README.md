# Viridian Assurance Research

Independent research on **AI evaluation validity, LLM-as-a-judge reliability, benchmark comparability, reproducibility, evaluator behaviour, provenance, and experimental assurance**.

Viridian Assurance asks a narrower question than ordinary model evaluation:

> **What does the available evidence actually justify claiming?**

This repository contains public technical notes, frozen analysis plans, result summaries, integrity records, and reproducibility material produced by Viridian. The aim is to make the evidential basis of published findings inspectable rather than asking readers to rely on a headline result.

## Technical notes

| Note | Study | Main result |
| --- | --- | --- |
| 001 | [Position Sensitivity in Pairwise LLM Judging](studies/001-position-sensitivity/) | 19/20 underlying preferences preserved under exact reversal; one second-position pattern; no systematic or directional bias established |
| 002 | [Evaluator Contract Stability](studies/002-evaluator-contract-stability/) | 0/20 winner-label disagreements under the tested semantically equivalent rubric formulations |
| 003 | [Presentation / Serialization Sensitivity](studies/003-presentation-serialization-sensitivity/) | 0/20 winner-label disagreements under the tested boundary-wrapper perturbations |

## Releases

- [Technical Note 001 — Position Sensitivity in Pairwise LLM Judging](https://github.com/ViridianAIQualityAssurance/viridian-assurance-research/releases/tag/study-001-v1)
- [Follow-up Studies 002–003 v1](https://github.com/ViridianAIQualityAssurance/viridian-assurance-research/releases/tag/studies-002-003-v1)

The 002–003 release includes the combined completed reproducibility package.

## Research sequence

Technical Note 001 is the parent **position-sensitivity** study. Notes 002 and 003 reuse the same frozen 20-prompt candidate sample from that study; they are **not independent replications of candidate generation**.

Note 001 found that exact response-order reversal preserved the preferred underlying response in 19/20 comparisons, with one observed second-position pattern. The manuscript explicitly withholds the stronger claim that GPT-5.6 Sol exhibits a systematic or directional position bias.

The completed follow-up runs in Notes 002 and 003 contain an important execution limitation: the frozen protocols requested fresh isolated judge contexts for each condition, but the completed judgments were performed by the same GPT-5.6 Sol judge within one conversation at the user's request. Shared judge state may increase cross-condition consistency and bias disagreement rates downward. This deviation is disclosed in each follow-up study directory and must travel with any citation of those results.

The maximum defensible conclusion from the two follow-ups is therefore narrow:

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

## Topics

This repository is relevant to work on:

**LLM-as-a-judge · LLM evaluation · AI evaluation · model evaluation · benchmarking · benchmark verification · evaluator reliability · position bias · reproducibility · provenance · experimental validity · experimental assurance**

## Repository structure

    studies/
      001-position-sensitivity/
      002-evaluator-contract-stability/
      003-presentation-serialization-sensitivity/

Study 001 contains its public research summary, frozen judge rubric, release notes, and selected artifact identities. Studies 002 and 003 additionally include their frozen analysis plans, completed analysis summaries, execution-deviation notes, integrity records, and analysis code.

## Citation

GitHub can generate a citation for this repository from [CITATION.cff](CITATION.cff). When citing an individual study, cite the relevant Technical Note and include the study-specific limitations stated in its README.

## Viridian Assurance

Independent experimental assurance for AI systems.

https://viridianassurance.com

> We do not sell certainty. We show you exactly what the evidence can justify.
