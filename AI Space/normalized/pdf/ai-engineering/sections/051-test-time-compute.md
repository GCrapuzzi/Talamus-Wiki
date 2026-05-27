---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 051
section-title: Test Time Compute
source-location: pages 120-122
previous-section: AI Space/normalized/pdf/ai-engineering/sections/050-sampling-strategies.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/052-structured-outputs.md
classification: reusable-knowledge-candidate
---
# Test Time Compute

29 There are things you can do to reduce the cost of generating multiple outputs for the same input. For exam‐
ple, the input might only be processed once and reused for all outputs.
Test Time Compute
The last section discussed how a model might sample the next token. This section
discusses how a model might sample the whole output.
One simple way to improve a model’s response quality is test time compute: instead of
generating only one response per query, you generate multiple responses to increase
the chance of good responses. One way to do test time compute is the best of N tech‐
nique discussed earlier in this chapter—you randomly generate multiple outputs and
pick one that works best. However, you can also be more strategic about how to gen‐
erate multiple outputs. For example, instead of generating all outputs independently,
which might include many less promising candidates, you can use beam search  to
generate a fixed number of most promising candidates (the beam) at each step of
sequence generation.
A simple strategy to increase the effectiveness of test time compute is to increase the
diversity of the outputs, because a more diverse set of options is more likely to yield
better candidates. If you use the same model to generate different options, it’s often a
good practice to vary the model’s sampling variables to diversify its outputs.
Although you can usually expect some model performance improvement by sam‐
pling multiple outputs, it’s expensive. On average, generating two outputs costs
approximately twice as much as generating one.29
I use the term test time compute  to be consistent with the existing
literature, even though several early reviewers protested that this
term is confusing. In AI research, test time is typically used to refer
to inference because researchers mostly only do inference to test a
model. However, this technique can be applied to models in pro‐
duction in general. It’s test time compute because the number of
outputs you can sample is determined by how much compute you
can allocate to each inference call.
To pick the best output, you can either show users multiple outputs and let them
choose the one that works best for them, or you can devise a method to select the best
one. One selection method is to pick the output with the highest probability. A lan‐
guage model’s output is a sequence of tokens, and each token has a probability com‐
puted by the model. The probability of an output is the product of the probabilities of
all tokens in the output.
96 | Chapter 2: Understanding Foundation Models

[Visual content extracted via GLM-OCR]

Test Time Compute

The last section discussed how a model might sample the next token. This section discusses how a model might sample the whole output.

One simple way to improve a model’s response quality is test time compute: instead of generating only one response per query, you generate multiple responses to increase the chance of good responses. One way to do test time compute is the best of N technique discussed earlier in this chapter—you randomly generate multiple outputs and pick one that works best. However, you can also be more strategic about how to generate multiple outputs. For example, instead of generating all outputs independently, which might include many less promising candidates, you can use beam search to generate a fixed number of most promising candidates (the beam) at each step of sequence generation.

A simple strategy to increase the effectiveness of test time compute is to increase the diversity of the outputs, because a more diverse set of options is more likely to yield better candidates. If you use the same model to generate different options, it’s often a good practice to vary the model’s sampling variables to diversify its outputs.

Although you can usually expect some model performance improvement by sampling multiple outputs, it’s expensive. On average, generating two outputs costs approximately twice as much as generating one.

I use the term test time compute to be consistent with the existing literature, even though several early reviewers protested that this term is confusing. In AI research, test time is typically used to refer to inference because researchers mostly only do inference to test a model. However, this technique can be applied to models in production in general. It’s test time compute because the number of outputs you can sample is determined by how much compute you can allocate to each inference call.

To pick the best output, you can either show users multiple outputs and let them choose the one that works best for them, or you can devise a method to select the best one. One selection method is to pick the output with the highest probability. A language model’s output is a sequence of tokens, and each token has a probability computed by the model. The probability of an output is the product of the probabilities of all tokens in the output.

29 There are things you can do to reduce the cost of generating multiple outputs for the same input. For example, the input might only be processed once and reused for all outputs.

