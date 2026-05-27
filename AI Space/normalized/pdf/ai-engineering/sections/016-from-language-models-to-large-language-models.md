---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 016
section-title: From Language Models to Large Language Models
source-location: pages 26-31
previous-section: AI Space/normalized/pdf/ai-engineering/sections/015-the-rise-of-ai-engineering.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/017-from-large-language-models-to-foundation-models.md
classification: reusable-knowledge-candidate
---
# From Language Models to Large Language Models

1 In this book, I use traditional ML to refer to all ML before foundation models.
large-scale, readily available models brings about new possibilities and new chal‐
lenges, which are the focus of this book.
This chapter begins with an overview of foundation models, the key catalyst behind
the explosion of AI engineering. I’ll then discuss a range of successful AI use cases,
each illustrating what AI is good and not yet good at. As AI’s capabilities expand
daily, predicting its future possibilities becomes increasingly challenging. However,
existing application patterns can help uncover opportunities today and offer clues
about how AI may continue to be used in the future.
To close out the chapter, I’ll provide an overview of the new AI stack, including what
has changed with foundation models, what remains the same, and how the role of an
AI engineer today differs from that of a traditional ML engineer.1
The Rise of AI Engineering
Foundation models emerged from large language models, which, in turn, originated
as just language models. While applications like ChatGPT and GitHub’s Copilot may
seem to have come out of nowhere, they are the culmination of decades of technology
advancements, with the first language models emerging in the 1950s. This section
traces the key breakthroughs that enabled the evolution from language models to AI
engineering.
From Language Models to Large Language Models
While language models have been around for a while, they’ve only been able to grow
to the scale they are today with self-supervision. This section gives a quick overview of
what language model and self-supervision mean. If you’re already familiar with those,
feel free to skip this section.
Language models
A language model encodes statistical information about one or more languages. Intui‐
tively, this information tells us how likely a word is to appear in a given context. For
example, given the context “My favorite color is __”, a language model that encodes
English should predict “blue” more often than “car”.
2 | Chapter 1: Introduction to Building AI Applications with Foundation Models

2 For non-English languages, a single Unicode character can sometimes be represented as multiple tokens.
The statistical nature of languages was discovered centuries ago. In the 1905 story
“The Adventure of the Dancing Men” , Sherlock Holmes leveraged simple statistical
information of English to decode sequences of mysterious stick figures. Since the
most common letter in English is E, Holmes deduced that the most common stick
figure must stand for E.
Later on, Claude Shannon used more sophisticated statistics to decipher enemies’
messages during the Second World War. His work on how to model English was
published in his 1951 landmark paper “Prediction and Entropy of Printed English” .
Many concepts introduced in this paper, including entropy, are still used for lan‐
guage modeling today.
In the early days, a language model involved one language. However, today, a lan‐
guage model can involve multiple languages.
The basic unit of a language model is token. A token can be a character, a word, or a
part of a word (like -tion), depending on the model. 2 For example, GPT-4, a model
behind ChatGPT, breaks the phrase “I can’t wait to build AI applications” into nine
tokens, as shown in Figure 1-1. Note that in this example, the word “can’t” is broken
into two tokens, can and ’t . You can see how different OpenAI models tokenize text
on the OpenAI website.
Figure 1-1. An example of how GPT-4 tokenizes a phrase.
The process of breaking the original text into tokens is called tokenization. For
GPT-4, an average token is approximately ¾ the length of a word . So, 100 tokens are
approximately 75 words.
The set of all tokens a model can work with is the model’s vocabulary. You can use a
small number of tokens to construct a large number of distinct words, similar to how
you can use a few letters in the alphabet to construct many words. The Mixtral 8x7B
model has a vocabulary size of 32,000. GPT-4’s vocabulary size is 100,256. The toke‐
nization method and vocabulary size are decided by model developers.
The Rise of AI Engineering | 3

[Visual content extracted via GLM-OCR]

The statistical nature of languages was discovered centuries ago. In the 1905 story “The Adventure of the Dancing Men”, Sherlock Holmes leveraged simple statistical information of English to decode sequences of mysterious stick figures. Since the most common letter in English is E, Holmes deduced that the most common stick figure must stand for E.

Later on, Claude Shannon used more sophisticated statistics to decipher enemies’ messages during the Second World War. His work on how to model English was published in his 1951 landmark paper “Prediction and Entropy of Printed English”. Many concepts introduced in this paper, including entropy, are still used for language modeling today.

In the early days, a language model involved one language. However, today, a language model can involve multiple languages.

The basic unit of a language model is token. A token can be a character, a word, or a part of a word (like -tion), depending on the model. For example, GPT-4, a model behind ChatGPT, breaks the phrase “I can’t wait to build AI applications” into nine tokens, as shown in Figure 1-1. Note that in this example, the word “can’t” is broken into two tokens, can and t. You can see how different OpenAI models tokenize text on the OpenAI website.

Figure 1-1. An example of how GPT-4 tokenizes a phrase.

