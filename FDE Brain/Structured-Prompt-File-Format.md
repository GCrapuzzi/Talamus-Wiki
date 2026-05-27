---
type: method
status: evergreen
aliases:
  - Structured Prompt File Format
  - Dotprompt
  - Prompt Template Format
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
      - Several tools have proposed special .prompt file formats to store prompts.
      - "Here’s an example of Firebase Dotprompt file: model: vertexai/gemini-1.5-flash... output: format: json schema: name: string..."
created: 2026-05-26T21:55:45.982911+00:00
updated: 2026-05-26T21:55:45.982911+00:00
ingestion_run: 8d527d59
---

# Structured Prompt File Format

## Summary

Use a standardized, structured file format (e.g., YAML, JSON, or specialized formats like Dotprompt) to store prompts and their associated operational parameters in a single file.

## Core Idea

Structured formats move beyond simple text files, allowing the prompt definition to encapsulate all necessary context for execution, including model selection, input/output schemas, and system instructions, making the prompt self-contained and machine-readable.

## Practical Use

Adopt a standardized format for prompt storage. This format should clearly delineate sections for the target model (`model:`), the input structure (`input:`), the desired output structure (`output:`), and the core prompt text. This facilitates automated validation and generation of API calls.

## Related

- [[Prompt-Metadata-Schema|Prompt Metadata Schema]]
