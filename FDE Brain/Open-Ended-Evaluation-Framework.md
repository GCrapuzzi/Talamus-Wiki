---
type: framework
status: evergreen
aliases:
  - Open-Ended Evaluation Framework
  - Generative Model Validation
  - Non-Ground-Truth Evaluation
tags:
  - ai-engineering
  - llm-evaluation
  - generative-ai
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/056-challenges-of-evaluating-foundation-models.md
    locator: pages 138-141
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - For an open-ended task, for a given input, there are so many possible correct responses. It’s impossible to curate a comprehensive list of correct outputs to compare against.
      - To validate the quality of a summary, you might need to read the book first.
created: 2026-05-26T21:55:45.638715+00:00
updated: 2026-05-26T21:55:45.638715+00:00
ingestion_run: 8d527d59
---

# Open-Ended Evaluation Framework

## Summary

A framework designed for Foundation Models (FMs) where the output space is vast and non-deterministic, requiring evaluation methods that go beyond simple comparison to a single 'ground truth' answer.

## Core Idea

Traditional ML evaluation relies on closed-ended tasks (e.g., classification: X or Y). FMs are open-ended, meaning there are countless correct responses. Evaluation must therefore focus on criteria like coherence, reasoning depth, factuality, and adherence to constraints, rather than just matching a single expected output.

## Practical Use

For open-ended tasks (e.g., summarization, creative writing), structure the evaluation around multiple dimensions: 1) Factuality/Hallucination Rate, 2) Coherence/Fluency, 3) Completeness (did it address all parts of the prompt?), and 4) Domain Specificity. Use structured prompts for evaluation rather than free-form human review.

## Related

- [[Systematic-Evaluation-Methodology|Systematic Evaluation Methodology]]
- Factuality Checking
- Domain Expertise Integration
