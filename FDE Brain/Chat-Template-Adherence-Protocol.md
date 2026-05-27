---
type: operational
status: evergreen
aliases:
  - Chat Template Adherence Protocol
  - Model API Formatting
  - Prompt Tokenization Safety
tags:
  - ai-engineering
  - deployment
  - llm-ops
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/094-system-prompt-and-user-prompt.md
    locator: pages 239-241
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - The model combines them into a single prompt, typically following a template.
      - Accidentally using the wrong template can lead to bewildering performance issues.
      - When constructing inputs for a foundation model, make sure that your inputs follow the model’s chat template exactly.
created: 2026-05-26T21:55:45.914426+00:00
updated: 2026-05-26T21:55:45.914426+00:00
ingestion_run: 8d527d59
---

# Chat Template Adherence Protocol

## Summary

Strict adherence to the model provider's defined chat template (e.g., Llama 2's <s>[INST] <<SYS>>...[/INST] or Llama 3's <|begin_of_text|>...) is critical for stable and predictable model performance.

## Core Idea

LLMs process input based on specific token sequences defined by the model developers. Deviations, even minor ones (like extra newlines or incorrect tokens), can cause the model to misinterpret the input structure, leading to significant performance degradation or silent failures.

## Practical Use

Always use the model provider's recommended API wrapper or library function to construct prompts, rather than manually concatenating tokens. Before deployment, implement a validation step that prints and verifies the final prompt structure against the model's documented template.

## Related

- [[System-Prompt-vs.-User-Prompt-Architecture|System Prompt vs. User Prompt Architecture]]
