---
type: glossary
tags: [statistics, evaluation, pitfalls]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#step-3-define-evaluation-methods-and-data
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Simpson's Paradox

A statistical phenomenon where Model A outperforms Model B on every data subset but underperforms on the aggregated data. Arises from uneven group sizes across compared conditions.

Example in model evaluation:

| | Group 1 | Group 2 | Overall |
|---|---|---|---|
| Model A | 93% (81/87) | 73% (192/263) | 78% |
| Model B | 87% (234/270) | 69% (55/80) | 83% |

Model A wins on both subgroups but loses overall because it has disproportionately more examples in the harder group.

Mitigation: **slice-based evaluation** — always examine performance on meaningful subsets (user segments, input types, difficulty tiers) rather than relying solely on aggregate scores.
