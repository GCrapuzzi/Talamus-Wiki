---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 050
section-title: Sampling Strategies
source-location: pages 114-119
previous-section: AI Space/normalized/pdf/ai-engineering/sections/049-sampling-fundamentals.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/051-test-time-compute.md
classification: reusable-knowledge-candidate
---
# Sampling Strategies

Figure 2-15. For each input, a language model produces a logit vector. Each logit corre‐
sponds to a token in the vocabulary.
While larger logits correspond to higher probabilities, logits don’t represent probabil‐
ities. Logits don’t sum up to one. Logits can even be negative, while probabilities have
to be non-negative. To convert logits to probabilities, a softmax layer is often used.
Let’s say the model has a vocabulary of N and the logit vector is x1, x2, ..., xN  The
probability for the ith token, pi is computed as follows:
pi = softmax(xi) =
e
xi
∑ j e
xj
Sampling Strategies
The right sampling strategy can make a model generate responses more suitable for
your application. For example, one sampling strategy can make the model generate
more creative responses, whereas another strategy can make its generations more
predictable. Many different sample strategies have been introduced to nudge models
toward responses with specific attributes. You can also design your own sampling
strategy, though this typically requires access to the model’s logits. Let’s go over a few
common sampling strategies to see how they work.
Temperature
One problem with sampling the next token according to the probability distribution
is that the model can be less creative. In the previous example, common colors like
“red”, “green”, “purple”, and so on have the highest probabilities. The language
model’s answer ends up sounding like that of a five-year-old: “My favorite color is
green”. Because “the” has a low probability, the model has a low chance of generating
a creative sentence such as “My favorite color is the color of a still lake on a spring
morning”.
90 | Chapter 2: Understanding Foundation Models

[Visual content extracted via GLM-OCR]

While larger logits correspond to higher probabilities, logits don’t represent probabilities. Logits don’t sum up to one. Logits can even be negative, while probabilities have to be non-negative. To convert logits to probabilities, a softmax layer is often used. Let’s say the model has a vocabulary of N and the logit vector is $[x_1, x_2, \ldots, x_N]$. The probability for the $i^{th}$ token, $p_i$, is computed as follows:

$$p_i = \text{softmax}(x_i) = \frac{e^{x_i}}{\sum_j e^{x_j}}$$

Sampling Strategies

The right sampling strategy can make a model generate responses more suitable for your application. For example, one sampling strategy can make the model generate more creative responses, whereas another strategy can make its generations more predictable. Many different sample strategies have been introduced to nudge models toward responses with specific attributes. You can also design your own sampling strategy, though this typically requires access to the model’s logits. Let’s go over a few common sampling strategies to see how they work.

Temperature

One problem with sampling the next token according to the probability distribution is that the model can be less creative. In the previous example, common colors like “red”, “green”, “purple”, and so on have the highest probabilities. The language model’s answer ends up sounding like that of a five-year-old: “My favorite color is green”. Because “the” has a low probability, the model has a low chance of generating a creative sentence such as “My favorite color is the color of a still lake on a spring morning”.

24 A visual image I have in mind when thinking about temperature, which isn’t entirely scientific, is that a
higher temperature causes the probability distribution to be more chaotic, which enables lower-probability
tokens to surface.
To redistribute the probabilities of the possible values, you can sample with a temper‐
ature. Intuitively, a higher temperature reduces the probabilities of common tokens,
and as a result, increases the probabilities of rarer tokens. This enables models to cre‐
ate more creative responses.
Temperature is a constant used to adjust the logits before the softmax transforma‐
tion. Logits are divided by temperature. For a given temperature T, the adjusted logit
for the ith token is xiT. Softmax is then applied on this adjusted logit instead of on xi.
Let’s walk through a simple example to examine the effect of temperature on proba‐
bilities. Imagine that we have a model that has only two possible outputs: A and B.
The logits computed from the last layer are [1, 2]. The logit for A is 1 and B is 2.
Without using temperature, which is equivalent to using the temperature of 1, the
softmax probabilities are [0.27, 0.73]. The model picks B 73% of the time.
With temperature = 0.5, the probabilities are [0.12, 0.88]. The model now picks B
88% of the time.
The higher the temperature, the less likely it is that the model is going to pick the
most obvious value (the value with the highest logit), making the model’s outputs
more creative but potentially less coherent. The lower the temperature, the more
likely it is that the model is going to pick the most obvious value, making the model’s
output more consistent but potentially more boring.24
Figure 2-16 shows the softmax probabilities for tokens A and B at different tempera‐
tures. As the temperature gets closer to 0, the probability that the model picks token
B becomes closer to 1. In our example, for a temperature below 0.1, the model almost
always outputs B. As the temperature increases, the probability that token A is picked
increases while the probability that token B is picked decreases. Model providers typ‐
ically limit the temperature to be between 0 and 2. If you own your model, you can
use any non-negative temperature. A temperature of 0.7 is often recommended for
creative use cases, as it balances creativity and predictability, but you should experi‐
ment and find the temperature that works best for you.
Sampling | 91

