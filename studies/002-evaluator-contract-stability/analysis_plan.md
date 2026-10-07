# Pre-judgment analysis plan — evaluator_contract_stability_v1

Created UTC: 2026-10-07T09:00:51.494340+00:00

## Research question

For the same 20 prompts, exact candidate response texts, and fixed A/B orientation inherited from `position_bias_v1` Condition 1, how stable are pairwise winner labels under two rubric formulations intended to preserve the same substantive decision criteria?

## Conditions

- **R0A** — original frozen rubric; reference repeat.
- **R0B** — exact same original rubric and exact same response orientation/texts, independently shuffled item order; repeat-control estimate.
- **R1** — the same six criteria and decision/output rules, with criteria reordered.
- **R2** — the same six criteria and decision/output rules, compactly restated.

Each condition was intended to be judged in a separate fresh context. The judge must not see `mapping.json`, another condition's results, or any previous result while judging a condition. Candidate response text must not be edited.

## Primary endpoints

Using prompt ID as the pairing key:

1. Winner-label disagreement proportion R0B vs R0A.
2. Winner-label disagreement proportion R1 vs R0A.
3. Winner-label disagreement proportion R2 vs R0A.
4. Descriptive excess disagreement for each perturbed rubric: perturbation disagreement minus R0B-vs-R0A disagreement.

A TIE is a winner label and disagreements involving a TIE count as disagreement.

## Item classification

- `CONTROL_UNSTABLE`: R0A != R0B.
- `STABLE_ACROSS_TESTED_RUBRICS`: R0A == R0B == R1 == R2.
- `RUBRIC_SENSITIVE`: control repeats agree but at least one of R1/R2 differs.

## Secondary endpoints

- A/B/TIE counts by condition.
- Mean and median reported confidence by condition.
- After unblinding: Qwen3.5 4B wins, K2 Horizon 3.7B wins, and ties by condition.
- Exact prompt IDs that change winner label in R1 or R2 relative to the stable control reference.
- Whether the aggregate model winner across the 20 prompts changes by rubric condition.

## Reporting limits

This is a 20-prompt reused candidate sample, not an independent replication of candidate generation. Results are descriptive only. Do not generalize to all LLM judges, all rubrics, or all tasks.
