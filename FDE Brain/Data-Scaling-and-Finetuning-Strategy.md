---
type: framework
status: evergreen
aliases:
  - Data Scaling and Finetuning Strategy
  - Data Quantity Decision Framework
  - Finetuning Data Strategy
tags:
  - ai-engineering
  - finetuning
  - llm-deployment
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/143-data-quantity.md
    locator: pages 396-400
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - If you have only a few hundred or a few thousand examples, PEFT might work best.
      - If you have tens of thousands to millions of (instruction, response) pairs, you might want to attempt full finetuning.
created: 2026-05-26T21:55:46.334454+00:00
updated: 2026-05-26T21:55:46.334454+00:00
ingestion_run: 8d527d59
---

# Data Scaling and Finetuning Strategy

## Summary

A decision framework guiding the choice between Full Finetuning and Parameter-Efficient Finetuning (PEFT) based on available data volume and task complexity.

## Core Idea

The optimal finetuning approach depends on the data volume. PEFT (e.g., LoRA) is preferred for small datasets (hundreds to thousands of examples), while Full Finetuning is necessary for large datasets (tens of thousands to millions of examples) to achieve peak performance.

## Practical Use

When starting a project, first assess the data volume. If data is scarce, use PEFT on a high-performing base model. If data is abundant, evaluate Full Finetuning, but be aware of the risk of 'ossification' (see related concepts).

## Related

- [[Ossification-in-Finetuning|Ossification in Finetuning]]
- [[Data-Scaling-and-Performance-Plotting|Data Scaling and Performance Plotting]]
- [[Data-Scarcity-Finetuning-Strategies|Data Scarcity Finetuning Strategies]]
