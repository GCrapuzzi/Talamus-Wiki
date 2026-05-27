---
type: framework
status: evergreen
aliases:
  - Evaluation-Driven Development (EDD)
  - Pre-deployment Evaluation Planning
  - Metrics-First AI Design
tags:
  - ai-engineering
  - MLOps
  - development-lifecycle
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/077-evaluation-criteria.md
    locator: pages 184-184
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - In AI engineering, evaluation-driven development means defining evaluation criteria before building.
      - Applications should demonstrate value to be deployed.
      - The most common enterprise applications in production are those with clear evaluation criteria.
created: 2026-05-26T21:55:45.791209+00:00
updated: 2026-05-26T21:55:45.791209+00:00
ingestion_run: 8d527d59
---

# Evaluation-Driven Development (EDD)

## Summary

A development methodology requiring the definition of clear, measurable evaluation criteria and success metrics before any AI model or application code is written or deployed.

## Core Idea

AI applications must demonstrate quantifiable value (ROI) to justify their existence. Deploying a system that cannot be reliably evaluated is worse than not deploying it at all, as it incurs maintenance costs without measurable benefit.

## Practical Use

Before starting model training, an AI engineer must conduct a discovery phase with stakeholders to define the primary success metric (e.g., 'increase purchase-through rate by 5%', 'reduce false negatives in fraud detection by 10%'). This metric dictates the model architecture, required data, and evaluation pipeline.

## Related

- A/B Testing
- ML Monitoring
- ROI Calculation
