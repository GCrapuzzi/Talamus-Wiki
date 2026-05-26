---
type: pattern
tags: [react, agents, reasoning, reflection, reflexion]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#planning
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# ReAct Pattern

Interleaving **reasoning** and **action** in agent execution (Yao et al., 2022). "Reasoning" encompasses both planning and reflection.

At each step, the agent:
1. **Thought**: explain thinking (planning)
2. **Act**: take an action
3. **Observation**: analyze results (reflection)

Repeat until the agent determines the task is finished:
```
Thought 1: …
Act 1: …
Observation 1: …
…
Thought N: …
Act N: Finish [Response]
```

### Trade-offs
- Thoughts, observations, and actions consume many tokens → increased cost and latency
- Requires many in-context examples to nudge the format → reduces available context
- But reflection brings surprisingly good performance improvement

Related: Reflexion (Shinn et al., 2023) separates reflection into an **evaluator** (scores outcomes) and a **self-reflection module** (analyzes what went wrong), generating new trajectories after failure.
