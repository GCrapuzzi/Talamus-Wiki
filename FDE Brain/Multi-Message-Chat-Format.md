---
type: pattern
status: evergreen
aliases:
  - Multi-Message Chat Format
  - Structured Turn Data
  - Source/Destination Messaging
tags:
  - data-format
  - agent-engineering
  - llm-training
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/140-data-curation.md
    locator: pages 389-391
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - for tool use, the AI might need to generate multiple messages each turn, with each message sent to a different location.
      - Llama 3 authors ( Dubey et al., 2024 ) designed a multimessage chat format that consists of message headers that specify the source and destination of each message
created: 2026-05-26T21:55:46.310868+00:00
updated: 2026-05-26T21:55:46.310868+00:00
ingestion_run: 8d527d59
---

# Multi-Message Chat Format

## Summary

A specialized chat data format that allows the model to generate multiple, distinct messages within a single turn, each message specifying its source and destination (e.g., code interpreter, user, internal system).

## Core Idea

This format is necessary for modeling complex agentic behavior where a single user query triggers multiple, simultaneous actions or communications.

## Practical Use

When building multi-step agents, use this format to explicitly define the flow of information, such as sending a query to a search API and simultaneously informing the user of the action being taken.

## Related

- [[Tool-Use-Data-Generation|Tool Use Data Generation]]
