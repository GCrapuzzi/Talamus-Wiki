---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 109
section-title: Summary
source-location: pages 275-276
previous-section: AI Space/normalized/pdf/ai-engineering/sections/108-defenses-against-prompt-attacks.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/110-chapter-6.-rag-and-agents.md
classification: reusable-knowledge-candidate
---
# Summary

simple way to do so is to filter out inputs that contain predefined phrases typically
associated with controversial topics, such as “immigration” or “antivax”.
More advanced algorithms use AI to understand the user’s intent by analyzing the
entire conversation, not just the current input. They can block requests with inappro‐
priate intentions or direct them to human operators. Use an anomaly detection algo‐
rithm to identify unusual prompts.
You should also place guardrails both to the inputs and outputs. On the input side,
you can have a list of keywords to block, known prompt attack patterns to match the
inputs against, or a model to detect suspicious requests. However, inputs that appear
harmless can produce harmful outputs, so it’s important to have output guardrails, as
well. For example, a guardrail can check if an output contains PII or toxic informa‐
tion. Guardrails are discussed more in Chapter 10.
Bad actors can be detected not just by their individual inputs and outputs but also by
their usage patterns. For example, if a user seems to send many similar-looking
requests in a short period of time, this user might be looking for a prompt that breaks
through safety filters.
Summary
Foundation models can do many things, but you must tell them exactly what you
want. The process of crafting an instruction to get a model to do what you want is
called prompt engineering. How much crafting is needed depends on how sensitive
the model is to prompts. If a small change can cause a big change in the model’s
response, more crafting will be necessary.
You can think of prompt engineering as human–AI communication. Anyone can
communicate, but not everyone can communicate well. Prompt engineering is easy
to get started, which misleads many into thinking that it’s easy to do it well.
The first part of this chapter discusses the anatomy of a prompt, why in-context
learning works, and best prompt engineering practices. Whether you’re communicat‐
ing with AI or other humans, clear instructions with examples and relevant informa‐
tion are essential. Simple tricks like asking the model to slow down and think step by
step can yield surprising improvements. Just like humans, AI models have their
quirks and biases, which need to be considered for a productive relationship with
them.
Foundation models are useful because they can follow instructions. However, this
ability also opens them up to prompt attacks in which bad actors get models to follow
malicious instructions. This chapter discusses different attack approaches and poten‐
tial defenses against them. As security is an ever-evolving cat-and-mouse game, no
Summary | 251

22 Given that many high-stakes use cases still haven’t adopted the internet, it’ll be a long while until they adopt
AI.
security measurements will be foolproof. Security risks will remain a significant road‐
block for AI adoption in high-stakes environments.22
This chapter also discusses techniques to write better instructions to get models to do
what you want. However, to accomplish a task, a model needs not just instructions
but also relevant context. How to provide a model with relevant information will be
discussed in the next chapter.
252 | Chapter 5: Prompt Engineering
