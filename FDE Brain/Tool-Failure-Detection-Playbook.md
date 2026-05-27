---
type: operation
status: evergreen
aliases:
  - Tool Failure Detection Playbook
  - Tool Reliability Testing
  - Agent Tool Validation
tags:
  - ai-engineering
  - testing
  - operations
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/121-memory.md
    locator: pages 324-328
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Tool failures are tool-dependent and need independent testing.
      - Always print out each tool call and its output for inspection.
      - If the agent frequently fails on a specific domain, work with human domain experts to identify missing tools.
created: 2026-05-26T21:55:46.139001+00:00
updated: 2026-05-26T21:55:46.139001+00:00
ingestion_run: 8d527d59
---

# Tool Failure Detection Playbook

## Summary

A systematic process for identifying and mitigating failures related to tool usage or missing tool capabilities.

## Core Idea

Tool failures are tool-dependent and must be tested independently. Detecting missing tools requires domain expertise to identify necessary capabilities the agent currently lacks.

## Practical Use

1. **Logging:** Always print and inspect every tool call and its output. 2. **Benchmarking:** Create specific benchmarks for complex tools (e.g., translators). 3. **Domain Gap Analysis:** When failure occurs in a specific domain, consult human domain experts to identify the missing tools or capabilities the agent needs.

## Related

- Agent Testing
- Tool Orchestration
