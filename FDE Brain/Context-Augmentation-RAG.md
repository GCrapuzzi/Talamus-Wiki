---
type: method
status: evergreen
aliases:
  - Context Augmentation (RAG)
  - Retrieval-Augmented Generation
  - External Context Injection
tags:
  - ai-engineering
  - rag
  - data-retrieval
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/167-step-1.-enhance-context.md
    locator: pages 474-474
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - The initial expansion of a platform usually involves adding mechanisms to allow the system to construct the relevant context needed by the model to answer each query.
      - Context can be constructed through various retrieval mechanisms, including text retrieval, image retrieval, and tabular data retrieval.
created: 2026-05-26T21:55:46.516764+00:00
updated: 2026-05-26T21:55:46.516764+00:00
ingestion_run: 8d527d59
---

# Context Augmentation (RAG)

## Summary

The process of enhancing a model's input by providing access to external, relevant data sources and tools, allowing the system to construct a comprehensive context for answering a query.

## Core Idea

Context augmentation solves the limitations of LLMs (knowledge cutoff, hallucination) by grounding responses in specific, verifiable, external data, making the system more reliable and domain-specific.

## Practical Use

Implement RAG pipelines by first identifying the data source (text, image, tabular), retrieving relevant chunks, and then injecting those chunks into the model's prompt context before the final generation step.

## Related

- Vector Databases
- Context Retrieval
- [[AI-Application-Enhancement-Pipeline|AI Application Enhancement Pipeline]]
