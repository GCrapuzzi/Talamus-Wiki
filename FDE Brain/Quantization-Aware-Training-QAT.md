---
type: method
status: evergreen
aliases:
  - Quantization-Aware Training (QAT)
  - Quantization during Training
  - QAT
tags:
  - ai-engineering
  - training
  - optimization
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/133-quantization.md
    locator: pages 352-355
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - QAT aims to create a model with high quality in low precision for inference.
      - With QAT, the model simulates low-precision (e.g., 8-bit) behavior during training, which allows the model to learn to produce high-quality outputs in low precision.
created: 2026-05-26T21:55:46.241760+00:00
updated: 2026-05-26T21:55:46.241760+00:00
ingestion_run: 8d527d59
---

# Quantization-Aware Training (QAT)

## Summary

A training technique where the model simulates low-precision behavior (e.g., 8-bit) during the training process. This allows the model to learn to maintain high quality even when running in low precision.

## Core Idea

QAT addresses the accuracy degradation often seen with PTQ by making the model robust to the quantization noise. However, it does not inherently reduce training time, as the computations are still performed in high precision.

## Practical Use

Use QAT when PTQ results in unacceptable performance degradation, but the goal is still to achieve high-quality low-precision inference. This method requires more complex training pipelines and increased computational effort.

## Related

- [[Post-Training-Quantization-PTQ|Post-Training Quantization (PTQ)]]
- [[Mixed-Precision-Inference|Mixed Precision Inference]]
