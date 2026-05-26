---
type: operation
tags: [data-processing, data-pipeline, deduplication, data-cleaning]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#inspect-data
  - AI Space/normalized/pdf/ai-engineering.md#deduplicate-data
  - AI Space/normalized/pdf/ai-engineering.md#clean-and-filter-data
  - AI Space/normalized/pdf/ai-engineering.md#format-data
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Training Data Processing Pipeline

Ordered steps for preparing finetuning data, though execution order should optimize for time/compute:

### 1. Inspect Data
- Plot distributions: token frequency, input/output lengths, topics, languages
- Analyze by source, annotator, time — detect scoring biases, length biases, outliers
- Compute inter-annotator disagreement and resolve conflicts
- **Manual inspection is irreplaceable** — 15 minutes of staring at data saves hours of debugging
- Use (verb, direct-object, noun) pair distributions to compare data sources or model generations

### 2. Deduplicate
- Types: whole-document, intra-document, cross-document
- Methods: pairwise similarity (exact/n-gram/fuzzy/semantic), hashing (MinHash, Bloom filter), dimensionality reduction
- Impact: repeating 0.1% of data 100× degraded an 800M model to 400M-equivalent performance (Anthropic)

### 3. Clean and Filter
- Remove extraneous formatting (HTML/Markdown) — Databricks saw 20% accuracy gain and 60% token reduction
- Strip non-compliant data: PII, toxic content, copyrighted material
- Remove low-quality examples via AI scoring and heuristics
- Consider Active Learning or importance sampling to select highest-value examples

### 4. Format
- Match the target model's tokenizer and chat template exactly
- SFT format: (system prompt, user prompt) → response
- Finetuning prompts are typically shorter than few-shot prompts (no examples or task descriptions needed)
- Format mismatches cause subtle, hard-to-debug model failures

**Tips:** Order steps to minimize total compute; always do trial runs; never modify data in place—keep originals.
