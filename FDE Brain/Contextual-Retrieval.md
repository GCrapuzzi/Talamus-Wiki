---
type: method
tags: [contextual-retrieval, rag, retrieval-optimization, anthropic]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#retrieval-optimization
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Contextual Retrieval

Augment each chunk with additional context to improve retrieval accuracy.

### Techniques
- **Metadata augmentation**: add tags, keywords, entity names, error codes, product descriptions
- **Question augmentation**: augment chunks with questions they can answer (e.g., password reset article → "I forgot my password", "I can't log in")
- **Document context**: prepend document title/summary to chunks that lost context during splitting

### Anthropic's approach
Use AI to generate 50–100 token context explaining each chunk's relationship to its parent document. Prompt:

```
<document>{{WHOLE_DOCUMENT}}</document>
<chunk>{{CHUNK_CONTENT}}</chunk>
Please give a short succinct context to situate this chunk within the overall document for improving search retrieval.
```

Generated context is prepended to the chunk before indexing.
