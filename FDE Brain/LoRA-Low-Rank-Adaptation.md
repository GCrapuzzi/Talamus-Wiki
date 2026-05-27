---
type: pattern
status: evergreen
aliases:
  - LoRA (Low-Rank Adaptation)
  - Low-Rank Finetuning
tags:
  - ai-engineering
  - finetuning
  - optimization
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/138-summary.md
    locator: pages 385-386
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - After giving an overview of PEFT, the chapter zoomed into LoRA—why and how it works.
      - On top of being parameter-efficient and data-efficient, it’s also modular, making it much easier to serve and combine multiple LoRA models.
created: 2026-05-26T21:55:46.285033+00:00
updated: 2026-05-26T21:55:46.285033+00:00
ingestion_run: 8d527d59
---

# LoRA (Low-Rank Adaptation)

## Summary

A specific PEFT technique that injects trainable low-rank matrices into the model's layers, allowing for efficient adaptation while preserving the model's core knowledge.

## Core Idea

LoRA provides a highly modular, parameter-efficient, and data-efficient method for customizing large models without the computational cost of updating the entire weight matrix.

## Practical Use

Use LoRA to create task-specific adapters for a foundation model. Its modularity is key, as multiple adapters can be easily combined or swapped for different use cases (e.g., combining a summarization adapter with a Q&A adapter).

## Related

- PEFT
- [[Model-Merging|Model Merging]]