The process of breaking the original text into tokens is called tokenization. For GPT-4, an average token is approximately ¾ the length of a word. So, 100 tokens are approximately 75 words.

The set of all tokens a model can work with is the model’s vocabulary. You can use a small number of tokens to construct a large number of distinct words, similar to how you can use a few letters in the alphabet to construct many words. The Mixtral 8x7B model has a vocabulary size of 32,000. GPT-4’s vocabulary size is 100,256. The tokenization method and vocabulary size are decided by model developers.

2 For non-English languages, a single Unicode character can sometimes be represented as multiple tokens.

3 Autoregressive language models are sometimes referred to as causal language models.
Why do language models use token as their unit instead of word or
character? There are three main reasons:
1. Compared to characters, tokens allow the model to break
words into meaningful components. For example, “cooking”
can be broken into “cook” and “ing”, with both components
carrying some meaning of the original word.
2. Because there are fewer unique tokens than unique words, this
reduces the model’s vocabulary size, making the model more
efficient (as discussed in Chapter 2).
3. Tokens also help the model process unknown words. For
instance, a made-up word like “chatgpting” could be split into
“chatgpt” and “ing”, helping the model understand its struc‐
ture. Tokens balance having fewer units than words while
retaining more meaning than individual characters.
There are two main types of language models: masked language models  and autore‐
gressive language models. They differ based on what information they can use to pre‐
dict a token:
Masked language model
A masked language model is trained to predict missing tokens anywhere in a
sequence, using the context from both before and after the missing tokens . In
essence, a masked language model is trained to be able to fill in the blank. For
example, given the context, “My favorite __ is blue”, a masked language model
should predict that the blank is likely “color”. A well-known example of a
masked language model is bidirectional encoder representations from transform‐
ers, or BERT (Devlin et al., 2018).
As of writing, masked language models are commonly used for non-generative
tasks such as sentiment analysis and text classification. They are also useful for
tasks requiring an understanding of the overall context, such as code debugging,
where a model needs to understand both the preceding and following code to
identify errors.
Autoregressive language model
An autoregressive language model is trained to predict the next token in a
sequence, using only the preceding tokens . It predicts what comes next in “My
favorite color is __ .” 3 An autoregressive model can continually generate one
token after another. Today, autoregressive language models are the models of
4 | Chapter 1: Introduction to Building AI Applications with Foundation Models

[Visual content extracted via GLM-OCR]

Why do language models use token as their unit instead of word or character? There are three main reasons:

1. Compared to characters, tokens allow the model to break words into meaningful components. For example, “cooking” can be broken into “cook” and “ing”, with both components carrying some meaning of the original word.

2. Because there are fewer unique tokens than unique words, this reduces the model’s vocabulary size, making the model more efficient (as discussed in Chapter 2).

3. Tokens also help the model process unknown words. For instance, a made-up word like “chatgpting” could be split into “chatgpt” and “ing”, helping the model understand its structure. Tokens balance having fewer units than words while retaining more meaning than individual characters.

There are two main types of language models: masked language models and autoregressive language models. They differ based on what information they can use to predict a token:

**Masked language model**

A masked language model is trained to predict missing tokens anywhere in a sequence, using the context from both before and after the missing tokens. In essence, a masked language model is trained to be able to fill in the blank. For example, given the context, “My favorite __ is blue”, a masked language model should predict that the blank is likely “color”. A well-known example of a masked language model is bidirectional encoder representations from transformers, or BERT (Devlin et al., 2018).

As of writing, masked language models are commonly used for non-generative tasks such as sentiment analysis and text classification. They are also useful for tasks requiring an understanding of the overall context, such as code debugging, where a model needs to understand both the preceding and following code to identify errors.

**Autoregressive language model**

An autoregressive language model is trained to predict the next token in a sequence, using only the preceding tokens. It predicts what comes next in “My favorite color is __.”$^3$ An autoregressive model can continually generate one token after another. Today, autoregressive language models are the models of

$^3$ Autoregressive language models are sometimes referred to as causal language models.

4 Technically, a masked language model like BERT can also be used for text generations if you try really hard.
choice for text generation, and for this reason, they are much more popular than
masked language models.4
Figure 1-2 shows these two types of language models.
Figure 1-2. Autoregressive language model and masked language model.
In this book, unless explicitly stated, language model will refer to an
autoregressive model.
The outputs of language models are open-ended. A language model can use its fixed,
finite vocabulary to construct infinite possible outputs. A model that can generate
open-ended outputs is called generative, hence the term generative AI.
You can think of a language model as a completion machine: given a text (prompt), it
tries to complete that text. Here’s an example:
Prompt (from user): “To be or not to be”
Completion (from language model): “, that is the question.”
It’s important to note that completions are predictions, based on probabilities, and
not guaranteed to be correct. This probabilistic nature of language models makes
them both so exciting and frustrating to use. We explore this further in Chapter 2.
The Rise of AI Engineering | 5

[Visual content extracted via GLM-OCR]

