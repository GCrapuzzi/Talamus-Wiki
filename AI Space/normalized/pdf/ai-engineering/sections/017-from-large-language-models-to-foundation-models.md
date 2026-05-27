---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 017
section-title: From Large Language Models to Foundation Models
source-location: pages 32-35
previous-section: AI Space/normalized/pdf/ai-engineering/sections/016-from-language-models-to-large-language-models.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/018-from-foundation-models-to-ai-engineering.md
classification: reusable-knowledge-candidate
---
# From Large Language Models to Foundation Models

7 In school, I was taught that model parameters include both model weights and model biases. However, today,
we generally use model weights to refer to all parameters.
8 It seems counterintuitive that larger models require more training data. If a model is more powerful,
shouldn’t it require fewer examples to learn from? However, we’re not trying to get a large model to match
the performance of a small model using the same data. We’re trying to maximize model performance.
Self-supervision differs from unsupervision. In self-supervised
learning, labels are inferred from the input data. In unsupervised
learning, you don’t need labels at all.
Self-supervised learning means that language models can learn from text sequences
without requiring any labeling. Because text sequences are everywhere—in books,
blog posts, articles, and Reddit comments—it’s possible to construct a massive
amount of training data, allowing language models to scale up to become LLMs.
LLM, however, is hardly a scientific term. How large does a language model have to
be to be considered large? What is large today might be considered tiny tomorrow. A
model’s size is typically measured by its number of parameters. A parameter is a vari‐
able within an ML model that is updated through the training process. 7 In general,
though this is not always true, the more parameters a model has, the greater its
capacity to learn desired behaviors.
When OpenAI’s first generative pre-trained transformer (GPT) model came out in
June 2018, it had 117 million parameters, and that was considered large. In February
2019, when OpenAI introduced GPT-2 with 1.5 billion parameters, 117 million was
downgraded to be considered small. As of the writing of this book, a model with 100
billion parameters is considered large. Perhaps one day, this size will be considered
small.
Before we move on to the next section, I want to touch on a question that is usually
taken for granted: Why do larger models need more data?  Larger models have more
capacity to learn, and, therefore, would need more training data to maximize their
performance.8 You can train a large model on a small dataset too, but it’d be a waste
of compute. You could have achieved similar or better results on this dataset with
smaller models.
From Large Language Models to Foundation Models
While language models are capable of incredible tasks, they are limited to text. As
humans, we perceive the world not just via language but also through vision, hearing,
touch, and more. Being able to process data beyond text is essential for AI to operate
in the real world.
8 | Chapter 1: Introduction to Building AI Applications with Foundation Models

[Visual content extracted via GLM-OCR]

Self-supervised learning means that language models can learn from text sequences without requiring any labeling. Because text sequences are everywhere—in books, blog posts, articles, and Reddit comments—it’s possible to construct a massive amount of training data, allowing language models to scale up to become LLMs.

LLM, however, is hardly a scientific term. How large does a language model have to be to be considered large? What is large today might be considered tiny tomorrow. A model’s size is typically measured by its number of parameters. A parameter is a variable within an ML model that is updated through the training process. In general, though this is not always true, the more parameters a model has, the greater its capacity to learn desired behaviors.

When OpenAI’s first generative pre-trained transformer (GPT) model came out in June 2018, it had 117 million parameters, and that was considered large. In February 2019, when OpenAI introduced GPT-2 with 1.5 billion parameters, 117 million was downgraded to be considered small. As of the writing of this book, a model with 100 billion parameters is considered large. Perhaps one day, this size will be considered small.

Before we move on to the next section, I want to touch on a question that is usually taken for granted: Why do larger models need more data? Larger models have more capacity to learn, and, therefore, would need more training data to maximize their performance. You can train a large model on a small dataset too, but it’d be a waste of compute. You could have achieved similar or better results on this dataset with smaller models.

From Large Language Models to Foundation Models

While language models are capable of incredible tasks, they are limited to text. As humans, we perceive the world not just via language but also through vision, hearing, touch, and more. Being able to process data beyond text is essential for AI to operate in the real world.

7 In school, I was taught that model parameters include both model weights and model biases. However, today, we generally use model weights to refer to all parameters.

