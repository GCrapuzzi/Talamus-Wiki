---
type: pattern
status: evergreen
aliases:
  - Metrics Correlation Strategy
  - North Star Metric Alignment
  - KPI Correlation
tags:
  - business-intelligence
  - metrics
  - ai-engineering
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/172-monitoring-and-observability.md
    locator: pages 489-495
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - it’s useful to measure how these metrics correlate to each other and, especially, to your business north star metrics, which can be DAU (daily active user), session duration... or subscriptions.
created: 2026-05-26T21:55:46.550873+00:00
updated: 2026-05-26T21:55:46.550873+00:00
ingestion_run: 8d527d59
---

# Metrics Correlation Strategy

## Summary

The practice of measuring how technical and operational metrics relate to high-level business Key Performance Indicators (KPIs) or North Star Metrics.

## Core Idea

Metrics are most valuable when they can be correlated to business outcomes (e.g., DAU, session duration). Strong correlation suggests an optimization path; zero correlation suggests an area to avoid optimizing.

## Practical Use

When a new metric is introduced (e.g., 'Context Relevance Score'), immediately test its correlation against the business North Star Metric. This ensures engineering effort is focused on features that drive business value.

## Related

- [[AI-Monitoring-Playbook|AI Monitoring Playbook]]
