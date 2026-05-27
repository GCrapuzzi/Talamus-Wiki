---
type: method
status: evergreen
aliases:
  - Rule-based Data Synthesis
  - Template-based Data Generation
  - Synthetic Data Generation via Templates
tags:
  - data-synthesis
  - structured-data
  - data-privacy
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/147-traditional-data-synthesis-techniques.md
    locator: pages 407-409
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - To create a credit card transaction, start with a transaction template and use a random generator like Faker to populate each field in this template.
created: 2026-05-26T21:55:46.367803+00:00
updated: 2026-05-26T21:55:46.367803+00:00
ingestion_run: 8d527d59
---

# Rule-based Data Synthesis

## Summary

Generating synthetic data by defining structured templates and populating the fields using predefined rules, random generators (e.g., Faker), or constrained distributions.

## Core Idea

This method is highly effective for structured data (e.g., financial records, invoices, medical forms) where the data must adhere to a specific schema, format, or grammar (like regex or specific date formats).

## Practical Use

Creating synthetic transaction data for fraud detection model training, generating mock configuration files, or creating structured documents (resumes, contracts) to test data pipeline robustness without using sensitive PII.

## Related

- Data Schema Definition
- Data Masking
