---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 044
section-title: Model Size
source-location: pages 91-101
previous-section: AI Space/normalized/pdf/ai-engineering/sections/043-model-architecture.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/045-post-training.md
classification: reusable-knowledge-candidate
---
# Model Size

Figure 2-7. A visualization of the transformer, Mamba, and Jamba layers. Image adap‐
ted from “Jamba: A Hybrid Transformer–Mamba Language Model” (Lieber et al.,
2024).
Model Size
Much of AI progress in recent years can be attributed to increased model size. It’s
hard to talk about foundation models without talking about their number of parame‐
ters. The number of parameters is usually appended at the end of a model name. For
example, Llama-13B refers to the version of Llama, a model family developed by
Meta, with 13 billion parameters.
In general, increasing a model’s parameters increases its capacity to learn, resulting in
better models. Given two models of the same model family, the one with 13 billion
parameters is likely to perform much better than the one with 7 billion parameters.
Modeling | 67

[Visual content extracted via GLM-OCR]

Model Size

Much of AI progress in recent years can be attributed to increased model size. It’s hard to talk about foundation models without talking about their number of parameters. The number of parameters is usually appended at the end of a model name. For example, Llama-13B refers to the version of Llama, a model family developed by Meta, with 13 billion parameters.

In general, increasing a model’s parameters increases its capacity to learn, resulting in better models. Given two models of the same model family, the one with 13 billion parameters is likely to perform much better than the one with 7 billion parameters.

13 The actual memory needed is higher. Chapter 7 discusses how to calculate a model’s memory usage.
As the community better understands how to train large models,
newer-generation models tend to outperform older-generation
models of the same size. For example, Llama 3-8B (2024)  outper‐
forms even Llama 2-70B (2023) on the MMLU benchmark.
The number of parameters helps us estimate the compute resources needed to train
and run this model. For example, if a model has 7 billion parameters, and each
parameter is stored using 2 bytes (16 bits), then we can calculate that the GPU mem‐
ory needed to do inference using this model will be at least 14 billion bytes (14 GB).13
The number of parameters can be misleading if the model is sparse. A sparse model
has a large percentage of zero-value parameters. A 7B-parameter model that is 90%
sparse only has 700 million non-zero parameters. Sparsity allows for more efficient
data storage and computation. This means that a large sparse model can require less
compute than a small dense model.
A type of sparse model that has gained popularity in recent years is mixture-ofexperts (MoE) (Shazeer et al., 2017 ). An MoE model is divided into different groups
of parameters, and each group is an expert. Only a subset of the experts is active for
(used to) process each token.
For example, Mixtral 8x7B is a mixture of eight experts, each expert with seven bil‐
lion parameters. If no two experts share any parameter, it should have 8 × 7 billion =
56 billion parameters. However, due to some parameters being shared, it has only
46.7 billion parameters.
At each layer, for each token, only two experts are active. This means that only 12.9
billion parameters are active for each token. While this model has 46.7 billion param‐
eters, its cost and speed are the same as a 12.9-billion-parameter model.
A larger model can also underperform a smaller model if it’s not trained on enough
data. Imagine a 13B-param model trained on a dataset consisting of a single sentence:
“I like pineapples.” This model will perform much worse than a much smaller model
trained on more data.
When discussing model size, it’s important to consider the size of the data it was
trained on. For most models, dataset sizes are measured by the number of training
samples. For example, Google’s Flamingo ( Alayrac et al., 2022) was trained using four
datasets—one of them has 1.8 billion (image, text) pairs and one has 312 million
(image, text) pairs.
68 | Chapter 2: Understanding Foundation Models

[Visual content extracted via GLM-OCR]

As the community better understands how to train large models, newer-generation models tend to outperform older-generation models of the same size. For example, Llama 3-8B (2024) outperforms even Llama 2-70B (2023) on the MMLU benchmark.

The number of parameters helps us estimate the compute resources needed to train and run this model. For example, if a model has 7 billion parameters, and each parameter is stored using 2 bytes (16 bits), then we can calculate that the GPU memory needed to do inference using this model will be at least 14 billion bytes (14 GB).13

The number of parameters can be misleading if the model is sparse. A sparse model has a large percentage of zero-value parameters. A 7B-parameter model that is 90% sparse only has 700 million non-zero parameters. Sparsity allows for more efficient data storage and computation. This means that a large sparse model can require less compute than a small dense model.

