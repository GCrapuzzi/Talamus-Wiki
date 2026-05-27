---
type: method
status: evergreen
aliases:
  - Reference Comparison Prompting
  - Ground Truth Matching
  - Similarity Check
tags:
  - ai-engineering
  - evaluation
  - rag
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/069-how-to-use-ai-as-a-judge.md
    locator: pages 162-164
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Compare a generated response to a reference response to evaluate whether the generated response is the same as the reference response.
created: 2026-05-26T21:55:45.721368+00:00
updated: 2026-05-26T21:55:45.721368+00:00
ingestion_run: 8d527d59
---

# Reference Comparison Prompting

## Summary

Using an AI judge to compare a generated response against a known reference answer (ground truth) to determine if the generated answer is equivalent or sufficiently similar.

## Core Idea

This is an alternative to traditional, human-designed similarity metrics (like BLEU scores) and is essential for evaluating factual accuracy and adherence to provided knowledge.

## Practical Use

When validating RAG outputs or fact-checking, the prompt must provide the question, the reference answer, and the generated answer, asking for a binary (True/False) or similarity score.

## Related

- [[AI-Judge-Prompting-Framework|AI Judge Prompting Framework]]
