---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 005
section-title: What This Book Is About
source-location: pages 14-15
previous-section: AI Space/normalized/pdf/ai-engineering/sections/004-preface.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/006-what-this-book-is-not.md
classification: reusable-knowledge-candidate
---
# What This Book Is About

The familiarity and ease of use of many AI engineering techniques can mislead peo‐
ple into thinking there is nothing new to AI engineering. But while many principles
for building AI applications remain the same, the scale and improved capabilities of
AI models introduce opportunities and challenges that require new solutions.
This book covers the end-to-end process of adapting foundation models to solve realworld problems, encompassing tried-and-true techniques from other engineering
fields and techniques emerging with foundation models.
I set out to write the book because I wanted to learn, and I did learn a lot. I learned
from the projects I worked on, the papers I read, and the people I interviewed.
During the process of writing this book, I used notes from over 100 conversations
and interviews, including researchers from major AI labs (OpenAI, Google,
Anthropic, ...), framework developers (NVIDIA, Meta, Hugging Face, Anyscale,
LangChain, LlamaIndex, ...), executives and heads of AI/data at companies of differ‐
ent sizes, product managers, community researchers, and independent application
developers (see “Acknowledgments” on page xx ).
I especially learned from early readers who tested my assumptions, introduced me to
different perspectives, and exposed me to new problems and approaches. Some sec‐
tions of the book have also received thousands of comments from the community
after being shared on my blog , many giving me new perspectives or confirming a
hypothesis.
I hope that this learning process will continue for me now that the book is in your
hands, as you have experiences and perspectives that are unique to you. Please
feel free to share any feedback you might have for this book with me via X, LinkedIn,
or email at hi@huyenchip.com.
What This Book Is About
This book provides a framework for adapting foundation models, which include both
large language models (LLMs) and large multimodal models (LMMs), to specific
applications.
There are many different ways to build an application. This book outlines various
solutions and also raises questions you can ask to evaluate the best solution for your
needs. Some of the many questions that this book can help you answer are:
• Should I build this AI application?
• How do I evaluate my application? Can I use AI to evaluate AI outputs?
• What causes hallucinations? How do I detect and mitigate hallucinations?
• What are the best practices for prompt engineering?
• Why does RAG work? What are the strategies for doing RAG?
xii | Preface

3 Teaching a course on how to use TensorFlow in 2017 taught me a painful lesson about how quickly tools and
tutorials become outdated.
• What’s an agent? How do I build and evaluate an agent?
• When to finetune a model? When not to finetune a model?
• How much data do I need? How do I validate the quality of my data?
• How do I make my model faster, cheaper, and secure?
• How do I create a feedback loop to improve my application continually?
The book will also help you navigate the overwhelming AI landscape: types of mod‐
els, evaluation benchmarks, and a seemingly infinite number of use cases and appli‐
cation patterns.
The content in this book is illustrated using case studies, many of which I worked on,
backed by ample references and extensively reviewed by experts from a wide range of
backgrounds. Although the book took two years to write, it draws from my experi‐
ence working with language models and ML systems from the last decade.
Like my previous O’Reilly book, Designing Machine Learning Systems  (DMLS), this
book focuses on the fundamentals of AI engineering instead of any specific tool or
API. Tools become outdated quickly, but fundamentals should last longer.3
Reading AI Engineering (AIE) with Designing
Machine Learning Systems (DMLS)
AIE can be a companion to DMLS. DMLS focuses on building applications on top of
traditional ML models, which involves more tabular data annotations, feature engi‐
neering, and model training. AIE focuses on building applications on top of founda‐
tion models, which involves more prompt engineering, context construction, and
parameter-efficient finetuning. Both books are self-contained and modular, so you
can read either book independently.
Since foundation models are ML models, some concepts are relevant to working with
both. If a topic is relevant to AIE but has been discussed extensively in DMLS, it’ll still
be covered in this book, but to a lesser extent, with pointers to relevant resources.
Note that many topics are covered in DMLS but not in AIE, and vice versa. The first
chapter of this book also covers the differences between traditional ML engineering
and AI engineering. A real-world system often involves both traditional ML models
and foundation models, so knowledge about working with both is often necessary.
Preface | xiii
