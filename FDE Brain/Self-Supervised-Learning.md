---
type: method
status: evergreen
aliases:
  - Self-supervised Learning
  - Self-supervision
tags:
  - ai-engineering
  - ml-training
  - data-strategy
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/017-from-large-language-models-to-foundation-models.md
    locator: pages 32-35
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - In self-supervised learning, labels are inferred from the input data.
      - Self-supervised learning means that language models can learn from text sequences without requiring any labeling.
      - OpenAI used a variant of self-supervision called natural language supervision to train their language-image model CLIP...
created: 2026-05-26T21:55:45.345972+00:00
updated: 2026-05-26T21:55:45.345972+00:00
ingestion_run: 8d527d59
---

# Self-supervised Learning

## Summary

A machine learning paradigm where the model generates its own labels (pseudo-labels) from the input data, eliminating the need for expensive manual labeling. This is crucial for scaling large models.

## Core Idea

By inferring labels from the data itself (e.g., predicting missing words in a sentence, or pairing images with co-occurring text), models can be trained on massive, readily available datasets (like the entire internet), enabling unprecedented scale.

## Practical Use

When building a model with limited labeled data, utilize self-supervised techniques. For multimodal data, use techniques like finding co-occurring (image, text) pairs to train joint embedding models (like CLIP).

## Related

- [[Natural-Language-Supervision|Natural Language Supervision]]
- [[Foundation-Model|Foundation Model]]
