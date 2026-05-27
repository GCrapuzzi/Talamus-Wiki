---
type: method
status: evergreen
aliases:
  - Prompt Metadata Schema
  - Structured Prompt Definition
  - Prompt Object Wrapper
tags:
  - ai-engineering
  - llm-ops
  - data-modeling
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/103-organize-and-version-prompts.md
    locator: pages 257-258
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - If you have a lot of prompts across multiple applications, it’s useful to give each prompt metadata...
      - "Your prompt template might also contain other information about how the prompt should be used, such as the following: The model endpoint URL, The ideal sampling parameters, The input schema, The expected output schema."
created: 2026-05-26T21:55:45.978014+00:00
updated: 2026-05-26T21:55:45.978014+00:00
ingestion_run: 8d527d59
---

# Prompt Metadata Schema

## Summary

Wrap prompts in a structured object (e.g., using Pydantic) to store not only the prompt text but also critical operational metadata.

## Core Idea

Metadata transforms a simple text string into a manageable, searchable, and auditable asset. It ensures that every prompt is tied to its intended use case, model, and optimal operational parameters.

## Practical Use

Define a schema that includes fields like `model_name`, `date_created`, `application` (use case), `creator`, `input_schema`, `expected_output_schema`, and optimal sampling parameters (e.g., `temperature`, `top_p`). This is crucial for building a centralized Prompt Library.

## Related

- Prompt Engineering Best Practices
- [[Prompt-Versioning-Strategy|Prompt Versioning Strategy]]
