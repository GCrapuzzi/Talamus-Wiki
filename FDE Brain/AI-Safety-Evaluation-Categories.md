---
type: concept
tags: [safety, evaluation, toxicity, bias]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#generation-capability
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# AI Safety Evaluation Categories

Taxonomy of unsafe content in model outputs:

1. **Inappropriate language** — profanity, explicit content
2. **Harmful recommendations** — dangerous tutorials, encouraging self-destructive behaviour
3. **Hate speech** — racist, sexist, homophobic, discriminatory content
4. **Violence** — threats, graphic detail
5. **Stereotypes** — e.g., always using female names for nurses, male names for CEOs
6. **Political/religious bias** — models can lean toward specific ideologies depending on training (e.g., GPT-4 more left-wing/libertarian, Llama more authoritarian per Feng et al. 2023)

Detection approaches:
- General-purpose AI judges (GPT, Claude, Gemini) with appropriate prompts
- Provider moderation tools (OpenAI content moderation endpoint, Meta's Llama Guard)
- Specialized small models: Facebook hate speech detector, Skolkovo toxicity classifier, Perspective API — smaller, faster, cheaper than general-purpose judges

Benchmarks: RealToxicityPrompts (100K prompts likely to elicit toxic outputs), BOLD (bias in open-ended language generation).
