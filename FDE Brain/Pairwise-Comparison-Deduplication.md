---
type: method
status: evergreen
aliases:
  - Pairwise Comparison Deduplication
  - Similarity Scoring Deduplication
tags:
  - data-engineering
  - algorithm
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/152-deduplicate-data.md
    locator: pages 423-424
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Compute the similarity score of each example to every other example in the dataset, using exact match, n-gram match, fuzzy match, or semantic similarity score.
created: 2026-05-26T21:55:46.406186+00:00
updated: 2026-05-26T21:55:46.406186+00:00
ingestion_run: 8d527d59
---

# Pairwise Comparison Deduplication

## Summary

A brute-force method that computes the similarity score between every single pair of examples in a dataset using various metrics (exact match, n-gram, fuzzy, semantic).

## Core Idea

This method provides the highest accuracy in identifying duplicates but suffers from high computational complexity (O(N^2)), making it impractical for very large datasets.

## Practical Use

Use this method for small, critical datasets where absolute accuracy is paramount, or when the data structure is complex and simple hashing methods might fail. Be prepared for significant computational cost.

## Related

- Similarity Measurement
- Hashing
