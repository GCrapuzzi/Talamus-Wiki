---
type: method
status: evergreen
aliases:
  - Data Augmentation via Paraphrasing
  - Query Expansion
  - Semantic Variation Generation
tags:
  - ai-engineering
  - dataset-engineering
  - llm-prompting
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/148-ai-powered-data-synthesis.md
    locator: pages 410-418
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - For example, given the query “How to reset my password?”, AI can paraphrase it to create three new queries...
created: 2026-05-26T21:55:46.377236+00:00
updated: 2026-05-26T21:55:46.377236+00:00
ingestion_run: 8d527d59
---

# Data Augmentation via Paraphrasing

## Summary

Using LLMs to generate semantically equivalent variations (paraphrases) of existing data points (e.g., questions, instructions) to increase dataset size and coverage.

## Core Idea

Paraphrasing helps models generalize better by exposing them to the same underlying concept expressed in multiple ways, mitigating the risk of overfitting to specific phrasing.

## Practical Use

When building instruction datasets, take a core query (e.g., 'How to reset my password?') and prompt an LLM to generate 5-10 variations ('I forgot my password.', 'Steps to reset passwords.') to ensure the model understands the intent regardless of the phrasing.

## Related

- AI-Powered Data Synthesis
- Instruction Data Synthesis
