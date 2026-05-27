---
type: glossary
status: evergreen
aliases:
  - Inference vs. Training Lifecycle
  - AI model lifecycle phases
  - forward pass vs backward pass
tags:
  - ai-engineering
  - llm-ops
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/157-understanding-inference-optimization.md
    locator: pages 430-430
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Training refers to the process of building a model.
      - Inference refers to the process of using a model to compute an output for a given input.
created: 2026-05-26T21:55:46.429197+00:00
updated: 2026-05-26T21:55:46.429197+00:00
ingestion_run: 8d527d59
---

# Inference vs. Training Lifecycle

## Summary

Training is the process of building a model (forward and backward passes). Inference is the process of using a trained model to compute an output for a given input (forward pass only).

## Core Idea

Understanding this distinction is crucial because, in production environments, most AI engineers only need to manage and optimize the inference phase, not the training phase.

## Practical Use

When diagnosing latency or cost issues in a deployed model, focus optimization efforts exclusively on the inference pipeline, ignoring training-related overheads.

## Related

- [[Inference-Service-Architecture|Inference Service Architecture]]
- [[Model-Optimization-Trade-offs|Model Optimization Trade-offs]]
