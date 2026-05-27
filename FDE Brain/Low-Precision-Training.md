---
type: method
status: evergreen
aliases:
  - Low-Precision Training
  - Training in Reduced Precision
  - Mixed Precision Training
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
      - Training a model directly in lower precision can help with both goals [reducing memory footprint and speeding up computation].
      - Character.AI (2024) shared that they were able to train their models entirely in INT8, which helped eliminate the training/serving precision mismatch...
created: 2026-05-26T21:55:46.244492+00:00
updated: 2026-05-26T21:55:46.244492+00:00
ingestion_run: 8d527d59
---

# Low-Precision Training

## Summary

Training the entire model, or significant parts of it, using a reduced-precision format (e.g., INT8) throughout the backpropagation process. This is the most complex but potentially most efficient method.

## Core Idea

Training directly in low precision eliminates the training/serving precision mismatch and can significantly improve training efficiency and reduce costs. However, it is computationally challenging due to the sensitivity of backpropagation to low-precision rounding errors.

## Practical Use

Use this method when the primary goal is to achieve maximum training efficiency and eliminate precision mismatch, and when the development team has specialized expertise in low-precision gradient calculation and optimization.

## Related

- [[Quantization-Aware-Training-QAT|Quantization-Aware Training (QAT)]]
- [[Mixed-Precision-Inference|Mixed Precision Inference]]
