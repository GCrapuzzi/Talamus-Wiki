---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 035
section-title: AI Engineering Versus ML Engineering
source-location: pages 63-69
previous-section: AI Space/normalized/pdf/ai-engineering/sections/034-three-layers-of-the-ai-stack.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/036-ai-engineering-versus-full-stack-engineering.md
classification: reusable-knowledge-candidate
---
# AI Engineering Versus ML Engineering

The data shows a big jump in the number of AI toolings in 2023, after the introduc‐
tion of Stable Diffusion and ChatGPT. In 2023, the categories that saw the highest
increases were applications and application development. The infrastructure layer
saw some growth, but it was much less than the growth seen in other layers. This is
expected. Even though models and applications have changed, the core infrastruc‐
tural needs—resource management, serving, monitoring, etc.—remain the same.
This brings us to the next point. While the level of excitement and creativity around
foundation models is unprecedented, many principles of building AI applications
remain the same. For enterprise use cases, AI applications still need to solve business
problems, and, therefore, it’s still essential to map from business metrics to ML met‐
rics and vice versa. You still need to do systematic experimentation. With classical
ML engineering, you experiment with different hyperparameters. With foundation
models, you experiment with different models, prompts, retrieval algorithms, sam‐
pling variables, and more. (Sampling variables are discussed in Chapter 2.) We still
want to make models run faster and cheaper. It’s still important to set up a feedback
loop so that we can iteratively improve our applications with production data.
This means that much of what ML engineers have learned and shared over the last
decade is still applicable. This collective experience makes it easier for everyone to
begin building AI applications. However, built on top of these enduring principles
are many innovations unique to AI engineering, which we’ll explore in this book.
AI Engineering Versus ML Engineering
While the unchanging principles of deploying AI applications are reassuring, it’s also
important to understand how things have changed. This is helpful for teams that
want to adapt their existing platforms for new AI use cases and developers who are
interested in which skills to learn to stay competitive in a new market.
At a high level, building applications using foundation models today differs from tra‐
ditional ML engineering in three major ways:
1. Without foundation models, you have to train your own models for your appli‐
cations. With AI engineering, you use a model someone else has trained for you.
This means that AI engineering focuses less on modeling and training, and more
on model adaptation.
2. AI engineering works with models that are bigger, consume more compute
resources, and incur higher latency than traditional ML engineering. This means
that there’s more pressure for efficient training and inference optimization. A
corollary of compute-intensive models is that many companies now need more
GPUs and work with bigger compute clusters than they previously did, which
The AI Engineering Stack | 39

23 As the head of AI at a Fortune 500 company told me: his team knows how to work with 10 GPUs, but they
don’t know how to work with 1,000 GPUs.
means there’s more need for engineers who know how to work with GPUs and
big clusters.23
3. AI engineering works with models that can produce open-ended outputs. Openended outputs give models the flexibility to be used for more tasks, but they are
also harder to evaluate. This makes evaluation a much bigger problem in AI
engineering.
In short, AI engineering differs from ML engineering in that it’s less about model
development and more about adapting and evaluating models. I’ve mentioned model
adaptation several times in this chapter, so before we move on, I want to make sure
that we’re on the same page about what model adaptation means. In general, model
adaptation techniques can be divided into two categories, depending on whether they
require updating model weights.
Prompt-based techniques, which include prompt engineering, adapt a model without
updating the model weights.  You adapt a model by giving it instructions and context
instead of changing the model itself. Prompt engineering is easier to get started and
requires less data. Many successful applications have been built with just prompt
engineering. Its ease of use allows you to experiment with more models, which
increases your chance of finding a model that is unexpectedly good for your applica‐
tions. However, prompt engineering might not be enough for complex tasks or appli‐
cations with strict performance requirements.
Finetuning, on the other hand, requires updating model weights. You adapt a model by
making changes to the model itself. In general, finetuning techniques are more com‐
plicated and require more data, but they can improve your model’s quality, latency,
and cost significantly. Many things aren’t possible without changing model weights,
such as adapting the model to a new task it wasn’t exposed to during training.
Now, let’s zoom into the application development and model development layers to
see how each has changed with AI engineering, starting with what existing ML engi‐
neers are more familiar with. This section gives an overview of different processes
involved in developing an AI application. How these processes work will be discussed
throughout this book.
Model development
Model development is the layer most commonly associated with traditional ML engi‐
neering. It has three main responsibilities: modeling and training, dataset engineer‐
ing, and inference optimization. Evaluation is also required, but because most people
40 | Chapter 1: Introduction to Building AI Applications with Foundation Models

