---
type: method
status: evergreen
aliases:
  - Post-Training Quantization (PTQ)
  - Quantization after Training
  - PTQ
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
      - Post-training quantization (PTQ) means quantizing a model after it’s been fully trained. PTQ is by far the most common.
      - Major ML frameworks, including PyTorch, TensorFlow, and HuggingFace’s transformers, offer PTQ for free with a few lines of code.
created: 2026-05-26T21:55:46.240037+00:00
updated: 2026-05-26T21:55:46.240037+00:00
ingestion_run: 8d527d59
---

# Post-Training Quantization (PTQ)

## Summary

The process of converting a fully trained model's weights and activations to a lower-precision format (e.g., INT8) without retraining the model. This is the most common and easiest method for application developers.

## Core Idea

PTQ is highly effective for reducing memory footprint and speeding up inference, making it ideal for rapid deployment. The primary risk is potential accuracy degradation due to the sudden change in numerical representation.

## Practical Use

Use PTQ when the model's performance is acceptable after quantization, or when time/resources prohibit full retraining. It is the standard first step for optimizing models for edge devices or low-memory cloud environments.

## Related

- [[Quantization-Aware-Training-QAT|Quantization-Aware Training (QAT)]]
- [[Mixed-Precision-Inference|Mixed Precision Inference]]
