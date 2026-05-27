---
type: framework
status: evergreen
aliases:
  - AI Application Evaluation Framework
  - AI system evaluation criteria
  - AI application assessment buckets
tags:
  - ai-engineering
  - evaluation
  - mlops
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/078-domain-specific-capability.md
    locator: pages 185-186
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - An AI application should start with a list of evaluation criteria specific to the application.
      - "Criteria can be grouped into: domain-specific capability, generation capability, instruction-following capability, and cost and latency."
created: 2026-05-26T21:55:45.794627+00:00
updated: 2026-05-26T21:55:45.794627+00:00
ingestion_run: 8d527d59
---

# AI Application Evaluation Framework

## Summary

A structured approach to evaluating AI applications by considering four distinct, necessary criteria: Domain-Specific Capability, Generation Capability, Instruction-Following Capability, and Cost/Latency.

## Core Idea

AI applications require holistic evaluation beyond just functional correctness. Focusing only on easily measurable outcomes (like classification) risks missing complex, game-changing applications. Evaluation must be multi-faceted.

## Practical Use

When starting a new AI project, define evaluation criteria across these four buckets: 1) Does the model understand the domain (e.g., legal jargon)? 2) Is the output coherent/faithful (Generation)? 3) Does it meet format constraints (Instruction-Following)? 4) Is it cost-effective and fast enough (Cost/Latency)?

## Related

- [[Domain-Specific-Capability-Evaluation|Domain-Specific Capability Evaluation]]
- Evaluation-Driven Development