A type of sparse model that has gained popularity in recent years is mixture-of-experts (MoE) (Shazeer et al., 2017). An MoE model is divided into different groups of parameters, and each group is an expert. Only a subset of the experts is active for (used to) process each token.

For example, Mixtral 8x7B is a mixture of eight experts, each expert with seven billion parameters. If no two experts share any parameter, it should have $8 \times 7$ billion = 56 billion parameters. However, due to some parameters being shared, it has only 46.7 billion parameters.

At each layer, for each token, only two experts are active. This means that only 12.9 billion parameters are active for each token. While this model has 46.7 billion parameters, its cost and speed are the same as a 12.9-billion-parameter model.

A larger model can also underperform a smaller model if it’s not trained on enough data. Imagine a 13B-param model trained on a dataset consisting of a single sentence: “I like pineapples.” This model will perform much worse than a much smaller model trained on more data.

When discussing model size, it’s important to consider the size of the data it was trained on. For most models, dataset sizes are measured by the number of training samples. For example, Google’s Flamingo (Alayrac et al., 2022) was trained using four datasets—one of them has 1.8 billion (image, text) pairs and one has 312 million (image, text) pairs.

13 The actual memory needed is higher. Chapter 7 discusses how to calculate a model’s memory usage.

14 Assuming a book contains around 50,000 words or 67,000 tokens.
15 As of this writing, large models are typically pre-trained on only one epoch of data.
For language models, a training sample can be a sentence, a Wikipedia page, a chat
conversation, or a book. A book is worth a lot more than a sentence, so the number
of training samples is no longer a good metric to measure dataset sizes. A better
measurement is the number of tokens in the dataset.
The number of tokens isn’t a perfect measurement either, as different models can
have different tokenization processes, resulting in the same dataset having different
numbers of tokens for different models. Why not just use the number of words or the
number of letters? Because a token is the unit that a model operates on, knowing the
number of tokens in a dataset helps us measure how much a model can potentially
learn from that data.
As of this writing, LLMs are trained using datasets in the order of trillions of tokens.
Meta used increasingly larger datasets to train their Llama models:
• 1.4 trillion tokens for Llama 1
• 2 trillion tokens for Llama 2
• 15 trillion tokens for Llama 3
Together’s open source dataset RedPajama-v2 has 30 trillion tokens . This is equiva‐
lent to 450 million books 14 or 5,400 times the size of Wikipedia. However, since
RedPajama-v2 consists of indiscriminate content, the amount of high-quality data is
much lower.
The number of tokens in a model’s dataset isn’t the same as its number of training
tokens. The number of training tokens measures the tokens that the model is trained
on. If a dataset contains 1 trillion tokens and a model is trained on that dataset for
two epochs—an epoch is a pass through the dataset—the number of training tokens is
2 trillion. 15 See Table 2-5 for examples of the number of training tokens for models
with different numbers of parameters.
Table 2-5. Examples of the number of training tokens for models with different numbers of
parameters. Source: “Training Compute-Optimal Large Language Models” ( DeepMind,
2022).
Model Size (# parameters) Training tokens
LaMDA (Thoppilan et al., 2022) 137 billion 168 billion
GPT-3 (Brown et al., 2020) 175 billion 300 billion
Jurassic (Lieber et al., 2021) 178 billion 300 billion
Gopher (Rae et al., 2021) 280 billion 300 billion
Modeling | 69

16 FLOP/s count is measured in FP32. Floating point formats is discussed in Chapter 7.
Model Size (# parameters) Training tokens
MT-NLG 530B (Smith et al., 2022) 530 billion 270 billion
Chinchilla 70 billion 1.4 trillion
While this section focuses on the scale of data, quantity isn’t the
only thing that matters. Data quality and data diversity matter, too.
Quantity, quality, and diversity are the three golden goals for train‐
ing data. They are discussed further in Chapter 8.
Pre-training large models requires compute. One way to measure the amount of
compute needed is by considering the number of machines, e.g., GPUs, CPUs, and
TPUs. However, different machines have very different capacities and costs. An
NVIDIA A10 GPU is different from an NVIDIA H100 GPU and an Intel Core Ultra
Processor.
A more standardized unit for a model’s compute requirement is FLOP, or floating
point operation. FLOP measures the number of floating point operations performed
for a certain task. Google’s largest PaLM-2 model, for example, was trained using 1022
FLOPs (Chowdhery et al., 2022 ). GPT-3-175B was trained using 3.14 × 10 23 FLOPs
(Brown et al., 2020).
The plural form of FLOP, FLOPs, is often confused with FLOP/s, floating point opera‐
tions per Second.  FLOPs measure the compute requirement for a task, whereas
FLOP/s measures a machine’s peak performance. For example, an NVIDIA H100
NVL GPU can deliver a maximum of 60 TeraFLOP/s: 6 × 10 13 FLOPs a second or
5.2 × 1018 FLOPs a day.16
Be alert for confusing notations. FLOP/s is often written as FLOPS,
which looks similar to FLOPs. To avoid this confusion, some com‐
panies, including OpenAI, use FLOP/s-day in place of FLOPs to
measure compute requirements:
1 FLOP/s-day = 60 × 60 × 24 = 86,400 FLOPs
This book uses FLOPs for counting floating point operations and
FLOP/s for FLOPs per second.
Assume that you have 256 H100s. If you can use them at their maximum capacity
and make no training mistakes, it’d take you (3.14 × 1023) / (256 × 5.2 × 10 18)
= ~236 days, or approximately 7.8 months, to train GPT-3-175B.
70 | Chapter 2: Understanding Foundation Models

[Visual content extracted via GLM-OCR]

While this section focuses on the scale of data, quantity isn’t the only thing that matters. Data quality and data diversity matter, too. Quantity, quality, and diversity are the three golden goals for training data. They are discussed further in Chapter 8.

Pre-training large models requires compute. One way to measure the amount of compute needed is by considering the number of machines, e.g., GPUs, CPUs, and TPUs. However, different machines have very different capacities and costs. An NVIDIA A10 GPU is different from an NVIDIA H100 GPU and an Intel Core Ultra Processor.

A more standardized unit for a model’s compute requirement is FLOP, or floating point operation. FLOP measures the number of floating point operations performed for a certain task. Google’s largest PaLM-2 model, for example, was trained using $10^{22}$ FLOPs (Chowdhery et al., 2022). GPT-3-175B was trained using $3.14 \times 10^{23}$ FLOPs (Brown et al., 2020).

The plural form of FLOP, FLOPs, is often confused with FLOP/s, floating point operations per Second. FLOPs measure the compute requirement for a task, whereas FLOP/s measures a machine’s peak performance. For example, an NVIDIA H100 NVL GPU can deliver a maximum of 60 TeraFLOP/s: $6 \times 10^{13}$ FLOPs a second or $5.2 \times 10^{18}$ FLOPs a day.$^{16}$

Be alert for confusing notations. FLOP/s is often written as FLOPS, which looks similar to FLOPs. To avoid this confusion, some companies, including OpenAI, use FLOP/s-day in place of FLOPs to measure compute requirements:

$$1 \text{ FLOP/s-day} = 60 \times 60 \times 24 = 86,400 \text{ FLOPs}$$

This book uses FLOPs for counting floating point operations and FLOP/s for FLOPs per second.

Assume that you have 256 H100s. If you can use them at their maximum capacity and make no training mistakes, it’d take you $(3.14 \times 10^{23}) / (256 \times 5.2 \times 10^{18}) = \sim 236 \text{ days},$ or approximately 7.8 months, to train GPT-3-175B.

$^{16}$ FLOP/s count is measured in FP32. Floating point formats is discussed in Chapter 7.

However, it’s unlikely you can use your machines at their peak capacity all the time. Utilization measures how much of the maximum compute capacity you can use. What’s considered good utilization depends on the model, the workload, and the hardware. Generally, if you can get half the advertised performance, 50% utilization, you’re doing okay. Anything above 70% utilization is considered great. Don’t let this rule stop you from getting even higher utilization. Chapter 9 discusses hardware metrics and utilization in more detail.

At 70% utilization and $2/h for one H100, training GPT-3-175B would cost over $4 million:

$$\frac{2}{H100/hour} \times 256 \times H100 \times 24 \text{ hours} \times 256 \text{ days} / 0.7 = \$4,142,811.43$$

In summary, three numbers signal a model’s scale:

- Number of parameters, which is a proxy for the model’s learning capacity.
- Number of tokens a model was trained on, which is a proxy for how much a model learned.
- Number of FLOPs, which is a proxy for the training cost.

Inverse Scaling

We’ve assumed that bigger models are better. Are there scenarios for which bigger models perform worse? In 2022, Anthropic discovered that, counterintuitively, more alignment training (discussed in “Post-Training” on page 78) leads to models that align less with human preference (Perez et al., 2022). According to their paper, models trained to be more aligned “are much more likely to express specific political views (pro-gun rights and immigration) and religious views (Buddhist), self-reported conscious experience and moral self-worth, and a desire to not be shut down.”

In 2023, a group of researchers, mostly from New York University, launched the Inverse Scaling Prize to find tasks where larger language models perform worse. They offered $5,000 for each third prize, $20,000 for each second prize, and $100,000 for one first prize. They received a total of 99 submissions, of which 11 were awarded third prizes. They found that larger language models are sometimes (only sometimes) worse on tasks that require memorization and tasks with strong priors. However, they didn’t award any second or first prizes because even though the submitted tasks show failures for a small test set, none demonstrated failures in the real world.

17 As of this writing, cloud providers are offering H100s for around $2 to $5 per hour. As compute is getting rapidly cheaper, this number will get much lower.

Scaling law: Building compute-optimal models
I hope that the last section has convinced you of three things:
1. Model performance depends on the model size and the dataset size.
2. Bigger models and bigger datasets require more compute.
3. Compute costs money.
Unless you have unlimited money, budgeting is essential. You don’t want to start
with an arbitrarily large model size and see how much it would cost. You start with a
budget—how much money you want to spend—and work out the best model perfor‐
mance you can afford. As compute is often the limiting factor—compute infrastruc‐
ture is not only expensive but also hard to set up—teams often start with a compute
budget. Given a fixed amount of FLOPs, what model size and dataset size would give
the best performance? A model that can achieve the best performance given a fixed
compute budget is compute-optional.
Given a compute budget, the rule that helps calculate the optimal model size and
dataset size is called the Chinchilla scaling law , proposed in the Chinchilla paper
“Training Compute-Optimal Large Language Models”  (DeepMind, 2022). To study
the relationship between model size, dataset size, compute budget, and model perfor‐
mance, the authors trained 400 language models ranging from 70 million to over 16
billion parameters on 5 to 500 billion tokens. They found that for compute-optimal
training, you need the number of training tokens to be approximately 20 times the
model size. This means that a 3B-parameter model needs approximately 60B training
tokens. The model size and the number of training tokens should be scaled equally:
for every doubling of the model size, the number of training tokens should also be
doubled.
We’ve come a long way from when the training process was treated like alchemy.
Figure 2-8 shows that we can predict not only the optimal number of parameters and
tokens for each FLOP budget but also the expected training loss from these settings
(assuming we do things right).
This compute-optimal calculation assumes that the cost of acquiring data is much
cheaper than the cost of compute. The same Chinchilla paper proposes another cal‐
culation for when the cost of training data is nontrivial.
72 | Chapter 2: Understanding Foundation Models

Figure 2-8. Graphs that depict the relationships between training loss, a model’s num‐
ber of parameters, FLOPs, and number of training tokens. Source: “Training ComputeOptional Large Language Models” (DeepMind, 2022).
The scaling law was developed for dense models trained on predominantly humangenerated data. Adapting this calculation for sparse models, such as mixture-ofexpert models, and synthetic data is an active research area.
The scaling law optimizes model quality given a compute budget. However, it’s
important to remember that for production, model quality isn’t everything. Some
models, most notably Llama, have suboptimal performance but better usability.
Given their compute budget, Llama authors could’ve chosen bigger models that
would perform better, but they opted for smaller models. Smaller models are easier to
work with and cheaper to run inference on, which helped their models gain wider
adoption. Sardana et al. (2023)  modified the Chinchilla scaling law to calculate the
optimal LLM parameter count and pre-training data size to account for this inference
demand.
On the topic of model performance given a compute budget, it’s worth noting that
the cost of achieving a given model performance is decreasing. For example, on the
ImageNet dataset, the cost to achieve 93% accuracy halved from 2019 to 2021,
according to the Artificial Intelligence Index Report 2022 (Stanford University HAI).
While the cost for the same model performance is decreasing, the cost for model perfor‐
mance improvement remains high.  Similar to the last mile challenge discussed in
Chapter 1 , improving a model’s accuracy from 90 to 95% is more expensive than
improving it from 85 to 90%. As Meta’s paper “Beyond Neural Scaling Laws: Beating
Power Law Scaling via Data Pruning”  pointed out, this means a model with a 2%
error rate might require an order of magnitude more data, compute, or energy than a
model with a 3% error rate.
Modeling | 73

[Visual content extracted via GLM-OCR]

The scaling law was developed for dense models trained on predominantly human-generated data. Adapting this calculation for sparse models, such as mixture-of-expert models, and synthetic data is an active research area.

The scaling law optimizes model quality given a compute budget. However, it’s important to remember that for production, model quality isn’t everything. Some models, most notably Llama, have suboptimal performance but better usability. Given their compute budget, Llama authors could’ve chosen bigger models that would perform better, but they opted for smaller models. Smaller models are easier to work with and cheaper to run inference on, which helped their models gain wider adoption. Sardana et al. (2023) modified the Chinchilla scaling law to calculate the optimal LLM parameter count and pre-training data size to account for this inference demand.

On the topic of model performance given a compute budget, it’s worth noting that the cost of achieving a given model performance is decreasing. For example, on the ImageNet dataset, the cost to achieve 93% accuracy halved from 2019 to 2021, according to the Artificial Intelligence Index Report 2022 (Stanford University HAI).

While the cost for the same model performance is decreasing, the cost for model performance improvement remains high. Similar to the last mile challenge discussed in Chapter 1, improving a model’s accuracy from 90 to 95% is more expensive than improving it from 85 to 90%. As Meta’s paper “Beyond Neural Scaling Laws: Beating Power Law Scaling via Data Pruning” pointed out, this means a model with a 2% error rate might require an order of magnitude more data, compute, or energy than a model with a 3% error rate.

18 Jascha Sohl-Dickstein, an amazing researcher, shared a beautiful visualization of what hyperparameters work
and don’t work  on his X page.
In language modeling, a drop in cross entropy loss from about 3.4 to 2.8 nats requires
10 times more training data. Cross entropy and its units, including nats, are discussed
in Chapter 3 . For large vision models, increasing the number of training samples
from 1 billion to 2 billion leads to an accuracy gain on ImageNet of only a few per‐
centage points.
However, small performance changes in language modeling loss or ImageNet accu‐
racy can lead to big differences in the quality of downstream applications. If you
switch from a model with a cross-entropy loss of 3.4 to one with a loss of 2.8, you’ll
notice a difference.
Scaling extrapolation
The performance of a model depends heavily on the values of its hyperparameters.
When working with small models, it’s a common practice to train a model multiple
times with different sets of hyperparameters and pick the best-performing one. This
is, however, rarely possible for large models as training them once is resourcedraining enough.
Parameter Versus Hyperparameter
A parameter can be learned by the model during the training process. A hyperpara‐
meter is set by users to configure the model and control how the model learns.
Hyperparameters to configure the model include the number of layers, the model
dimension, and vocabulary size. Hyperparameters to control how a model learns
include batch size, number of epochs, learning rate, per-layer initial variance, and
more.
This means that for many models, you might have only one shot of getting the right
set of hyperparameters. As a result, scaling extrapolation (also called hyperparameter
transferring) has emerged as a research subfield that tries to predict, for large models,
what hyperparameters will give the best performance. The current approach is to
study the impact of hyperparameters on models of different sizes, usually much
smaller than the target model size, and then extrapolate how these hyperparameters
would work on the target model size.18 A 2022 paper by Microsoft and OpenAI shows
that it was possible to transfer hyperparameters from a 40M model to a 6.7B model.
74 | Chapter 2: Understanding Foundation Models

19 Dario Amodei, Anthropic CEO, said that if the scaling hypothesis is true, a $100 billion AI model will be as
good as a Nobel prize winner.
Scaling extrapolation is still a niche topic, as few people have the experience and
resources to study the training of large models. It’s also difficult to do due to the
sheer number of hyperparameters and how they interact with each other. If you have
ten hyperparameters, you’d have to study 1,024 hyperparameter combinations. You
would have to study each hyperparameter individually, then two of them together,
and three of them together, and so on.
In addition, emergent abilities (Wei et al., 2022) make the extrapolation less accurate.
Emergent abilities refer to those that are only present at scale might not be observable
on smaller models trained on smaller datasets. To learn more about scaling extrapo‐
lation, check out this excellent blog post: “On the Difficulty of Extrapolation with NN
Scaling” ( Luke Metz, 2022).
Scaling bottlenecks
Until now, every order of magnitude increase in model size has led to an increase in
model performance. GPT-2 has an order of magnitude more parameters than GPT-1
(1.5 billion versus 117 million). GPT-3 has two orders of magnitude more than
GPT-2 (175 billion versus 1.5 billion). This means a three-orders-of-magnitude
increase in model sizes between 2018 and 2021. Three more orders of magnitude
growth would result in 100-trillion-parameter models.19
How many more orders of magnitude can model sizes grow? Would there be a point
where the model performance plateaus regardless of its size? While it’s hard to
answer these questions, there are already two visible bottlenecks for scaling: training
data and electricity.
Foundation models use so much data that there’s a realistic concern we’ll run out of
internet data in the next few years. The rate of training dataset size growth is much
faster than the rate of new data being generated ( Villalobos et al., 2022), as illustrated
in Figure 2-9. If you’ve ever put anything on the internet, you should assume that it
already is or will be included in the training data for some language models,  whether
you consent or not. This is similar to how, if you post something on the internet, you
should expect it to be indexed by Google.
Modeling | 75

Figure 2-9. Projection of historical trend of training dataset sizes and available data
stock. Source: Villalobos et al., 2024.
Some people are leveraging this fact to inject data they want into the training data of
future models. They do this simply by publishing the text they want on the internet,
hoping it will influence future models to generate the responses they desire. Bad
actors can also leverage this approach for prompt injection attacks, as discussed in
Chapter 5.
An open research question is how to make a model forget specific
information it has learned during training. Imagine you published
a blog post that you eventually deleted. If that blog post was
included in a model’s training data, the model might still repro‐
duce the post’s content. As a result, people could potentially access
removed content without your consent.
On top of that, the internet is being rapidly populated with data generated by AI
models. If companies continue using internet data to train future models, these
new models will be partially trained on AI-generated data. In December 2023, Grok,
a model trained by X, was caught refusing a request by saying that it goes against
OpenAI’s use case policy. This caused some people to speculate that Grok was
trained using ChatGPT outputs. Igor Babuschkin, a core developer behind Grok ,
76 | Chapter 2: Understanding Foundation Models

[Visual content extracted via GLM-OCR]

Some people are leveraging this fact to inject data they want into the training data of future models. They do this simply by publishing the text they want on the internet, hoping it will influence future models to generate the responses they desire. Bad actors can also leverage this approach for prompt injection attacks, as discussed in Chapter 5.

An open research question is how to make a model forget specific information it has learned during training. Imagine you published a blog post that you eventually deleted. If that blog post was included in a model’s training data, the model might still reproduce the post’s content. As a result, people could potentially access removed content without your consent.

On top of that, the internet is being rapidly populated with data generated by AI models. If companies continue using internet data to train future models, these new models will be partially trained on AI-generated data. In December 2023, Grok, a model trained by X, was caught refusing a request by saying that it goes against OpenAI’s use case policy. This caused some people to speculate that Grok was trained using ChatGPT outputs. Igor Babuschkin, a core developer behind Grok,

20 AI-generated content is multiplied by the ease of machine translation. AI can be used to generate an article,
then translate that article into multiple languages, as shown in “A Shocking Amount of the Web Is Machine
Translated” ( Thompson et al., 2024).
responded that it was because Grok was trained on web data, and “the web is full of
ChatGPT outputs.” 20
Some researchers worry that recursively training new AI models on AI-generated
data causes the new models to gradually forget the original data patterns, degrading
their performance over time ( Shumailov et al., 2023 ). However, the impact of AIgenerated data on models is more nuanced and is discussed in Chapter 8.
Once the publicly available data is exhausted, the most feasible paths for more
human-generated training data is proprietary data. Unique proprietary data—copy‐
righted books, translations, contracts, medical records, genome sequences, and so
forth—will be a competitive advantage in the AI race. This is a reason why OpenAI
negotiated deals with publishers and media outlets including Axel Springer and the
Associated Press.
It’s not surprising that in light of ChatGPT, many companies, including Reddit and
Stack Overflow , have changed their data terms to prevent other companies from
scraping their data for their models. Longpre et al. (2024) observed that between 2023
and 2024, the rapid crescendo of data restrictions from web sources rendered over
28% of the most critical sources in the popular public dataset C4 fully restricted from
use. Due to changes in its Terms of Service and crawling restrictions, a full 45% of C4
is now restricted.
The other bottleneck, which is less obvious but more pressing, is electricity. Machines
require electricity to run. As of this writing, data centers are estimated to consume 1–
2% of global electricity. This number is estimated to reach between 4% and 20% by
2030 (Patel, Nishball, and Ontiveros, 2024). Until we can figure out a way to produce
more energy, data centers can grow at most 50 times, which is less than two orders of
magnitude. This leads to a concern about a power shortage in the near future, which
will drive up the cost of electricity.
Now that we’ve covered two key modeling decisions—architecture and scale—let’s
move on to the next critical set of design choices: how to align models with human
preferences.
Modeling | 77
