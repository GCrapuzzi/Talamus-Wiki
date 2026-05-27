---
type: pattern
status: evergreen
aliases:
  - Prompt Engineering Structure
  - Structured Prompting
  - Prompt Components
tags:
  - ai-engineering
  - prompt-engineering
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/092-introduction-to-prompting.md
    locator: pages 236-236
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - "A prompt generally consists of one or more of the following parts: Task description, Example(s) of how to do this task, The task."
created: 2026-05-26T21:55:45.897843+00:00
updated: 2026-05-26T21:55:45.897843+00:00
ingestion_run: 8d527d59
---

# Prompt Engineering Structure

## Summary

A systematic pattern for constructing effective prompts by explicitly including a Task Description, Examples, and the concrete Task input, ensuring the model understands its role and required output format.

## Core Idea

Effective prompting requires moving beyond simple natural language queries. By structuring the prompt with defined components (Role, Task, Examples), the engineer guides the model's behavior, significantly improving adherence and output reliability.

## Practical Use

When designing an LLM application, decompose the requirement into these components: 1) Define the model's role/persona. 2) Provide explicit instructions (Task Description). 3) Include 1-3 examples (Few-Shot). 4) Insert the variable input (The Task).

## Related

- Few-Shot Learning
- Role Prompting
