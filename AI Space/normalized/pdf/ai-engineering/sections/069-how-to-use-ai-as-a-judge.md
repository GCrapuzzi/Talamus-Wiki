---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 069
section-title: How to Use AI as a Judge
source-location: pages 162-164
previous-section: AI Space/normalized/pdf/ai-engineering/sections/068-why-ai-as-a-judge.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/070-limitations-of-ai-as-a-judge.md
classification: reusable-knowledge-candidate
---
# How to Use AI as a Judge

evaluate the quality of the following paragraph. give it a score from 1 to 5, and explain your decision.

Another drawback of this measurement is that higher lexical similarity scores don't always mean better responses. For example, on HumanEval, a code generation benchmark, OpenAI found that BLEU scores for incorrect and correct solutions were similar. This indicates that optimizing for BLEU scores isn't the same as optimizing for functional correctness (Chen et al., 2021).

I would rate the paragraph a 4.5 out of 5.

Strengths:

1. Clarity: The paragraph clearly explains the drawback of using lexical similarity scores, providing a specific example.
2. Evidence: It effectively uses the HumanEval benchmark and OpenAI's findings to support the argument.
3. Conciseness: The paragraph is concise and directly to the point, making it easy to understand.

Areas for Improvement:

1. Flow: The transition between sentences is smooth, but the paragraph could benefit from a slightly stronger connection between the general statement and the specific example.

Figure 3-7. Not only can AI judges score, they also can explain their decisions.

How to Use AI as a Judge

There are many ways you can use AI to make judgments. For example, you can use AI to evaluate the quality of a response by itself, compare that response to reference data, or compare that response to another response. Here are naive example prompts for these three approaches:

1. Evaluate the quality of a response by itself, given the original question:

“Given the following question and answer, evaluate how good the answer is for the question. Use the score from 1 to 5.

- 1 means very bad.
- 5 means very good.

Question: [QUESTION]

Answer: [ANSWER]

Score:”

2. Compare a generated response to a reference response to evaluate whether the
generated response is the same as the reference response. This can be an alterna‐
tive approach to human-designed similarity measurements:
“Given the following question, reference answer, and generated answer,
evaluate whether this generated answer is the same as the reference answer.
Output True or False.
Question: [QUESTION]
Reference answer: [REFERENCE ANSWER]
Generated answer: [GENERATED ANSWER]”
3. Compare two generated responses and determine which one is better or predict
which one users will likely prefer. This is helpful for generating preference data
for post-training alignment (discussed in Chapter 2 ), test-time compute (dis‐
cussed in Chapter 2 ), and ranking models using comparative evaluation (dis‐
cussed in the next section):
“Given the following question and two answers, evaluate which answer is
better. Output A or B.
Question: [QUESTION]
A: [FIRST ANSWER]
B: [SECOND ANSWER]
The better answer is:”
A general-purpose AI judge can be asked to evaluate a response based on any criteria.
If you’re building a roleplaying chatbot, you might want to evaluate if a chatbot’s
response is consistent with the role users want it to play, such as “Does this response
sound like something Gandalf would say?” If you’re building an application to gener‐
ate promotional product photos, you might want to ask “From 1 to 5, how would you
rate the trustworthiness of the product in this image?” Table 3-3  shows common
built-in AI as a judge criteria offered by some AI tools.
Table 3-3. Examples of built-in AI as a judge criteria offered by some AI tools, as of
September 2024. Note that as these tools evolve, these built-in criteria will change.
AI Tools Built-in criteria
Azure AI Studio Groundedness, relevance, coherence, fluency, similarity
MLflow.metrics Faithfulness, relevance
LangChain Criteria Evaluation Conciseness, relevance, correctness, coherence, harmfulness, maliciousness, helpfulness,
controversiality, misogyny, insensitivity, criminality
Ragas Faithfulness, answer relevance
It’s essential to remember that AI as a judge criteria aren’t standardized. Azure AI
Studio’s relevance scores might be very different from MLflow’s relevance scores.
These scores depend on the judge’s underlying model and prompt.
AI as a Judge | 139

