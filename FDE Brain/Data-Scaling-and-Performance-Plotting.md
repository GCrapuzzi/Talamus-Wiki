---
type: method
status: evergreen
aliases:
  - Data Scaling and Performance Plotting
  - Performance Scaling Curve
  - Data Subset Experimentation
tags:
  - ai-engineering
  - data-curation
  - experimentation
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/143-data-quantity.md
    locator: pages 396-400
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Experimenting with a small dataset can help you estimate how much more data you’ll need. You can finetune a model on subsets of your current dataset—e.g., 25%, 50%, 100%—and plot how performance scales with dataset size.
created: 2026-05-26T21:55:46.341299+00:00
updated: 2026-05-26T21:55:46.341299+00:00
ingestion_run: 8d527d59
---

# Data Scaling and Performance Plotting

## Summary

An empirical method used to estimate the required data volume by finetuning a model on systematically increasing subsets of the available dataset (e.g., 25%, 50%, 100%).

## Core Idea

Analyzing the resulting performance curve (slope) helps predict future performance gains. A steep slope indicates significant gains are expected by increasing data; a plateau indicates diminishing returns.

## Practical Use

Before committing resources to massive data curation, run this experiment. If the performance curve plateaus quickly, focus efforts on improving data quality or hyperparameters rather than simply collecting more data.

## Related

- Data Quality and Diversity
- [[Data-Scaling-and-Finetuning-Strategy|Data Scaling and Finetuning Strategy]]
