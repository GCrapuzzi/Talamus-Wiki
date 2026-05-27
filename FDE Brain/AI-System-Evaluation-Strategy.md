---
type: method
status: evergreen
aliases:
  - AI System Evaluation Strategy
  - Post-Deployment Validation
  - Impact Differentiation Testing
tags:
  - ai-engineering
  - experimentation
  - MLOps
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/077-evaluation-criteria.md
    locator: pages 184-184
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - It’s important to do A/B testing to differentiate impact.
      - Recommendations can increase purchases, but increased purchases are not always because of good recommendations. Other factors, such as promotional campaigns and new product launches, can also increase purchases.
created: 2026-05-26T21:55:45.793156+00:00
updated: 2026-05-26T21:55:45.793156+00:00
ingestion_run: 8d527d59
---

# AI System Evaluation Strategy

## Summary

A structured approach to determining the true causal impact of an AI system, ensuring that observed changes in business metrics are attributable to the model itself, rather than external factors.

## Core Idea

Correlation (increased purchases) does not equal causation (good recommendations). To prove value, the system's impact must be isolated from confounding variables like promotional campaigns or new product launches.

## Practical Use

When deploying a recommender system, do not simply measure overall sales lift. Implement A/B testing where the control group receives standard recommendations and the test group receives the AI-driven recommendations, allowing for direct comparison of the incremental lift.

## Related

- A/B Testing
- Causal Inference
- [[Evaluation-Driven-Development-EDD|Evaluation-Driven Development (EDD)]]
