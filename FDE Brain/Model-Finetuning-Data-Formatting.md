---
type: method
status: evergreen
aliases:
  - Model Finetuning Data Formatting
  - Chat Template Structuring
  - Instruction Formatting
tags:
  - ai-engineering
  - llm-ops
  - data-formatting
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/153-clean-and-filter-data.md
    locator: pages 425-425
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Each model uses a specific tokenizer and expects data in a specific chat template.
      - If you’re doing supervised finetuning, your data is most likely in the format (instruction, response).
created: 2026-05-26T21:55:46.414280+00:00
updated: 2026-05-26T21:55:46.414280+00:00
ingestion_run: 8d527d59
---

# Model Finetuning Data Formatting

## Summary

The process of structuring cleaned data into the specific format (e.g., chat template, instruction/response pairs) required by a target LLM for successful finetuning.

## Core Idea

LLMs are highly sensitive to input structure. Using the wrong chat template or data format can cause functional bugs, even if the underlying data is correct.

## Practical Use

For supervised finetuning, structure data as (instruction, response). Decompose instructions into (system prompt, user prompt) if necessary. Always verify the required format against the target model's documentation and tokenizer requirements.

## Related

- Tokenizer
- [[Prompt-Engineering|Prompt Engineering]]
- Supervised Finetuning
