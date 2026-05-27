---
type: glossary
status: evergreen
aliases:
  - Prompt
  - LLM Instruction
  - Input Query
tags:
  - ai-engineering
  - llm
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/092-introduction-to-prompting.md
    locator: pages 236-236
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - A prompt is an instruction given to a model to perform a task.
      - "A prompt generally consists of one or more of the following parts: Task description, Example(s) of how to do this task, The task."
created: 2026-05-26T21:55:45.899454+00:00
updated: 2026-05-26T21:55:45.899454+00:00
ingestion_run: 8d527d59
---

# Prompt

## Summary

The complete instruction given to a Large Language Model (LLM) to elicit a desired output. It is a structured artifact, not merely a question.

## Core Idea

A prompt must contain enough explicit instruction (including role and format) for the model to successfully execute the task. If the model struggles to follow instructions, the prompt's quality is irrelevant.

## Practical Use

When documenting an LLM pipeline, treat the prompt as a template containing placeholders for variables (e.g., `{{user_input}}`, `{{desired_format}}`) rather than a static string.

## Related

- [[Prompt-Engineering-Structure|Prompt Engineering Structure]]
