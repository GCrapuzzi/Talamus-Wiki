---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 020
section-title: Coding
source-location: pages 44-45
previous-section: AI Space/normalized/pdf/ai-engineering/sections/019-foundation-model-use-cases.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/021-image-and-video-production.md
classification: reusable-knowledge-candidate
---
# Coding

Even after seeing hundreds of AI applications, I still find new applications that sur‐
prise me every week. In the early days of the internet, few people foresaw that the
dominating use case on the internet one day would be social media. As we learn to
make the most out of AI, the use case that will eventually dominate might surprise us.
With luck, the surprise will be a good one.
Coding
In multiple generative AI surveys, coding is hands down the most popular use case.
AI coding tools are popular both because AI is good at coding and because early AI
engineers are coders who are more exposed to coding challenges.
One of the earliest successes of foundation models in production is the code comple‐
tion tool GitHub Copilot, whose annual recurring revenue crossed $100 million  only
two years after its launch. As of this writing, AI-powered coding startups have raised
hundreds of millions of dollars, with Magic raising $320 million and Anysphere rais‐
ing $60 million, both in August 2024. Open source coding tools like gpt-engineer and
screenshot-to-code both got 50,000 stars on GitHub within a year, and many more
are being rapidly introduced.
Other than tools that help with general coding, many tools specialize in certain cod‐
ing tasks. Here are examples of these tasks:
• Extracting structured data from web pages and PDFs (AgentGPT)
• Converting English to code (DB-GPT, SQL Chat, PandasAI)
• Given a design or a screenshot, generating code that will render into a website
that looks like the given image (screenshot-to-code, draw-a-ui)
• Translating from one programming language or framework to another ( GPTMigrate, AI Code Translator)
• Writing documentation (Autodoc)
• Creating tests (PentestGPT)
• Generating commit messages (AI Commits)
20 | Chapter 1: Introduction to Building AI Applications with Foundation Models

It’s clear that AI can do many software engineering tasks. The question is whether AI
can automate software engineering altogether. At one end of the spectrum, Jensen
Huang, CEO of NVIDIA, predicts that AI will replace human software engineers and
that we should stop saying kids should learn to code. In a leaked recording, AWS
CEO Matt Garman  shared that in the near future, most developers will stop coding.
He doesn’t mean it as the end of software developers; it’s just that their jobs will
change.
At the other end are many software engineers who are convinced that they will never
be replaced by AI, both for technical and emotional reasons (people don’t like admit‐
ting that they can be replaced).
Software engineering consists of many tasks. AI is better at some than others. McKin‐
sey researchers found that AI can help developers be twice as productive for docu‐
mentation, and 25–50% more productive for code generation and code refactoring.
Minimal productivity improvement was observed for highly complex tasks, as shown
in Figure 1-9. In my conversations with developers of AI coding tools, many told me
that they’ve noticed that AI is much better at frontend development than backend
development.
Figure 1-9. AI can help developers be significantly more productive, especially for sim‐
ple tasks, but this applies less for highly complex tasks. Data by McKinsey.
Foundation Model Use Cases | 21

[Visual content extracted via GLM-OCR]

It’s clear that AI can do many software engineering tasks. The question is whether AI can automate software engineering altogether. At one end of the spectrum, Jensen Huang, CEO of NVIDIA, predicts that AI will replace human software engineers and that we should stop saying kids should learn to code. In a leaked recording, AWS CEO Matt Garman shared that in the near future, most developers will stop coding. He doesn’t mean it as the end of software developers; it’s just that their jobs will change.

At the other end are many software engineers who are convinced that they will never be replaced by AI, both for technical and emotional reasons (people don’t like admitting that they can be replaced).

Software engineering consists of many tasks. AI is better at some than others. McKinsey researchers found that AI can help developers be twice as productive for documentation, and 25–50% more productive for code generation and code refactoring. Minimal productivity improvement was observed for highly complex tasks, as shown in Figure 1-9. In my conversations with developers of AI coding tools, many told me that they’ve noticed that AI is much better at frontend development than backend development.

Figure 1-9. AI can help developers be significantly more productive, especially for simple tasks, but this applies less for highly complex tasks. Data by McKinsey.
