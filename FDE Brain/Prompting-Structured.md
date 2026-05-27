---
type: method
status: evergreen
aliases:
  - Prompting (Structured)
  - Instruction-Based Formatting
  - Zero-Shot Structuring
tags:
  - ai-engineering
  - prompt-engineering
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/052-structured-outputs.md
    locator: pages 123-128
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Prompting is the first line of action for structured outputs.
      - Whether a model can follow this instruction depends on the model’s instruction-following capability.
created: 2026-05-26T21:55:45.606214+00:00
updated: 2026-05-26T21:55:45.606214+00:00
ingestion_run: 8d527d59
---

# Prompting (Structured)

## Summary

The initial, simplest method of guiding an LLM to generate structured output by explicitly instructing the model within the prompt (e.g., 'Return only a JSON object...').

## Core Idea

Prompting is the first line of defense for structured outputs. While easy to implement, its reliability is highly dependent on the model's inherent instruction-following capability and is not guaranteed.

## Practical Use

Use this method for low-stakes, exploratory tasks or as a preliminary step. Always pair it with a validation layer (like post-processing) if the output is critical.

## Related

- Post-processing
- [[Constrained-Sampling|Constrained Sampling]]
