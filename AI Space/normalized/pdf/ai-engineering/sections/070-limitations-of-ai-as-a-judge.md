---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 070
section-title: Limitations of AI as a Judge
source-location: pages 165-168
previous-section: AI Space/normalized/pdf/ai-engineering/sections/069-how-to-use-ai-as-a-judge.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/071-what-models-can-act-as-judges.md
classification: reusable-knowledge-candidate
---
# Limitations of AI as a Judge

If the generated answer contradicts the ground truth answer, it will
receive a low score of 1-2.
For example, for the question "Is the sky blue?" the ground truth answer
is "Yes, the sky is blue." and the generated answer is "No, the sky is
not blue."
In this example, the generated answer contradicts the ground truth answer
by stating that the sky is not blue, when in fact it is blue.
This inconsistency would result in a low score of 1–2, and the reason for
the low score would reflect the contradiction between the generated
answer and the ground truth answer.
Figure 3-8 shows an example of an AI judge that evaluates the quality of an answer
when given the question.
Figure 3-8. An example of an AI judge that evaluates the quality of an answer given a
question.
An AI judge is not just a model—it’s a system that includes both a model and a
prompt. Altering the model, the prompt, or the model’s sampling parameters results
in a different judge.
Limitations of AI as a Judge
Despite the many advantages of AI as a judge, many teams are hesitant to adopt this
approach. Using AI to evaluate AI seems tautological. The probabilistic nature of AI
makes it seem too unreliable to act as an evaluator. AI judges can potentially intro‐
duce nontrivial costs and latency to an application. Given these limitations, some
teams see AI as a judge as a fallback option when they don’t have any other way of
evaluating their systems, especially in production.
AI as a Judge | 141

[Visual content extracted via GLM-OCR]

If the generated answer contradicts the ground truth answer, it will receive a low score of 1-2.

For example, for the question "Is the sky blue?" the ground truth answer is "Yes, the sky is blue." and the generated answer is "No, the sky is not blue."

In this example, the generated answer contradicts the ground truth answer by stating that the sky is not blue, when in fact it is blue.

This inconsistency would result in a low score of 1-2, and the reason for the low score would reflect the contradiction between the generated answer and the ground truth answer.

Figure 3-8 shows an example of an AI judge that evaluates the quality of an answer when given the question.

An AI judge is not just a model—it’s a system that includes both a model and a prompt. Altering the model, the prompt, or the model’s sampling parameters results in a different judge.

Limitations of AI as a Judge

Despite the many advantages of AI as a judge, many teams are hesitant to adopt this approach. Using AI to evaluate AI seems tautological. The probabilistic nature of AI makes it seem too unreliable to act as an evaluator. AI judges can potentially introduce nontrivial costs and latency to an application. Given these limitations, some teams see AI as a judge as a fallback option when they don’t have any other way of evaluating their systems, especially in production.

Inconsistency
For an evaluation method to be trustworthy, its results should be consistent. Yet AI
judges, like all AI applications, are probabilistic. The same judge, on the same input,
can output different scores if prompted differently. Even the same judge, prompted
with the same instruction, can output different scores if run twice. This inconsistency
makes it hard to reproduce or trust evaluation results.
It’s possible to get an AI judge to be more consistent. Chapter 2 discusses how to do
so with sampling variables. Zheng et al. (2023)  showed that including evaluation
examples in the prompt can increase the consistency of GPT-4 from 65% to 77.5%.
However, they acknowledged that high consistency may not imply high accuracy—
the judge might consistently make the same mistakes. On top of that, including more
examples makes prompts longer, and longer prompts mean higher inference costs. In
Zheng et al.’s experiment, including more examples in their prompts caused their
GPT-4 spending to quadruple.
Criteria ambiguity
Unlike many human-designed metrics, AI as a judge metrics aren’t standardized,
making it easy to misinterpret and misuse them. As of this writing, the open source
tools MLflow, Ragas, and LlamaIndex all have the built-in criterion faithfulness to
measure how faithful a generated output is to the given context, but their instructions
and scoring systems are all different. As shown in Table 3-4, MLflow uses a scoring
system from 1 to 5, Ragas uses 0 and 1, whereas LlamaIndex’s prompt asks the judge
to output YES and NO.
Table 3-4. Different tools can have very difficult default prompts for the same criteria.
Tool Prompt
[partially omitted for brevity]
Scoring
system
MLflow Faithfulness is only evaluated with the provided output and pro
vided context, please ignore the provided input entirely when
scoring faithfulness. Faithfulness assesses how much of the
provided output is factually consistent with the provided con
text.…
Faithfulness: Below are the details for different scores:
- Score 1: None of the claims in the output can be inferred
from the provided  context.
- Score 2: …
1–5
Ragas Your task is to judge the faithfulness of a series of state
ments based on a given context. For each statement you must
return verdict as 1 if the statement  can be verified based on
the context or 0 if the statement can not be verified based on
the context.
0 and 1
142 | Chapter 3: Evaluation Methodology

