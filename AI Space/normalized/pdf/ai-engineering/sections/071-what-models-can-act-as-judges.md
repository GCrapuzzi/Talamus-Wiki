---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 071
section-title: What Models Can Act as Judges?
source-location: pages 169-171
previous-section: AI Space/normalized/pdf/ai-engineering/sections/070-limitations-of-ai-as-a-judge.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/072-ranking-models-with-comparative-evaluation.md
classification: reusable-knowledge-candidate
---
# What Models Can Act as Judges?

19 Saito et al. (2023) found that humans tend to favor longer responses too, but to a much lesser extent.
Zheng et al.’s 2023 experiment , GPT-4 favors itself with a 10% higher win rate, while
Claude-v1 favors itself with a 25% higher win rate.
Many AI models have first-position bias. An AI judge may favor the first answer in a
pairwise comparison or the first in a list of options. This can be mitigated by repeat‐
ing the same test multiple times with different orderings or with carefully crafted
prompts. The position bias of AI is the opposite of that of humans. Humans tend to
favor the answer they see last, which is called recency bias.
Some AI judges have verbosity bias , favoring lengthier answers, regardless of their
quality. Wu and Aji (2023)  found that both GPT-4 and Claude-1 prefer longer
responses (~100 words) with factual errors over shorter, correct responses (~50
words). Saito et al. (2023) studied this bias for creative tasks and found that when the
length difference is large enough (e.g., one response is twice as long as the other), the
judge almost always prefers the longer one. 19 Both Zheng et al. (2023) and Saito et al.
(2023), however, discovered that GPT-4 is less prone to this bias than GPT-3.5, sug‐
gesting that this bias might go away as models become stronger.
On top of all these biases, AI judges have the same limitations as all AI applications,
including privacy and IP. If you use a proprietary model as your judge, you’d need to
send your data to this model. If the model provider doesn’t disclose their training
data, you won’t know for sure if the judge is commercially safe to use.
Despite the limitations of the AI as a judge approach, its many advantages make me
believe that its adoption will continue to grow. However, AI judges should be supple‐
mented with exact evaluation methods and/or human evaluation.
What Models Can Act as Judges?
The judge can either be stronger, weaker, or the same as the model being judged.
Each scenario has its pros and cons.
At first glance, a stronger judge makes sense. Shouldn’t the exam grader be more
knowledgeable than the exam taker? Not only can stronger models make better judg‐
ments, but they can also help improve weaker models by guiding them to generate
better responses.
You might wonder: if you already have access to the stronger model, why bother
using a weaker model to generate responses? The answer is cost and latency. You
might not have the budget to use the stronger model to generate all responses, so you
use it to evaluate a subset of responses. For example, you may use a cheap in-house
model to generate responses and GPT-4 to evaluate 1% of the responses.
AI as a Judge | 145

20 This technique is sometimes referred to as self-critique or self-ask.
The stronger model also might be too slow for your application. You can use a fast
model to generate responses while the stronger, but slower, model does evaluation in
the background. If the strong model thinks that the weak model’s response is bad,
remedy actions might be taken, such as updating the response with that of the strong
model. Note that the opposite pattern is also common. You use a strong model to
generate responses, with a weak model running in the background to do evaluation.
Using the stronger model as a judge leaves us with two challenges. First, the strongest
model will be left with no eligible judge. Second, we need an alternative evaluation
method to determine which model is the strongest.
Using a model to judge itself, self-evaluation or self-critique, sounds like cheating,
especially because of self-bias. However, self-evaluation can be great for sanity
checks. If a model thinks its own response is incorrect, the model might not be that
reliable. Beyond sanity checks, asking a model to evaluate itself can nudge a model to
revise and improve its responses ( Press et al., 2022; Gou et al., 2023; Valmeekamet et
al., 2023).20 This example shows what self-evaluation might look like:
Prompt [from user]: What’s 10+3?
First response [from AI]: 30
Self-critique [from AI]: Is this answer correct?
Final response [from AI]: No it’s not. The correct answer is 13.
One open question is whether the judge can be weaker than the model being judged.
Some argue that judging is an easier task than generating. Anyone can have an opin‐
ion about whether a song is good, but not everyone can write a song. Weaker models
should be able to judge the outputs of stronger models.
Zheng et al. (2023) found that stronger models are better correlated to human prefer‐
ence, which makes people opt for the strongest models they can afford. However, this
experiment was limited to general-purpose judges. One research direction that I’m
excited about is small, specialized judges. Specialized judges are trained to make spe‐
cific judgments, using specific criteria and following specific scoring systems. A
small, specialized judge can be more reliable than larger, general-purpose judges for
specific judgments.
146 | Chapter 3: Evaluation Methodology

21 The BLEURT score range is confusing. It’s approximately between -2.5 and 1.0. This highlights the challenge
of criteria ambiguity with AI judges: the score range can be arbitrary.
Because there are many possible ways to use AI judges, there are many possible speci‐
alized AI judges. Here, I’ll go over examples of three specialized judges: reward mod‐
els, reference-based judges, and preference models:
Reward model
A reward model takes in a (prompt, response) pair and scores how good the
response is given the prompt. Reward models have been successfully used in
RLHF for many years. Cappy is an example of a reward model developed by
Google (2023). Given a pair of (prompt, response), Cappy produces a score
between 0 and 1, indicating how correct the response is. Cappy is a lightweight
scorer with 360 million parameters, much smaller than general-purpose founda‐
tion models.
Reference-based judge
A reference-based judge evaluates the generated response with respect to one or
more reference responses. This judge can output a similarity score or a quality
score (how good the generated response is compared to the reference responses).
For example, BLEURT ( Sellam et al., 2020 ) takes in a (candidate response, refer‐
ence response) pair and outputs a similarity score between the candidate and ref‐
erence response. 21 Prometheus ( Kim et al., 2023 ) takes in (prompt, generated
response, reference response, scoring rubric) and outputs a quality score between
1 and 5, assuming that the reference response gets a 5.
Preference model
A preference model takes in (prompt, response 1, response 2) as input and out‐
puts which of the two responses is better (preferred by users) for the given
prompt. This is perhaps one of the more exciting directions for specialized
judges. Being able to predict human preference opens up many possibilities. As
discussed in Chapter 2 , preference data is essential for aligning AI models to
human preference, and it’s challenging and expensive to obtain. Having a good
human preference predictor can generally make evaluation easier and models
safer to use. There have been many initiatives in building preference models,
including PandaLM ( Wang et al., 2023 ) and JudgeLM ( Zhu et al., 2023 ).
Figure 3-9 shows an example of how PandaLM works. It not only outputs which
response is better but also explains its rationale.
AI as a Judge | 147
