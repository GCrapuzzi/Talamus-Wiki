---
type: concept
status: evergreen
aliases:
  - Multi-modal Data Extraction
  - Image Leakage
  - Diffusion Model Vulnerability
tags:
  - ai-engineering
  - multimodal
  - privacy
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/107-information-extraction.md
    locator: pages 267-271
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Diffusion models demonstrated how to extract over a thousand images with near-duplication of existing images.
      - Mitigating these vulnerabilities may require new advances in privacy-preserving training.
created: 2026-05-26T21:55:46.015704+00:00
updated: 2026-05-26T21:55:46.015704+00:00
ingestion_run: 8d527d59
---

# Multi-modal Data Extraction

## Summary

The vulnerability in generative models (like diffusion models) that allows the extraction of near-duplicate or copyrighted images/content from the training dataset.

## Core Idea

The risk of data leakage is not limited to text. Multi-modal models can memorize and reproduce visual data, requiring specialized privacy-preserving techniques beyond text-based filtering.

## Practical Use

When deploying multi-modal AI, ensure that the training data is scrubbed of proprietary or copyrighted visual assets. Consider watermarking or using techniques that prevent the model from reproducing specific training examples.

## Related

- [[Training-Data-Extraction-Memorization-Attacks|Training Data Extraction (Memorization Attacks)]]
