---
type: framework
status: evergreen
aliases:
  - Finetuning Development Paths
  - Progression Path
  - Distillation Path
tags:
  - ai-engineering
  - finetuning
  - workflow
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/137-finetuning-tactics.md
    locator: pages 381-384
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - The Progression path involves testing with cheapest/fastest model, then middling model, then best model.
      - The Distillation path involves starting with a small dataset and the strongest model, using it to generate more training data, and then training a cheaper model on that new dataset.
created: 2026-05-26T21:55:46.269478+00:00
updated: 2026-05-26T21:55:46.269478+00:00
ingestion_run: 8d527d59
---

# Finetuning Development Paths

## Summary

Structured approaches for finetuning a model, depending on whether the goal is incremental performance improvement or knowledge transfer from a strong model.

## Core Idea

The choice of development path dictates the sequence of experiments, optimizing resource use and maximizing performance gains. The Progression Path is linear testing, while the Distillation Path leverages a strong model to generate data for a cheaper model.

## Practical Use

When starting a new finetuning project, use the Progression Path (cheap model -> mid model -> best model) to validate code and data before committing to the most expensive model. If data is scarce, use the Distillation Path (strong model -> generate data -> train cheaper model).

## Related

- Model Selection Criteria
- LoRA
