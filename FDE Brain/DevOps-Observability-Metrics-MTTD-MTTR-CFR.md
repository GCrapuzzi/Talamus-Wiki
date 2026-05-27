---
type: framework
status: evergreen
aliases:
  - DevOps Observability Metrics (MTTD, MTTR, CFR)
  - System Reliability Metrics
  - Operational Health Metrics
tags:
  - devops
  - reliability
  - ai-engineering
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/172-monitoring-and-observability.md
    locator: pages 489-495
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - "MTTD (mean time to detection): When something bad happens, how long does it take to detect it?"
      - "MTTR (mean time to response): After detection, how long does it take to be resolved?"
      - "CFR (change failure rate): The percentage of changes or deployments that result in failures requiring fixes or rollbacks."
created: 2026-05-26T21:55:46.549583+00:00
updated: 2026-05-26T21:55:46.549583+00:00
ingestion_run: 8d527d59
---

# DevOps Observability Metrics (MTTD, MTTR, CFR)

## Summary

Three core metrics used to evaluate the quality and resilience of a software system's monitoring and deployment pipeline.

## Core Idea

These metrics provide a quantitative measure of operational maturity. A high Change Failure Rate (CFR) signals a need to improve the evaluation and deployment pipeline, ensuring bad changes are caught before production.

## Practical Use

Use these metrics to benchmark the reliability of your AI platform. If MTTR is high, focus on improving incident response playbooks. If CFR is high, implement stricter pre-deployment evaluation gates.

## Related

- [[AI-Monitoring-Playbook|AI Monitoring Playbook]]
