---
type: method
tags: [inference, caching, prompt-caching, cost-optimization, latency]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#inference-service-optimization
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Prompt Caching

Stores processed representations of overlapping prompt segments (typically system prompts or shared documents) to avoid redundant prefill computation across requests. Also called context cache or prefix cache.

### Impact
- A 1,000-token system prompt across 1M daily API calls = ~1B redundant input tokens/day eliminated.
- Anthropic: up to 90% cost savings, 75% latency reduction for long cached contexts.
- Google Gemini: 75% discount on cached tokens (plus cache storage fee).

### Example results (Anthropic, 2024)
| Use case | TTFT without | TTFT with | Cost reduction |
|---|---|---|---|
| Chat with book (100K cached) | 11.5 s | 2.4 s (–79%) | –90% |
| Many-shot (10K prompt) | 1.6 s | 1.1 s (–31%) | –86% |
| 10-turn convo + long system prompt | ~10 s | ~2.5 s (–75%) | –53% |

Trade-off: cache consumes memory (like KV cache). Engineering effort is non-trivial if self-hosting. Introduced by Gim et al. (Nov 2023), now widely adopted by API providers.
