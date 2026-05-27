---
type: concept
status: evergreen
aliases:
  - Tool Use Failure Modes
  - Tool Output Errors
  - Tool Execution Failures
tags:
  - ai-engineering
  - tool-use
  - reliability
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/120-agent-failure-modes-and-evaluation.md
    locator: pages 322-323
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Tool failures happen when the correct tool is used, but the tool output is wrong.
      - One failure mode is when a tool just gives the wrong outputs.
      - failures can happen because of translation errors.
created: 2026-05-26T21:55:46.125527+00:00
updated: 2026-05-26T21:55:46.125527+00:00
ingestion_run: 8d527d59
---

# Tool Use Failure Modes

## Summary

Failures occurring after the agent correctly identifies and calls a tool, but the tool's output or the subsequent processing of that output is incorrect.

## Core Idea

Tool failures shift the focus from the agent's planning ability to the reliability of the external components (tools, APIs, translation layers). Mitigation requires validating tool outputs and implementing robust error handling.

## Practical Use

If an agent fails, and the plan structure is sound, suspect a tool failure. This could mean the tool itself is buggy (e.g., image captioner returns wrong description) or that an intermediate translation layer is faulty.

## Related

- [[Agent-Failure-Mode-Taxonomy|Agent Failure Mode Taxonomy]]
- Translation Error
