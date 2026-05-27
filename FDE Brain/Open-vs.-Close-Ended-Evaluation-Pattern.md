---
type: pattern
status: evergreen
aliases:
  - Open vs. Close-Ended Evaluation Pattern
  - Multiple-choice evaluation
  - Structured output testing
tags:
  - ai-engineering
  - evaluation
  - benchmarking
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/078-domain-specific-capability.md
    locator: pages 185-186
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Non-coding domain capabilities are often evaluated with close-ended tasks, such as multiple-choice questions.
      - Close-ended outputs are easier to verify and reproduce.
created: 2026-05-26T21:55:45.799343+00:00
updated: 2026-05-26T21:55:45.799343+00:00
ingestion_run: 8d527d59
---

# Open vs. Close-Ended Evaluation Pattern

## Summary

A methodological pattern for evaluating model performance by restricting the model's output to a predefined set of options (close-ended) rather than allowing free-form generation (open-ended).

## Core Idea

Close-ended tasks are significantly easier to verify, reproduce, and automate evaluation for, leading to more consistent and reliable benchmark results compared to open-ended tasks.

## Practical Use

When building a benchmark for non-coding tasks (e.g., math, general knowledge), structure the task as a multiple-choice question (MCQ) rather than asking the model to generate a full solution. This maximizes evaluation reliability, as seen in MMLU and AGIEval.

## Related

- [[Domain-Specific-Capability-Evaluation|Domain-Specific Capability Evaluation]]
- Evaluation-Driven Development
