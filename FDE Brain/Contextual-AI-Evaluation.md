---
type: framework
status: evergreen
aliases:
  - Contextual AI Evaluation
  - Application-Specific Evaluation
  - Purpose-Driven Testing
tags:
  - ai-engineering
  - evaluation
  - llm-deployment
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/076-chapter-4.-evaluate-ai-systems.md
    locator: pages 183-183
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - A model is only useful if it works for its intended purposes.
      - You need to evaluate models in the context of your application.
created: 2026-05-26T21:55:45.783708+00:00
updated: 2026-05-26T21:55:45.783708+00:00
ingestion_run: 8d527d59
---

# Contextual AI Evaluation

## Summary

Evaluating an AI model based on its performance against the specific requirements and use cases of the intended application, rather than relying solely on general benchmarks.

## Core Idea

A model's utility is defined by its performance in a specific operational context. General benchmarks (like MMLU) measure breadth, but contextual evaluation measures fitness for purpose, which is critical for deployment success.

## Practical Use

When integrating a foundational model, define a narrow set of 'golden path' use cases (e.g., 'summarize medical notes for billing') and create a custom test suite that measures success metrics (e.g., factual consistency, specific entity extraction) relevant only to that domain.

## Related

- Evaluation Pipeline
- [[Defining-Evaluation-Criteria|Defining Evaluation Criteria]]
