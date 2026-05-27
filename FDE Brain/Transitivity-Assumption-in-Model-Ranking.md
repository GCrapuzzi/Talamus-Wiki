---
type: concept
status: evergreen
aliases:
  - Transitivity Assumption in Model Ranking
  - Transitive Ranking
  - A > B and B > C implies A > C
tags:
  - ai-engineering
  - statistics
  - evaluation
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/073-challenges-of-comparative-evaluation.md
    locator: pages 176-178
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Ranking algorithms typically assume transitivity.
      - Human preference is not necessarily transitive.
      - Non-transitivity can happen because different model pairs are evaluated by different evaluators and on different prompts.
created: 2026-05-26T21:55:45.766138+00:00
updated: 2026-05-26T21:55:45.766138+00:00
ingestion_run: 8d527d59
---

# Transitivity Assumption in Model Ranking

## Summary

The assumption that if Model A ranks higher than Model B, and Model B ranks higher than Model C, then Model A must also rank higher than Model C. This assumption allows ranking algorithms to infer relationships without direct comparison.

## Core Idea

Transitivity simplifies the computational load of comparative evaluation by reducing the need for every possible pairwise comparison. However, human preference and AI model performance are not guaranteed to be transitive, especially when comparisons are conducted by different evaluators or on different prompts.

## Practical Use

When designing a ranking system, acknowledge the risk of non-transitivity. If the system relies heavily on inferred rankings, consider incorporating mechanisms to flag or weight comparisons that violate the transitivity assumption, especially if the evaluation source is known to be variable (e.g., crowdsourced).

## Related

- [[Comparative-Evaluation-Framework|Comparative Evaluation Framework]]
- Non-Transitivity Bias
