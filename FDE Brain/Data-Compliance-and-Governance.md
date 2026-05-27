---
type: concept
status: evergreen
aliases:
  - Data Compliance and Governance
  - PII Filtering
  - Regulatory Adherence
tags:
  - data-governance
  - compliance
  - ai-ethics
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/142-data-coverage.md
    locator: pages 393-395
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Data should be compliant with all relevant internal and external policies (including laws and regulations).
      - For example, if you’re not allowed to use PII data to train your models, your data shouldn’t contain any PII data.
created: 2026-05-26T21:55:46.330278+00:00
updated: 2026-05-26T21:55:46.330278+00:00
ingestion_run: 8d527d59
---

# Data Compliance and Governance

## Summary

The mandatory process of verifying that all training data adheres to relevant internal policies, external laws, and privacy regulations (e.g., GDPR, HIPAA).

## Core Idea

Using non-compliant data poses legal and ethical risks. Data governance requires proactive filtering and anonymization to ensure the model does not memorize or leak sensitive information.

## Practical Use

Before ingestion, run data through automated PII detection tools. Implement differential privacy techniques or synthetic data generation where direct use of sensitive real-world data is prohibited by law or policy.

## Related

- [[Data-Formatting-and-Cleaning|Data Formatting and Cleaning]]
