---
type: framework
tags: [architecture, production-systems, ai-engineering]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#chapter-10-ai-engineering-architecture-and-user-feedback
  - AI Space/normalized/pdf/ai-engineering.md#step-1-enhance-context
  - AI Space/normalized/pdf/ai-engineering.md#step-2-put-in-guardrails
  - AI Space/normalized/pdf/ai-engineering.md#step-3-add-model-router-and-gateway
  - AI Space/normalized/pdf/ai-engineering.md#step-4-reduce-latency-with-caches
  - AI Space/normalized/pdf/ai-engineering.md#step-5-add-agent-patterns
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# AI Application Architecture Progression

A five-step incremental architecture for building production AI applications on foundation models:

1. **Enhance context** — add retrieval (text, image, tabular) and tool-use for information gathering. Context construction is feature engineering for foundation models.
2. **Put in guardrails** — input guardrails (PII detection, prompt-attack defense) and output guardrails (format validation, toxicity detection, retry/fallback policies).
3. **Add model router and gateway** — intent classifiers route queries to specialised or cheaper models; a gateway provides a unified interface, access control, cost management, and fallback policies across providers.
4. **Reduce latency with caches** — exact caching (deterministic key match) and [[Semantic Cache]] (embedding-similarity match with a threshold). Cache eviction via LRU/LFU/FIFO.
5. **Add agent patterns** — loops, parallel execution, conditional branching, and Write Actions that let the model change its environment.

Monitoring/observability is integral throughout, not an afterthought. Orchestration chains all components via function composition.
