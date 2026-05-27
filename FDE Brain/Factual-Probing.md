---
type: framework
status: evergreen
aliases:
  - Factual Probing
  - Knowledge Probing
  - LAMA Benchmark
tags:
  - ai-engineering
  - auditing
  - evaluation
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/107-information-extraction.md
    locator: pages 267-271
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Factual probing focuses on figuring out what a model knows.
      - Relational knowledge follows the format 'X [relation] Y'.
created: 2026-05-26T21:55:46.011890+00:00
updated: 2026-05-26T21:55:46.011890+00:00
ingestion_run: 8d527d59
---

# Factual Probing

## Summary

A systematic research methodology used to determine the specific relational knowledge ('X [relation] Y') that an LLM has memorized from its training data.

## Core Idea

By using structured prompts (like fill-in-the-blank statements), researchers can test the boundaries of the model's knowledge, revealing not only general facts but also potential points of data leakage.

## Practical Use

Use this framework during model auditing and red-teaming to assess the risk of data leakage and ensure the model's knowledge base adheres to required privacy and compliance standards before deployment.

## Related

- [[Training-Data-Extraction-Memorization-Attacks|Training Data Extraction (Memorization Attacks)]]
