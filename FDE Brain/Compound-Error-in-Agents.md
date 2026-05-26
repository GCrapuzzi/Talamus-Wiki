---
type: concept
tags: [agents, reliability, compound-error, accuracy]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#agent-overview
  - AI Space/normalized/pdf/ai-engineering.md#tools
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Compound Error in Agents

In multi-step agent execution, overall accuracy degrades exponentially with the number of steps.

If per-step accuracy is p, accuracy over n steps is approximately p^n:
- 95% per step → 60% over 10 steps → 0.6% over 100 steps

This is why agents require more powerful models than single-shot applications, and why [[Agent Planning]] with reflection and error correction is critical. It also explains why efficiency (minimizing steps) directly impacts reliability, not just cost.
