---
type: pattern
status: evergreen
aliases:
  - Prompt-Code Separation Pattern
  - External Prompt Management
  - Separating Prompts from Application Logic
tags:
  - ai-engineering
  - llm-ops
  - software-design
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/103-organize-and-version-prompts.md
    locator: pages 257-258
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - It’s good practice to separate prompts from code.
      - Multiple applications can reuse the same prompt.
      - Code and prompts can be tested separately.
created: 2026-05-26T21:55:45.976199+00:00
updated: 2026-05-26T21:55:45.976199+00:00
ingestion_run: 8d527d59
---

# Prompt-Code Separation Pattern

## Summary

Store prompts in dedicated files or modules (e.g., `prompts.py`) and import them into application code, rather than hardcoding them within the function logic.

## Core Idea

Separating prompts from code increases reusability, allows for independent testing of prompts and code, improves readability, and facilitates collaboration among subject matter experts who may not be proficient in coding.

## Practical Use

When building an application that uses LLMs, define system prompts or core instructions in a dedicated Python file or configuration module. This allows multiple services to reference the same prompt template without duplicating the text, simplifying updates and maintenance.

## Related

- [[Prompt-Versioning-Strategy|Prompt Versioning Strategy]]
- [[Prompt-Metadata-Schema|Prompt Metadata Schema]]
