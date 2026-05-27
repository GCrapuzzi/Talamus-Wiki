---
type: framework
status: evergreen
aliases:
  - Quantization Strategy Selection
  - Precision Reduction Workflow
  - Model Optimization Decision Tree
tags:
  - ai-engineering
  - optimization
  - deployment
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/133-quantization.md
    locator: pages 352-355
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - PTQ is by far the most common [method].
      - QAT aims to create a model with high quality in low precision for inference.
      - Training a model directly in lower precision... helps eliminate the training/serving precision mismatch.
created: 2026-05-26T21:55:46.238751+00:00
updated: 2026-05-26T21:55:46.238751+00:00
ingestion_run: 8d527d59
---

# Quantization Strategy Selection

## Summary

A decision framework for choosing the appropriate quantization technique (PTQ, QAT, or full low-precision training) based on deployment constraints, performance requirements, and available training resources.

## Core Idea

The choice of quantization method dictates the trade-off between model quality (accuracy loss), development effort, and deployment efficiency. The goal is to achieve the lowest possible bit depth without unacceptable performance degradation.

## Practical Use

1. **Initial Deployment/Quick Iteration:** Use PTQ (Post-Training Quantization) for rapid deployment on standard hardware. 2. **High Accuracy Requirement:** Use QAT (Quantization-Aware Training) if PTQ causes unacceptable accuracy loss. 3. **Maximum Efficiency/Novel Hardware:** Consider full low-precision training if the hardware supports it and the team has the resources to manage the complexity.

## Related

- [[Post-Training-Quantization-PTQ|Post-Training Quantization (PTQ)]]
- [[Quantization-Aware-Training-QAT|Quantization-Aware Training (QAT)]]
- [[Mixed-Precision-Inference|Mixed Precision Inference]]