How to prompt an AI judge is similar to how to prompt any AI application. In gen‐
eral, a judge’s prompt should clearly explain the following:
1. The task the model is to perform, such as to evaluate the relevance between a
generated answer and the question.
2. The criteria the model should follow to evaluate, such as “Your primary focus
should be on determining whether the generated answer contains sufficient
information to address the given question according to the ground truth
answer”. The more detailed the instruction, the better.
3. The scoring system, which can be one of these:
• Classification, such as good/bad or relevant/irrelevant/neutral.
• Discrete numerical values, such as 1 to 5. Discrete numerical values can be
considered a special case of classification, where each class has a numerical
interpretation instead of a semantic interpretation.
• Continuous numerical values, such as between 0 and 1, e.g., when you want to
evaluate the degree of similarity.
Language models are generally better with text than with numbers.
It’s been reported that AI judges work better with classification
than with numerical scoring systems.
For numerical scoring systems, discrete scoring seems to work bet‐
ter than continuous scoring. Empirically, the wider the range for
discrete scoring, the worse the model seems to get. Typical discrete
scoring systems are between 1 and 5.
Prompts with examples have been shown to perform better. If you use a scoring sys‐
tem between 1 and 5, include examples of what a response with a score of 1, 2, 3, 4, or
5 looks like, and if possible, why a response receives a certain score. Best practices for
prompting are discussed in Chapter 5.
Here’s part of the prompt used for the criteria relevance by Azure AI Studio. It
explains the task, the criteria, the scoring system, an example of an input with a low
score, and a justification for why this input has a low score. Part of the prompt was
removed for brevity.
Your task is to score the relevance between a generated answer and the
question based on the ground truth answer in the range between 1 and 5,
and please also provide the scoring reason.
Your primary focus should be on determining whether the generated answer
contains sufficient information to address the given question according
to the ground truth answer. …
140 | Chapter 3: Evaluation Methodology

[Visual content extracted via GLM-OCR]

How to prompt an AI judge is similar to how to prompt any AI application. In general, a judge’s prompt should clearly explain the following:

1. The task the model is to perform, such as to evaluate the relevance between a generated answer and the question.

2. The criteria the model should follow to evaluate, such as “Your primary focus should be on determining whether the generated answer contains sufficient information to address the given question according to the ground truth answer”. The more detailed the instruction, the better.

3. The scoring system, which can be one of these:
   - Classification, such as good/bad or relevant/irrelevant/neutral.
   - Discrete numerical values, such as 1 to 5. Discrete numerical values can be considered a special case of classification, where each class has a numerical interpretation instead of a semantic interpretation.
   - Continuous numerical values, such as between 0 and 1, e.g., when you want to evaluate the degree of similarity.

Language models are generally better with text than with numbers. It’s been reported that AI judges work better with classification than with numerical scoring systems.

For numerical scoring systems, discrete scoring seems to work better than continuous scoring. Empirically, the wider the range for discrete scoring, the worse the model seems to get. Typical discrete scoring systems are between 1 and 5.

Prompts with examples have been shown to perform better. If you use a scoring system between 1 and 5, include examples of what a response with a score of 1, 2, 3, 4, or 5 looks like, and if possible, why a response receives a certain score. Best practices for prompting are discussed in Chapter 5.

Here’s part of the prompt used for the criteria relevance by Azure AI Studio. It explains the task, the criteria, the scoring system, an example of an input with a low score, and a justification for why this input has a low score. Part of the prompt was removed for brevity.

Your task is to score the relevance between a generated answer and the question based on the ground truth answer in the range between 1 and 5, and please also provide the scoring reason.

Your primary focus should be on determining whether the generated answer contains sufficient information to address the given question according to the ground truth answer. ...
