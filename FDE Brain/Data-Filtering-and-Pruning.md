---
type: pattern
status: evergreen
aliases:
  - Data Filtering and Pruning
  - Data Selection
  - Active Learning for Data
tags:
  - ai-engineering
  - optimization
  - data-pruning
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/153-clean-and-filter-data.md
    locator: pages 425-425
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Active learning techniques can select examples that are the most helpful for the model to learn from.
      - Importance sampling can find examples that are most important to your task.
created: 2026-05-26T21:55:46.412072+00:00
updated: 2026-05-26T21:55:46.412072+00:00
ingestion_run: 8d527d59
---

# Data Filtering and Pruning

## Summary

Advanced techniques used to select the most informative or valuable subset of data when the full dataset is too large or expensive to use.

## Core Idea

Not all data points contribute equally to model learning. Pruning focuses resources by identifying examples that maximize learning efficiency, significantly reducing resource costs.

## Practical Use

Use Active Learning to select examples where the model is most uncertain. Employ Importance Sampling to prioritize examples that are critical to the specific task objective. Requires developing robust metrics to evaluate example importance.

## Related

- Active Learning
- Importance Sampling
- Data Verification
