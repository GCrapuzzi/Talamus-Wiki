---
type: method
status: evergreen
aliases:
  - Rating Algorithms for Pairwise Data
  - Elo Rating System
  - Bradley-Terry Model
  - TrueSkill
tags:
  - evaluation
  - statistics
  - ai-engineering
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/072-ranking-models-with-comparative-evaluation.md
    locator: pages 172-175
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Given comparative signals, a rating algorithm is then used to compute a ranking of models.
      - Many rating algorithms developed for these other domains can be adapted to evaluating AI models, such as Elo, Bradley–Terry, and TrueSkill.
created: 2026-05-26T21:55:45.759847+00:00
updated: 2026-05-26T21:55:45.759847+00:00
ingestion_run: 8d527d59
---

# Rating Algorithms for Pairwise Data

## Summary

Mathematical algorithms used to convert a series of pairwise comparison results (win rates) into a single, comparable ranking score for each model. These algorithms model the probability of one model beating another.

## Core Idea

These algorithms treat model ranking as a predictive problem: they use historical match outcomes to estimate the underlying skill level of each model, allowing prediction of future match outcomes. The choice of algorithm depends on the desired mathematical properties (e.g., sensitivity to order).

## Practical Use

After collecting a dataset of pairwise comparisons (e.g., 100 matches between Model A and Model B), feed the win rates into a specialized ranking algorithm (like Bradley-Terry) to generate a robust, normalized score for Model A and Model B.

## Related

- [[Comparative-Evaluation-Pairwise-Comparison|Comparative Evaluation (Pairwise Comparison)]]
