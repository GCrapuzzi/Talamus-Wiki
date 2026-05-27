---
type: pattern
status: evergreen
aliases:
  - Human-in-the-Loop (HITL)
  - Human Oversight System
  - AI Assisted Workflow
tags:
  - ai-engineering
  - workflow-automation
  - risk-management
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/029-use-case-evaluation.md
    locator: pages 53-55
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Involving humans in AI’s decision-making processes is called human-in-the-loop.
      - AI shows several responses that human agents can reference to write faster responses.
      - AI responds only to simple requests and routes more complex requests to humans.
created: 2026-05-26T21:55:45.448221+00:00
updated: 2026-05-26T21:55:45.448221+00:00
ingestion_run: 8d527d59
---

# Human-in-the-Loop (HITL)

## Summary

A design pattern where human judgment and intervention are integrated into the AI decision-making process, allowing for gradual automation and quality assurance.

## Core Idea

HITL mitigates risk by ensuring that AI's output is validated or guided by human expertise, enabling a controlled transition from human-only processes to full automation.

## Practical Use

Implement HITL by starting with AI generating suggestions for human agents (low automation). As confidence increases, move to AI handling simple requests and routing complex ones to humans (medium automation).

## Related

- [[Crawl-Walk-Run-Automation-Model|Crawl-Walk-Run Automation Model]]
