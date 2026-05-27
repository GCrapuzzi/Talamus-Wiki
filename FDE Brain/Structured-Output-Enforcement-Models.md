---
type: method
status: evergreen
aliases:
  - Structured Output Enforcement Models
  - Schema-Guided Generation
  - Constrained Output
tags:
  - ai-engineering
  - data-extraction
  - llm-ops
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/102-evaluate-prompt-engineering-tools.md
    locator: pages 254-256
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Many tools aim to assist parts of prompt engineering. For example, Guidance, Outlines, and Instructor guide models toward structured outputs.
created: 2026-05-26T21:55:45.971940+00:00
updated: 2026-05-26T21:55:45.971940+00:00
ingestion_run: 8d527d59
---

# Structured Output Enforcement Models

## Summary

Using specialized models or tools (e.g., Guidance, Instructor) to force the LLM output into a predefined, machine-readable structure (like JSON or XML), minimizing parsing errors.

## Core Idea

For reliable integration into downstream systems, the LLM output must be predictable. These tools enforce structure at the generation level, rather than relying on post-processing validation.

## Practical Use

When the LLM output needs to feed directly into a database, API, or structured workflow, use a structured output model. Provide the schema definition (e.g., JSON schema) as part of the prompt context.

## Related

- Pydantic Integration
- API Design