25 Performing an arg max function.
Figure 2-16. The softmax probabilities for tokens A and B at different temperatures,
given their logits being [1, 2]. Without setting the temperature value, which is equiva‐
lent to using the temperature of 1, the softmax probability of B would be 73%.
It’s common practice to set the temperature to 0 for the model’s outputs to be more
consistent. Technically, temperature can never be 0—logits can’t be divided by 0. In
practice, when we set the temperature to 0, the model just picks the token with the
largest logit,25 without doing logit adjustment and softmax calculation.
A common debugging technique when working with an AI model
is to look at the probabilities this model computes for given inputs.
For example, if the probabilities look random, the model hasn’t
learned much.
92 | Chapter 2: Understanding Foundation Models

[Visual content extracted via GLM-OCR]

Figure 2-16. The softmax probabilities for tokens A and B at different temperatures, given their logits being [1, 2]. Without setting the temperature value, which is equivalent to using the temperature of 1, the softmax probability of B would be 73%.

It’s common practice to set the temperature to 0 for the model’s outputs to be more consistent. Technically, temperature can never be 0—logits can’t be divided by 0. In practice, when we set the temperature to 0, the model just picks the token with the largest logit, without doing logit adjustment and softmax calculation.

A common debugging technique when working with an AI model is to look at the probabilities this model computes for given inputs. For example, if the probabilities look random, the model hasn’t learned much.

25 Performing an arg max function.

26 The underflow problem occurs when a number is too small to be represented in a given format, leading to it
being rounded down to zero.
27 To be more specific, as of this writing, OpenAI API only shows you the logprobs of up to the 20 most likely
tokens. It used to let you get the logprobs of arbitrary user-provided text but discontinued this in September
2023. Anthropic doesn’t expose its models’ logprobs.
Many model providers return probabilities generated by their models as logprobs.
Logprobs, short for log probabilities, are probabilities in the log scale. Log scale is pre‐
ferred when working with a neural network’s probabilities because it helps reduce the
underflow problem.26 A language model might be working with a vocabulary size of
100,000, which means the probabilities for many of the tokens can be too small to be
represented by a machine. The small numbers might be rounded down to 0. Log scale
helps reduce this problem.
Figure 2-17  shows the workflow of how logits, probabilities, and logprobs are
computed.
Figure 2-17. How logits, probabilities, and logprobs are computed.
As you’ll see throughout the book, logprobs are useful for building applications
(especially for classification), evaluating applications, and understanding how models
work under the hood. However, as of this writing, many model providers don’t
expose their models’ logprobs, or if they do, the logprobs API is limited. 27 The limited
logprobs API is likely due to security reasons as a model’s exposed logprobs make it
easier for others to replicate the model.
Sampling | 93

[Visual content extracted via GLM-OCR]

Many model providers return probabilities generated by their models as logprobs. Logprobs, short for log probabilities, are probabilities in the log scale. Log scale is preferred when working with a neural network’s probabilities because it helps reduce the underflow problem. A language model might be working with a vocabulary size of 100,000, which means the probabilities for many of the tokens can be too small to be represented by a machine. The small numbers might be rounded down to 0. Log scale helps reduce this problem.

Figure 2-17 shows the workflow of how logits, probabilities, and logprobs are computed.

Figure 2-17. How logits, probabilities, and logprobs are computed.

As you’ll see throughout the book, logprobs are useful for building applications (especially for classification), evaluating applications, and understanding how models work under the hood. However, as of this writing, many model providers don’t expose their models’ logprobs, or if they do, the logprobs API is limited. The limited logprobs API is likely due to security reasons as a model’s exposed logprobs make it easier for others to replicate the model.

26 The underflow problem occurs when a number is too small to be represented in a given format, leading to it being rounded down to zero.

27 To be more specific, as of this writing, OpenAI API only shows you the logprobs of up to the 20 most likely tokens. It used to let you get the logprobs of arbitrary user-provided text but discontinued this in September 2023. Anthropic doesn’t expose its models’ logprobs.

