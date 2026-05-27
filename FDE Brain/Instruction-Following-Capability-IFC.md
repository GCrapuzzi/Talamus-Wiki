---
type: concept
status: evergreen
aliases:
  - Instruction-Following Capability (IFC)
  - Instruction Adherence
  - Prompt Following
tags:
  - ai-engineering
  - evaluation
  - llm-reliability
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/080-instruction-following-capability.md
    locator: pages 196-200
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Instruction-following capability is essential for applications that require structured outputs, such as in JSON format or matching a regular expression (regex).
      - If the model outputs 'That’s correct', this output isn’t very helpful and will likely break downstream applications that expect only A, B, or C.
created: 2026-05-26T21:55:45.811496+00:00
updated: 2026-05-26T21:55:45.811496+00:00
ingestion_run: 8d527d59
---

# Instruction-Following Capability (IFC)

## Summary

The model's ability to generate outputs that strictly adhere to all constraints, formats, and rules specified in the prompt, regardless of its underlying domain knowledge.

## Core Idea

IFC is a core requirement for foundation models, especially for downstream applications. Poor IFC means even domain-specific knowledge cannot be reliably utilized if the output format is incorrect (e.g., generating 'That's correct' instead of a required JSON field).

## Practical Use

When designing an LLM application, always test for IFC using structured output requirements (JSON, YAML, regex matching) and explicit constraints (word count, forbidden words) to ensure reliability for production systems.

## Related

- [[Structured-Output-Generation|Structured Output Generation]]
- [[Prompt-Engineering|Prompt Engineering]]