8 It seems counterintuitive that larger models require more training data. If a model is more powerful, shouldn’t it require fewer examples to learn from? However, we’re not trying to get a large model to match the performance of a small model using the same data. We’re trying to maximize model performance.

For this reason, language models are being extended to incorporate more data
modalities. GPT-4V and Claude 3 can understand images and texts. Some models
even understand videos, 3D assets, protein structures, and so on. Incorporating more
data modalities into language models makes them even more powerful. OpenAI
noted in their GPT-4V system card  in 2023 that “incorporating additional modalities
(such as image inputs) into LLMs is viewed by some as a key frontier in AI research
and development.”
While many people still call Gemini and GPT-4V LLMs, they’re better characterized
as foundation models . The word foundation signifies both the importance of these
models in AI applications and the fact that they can be built upon for different needs.
Foundation models mark a breakthrough from the traditional structure of AI
research. For a long time, AI research was divided by data modalities. Natural lan‐
guage processing (NLP) deals only with text. Computer vision deals only with vision.
Text-only models can be used for tasks such as translation and spam detection.
Image-only models can be used for object detection and image classification. Audioonly models can handle speech recognition (speech-to-text, or STT) and speech syn‐
thesis (text-to-speech, or TTS).
A model that can work with more than one data modality is also called a multimodal
model. A generative multimodal model is also called a large multimodal model
(LMM). If a language model generates the next token conditioned on text-only
tokens, a multimodal model generates the next token conditioned on both text and
image tokens, or whichever modalities that the model supports, as shown in
Figure 1-3.
Figure 1-3. A multimodal model can generate the next token using information from
both text and visual tokens.
The Rise of AI Engineering | 9

[Visual content extracted via GLM-OCR]

For this reason, language models are being extended to incorporate more data modalities. GPT-4V and Claude 3 can understand images and texts. Some models even understand videos, 3D assets, protein structures, and so on. Incorporating more data modalities into language models makes them even more powerful. OpenAI noted in their GPT-4V system card in 2023 that “incorporating additional modalities (such as image inputs) into LLMs is viewed by some as a key frontier in AI research and development.”

While many people still call Gemini and GPT-4V LLMs, they’re better characterized as foundation models. The word foundation signifies both the importance of these models in AI applications and the fact that they can be built upon for different needs.

Foundation models mark a breakthrough from the traditional structure of AI research. For a long time, AI research was divided by data modalities. Natural language processing (NLP) deals only with text. Computer vision deals only with vision. Text-only models can be used for tasks such as translation and spam detection. Image-only models can be used for object detection and image classification. Audio-only models can handle speech recognition (speech-to-text, or STT) and speech synthesis (text-to-speech, or TTS).

A model that can work with more than one data modality is also called a multimodal model. A generative multimodal model is also called a large multimodal model (LMM). If a language model generates the next token conditioned on text-only tokens, a multimodal model generates the next token conditioned on both text and image tokens, or whichever modalities that the model supports, as shown in Figure 1-3.

Figure 1-3. A multimodal model can generate the next token using information from both text and visual tokens.

Just like language models, multimodal models need data to scale up. Self-supervision
works for multimodal models too. For example, OpenAI used a variant of selfsupervision called natural language supervision  to train their language-image model
CLIP (OpenAI, 2021) . Instead of manually generating labels for each image, they
found (image, text) pairs that co-occurred on the internet. They were able to generate
a dataset of 400 million (image, text) pairs, which was 400 times larger than Image‐
Net, without manual labeling cost. This dataset enabled CLIP to become the first
model that could generalize to multiple image classification tasks without requiring
additional training.
This book uses the term foundation models to refer to both large
language models and large multimodal models.
Note that CLIP isn’t a generative model—it wasn’t trained to generate open-ended
outputs. CLIP is an embedding model, trained to produce joint embeddings of both
texts and images. “Introduction to Embedding”  on page 134 discusses embeddings in
detail. For now, you can think of embeddings as vectors that aim to capture the
meanings of the original data. Multimodal embedding models like CLIP are the back‐
bones of generative multimodal models, such as Flamingo, LLaVA, and Gemini (pre‐
viously Bard).
Foundation models also mark the transition from task-specific models to generalpurpose models. Previously, models were often developed for specific tasks, such as
sentiment analysis or translation. A model trained for sentiment analysis wouldn’t be
able to do translation, and vice versa.
Foundation models, thanks to their scale and the way they are trained, are capable of a
wide range of tasks.  Out of the box, general-purpose models can work relatively well
for many tasks. An LLM can do both sentiment analysis and translation. However,
you can often tweak a general-purpose model to maximize its performance on a spe‐
cific task.
Figure 1-4 shows the tasks used by the Super-NaturalInstructions benchmark to eval‐
uate foundation models ( Wang et al., 2022 ), providing an idea of the types of tasks a
foundation model can perform.
Imagine you’re working with a retailer to build an application to generate product
descriptions for their website. An out-of-the-box model might be able to generate
accurate descriptions but might fail to capture the brand’s voice or highlight the
brand’s messaging. The generated descriptions might even be full of marketing
speech and cliches.
10 | Chapter 1: Introduction to Building AI Applications with Foundation Models

