---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 015
section-title: The Rise of AI Engineering
source-location: pages 26-26
previous-section: AI Space/normalized/pdf/ai-engineering/sections/014-chapter-1.-introduction-to-building-ai-applications-with-foundation-models.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/016-from-language-models-to-large-language-models.md
classification: reusable-knowledge-candidate
---
# The Rise of AI Engineering

1 In this book, I use traditional ML to refer to all ML before foundation models.
large-scale, readily available models brings about new possibilities and new chal‐
lenges, which are the focus of this book.
This chapter begins with an overview of foundation models, the key catalyst behind
the explosion of AI engineering. I’ll then discuss a range of successful AI use cases,
each illustrating what AI is good and not yet good at. As AI’s capabilities expand
daily, predicting its future possibilities becomes increasingly challenging. However,
existing application patterns can help uncover opportunities today and offer clues
about how AI may continue to be used in the future.
To close out the chapter, I’ll provide an overview of the new AI stack, including what
has changed with foundation models, what remains the same, and how the role of an
AI engineer today differs from that of a traditional ML engineer.1
The Rise of AI Engineering
Foundation models emerged from large language models, which, in turn, originated
as just language models. While applications like ChatGPT and GitHub’s Copilot may
seem to have come out of nowhere, they are the culmination of decades of technology
advancements, with the first language models emerging in the 1950s. This section
traces the key breakthroughs that enabled the evolution from language models to AI
engineering.
From Language Models to Large Language Models
While language models have been around for a while, they’ve only been able to grow
to the scale they are today with self-supervision. This section gives a quick overview of
what language model and self-supervision mean. If you’re already familiar with those,
feel free to skip this section.
Language models
A language model encodes statistical information about one or more languages. Intui‐
tively, this information tells us how likely a word is to appear in a given context. For
example, given the context “My favorite color is __”, a language model that encodes
English should predict “blue” more often than “car”.
2 | Chapter 1: Introduction to Building AI Applications with Foundation Models
