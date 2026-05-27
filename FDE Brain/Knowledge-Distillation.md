---
type: method
status: evergreen
aliases:
  - Knowledge Distillation
  - Student-Teacher Learning
  - Model Mimicry
tags:
  - ai-engineering
  - model-compression
  - transfer-learning
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/162-model-optimization.md
    locator: pages 450-463
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Model distillation, training a small model to mimic the behavior of the large model.
      - Model distillation suggests that it’s possible to capture a large model’s behaviors using fewer parameters.
created: 2026-05-26T21:55:46.475941+00:00
updated: 2026-05-26T21:55:46.475941+00:00
ingestion_run: 8d527d59
---

# Knowledge Distillation

## Summary

Training a smaller, more efficient 'student' model to replicate the behavior and output distribution of a large, high-performing 'teacher' model. This captures the knowledge of the large model using fewer parameters.

## Core Idea

It is possible to capture the complex behavior of a massive model using a significantly smaller model. This allows deployment of high-quality AI functionality on resource-constrained hardware.

## Practical Use

When a state-of-the-art model is too large for deployment, use distillation. Train a smaller model (the student) using the outputs or intermediate representations of the large model (the teacher) as soft targets, rather than just the ground truth labels.

## Related

- [[Model-Compression-Techniques|Model Compression Techniques]]
