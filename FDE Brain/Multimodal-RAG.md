---
type: pattern
tags: [multimodal, rag, clip, text-to-sql, tabular-data]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#rag-beyond-texts
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Multimodal RAG

Extends RAG to retrieve not just text but images, video, audio, etc.

### Metadata-based retrieval
Retrieve images by matching query against titles, tags, captions.

### Content-based retrieval
Requires a **multimodal embedding model** (e.g., CLIP) that generates embeddings for both text and images in a shared space.

Workflow:
1. Generate CLIP embeddings for all data (text + images) → store in vector database
2. Generate CLIP embedding for query
3. Search vector database for nearest neighbors across modalities

### Tabular RAG (Text-to-SQL)
For structured data, RAG uses a different workflow:
1. **Text-to-SQL**: generate SQL from user query + table schemas
2. **SQL execution**: run the query
3. **Generation**: produce response from SQL results + original query

If many tables exist, an intermediate step predicts which tables are relevant.
