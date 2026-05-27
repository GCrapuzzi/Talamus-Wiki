---
type: glossary
status: evergreen
aliases:
  - Demonstration Data
  - Prompt-Response Pairs
  - Instruction Examples
tags:
  - data-curation
  - llm-data
  - prompt-engineering
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/046-supervised-finetuning.md
    locator: pages 104-106
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - To encourage a model to generate the appropriate responses, you can show examples of appropriate responses. Such examples follow the format (prompt, response) and are called demonstration data.
      - Since different types of requests require different types of responses, your demonstration data should contain the range of requests you want your model to handle.
created: 2026-05-26T21:55:45.555165+00:00
updated: 2026-05-26T21:55:45.555165+00:00
ingestion_run: 8d527d59
---

# Demonstration Data

## Summary

A curated dataset consisting of high-quality (prompt, response) pairs used to fine-tune an LLM. These pairs explicitly demonstrate the desired input-output behavior for specific tasks.

## Core Idea

The model learns by mimicking the provided examples. The quality and diversity of this data are paramount, as the model will attempt to replicate the patterns, judgment, and structure found in the dataset.

## Practical Use

When designing a dataset, the engineer must ensure the data is not only accurate but also covers the full range of required tasks (e.g., question answering, summarization, translation) to prevent the model from failing on novel inputs.

## Related

- [[Supervised-Finetuning-SFT|Supervised Finetuning (SFT)]]
- [[Behavior-Cloning|Behavior Cloning]]
