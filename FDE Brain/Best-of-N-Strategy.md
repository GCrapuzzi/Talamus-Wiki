---
type: pattern
status: evergreen
aliases:
  - Best of N Strategy
  - Ensemble Sampling
  - Multiple Output Selection
tags:
  - llm-deployment
  - optimization
  - prompt-engineering
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/049-sampling-fundamentals.md
    locator: pages 112-113
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - They get their models to generate multiple outputs and pick the ones given high scores by their reward models. This approach, often referred to as the best of N strategy...
created: 2026-05-26T21:55:45.577783+00:00
updated: 2026-05-26T21:55:45.577783+00:00
ingestion_run: 8d527d59
---

# Best of N Strategy

## Summary

A performance improvement strategy where the model is prompted or configured to generate N multiple outputs (samples), and a subsequent mechanism (like a reward model or classifier) selects the optimal output from the set.

## Core Idea

This pattern leverages the model's ability to sample multiple outputs to mitigate the risk of poor single-shot generation, improving overall reliability and quality without requiring complex model retraining.

## Practical Use

Implement this when the single best answer is not guaranteed, such as in complex reasoning, code generation, or multi-step planning. The reward model acts as a quality filter on the generated candidates.

## Related

- Reward Model
- [[Stochastic-Sampling|Stochastic Sampling]]
