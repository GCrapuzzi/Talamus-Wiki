---
type: pattern
status: evergreen
aliases:
  - Model Overfitting Detection
  - Validation Loss Monitoring
tags:
  - ai-engineering
  - evaluation
  - finetuning
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/137-finetuning-tactics.md
    locator: pages 381-384
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - If the training loss still decreases but the validation loss increases, the model is overfitting to the training data.
created: 2026-05-26T21:55:46.279068+00:00
updated: 2026-05-26T21:55:46.279068+00:00
ingestion_run: 8d527d59
---

# Model Overfitting Detection

## Summary

A diagnostic pattern used during finetuning where the relationship between training loss and validation loss is monitored to detect when the model is memorizing the training data rather than generalizing.

## Core Idea

If the training loss continues to decrease while the validation loss begins to increase, the model is overfitting. This signals that the model is learning noise specific to the training set.

## Practical Use

When monitoring training runs, if validation loss increases, stop training and consider reducing the number of epochs or increasing the dataset size.

## Related

- Number of Epochs
- Regularization Techniques
