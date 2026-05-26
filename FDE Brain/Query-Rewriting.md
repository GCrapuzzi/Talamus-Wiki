---
type: method
tags: [query-rewriting, rag, retrieval-optimization, conversational-ai]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#retrieval-optimization
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Query Rewriting

Also called query reformulation, normalization, or expansion. Rewrites ambiguous or context-dependent queries into self-contained queries for better retrieval.

### Problem
Conversational follow-ups like "How about Emily Doe?" lack context when used as retrieval queries.

### Approach
Use an AI model with a prompt like: *"Given the following conversation, rewrite the last user input to reflect what the user is actually asking."*

The rewritten query should make sense on its own.

### Complications
- **Identity resolution**: "How about his wife?" requires a database lookup first
- **Knowledge gaps**: the rewriting model should acknowledge unsolvable queries rather than hallucinating
- In traditional search, done with heuristics; in AI applications, done with AI models
