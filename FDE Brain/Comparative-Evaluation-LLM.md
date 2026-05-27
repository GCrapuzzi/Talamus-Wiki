---
type: framework
status: evergreen
aliases:
  - Comparative Evaluation (LLM)
  - Pairwise Comparison
  - A/B Testing (LLM)
tags:
  - ai-engineering
  - evaluation
  - llm-deployment
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/074-the-future-of-comparative-evaluation.md
    locator: pages 179-179
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Comparative evaluation is easier than giving concrete scores to outputs.
      - Comparative evaluation captures human preference.
      - Comparative evaluation is robust against saturation.
      - Comparative evaluation is insufficient without considering cost and operational context.
created: 2026-05-26T21:55:45.773014+00:00
updated: 2026-05-26T21:55:45.773014+00:00
ingestion_run: 8d527d59
---

# Comparative Evaluation (LLM)

## Summary

A methodology where model performance is assessed by pitting two models (A vs. B) against each other to determine relative superiority, rather than assigning absolute scores or relying on fixed benchmarks.

## Core Idea

Comparative evaluation is valuable because it captures human preference and is robust against saturation (unlike benchmarks that hit perfect scores). However, it is insufficient on its own, as the win rate (e.g., 51% win rate) does not automatically translate into actionable business metrics (e.g., resolved tickets) without integrating cost, utility, and specific operational context.

## Practical Use

When deciding between two models (A and B), do not rely solely on the win rate. Implement a multi-factor decision framework that includes: 1) Comparative performance (A vs. B), 2) Operational Cost (Cost_B / Cost_A), and 3) Expected Utility/Impact (How a 1% performance boost translates to real-world value). Use comparative evaluation primarily as a signal for human preference, not as the final decision metric.

## Related

- Cost-Benefit Analysis (AI)
- Human Preference Scoring
- Operational Utility Modeling
