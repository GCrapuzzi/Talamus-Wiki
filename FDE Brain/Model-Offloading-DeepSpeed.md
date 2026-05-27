---
type: operation
status: evergreen
aliases:
  - Model Offloading (DeepSpeed)
  - CPU Offloading
tags:
  - ai-engineering
  - optimization
  - hardware-management
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/135-parameter-efficient-finetuning.md
    locator: pages 356-370
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Instead of trying to fit the whole model on GPUs, you can offload the excess memory onto CPUs, as demonstrated by DeepSpeed.
created: 2026-05-26T21:55:46.259211+00:00
updated: 2026-05-26T21:55:46.259211+00:00
ingestion_run: 8d527d59
---

# Model Offloading (DeepSpeed)

## Summary

A memory management technique that moves excess model parameters, gradients, or optimizer states from the high-speed GPU VRAM to the slower, but larger, system RAM (CPU memory).

## Core Idea

This technique allows engineers to train or run models that are too large to fit entirely within the GPU's limited memory capacity. It trades computational speed for increased memory capacity.

## Practical Use

When attempting to fit a massive model (e.g., >40GB) on a GPU with limited VRAM (e.g., 12GB), implement offloading strategies (like those provided by DeepSpeed) to make the model runnable, accepting a potential slowdown in inference/training speed.

## Related

- [[Parameter-Efficient-Finetuning-PEFT|Parameter-Efficient Finetuning (PEFT)]]
- [[Full-Finetuning|Full Finetuning]]
