---
type: method
status: evergreen
aliases:
  - Perplexity Calculation and Units
  - PPL Formula
  - Cross-Entropy to Perplexity
tags:
  - ai-engineering
  - math-modeling
  - llm-evaluation
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/062-perplexity-interpretation-and-use-cases.md
    locator: pages 146-148
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - PPL (P, Q) = 2H (P ,Q)
      - "If you use nat as the unit, perplexity is the exponential of e: PPL (P, Q) = e H (P ,Q)"
created: 2026-05-26T21:55:45.672281+00:00
updated: 2026-05-26T21:55:45.672281+00:00
ingestion_run: 8d527d59
---

# Perplexity Calculation and Units

## Summary

Perplexity is mathematically related to cross-entropy (H). The specific formula depends on the base used for entropy calculation (base 2 for bits, base e for natural log).

## Core Idea

PPL is calculated as the exponential of the cross-entropy (PPL = e^(H)). While bit-based calculations use base 2, most ML frameworks (TensorFlow, PyTorch) use natural log (base e), making the exponential function necessary for the final PPL value.

## Practical Use

When comparing PPL values reported by different frameworks or researchers, confirm the underlying base (e or 2) used for the cross-entropy calculation to ensure apples-to-apples comparisons. Always be aware of the unit (bits vs. nat).

## Related

- Cross-Entropy
- Entropy
