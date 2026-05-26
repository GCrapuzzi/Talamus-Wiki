---
type: method
tags: [evaluation, metrics, BLEU, ROUGE, nlp]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#similarity-measurements-against-reference-data
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Lexical Similarity

Measures how much two texts overlap at the token or n-gram level. Reference-based: requires curated ground-truth responses.

**Techniques:**
- **Exact match**: Binary—does the output match a reference exactly? Works only for short, unambiguous answers. Substring-contains variant accepts any output containing the reference, but can false-positive (e.g., "September 12, 1929" contains "1929" but is factually wrong).
- **Fuzzy matching** (approximate string matching): Counts edit distance (insertion, deletion, substitution, optionally transposition) between two strings.
- **N-gram similarity**: Measures overlap of token sequences. Metrics: BLEU, ROUGE, METEOR++, TER, CIDEr—differ in how overlap is calculated.

**Drawbacks:**
- Requires comprehensive reference sets; correct answers missing from references get penalized (Adept's Fuyu example).
- References can themselves be wrong (WMT 2023 found many bad reference translations).
- Higher lexical similarity ≠ better quality. On HumanEval, BLEU scores for correct and incorrect code solutions were similar.

Since foundation models, fewer benchmarks rely on lexical similarity. Still used in WMT, COCO Captions, GEMv2.
