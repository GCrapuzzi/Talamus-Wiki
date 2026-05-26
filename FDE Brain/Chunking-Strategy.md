---
type: method
tags: [chunking, rag, indexing, retrieval-optimization]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#retrieval-optimization
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Chunking Strategy

How documents are split into chunks significantly impacts retrieval performance.

### Strategies
- **Fixed-length**: split by characters, words, sentences, or paragraphs (e.g., 2048 chars, 512 words)
- **Recursive**: split by sections → paragraphs → sentences, stopping when chunks fit max size
- **Domain-specific**: programming language splitters, Q&A pair splitting, language-specific splitting
- **Token-based**: use the generative model's tokenizer as boundaries (but requires reindexing if model changes)

### Overlapping
Chunks without overlap can break mid-context ("I left my wife" / "a note"). Overlapping (e.g., 20 chars) ensures boundary information is preserved in at least one chunk.

### Chunk size trade-offs
- **Smaller chunks**: more diverse information, fit more chunks in context. But risk losing cross-chunk information, increase computational overhead (more embeddings, larger search space).
- **Larger chunks**: preserve more context per chunk. But fewer fit in context, may retrieve less diverse information.

Constraints: chunk size ≤ model's max context length; for embedding-based, also ≤ embedding model's context limit.

No universal best size — experiment to find what works.