24 And they are offered incredible compensation packages.
will come across it first in the application development layer, I’ll discuss evaluation in
the next section.
Modeling and training.    Modeling and training refers to the process of coming up with
a model architecture, training it, and finetuning it. Examples of tools in this category
are Google’s TensorFlow, Hugging Face’s Transformers, and Meta’s PyTorch.
Developing ML models requires specialized ML knowledge. It requires knowing dif‐
ferent types of ML algorithms (such as clustering, logistic regression, decision trees,
and collaborative filtering) and neural network architectures (such as feedforward,
recurrent, convolutional, and transformer). It also requires understanding how a
model learns, including concepts such as gradient descent, loss function, regulariza‐
tion, etc.
With the availability of foundation models, ML knowledge is no longer a must-have
for building AI applications. I’ve met many wonderful and successful AI application
builders who aren’t at all interested in learning about gradient descent. However, ML
knowledge is still extremely valuable, as it expands the set of tools that you can use
and helps troubleshooting when a model doesn’t work as expected.
On the Differences Among Training, Pre-Training,
Finetuning, and Post-Training
Training always involves changing model weights, but not all changes to model
weights constitute training. For example, quantization, the process of reducing the
precision of model weights, technically changes the model’s weight values but isn’t
considered training.
The term training can often be used in place of pre-training, finetuning, and posttraining, which refer to different training phases:
Pre-training
Pre-training refers to training a model from scratch—the model weights are ran‐
domly initialized. For LLMs, pre-training often involves training a model for text
completion. Out of all training steps, pre-training is often the most resourceintensive by a long shot. For the InstructGPT model, pre-training takes up to
98% of the overall compute and data resources . Pre-training also takes a long
time to do. A small mistake during pre-training can incur a significant financial
loss and set back the project significantly. Due to the resource-intensive nature of
pre-training, this has become an art that only a few practice. Those with expertise
in pre-training large models, however, are heavily sought after.24
The AI Engineering Stack | 41

25 If you find the terms “pre-training” and “post-training” lacking in imagination, you’re not alone. The AI
research community is great at many things, but naming isn’t one of them. We already talked about how
“large language models” is hardly a scientific term because of the ambiguity of the word “large”. And I really
wish people would stop publishing papers with the title “X is all you need.”
Finetuning
Finetuning means continuing to train a previously trained model—the model
weights are obtained from the previous training process. Because the model
already has certain knowledge from pre-training, finetuning typically requires
fewer resources (e.g., data and compute) than pre-training.
Post-training
Many people use post-training to refer to the process of training a model after the
pre-training phase. Conceptually, post-training and finetuning are the same and
can be used interchangeably. However, sometimes, people might use them differ‐
ently to signify the different goals. It’s usually post-training when it’s done by
model developers. For example, OpenAI might post-train a model to make it
better at following instructions before releasing it. It’s finetuning when it’s done
by application developers. For example, you might finetune an OpenAI model
(which might have been post-trained itself) to adapt it to your needs.
Pre-training and post-training make up a spectrum. 25 Their processes and toolings
are very similar. Their differences are explored further in Chapters 2 and 7.
Some people use the term training to refer to prompt engineering, which isn’t correct.
I read a Business Insider article where the author said she trained ChatGPT to mimic
her younger self. She did so by feeding her childhood journal entries into ChatGPT.
Colloquially, the author’s usage of the word training is correct, as she’s teaching the
model to do something. But technically, if you teach a model what to do via the con‐
text input into the model, you’re doing prompt engineering. Similarly, I’ve seen peo‐
ple using the term finetuning when what they do is prompt engineering.
Dataset engineering.    Dataset engineering refers to curating, generating, and annotat‐
ing the data needed for training and adapting AI models.
In traditional ML engineering, most use cases are close-ended—a model’s output can
only be among predefined values. For example, spam classification with only two
possible outputs, “spam” and “not spam”, is close-ended. Foundation models, how‐
ever, are open-ended. Annotating open-ended queries is much harder than annotat‐
ing close-ended queries—it’s easier to determine whether an email is spam than to
write an essay. So data annotation is a much bigger challenge for AI engineering.
Another difference is that traditional ML engineering works more with tabular data,
whereas foundation models work with unstructured data. In AI engineering, data
42 | Chapter 1: Introduction to Building AI Applications with Foundation Models

manipulation is more about deduplication, tokenization, context retrieval, and qual‐
ity control, including removing sensitive information and toxic data. Dataset engi‐
neering is the focus of Chapter 8.
Many people argue that because models are now commodities, data will be the main
differentiator, making dataset engineering more important than ever. How much
data you need depends on the adapter technique you use. Training a model from
scratch generally requires more data than finetuning, which, in turn, requires more
data than prompt engineering.
Regardless of how much data you need, expertise in data is useful when examining a
model, as its training data gives important clues about that model’s strengths and
weaknesses.
Inference optimization.    Inference optimization  means making models faster and
cheaper. Inference optimization has always been important for ML engineering.
Users never say no to faster models, and companies can always benefit from cheaper
inference. However, as foundation models scale up to incur even higher inference
cost and latency, inference optimization has become even more important.
One challenge with foundation models is that they are often autoregressive—tokens
are generated sequentially. If it takes 10 ms for a model to generate a token, it’ll take a
second to generate an output of 100 tokens, and even more for longer outputs. As
users are getting notoriously impatient, getting AI applications’ latency down to the
100 ms latency  expected for a typical internet application is a huge challenge. Infer‐
ence optimization has become an active subfield in both industry and academia.
A summary of how the importance of different categories of model development
change with AI engineering is shown in Table 1-4.
Table 1-4. How different responsibilities of model development have changed with
foundation models.
Category Building with traditional ML Building with foundation models
Modeling and training ML knowledge is required for training a
model from scratch
ML knowledge is a nice-to-have, not a must-have a
Dataset engineering More about feature engineering, especially
with tabular data
Less about feature engineering and more about data
deduplication, tokenization, context retrieval, and
quality control
Inference optimization Important Even more important
a Many people would dispute this claim, saying that ML knowledge is a must-have.
The AI Engineering Stack | 43

