---
type: glossary
status: evergreen
aliases:
  - Open Model Taxonomy
  - Open Source Model Definition
  - Open Data Model
tags:
  - ai-engineering
  - glossary
  - open-source
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/084-model-build-versus-buy.md
    locator: pages 205-214
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - To signal whether the data is also open, the term 'open weight' is used for models that don’t come with open data, whereas the term 'open model' is used for models that come with open data.
      - Open data allows more flexible model usage, such as retraining the model from scratch...
created: 2026-05-26T21:55:45.838503+00:00
updated: 2026-05-26T21:55:45.838503+00:00
ingestion_run: 8d527d59
---

# Open Model Taxonomy

## Summary

A classification system for open models based on the availability of weights and training data.

## Core Idea

The term 'open source' is ambiguous. Engineers must distinguish between three states to understand true flexibility and auditability.

## Practical Use

When evaluating a model, confirm its status: 1. **Open Model:** Weights + Training Data (Highest transparency, best for auditing). 2. **Open Weight Model:** Weights only (Most common, good for customization). 3. **Closed/API Model:** Weights/Data proprietary (Requires trust in the vendor).

## Related

- Model Licensing Due Diligence
