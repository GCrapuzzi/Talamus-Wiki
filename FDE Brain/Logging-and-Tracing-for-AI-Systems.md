---
type: operation
tags: [logging, tracing, drift-detection, observability]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#monitoring-and-observability
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Logging and Tracing for AI Systems

Metrics tell you *something* went wrong; logs and traces tell you *what* went wrong.

### Logging
General rule: **log everything**.
- Configurations: model endpoint, model name, sampling params (temperature, top-p, top-k, stop condition), prompt template.
- Data flow: user query, final prompt sent to model, output, intermediate outputs.
- Tool use: tool calls, tool outputs.
- Lifecycle events: component start/end, crashes.
- Tag every log entry with IDs tracing it to its origin in the system.

Logs must be real-time (not 15-min delayed) for fast incident response. Use AI-powered log analysis and anomaly detection for scale, but also manually inspect production data daily — developer perception of good/bad outputs evolves with exposure to real data (Shankar et al., 2024).

### Tracing
A trace reconstructs the full execution path of a request: query → preprocessing → retrieval → prompt assembly → generation → scoring → response, with time and cost per step. If a query fails, tracing should pinpoint the exact failing step.

### Drift detection
Three drift sources unique to AI applications:
1. **System prompt changes** — template updates, typo fixes by coworkers.
2. **User behavior changes** — users adapt queries over time (shorter prompts, gaming strategies).
3. **Underlying model changes** — API-served model silently updated (e.g., GPT-3.5/4 version differences causing 10%+ performance swings).
