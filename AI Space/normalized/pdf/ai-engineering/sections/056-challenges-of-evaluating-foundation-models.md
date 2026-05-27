---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 056
section-title: Challenges of Evaluating Foundation Models
source-location: pages 138-141
previous-section: AI Space/normalized/pdf/ai-engineering/sections/055-chapter-3.-evaluation-methodology.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/057-understanding-language-modeling-metrics.md
classification: reusable-knowledge-candidate
---
# Challenges of Evaluating Foundation Models

2 A 2023 study by a16z showed that 6 out of 70 decision makers evaluated models by word of mouth.
3 Also known as vibe check.
4 When OpenAI’s GPT-o1 came out in September 2024, the Fields medalist Terrence Tao compared the expe‐
rience of working with this model to working with “a mediocre, but not completely incompetent, graduate
student.” He speculated that it may only take one or two further iterations until AI reaches the level of a
“competent graduate student.” In response to his assessment, many people joked that if we’re already at the
point where we need the brightest human minds to evaluate AI models, we’ll have no one qualified to evalu‐
ate future models.
Before diving into evaluation methods, it’s important to acknowledge the challenges
of evaluating foundation models. Because evaluation is difficult, many people settle
for word of mouth
 (e.g., someone says that the model X is good) or eyeballing the
results.3 This creates even more risk and slows application iteration. Instead, we need
to invest in systematic evaluation to make the results more reliable.
Since many foundation models have a language model component, this chapter will
provide a quick overview of the metrics used to evaluate language models, including
cross entropy and perplexity. These metrics are essential for guiding the training and
finetuning of language models and are frequently used in many evaluation methods.
Evaluating foundation models is especially challenging because they are open-ended,
and I’ll cover best practices for how to tackle these. Using human evaluators remains
a necessary option for many applications. However, given how slow and expensive
human annotations can be, the goal is to automate the process. This book focuses on
automatic evaluation, which includes both exact and subjective evaluation.
The rising star of subjective evaluation is AI as a judge—the approach of using AI to
evaluate AI responses. It’s subjective because the score depends on what model and
prompt the AI judge uses. While this approach is gaining rapid traction in the indus‐
try, it also invites intense opposition from those who believe that AI isn’t trustworthy
enough for this important task. I’m especially excited to go deeper into this discus‐
sion, and I hope you will be, too.
Challenges of Evaluating Foundation Models
Evaluating ML models has always been difficult. With the introduction of foundation
models, evaluation has become even more so. There are multiple reasons why evalu‐
ating foundation models is more challenging than evaluating traditional ML models.
First, the more intelligent AI models become, the harder it is to evaluate them. Most
people can tell if a first grader’s math solution is wrong. Few can do the same for a
PhD-level math solution. 4 It’s easy to tell if a book summary is bad if it’s gibberish,
but a lot harder if the summary is coherent. To validate the quality of a summary, you
might need to read the book first. This brings us to a corollary: evaluation can be so
114 | Chapter 3: Evaluation Methodology

much more time-consuming for sophisticated tasks. You can no longer evaluate a
response based on how it sounds. You’ll also need to fact-check, reason, and even
incorporate domain expertise.
Second, the open-ended nature of foundation models undermines the traditional
approach of evaluating a model against ground truths. With traditional ML, most
tasks are close-ended. For example, a classification model can only output among the
expected categories. To evaluate a classification model, you can evaluate its outputs
against the expected outputs. If the expected output is category X but the model’s
output is category Y, the model is wrong. However, for an open-ended task, for a
given input, there are so many possible correct responses. It’s impossible to curate a
comprehensive list of correct outputs to compare against.
Third, most foundation models are treated as black boxes, either because model pro‐
viders choose not to expose models’ details, or because application developers lack
the expertise to understand them. Details such as the model architecture, training
data, and the training process can reveal a lot about a model’s strengths and weak‐
nesses. Without those details, you can evaluate only a model by observing its outputs.
At the same time, publicly available evaluation benchmarks have proven to be inade‐
quate for evaluating foundation models. Ideally, evaluation benchmarks should
capture the full range of model capabilities. As AI progresses, benchmarks need to
evolve to catch up. A benchmark becomes saturated for a model once the model ach‐
ieves the perfect score. With foundation models, benchmarks are becoming saturated
fast. The benchmark GLUE (General Language Understanding Evaluation) came out
in 2018 and became saturated in just a year, necessitating the introduction of Super‐
GLUE in 2019. Similarly, NaturalInstructions (2021) was replaced by SuperNaturalInstructions (2022). MMLU (2020), a strong benchmark that many early
foundation models relied on, was largely replaced by MMLU-Pro (2024).
Last but not least, the scope of evaluation has expanded for general-purpose models.
With task-specific models, evaluation involves measuring a model’s performance on
its trained task. However, with general-purpose models, evaluation is not only about
assessing a model’s performance on known tasks but also about discovering new
tasks that the model can do, and these might include tasks that extend beyond human
capabilities. Evaluation takes on the added responsibility of exploring the potential
and limitations of AI.
Challenges of Evaluating Foundation Models | 115

