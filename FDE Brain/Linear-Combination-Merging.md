---
type: method
status: evergreen
aliases:
  - Linear Combination Merging
  - Weighted Averaging
  - Parameter Averaging
tags:
  - ai-engineering
  - mathematics
  - finetuning
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/136-model-merging-and-multi-task-finetuning.md
    locator: pages 371-380
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - "Given two models, A and B, their weighted average is: Merge(A, B) = (W_A A + W_B B) / (W_A + W_B)"
      - Linear combination is the most effective for models finetuned on top of the same base model.
created: 2026-05-26T21:55:46.266525+00:00
updated: 2026-05-26T21:55:46.266525+00:00
ingestion_run: 8d527d59
---

# Linear Combination Merging

## Summary

A mathematical technique for merging models by calculating a weighted average of the weight values (parameters) of the constituent models.

## Core Idea

This method assumes that the combined performance is linearly related to the combination of the component weights. It is highly effective when models are finetuned on the same base model.

## Practical Use

When merging two models, A and B, the merged weight set W can be calculated as: Merge(A, B) = (W_A * A + W_B * B) / (W_A + W_B). This is particularly useful for combining adapter weights (LoRA) or entire model weights.

## Related

- Task Vectors
- [[Model-Merging|Model Merging]]
