---
type: framework
status: evergreen
aliases:
  - Deduplication Granularity Definition
  - Scope of Duplication Check
  - Matching Level Definition
tags:
  - data-engineering
  - preprocessing
  - nlp
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/152-deduplicate-data.md
    locator: pages 423-424
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Do you want to deal with duplications at the document level, paragraph level, sentence level, or token level?
      - Would two texts have to match exactly to be considered duplicates, or would an 80% overlap be sufficient?
created: 2026-05-26T21:55:46.404887+00:00
updated: 2026-05-26T21:55:46.404887+00:00
ingestion_run: 8d527d59
---

# Deduplication Granularity Definition

## Summary

A decision framework requiring the engineer to define the scope and required match threshold for identifying duplicates within a dataset.

## Core Idea

The definition of 'duplicate' is not universal. The engineer must explicitly decide the level of comparison (e.g., document level, paragraph level, sentence level, or token level) and the required similarity threshold (e.g., exact match vs. 80% overlap) to ensure the deduplication process is relevant to the data's structure and the model's task.

## Practical Use

When dealing with unstructured text (e.g., legal documents, articles), first define the unit of analysis. If the goal is to prevent plagiarism, use the sentence/paragraph level. If the goal is to ensure unique records, use the document level. This definition guides the choice of matching algorithm.

## Related

- Similarity Measurement
- Text Preprocessing
