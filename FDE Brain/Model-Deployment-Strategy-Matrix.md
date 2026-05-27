---
type: framework
status: evergreen
aliases:
  - Model Deployment Strategy Matrix
  - API vs Self-hosting vs Edge
  - AI Model Deployment Options
tags:
  - ai-engineering
  - deployment
  - architecture
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/085-navigate-public-benchmarks.md
    locator: pages 215-223
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Comparing Commercial APIs, Self-hosting models, and Edge use cases based on control, rate limits, and internet dependency.
created: 2026-05-26T21:55:45.843926+00:00
updated: 2026-05-26T21:55:45.843926+00:00
ingestion_run: 8d527d59
---

# Model Deployment Strategy Matrix

## Summary

A decision framework comparing three primary deployment methods for AI models: Commercial APIs, Self-hosted Models, and Edge Devices, based on control, access, and operational constraints.

## Core Idea

The choice of deployment method dictates the trade-off between ease of use/maintenance (API) and control/transparency (Self-hosting/Edge). Understanding these constraints is the first step in narrowing down the technical feasibility of an AI solution.

## Practical Use

When starting a project, use this matrix to determine if the required level of data privacy, customization, or offline capability mandates self-hosting or edge deployment, rather than relying on a commercial API.

## Related

- [[AI-Model-Evaluation-Pipeline|AI Model Evaluation Pipeline]]
