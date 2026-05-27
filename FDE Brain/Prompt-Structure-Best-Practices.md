---
type: pattern
status: evergreen
aliases:
  - Prompt Structure Best Practices
  - Task placement strategy
tags:
  - prompt-engineering
  - llm-optimization
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/093-in-context-learning-zero-shot-and-few-shot.md
    locator: pages 237-238
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Most models, including GPT-4, empirically perform better when the task description is at the beginning of the prompt.
      - However, some models, including Llama 3, seem to perform better when the task description is at the end of the prompt.
created: 2026-05-26T21:55:45.907719+00:00
updated: 2026-05-26T21:55:45.907719+00:00
ingestion_run: 8d527d59
---

# Prompt Structure Best Practices

## Summary

Guidelines for optimizing the placement of the task description within the overall prompt input, as different LLMs exhibit varying preferences.

## Core Idea

While general best practice suggests placing the task description at the beginning (e.g., GPT-4), some models (e.g., Llama 3) perform better when the task description is placed at the end of the prompt, following the examples or context.

## Practical Use

When developing a prompt template, test the task description placement (beginning vs. end) across the target model family. If the model is known to prefer a specific structure, adhere to that pattern to maximize performance.

## Related

- [[In-Context-Learning-ICL|In-Context Learning (ICL)]]
