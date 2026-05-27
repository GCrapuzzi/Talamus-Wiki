---
type: glossary
status: evergreen
aliases:
  - Generation Capability Metrics (NLG)
  - Open-ended Text Evaluation
  - NLG Metrics
tags:
  - ai-engineering
  - evaluation
  - nlp
sources:
  - raw_path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
    normalized_path: AI Space/normalized/pdf/ai-engineering/sections/079-generation-capability.md
    locator: pages 187-195
    source_hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
    supported_claims:
      - Fluency measures whether the text is grammatically correct and natural-sounding.
      - Coherence measures how well-structured the whole text is (does it follow a logical structure?).
      - "A metric that a translation task might use is faithfulness: how faithful is the generated translation to the original sentence?"
      - "A metric that a summarization task might use is relevance: does the summary focus on the most important aspects of the source document?"
created: 2026-05-26T21:55:45.804509+00:00
updated: 2026-05-26T21:55:45.804509+00:00
ingestion_run: 8d527d59
---

# Generation Capability Metrics (NLG)

## Summary

A set of metrics used to evaluate the quality of open-ended text generation, evolving from structural checks to semantic fidelity.

## Core Idea

Early metrics focused on structural quality (Fluency and Coherence). Modern metrics focus on semantic fidelity and safety (Faithfulness, Relevance, Factual Consistency). As models improve, the importance shifts from grammar to factual grounding.

## Practical Use

Select metrics based on the task type: Use Faithfulness for translation/summarization (ensuring the output sticks to the source meaning). Use Relevance for summarization (ensuring the summary focuses on key aspects). Use Factual Consistency for all high-stakes applications.

## Related

- [[Factual-Consistency-Evaluation|Factual Consistency Evaluation]]
- Fluency and Coherence
