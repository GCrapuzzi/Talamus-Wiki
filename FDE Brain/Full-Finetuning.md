---
type: method
status: evergreen
aliases:
  - Full Finetuning
  - Complete Finetuning
tags:
  - ai-engineering
  - finetuning
  - resource-intensive
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/135-parameter-efficient-finetuning.md
    locator: pages 356-370
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - In full finetuning, the number of trainable parameters is exactly the same as the number of parameters.
      - The total memory needed for the model’s weights, gradients, and optimizer states is then 14 GB + 42 GB = 56 GB (for a 7B model in FP16).
      - Full finetuning typically requires a lot of high-quality annotated data.
created: 2026-05-26T21:55:46.253957+00:00
updated: 2026-05-26T21:55:46.253957+00:00
ingestion_run: 8d527d59
---

# Full Finetuning

## Summary

The process of updating every single parameter in a pre-trained model using task-specific data. All parameters are trainable.

## Core Idea

Full finetuning ensures maximum potential performance by allowing every weight to adapt to the new task. However, it is extremely memory-intensive because the memory required scales linearly with the total number of parameters, gradients, and optimizer states (e.g., 7B model requires ~56 GB for weights, gradients, and optimizer states in FP16).

## Practical Use

Use full finetuning only when hardware resources are abundant (e.g., large cloud clusters with high VRAM) and when the absolute highest performance ceiling is required, and when the dataset is large and high-quality.

## Related

- [[Parameter-Efficient-Finetuning-PEFT|Parameter-Efficient Finetuning (PEFT)]]
- Memory Math
