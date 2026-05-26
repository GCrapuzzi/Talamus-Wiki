---
type: concept
tags: [ai-engineering, ml-engineering, foundations]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#preface
  - AI Space/normalized/pdf/ai-engineering.md#what-this-book-is-about
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# AI Engineering vs ML Engineering

Traditional ML engineering and AI engineering (foundation-model engineering) differ in their primary levers:

| Dimension | Traditional ML | AI Engineering |
|---|---|---|
| Data work | Tabular annotations, feature engineering | Prompt engineering, context construction |
| Model adaptation | Full model training | Parameter-efficient finetuning |
| Core loop | Train → evaluate → retrain | Prompt → evaluate → refine context/finetune |

Both share fundamentals: systematic experimentation, rigorous evaluation, relentless optimization for speed and cost. Real-world systems often combine both traditional ML models and foundation models, so practitioners benefit from fluency in both paradigms.

See also: Prompt Engineering, RAG, [[Parameter-Efficient Finetuning]].
