---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 118
section-title: Tools
source-location: pages 302-304
previous-section: AI Space/normalized/pdf/ai-engineering/sections/117-agent-overview.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/119-planning.md
classification: reusable-knowledge-candidate
---
# Tools

11 A complaint in the early days of agents is that agents are only good for burning through your API credits.
5. Invoke SQL query generation to generate the queries for past marketing cam‐
paigns.
6. Invoke SQL query execution.
7. Reason that this new information is sufficient to help predict future sales. It then
generates a projection.
8. Reason that the task has been successfully completed.
Compared to non-agent use cases, agents typically require more powerful models for
two reasons:
• Compound mistakes: an agent often needs to perform multiple steps to accom‐
plish a task, and the overall accuracy decreases as the number of steps increases.
If the model’s accuracy is 95% per step, over 10 steps, the accuracy will drop to
60%, and over 100 steps, the accuracy will be only 0.6%.
• Higher stakes: with access to tools, agents are capable of performing more
impactful tasks, but any failure could have more severe consequences.
A task that requires many steps can take time and money to run. 11 However, if agents
can be autonomous, they can save a lot of human time, making their costs worth‐
while.
Given an environment, the success of an agent in an environment depends on the
tool inventory it has access to and the strength of its AI planner. Let’s start by looking
into different kinds of tools a model can use.
Tools
A system doesn’t need access to external tools to be an agent. However, without
external tools, the agent’s capabilities would be limited. By itself, a model can typi‐
cally perform one action—for example, an LLM can generate text, and an image gen‐
erator can generate images. External tools make an agent vastly more capable.
Tools help an agent to both perceive the environment and act upon it. Actions that
allow an agent to perceive the environment are read-only actions , whereas actions
that allow an agent to act upon the environment are write actions.
This section gives an overview of external tools. How tools can be used will be dis‐
cussed in “Planning” on page 281 .
The set of tools an agent has access to is its tool inventory. Since an agent’s tool
inventory determines what an agent can do, it’s important to think through what and
278 | Chapter 6: RAG and Agents

how many tools to give an agent. More tools give an agent more capabilities. How‐
ever, the more tools there are, the more challenging it is to understand and utilize
them well. Experimentation is necessary to find the right set of tools, as discussed in
“Tool selection” on page 295 .
Depending on the agent’s environment, there are many possible tools. Here are three
categories of tools that you might want to consider: knowledge augmentation (i.e.,
context construction), capability extension, and tools that let your agent act upon its
environment.
Knowledge augmentation
I hope that this book, so far, has convinced you of the importance of having the rele‐
vant context for a model’s response quality. An important category of tools includes
those that help augment your agent’s knowledge of your agent. Some of them have
already been discussed: text retriever, image retriever, and SQL executor. Other
potential tools include internal people search, an inventory API that returns the sta‐
tus of different products, Slack retrieval, an email reader, etc.
Many such tools augment a model with your organization’s private processes and
information. However, tools can also give models access to public information, espe‐
cially from the internet.
Web browsing was among the earliest and most anticipated capabilities to be incor‐
porated into chatbots like ChatGPT. Web browsing prevents a model from going
stale. A model goes stale when the data it was trained on becomes outdated. If the
model’s training data was cut off last week, it won’t be able to answer questions that
require information from this week unless this information is provided in the con‐
text. Without web browsing, a model won’t be able to tell you about the weather,
news, upcoming events, stock prices, flight status, etc.
I use web browsing as an umbrella term to cover all tools that access the internet,
including web browsers and specific APIs such as search APIs, news APIs, GitHub
APIs, or social media APIs such as those of X, LinkedIn, and Reddit.
While web browsing allows your agent to reference up-to-date information to gener‐
ate better responses and reduce hallucinations, it can also open up your agent to the
cesspools of the internet. Select your Internet APIs with care.
Capability extension
The second category of tools to consider are those that address the inherent limita‐
tions of AI models. They are easy ways to give your model a performance boost. For
example, AI models are notorious for being bad at math. If you ask a model what is
199,999 divided by 292, the model will likely fail. However, this calculation is trivial if
Agents | 279

the model has access to a calculator. Instead of trying to train the model to be good at
arithmetic, it’s a lot more resource-efficient to just give the model access to a tool.
Other simple tools that can significantly boost a model’s capability include a calen‐
dar, timezone converter, unit converter (e.g., from lbs to kg), and translator that can
translate to and from the languages that the model isn’t good at.
More complex but powerful tools are code interpreters. Instead of training a model to
understand code, you can give it access to a code interpreter so that it can execute a
piece of code, return the results, or analyze the code’s failures. This capability lets
your agents act as coding assistants, data analysts, and even research assistants that
can write code to run experiments and report results. However, automated code exe‐
cution comes with the risk of code injection attacks, as discussed in “Defensive
Prompt Engineering” on page 235. Proper security measurements are crucial to keep
you and your users safe.
External tools can make a text-only or image-only model multimodal. For example, a
model that can generate only texts can leverage a text-to-image model as a tool,
allowing it to generate both texts and images. Given a text request, the agent’s AI
planner decides whether to invoke text generation, image generation, or both. This is
how ChatGPT can generate both text and images—it uses DALL-E as its image gen‐
erator. Agents can also use a code interpreter to generate charts and graphs, a LaTeX
compiler to render math equations, or a browser to render web pages from HTML
code.
Similarly, a model that can process only text inputs can use an image captioning tool
to process images and a transcription tool to process audio. It can use an OCR (opti‐
cal character recognition) tool to read PDFs.
Tool use can significantly boost a model’s performance compared to just prompting or
even finetuning. Chameleon (Lu et al., 2023) shows that a GPT-4-powered agent, aug‐
mented with a set of 13 tools, can outperform GPT-4 alone on several benchmarks.
Examples of tools this agent used are knowledge retrieval, a query generator, an
image captioner, a text detector, and Bing search.
On ScienceQA, a science question answering benchmark, Chameleon improves the
best published few-shot result by 11.37%. On TabMWP (Tabular Math Word Prob‐
lems) (Lu et al., 2022), a benchmark involving tabular math questions, Chameleon
improves the accuracy by 17%.
Write actions
So far, we’ve discussed read-only actions that allow a model to read from its data
sources. But tools can also perform write actions, making changes to the data sources.
A SQL executor can retrieve a data table (read) but can also change or delete the table
280 | Chapter 6: RAG and Agents