choice for text generation, and for this reason, they are much more popular than masked language models.4

Figure 1-2 shows these two types of language models.

Figure 1-2. Autoregressive language model and masked language model.

In this book, unless explicitly stated, language model will refer to an autoregressive model.

The outputs of language models are open-ended. A language model can use its fixed, finite vocabulary to construct infinite possible outputs. A model that can generate open-ended outputs is called generative, hence the term generative AI.

You can think of a language model as a completion machine: given a text (prompt), it tries to complete that text. Here’s an example:

Prompt (from user): “To be or not to be”
Completion (from language model): “, that is the question.”

It’s important to note that completions are predictions, based on probabilities, and not guaranteed to be correct. This probabilistic nature of language models makes them both so exciting and frustrating to use. We explore this further in Chapter 2.

4 Technically, a masked language model like BERT can also be used for text generations if you try really hard.

As simple as it sounds, completion is incredibly powerful. Many tasks, including
translation, summarization, coding, and solving math problems, can be framed as
completion tasks. For example, given the prompt: “How are you in French is …”, a
language model might be able to complete it with: “Comment ça va”, effectively
translating from one language to another.
As another example, given the prompt:
Question: Is this email likely spam? Here’s the email: <email content>
Answer:
A language model might be able to complete it with: “Likely spam”, which turns this
language model into a spam classifier.
While completion is powerful, completion isn’t the same as engaging in a conversa‐
tion. For example, if you ask a completion machine a question, it can complete what
you said by adding another question instead of answering the question. “PostTraining” on page 78  discusses how to make a model respond appropriately to a user’s
request.
Self-supervision
Language modeling is just one of many ML algorithms. There are also models for
object detection, topic modeling, recommender systems, weather forecasting, stock
price prediction, etc. What’s special about language models that made them the cen‐
ter of the scaling approach that caused the ChatGPT moment?
The answer is that language models can be trained using self-supervision, while many
other models require supervision. Supervision refers to the process of training ML
algorithms using labeled data, which can be expensive and slow to obtain. Selfsupervision helps overcome this data labeling bottleneck to create larger datasets for
models to learn from, effectively allowing models to scale up. Here’s how.
With supervision, you label examples to show the behaviors you want the model to
learn, and then train the model on these examples. Once trained, the model can be
applied to new data. For example, to train a fraud detection model, you use examples
of transactions, each labeled with “fraud” or “not fraud”. Once the model learns from
these examples, you can use this model to predict whether a transaction is fraudulent.
The success of AI models in the 2010s lay in supervision. The model that started the
deep learning revolution, AlexNet ( Krizhevsky et al., 2012 ), was supervised. It was
trained to learn how to classify over 1 million images in the dataset ImageNet. It clas‐
sified each image into one of 1,000 categories such as “car”, “balloon”, or “monkey”.
6 | Chapter 1: Introduction to Building AI Applications with Foundation Models

5 The actual data labeling cost varies depending on several factors, including the task’s complexity, the scale
(larger datasets typically result in lower per-sample costs), and the labeling service provider. For example, as
of September 2024, Amazon SageMaker Ground Truth charges 8 cents per image for labeling fewer than
50,000 images, but only 2 cents per image for labeling more than 1 million images.
6 This is similar to how it’s important for humans to know when to stop talking.
A drawback of supervision is that data labeling is expensive and time-consuming. If it
costs 5 cents for one person to label one image, it’d cost $50,000 to label a million
images for ImageNet. 5 If you want two different people to label each image—so that
you could cross-check label quality—it’d cost twice as much. Because the world con‐
tains vastly more than 1,000 objects, to expand models’ capabilities to work with
more objects, you’d need to add labels of more categories. To scale up to 1 million
categories, the labeling cost alone would increase to $50 million.
Labeling everyday objects is something that most people can do without prior train‐
ing. Hence, it can be done relatively cheaply. However, not all labeling tasks are that
simple. Generating Latin translations for an English-to-Latin model is more expen‐
sive. Labeling whether a CT scan shows signs of cancer would be astronomical.
Self-supervision helps overcome the data labeling bottleneck. In self-supervision,
instead of requiring explicit labels, the model can infer labels from the input data.
Language modeling is self-supervised because each input sequence provides both the
labels (tokens to be predicted) and the contexts the model can use to predict these
labels. For example, the sentence “I love street food.” gives six training samples, as
shown in Table 1-1.
Table 1-1. Training samples from the sentence “I love street food.” for language modeling.
Input (context) Output (next token)
<BOS> I
<BOS>, I love
<BOS>, I, love street
<BOS>, I, love, street food
<BOS>, I, love, street, food .
<BOS>, I, love, street, food, . <EOS>
In Table 1-1 , <BOS> and <EOS> mark the beginning and the end of a sequence.
These markers are necessary for a language model to work with multiple sequences.
Each marker is typically treated as one special token by the model. The end-ofsequence marker is especially important as it helps language models know when to
end their responses.6
The Rise of AI Engineering | 7
