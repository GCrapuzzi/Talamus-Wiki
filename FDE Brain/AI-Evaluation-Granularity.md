---
type: framework
status: evergreen
aliases:
  - AI Evaluation Granularity
  - Multi-Level Evaluation
tags:
  - ai-engineering
  - evaluation
  - llm-ops
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/087-step-1.-evaluate-all-components-in-a-system.md
    locator: pages 224-225
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - "Evaluation can happen at different levels: per task, per turn, and per intermediate output."
      - You should evaluate the end-to-end output and each component’s intermediate output independently.
created: 2026-05-26T21:55:45.857851+00:00
updated: 2026-05-26T21:55:45.857851+00:00
ingestion_run: 8d527d59
---

# AI Evaluation Granularity

## Summary

The principle that AI system evaluation must occur at multiple levels of abstraction: per task, per turn, and per intermediate output.

## Core Idea

The success of an AI application depends on the ability to differentiate good outcomes from bad ones. A comprehensive evaluation pipeline must account for the entire operational lifecycle, from raw input processing to final output generation.

## Practical Use

When designing a benchmark, define specific evaluation points: 1) The quality of the initial text extraction (intermediate output). 2) The accuracy of the core extraction (per task). 3) The overall success of the goal (per task).

## Related

- [[Multi-Component-Evaluation-Pipeline|Multi-Component Evaluation Pipeline]]
- [[Conversational-Evaluation-Paradigms|Conversational Evaluation Paradigms]]
