---
type: pattern
status: evergreen
aliases:
  - Prompting-First Experimentation Hierarchy
  - Prompting before Finetuning
  - Systematic Prompting Approach
tags:
  - ai-engineering
  - llm-development
  - experimentation
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/127-reasons-not-to-finetune.md
    locator: pages 336-339
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - AI engineering experiments should start with prompting, following the best practices discussed in Chapter 6.
      - Explore more advanced solutions only if prompting alone proves inadequate.
created: 2026-05-26T21:55:46.188210+00:00
updated: 2026-05-26T21:55:46.188210+00:00
ingestion_run: 8d527d59
---

# Prompting-First Experimentation Hierarchy

## Summary

Always start AI engineering experiments with systematic prompt engineering and context provision before attempting finetuning. Finetuning should only be considered if prompting alone proves inadequate.

## Core Idea

Finetuning requires significant upfront investment (data, compute, maintenance) and is complex. Prompting is the lowest-effort, highest-leverage starting point. This minimizes risk and cost during the initial proof-of-concept phase.

## Practical Use

When building a new AI feature, first define the prompt structure, test various examples, and rigorously define metrics. Only if the performance ceiling is hit by the best prompts should resources be allocated to data collection and finetuning.

## Related

- Contextual Prompting
- Systematic Prompt Testing
