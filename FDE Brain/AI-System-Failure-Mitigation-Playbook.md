---
type: operation
status: evergreen
aliases:
  - AI System Failure Mitigation Playbook
  - LLM Resilience Strategy
  - Failure Handling Workflow
tags:
  - ai-engineering
  - operations
  - reliability
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/168-step-2.-put-in-guardrails.md
    locator: pages 475-479
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Many failures can be mitigated by simple retry logic.
      - To reduce latency, you can make calls in parallel.
      - It’s also common to fall back on humans for tricky requests.
created: 2026-05-26T21:55:46.524868+00:00
updated: 2026-05-26T21:55:46.524868+00:00
ingestion_run: 8d527d59
---

# AI System Failure Mitigation Playbook

## Summary

A structured approach to handling model failures (empty, malformatted, or incorrect) by implementing layered recovery strategies to maintain user experience and system reliability.

## Core Idea

Since LLMs are probabilistic, failure is expected. A robust system must anticipate failure and implement escalating recovery methods to minimize user-perceived latency and maximize successful outcomes.

## Practical Use

Design a workflow that incorporates these strategies in order: 1) **Retry Logic:** Attempt the query X times (simple, low cost). 2) **Parallel Calls:** Send the query multiple times simultaneously and select the best response (higher cost, lower latency). 3) **Human Fallback:** Route complex or ambiguous queries (e.g., based on sentiment analysis) to human operators.

## Related

- Circuit Breaker Pattern
- [[Human-in-the-Loop-HITL|Human-in-the-Loop (HITL)]]
