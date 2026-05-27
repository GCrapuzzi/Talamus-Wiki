---
type: method
status: evergreen
aliases:
  - Feature-based Transfer
  - Embedding Transfer
  - Feature Extraction
tags:
  - ai-engineering
  - computer-vision
  - llm-architecture
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/124-finetuning-overview.md
    locator: pages 332-334
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Another approach is feature-based transfer. In this approach, a model is trained to extract features from the data, usually as embedding vectors, which are then used by another model.
created: 2026-05-26T21:55:46.171115+00:00
updated: 2026-05-26T21:55:46.171115+00:00
ingestion_run: 8d527d59
---

# Feature-based Transfer

## Summary

A transfer learning approach where a model is trained solely to extract rich, generalized features (usually embedding vectors) from data. These extracted features are then passed to a separate, smaller model (e.g., a classifier head) for the final task.

## Core Idea

This decouples the feature extraction process from the final task prediction. It is highly effective in domains like computer vision, where the feature extractor (e.g., ImageNet model) is robust and reusable.

## Practical Use

When the task is classification or detection, and the underlying data structure is complex (e.g., images, time series), use a pre-trained model to generate embeddings, and then train a simple, lightweight classifier on top of those embeddings rather than finetuning the entire large model.

## Related

- [[Foundation-Models|Foundation Models]]
- Classification
