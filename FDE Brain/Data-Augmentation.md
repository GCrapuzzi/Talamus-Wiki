---
type: method
status: evergreen
aliases:
  - Data Augmentation
  - Data Augmentation Techniques
tags:
  - ai-engineering
  - data-pipeline
  - data-augmentation
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/145-data-augmentation-and-synthesis.md
    locator: pages 404-404
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Data augmentation creates new data from existing data (which is real). For example, given a real image of a cat, you can flip it to create a new image of the same cat.
created: 2026-05-26T21:55:46.354662+00:00
updated: 2026-05-26T21:55:46.354662+00:00
ingestion_run: 8d527d59
---

# Data Augmentation

## Summary

Creating new training data by applying transformations (e.g., flipping, rotating) to existing, real data samples.

## Core Idea

It leverages the inherent structure of real data by generating variations that maintain the original data's properties, thereby increasing dataset size and improving model robustness without requiring new real-world collection.

## Practical Use

When a dataset is limited in variety (e.g., only frontal images of an object), apply geometric or photometric transformations (like rotation, cropping, or color jittering) to simulate diverse real-world conditions for training.

## Related

- [[Data-Synthesis|Data Synthesis]]
- Dataset Engineering