30 As of this writing, in the OpenAI API, you can set the parameter best_of to a specific value, say 10, to ask
OpenAI models to return the output with the highest average logprob out of 10 different outputs.
Consider the sequence of tokens [“I”, “love”, “food”]. If the probability for “I” is 0.2,
the probability for “love” given “I” is 0.1, and the probability for “food” given “I” and
“love” is 0.3, the sequence’s probability is: 0.2 × 0.1 × 0.3 = 0.006 . Mathemati‐
cally, this can be denoted as follows:
p(I love food) = p(I) × p(I | love) × p(food | I, love)
Remember that it’s easier to work with probabilities on a log scale. The logarithm of a
product is equal to a sum of logarithms, so the logprob of a sequence of tokens is the
sum of the logprob of all tokens in the sequence:
logprob(I love food) = logprob(I) + logprob(I | love) + logprob(food | I, love)
With summing, longer sequences are likely to have a lower total logprob (logprob
values are usually negative, because log of values between 0 and 1 is negative). To
avoid biasing toward short sequences, you can use the average logprob by dividing
the sum of a sequence by its length. After sampling multiple outputs, you pick the
one with the highest average logprob. As of this writing, this is what the OpenAI API
uses.30
Another selection method is to use a reward model to score each output, as discussed
in the previous section. Recall that both Stitch Fix and Grab pick the outputs given
high scores by their reward models or verifiers. Nextdoor found that using a reward
model was the key factor in improving their application’s performance (2023).
OpenAI also trained verifiers to help their models pick the best solutions to math
problems (Cobbe et al., 2021 ). They found that using a verifier significantly boosted
the model performance. In fact, the use of verifiers resulted in approximately the same
performance boost as a 30× model size increase.  This means that a 100-millionparameter model that uses a verifier can perform on par with a 3-billion-parameter
model that doesn’t use a verifier.
DeepMind further proves the value of test time compute, arguing that scaling test
time compute (e.g., allocating more compute to generate more outputs during infer‐
ence) can be more efficient than scaling model parameters ( Snell et al., 2024 ). The
same paper asks an interesting question: If an LLM is allowed to use a fixed but non‐
trivial amount of inference-time compute, how much can it improve its performance
on a challenging prompt?
Sampling | 97

In OpenAI’s experiment, sampling more outputs led to better performance, but only
up to a certain point. In this experiment, that point was 400 outputs. Beyond this
point, performance decreases, as shown in Figure 2-19. They hypothesized that as the
number of sampled outputs increases, the chance of finding adversarial outputs that
can fool the verifier also increases. However, a Stanford experiment showed a differ‐
ent conclusion. “Monkey Business” ( Brown et al., 2024 ) finds that the number of
problems solved often increases log-linearly as the number of samples increases from
1 to 10,000. While it’s interesting to think about whether test time compute can be
scaled indefinitely, I don’t believe anyone in production samples 400 or 10,000 differ‐
ent outputs for each input. The cost would be astronomical.
Figure 2-19. OpenAI (2021) found that sampling more outputs led to better perfor‐
mance, but only up to 400 outputs.
You can also use application-specific heuristics to select the best response. For exam‐
ple, if your application benefits from shorter responses, you can pick the shortest
candidate. If your application converts natural language to SQL queries, you can get
the model to keep on generating outputs until it generates a valid SQL query.
98 | Chapter 2: Understanding Foundation Models

[Visual content extracted via GLM-OCR]

In OpenAI’s experiment, sampling more outputs led to better performance, but only up to a certain point. In this experiment, that point was 400 outputs. Beyond this point, performance decreases, as shown in Figure 2-19. They hypothesized that as the number of sampled outputs increases, the chance of finding adversarial outputs that can fool the verifier also increases. However, a Stanford experiment showed a different conclusion. “Monkey Business” (Brown et al., 2024) finds that the number of problems solved often increases log-linearly as the number of samples increases from 1 to 10,000. While it’s interesting to think about whether test time compute can be scaled indefinitely, I don’t believe anyone in production samples 400 or 10,000 different outputs for each input. The cost would be astronomical.

Figure 2-19. OpenAI (2021) found that sampling more outputs led to better performance, but only up to 400 outputs.

You can also use application-specific heuristics to select the best response. For example, if your application benefits from shorter responses, you can pick the shortest candidate. If your application converts natural language to SQL queries, you can get the model to keep on generating outputs until it generates a valid SQL query.
