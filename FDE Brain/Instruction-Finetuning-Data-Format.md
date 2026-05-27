---
type: pattern
status: evergreen
aliases:
  - Instruction Finetuning Data Format
  - Instruction-Response Pair
  - Prompt-Completion Format
tags:
  - data-format
  - finetuning
  - llm-training
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/140-data-curation.md
    locator: pages 389-391
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - For instruction finetuning, you need data in the (instruction, response) format.
created: 2026-05-26T21:55:46.301151+00:00
updated: 2026-05-26T21:55:46.301151+00:00
ingestion_run: 8d527d59
---

# Instruction Finetuning Data Format

## Summary

Data structured as explicit pairs of instructions and desired responses, used to teach models to follow specific commands and generate targeted outputs.

## Core Idea

This format is foundational for teaching models general task-following abilities, moving beyond simple next-token prediction to structured, goal-oriented responses.

## Practical Use

Use this format when training a model to perform specific tasks, such as summarizing text, translating languages, or answering factual questions based on a prompt.

## Related

- Chain-of-Thought Data
- Preference Finetuning Data
