---
type: method
status: evergreen
aliases:
  - "Output Selection Strategy: Average Log Probability"
  - Logprob averaging
  - Best average logprob
tags:
  - ai-engineering
  - llm-evaluation
  - metrics
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/051-test-time-compute.md
    locator: pages 120-122
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - The probability of an output is the product of the probabilities of all tokens in the output.
      - The logarithm of a product is equal to a sum of logarithms, so the logprob of a sequence of tokens is the sum of the logprob of all tokens in the sequence:
      - To avoid biasing toward short sequences, you can use the average logprob by dividing the sum of a sequence by its length.
created: 2026-05-26T21:55:45.591773+00:00
updated: 2026-05-26T21:55:45.591773+00:00
ingestion_run: 8d527d59
---

# Output Selection Strategy: Average Log Probability

## Summary

A quantitative method for selecting the best output among multiple candidates by calculating the average log probability (logprob) across all tokens in the sequence. This method is preferred over simple product probability due to numerical stability and avoiding bias toward short sequences.

## Core Idea

The logprob of a sequence is the sum of the logprobs of its tokens. By averaging this sum across multiple samples, the selection process balances high probability with sequence length, providing a robust metric for comparison.

## Practical Use

When using an LLM API that supports multiple sampling runs, calculate the logprob for each generated output. Select the output that maximizes the average logprob (Sum of logprobs / Length of sequence).

## Related

- [[Test-Time-Compute-TTC|Test Time Compute (TTC)]]
