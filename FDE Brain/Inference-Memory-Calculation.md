---
type: method
status: evergreen
aliases:
  - Inference Memory Calculation
  - LLM Inference Memory Budgeting
  - Forward Pass Memory Estimate
tags:
  - ai-engineering
  - inference
  - llm-deployment
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/131-memory-math.md
    locator: pages 346-348
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - "The memory needed to load the model’s parameters is: N × M"
      - The memory for both activation values and key-value vectors grows linearly with sequence length and batch size.
      - "This assumption brings the model’s memory footprint to: N × M × 1.2"
created: 2026-05-26T21:55:46.223029+00:00
updated: 2026-05-26T21:55:46.223029+00:00
ingestion_run: 8d527d59
---

# Inference Memory Calculation

## Summary

Estimates the memory required during the forward pass (inference), primarily based on model weights and activation/key-value cache storage.

## Core Idea

The memory requirement is dominated by the model weights (N * M) and the memory needed for attention mechanisms (Key-Value vectors), which scale linearly with sequence length and batch size. A common approximation is to multiply the weight memory by 1.2.

## Practical Use

When deploying a model, calculate the weight memory (N * M) and then apply the 1.2 multiplier (or a more precise calculation based on expected context length) to get a rough estimate of the total VRAM needed for stable inference.

## Related

- [[Model-Memory-Footprint-Analysis|Model Memory Footprint Analysis]]
- Key-Value Caching
