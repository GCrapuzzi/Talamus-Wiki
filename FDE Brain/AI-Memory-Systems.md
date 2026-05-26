---
type: framework
tags: [memory, short-term-memory, long-term-memory, context-management, agents]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#memory
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# AI Memory Systems

Memory mechanisms that allow a model to retain and utilize information across and within tasks.

### Three memory tiers
1. **Internal knowledge**: baked into model weights via training. Doesn't change without retraining. Available to all queries.
2. **Short-term memory**: the model's context window. Stores conversation history and current task info. Fast access, limited capacity, doesn't persist across tasks.
3. **Long-term memory**: external data sources accessed via retrieval (RAG). Persists across tasks. Can be updated/deleted without model changes.

### Benefits
- Manage information overflow within a session
- Persist information between sessions (personalization)
- Boost model consistency across responses
- Maintain data structural integrity (structured storage for tables, queues)

### Memory management operations
- **Add**: store new information
- **Delete**: remove outdated/redundant information (critical for short-term memory due to context limits)

### Short-term memory strategies
- **FIFO** (first in, first out): simple but can lose critical early context
- **Summarization**: compress conversation; track named entities
- **Reflection-based** (Liu et al., 2023): after each action, determine if new info should be inserted, merged, or replace outdated info
- **Redundancy detection** (Bae et al., 2022): classifier determines which sentences from memory + summary to keep

### Allocation
Decide what % of context to reserve for long-term memory retrieval vs. short-term memory. Overflow from short-term → long-term.
