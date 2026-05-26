---
type: method
tags: [data-verification, synthetic-data, data-quality]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#ai-powered-data-synthesis
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Synthetic Data Verification

Techniques to ensure AI-generated training data meets quality standards:

**Functional correctness** — execute generated code, run unit tests, validate outputs. Coding data is popular for synthesis partly because it's verifiable.

**AI judges** — score examples 1–5, classify as good/bad, or check against stated quality requirements. Use AI-as-Judge techniques with position-bias mitigation (e.g., NVIDIA swapped response order and kept only consistent judgments).

**Factual consistency detection** — filter hallucinated examples using techniques from evaluation (Chapter 4).

**Back-translation** — translate output back to input domain; discard if the round-trip diverges.

**Topic detection + anomaly detection** — classify example topics and remove off-topic or outlier examples.

**Heuristic filters** (from Self-Instruct):
- Remove repetitive examples
- Filter too-long or too-short instructions
- Discard same-instruction-different-response pairs
- Remove output-repeats-input examples

The ultimate quality test remains real-world performance: does the synthetic data actually improve the model?
