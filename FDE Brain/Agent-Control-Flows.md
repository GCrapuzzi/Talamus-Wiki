---
type: concept
tags: [agents, control-flow, planning, parallel-execution]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#planning
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Agent Control Flows

The order in which actions in a plan can be executed. AI models determine control flows in agent systems (vs. exact conditions in traditional software).

### Types
- **Sequential**: B executes after A completes (dependency). SQL execution after SQL generation.
- **Parallel**: A and B execute simultaneously. Fetch prices for 100 products at once.
- **If statement**: execute B or C depending on prior output. Check earnings report → buy or sell.
- **For loop**: repeat A until condition met. Generate random numbers until prime.

Plans with non-sequential control flows are harder to generate and translate into executable commands.

When evaluating agent frameworks, check what control flows are supported. **Parallel execution** can significantly reduce user-perceived latency.
