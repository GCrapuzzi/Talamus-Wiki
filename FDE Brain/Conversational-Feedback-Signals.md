---
type: framework
tags: [feedback, user-signals, evaluation, rlhf, conversational-ai]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#extracting-conversational-feedback
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Conversational Feedback Signals

Foundation-model applications unlock new feedback genres beyond traditional explicit (thumbs up/down) and implicit (purchase, click) signals.

### Natural language feedback (from message content)
- **Early termination** — user stops generation, exits app, leaves agent hanging → conversation going poorly.
- **Error correction** — "No, …", "I meant, …", rephrasing attempts (detectable via heuristics or ML).
- **Action-correcting feedback** — "You should also check their GitHub page" → nudging agent toward better actions.
- **Confirmation requests** — "Are you sure?", "Show me the sources" → low trust or insufficient detail.
- **User edits** — direct edits to model output are strong signals; each edit creates a preference pair (original = losing, edited = winning) for RLHF.
- **Complaints** — FITS dataset clustering (Yuan et al., 2023) found 8 groups: clarify demand (27%), irrelevant answer (16%), point to search results (16%), suggest using search results (15%), factual errors (11%), lack of detail (9%), low confidence hedging (4%), repetition/rudeness (1%).
- **Sentiment** — general frustration/satisfaction trajectory across a conversation.
- **Model refusal rate** — "As a language model, I can't …" correlates with user dissatisfaction.

### Behavioural feedback (from actions)
- **Regeneration** — dissatisfaction or desire for comparison; stronger signal with usage-based billing.
- **Conversation organisation** — delete (bad), rename (good content, bad title), share, bookmark.
- **Conversation length** — positive for companion apps, negative for productivity tools.
- **Dialogue diversity** — low distinct-token count + high length → user stuck in a loop.

Explicit feedback is sparse but interpretable; implicit feedback is abundant but noisy. Combine multiple signals to disambiguate intent.
