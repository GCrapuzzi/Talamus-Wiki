---
type: concept
status: evergreen
aliases:
  - Task-Based Evaluation
  - Goal-Oriented Evaluation
tags:
  - ai-engineering
  - evaluation
  - benchmarking
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/087-step-1.-evaluate-all-components-in-a-system.md
    locator: pages 224-225
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Given that what users really care about is whether a model can help them accomplish their tasks, task-based evaluation is more important.
      - Task-based evaluation evaluates whether a system completes a task.
created: 2026-05-26T21:55:45.859925+00:00
updated: 2026-05-26T21:55:45.859925+00:00
ingestion_run: 8d527d59
---

# Task-Based Evaluation

## Summary

A method of evaluation that measures whether an AI system successfully completes a defined, overarching task, regardless of the number of turns or steps required to achieve it.

## Core Idea

From a user perspective, the most critical metric is whether the model can help them accomplish their goal. Task-based evaluation directly measures this utility, making it generally more important than simply evaluating the quality of individual responses.

## Practical Use

Using benchmarks like the Twenty Questions game, the score is based on whether the model successfully guesses the concept, not just the quality of the 'yes/no' answers provided in each turn.

## Related

- [[Conversational-Evaluation-Paradigms|Conversational Evaluation Paradigms]]
