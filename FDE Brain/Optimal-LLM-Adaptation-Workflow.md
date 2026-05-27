---
type: pattern
status: evergreen
aliases:
  - Optimal LLM Adaptation Workflow
  - AI Model Improvement Workflow
  - LLM Iterative Development
tags:
  - ai-engineering
  - llm-deployment
  - workflow
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/128-finetuning-and-rag.md
    locator: pages 340-342
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Note that before any of the adaptation steps, you should define your evaluation criteria and design your evaluation pipeline.
      - If your model has both information and behavior issues, start with RAG.
      - RAG and finetuning aren’t mutually exclusive. They can sometimes be used together to maximize your application’s performance.
created: 2026-05-26T21:55:46.204322+00:00
updated: 2026-05-26T21:55:46.204322+00:00
ingestion_run: 8d527d59
---

# Optimal LLM Adaptation Workflow

## Summary

A recommended, iterative process for improving model performance, prioritizing external knowledge injection before deep model modification.

## Core Idea

Always define evaluation criteria and build an evaluation pipeline first. When adapting a model, start with the least invasive and most effective method (RAG) before moving to more complex or costly methods (Finetuning).

## Practical Use

1. Define Evaluation Criteria. 2. Start with Prompt Engineering. 3. If information is missing, implement RAG (starting with BM25). 4. If format/style is wrong, consider Finetuning. 5. If both are needed, combine RAG and Finetuning.

## Related

- [[Evaluation-Pipeline-Design|Evaluation Pipeline Design]]
- [[Retrieval-Augmented-Generation-RAG|Retrieval-Augmented Generation (RAG)]]
