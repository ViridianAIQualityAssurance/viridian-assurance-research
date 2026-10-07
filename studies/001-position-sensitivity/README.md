# Technical Note 001 — Position Sensitivity in Pairwise LLM Judging

**We Tried to Reproduce LLM Judge Position Bias. The Evidence Wasn't Strong Enough.**

A controlled replication and experimental-assurance study of response-order sensitivity in pairwise LLM judging.

Author: Derry Mitchell  
Viridian  
5 October 2026  
Status: revised technical manuscript for public release; not peer reviewed.

[View the v1 GitHub release](https://github.com/ViridianAIQualityAssurance/viridian-assurance-research/releases/tag/study-001-v1)

## Research question

Does reversing the presentation order of two frozen candidate responses change the preferred underlying response under the tested GPT-5.6 Sol judge configuration?

The study uses a frozen 20-prompt response set. Two local candidate models generated one response per prompt, all forty response strings were frozen and hashed, and the same response pairs were then judged in an original orientation and an exact A/B reversal. A same-order repeat control was added before any judge outcome was observed.

## Result

- Same-order control agreement with Pass 1: **20/20 (100%)**
- Same underlying winner after exact reversal: **19/20 (95%)**
- Underlying winner changed after reversal: **1/20 (5%)**
- First-position patterns: **0/20**
- Second-position patterns: **1/20**
- Across the 40 formal orientation judgments, first position won **19** times and second position won **21** times.

The single changed pair was **P007**. The judge selected surface position B in both orientations; because the candidate strings were swapped, the preferred underlying response changed. This is a genuine second-position pattern in the paired record, but it is not sufficient evidence for a systematic or directional position bias.

## Maximum defensible claim

> Under the tested GPT-5.6 Sol judging configuration and frozen 20-prompt response set, reversing candidate presentation order preserved the underlying preferred response in 19 of 20 comparisons. One comparison exhibited a second-position preference pattern. This small study does not establish a systematic or directional position bias.

The evidence also does not establish the opposite claim that GPT-5.6 Sol is generally position-robust.

## Statistical boundary

The observed reversal switch rate was **1/20 = 5%**. The exact 95% Clopper-Pearson interval was approximately **0.1%–24.9%**, which is too wide to support a precise population-level estimate. The same-order control reproduced all 20 Pass 1 winner labels, but one repeat per prompt is not enough to estimate the full within-condition variability of the judge.

## Experimental identity

Candidate models:

- Jackrong/DeepSeek-V4-Pro-Qwen3.5-4B — architecture Qwen3_5ForConditionalGeneration
- K2 Horizon 3.7B — architecture K2HorizonForCausalLM

Candidate generation used local model-native chat templates, greedy decoding, max_new_tokens=256, BF16 with bitsandbytes 8-bit quantisation, SDPA attention, and device_map=auto.

The evaluator was GPT-5.6 Sol through ChatGPT using the frozen pairwise rubric. The judge-facing packet exposed only the evaluation identifier, user prompt, Response A, and Response B.

## Important limitations

- Only 20 prompt pairs were tested.
- Only one same-order repeat and one reversed judgment were obtained per prompt.
- The judge was accessed through ChatGPT rather than a pinned API snapshot with an exposed deterministic serving seed.
- Several candidate outputs were truncated by the 256-token generation ceiling.
- Some candidate outputs exposed meta-reasoning text.
- Candidate generation was not designed to support a general model-capability comparison.

These limitations constrain the claims they affect; they do not invalidate the exact response-order contrast because the same frozen response strings were reused across orientations.

## Osmium assurance execution

After the evidence package was frozen, Viridian Osmium evaluated the study using its qualified position-sensitivity procedure and returned **PARTIALLY_SUPPORTED**. That execution preserved the same maximum defensible claim.

This is a reproducibility/product-behaviour check on Viridian's assurance implementation, **not** an independent scientific replication and not additional evidence about GPT-5.6 Sol.

## Study materials

- [Frozen judge rubric](judge_rubric.md)
- [Selected artifact identities](integrity.md)
- [Release notes](RELEASE_NOTES.md)
- [Technical Note 002 — Evaluator Contract Stability](../002-evaluator-contract-stability/)
- [Technical Note 003 — Presentation / Serialization Sensitivity](../003-presentation-serialization-sensitivity/)

The source manuscript is Viridian Technical Note 001 dated 5 October 2026. The original DOCX is intentionally not included in this repository.
