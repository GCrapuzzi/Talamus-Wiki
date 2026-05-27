---
type: concept
status: evergreen
aliases:
  - Training Data Extraction (Memorization Attacks)
  - Data Leakage
  - Regurgitation Attack
tags:
  - ai-engineering
  - privacy
  - security
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/107-information-extraction.md
    locator: pages 267-271
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - The model can be prompted to divulge sensitive information without knowing the exact context.
      - The model can regurgitate copyrighted content if trained on it.
      - The larger the model, the more it memorizes, increasing vulnerability.
created: 2026-05-26T21:55:46.010460+00:00
updated: 2026-05-26T21:55:46.010460+00:00
ingestion_run: 8d527d59
---

# Training Data Extraction (Memorization Attacks)

## Summary

The vulnerability where an LLM outputs verbatim or near-verbatim text, PII, or copyrighted material that was present in its training dataset.

## Core Idea

LLMs are highly effective at encoding vast amounts of data, including private or copyrighted material. This memorization can be triggered by specific prompts (e.g., repeated tokens, targeted fill-in-the-blank prompts, or divergence attacks), making the model a potential source of data leakage.

## Practical Use

Implement robust output filtering and guardrails to detect and block responses that contain known sensitive patterns (PII, license text, copyrighted phrases). When training or fine-tuning, consider differential privacy techniques to minimize memorization.

## Related

- [[Factual-Probing|Factual Probing]]
- [[Defense-against-Data-Extraction|Defense against Data Extraction]]
