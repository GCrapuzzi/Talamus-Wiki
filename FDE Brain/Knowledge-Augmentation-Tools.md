---
type: concept
status: evergreen
aliases:
  - Knowledge Augmentation Tools
  - Context Retrieval Tools
  - Information Grounding Tools
tags:
  - ai-engineering
  - data-retrieval
  - grounding
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/118-tools.md
    locator: pages 302-304
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Web browsing prevents a model from going stale.
      - Tools help an agent to both perceive the environment and act upon it.
      - Many such tools augment a model with your organization’s private processes and information.
created: 2026-05-26T21:55:46.098382+00:00
updated: 2026-05-26T21:55:46.098382+00:00
ingestion_run: 8d527d59
---

# Knowledge Augmentation Tools

## Summary

Tools designed to provide the agent with external, up-to-date, or private data sources, preventing the model from relying solely on its stale training data.

## Core Idea

These tools are critical for reducing hallucinations and ensuring relevance. They allow the agent to ground its responses in specific, verifiable context, whether that context is internal (e.g., internal APIs, Slack) or external (e.g., web search).

## Practical Use

Implement a multi-stage retrieval system: first, check internal knowledge bases (RAG/Vector DBs); second, check real-time data sources (Search APIs); third, if necessary, use specialized APIs (e.g., inventory status).

## Related

- [[Web-Browsing-Tool|Web Browsing Tool]]
- [[RAG-Architecture|RAG Architecture]]
