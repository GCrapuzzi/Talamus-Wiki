---
type: method
status: evergreen
aliases:
  - Exact Match Evaluation
  - Strict matching
  - Binary comparison
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
      - It’s considered an exact match if the generated response matches one of the reference responses exactly. Exact matching works for tasks that expect short, exact responses such as simple math problems, common knowledge queries, and trivia-style questions.
created: 2026-05-26T21:55:45.692967+00:00
updated: 2026-05-26T21:55:45.692967+00:00
ingestion_run: 8d527d59
---

# Exact Match Evaluation

## Summary

A reference-based metric that determines if the generated response matches one of the reference responses character-for-character. It is binary (match or not).

## Core Idea

Ideal for tasks requiring short, definitive, and unambiguous answers (e.g., math problems, trivia). It fails for complex, open-ended tasks where multiple correct formulations exist.

## Practical Use

Use this method only when the expected output format is highly constrained and non-negotiable. Be cautious, as minor factual errors (e.g., wrong date) can lead to a failed match even if the core concept is correct.

## Related

- [[Lexical-Similarity|Lexical Similarity]]
- [[Semantic-Similarity|Semantic Similarity]]
