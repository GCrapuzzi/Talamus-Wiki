---
type: method
status: evergreen
aliases:
  - Finetuning Data Format Standardization
  - Chat Template Adherence
  - Instruction Tuning Format
tags:
  - llm-ops
  - finetuning
  - data-formatting
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/154-format-data.md
    locator: pages 425-426
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Each model uses a specific tokenizer and expects data in a specific chat template
      - If you’re doing supervised finetuning, your data is most likely in the format (instruction, response)
      - For finetuning, all the examples included in the 3-shot prompt can be converted into training examples.
created: 2026-05-26T21:55:46.418837+00:00
updated: 2026-05-26T21:55:46.418837+00:00
ingestion_run: 8d527d59
---

# Finetuning Data Format Standardization

## Summary

The process of structuring cleaned data into the specific (Input, Output) pairs or chat templates required by the target LLM for effective finetuning.

## Core Idea

Models are highly sensitive to input format. Using the wrong chat template or data structure can cause significant performance degradation, even if the underlying data is correct.

## Practical Use

1. **Supervised Finetuning:** Format data as (instruction, response). Decompose instructions into (system prompt, user prompt). 2. **Conversion:** Convert multi-shot prompt examples (e.g., 'Item: burger
Label: edible') into structured training pairs (Input: 'burger', Output: 'edible'). 3. **Consistency:** Ensure the prompt used during inference exactly matches the format used during finetuning.

## Related

- [[Prompt-Engineering|Prompt Engineering]]
- Chat Templates
