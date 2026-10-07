# Frozen pairwise judge rubric

PAIRWISE JUDGE RUBRIC

Evaluate Response A and Response B only against the user's prompt.

Consider:

1. Factual correctness
2. Reasoning/calculation correctness
3. Instruction following
4. Completeness
5. Relevance
6. Clarity and concision

Do not prefer a response because it is longer, more elaborate, or appears stylistically sophisticated.

If both responses are substantively equivalent in quality, return TIE.

Return exactly:

```text
WINNER: A | B | TIE
CONFIDENCE: <0.00-1.00>
REASON: <one concise sentence>
```

Do not infer or identify which model produced either response.

Do not use information from other evaluation items.

Judge each pair independently.

SHA-256: `2cc0004b684007187d4bb5d24a6f6843053a3389d434d6d775e74e8a40a4e198`