Top-k
Top-k is a sampling strategy to reduce the computation workload without sacrificing
too much of the model’s response diversity. Recall that a softmax layer is used to
compute the probability distribution over all possible values. Softmax requires two
passes over all possible values: one to perform the exponential sum ∑jexj, and one to
perform exi∑jexj for each value. For a language model with a large vocabulary, this pro‐
cess is computationally expensive.
To avoid this problem, after the model has computed the logits, we pick the top-k
logits and perform softmax over these top-k logits only. Depending on how diverse
you want your application to be, k can be anywhere from 50 to 500—much smaller
than a model’s vocabulary size. The model then samples from these top values. A
smaller k value makes the text more predictable but less interesting, as the model is
limited to a smaller set of likely words.
Top-p
In top-k sampling, the number of values considered is fixed to k. However, this num‐
ber should change depending on the situation. For example, given the prompt “Do
you like music? Answer with only yes or no.” the number of values considered should
be two: yes and no. Given the prompt “What’s the meaning of life?” the number of
values considered should be much larger.
Top-p, also known as nucleus sampling, allows for a more dynamic selection of values
to be sampled from. In top-p sampling, the model sums the probabilities of the most
likely next values in descending order and stops when the sum reaches p. Only the
values within this cumulative probability are considered. Common values for top-p
(nucleus) sampling in language models typically range from 0.9 to 0.95. A top-p value
of 0.9, for example, means that the model will consider the smallest set of values
whose cumulative probability exceeds 90%.
Let’s say the probabilities of all tokens are as shown in Figure 2-18. If top-p is 90%,
only “yes” and “maybe” will be considered, as their cumulative probability is greater
than 90%. If top-p is 99%, then “yes”, “maybe”, and “no” are considered.
94 | Chapter 2: Understanding Foundation Models

28 Paid model APIs often charge per number of output tokens.
Figure 2-18. Example token probabilities.
Unlike top-k, top-p doesn’t necessarily reduce the softmax computation load. Its ben‐
efit is that because it focuses only on the set of most relevant values for each context,
it allows outputs to be more contextually appropriate. In theory, there don’t seem to
be a lot of benefits to top-p sampling. However, in practice, top-p sampling has pro‐
ven to work well, causing its popularity to rise.
A related sampling strategy is min-p, where you set the minimum probability that a
token must reach to be considered during sampling.
Stopping condition
An autoregressive language model generates sequences of tokens by generating one
token after another. A long output sequence takes more time, costs more compute
(money),28 and can sometimes annoy users. We might want to set a condition for the
model to stop the sequence.
One easy method is to ask models to stop generating after a fixed number of tokens.
The downside is that the output is likely to be cut off mid-sentence. Another method
is to use stop tokens or stop words. For example, you can ask a model to stop generat‐
ing when it encounters the end-of-sequence token. Stopping conditions are helpful to
keep latency and costs down.
The downside of early stopping is that if you want models to generate outputs in a
certain format, premature stopping can cause outputs to be malformatted. For exam‐
ple, if you ask the model to generate JSON, early stopping can cause the output JSON
to be missing things like closing brackets, making the generated JSON hard to parse.
Sampling | 95

[Visual content extracted via GLM-OCR]

Unlike top-k, top-p doesn’t necessarily reduce the softmax computation load. Its benefit is that because it focuses only on the set of most relevant values for each context, it allows outputs to be more contextually appropriate. In theory, there don’t seem to be a lot of benefits to top-p sampling. However, in practice, top-p sampling has proven to work well, causing its popularity to rise.

A related sampling strategy is min-p, where you set the minimum probability that a token must reach to be considered during sampling.

Stopping condition

An autoregressive language model generates sequences of tokens by generating one token after another. A long output sequence takes more time, costs more compute (money), and can sometimes annoy users. We might want to set a condition for the model to stop the sequence.

One easy method is to ask models to stop generating after a fixed number of tokens. The downside is that the output is likely to be cut off mid-sentence. Another method is to use stop tokens or stop words. For example, you can ask a model to stop generating when it encounters the end-of-sequence token. Stopping conditions are helpful to keep latency and costs down.

The downside of early stopping is that if you want models to generate outputs in a certain format, premature stopping can cause outputs to be malformatted. For example, if you ask the model to generate JSON, early stopping can cause the output JSON to be missing things like closing brackets, making the generated JSON hard to parse.

28 Paid model APIs often charge per number of output tokens.
