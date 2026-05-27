---
type: concept
status: evergreen
aliases:
  - Capability Extension Tools
  - Utility Tools
  - Computational Boosters
tags:
  - ai-engineering
  - computation
  - tooling
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/118-tools.md
    locator: pages 302-304
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - AI models are notorious for being bad at math. ... it’s a lot more resource-efficient to just give the model access to a tool.
      - Other simple tools that can significantly boost a model’s capability include a calendar, timezone converter, unit converter... and translator.
      - More complex but powerful tools are code interpreters.
created: 2026-05-26T21:55:46.102950+00:00
updated: 2026-05-26T21:55:46.102950+00:00
ingestion_run: 8d527d59
---

# Capability Extension Tools

## Summary

Tools that address inherent mathematical, logical, or format limitations of the base LLM, allowing the agent to perform tasks outside the model's core text generation competency.

## Core Idea

It is more resource-efficient and accurate to provide a model with a specialized tool (e.g., calculator, code interpreter) than to attempt to fine-tune the model to perform complex, deterministic tasks like arithmetic or unit conversion.

## Practical Use

Prioritize integrating deterministic tools for known weaknesses: use a calculator for math, a code interpreter for data analysis/experimentation, and specialized APIs (e.g., timezone converter) for formatting/utility.

## Related

- [[Code-Interpreter-Tool|Code Interpreter Tool]]
- Math Tool Integration
