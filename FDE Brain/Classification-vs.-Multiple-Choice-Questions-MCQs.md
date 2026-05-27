---
type: pattern
status: evergreen
aliases:
  - Classification vs. Multiple Choice Questions (MCQs)
  - Closed-ended Evaluation
  - Discrete Choice Tasks
tags:
  - ai-engineering
  - evaluation
  - metrics
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/079-generation-capability.md
    locator: pages 187-195
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - MCQs are best suited for evaluating knowledge... and reasoning...
      - They aren’t ideal for evaluating generation capabilities such as summarization, translation, and essay writing.
created: 2026-05-26T21:55:45.809976+00:00
updated: 2026-05-26T21:55:45.809976+00:00
ingestion_run: 8d527d59
---

# Classification vs. Multiple Choice Questions (MCQs)

## Summary

A pattern for evaluating model performance on tasks where the output is restricted to a predefined set of choices.

## Core Idea

MCQs and Classification are useful for evaluating knowledge and reasoning (differentiating good from bad responses) but are poor proxies for evaluating open-ended generation capabilities (like summarization or writing).

## Practical Use

Use MCQs/Classification when the goal is to test knowledge recall or logical inference against a fixed set of options. If the goal is creative writing or open-ended synthesis, switch to generation-based evaluation methods (e.g., AI as a Judge).

## Related

- [[Generation-Capability-Metrics-NLG|Generation Capability Metrics (NLG)]]
