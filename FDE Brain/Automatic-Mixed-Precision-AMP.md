---
type: concept
status: evergreen
aliases:
  - Automatic Mixed Precision (AMP)
  - Mixed Precision Functionality
tags:
  - ai-engineering
  - optimization
  - frameworks
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/134-finetuning-techniques.md
    locator: pages 356-356
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - The portions of the model that should be in lower precision can be set automatically using the automatic mixed precision (AMP) functionality offered by many ML frameworks.
created: 2026-05-26T21:55:46.250650+00:00
updated: 2026-05-26T21:55:46.250650+00:00
ingestion_run: 8d527d59
---

# Automatic Mixed Precision (AMP)

## Summary

A feature offered by ML frameworks that automatically manages the use of different numerical precision levels (e.g., FP16, BF16, FP32) during training, optimizing performance and memory usage without manual intervention.

## Core Idea

AMP simplifies the implementation of mixed precision. It allows engineers to benefit from the memory and speed gains of lower precision while the framework handles the necessary casting and gradient scaling to maintain numerical stability, especially during gradient calculations.

## Practical Use

When setting up a training pipeline, enable AMP functionality in the chosen ML framework (PyTorch/TensorFlow). This is the first step to optimizing resource usage when training large models.

## Related

- [[Mixed-Precision-Training|Mixed Precision Training]]
