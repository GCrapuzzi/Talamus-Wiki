---
type: pattern
status: evergreen
aliases:
  - Model Licensing Due Diligence Checklist
  - AI Model Legal Review
  - License Compliance Audit
tags:
  - ai-engineering
  - legal
  - compliance
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/084-model-build-versus-buy.md
    locator: pages 205-214
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Does the license allow commercial use?
      - If it allows commercial use, are there any restrictions?
      - Does the license allow using the model’s outputs to train or improve upon other models?
created: 2026-05-26T21:55:45.839837+00:00
updated: 2026-05-26T21:55:45.839837+00:00
ingestion_run: 8d527d59
---

# Model Licensing Due Diligence Checklist

## Summary

A mandatory checklist for evaluating the legal and commercial viability of any foundation model license.

## Core Idea

A model's license dictates its usage rights, which can be more restrictive than the model's technical capabilities. Compliance must be checked before deployment.

## Practical Use

Before integrating a model, run it through this checklist: 1. **Commercial Use:** Is it allowed? (Crucial for revenue-generating products). 2. **Restrictions:** Are there usage caps (e.g., user count, geographic limits)? 3. **Data Lineage/Output Use:** Does the license permit using the model's outputs (synthetic data) for further training or improvement (e.g., model distillation)?

## Related

- Data Lineage Tracking
