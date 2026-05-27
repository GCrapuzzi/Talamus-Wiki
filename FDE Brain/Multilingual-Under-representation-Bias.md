---
type: concept
status: evergreen
aliases:
  - Multilingual Under-representation Bias
  - Language data imbalance
  - Common Crawl bias
tags:
  - multilingual-llm
  - data-bias
  - global-deployment
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/040-multilingual-models.md
    locator: pages 75-79
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - English accounts for almost half of the data (45.88%), making it eight times more prevalent than the second-most common language, Russian (5.97%)
      - Given the dominance of English in the internet data, it’s not surprising that general-purpose models work much better for English than other languages
created: 2026-05-26T21:55:45.515150+00:00
updated: 2026-05-26T21:55:45.515150+00:00
ingestion_run: 8d527d59
---

# Multilingual Under-representation Bias

## Summary

The systemic bias in LLM training data (e.g., Common Crawl) where high-resource languages (like English) are vastly overrepresented compared to the world's actual population distribution, leading to performance degradation in low-resource languages.

## Core Idea

Model performance is highly correlated with the availability and volume of training data. English dominance in the internet data leads to general-purpose models performing significantly better in English than in under-represented languages, regardless of the language's actual speaker population.

## Practical Use

When deploying an LLM globally, benchmark performance rigorously across all target languages. If performance gaps are observed, the primary mitigation strategy must be targeted data collection and fine-tuning for the under-represented languages.

## Related

- Low-Resource Language Modeling
- Data Bias Mitigation
