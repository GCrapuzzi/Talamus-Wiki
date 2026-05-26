---
type: pattern
tags: [routing, intent-classification, cost-optimization, architecture]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#step-3-add-model-router-and-gateway
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Model Router

A routing layer (typically an intent classifier) that directs queries to the optimal downstream solution. Benefits:

- **Specialisation** — route technical issues to a troubleshooting model, billing to a billing model.
- **Cost reduction** — send simple queries to cheaper/smaller models.
- **Scope enforcement** — decline out-of-scope queries with stock responses, avoiding wasted API calls.
- **Disambiguation** — detect ambiguous queries and ask for clarification.
- **Next-action prediction** — in agentic systems, decide whether to invoke code interpreter, search API, or memory retrieval.

Implementation: commonly fine-tuned small models (GPT-2, BERT, Llama 7B) or even smaller classifiers trained from scratch. Routers must be fast and cheap — they sit on the critical path. Routing typically happens *before* retrieval (scope check → retrieval → generation → scoring is the common pattern).

When routing to models with different context limits, the query context may need truncation or the query may be re-routed to a larger-context model.
