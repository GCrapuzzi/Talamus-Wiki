---
type: method
status: evergreen
aliases:
  - Comparative Evaluation (Pairwise Comparison)
  - Match-based Ranking
  - A/B Comparison (for LLMs)
tags:
  - evaluation
  - ai-engineering
  - llm-evaluation
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/072-ranking-models-with-comparative-evaluation.md
    locator: pages 172-175
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - With comparative evaluation, you evaluate models against each other and compute a ranking from comparison results.
      - For each request, two or more models are selected to respond. An evaluator, which can be human or AI, picks the winner.
      - The probability that model A is preferred over model B is the win rate of A over B.
created: 2026-05-26T21:55:45.754451+00:00
updated: 2026-05-26T21:55:45.754451+00:00
ingestion_run: 8d527d59
---

# Comparative Evaluation (Pairwise Comparison)

## Summary

An evaluation method where models are tested in pairs (matches), and an evaluator (human or AI) determines a winner. The overall ranking is derived from the win rates across all pairwise comparisons.

## Core Idea

Instead of assigning absolute scores, models are ranked based on relative performance. This method is highly effective for subjective quality assessment because it simplifies the decision process for the evaluator (choosing a winner) compared to assigning a numerical score.

## Practical Use

Implement a system where users or a dedicated LLM judge are presented with two model outputs side-by-side and asked to select the preferred output. This generates structured data (Match #, Model A, Model B, Winner) used for ranking.

## Related

- Rating Algorithms
- [[Pointwise-vs.-Comparative-Evaluation|Pointwise vs. Comparative Evaluation]]
