---
type: pattern
status: evergreen
aliases:
  - Model Merging
  - Adapter Combination
tags:
  - ai-engineering
  - finetuning
  - deployment
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/138-summary.md
    locator: pages 385-386
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - The idea of combining finetuned models brought the chapter to model merging; its goal is to combine multiple models into one model that works better than these models separately.
created: 2026-05-26T21:55:46.286947+00:00
updated: 2026-05-26T21:55:46.286947+00:00
ingestion_run: 8d527d59
---

# Model Merging

## Summary

The process of combining the weights or knowledge from multiple independently finetuned models (or adapters) into a single, unified model that ideally performs better than the individual components.

## Core Idea

It enables the aggregation of specialized knowledge from multiple sources or tasks into one cohesive, deployable asset, improving overall system performance and utility.

## Practical Use

Combine multiple LoRA adapters trained on different datasets (e.g., one for medical jargon, one for legal summarization) into a single model for comprehensive, multi-domain deployment.

## Related

- [[LoRA-Low-Rank-Adaptation|LoRA (Low-Rank Adaptation)]]
- PEFT
