---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 018
section-title: From Foundation Models to AI Engineering
source-location: pages 36-39
previous-section: AI Space/normalized/pdf/ai-engineering/sections/017-from-large-language-models-to-foundation-models.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/019-foundation-model-use-cases.md
classification: reusable-knowledge-candidate
---
# From Foundation Models to AI Engineering

Adapting an existing powerful model to your task is generally a lot easier than build‐
ing a model for your task from scratch—for example, ten examples and one weekend
versus 1 million examples and six months. Foundation models make it cheaper to
develop AI applications and reduce time to market. Exactly how much data is needed
to adapt a model depends on what technique you use. This book will also touch on
this question when discussing each technique. However, there are still many benefits
to task-specific models, for example, they might be a lot smaller, making them faster
and cheaper to use.
Whether to build your own model or leverage an existing one is a classic buy-orbuild question that teams will have to answer for themselves. Discussions throughout
the book can help with that decision.
From Foundation Models to AI Engineering
AI engineering  refers to the process of building applications on top of foundation
models. People have been building AI applications for over a decade—a process often
known as ML engineering or MLOps (short for ML operations). Why do we talk
about AI engineering now?
If traditional ML engineering involves developing ML models, AI engineering lever‐
ages existing ones. The availability and accessibility of powerful foundation models
lead to three factors that, together, create ideal conditions for the rapid growth of AI
engineering as a discipline:
Factor 1: General-purpose AI capabilities
Foundation models are powerful not just because they can do existing tasks bet‐
ter. They are also powerful because they can do more tasks. Applications previ‐
ously thought impossible are now possible, and applications not thought of
before are emerging. Even applications not thought possible today might be pos‐
sible tomorrow. This makes AI more useful for more aspects of life, vastly
increasing both the user base and the demand for AI applications.
For example, since AI can now write as well as humans, sometimes even better,
AI can automate or partially automate every task that requires communication,
which is pretty much everything. AI is used to write emails, respond to customer
requests, and explain complex contracts. Anyone with a computer has access to
tools that can instantly generate customized, high-quality images and videos to
help create marketing materials, edit professional headshots, visualize art con‐
cepts, illustrate books, and so on. AI can even be used to synthesize training data,
develop algorithms, and write code, all of which will help train even more power‐
ful models in the future.
12 | Chapter 1: Introduction to Building AI Applications with Foundation Models

9 For comparison, the entire US expenditures for public elementary and secondary schools are around $900
billion, only nine times the investments in AI in the US.
Factor 2: Increased AI investments
The success of ChatGPT prompted a sharp increase in investments in AI, both
from venture capitalists and enterprises. As AI applications become cheaper to
build and faster to go to market, returns on investment for AI become more
attractive. Companies rush to incorporate AI into their products and processes.
Matt Ross, a senior manager of applied research at Scribd, told me that the esti‐
mated AI cost for his use cases has gone down two orders of magnitude from
April 2022 to April 2023.
Goldman Sachs Research estimated that AI investment could approach $100 bil‐
lion in the US and $200 billion globally by 2025.9 AI is often mentioned as a com‐
petitive advantage. FactSet found that one in three S&P 500 companies
mentioned AI in their earnings calls for the second quarter of 2023, three times
more than did so the year earlier. Figure 1-5 shows the number of S&P 500 com‐
panies that mentioned AI in their earning calls from 2018 to 2023.
Figure 1-5. The number of S&P 500 companies that mention AI in their earnings
calls reached a record high in 2023. Data from FactSet.
According to WallStreetZen, companies that mentioned AI in their earning calls
saw their stock price increase more than those that didn’t: an average of a 4.6%
The Rise of AI Engineering | 13

[Visual content extracted via GLM-OCR]

Factor 2: Increased AI investments

The success of ChatGPT prompted a sharp increase in investments in AI, both from venture capitalists and enterprises. As AI applications become cheaper to build and faster to go to market, returns on investment for AI become more attractive. Companies rush to incorporate AI into their products and processes. Matt Ross, a senior manager of applied research at Scribd, told me that the estimated AI cost for his use cases has gone down two orders of magnitude from April 2022 to April 2023.

Goldman Sachs Research estimated that AI investment could approach $100 billion in the US and $200 billion globally by 2025. AI is often mentioned as a competitive advantage. FactSet found that one in three S&P 500 companies mentioned AI in their earnings calls for the second quarter of 2023, three times more than did so the year earlier. Figure 1-5 shows the number of S&P 500 companies that mentioned AI in their earning calls from 2018 to 2023.

