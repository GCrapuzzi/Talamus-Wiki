---
type: pattern
status: evergreen
aliases:
  - Data Dependency Principle
  - Data-Model Correlation
  - Garbage In, Garbage Out (AI)
tags:
  - data-engineering
  - ai-engineering
  - data-governance
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/039-training-data.md
    locator: pages 74-74
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - An AI model is only as good as the data it was trained on.
      - If there’s no Vietnamese in the training data, the model won’t be able to translate from English into Vietnamese.
created: 2026-05-26T21:55:45.504220+00:00
updated: 2026-05-26T21:55:45.504220+00:00
ingestion_run: 8d527d59
---

# Data Dependency Principle

## Summary

A model's performance, capabilities, and limitations are fundamentally constrained by the diversity, volume, and quality of its training data.

## Core Idea

The model is a mirror of its training data. If the data lacks representation for a specific task (e.g., Vietnamese translation), the model cannot perform that task, regardless of its underlying architecture.

## Practical Use

When designing a new AI feature, perform a data gap analysis to identify necessary data types or domains that are currently underrepresented in the training corpus. Prioritize targeted data collection for weak points.

## Related

- Model Alignment
- Data Quality Assessment
