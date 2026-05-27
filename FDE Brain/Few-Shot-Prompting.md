---
type: pattern
status: evergreen
aliases:
  - Few-Shot Prompting
  - Example-based prompting
  - In-context learning
tags:
  - prompt-engineering
  - pattern
  - llm-design
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/097-write-clear-and-explicit-instructions.md
    locator: pages 244-246
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Examples can reduce ambiguity about how you want the model to respond.
      - Providing an example can nudge the model toward the response you want.
created: 2026-05-26T21:55:45.932119+00:00
updated: 2026-05-26T21:55:45.932119+00:00
ingestion_run: 8d527d59
---

# Few-Shot Prompting

## Summary

Providing the model with one or more input-output examples within the prompt to demonstrate the desired format, style, or logic.

## Core Idea

Ambiguity is reduced by demonstration. Instead of merely describing the desired output, the model learns the pattern by observing concrete examples, making the response highly predictable.

## Practical Use

When building a classifier or a structured data extraction bot, provide 2-3 examples of (Input: X, Output: Y) pairs. This is crucial for ensuring the model adheres to specific formatting rules (e.g., always outputting JSON, or always using a specific tone).

## Related

- [[Explicit-Instruction-Writing|Explicit Instruction Writing]]
- [[Prompt-Components|Prompt Components]]