[Visual content extracted via GLM-OCR]

Just like language models, multimodal models need data to scale up. Self-supervision works for multimodal models too. For example, OpenAI used a variant of self-supervision called natural language supervision to train their language-image model CLIP (OpenAI, 2021). Instead of manually generating labels for each image, they found (image, text) pairs that co-occurred on the internet. They were able to generate a dataset of 400 million (image, text) pairs, which was 400 times larger than Image-Net, without manual labeling cost. This dataset enabled CLIP to become the first model that could generalize to multiple image classification tasks without requiring additional training.

This book uses the term foundation models to refer to both large language models and large multimodal models.

Note that CLIP isn’t a generative model—it wasn’t trained to generate open-ended outputs. CLIP is an embedding model, trained to produce joint embeddings of both texts and images. “Introduction to Embedding” on page 134 discusses embeddings in detail. For now, you can think of embeddings as vectors that aim to capture the meanings of the original data. Multimodal embedding models like CLIP are the back-bones of generative multimodal models, such as Flamingo, LLaVA, and Gemini (previously Bard).

Foundation models also mark the transition from task-specific models to general-purpose models. Previously, models were often developed for specific tasks, such as sentiment analysis or translation. A model trained for sentiment analysis wouldn’t be able to do translation, and vice versa.

Foundation models, thanks to their scale and the way they are trained, are capable of a wide range of tasks. Out of the box, general-purpose models can work relatively well for many tasks. An LLM can do both sentiment analysis and translation. However, you can often tweak a general-purpose model to maximize its performance on a specific task.

Figure 1-4 shows the tasks used by the Super-NaturalInstructions benchmark to evaluate foundation models (Wang et al., 2022), providing an idea of the types of tasks a foundation model can perform.

Imagine you’re working with a retailer to build an application to generate product descriptions for their website. An out-of-the-box model might be able to generate accurate descriptions but might fail to capture the brand’s voice or highlight the brand’s messaging. The generated descriptions might even be full of marketing speech and cliches.

Figure 1-4. The range of tasks in the Super-NaturalInstructions benchmark (Wang et
al., 2022).
There are multiple techniques you can use to get the model to generate what you
want. For example, you can craft detailed instructions with examples of the desirable
product descriptions. This approach is prompt engineering . You can connect the
model to a database of customer reviews that the model can leverage to generate bet‐
ter descriptions. Using a database to supplement the instructions is called retrievalaugmented generation (RAG). You can also finetune—further train—the model on a
dataset of high-quality product descriptions.
Prompt engineering, RAG, and finetuning are three very common AI engineering
techniques that you can use to adapt a model to your needs. The rest of the book will
discuss all of them in detail.
The Rise of AI Engineering | 11

[Visual content extracted via GLM-OCR]

There are multiple techniques you can use to get the model to generate what you want. For example, you can craft detailed instructions with examples of the desirable product descriptions. This approach is prompt engineering. You can connect the model to a database of customer reviews that the model can leverage to generate better descriptions. Using a database to supplement the instructions is called retrieval-augmented generation (RAG). You can also finetune—further train—the model on a dataset of high-quality product descriptions.

Prompt engineering, RAG, and finetuning are three very common AI engineering techniques that you can use to adapt a model to your needs. The rest of the book will discuss all of them in detail.
