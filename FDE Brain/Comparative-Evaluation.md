---
type: pattern
status: evergreen
aliases:
  - Comparative Evaluation
  - Pairwise Comparison
  - A vs B Evaluation
tags:
  - ai-engineering
  - evaluation
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/075-summary.md
    locator: pages 180-182
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - "When evaluating models, you can... rank them using comparative signals: which of the two models is better?"
      - Comparative evaluation is common in sports, especially chess, and is gaining traction in AI evaluation.
created: 2026-05-26T21:55:45.775570+00:00
updated: 2026-05-26T21:55:45.775570+00:00
ingestion_run: 8d527d59
---

# Comparative Evaluation

## Summary

Evaluating two models against each other to determine which is superior, rather than scoring each model independently.

## Core Idea

When models are powerful and open-ended, determining relative performance (which is better) can provide more discriminating signals than absolute scoring, especially for preference-driven tasks.

## Practical Use

When building an evaluation pipeline for open-ended applications, implement pairwise comparison tests (e.g., 'Which response is better?') to gather preference signals, which are crucial for training preference models.

## Related

- [[Preference-Models|Preference Models]]
- [[Hybrid-Evaluation-Pipeline|Hybrid Evaluation Pipeline]]
