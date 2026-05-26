---
type: framework
tags: [data-quality, finetuning, annotation]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#data-quality
  - AI Space/normalized/pdf/ai-engineering.md#data-curation
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Data Quality Criteria for Finetuning

Six characteristics define high-quality finetuning data:

1. **Relevant** — examples match the target task's domain and era
2. **Aligned with task requirements** — annotations reflect what the task actually demands (factual consistency, creativity, conciseness, etc.)
3. **Consistent** — inter-annotator agreement is high; same-quality examples receive same scores
4. **Correctly formatted** — no extraneous tokens (HTML tags, trailing whitespace, inconsistent casing, wrong numeric types)
5. **Sufficiently unique** — duplicates are controlled to avoid bias and contamination
6. **Compliant** — meets internal policies, laws, and regulations (e.g., no PII if prohibited)

A small amount of high-quality data can outperform large noisy datasets. The Yi model family showed 10K carefully crafted instructions beat hundreds of thousands of noisy ones. LIMA demonstrated 1,000 curated examples made a 65B model competitive with GPT-4 in 43% of cases.

Good annotation guidelines are essential for achieving both alignment and consistency.
