---
type: method
status: evergreen
aliases:
  - Preference Models
  - Pairwise Preference Learning
tags:
  - ai-engineering
  - alignment
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/075-summary.md
    locator: pages 180-182
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - "Both comparative evaluation and the post-training alignment process need preference signals... This motivated the development of preference models: specialized AI judges that predict which response users prefer."
created: 2026-05-26T21:55:45.777148+00:00
updated: 2026-05-26T21:55:45.777148+00:00
ingestion_run: 8d527d59
---

# Preference Models

## Summary

Specialized AI judges trained to predict which of two given responses a user would prefer, converting comparative signals into usable training data.

## Core Idea

Since preference signals are expensive to collect, preference models automate the process of gathering these comparative signals, which is essential for post-training alignment and fine-tuning.

## Practical Use

Use preference models to generate synthetic preference data (e.g., comparing model outputs on a dataset) to fine-tune a model's alignment or to train a reward model for RLHF.

## Related

- [[Comparative-Evaluation|Comparative Evaluation]]
- RLHF
