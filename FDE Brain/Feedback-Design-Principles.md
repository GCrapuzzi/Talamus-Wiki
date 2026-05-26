---
type: pattern
tags: [feedback, ux-design, product, data-collection]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#feedback-design
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Feedback Design Principles

Design guidance for when and how to collect user feedback in AI applications.

### When to collect
- **Onboarding** — calibrate the app (face scan, voice sample, skill-level quiz). Make initial feedback optional to reduce friction; fall back to neutral defaults.
- **When something bad happens** — let users downvote, regenerate, switch models, or give conversational corrections. Ideally, users can still complete their task (e.g., inpainting for image gen, manual edits for text).
- **When the model has low confidence** — present alternatives side-by-side for comparative evaluation; the choice generates preference data for finetuning.
- **Positive feedback** — controversial. Apple HIG warns against it (implies good results are exceptions). Counter-argument: reveals which features users love, enabling focus. Compromise: show feedback prompts to a small percentage of users.

### How to collect
- **Integrate into workflow** — feedback should require zero extra effort. Examples: Midjourney's upscale/variation/regenerate buttons; GitHub Copilot's Tab-to-accept.
- **Standalone app disadvantage** — ChatGPT/Claude can't track whether generated emails were actually sent; integrated tools (Gmail, Copilot) get richer signals.
- **Context with feedback** — thumbs up/down alone is shallow; the surrounding 5–10 turns enable root-cause analysis. May require explicit consent or data-donation flow.
- **Explain usage** — telling users how feedback is used motivates higher quality input.
- **Don't ask the impossible** — don't ask users to choose between two answers they can't evaluate (e.g., complex math).
- **Avoid ambiguity** — unclear icons/emojis lead to noisy data (Luma angry-emoji-as-5-stars example).
- **Private vs public feedback** — private signals yield more candid responses (X/Twitter likes went private → likes increased). Trade-off: reduced discoverability.
