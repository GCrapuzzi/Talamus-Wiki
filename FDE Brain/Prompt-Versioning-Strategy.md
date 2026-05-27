---
type: pattern
status: evergreen
aliases:
  - Prompt Versioning Strategy
  - GitOps for Prompts
  - Prompt Source Control
tags:
  - ai-engineering
  - mlops
  - devops
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/103-organize-and-version-prompts.md
    locator: pages 257-258
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - If the prompt files are part of your git repository, these prompts can be versioned using git.
created: 2026-05-26T21:55:45.980671+00:00
updated: 2026-05-26T21:55:45.980671+00:00
ingestion_run: 8d527d59
---

# Prompt Versioning Strategy

## Summary

Treat prompt files as code assets and store them within a Git repository. This allows for full version history, rollback capabilities, and collaborative review of prompt changes.

## Core Idea

Version control is mandatory for reproducibility. By committing prompts to Git, you ensure that any deployed application can be traced back to the exact prompt version used at the time of deployment, mitigating 'prompt drift' and ensuring auditability.

## Practical Use

Integrate prompt files into the CI/CD pipeline. When a prompt is updated, the change must be reviewed, versioned, and tested alongside the application code that consumes it. Use Git branching strategies to test prompt updates before merging to production.

## Related

- [[Prompt-Metadata-Schema|Prompt Metadata Schema]]
- [[Prompt-Code-Separation-Pattern|Prompt-Code Separation Pattern]]
