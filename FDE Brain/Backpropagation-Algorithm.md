---
type: operation
status: evergreen
aliases:
  - Backpropagation Algorithm
  - backprop
tags:
  - ai-engineering
  - training
  - optimization
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/130-backpropagation-and-trainable-parameters.md
    locator: pages 344-345
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - "With backpropagation, each training step consists of two phases: 1. Forward pass... 2. Backward pass..."
      - Compute how much each trainable parameter contributes to the mistake. This value is called the gradient.
      - Adjust trainable parameter values using their corresponding gradient.
created: 2026-05-26T21:55:46.217524+00:00
updated: 2026-05-26T21:55:46.217524+00:00
ingestion_run: 8d527d59
---

# Backpropagation Algorithm

## Summary

The core algorithm used to train neural networks, calculating the gradient of the loss function with respect to every trainable parameter.

## Core Idea

Backpropagation is an iterative process that determines how much each trainable parameter contributed to the overall error (loss), allowing the model to adjust its weights in the direction that minimizes future errors.

## Practical Use

Understand the backpropagation cycle (Forward Pass -> Loss Calculation -> Backward Pass -> Optimization) to debug training instability or to implement custom optimization steps.

## Related

- Gradient Descent
- [[Trainable-vs.-Frozen-Parameters|Trainable vs. Frozen Parameters]]
