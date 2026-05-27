---
type: concept
status: evergreen
aliases:
  - Behavior-Based Failure (Finetuning Use Case)
  - Format Adherence
  - Style Correction
  - Semantic Parsing
tags:
  - ai-engineering
  - llm-training
  - data-structuring
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/128-finetuning-and-rag.md
    locator: pages 340-342
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - If the model has behavioral issues, finetuning might help.
      - Another issue is when it fails to follow the expected output format.
      - Semantic parsing is a category of tasks whose success hinges on the model’s ability to generate outputs in the expected format, therefore, often requires finetuning.
created: 2026-05-26T21:55:46.202615+00:00
updated: 2026-05-26T21:55:46.202615+00:00
ingestion_run: 8d527d59
---

# Behavior-Based Failure (Finetuning Use Case)

## Summary

Failures where the model's output is factually correct but fails to meet specific structural requirements, desired style, or expected output format.

## Core Idea

Finetuning is used to teach the model specific behaviors, styles, and formats (like generating valid JSON or adhering to a domain-specific language) that were not sufficiently represented in its general training data.

## Practical Use

Use finetuning when the task requires strict adherence to a schema (e.g., JSON, XML), a specific technical style (e.g., generating compilable code), or when the model needs to adopt a specific persona or tone.

## Related

- [[Semantic-Parsing|Semantic Parsing]]
- Prompt Engineering (for format definition)
