---
type: concept
tags: [multilingual, low-resource-languages, tokenization, bias, foundation-models]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#multilingual-models
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Low-Resource Languages in LLMs

English dominates internet training data (~46% of Common Crawl), making it 8x more prevalent than the second-most common language (Russian, ~6%). Languages like Punjabi, Swahili, Urdu, and Bengali are severely under-represented (world-to-CC ratios of 36x–232x).

Consequences:
- **Quality gap**: GPT-4 performs significantly worse on MMLU in under-represented languages (Telugu, Marathi, Punjabi are worst)
- **Cost/latency gap**: Tokenization efficiency varies drastically. Burmese requires ~10x more tokens than English for the same content, meaning ~10x cost and latency
- **Safety gap**: ChatGPT was found more willing to produce misinformation in Chinese than English

The translate-to-English workaround is imperfect: requires the model to understand the source language, and translation causes information loss (e.g., Vietnamese relational pronouns collapse to "I" and "you").

Multiple language-specific models exist: ChatGLM (Chinese), CroissantLLM (French), PhoGPT (Vietnamese), Jais (Arabic).
