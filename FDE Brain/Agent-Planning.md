---
type: framework
tags: [planning, agents, task-decomposition, human-in-the-loop]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#planning
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Agent Planning

Planning is the core capability of an AI agent. A plan is a roadmap of steps to accomplish a task (defined by goal + constraints).

### Core process
1. **Plan generation** (task decomposition): decompose task into manageable actions
2. **Reflection & error correction**: evaluate the plan; regenerate if bad
3. **Execution**: perform actions, often via [[Function Calling]]
4. **Reflection & error correction**: evaluate outcomes, determine if goal met, correct mistakes

### Decouple planning from execution
Generate plan → validate (heuristics or AI judges) → execute only if valid. Avoids wasting time/money on fruitless 1000-step plans.

### Planning granularity trade-off
- **Detailed plans** (exact function names): harder to generate, easier to execute, brittle to API changes
- **High-level plans** (natural language): easier to generate, need a translator to convert to executable commands, more robust to tool changes
- **Hierarchical planning**: generate high-level plan first, then detail each step

### Human-in-the-loop
Humans can provide plans, validate plans, or execute risky operations. Define the **level of automation** per action.

### Intent classification
Often needed to help agents pick the right tools. Should classify out-of-scope requests as IRRELEVANT.
