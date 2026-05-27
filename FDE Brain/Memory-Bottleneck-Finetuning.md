---
type: concept
status: evergreen
aliases:
  - Memory Bottleneck (Finetuning)
  - Finetuning Memory Constraint
  - LLM Training Memory Overhead
tags:
  - ai-engineering
  - llm-training
  - hardware-optimization
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/129-memory-bottlenecks.md
    locator: pages 343-343
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Finetuning is memory-intensive.
      - Many finetuning techniques aim to minimize their memory footprint.
      - Understanding what causes this memory bottleneck is necessary to understand why and how these techniques work.
created: 2026-05-26T21:55:46.209394+00:00
updated: 2026-05-26T21:55:46.209394+00:00
ingestion_run: 8d527d59
---

# Memory Bottleneck (Finetuning)

## Summary

The primary challenge in finetuning large language models, referring to the intensive computational memory required to train the model parameters.

## Core Idea

Finetuning is memory-intensive. Understanding the source of this bottleneck is crucial for selecting appropriate parameter-efficient finetuning (PEFT) techniques and estimating necessary hardware resources.

## Practical Use

When planning a finetuning project, first estimate the memory requirements using back-of-the-napkin formulas. This guides the selection of memory-efficient techniques (e.g., LoRA, QLoRA) to ensure the project is feasible on available hardware.

## Related

- Finetuning Strategy
- [[Parameter-Efficient-Finetuning-PEFT|Parameter-Efficient Finetuning (PEFT)]]
