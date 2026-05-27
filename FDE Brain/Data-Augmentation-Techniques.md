---
type: pattern
status: evergreen
aliases:
  - Data Augmentation Techniques
  - Data Transformation
  - Synthetic Data Generation from Existing Data
tags:
  - data-augmentation
  - machine-learning
  - robustness
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/147-traditional-data-synthesis-techniques.md
    locator: pages 407-409
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - For images, you can randomly rotate, crop, scale, or erase part of an image.
      - For texts, you can randomly replace a word with a similar word...
      - "Perturbation: adding noise to existing data to generate new data."
created: 2026-05-26T21:55:46.369920+00:00
updated: 2026-05-26T21:55:46.369920+00:00
ingestion_run: 8d527d59
---

# Data Augmentation Techniques

## Summary

Creating new training examples by applying controlled transformations to existing data samples, increasing dataset size and improving model robustness.

## Core Idea

Augmentation helps mitigate overfitting and improves model generalization by exposing the model to variations it might encounter in the real world. It is crucial for addressing data scarcity and inherent biases.

## Practical Use

Applying transformations like random cropping/rotation (images), synonym replacement (text), or adding noise (perturbation) to existing datasets to train more robust and generalizable AI models.

## Related

- Perturbation
- [[Bias-Mitigation-in-Data|Bias Mitigation in Data]]
- [[Simulation-Based-Data-Generation|Simulation-Based Data Generation]]
