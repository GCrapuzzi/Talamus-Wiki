---
type: concept
tags: [evaluation, hallucination, factual-consistency, NLI]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#generation-capability
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Factual Consistency Verification

Two settings for verifying factual consistency of model outputs:

**Local factual consistency** — output evaluated against an explicit context (e.g., summary vs. source document, chatbot vs. company policy). Easier to verify.

**Global factual consistency** — output evaluated against open-world knowledge. Requires first finding reliable sources, then validating.

Verification techniques:
- **AI as a judge** — prompt an LLM to assess consistency (Liu et al. 2023 showed GPT-3.5/4 outperform prior methods)
- **Self-verification (SelfCheckGPT)** — generate N alternative responses; if they disagree with the original, it's likely hallucinated. Expensive.
- **Knowledge-augmented verification (SAFE)** — decompose response into individual statements → make each self-contained → generate fact-checking queries → search → verify via AI. Leverages search engine as ground truth.
- **Textual entailment (NLI)** — classify (premise, hypothesis) pairs as entailment / contradiction / neutral. Specialized small models (e.g., DeBERTa-v3-base-mnli-fever-anli, 184M params) can do this cheaply.

Hallucination-prone queries: niche knowledge (VMO vs. IMO) and queries about things that don't exist ("What did X say about Y?" when X never addressed Y).

Benchmark: TruthfulQA — 817 questions across 38 categories where humans often answer incorrectly due to misconceptions.
