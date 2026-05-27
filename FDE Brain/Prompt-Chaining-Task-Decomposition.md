---
type: pattern
status: evergreen
aliases:
  - Prompt Chaining (Task Decomposition)
  - Task Decomposition
  - Multi-step Prompting
tags:
  - ai-engineering
  - prompt-engineering
  - workflow
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/099-break-complex-tasks-into-simpler-subtasks.md
    locator: pages 248-250
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - For complex tasks that require multiple steps, break those tasks into subtasks.
      - These subtasks are then chained together.
      - "Monitoring: You can monitor not just the final output but also all intermediate outputs."
      - "Debugging: You can isolate the step that is having trouble and fix it independently."
created: 2026-05-26T21:55:45.949182+00:00
updated: 2026-05-26T21:55:45.949182+00:00
ingestion_run: 8d527d59
---

# Prompt Chaining (Task Decomposition)

## Summary

Breaking a complex, multi-step task into a sequence of smaller, independent subtasks, each handled by its own dedicated prompt.

## Core Idea

LLMs perform better and are more reliable when given simpler, focused instructions. Chaining allows the output of one subtask to serve as the input/context for the next, mimicking structured workflow execution.

## Practical Use

Designing complex workflows like customer support chatbots (e.g., Step 1: Intent Classification -> Step 2: Data Retrieval -> Step 3: Response Generation). This approach is crucial for improving reliability and enabling parallel processing.

## Related

- Intent Classification
- [[Context-Grounding|Context Grounding]]
