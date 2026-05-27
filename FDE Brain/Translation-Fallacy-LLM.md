---
type: warning
status: evergreen
aliases:
  - Translation Fallacy (LLM)
  - Translate-to-English-Back
  - Interlingual processing risk
tags:
  - multilingual-llm
  - deployment-risk
  - linguistics
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/040-multilingual-models.md
    locator: pages 75-79
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - translation can cause information loss. For example, some languages, like Vietnamese, have pronouns to denote the relationship between the two speakers. When translating into English, all these pronouns are translated into I and you, causing the loss of the relationship information.
created: 2026-05-26T21:55:45.516550+00:00
updated: 2026-05-26T21:55:45.516550+00:00
ingestion_run: 8d527d59
---

# Translation Fallacy (LLM)

## Summary

The flawed assumption that translating all input queries into a high-resource language (like English), obtaining a response, and translating it back is an effective or reliable method for multilingual LLM interaction.

## Core Idea

This approach is unreliable because it requires a model capable of understanding under-represented languages for translation, and critically, the translation process itself causes information loss (e.g., loss of relationship pronouns, cultural context).

## Practical Use

Avoid relying solely on translation pipelines for critical applications. Design the LLM to process and generate responses directly in the target language to preserve linguistic nuance and cultural context.

## Related

- [[Multilingual-Under-representation-Bias|Multilingual Under-representation Bias]]
- Direct Language Processing
