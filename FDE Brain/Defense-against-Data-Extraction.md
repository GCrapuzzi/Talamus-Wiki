---
type: method
status: evergreen
aliases:
  - Defense against Data Extraction
  - Guardrails Implementation
  - Output Filtering
tags:
  - ai-engineering
  - security
  - deployment
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/107-information-extraction.md
    locator: pages 267-271
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - The risk of PII data extraction can be mitigated by placing filters to block requests that ask for PII data and responses that contain PII data.
      - Some models block suspicious fill-in-the-blank requests.
created: 2026-05-26T21:55:46.013775+00:00
updated: 2026-05-26T21:55:46.013775+00:00
ingestion_run: 8d527d59
---

# Defense against Data Extraction

## Summary

A multi-layered defense strategy involving input validation, output filtering, and model-level constraints to prevent the leakage of PII, copyrighted material, or proprietary training data.

## Core Idea

Mitigation requires both external controls (filters blocking suspicious requests/responses) and internal model design (e.g., training on privacy-preserving data). The goal is to prevent the model from fulfilling requests that ask for sensitive information.

## Practical Use

Implement a pipeline that includes: 1) Input validation (blocking PII requests); 2) Core LLM call; 3) Output validation (blocking responses containing PII or known sensitive patterns). This is critical for production systems handling user data.

## Related

- [[Active-Injection-Attacks|Active Injection Attacks]]
- Privacy-Preserving Training
