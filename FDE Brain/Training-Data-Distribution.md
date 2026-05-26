---
type: concept
tags: [training-data, data-quality, foundation-models, common-crawl]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#training-data
  - AI Space/normalized/pdf/ai-engineering.md#multilingual-models
  - AI Space/normalized/pdf/ai-engineering.md#domain-specific-models
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Training Data Distribution

A model's capabilities are bounded by its training data distribution. Most foundation models rely on Common Crawl (and its cleaned subset C4), despite known quality issues (misinformation, bias, low trustworthiness). The pragmatic reality: model developers use available data, not ideal data.

Key tension: training on more data requires more compute and doesn't always yield better performance. A model trained on smaller high-quality data can outperform one trained on larger low-quality data (e.g., Gunasekar et al. 2023: 1.3B params on 7B high-quality coding tokens beat much larger models).

Three golden goals for training data: **quantity**, **quality**, and **diversity**.

To address distribution gaps, practitioners can:
- Curate language-specific or domain-specific datasets
- Finetune general-purpose models on specialized data
- Train domain-specific models from scratch

See also: [[Low-Resource Languages in LLMs]], [[Domain-Specific Models]].
