---
type: technique
status: evergreen
aliases:
  - DPO (Direct Preference Optimization)
  - Direct Preference Optimization
tags:
  - ai-engineering
  - llm-methods
  - optimization
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/045-post-training.md
    locator: pages 102-103
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Techniques for preference finetuning include... DPO (Direct Preference Optimization) (used by Llama 3).
created: 2026-05-26T21:55:45.550372+00:00
updated: 2026-05-26T21:55:45.550372+00:00
ingestion_run: 8d527d59
---

# DPO (Direct Preference Optimization)

## Summary

A modern, resource-efficient preference finetuning technique that directly optimizes the LLM's policy using preferred/rejected pairs, bypassing the need to explicitly train a separate reward model.

## Core Idea

DPO simplifies the alignment process by formulating the preference objective as a direct loss function applied to the policy model, making the training loop more stable and computationally cheaper than traditional RLHF.

## Practical Use

Ideal for rapid iteration and resource-constrained environments. Used by models like Llama 3, demonstrating a shift toward simpler, direct optimization methods.

## Related

- [[Preference-Finetuning|Preference Finetuning]]
- RLHF
