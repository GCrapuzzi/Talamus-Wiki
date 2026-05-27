---
type: glossary
status: evergreen
aliases:
  - AI System Metrics Taxonomy
  - AI Performance Metrics
  - LLM Operational Metrics
tags:
  - metrics
  - ai-engineering
  - llm-ops
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/172-monitoring-and-observability.md
    locator: pages 489-495
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - "Time to first token (TTFT): the time it takes for the first token to be generated."
      - "Time per output token (TPOT): the time it takes to generate each output token."
      - Cost-related metrics are the number of queries and the volume of input and output tokens...
created: 2026-05-26T21:55:46.548256+00:00
updated: 2026-05-26T21:55:46.548256+00:00
ingestion_run: 8d527d59
---

# AI System Metrics Taxonomy

## Summary

A categorized list of essential metrics for monitoring AI applications, covering performance, cost, quality, and user experience.

## Core Idea

AI systems require a diverse set of metrics because failure can manifest in many ways (technical, financial, or qualitative). Metrics must be granularly tracked and correlated to identify actionable insights.

## Practical Use

When building a monitoring dashboard, ensure the following categories are included: 1. **Latency:** TTFT, TPOT, Total Latency. 2. **Cost:** Input/Output tokens, Queries/second. 3. **Quality:** Format validity, Factual consistency, Toxicity triggers. 4. **User Behavior:** Turns per conversation, Tokens per input/output.

## Related

- [[AI-Monitoring-Playbook|AI Monitoring Playbook]]
- Latency Metrics
