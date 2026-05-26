---
type: concept
tags: [ai-engineering, ml-engineering, model-adaptation, discipline]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#from-foundation-models-to-ai-engineering
  - AI Space/normalized/pdf/ai-engineering.md#ai-engineering-versus-ml-engineering
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# AI Engineering

The discipline of building applications on top of existing foundation models, as opposed to training models from scratch (traditional ML Engineering).

Three factors driving its rapid growth:

1. **General-purpose AI capabilities** — foundation models handle tasks previously impossible, vastly expanding the application space.
2. **Increased AI investment** — AI cost per use case dropped ~100× between April 2022 and April 2023 (per Scribd). Global AI investment projected at $200B by 2025.
3. **Low entrance barrier** — model-as-a-service APIs give access to powerful models via single calls. AI can also write code, enabling non-engineers to build applications.

**How it differs from ML engineering:**

| Dimension | Traditional ML | AI Engineering |
|---|---|---|
| Model source | Train your own | Adapt someone else's |
| Compute pressure | Moderate | Higher (bigger models) |
| Output type | Close-ended | Open-ended |
| Key challenge | Model development | Model adaptation + evaluation |

Adaptation techniques split into **prompt-based** (no weight updates — easier, less data) and **finetuning** (weight updates — harder, more powerful). The workflow inverts: ML engineering goes Data → Model → Product; AI engineering goes Product → Data → Model.
