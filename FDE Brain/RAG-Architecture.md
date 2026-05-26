---
type: framework
tags: [rag, architecture, retriever, generator]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#rag-architecture
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# RAG Architecture

A RAG system has two components:

1. **Retriever** — fetches information from external memory sources
   - **Indexing**: processing data so it can be quickly retrieved later
   - **Querying**: sending a query to retrieve relevant data
2. **Generator** — produces a response based on retrieved information

In the original RAG paper (Lewis et al., 2020), retriever and generator were trained jointly. Modern systems typically use off-the-shelf components trained separately, though end-to-end finetuning improves performance significantly.

Documents are split into **chunks** to avoid arbitrarily long contexts. Retrieved chunks are joined with the user prompt via minor post-processing to form the final prompt fed to the generator.

The success of a RAG system depends primarily on retriever quality.
