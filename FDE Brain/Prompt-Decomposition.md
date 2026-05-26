---
type: pattern
tags: [prompt-engineering, prompt-chaining, system-design, latency, cost-optimization]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#break-complex-tasks-into-simpler-subtasks
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Prompt Decomposition

Break complex tasks into a chain of simpler subtasks, each with its own focused prompt. The outputs of earlier steps feed into later ones.

### Example: Customer support chatbot
1. **Intent classification prompt** → identifies category (Billing, Technical Support, etc.)
2. **Response prompt** (one per intent) → generates the appropriate reply

### Benefits
- **Monitoring** — inspect intermediate outputs, not just the final result.
- **Debugging** — isolate and fix the failing step independently.
- **Parallelization** — run independent branches concurrently (e.g., generate 3 reading-level variants simultaneously).
- **Cost optimization** — use cheaper models for simpler steps (e.g., weak model for classification, strong model for generation).
- **Easier authoring** — simple prompts are easier to write and maintain.

### Trade-offs
- **Latency** — more sequential steps = longer time-to-first-token for the final output.
- **Cost** — more API calls, though decomposed prompts are individually shorter. GoDaddy found decomposition actually *reduced* total token cost while improving quality (from a 1,500-token monolith).

Granularity is empirical — experiment to find the optimal decomposition for your performance/cost/latency budget.
