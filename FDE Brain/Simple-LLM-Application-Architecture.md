---
type: pattern
status: evergreen
aliases:
  - Simple LLM Application Architecture
  - Baseline AI Workflow
  - Query-Response Pattern
tags:
  - ai-engineering
  - architecture
  - pattern
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/167-step-1.-enhance-context.md
    locator: pages 474-474
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - In its simplest form, your application receives a query and sends it to the model. The model generates a response, which is returned to the user... There is no context augmentation, no guardrails, and no optimization.
created: 2026-05-26T21:55:46.518424+00:00
updated: 2026-05-26T21:55:46.518424+00:00
ingestion_run: 8d527d59
---

# Simple LLM Application Architecture

## Summary

The most basic AI application flow: User Query -> Model API (Third-party or Self-hosted) -> Generated Response.

## Core Idea

This pattern represents the Minimum Viable Product (MVP) baseline. It lacks context augmentation, guardrails, and optimization, serving as the starting point before adding complexity.

## Practical Use

Used to define the initial scope and measure the complexity increase when implementing advanced features like RAG or complex routing.

## Related

- [[AI-Application-Enhancement-Pipeline|AI Application Enhancement Pipeline]]
