---
type: operation
status: evergreen
aliases:
  - AI Application Evaluation Playbook
  - AI output validation
  - LLM system evaluation
tags:
  - ai-engineering
  - evaluation
  - llm-ops
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/005-what-this-book-is-about.md
    locator: pages 14-15
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - How do I evaluate my application? Can I use AI to evaluate AI outputs?
      - What causes hallucinations? How do I detect and mitigate hallucinations?
      - How do I create a feedback loop to improve my application continually?
created: 2026-05-26T21:55:45.255054+00:00
updated: 2026-05-26T21:55:45.255054+00:00
ingestion_run: 8d527d59
---

# AI Application Evaluation Playbook

## Summary

A checklist of critical questions and techniques required to evaluate the feasibility, performance, and reliability of an AI application before deployment.

## Core Idea

Evaluation must go beyond simple accuracy metrics. Key areas include mitigating hallucinations, assessing the need for complex components (agents), and validating data quality.

## Practical Use

Use this playbook during the design phase to structure evaluation tests. Specifically, address hallucination detection, determine the optimal RAG strategy, and validate the data quality required for finetuning.

## Related

- [[Hallucination-Mitigation-Strategies|Hallucination Mitigation Strategies]]
- [[Retrieval-Augmented-Generation-RAG|Retrieval Augmented Generation (RAG)]]
