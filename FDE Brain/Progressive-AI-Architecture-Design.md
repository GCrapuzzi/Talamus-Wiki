---
type: pattern
status: evergreen
aliases:
  - Progressive AI Architecture Design
  - Iterative AI System Build
  - Minimum Viable AI Architecture
tags:
  - ai-engineering
  - design-framework
  - architecture
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/166-ai-engineering-architecture.md
    locator: pages 473-473
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - It starts with the simplest architecture for a foundation model application, highlights the challenges of that architecture, and gradually adds components to address them.
created: 2026-05-26T21:55:46.510633+00:00
updated: 2026-05-26T21:55:46.510633+00:00
ingestion_run: 8d527d59
---

# Progressive AI Architecture Design

## Summary

A methodology for developing complex AI applications by starting with the simplest functional architecture and incrementally adding components and complexity to address identified limitations and improve performance.

## Core Idea

Instead of attempting to build a fully featured, complex system upfront, this pattern mandates a gradual, validated approach. This minimizes initial development risk and allows for targeted resource allocation based on real-world performance gaps.

## Practical Use

When designing a new AI product, first implement the core foundation model functionality (the simplest architecture). Then, systematically introduce components like RAG, tool calling, or advanced feedback mechanisms only after the initial version proves insufficient or hits a defined bottleneck.

## Related

- Minimum Viable Product (MVP)
- [[AI-Engineering-Architecture|AI Engineering Architecture]]
