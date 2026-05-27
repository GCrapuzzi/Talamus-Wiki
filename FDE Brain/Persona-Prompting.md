---
type: pattern
status: evergreen
aliases:
  - Persona Prompting
  - Role-playing prompt
  - Adopting a persona
tags:
  - prompt-engineering
  - pattern
  - tone-control
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/097-write-clear-and-explicit-instructions.md
    locator: pages 244-246
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Ask the model to adopt a persona
      - A persona can help the model to understand the perspective it’s supposed to use to generate responses.
created: 2026-05-26T21:55:45.934069+00:00
updated: 2026-05-26T21:55:45.934069+00:00
ingestion_run: 8d527d59
---

# Persona Prompting

## Summary

Instructing the model to adopt a specific professional, emotional, or fictional persona before generating a response.

## Core Idea

The persona acts as a constraint on the model's knowledge base, tone, and perspective. It forces the model to filter its general knowledge through a specific lens, leading to more contextually appropriate and consistent output.

## Practical Use

When generating educational content, instruct the model: 'Act as a fifth-grade science teacher...' When writing marketing copy, instruct: 'Adopt the persona of a witty, cynical copywriter.' This ensures the tone matches the intended audience.

## Related

- [[Explicit-Instruction-Writing|Explicit Instruction Writing]]
