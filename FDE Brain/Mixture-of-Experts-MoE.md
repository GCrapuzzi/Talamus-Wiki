---
type: pattern
status: evergreen
aliases:
  - Mixture-of-Experts (MoE)
  - MoE Model
  - Sparse Activation Model
tags:
  - ai-engineering
  - model-architecture
  - optimization
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/044-model-size.md
    locator: pages 91-101
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - An MoE model is divided into different groups of parameters, and each group is an expert.
      - Only a subset of the experts is active for (used to) process each token.
created: 2026-05-26T21:55:45.538606+00:00
updated: 2026-05-26T21:55:45.538606+00:00
ingestion_run: 8d527d59
---

# Mixture-of-Experts (MoE)

## Summary

An architectural pattern where the model is divided into multiple specialized groups of parameters (experts). For any given input token, only a small, selected subset of experts is activated and used for processing.

## Core Idea

MoE models decouple the total parameter count (which can be very large) from the active compute cost (which is determined by the number of experts used per token). This allows for high capacity with efficient inference speed.

## Practical Use

When designing or selecting a model, if the goal is to maximize parameter count while maintaining low inference latency, an MoE architecture is preferred. The effective compute cost is proportional to the number of active experts, not the total number of experts.

## Related

- [[Sparsity-in-Large-Models|Sparsity in Large Models]]
- [[Model-Parameter-Count|Model Parameter Count]]
