---
type: method
status: evergreen
aliases:
  - Chain-of-Thought (CoT) Data Generation
  - Step-by-Step Reasoning Data
  - CoT Prompting Data
tags:
  - data-curation
  - reasoning
  - llm-training
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/140-data-curation.md
    locator: pages 389-391
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - To teach a model to generate step-by-step responses, its training data should include CoT responses.
      - incorporating step-by-step responses in the finetuning data greatly enhances the performance of models of various sizes on CoT tasks
created: 2026-05-26T21:55:46.306858+00:00
updated: 2026-05-26T21:55:46.306858+00:00
ingestion_run: 8d527d59
---

# Chain-of-Thought (CoT) Data Generation

## Summary

Curating data where the desired response includes explicit, intermediate reasoning steps leading to the final answer, rather than just the final answer itself.

## Core Idea

Teaching step-by-step reasoning significantly enhances model performance on complex tasks, allowing the model to show its work and improve accuracy on multi-step problems.

## Practical Use

For tasks involving mathematical problem-solving, logical deduction, or complex planning, ensure the training dataset includes examples where the solution path is explicitly written out.

## Related

- [[Tool-Use-Data-Generation|Tool Use Data Generation]]
