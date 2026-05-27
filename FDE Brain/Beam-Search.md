---
type: method
status: evergreen
aliases:
  - Beam Search
  - Fixed candidate generation
tags:
  - ai-engineering
  - generation-algorithms
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/051-test-time-compute.md
    locator: pages 120-122
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - For example, instead of generating all outputs independently, which might include many less promising candidates, you can use beam search to generate a fixed number of most promising candidates (the beam) at each step of sequence generation.
created: 2026-05-26T21:55:45.597326+00:00
updated: 2026-05-26T21:55:45.597326+00:00
ingestion_run: 8d527d59
---

# Beam Search

## Summary

A sequence generation algorithm that, instead of sampling the next token randomly, maintains a fixed number (the beam) of the most promising candidate sequences at each step, guiding the generation toward high-probability paths.

## Core Idea

Beam search provides a more strategic way to generate multiple outputs compared to independent random sampling, focusing computational effort on the most likely candidates and improving the quality of the generated sequence.

## Practical Use

Use beam search when high fidelity and coherence are paramount, such as in machine translation or summarization, where exploring only the top K paths is sufficient and computationally efficient.

## Related

- [[Test-Time-Compute-TTC|Test Time Compute (TTC)]]
