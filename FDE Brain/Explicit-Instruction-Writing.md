---
type: method
status: evergreen
aliases:
  - Explicit Instruction Writing
  - Constraint definition
  - Clarity mandate
tags:
  - prompt-engineering
  - method
  - reliability
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/097-write-clear-and-explicit-instructions.md
    locator: pages 244-246
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Explain, without ambiguity, what you want the model to do
      - If the model outputs fractional scores (4.5) and you don’t want fractional scores, update your prompt to tell the model to output only integer scores.
created: 2026-05-26T21:55:45.936941+00:00
updated: 2026-05-26T21:55:45.936941+00:00
ingestion_run: 8d527d59
---

# Explicit Instruction Writing

## Summary

Writing instructions that eliminate all ambiguity regarding the desired output format, scope, and constraints.

## Core Idea

Vague instructions lead to variable and unpredictable outputs. By explicitly defining boundaries (e.g., score range, data type, required format), the model's output becomes reliable and deterministic.

## Practical Use

Always specify constraints: If scoring, define the scale (e.g., 'Use a 1-5 scale'). If outputting data, specify the format (e.g., 'Output only a JSON object with keys: name, score'). If the model must fail, specify the failure output (e.g., 'If uncertain, output 'I don't know'').

## Related

- [[Prompt-Components|Prompt Components]]
