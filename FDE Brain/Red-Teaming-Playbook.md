---
type: operation
status: evergreen
aliases:
  - Red Teaming Playbook
  - Adversarial Testing
  - Security Probing
tags:
  - ai-engineering
  - security
  - testing
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/108-defenses-against-prompt-attacks.md
    locator: pages 272-274
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Many organizations have a security red team that comes up with new attacks so that they can make their systems safe against them.
created: 2026-05-26T21:55:46.020746+00:00
updated: 2026-05-26T21:55:46.020746+00:00
ingestion_run: 8d527d59
---

# Red Teaming Playbook

## Summary

A structured process of actively attempting to break or bypass an LLM system using novel, adversarial prompts and inputs to identify vulnerabilities.

## Core Idea

Security testing must be proactive. Red teaming moves beyond known attack templates (like those used in automated benchmarks) to simulate real-world, creative attacks, providing actionable data for defense mechanism development.

## Practical Use

Before deployment, dedicate resources to a red team exercise. Use automated tools (e.g., Advbench, PromptRobust) for baseline testing, but supplement this with human-led, creative attack simulations to find zero-day vulnerabilities.

## Related

- [[Prompt-Attack-Defense-Framework|Prompt Attack Defense Framework]]