Figure 1-5. The number of S&P 500 companies that mention AI in their earnings calls reached a record high in 2023. Data from FactSet.

According to WallStreetZen, companies that mentioned AI in their earning calls saw their stock price increase more than those that didn’t: an average of a 4.6%

9 For comparison, the entire US expenditures for public elementary and secondary schools are around $900 billion, only nine times the investments in AI in the US.

increase compared to 2.4% . It’s unclear whether it’s causation (AI makes these
companies more successful) or correlation (companies are successful because
they are quick to adapt to new technologies).
Factor 3: Low entrance barrier to building AI applications
The model as a service approach popularized by OpenAI and other model pro‐
viders makes it easier to leverage AI to build applications. In this approach, mod‐
els are exposed via APIs that receive user queries and return model outputs.
Without these APIs, using an AI model requires the infrastructure to host and
serve this model. These APIs give you access to powerful models via single API
calls.
Not only that, AI also makes it possible to build applications with minimal cod‐
ing. First, AI can write code for you, allowing people without a software engi‐
neering background to quickly turn their ideas into code and put them in front
of their users. Second, you can work with these models in plain English instead of
having to use a programming language. Anyone, and I mean anyone, can now
develop AI applications.
Because of the resources it takes to develop foundation models, this process is possi‐
ble only for big corporations (Google, Meta, Microsoft, Baidu, Tencent), govern‐
ments ( Japan, the UAE), and ambitious, well-funded startups (OpenAI, Anthropic,
Mistral). In a September 2022 interview, Sam Altman, CEO of OpenAI , said that the
biggest opportunity for the vast majority of people will be to adapt these models for
specific applications.
The world is quick to embrace this opportunity. AI engineering has rapidly emerged
as one of the fastest, and quite possibly the fastest-growing, engineering discipline.
Tools for AI engineering are gaining traction faster than any previous software engi‐
neering tools. Within just two years, four open source AI engineering tools
(AutoGPT, Stable Diffusion eb UI, LangChain, Ollama) have already garnered more
stars on GitHub than Bitcoin. They are on track to surpass even the most popular
web development frameworks, including React and Vue, in star count. Figure 1-6
shows the GitHub star growth of AI engineering tools compared to Bitcoin, Vue, and
React.
A LinkedIn survey from August 2023 shows that the number of professionals adding
terms like “Generative AI,” “ChatGPT,” “Prompt Engineering,” and “Prompt Craft‐
ing” to their profile increased on average 75% each month . ComputerWorld declared
that “teaching AI to behave is the fastest-growing career skill”.
14 | Chapter 1: Introduction to Building AI Applications with Foundation Models

Figure 1-6. Open source AI engineering tools are growing faster than any other software
engineering tools, according to their GitHub star counts.
Why the Term “AI Engineering?”
Many terms are being used to describe the process of building applications on top of
foundation models, including ML engineering, MLOps, AIOps, LLMOps, etc. Why
did I choose to go with AI engineering for this book?
I didn’t go with the term ML engineering because, as discussed in “AI Engineering
Versus ML Engineering” on page 39, working with foundation models differs from
working with traditional ML models in several important aspects. The term ML engi‐
neering won’t be sufficient to capture this differentiation. However, ML engineering
is a great term to encompass both processes.
I didn’t go with all the terms that end with “Ops” because, while there are operational
components of the process, the focus is more on tweaking (engineering) foundation
models to do what you want.
Finally, I surveyed 20 people who were developing applications on top of foundation
models about what term they would use to describe what they were doing. Most peo‐
ple preferred AI engineering. I decided to go with the people.
The Rise of AI Engineering | 15

[Visual content extracted via GLM-OCR]

Why the Term “AI Engineering?”

Many terms are being used to describe the process of building applications on top of foundation models, including ML engineering, MLOps, AIOps, LLMOps, etc. Why did I choose to go with AI engineering for this book?

I didn’t go with the term ML engineering because, as discussed in “AI Engineering Versus ML Engineering” on page 39, working with foundation models differs from working with traditional ML models in several important aspects. The term ML engineering won’t be sufficient to capture this differentiation. However, ML engineering is a great term to encompass both processes.

I didn’t go with all the terms that end with “Ops” because, while there are operational components of the process, the focus is more on tweaking (engineering) foundation models to do what you want.

Finally, I surveyed 20 people who were developing applications on top of foundation models about what term they would use to describe what they were doing. Most people preferred AI engineering. I decided to go with the people.
