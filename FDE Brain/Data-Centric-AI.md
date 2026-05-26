---
type: concept
tags: [dataset-engineering, data-centric-ai, training-data]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#chapter-8-dataset-engineering
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Data-Centric AI

A paradigm that improves AI performance by enhancing data rather than models, contrasting with **model-centric AI** which focuses on architectures, scale, and training techniques.

Data-centric benchmarks flip the traditional setup: given a fixed model, participants compete to build the best dataset. Examples include DataComp (CLIP training datasets evaluated on 38 downstream tasks), DataPerf, and dcbench.

Andrew Ng's 2021 data-centric competition asked participants to improve a base dataset via label fixing, edge-case addition, and augmentation—keeping the model constant.

In practice, meaningful progress requires investment in both model and data improvements. The division is a useful research lens, not a strict either/or.
