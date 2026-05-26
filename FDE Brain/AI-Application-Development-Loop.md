---
type: framework
tags: [ai-engineering, development-process, framework, production]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#navigating-this-book
  - AI Space/normalized/pdf/ai-engineering.md#what-this-book-is-about
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# AI Application Development Loop

End-to-end process for adapting foundation models to real-world problems. The loop progresses through ordered concerns:

1. **Feasibility** — Is AI needed? Should I build or buy? (use-case evaluation)
2. **Model understanding** — How the foundation model works under the hood: training data, architecture, alignment, generation settings
3. **Evaluation** — Hardest challenge; requires reliable, systematic pipelines (domain-specific metrics, AI-as-judge, human eval)
4. **Instruction optimization** — Prompt Engineering: crafting instructions, defending against prompt attacks
5. **Context optimization** — RAG and agentic patterns for context construction
6. **Model adaptation** — Finetuning and model merging when prompting/context aren't enough
7. **Data engineering** — Acquisition, annotation, synthesis, quality validation
8. **Inference optimization** — Latency and cost reduction at model and serving level
9. **Production feedback** — User feedback systems for continuous improvement

Each stage feeds back into evaluation. The framework is modular—enter at whichever stage matches your current bottleneck.
