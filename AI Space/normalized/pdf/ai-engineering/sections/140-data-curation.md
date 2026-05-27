---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 140
section-title: Data Curation
source-location: pages 389-391
previous-section: AI Space/normalized/pdf/ai-engineering/sections/139-chapter-8.-dataset-engineering.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/141-data-quality.md
classification: reusable-knowledge-candidate
---
# Data Curation

2 If you use a lot of data, ensuring data compliance alone can be a full-time job.
The model-centric and data-centric division helps guide research. In reality, however,
meaningful technological progress often requires investment in both model and data
improvements.
Data Curation
While not all issues with AI models can be solved with data, data is often a key part of
the solution. The right data can make the model more capable, safer, and able to han‐
dle longer contexts. Conversely, poor data can cause the model to increase biases and
hallucinations. Mistakes in data can harm the model and waste resources.
Data curation is a science that requires understanding how the model learns and
what resources are available to help it learn. Dataset builders should work closely
with application and model developers. In a small team, they might be the same
person—the  person responsible for training a model is also responsible for acquiring
the data for it. However, organizations with high data demands often employ special‐
ized roles.2
What data you need depends on your task and what you want to teach the model. For
self-supervised finetuning, you need sequences of data. For instruction finetuning,
you need data in the (instruction, response) format. For preference finetuning, you
need data in the (instruction, winning response, losing response) format. To train a
reward model, you can use the same data format as preference finetuning or use data
with annotated scores for each of your examples in the ((instruction, response),
score) format.
Training data should exhibit the behaviors you want your model to learn. Acquiring
high-quality data annotations is always challenging, but it’s even more challenging if
you want to teach models complex behaviors such as chain-of-thought (CoT) reason‐
ing and tool use. Let’s go over these two examples to understand why:
Chain-of-thought
As discussed in Chapter 5, CoT prompting nudges the model to work through a
problem step-by-step before producing the final answer. To teach a model to
generate step-by-step responses, its training data should include CoT responses.
“Scaling Instruction-Finetuned Language Models” ( Chun et al., 2024) shows that
incorporating step-by-step responses in the finetuning data greatly enhances the
performance of models of various sizes on CoT tasks, with accuracy nearly dou‐
bling for certain tasks.
Data Curation | 365

Generating multi-step responses can be tedious and time-consuming—explain‐
ing how to solve a math problem step-by-step is much more challenging than
simply giving the final answer. To illustrate this, here are two examples, one with
only the final answer and one with CoT. Both are from Chun et al. (2024):
Instruction: Please answer the following question. What is the boil
ing point of Nitrogen?
Response (without CoT): -320.4F
CoT instruction: Answer the following question by reasoning step-bystep. The cafeteria had 23 apples. If they used 20 for lunch and
bought 6 more, how many apples do they have?
Response (with CoT) : The cafeteria had 23 apples originally. They
used 20 to make lunch. So they had 23 - 20 = 3. They bought 6 more
apples, so they have 3 + 6 = 9.
As a result, CoT datasets are less common compared to other instruction
datasets.
Tool use
Given the vast amount of knowledge a model acquires during pre-training, many
models might intuitively know how to use certain tools. However, a model’s tool
use ability can be improved by showing it tool use examples. It’s common to use
domain experts to create tool use data, where each prompt is a task that requires
tool use, and its response is the actions needed to perform that task. For example,
if you want data to finetune a model to act as a personal assistant, you might
want to ask professional personal assistants what types of tasks they usually per‐
form, how they perform them, and what tools they need. If you ask human
experts to explain how they do things, they might miss certain steps, either
because of faulty memory or because they might think these steps aren’t impor‐
tant. It’s often necessary to observe how humans perform these tasks to ensure
accuracy.
However, what’s efficient for humans might not be efficient for AI, and vice
versa. As a result, human annotations might not be ideal for AI agents. For
example, a human might prefer a web interface, whereas it’s easier for a model to
use an API. To search for something, a human might first open a browser, copy
and paste that query into the search bar, and click on each result. Meanwhile, a
model can just send a request to the search API with the query and process all
the results at once. For this reason, many rely on simulations and other synthetic
techniques to generate tool use data, as explored later in this chapter.
366 | Chapter 8: Dataset Engineering

Tool use data might also require special formats. In typical conversation data, the
user and AI take turns, with each turn containing one message. However, for tool
use, the AI might need to generate multiple messages each turn, with each mes‐
sage sent to a different location. For example, it might send one message to the
code interpreter and one message to the user (such as to inform the user what it’s
doing). To support this, Llama 3 authors ( Dubey et al., 2024 ) designed a multimessage chat format that consists of message headers that specify the source and
destination of each message, and special termination tokens to specify where the
human and AI turns start.
When curating data for applications with conversation interfaces, you need to con‐
sider whether you require single-turn data, multi-turn data, or both. Single-turn data
helps train a model to respond to individual instructions. Multi-turn data, on the
other hand, teaches the model how to solve tasks—many real-world tasks involve
back-and-forth. For instance, when given a query, a model may need to first clarify
the user’s intent before addressing the task. After the model’s response, the user
might provide corrections or additional information for the next step.
Single-turn data is simpler and, therefore, easier to obtain. Multi-turn data often
requires purpose-built scenarios or more involved interactions to capture.
Data curation isn’t just about creating new data to help a model learn new behaviors
but is also about removing existing data to help a model unlearn bad behaviors.
Imagine you work on a chatbot like ChatGPT and you hear user complaints that the
chatbot is a bit arrogant, annoying users and wasting their tokens. For example, when
a user asks it to verify if a statement is factually correct, the chatbot responds with:
“The statement is correct, but its style can be improved to be better.” It then contin‐
ues to produce an unsolicited rewriting of the statement.
You investigate and find that in the training data, there are several examples of anno‐
tations with unsolicited suggestions. You put in a request to remove these examples
from the training data and another request to acquire new examples that demonstrate
fact-checking without unsolicited rewriting.
Each application might require data of different characteristics. Different training
phases also require different data mixes. At a high level, however, data curation fol‐
lows the three criteria: data quality, data coverage, and data quantity.
To give an intuition about these terms, if you think of model training as cooking, the
data fed into the model is the ingredients. Data quality is equivalent to the quality of
the ingredients—you can’t have good food if your ingredients are spoiled. Data cov‐
erage is equivalent to having the right mix of ingredients (e.g., you shouldn’t have too
much or too little sugar). Data quantity is about how many ingredients you should
have. Let’s explore these terms in detail.
Data Curation | 367
