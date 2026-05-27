---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 092
section-title: Introduction to Prompting
source-location: pages 236-236
previous-section: AI Space/normalized/pdf/ai-engineering/sections/091-chapter-5.-prompt-engineering.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/093-in-context-learning-zero-shot-and-few-shot.md
classification: reusable-knowledge-candidate
---
# Introduction to Prompting

a real and useful skill to have. The problem is when prompt engineering is the only thing people know.” To build production-ready AI applications, you need more than just prompt engineering. You need statistics, engineering, and classic ML knowledge to do experiment tracking, evaluation, and dataset curation.

This chapter covers both how to write effective prompts and how to defend your applications against prompt attacks. Before diving into all the fun applications you can build with prompts, let’s first start with the fundamentals, including what exactly a prompt is and prompt engineering best practices.

Introduction to Prompting

A prompt is an instruction given to a model to perform a task. The task can be as simple as answering a question, such as “Who invented the number zero?” It can also be more complex, such as asking the model to research competitors for your product idea, build a website from scratch, or analyze your data.

A prompt generally consists of one or more of the following parts:

Task description
What you want the model to do, including the role you want the model to play and the output format.

Example(s) of how to do this task
For example, if you want the model to detect toxicity in text, you might provide a few examples of what toxicity and non-toxicity look like.

The task
The concrete task you want the model to do, such as the question to answer or the book to summarize.

Figure 5-1 shows a very simple prompt that one might use for an NER (named-entity recognition) task.

Task description
Given a text, extract all entities. Output only the list of extracted entities, separated by commas, and nothing else.

Example
Text: "Brave New World is a dystopian novel written by Aldous Huxley, first published in 1932."
Entities: Brave New World, Aldous Huxley

The task
Text: ${THE TEXT THAT YOU WANT TO EXTRACT ENTITIES FROM}
Entities:

Figure 5-1. A simple prompt for NER.

For prompting to work, the model has to be able to follow instructions. If a model is bad at it, it doesn’t matter how good your prompt is, the model won’t be able to
