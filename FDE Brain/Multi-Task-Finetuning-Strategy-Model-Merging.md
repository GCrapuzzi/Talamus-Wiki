---
type: method
status: evergreen
aliases:
  - "Multi-Task Finetuning Strategy: Model Merging"
  - Parallel Task Learning
  - Task Combination via Merging
tags:
  - ai-engineering
  - finetuning
  - multi-task-learning
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/136-model-merging-and-multi-task-finetuning.md
    locator: pages 371-380
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Model merging offers another method for multi-task finetuning.
      - Because there’s no sequential learning, there’s less risk of catastrophic forgetting.
      - This approach is appealing for on-device deployment due to memory constraints.
created: 2026-05-26T21:55:46.262118+00:00
updated: 2026-05-26T21:55:46.262118+00:00
ingestion_run: 8d527d59
---

# Multi-Task Finetuning Strategy: Model Merging

## Summary

A strategy for training a model on multiple tasks by finetuning the model for each task separately and then merging the resulting specialized models into a single, unified model.

## Core Idea

Model merging is superior to sequential finetuning because it avoids catastrophic forgetting (where learning a new task causes the model to forget an old one). It allows the model to learn each task optimally without interference.

## Practical Use

Instead of training a model sequentially (Task A -> Task B -> Task C), train Model A, Model B, and Model C independently. Then, use model merging techniques (e.g., linear combination) to combine them into a single model capable of all three tasks.

## Related

- [[Model-Merging|Model Merging]]
- Simultaneous Finetuning
- Sequential Finetuning
