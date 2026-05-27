---
type: framework
status: evergreen
aliases:
  - Usefulness Threshold Definition
  - Success Metrics Definition
  - Product Readiness Criteria
tags:
  - ai-engineering
  - metrics
  - product-management
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/031-milestone-planning.md
    locator: pages 57-57
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - "Usefulness thresholds might include the following metrics groups: Quality metrics... Latency metrics... Cost metrics... Other metrics such as interpretability and fairness."
created: 2026-05-26T21:55:45.456365+00:00
updated: 2026-05-26T21:55:45.456365+00:00
ingestion_run: 8d527d59
---

# Usefulness Threshold Definition

## Summary

A structured approach to defining measurable, non-negotiable criteria (metrics) that a deployed AI product must meet to be considered useful and ready for customer interaction.

## Core Idea

Defining usefulness thresholds upfront prevents premature deployment and ensures that the product's minimum viable quality is established. Failure to define these metrics leads to subjective success criteria.

## Practical Use

Before starting development, define specific, measurable targets for: 1) Quality (e.g., F1 score, accuracy); 2) Latency (e.g., TTFT < 1s, TPOT < 0.1s); 3) Cost (e.g., < $0.001 per inference); 4) Ethical concerns (Interpretability, Fairness).

## Related

- [[AI-Product-Milestone-Planning|AI Product Milestone Planning]]
- Operational Playbook: Metric Tracking
