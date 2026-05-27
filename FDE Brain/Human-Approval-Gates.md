---
type: pattern
status: evergreen
aliases:
  - Human Approval Gates
  - Explicit Authorization Check
  - High-Impact Command Gate
tags:
  - ai-engineering
  - security
  - data-governance
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/108-defenses-against-prompt-attacks.md
    locator: pages 272-274
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - For example, if your AI system has access to an SQL database, you can set a rule that all queries attempting to change the database, such as those containing “DELETE”, “DROP”, or “UPDATE”, must be approved before executing.
created: 2026-05-26T21:55:46.026141+00:00
updated: 2026-05-26T21:55:46.026141+00:00
ingestion_run: 8d527d59
---

# Human Approval Gates

## Summary

Implementing a mandatory human review and explicit approval step before the system executes any potentially impactful or irreversible command (e.g., database writes, financial transactions, system deletions).

## Core Idea

For actions that carry high risk (e.g., SQL DELETE, DROP, UPDATE), the system should not proceed automatically. This gate ensures accountability and prevents automated malicious or accidental execution.

## Practical Use

If your AI system interacts with databases, set up a rule that any query containing destructive keywords ('DELETE', 'DROP', 'UPDATE') must be flagged and presented to a human operator for explicit confirmation before execution.

## Related

- [[Prompt-Attack-Defense-Framework|Prompt Attack Defense Framework]]
