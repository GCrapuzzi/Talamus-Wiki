---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 008
section-title: Navigating This Book
source-location: pages 18-18
previous-section: AI Space/normalized/pdf/ai-engineering/sections/007-who-this-book-is-for.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/009-conventions-used-in-this-book.md
classification: reusable-knowledge-candidate
---
# Navigating This Book

Navigating This Book
This book is structured to follow the typical process for developing an AI application.
Here’s what this typical process looks like and how each chapter fits into the process.
Because this book is modular, you’re welcome to skip any section that you’re already
familiar with or that is less relevant to you.
Before deciding to build an AI application, it’s necessary to understand what this pro‐
cess involves and answer questions such as: Is this application necessary? Is AI
needed? Do I have to build this application myself? The first chapter of the book
helps you answer these questions. It also covers a range of successful use cases to give
a sense of what foundation models can do.
While an ML background is not necessary to build AI applications, understanding
how a foundation model works under the hood is useful to make the most out of it.
Chapter 2 analyzes the making of a foundation model and the design decisions with
significant impacts on downstream applications, including its training data recipe,
model architectures and scales, and how the model is trained to align to human pref‐
erence. It then discusses how a model generates a response, which helps explain the
model’s seemingly baffling behaviors, like inconsistency and hallucinations. Chang‐
ing the generation setting of a model is also often a cheap and easy way to signifi‐
cantly boost the model’s performance.
Once you’ve committed to building an application with foundation models, evalua‐
tion will be an integral part of every step along the way. Evaluation is one of the hard‐
est, if not the hardest, challenges of AI engineering. This book dedicates two chapters,
Chapters 3 and 4, to explore different evaluation methods and how to use them to
create a reliable and systematic evaluation pipeline for your application.
Given a query, the quality of a model’s response depends on the following aspects
(outside of the model’s generation setting):
• The instructions for how the model should behave
• The context the model can use to respond to the query
• The model itself
The next three chapters of the book focus on how to optimize each of these aspects to
improve a model’s performance for an application. Chapter 5  covers prompt engi‐
neering, starting with what a prompt is, why prompt engineering works, and prompt
engineering best practices. It then discusses how bad actors can exploit your applica‐
tion with prompt attacks and how to defend your application against them.
Chapter 6 explores why context is important for a model to generate accurate respon‐
ses. It zooms into two major application patterns for context construction: RAG and
agentic. The RAG pattern is better understood and has proven to work well in
xvi | Preface
