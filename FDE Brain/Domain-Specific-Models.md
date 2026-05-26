---
type: concept
tags: [domain-specific, foundation-models, specialization, transfer-learning]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#domain-specific-models
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Domain-Specific Models

General-purpose models trained on internet data excel at tasks present in that data but struggle with specialized domains whose data is rare online (e.g., protein structures, medical imaging, factory layouts).

Examples of domain-specific models:
- **AlphaFold** (DeepMind): trained on ~100K known protein sequences and 3D structures
- **BioNeMo** (NVIDIA): biomolecular data for drug discovery
- **Med-PaLM2** (Google): LLM + medical data for clinical queries

Domain-specific models can be trained from scratch or finetuned on top of general-purpose models. The choice depends on data availability and compute budget.

A model's domain coverage can be inferred from its benchmark performance across categories. Vision models especially lack transparent domain distribution analysis compared to text models.
