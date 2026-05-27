---
type: concept
status: evergreen
aliases:
  - Multimodal Embedding Space
  - Joint embedding space
tags:
  - ai-engineering
  - embeddings
  - multimodal
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/067-ai-as-a-judge.md
    locator: pages 160-160
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - A joint embedding space that can represent data of different modalities is a multimodal embedding space.
      - In a text–image joint embedding space, the embedding of an image... should be closer to the embedding of the text... than the embedding of the text...
created: 2026-05-26T21:55:45.709543+00:00
updated: 2026-05-26T21:55:45.709543+00:00
ingestion_run: 8d527d59
---

# Multimodal Embedding Space

## Summary

A joint vector space that represents data from multiple modalities (e.g., text and images) in a single, comparable mathematical space.

## Core Idea

It allows embeddings of different modalities to be compared and combined, enabling cross-modal tasks like text-based image search, where the query modality differs from the content modality.

## Practical Use

Designing search or retrieval systems that must handle mixed inputs (e.g., using a text prompt to find a relevant image).

## Related

- CLIP Architecture
