---
type: concept
tags: [self-supervision, training, data-labeling, scaling, fundamentals]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#from-language-models-to-large-language-models
  - AI Space/normalized/pdf/ai-engineering.md#from-large-language-models-to-foundation-models
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Self-Supervised Learning

A training paradigm where labels are inferred from the input data itself, eliminating the manual labeling bottleneck that constrains supervised learning.

In language modeling, each input sequence provides both context and labels: the sentence "I love street food." yields multiple training samples where preceding tokens predict the next token. This means language models can learn from any text corpus — books, articles, Reddit — enabling massive dataset construction at zero labeling cost.

Distinct from **unsupervised learning** (no labels at all) and **supervised learning** (explicit human-provided labels).

**Why it matters for scale:** Supervised labeling costs ~$0.05/image; labeling 1M images for ImageNet costs ~$50K. Scaling to 1M categories would cost ~$50M. Domain-expert labeling (e.g. CT scans, Latin translations) costs far more. Self-supervision removes this ceiling entirely, enabling the data scale that turned language models into LLMs.

Extends beyond text: OpenAI's CLIP used **natural language supervision** — harvesting 400M (image, text) pairs co-occurring on the internet — to train a multimodal model without manual labels.
