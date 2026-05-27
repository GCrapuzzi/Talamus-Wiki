---
type: method
status: evergreen
aliases:
  - Self-Supervision
  - Unsupervised pre-training
tags:
  - ai-engineering
  - training
  - llm
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/015-the-rise-of-ai-engineering.md
    locator: pages 26-26
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Language models... only been able to grow to the scale they are today with self-supervision.
created: 2026-05-26T21:55:45.323870+00:00
updated: 2026-05-26T21:55:45.323870+00:00
ingestion_run: 8d527d59
---

# Self-Supervision

## Summary

A training methodology where a model learns from unlabeled data by creating proxy tasks (e.g., predicting masked words or filling in blanks) that force the model to learn the underlying structure and relationships within the data.

## Core Idea

Self-supervision is the mechanism that allows models to scale to massive datasets (like the entire internet) without requiring expensive, human-labeled data, enabling the creation of LLMs.

## Practical Use

Understanding this method explains why LLMs are so powerful: they have learned general world knowledge and linguistic patterns from the sheer volume of raw, unlabeled text, making them highly adaptable.

## Related

- Large Language Models (LLMs)
- [[Foundation-Models-FMs|Foundation Models (FMs)]]
