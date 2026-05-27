---
type: concept
status: evergreen
aliases:
  - Trainable vs. Frozen Parameters
  - trainable parameters
  - frozen parameters
tags:
  - ai-engineering
  - finetuning
  - memory-optimization
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/130-backpropagation-and-trainable-parameters.md
    locator: pages 344-345
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - A trainable parameter is a parameter that can be updated during finetuning.
      - The parameters that are kept unchanged are frozen parameters.
      - If a parameter is not trainable, it doesn’t need to be updated and, therefore, there’s no need to compute its gradient.
created: 2026-05-26T21:55:46.210738+00:00
updated: 2026-05-26T21:55:46.210738+00:00
ingestion_run: 8d527d59
---

# Trainable vs. Frozen Parameters

## Summary

A classification of model parameters: trainable parameters are those updated during fine-tuning, while frozen parameters are kept unchanged.

## Core Idea

During fine-tuning, only trainable parameters are updated, significantly reducing the computational load and memory footprint compared to updating all parameters (as done during pre-training).

## Practical Use

When fine-tuning large foundation models, identify which layers or parameter groups can be frozen (e.g., the core transformer layers) to drastically reduce the number of parameters requiring gradient computation and memory storage.

## Related

- [[Parameter-Efficient-Fine-Tuning-PEFT|Parameter-Efficient Fine-Tuning (PEFT)]]
