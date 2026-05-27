---
type: method
status: evergreen
aliases:
  - Top-k Sampling
  - k-sampling
tags:
  - ai-engineering
  - llm-sampling
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/050-sampling-strategies.md
    locator: pages 114-119
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - To avoid this problem [computational expense], after the model has computed the logits, we pick the top-k logits and perform softmax over these top-k logits only.
created: 2026-05-26T21:55:45.584835+00:00
updated: 2026-05-26T21:55:45.584835+00:00
ingestion_run: 8d527d59
---

# Top-k Sampling

## Summary

A sampling strategy that restricts the model's vocabulary choice to the $k$ tokens with the highest logits, performing softmax only over this reduced set.

## Core Idea

Instead of calculating probabilities for the entire vocabulary (which is computationally expensive), Top-k limits the search space to the $k$ most probable tokens. This reduces computational load while maintaining a degree of diversity.

## Practical Use

Use Top-k when the full vocabulary is too large for efficient sampling, but you still want to allow for some variation beyond the single most likely token. The value of $k$ controls the balance between predictability (small $k$) and diversity (large $k$).

## Related

- [[Top-p-Sampling|Top-p Sampling]]
- Sampling Strategies
