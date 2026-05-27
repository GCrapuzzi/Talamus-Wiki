---
type: pattern
status: evergreen
aliases:
  - Open-Ended vs. Close-Ended Evaluation
  - Text Generation Evaluation Scope
tags:
  - ai-engineering
  - evaluation-design
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/063-exact-evaluation.md
    locator: pages 149-149
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - This section focuses on evaluating open-ended responses (arbitrary text generation) as opposed to close-ended responses (such as classification).
      - Close-ended evaluation is already well understood.
created: 2026-05-26T21:55:45.682034+00:00
updated: 2026-05-26T21:55:45.682034+00:00
ingestion_run: 8d527d59
---

# Open-Ended vs. Close-Ended Evaluation

## Summary

A classification pattern for LLM evaluation based on the required output format: close-ended tasks have limited, predefined answers (e.g., classification), while open-ended tasks involve arbitrary text generation (e.g., summarization).

## Core Idea

The choice of evaluation methodology (exact vs. subjective) is dictated by whether the task is open-ended or close-ended. Open-ended tasks require specialized exact methods.

## Practical Use

When scoping an LLM project, first classify the task. If the output is free-form text, plan for exact methods like functional correctness. If the output is limited to predefined categories, standard classification metrics apply.

## Related

- [[Exact-Evaluation|Exact Evaluation]]
- Functional Correctness
