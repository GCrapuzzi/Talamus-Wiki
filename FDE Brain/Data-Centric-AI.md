---
type: framework
status: evergreen
aliases:
  - Data-Centric AI
  - data-centric approach
  - data-first AI
tags:
  - ai-engineering
  - data-strategy
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/139-chapter-8.-dataset-engineering.md
    locator: pages 387-388
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - The goal of dataset engineering is to create a dataset that allows you to train the best model.
      - Data-centric AI tries to improve AI performance by enhancing the data.
      - In recent years, more benchmarks have become data-centric.
created: 2026-05-26T21:55:46.290321+00:00
updated: 2026-05-26T21:55:46.290321+00:00
ingestion_run: 8d527d59
---

# Data-Centric AI

## Summary

An AI development paradigm that prioritizes improving model performance by enhancing the quality, structure, and quantity of the training data, rather than solely focusing on improving model architecture or size.

## Core Idea

The quality of the model is fundamentally limited by the quality of the data. By focusing on data improvements (e.g., fixing labels, adding edge cases, augmenting data), performance gains can be achieved with fewer computational resources.

## Practical Use

When faced with budget constraints, an AI engineer should first evaluate if performance bottlenecks are due to model limitations (requiring more compute/architecture changes) or data limitations (requiring more data labeling, cleaning, or augmentation). This guides resource allocation.

## Related

- [[Model-Centric-AI|Model-Centric AI]]
- [[Dataset-Engineering-Lifecycle|Dataset Engineering Lifecycle]]
