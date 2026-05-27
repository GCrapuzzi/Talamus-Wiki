---
type: method
status: evergreen
aliases:
  - Memory Management Strategies
  - Context Pruning Techniques
  - Information Retention Policies
tags:
  - ai-engineering
  - data-management
  - llm-optimization
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/121-memory.md
    locator: pages 324-328
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - FIFO (First In, First Out) is the simplest strategy.
      - Usage-based strategies (e.g., removing least frequently used info) are challenging but ideal.
      - Redundancy removal via summarization and entity tracking significantly reduces memory footprint.
created: 2026-05-26T21:55:46.134664+00:00
updated: 2026-05-26T21:55:46.134664+00:00
ingestion_run: 8d527d59
---

# Memory Management Strategies

## Summary

Algorithms for deciding which information to keep in the limited short-term memory and which to archive or discard.

## Core Idea

Since short-term memory is limited, a strategy must be employed to decide what to add and what to delete. Strategies range from simple chronological methods to complex semantic analysis.

## Practical Use

Select a strategy based on the application's needs: Use FIFO for simple, predictable logging. Use advanced summarization/classification for complex, high-stakes conversations to preserve semantic meaning.

## Related

- Summarization Techniques
- Vector Database Indexing
