---
type: method
status: evergreen
aliases:
  - Post-processing (Structured)
  - Defensive Parsing
  - Output Correction Scripting
tags:
  - ai-engineering
  - data-validation
  - pipeline-design
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/052-structured-outputs.md
    locator: pages 123-128
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Post-processing is simple and cheap but can work surprisingly well.
      - LinkedIn’s defensive YAML parser increased the percentage of correct YAML outputs from 90% to 99.99%.
created: 2026-05-26T21:55:45.608620+00:00
updated: 2026-05-26T21:55:45.608620+00:00
ingestion_run: 8d527d59
---

# Post-processing (Structured)

## Summary

A programmatic layer applied after LLM generation to validate, repair, or transform the raw output into the required structured format (e.g., fixing missing brackets in JSON or YAML).

## Core Idea

LLMs often make predictable, minor formatting errors. Post-processing leverages these common failure modes by implementing simple, cheap scripts to correct the output, significantly boosting the reliability and validity rate.

## Practical Use

Implement a robust parser (e.g., a defensive YAML parser) as the final step in the pipeline. This is highly effective when the model's output is *mostly* correct but contains minor, fixable syntax errors.

## Related

- [[Structured-Outputs|Structured Outputs]]
- JSON
- YAML
