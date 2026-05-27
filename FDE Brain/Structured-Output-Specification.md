---
type: method
status: evergreen
aliases:
  - Structured Output Specification
  - JSON Schema Prompting
  - Forced Output Format
tags:
  - ai-engineering
  - prompt-engineering
  - json
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/098-provide-sufficient-context.md
    locator: pages 247-247
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - If you want the model to generate JSON, specify what the keys in the JSON should be. Give examples if necessary.
      - For tasks expecting structured outputs, such as classification, use markers to mark the end of the prompts to let the model know that the structured outputs should begin.
created: 2026-05-26T21:55:45.943915+00:00
updated: 2026-05-26T21:55:45.943915+00:00
ingestion_run: 8d527d59
---

# Structured Output Specification

## Summary

A technique requiring the explicit definition of the desired output format (e.g., JSON schema, XML, list format) and the use of unique markers to delineate the end of the input and the start of the structured output.

## Core Idea

LLMs require explicit boundaries to transition from processing input to generating structured output. Failure to use markers can cause the model to append generated content to the input prompt, corrupting the data.

## Practical Use

When requesting JSON output, specify the exact keys and data types (e.g., 'The output must be a JSON object with keys: 'name' (string) and 'score' (integer)'). Use unique delimiters (e.g., 'OUTPUT_START: {...') to signal the model where the structured response must begin.

## Related

- Pydantic Integration
- Prompt Delimiters