5 I searched for all repositories with at least 500 stars using the keywords “LLM”, “GPT”, “generative”, and
“transformer”. I also crowdsourced for missing repositories through my website https://huyenchip.com.
The good news is that the new challenges of evaluation have prompted many new
methods and benchmarks. Figure 3-1 shows that the number of published papers on
LLM evaluation grew exponentially every month in the first half of 2023, from 2
papers a month to almost 35 papers a month.
Figure 3-1. The trend of LLMs evaluation papers over time. Image from Chang et al.
(2023).
In my own analysis of the top 1,000 AI-related repositories on GitHub , as ranked by
the number of stars, I found over 50 repositories dedicated to evaluation (as of May
2024).5 When plotting the number of evaluation repositories by their creation date,
the growth curve looks exponential, as shown in Figure 3-2.
The bad news is that despite the increased interest in evaluation, it lags behind in
terms of interest in the rest of the AI engineering pipeline. Balduzzi et al. from Deep‐
Mind noted in their paper that “developing evaluations has received little systematic
attention compared to developing algorithms.” According to the paper, experiment
results are almost exclusively used to improve algorithms and are rarely used to
improve evaluation. Recognizing the lack of investments in evaluation, Anthropic
called on policymakers to increase government funding and grants both for develop‐
ing new evaluation methodologies and analyzing the robustness of existing
evaluations.
116 | Chapter 3: Evaluation Methodology

[Visual content extracted via GLM-OCR]

The good news is that the new challenges of evaluation have prompted many new methods and benchmarks. Figure 3-1 shows that the number of published papers on LLM evaluation grew exponentially every month in the first half of 2023, from 2 papers a month to almost 35 papers a month.

Figure 3-1. The trend of LLMs evaluation papers over time. Image from Chang et al. (2023).

In my own analysis of the top 1,000 AI-related repositories on GitHub, as ranked by the number of stars, I found over 50 repositories dedicated to evaluation (as of May 2024). When plotting the number of evaluation repositories by their creation date, the growth curve looks exponential, as shown in Figure 3-2.

The bad news is that despite the increased interest in evaluation, it lags behind in terms of interest in the rest of the AI engineering pipeline. Balduzzi et al. from DeepMind noted in their paper that “developing evaluations has received little systematic attention compared to developing algorithms.” According to the paper, experiment results are almost exclusively used to improve algorithms and are rarely used to improve evaluation. Recognizing the lack of investments in evaluation, Anthropic called on policymakers to increase government funding and grants both for developing new evaluation methodologies and analyzing the robustness of existing evaluations.

5 I searched for all repositories with at least 500 stars using the keywords “LLM”, “GPT”, “generative”, and “transformer”. I also crowdsourced for missing repositories through my website https://huyenchip.com.

Figure 3-2. Number of open source evaluation repositories among the 1,000 most popu‐
lar AI repositories on GitHub.
To further demonstrate how the investment in evaluation lags behind other areas in
the AI space, the number of tools for evaluation is small compared to the number of
tools for modeling and training and AI orchestration, as shown in Figure 3-3.
Inadequate investment leads to inadequate infrastructure, making it hard for people
to carry out systematic evaluations. When asked how they are evaluating their AI
applications, many people told me that they just eyeballed the results. Many have a
small set of go-to prompts that they use to evaluate models. The process of curating
these prompts is ad hoc, usually based on the curator’s personal experience instead of
based on the application’s needs. You might be able to get away with this ad hoc
approach when getting a project off the ground, but it won’t be sufficient for applica‐
tion iteration. This book focuses on a systematic approach to evaluation.
Challenges of Evaluating Foundation Models | 117

[Visual content extracted via GLM-OCR]

To further demonstrate how the investment in evaluation lags behind other areas in the AI space, the number of tools for evaluation is small compared to the number of tools for modeling and training and AI orchestration, as shown in Figure 3-3.

Inadequate investment leads to inadequate infrastructure, making it hard for people to carry out systematic evaluations. When asked how they are evaluating their AI applications, many people told me that they just eyeballed the results. Many have a small set of go-to prompts that they use to evaluate models. The process of curating these prompts is ad hoc, usually based on the curator’s personal experience instead of based on the application’s needs. You might be able to get away with this ad hoc approach when getting a project off the ground, but it won’t be sufficient for application iteration. This book focuses on a systematic approach to evaluation.