Tool Prompt
[partially omitted for brevity]
Scoring
system
LlamaIndex Please tell if a given piece of information is supported by the
context.
You need to answer with either YES or NO.
Answer YES if any of the context supports  the information, even
if most of the context is unrelated. Some examples are provided
below.
Information: Apple pie is generally double-crusted.
Context: An apple pie is a fruit pie… It is generally doublecrusted, with pastry both above and below the filling ...
Answer: YES
YES and
NO
The faithfulness scores outputted by these three tools won’t be comparable. If, given a
(context, answer) pair, MLflow gives a faithfulness score of 3, Ragas outputs 1, and
LlamaIndex outputs NO, which score would you use?
An application evolves over time, but the way it’s evaluated ideally should be fixed.
This way, evaluation metrics can be used to monitor the application’s changes. How‐
ever, AI judges are also AI applications, which means that they also can change over
time.
Imagine that last month, your application’s coherence score was 90%, and this
month, this score is 92%. Does this mean that your application’s coherence has
improved? It’s hard to answer this question unless you know for sure that the AI
judges used in both cases are exactly the same. What if the judge’s prompt this month
is different from the one last month? Maybe you switched to a slightly betterperforming prompt or a coworker fixed a typo in last month’s prompt, and the judge
this month is more lenient.
This can become especially confusing if the application and the AI judge are man‐
aged by different teams. The AI judge team might change the judges without inform‐
ing the application team. As a result, the application team might mistakenly attribute
the changes in the evaluation results to changes in the application, rather than the
changes in the judges.
Do not trust any AI judge if you can’t see the model and the
prompt used for the judge.
AI as a Judge | 143

[Visual content extracted via GLM-OCR]

The faithfulness scores outputted by these three tools won’t be comparable. If, given a (context, answer) pair, MLflow gives a faithfulness score of 3, Ragas outputs 1, and LlamaIndex outputs NO, which score would you use?

An application evolves over time, but the way it’s evaluated ideally should be fixed. This way, evaluation metrics can be used to monitor the application’s changes. However, AI judges are also AI applications, which means that they also can change over time.

Imagine that last month, your application’s coherence score was 90%, and this month, this score is 92%. Does this mean that your application’s coherence has improved? It’s hard to answer this question unless you know for sure that the AI judges used in both cases are exactly the same. What if the judge’s prompt this month is different from the one last month? Maybe you switched to a slightly better-performing prompt or a coworker fixed a typo in last month’s prompt, and the judge this month is more lenient.

This can become especially confusing if the application and the AI judge are managed by different teams. The AI judge team might change the judges without informing the application team. As a result, the application team might mistakenly attribute the changes in the evaluation results to changes in the application, rather than the changes in the judges.

Do not trust any AI judge if you can’t see the model and the prompt used for the judge.

17 In some cases, evaluation can take up the majority of the budget, even more than response generation.
18 Spot-checking is the same as sampling.
Evaluation methods take time to standardize. As the field evolves and more guard‐
rails are introduced, I hope that future AI judges will become a lot more standardized
and reliable.
Increased costs and latency
You can use AI judges to evaluate applications both during experimentation and in
production. Many teams use AI judges as guardrails in production to reduce risks,
showing users only generated responses deemed good by the AI judge.
Using powerful models to evaluate responses can be expensive. If you use GPT-4 to
both generate and evaluate responses, you’ll do twice as many GPT-4 calls, approxi‐
mately doubling your API costs. If you have three evaluation prompts because you
want to evaluate three criteria—say, overall response quality, factual consistency, and
toxicity—you’ll increase your number of API calls four times. 17
You can reduce costs by using weaker models as the judges (see “What Models Can
Act as Judges?” on page 145 .) You can also reduce costs with spot-checking: evaluating
only a subset of responses. 18 Spot-checking means you might fail to catch some fail‐
ures. The larger the percentage of samples you evaluate, the more confidence you will
have in your evaluation results, but also the higher the costs. Finding the right bal‐
ance between cost and confidence might take trial and error. This process is dis‐
cussed further in Chapter 4. All things considered, AI judges are much cheaper than
human evaluators.
Implementing AI judges in your production pipeline can add latency. If you evaluate
responses before returning them to users, you face a trade-off: reduced risk but
increased latency. The added latency might make this option a nonstarter for applica‐
tions with strict latency requirements.
Biases of AI as a judge
Human evaluators have biases, and so do AI judges. Different AI judges have differ‐
ent biases. This section will discuss some of the common ones. Being aware of your
AI judges’ biases helps you interpret their scores correctly and even mitigate these
biases.
AI judges tend to have self-bias, where a model favors its own responses over the
responses generated by other models. The same mechanism that helps a model com‐
pute the most likely response to generate will also give this response a high score. In
144 | Chapter 3: Evaluation Methodology