Inference optimization techniques, including quantization, distillation, and parallel‐
ism, are discussed in Chapters 7 through 9.
Application development
With traditional ML engineering, where teams build applications using their propri‐
etary models, the model quality is a differentiation. With foundation models, where
many teams use the same model, differentiation must be gained through the applica‐
tion development process.
The application development layer consists of these responsibilities: evaluation,
prompt engineering, and AI interface.
Evaluation.    Evaluation is about mitigating risks and uncovering opportunities. Eval‐
uation is necessary throughout the whole model adaptation process. Evaluation is
needed to select models, to benchmark progress, to determine whether an application
is ready for deployment, and to detect issues and opportunities for improvement in
production.
While evaluation has always been important in ML engineering, it’s even more
important with foundation models, for many reasons. The challenges of evaluating
foundation models are discussed in Chapter 3 . To summarize, these challenges
chiefly arise from foundation models’ open-ended nature and expanded capabilities.
For example, in close-ended ML tasks like fraud detection, there are usually expected
ground truths that you can compare your model’s outputs against. If a model’s out‐
put differs from the expected output, you know the model is wrong. For a task like
chatbots, however, there are so many possible responses to each prompt that it is
impossible to curate an exhaustive list of ground truths to compare a model’s
response to.
The existence of so many adaptation techniques also makes evaluation harder. A sys‐
tem that performs poorly with one technique might perform much better with
another. When Google launched Gemini in December 2023, they claimed that Gem‐
ini is better than ChatGPT in the MMLU benchmark ( Hendrycks et al., 2020 ). Goo‐
gle had evaluated Gemini using a prompt engineering technique called CoT@32. In
this technique, Gemini was shown 32 examples, while ChatGPT was shown only 5
examples. When both were shown five examples, ChatGPT performed better, as
shown in Table 1-5.
44 | Chapter 1: Introduction to Building AI Applications with Foundation Models

Table 1-5. Different prompts can cause models to perform very differently, as seen in
Gemini’s technical report (December 2023).
Gemini
Ultra
Gemini
Pro
GPT-4 GPT-3.5 PaLM
2-L
Claude 2 Inflection-2 Grok 1 Llama-2
MMLU
performance
90.04%
CoT@32
79.13%
CoT@8
87.29%
CoT@32
(via API)
70%
5-shot
78.4%
5-shot
78.5%
5-shot
CoT
79.6%
5-shot
73.0%
5-shot
68.0%
83.7%
5-shot
71.8%
5-shot
86.4%
5-shot
(reported)
Prompt engineering and context construction.    Prompt engineering  is about getting AI
models to express the desirable behaviors from the input alone, without changing the
model weights. The Gemini evaluation story highlights the impact of prompt engi‐
neering on model performance. By using a different prompt engineering technique,
Gemini Ultra’s performance on MMLU went from 83.7% to 90.04%.
It’s possible to get a model to do amazing things with just prompts. The right instruc‐
tions can get a model to perform the task you want, in the format of your choice.
Prompt engineering is not just about telling a model what to do. It’s also about giving
the model the necessary context and tools to do a given task. For complex tasks with
long context, you might also need to provide the model with a memory management
system so that the model can keep track of its history. Chapter 5 discusses prompt
engineering, and Chapter 6 discusses context construction.
AI interface.    AI interface  means creating an interface for end users to interact with
your AI applications. Before foundation models, only organizations with sufficient
resources to develop AI models could develop AI applications. These applications
were often embedded into the organizations’ existing products. For example, fraud
detection was embedded into Stripe, Venmo, and PayPal. Recommender systems
were part of social networks and media apps like Netflix, TikTok, and Spotify.
With foundation models, anyone can build AI applications. You can serve your AI
applications as standalone products or embed them into other products, including
products developed by other people. For example, ChatGPT and Perplexity are
standalone products, whereas GitHub’s Copilot is commonly used as a plug-in in
VSCode, and Grammarly is commonly used as a browser extension for Google Docs.
Midjourney can either be used via its standalone web app or via its integration in
Discord.
The AI Engineering Stack | 45
