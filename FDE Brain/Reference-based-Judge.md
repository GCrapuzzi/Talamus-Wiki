---
type: concept
status: evergreen
aliases:
  - Reference-based Judge
  - Similarity Judge
  - Comparison Judge
tags:
  - ai-engineering
  - evaluation-methodology
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/071-what-models-can-act-as-judges.md
    locator: pages 169-171
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - A reference-based judge evaluates the generated response with respect to one or more reference responses.
      - For example, BLEURT ( Sellam et al., 2020 ) takes in a (candidate response, reference response) pair and outputs a similarity score...
created: 2026-05-26T21:55:45.747207+00:00
updated: 2026-05-26T21:55:45.747207+00:00
ingestion_run: 8d527d59
---

# Reference-based Judge

## Summary

A specialized judge that evaluates a generated response against one or more predefined reference responses, outputting a similarity or quality score.

## Core Idea

This method is useful when the desired output must adhere closely to established ground truth or canonical examples. The score measures the degree of overlap or quality relative to the reference.

## Practical Use

Use BLEURT-like models to calculate the similarity score between a candidate response and a gold-standard reference response, ensuring the generated text maintains semantic fidelity.

## Related

- Reward Model
- Reference Response
