---
type: method
status: evergreen
aliases:
  - Natural Language Supervision
  - Co-occurrence pairing
tags:
  - ai-engineering
  - data-strategy
  - ml-training
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/017-from-large-language-models-to-foundation-models.md
    locator: pages 32-35
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - OpenAI used a variant of self-supervision called natural language supervision to train their language-image model CLIP...
      - Instead of manually generating labels for each image, they found (image, text) pairs that co-occurred on the internet.
created: 2026-05-26T21:55:45.348400+00:00
updated: 2026-05-26T21:55:45.348400+00:00
ingestion_run: 8d527d59
---

# Natural Language Supervision

## Summary

A specific self-supervised technique used to create massive, weakly labeled datasets by identifying pairs of data (e.g., image and text) that naturally co-occur on the internet, rather than requiring manual labeling.

## Core Idea

This method drastically reduces the cost and time associated with data labeling, allowing models to scale by leveraging the vast, unstructured data available online.

## Practical Use

When training a multimodal embedding model (like CLIP), instead of manually labeling every image, scrape and use large datasets of (image, text) pairs found on the web to train the model's joint embedding space.

## Related

- [[Self-supervised-Learning|Self-supervised Learning]]
- [[Multimodal-Model|Multimodal Model]]
