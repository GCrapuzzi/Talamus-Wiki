---
type: pattern
status: evergreen
aliases:
  - Data Filtering and Pruning Strategies
  - Data Quality Improvement
  - Active Learning for Data Selection
tags:
  - data-engineering
  - llm-ops
  - data-pruning
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/154-format-data.md
    locator: pages 425-426
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - use active learning techniques to select examples that are the most helpful for your model to learn from.
      - use importance sampling to find examples that are most important to your task.
      - Manual inspection of data is especially important in this step.
created: 2026-05-26T21:55:46.417012+00:00
updated: 2026-05-26T21:55:46.417012+00:00
ingestion_run: 8d527d59
---

# Data Filtering and Pruning Strategies

## Summary

Techniques used to reduce the dataset size while maximizing the model's learning efficiency by identifying and retaining the most informative examples.

## Core Idea

Training on excessive or low-quality data wastes compute resources and slows convergence. Pruning focuses resources on the most impactful examples.

## Practical Use

1. **Active Learning:** Select examples where the model is most uncertain (high entropy). 2. **Importance Sampling:** Prioritize examples that are critical to the task's success. 3. **Heuristics:** Manually inspect data to detect non-obvious patterns of low quality (e.g., data from the end of an annotation session).

## Related

- Active Learning
- Importance Sampling
