---
type: pattern
status: evergreen
aliases:
  - Structured Extraction Playbook
  - Action Item Parsing
  - Meeting Minutes Structuring
tags:
  - ai-engineering
  - prompt-engineering
  - workflow-automation
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/026-data-organization.md
    locator: pages 51-51
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - This template asks AI to summarize meeting notes, emails, and Slack conversations with facts, open questions, and action items.
      - These action items can then be automatically inserted into a project tracking tool and assigned to the right owners.
created: 2026-05-26T21:55:45.424476+00:00
updated: 2026-05-26T21:55:45.424476+00:00
ingestion_run: 8d527d59
---

# Structured Extraction Playbook

## Summary

A prompt engineering and workflow pattern used to systematically extract specific, predefined data fields (e.g., Facts, Open Questions, Action Items) from unstructured text sources.

## Core Idea

It converts narrative, unstructured text into machine-readable, structured data points that can be automatically inserted into project management or tracking tools.

## Practical Use

Developing a standardized prompt template that forces an LLM to output JSON or markdown tables containing 'Action Item Owner,' 'Due Date,' and 'Task Description' based on meeting transcripts.

## Related

- [[Information-Aggregation-Distillation|Information Aggregation & Distillation]]
