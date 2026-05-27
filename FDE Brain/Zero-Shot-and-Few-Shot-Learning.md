---
type: pattern
status: evergreen
aliases:
  - Zero-Shot and Few-Shot Learning
  - Shot-based prompting
  - Example-based prompting
tags:
  - prompt-engineering
  - llm-optimization
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/093-in-context-learning-zero-shot-and-few-shot.md
    locator: pages 237-238
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - When no example is provided, it’s zero-shot learning.
      - Teaching a model to learn from examples in the prompt is also called few-shot learning.
created: 2026-05-26T21:55:45.902977+00:00
updated: 2026-05-26T21:55:45.902977+00:00
ingestion_run: 8d527d59
---

# Zero-Shot and Few-Shot Learning

## Summary

A methodology for guiding LLM behavior by providing examples within the prompt. Zero-shot learning provides no examples, while few-shot learning provides a small number of input-output examples (shots).

## Core Idea

The number of examples (shots) provided in the prompt dictates the learning approach. While more examples generally improve performance, modern, powerful models (like GPT-4) often show diminishing returns, suggesting that strong models can follow instructions effectively with fewer examples.

## Practical Use

Start with zero-shot prompting for simple tasks. If performance is insufficient, incrementally add few-shot examples (e.g., 1 to 5 examples) to define the desired input/output format or complex reasoning pattern. Monitor the trade-off between performance gain and increased inference cost due to longer prompts.

## Related

- [[In-Context-Learning-ICL|In-Context Learning (ICL)]]
