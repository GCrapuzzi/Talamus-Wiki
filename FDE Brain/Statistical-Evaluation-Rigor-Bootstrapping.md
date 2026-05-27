---
type: method
status: evergreen
aliases:
  - Statistical Evaluation Rigor (Bootstrapping)
  - sample size calculation
  - variance testing
tags:
  - ai-engineering
  - statistics
  - evaluation
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/089-step-3.-define-evaluation-methods-and-data.md
    locator: pages 228-231
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - To know whether 100 is sufficient for the result to be reliable, you can create multiple bootstraps of these 100 examples and see if they give similar evaluation results.
      - If the evaluation results vary wildly for different bootstraps, this means that you’ll need a bigger evaluation set.
created: 2026-05-26T21:55:45.880336+00:00
updated: 2026-05-26T21:55:45.880336+00:00
ingestion_run: 8d527d59
---

# Statistical Evaluation Rigor (Bootstrapping)

## Summary

Using statistical techniques like bootstrapping and sample size estimation to determine if observed performance differences between models or prompts are statistically significant, rather than due to random chance.

## Core Idea

Evaluation results must be reliable. Bootstrapping involves repeatedly sampling with replacement from the original evaluation set to measure the variance of the performance score. This determines if the evaluation pipeline is trustworthy.

## Practical Use

If a new prompt claims a 10% improvement, calculate the required sample size using established rules (e.g., the 3x rule of thumb) and run multiple bootstraps (e.g., 100 times) to confirm that the score difference is consistent and not highly variable.

## Related

- Hypothesis Testing
- [[Evaluation-Set-Design-Principles|Evaluation Set Design Principles]]
