---
type: concept
status: evergreen
aliases:
  - Task Vectors (Delta Parameters)
  - Task Embedding
  - Task Delta
tags:
  - ai-engineering
  - llm-theory
  - task-arithmetic
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/136-model-merging-and-multi-task-finetuning.md
    locator: pages 371-380
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Subtracting the base model from it should give you a vector that captures the essence of the task.
      - Task vectors allow us to do task arithmetic, such as adding two task vectors to combine task capabilities or subtracting a task vector to reduce specific capabilities.
created: 2026-05-26T21:55:46.267833+00:00
updated: 2026-05-26T21:55:46.267833+00:00
ingestion_run: 8d527d59
---

# Task Vectors (Delta Parameters)

## Summary

A vector representation that captures the specific capability or knowledge gained by finetuning a base model for a single task. It is derived by subtracting the base model's parameters from the task-specific model's parameters.

## Core Idea

By isolating the task-specific changes (the delta), complex task capabilities can be treated as vectors. This allows for 'task arithmetic,' enabling the combination or subtraction of skills.

## Practical Use

To combine two tasks (Task A and Task B), calculate the task vector for A and the task vector for B, and then add them together (Task A + Task B). Task subtraction can be used to remove undesirable behaviors or biases.

## Related

- [[Linear-Combination-Merging|Linear Combination Merging]]
- [[Model-Merging|Model Merging]]
