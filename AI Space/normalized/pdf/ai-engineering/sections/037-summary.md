---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 037
section-title: Summary
source-location: pages 71-72
previous-section: AI Space/normalized/pdf/ai-engineering/sections/036-ai-engineering-versus-full-stack-engineering.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/038-chapter-2.-understanding-foundation-models.md
classification: reusable-knowledge-candidate
---
# Summary

lar, but there is also increasing support for JavaScript APIs, with LangChain.js, Transformers.js, OpenAI’s Node library, and Vercel’s AI SDK.

While many AI engineers come from traditional ML backgrounds, more are increasingly coming from web development or full-stack backgrounds. An advantage that full-stack engineers have over traditional ML engineers is their ability to quickly turn ideas into demos, get feedback, and iterate.

With traditional ML engineering, you usually start with gathering data and training a model. Building the product comes last. However, with AI models readily available today, it’s possible to start with building the product first, and only invest in data and models once the product shows promise, as visualized in Figure 1-16.

ML Engineering: Data → Model → Product

AI Engineering: Product → Data → Model

Figure 1-16. The new AI engineering workflow rewards those who can iterate fast. Image recreated from “The Rise of the AI Engineer” (Shawn Wang, 2023).

In traditional ML engineering, model development and product development are often disjointed processes, with ML engineers rarely involved in product decisions at many organizations. However, with foundation models, AI engineers tend to be much more involved in building the product.

Summary

I meant this chapter to serve two purposes. One is to explain the emergence of AI engineering as a discipline, thanks to the availability of foundation models. Two is to give an overview of the process needed to build applications on top of these models. I hope that this chapter achieved this goal. As an overview chapter, it only lightly touched on many concepts. These concepts will be explored further in the rest of the book.

The chapter discussed the rapid evolution of AI in recent years. It walked through some of the most notable transformations, starting with the transition from language models to large language models, thanks to a training approach called self-supervision. It then traced how language models incorporated other data modalities to become foundation models, and how foundation models gave rise to AI engineering.

The rapid growth of AI engineering is motivated by the many applications enabled by the emerging capabilities of foundation models. This chapter discussed some of the most successful application patterns, both for consumers and enterprises. Despite the

incredible number of AI applications already in production, we’re still in the early
stages of AI engineering, with countless more innovations yet to be built.
Before building an application, an important yet often overlooked question is
whether you should build it. This chapter discussed this question together with major
considerations for building AI applications.
While AI engineering is a new term, it evolved out of ML engineering, which is the
overarching discipline involved with building applications with all ML models. Many
principles from ML engineering are still applicable to AI engineering. However, AI
engineering also brings with it new challenges and solutions. The last section of the
chapter discusses the AI engineering stack, including how it has changed from ML
engineering.
One aspect of AI engineering that is especially challenging to capture in writing is the
incredible amount of collective energy, creativity, and engineering talent that the
community brings. This collective enthusiasm can often be overwhelming, as it’s
impossible to keep up-to-date with new techniques, discoveries, and engineering
feats that seem to happen constantly.
One consolation is that since AI is great at information aggregation, it can help us
aggregate and summarize all these new updates. But tools can help only to a certain
extent. The more overwhelming a space is, the more important it is to have a frame‐
work to help us navigate it. This book aims to provide such a framework.
The rest of the book will explore this framework step-by-step, starting with the fun‐
damental building block of AI engineering: the foundation models that make so
many amazing applications possible.
48 | Chapter 1: Introduction to Building AI Applications with Foundation Models
