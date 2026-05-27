---
type: pattern
status: evergreen
aliases:
  - RAG Architecture
  - Retrieval-Augmented Generation
  - RAG System
tags:
  - ai-engineering
  - llm
  - retrieval
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/112-rag-architecture.md
    locator: pages 280-280
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - "A RAG system has two components: a retriever that retrieves information from external memory sources and a generator that generates a response based on the retrieved information."
      - The success of a RAG system depends on the quality of its retriever.
      - "A retriever has two main functions: indexing and querying."
created: 2026-05-26T21:55:46.045430+00:00
updated: 2026-05-26T21:55:46.045430+00:00
ingestion_run: 8d527d59
---

# RAG Architecture

## Summary

A system architecture that enhances Large Language Model (LLM) responses by retrieving relevant, external information from a knowledge base before generating an answer.

## Core Idea

RAG decouples the knowledge source from the generative model. Instead of relying solely on the model's internal training data (which may be outdated or lack proprietary context), it uses a dedicated retriever component to fetch context, grounding the LLM's response in verifiable, external data. This significantly improves accuracy and reduces hallucination.

## Practical Use

1. **System Design:** Implement a two-stage pipeline: (1) Indexing/Retrieval, (2) Generation. 2. **Optimization:** Focus performance efforts on the retriever component, as its quality dictates the success of the entire system. 3. **Implementation:** Use off-the-shelf components for the retriever and generator, but consider end-to-end fine-tuning for significant performance gains.

## Related

- Indexing Strategy
- Querying
- Long Context Models
