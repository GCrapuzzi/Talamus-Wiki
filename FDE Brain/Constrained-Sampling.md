---
type: method
status: evergreen
aliases:
  - Constrained Sampling
  - Grammar-Guided Generation
  - Logit Filtering
tags:
  - ai-engineering
  - llm-architecture
  - constrained-generation
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/052-structured-outputs.md
    locator: pages 123-128
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Constrained sampling filters this logit vector to keep only the tokens that meet the constraints.
      - Building out that grammar and incorporating it into the sampling process is nontrivial.
created: 2026-05-26T21:55:45.610617+00:00
updated: 2026-05-26T21:55:45.610617+00:00
ingestion_run: 8d527d59
---

# Constrained Sampling

## Summary

A technical generation technique that filters the model's logit vector at the token level, ensuring that the model can only sample tokens that adhere to a predefined grammar (e.g., JSON grammar, Regex pattern).

## Core Idea

This method provides the highest level of structural guarantee during generation. It moves beyond simple prompting by mathematically restricting the model's vocabulary choices at every step, making it ideal for complex, formal formats.

## Practical Use

Use this technique when the output format is highly complex (e.g., nested JSON, specific regex patterns) and the reliability of the structure is paramount. Requires specialized library support (e.g., external tools or model APIs supporting grammar constraints).

## Related

- [[Structured-Outputs|Structured Outputs]]
- Grammar Theory
