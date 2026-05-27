---
type: method
status: evergreen
aliases:
  - Lexical Similarity
  - Text overlap measurement
  - Token matching
tags:
  - ai-engineering
  - evaluation
  - metrics
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/065-similarity-measurements-against-reference-data.md
    locator: pages 151-157
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Lexical similarity measures how much two texts overlap. [...] One way to measure lexical similarity is approximate string matching, known colloquially as fuzzy matching. [...] Another way to measure lexical similarity is n-gram similarity, measured based on the overlapping of sequences of tokens, n-grams, instead of single tokens.
created: 2026-05-26T21:55:45.694908+00:00
updated: 2026-05-26T21:55:45.694908+00:00
ingestion_run: 8d527d59
---

# Lexical Similarity

## Summary

A reference-based metric that quantifies how much two texts overlap, measuring similarity based on shared tokens or sequences of tokens, regardless of meaning.

## Core Idea

It measures surface-level textual resemblance. While useful for detecting minor variations, it is prone to failure if the generated response uses synonyms or different phrasing, even if the meaning is identical.

## Practical Use

Implement fuzzy matching (edit distance) or n-gram analysis when the expected output is variable in phrasing but must retain key vocabulary. Be aware that high lexical similarity does not guarantee functional correctness.

## Related

- Fuzzy Matching
- N-gram Similarity
- [[Semantic-Similarity|Semantic Similarity]]
