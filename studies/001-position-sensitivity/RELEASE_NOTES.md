# Release notes — Technical Note 001

## Viridian Technical Note 001 — Position Sensitivity in Pairwise LLM Judging

**We Tried to Reproduce LLM Judge Position Bias. The Evidence Wasn't Strong Enough.**

This release publishes Viridian's first technical note on response-order sensitivity in pairwise LLM judging.

### Main result

Under the tested GPT-5.6 Sol judging configuration and frozen 20-prompt response set, reversing candidate presentation order preserved the underlying preferred response in **19 of 20** comparisons.

One comparison, **P007**, exhibited a second-position preference pattern. The same-order control reproduced the Pass 1 winner in **20 of 20** comparisons.

The evidence does **not** establish systematic or directional position bias, and it also does not establish general position robustness.

### Statistical boundary

The observed reversal-switch rate was **1/20 = 5%**, with an exact 95% Clopper-Pearson interval of approximately **0.1%–24.9%**. This sample is too small to support a precise population-level estimate.

### Reproducibility

The repository contains:

- the public study summary;
- the frozen pairwise judge rubric;
- selected SHA-256 artifact identities;
- links to the study sequence used by later Technical Notes 002 and 003.

The original DOCX is intentionally not included in the GitHub repository. The human-readable repository materials are the public release surface.

### Status

Revised technical manuscript for public release; not peer reviewed.

Viridian Assurance  
https://viridianassurance.com
