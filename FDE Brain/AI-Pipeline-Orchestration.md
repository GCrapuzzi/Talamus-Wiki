---
type: concept
tags: [orchestration, pipeline, architecture, tooling]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#ai-pipeline-orchestration
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# AI Pipeline Orchestration

An orchestrator specifies how components (models, databases, tools, evaluators) compose into an end-to-end pipeline. Two-step operation:

1. **Components definition** — declare models, data sources, tools, evaluation/monitoring modules. A [[Model Gateway]] simplifies adding models.
2. **Chaining** — function composition defining the execution flow: process query → retrieve → prompt → generate → evaluate → return or escalate.

The orchestrator passes data between steps, validates format compatibility, and notifies on failures (component errors, data mismatches).

### Evaluation criteria
- **Integration & extensibility** — does it support your models/databases? How hard to add unsupported components?
- **Complex pipeline support** — branching, parallel processing, error handling.
- **Ease of use, performance, scalability** — intuitive APIs, no hidden API calls or added latency.

Tools: LangChain, LlamaIndex, Flowise, Langflow, Haystack.

**Pragmatic advice**: start without an orchestrator. Orchestrators abstract away critical details, making systems harder to debug. Adopt one only when pipeline complexity justifies it. Note: AI pipeline orchestrators differ from general workflow orchestrators (Airflow, Metaflow).
