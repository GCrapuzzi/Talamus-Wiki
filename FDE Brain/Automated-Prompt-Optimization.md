---
type: concept
tags: [prompt-engineering, automation, DSPy, prompt-optimization, tooling]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#evaluate-prompt-engineering-tools
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Automated Prompt Optimization

Tools that search the space of possible prompts to find ones maximizing evaluation metrics, analogous to AutoML for hyperparameters.

### End-to-end tools
- **DSPy** (Khattab et al., 2023) — specify I/O formats, metrics, and eval data; the tool finds optimal prompt chains.
- **OpenPrompt** (Ding et al., 2021) — similar declarative optimization.

### AI-powered approaches
- **Promptbreeder** (DeepMind, Fernando et al., 2023) — evolutionary strategy that "breeds" prompts via mutation, guided by mutator prompts. Iteratively selects and re-mutates the most promising variants.
- **TextGrad** (Stanford, Yüksekgönül et al., 2024) — gradient-inspired prompt optimization.
- Simple approach: ask a model to write, critique, and improve prompts directly.

### Structured output tools
Guidance, Outlines, Instructor — constrain model outputs to valid schemas.

### Caveats
- **Hidden API costs** — 10 prompt variants × 30 eval examples × 3 calls/prompt = 900 API calls.
- **Tool bugs** — wrong chat templates, typos in default prompts (e.g., LangChain critique prompt typos), silent template changes between versions.
- **Start simple** — write your own prompts first to understand the model and requirements. If using tools, always inspect generated prompts and track API call volume.
