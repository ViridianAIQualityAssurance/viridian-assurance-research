# Pre-judgment analysis plan — presentation_serialization_sensitivity_v1

Created UTC: 2026-10-07T09:00:51.494340+00:00

## Research question

For the same 20 prompts, exact substantive candidate response strings, and fixed A/B orientation inherited from `position_bias_v1` Condition 1, does adding a standardized, semantically inert boundary wrapper to one candidate change pairwise judge decisions?

The wrapper is exactly:

```text
<<<BEGIN CANDIDATE RESPONSE>>>
<unchanged response text>
<<<END CANDIDATE RESPONSE>>>
```

No character inside the original response text is edited, removed, normalized, or reordered.

## Conditions

- **P0** — neither response wrapped.
- **PA** — Response A only wrapped.
- **PB** — Response B only wrapped.
- **PAB** — both responses wrapped.

All conditions use the exact original frozen pairwise rubric. Each condition was intended to be judged in a separate fresh context.

## Primary endpoints

1. Winner-label disagreement PA vs P0.
2. Winner-label disagreement PB vs P0.
3. Winner-label disagreement PAB vs P0.
4. `WRAPPER_ATTRACTION_PATTERN`: both unilateral conditions are decisive, PA chooses A and PB chooses B.
5. `WRAPPER_AVERSION_PATTERN`: both unilateral conditions are decisive, PA chooses B and PB chooses A.

A TIE is a winner label.

## Item classification

- `COMMON_WRAPPER_OR_REPEAT_UNSTABLE`: PAB != P0.
- `WRAPPER_ATTRACTION_PATTERN`: PA=A and PB=B, both decisive.
- `WRAPPER_AVERSION_PATTERN`: PA=B and PB=A, both decisive.
- `CONTENT_STABLE`: P0 == PA == PB.
- `MIXED_OR_TIE`: all remaining cases.

The attraction/aversion labels are descriptive patterns, not psychological claims about the judge.

## Secondary endpoints

- A/B/TIE counts by condition.
- Mean and median confidence by condition.
- Model wins after unblinding.
- Exact prompt IDs changing under unilateral wrapping.
- Whether aggregate model ranking changes across P0/PA/PB/PAB.

## Reporting limits

This tests one exact wrapper format on one reused 20-prompt candidate sample. It does not establish a general presentation-bias rate. The wrapper is content-preserving, but added boundary tokens may alter judge processing; that sensitivity is the object of measurement.
