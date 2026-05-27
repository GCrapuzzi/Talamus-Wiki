---
type: method
status: evergreen
aliases:
  - Mixed Precision Training
  - Mixed Preci-sion Training
tags:
  - ai-engineering
  - optimization
  - hardware-acceleration
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/135-parameter-efficient-finetuning.md
    locator: pages 356-370
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - You can also have less-sensitive weight values computed in lower precision and more-sensitive weight values computed in higher precision.
      - The portions of the model that should be in lower precision can be set automatically using the automatic mixed precision (AMP) functionality.
created: 2026-05-26T21:55:46.256900+00:00
updated: 2026-05-26T21:55:46.256900+00:00
ingestion_run: 8d527d59
---

# Mixed Precision Training

## Summary

Training or running inference by using a combination of different numerical precision formats (e.g., 16-bit floating point (FP16) for weights and 32-bit (FP32) for sensitive calculations).

## Core Idea

Mixed precision reduces memory consumption and increases computational speed by allowing most weights and activations to be stored and processed in lower precision (like FP16 or even 4-bit quantization) while maintaining high accuracy by keeping critical components (like embeddings) in higher precision.

## Practical Use

Implement this technique using framework features like Automatic Mixed Precision (AMP) to fit larger models onto consumer GPUs or accelerate training cycles without significant loss of model accuracy.

## Related

- [[Quantization|Quantization]]
- [[Parameter-Efficient-Finetuning-PEFT|Parameter-Efficient Finetuning (PEFT)]]
