---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 038
section-title: Chapter 2. Understanding Foundation Models
source-location: pages 73-73
previous-section: AI Space/normalized/pdf/ai-engineering/sections/037-summary.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/039-training-data.md
classification: reusable-knowledge-candidate
---
# Chapter 2. Understanding Foundation Models

CHAPTER 2
Understanding Foundation Models
To build applications with foundation models, you first need foundation models.
While you don’t need to know how to develop a model to use it, a high-level under‐
standing will help you decide what model to use and how to adapt it to your needs.
Training a foundation model is an incredibly complex and costly process. Those who
know how to do this well are likely prevented by confidentiality agreements from dis‐
closing the secret sauce. This chapter won’t be able to tell you how to build a model
to compete with ChatGPT. Instead, I’ll focus on design decisions with consequential
impact on downstream applications.
With the growing lack of transparency in the training process of foundation models,
it’s difficult to know all the design decisions that go into making a model. In general,
however, differences in foundation models can be traced back to decisions about
training data, model architecture and size, and how they are post-trained to align
with human preferences.
Since models learn from data, their training data reveals a great deal about their capa‐
bilities and limitations. This chapter begins with how model developers curate train‐
ing data, focusing on the distribution of training data. Chapter 8  explores dataset
engineering techniques in detail, including data quality evaluation and data synthesis.
Given the dominance of the transformer architecture, it might seem that model
architecture is less of a choice. You might be wondering, what makes the transformer
architecture so special that it continues to dominate? How long until another archi‐
tecture takes over, and what might this new architecture look like? This chapter will
address all of these questions. Whenever a new model is released, one of the first
things people want to know is its size. This chapter will also explore how a model
developer might determine the appropriate size for their model.
