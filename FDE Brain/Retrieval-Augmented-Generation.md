---
type: pattern
tags: [rag, retrieval, context-construction, architecture-pattern]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#chapter-6-rag-and-agents
  - AI Space/normalized/pdf/ai-engineering.md#rag
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Retrieval-Augmented Generation

RAG enhances a model's generation by retrieving relevant information from external memory sources (internal databases, user chat history, the internet) and injecting it as context.

Core two-step process:
1. **Retrieve** — fetch chunks most relevant to the query from external memory
2. **Generate** — produce a response conditioned on retrieved context + user prompt

RAG constructs **query-specific context** rather than using the same context for all queries. This is the foundation-model equivalent of Feature Engineering for classical ML.

RAG remains valuable even with long-context models because:
- Data volume always grows faster than context windows
- Longer context degrades attention — models focus on the wrong parts
- Every extra token adds cost and latency
- RAG surfaces only the most relevant information, potentially improving performance

Anthropic guidance: if knowledge base < 200k tokens (~500 pages), stuffing context directly can work without RAG.

Origin: retrieve-then-generate pattern from Chen et al. (2017); term "RAG" coined by Lewis et al. (2020).
