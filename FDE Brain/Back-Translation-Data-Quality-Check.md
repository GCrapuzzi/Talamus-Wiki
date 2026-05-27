---
type: method
status: evergreen
aliases:
  - Back-Translation (Data Quality Check)
  - Cross-lingual Verification
  - Round-trip Translation
tags:
  - ai-engineering
  - nlp
  - data-quality
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/148-ai-powered-data-synthesis.md
    locator: pages 410-418
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - You can use another model to translate the translation back into the original language, Xʹ, then compare Xʹ with the original sentence X. If they are very different, the translation Y is likely bad.
created: 2026-05-26T21:55:46.378847+00:00
updated: 2026-05-26T21:55:46.378847+00:00
ingestion_run: 8d527d59
---

# Back-Translation (Data Quality Check)

## Summary

A technique used to verify the quality of a translation (e.g., X -> Y) by translating the target language (Y) back into the source language (X') and comparing X' to the original X.

## Core Idea

If the back-translated text (X') significantly deviates from the original text (X), the initial translation (Y) is likely inaccurate or poor quality. This is crucial for building reliable multilingual datasets.

## Practical Use

When translating data from a high-resource language (English) to a low-resource language (Quechua), perform back-translation checks. If the fidelity is low, the translation must be manually reviewed or the source/target pair discarded.

## Related

- Low-Resource Language Modeling
- AI-Powered Data Synthesis
