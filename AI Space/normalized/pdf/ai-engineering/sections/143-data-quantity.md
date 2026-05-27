---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 143
section-title: Data Quantity
source-location: pages 396-400
previous-section: AI Space/normalized/pdf/ai-engineering/sections/142-data-coverage.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/144-data-acquisition-and-annotation.md
classification: reusable-knowledge-candidate
---
# Data Quantity

Figure 8-1. A 7B-parameter model, finetuned on a dataset that is both high-quality and
diverse, outperforms that same model finetuned on a dataset that is either diverse or
high-quality. Image from Zhou et al. (2023). The image is licensed under CC BY 4.0.
Data Quantity
Asking how much data you need is like asking how much money you need. The
answer varies widely from one situation to the next. At one extreme, Jeremy Howard
and Jonathan Whitaker  did a fun experiment to show that LLMs can learn from a
single example. At another extreme, some teams have finetuned models with millions
of examples.
While millions of examples sounds like a lot, it’s small compared to the data typically
needed to train a foundation model from scratch. For reference, Llama 2 and Llama 3
were trained using 2 trillion and 16 trillion tokens, respectively. If each example is
2,000 tokens, it’d be equivalent to 1 billion and 15 billion examples.
372 | Chapter 8: Dataset Engineering

[Visual content extracted via GLM-OCR]

Data Quantity

Asking how much data you need is like asking how much money you need. The answer varies widely from one situation to the next. At one extreme, Jeremy Howard and Jonathan Whitaker did a fun experiment to show that LLMs can learn from a single example. At another extreme, some teams have finetuned models with millions of examples.

While millions of examples sounds like a lot, it’s small compared to the data typically needed to train a foundation model from scratch. For reference, Llama 2 and Llama 3 were trained using 2 trillion and 16 trillion tokens, respectively. If each example is 2,000 tokens, it’d be equivalent to 1 billion and 15 billion examples.

You might wonder: if I have millions of examples, shouldn’t I just
train a model from scratch? You can and should evaluate whether
training a model from scratch would improve your performance.
While finetuning on top of a pre-trained model is typically more
efficient than training from scratch, there are situations when fine‐
tuning can be worse, especially when you have a lot of training
data. This is due to a phenomenon called ossification, where pretraining can ossify (i.e., freeze) the model weights so that they don’t
adapt as well to the finetuning data ( Hernandez et al., 2021 ).
Smaller models are more susceptible to ossification than larger
models.
Other than data quality and data diversity, three other factors influence how much
data you need:
Finetuning techniques
Full finetuning promises to give the best performance, but it requires orders of
magnitude more data than PEFT methods like LoRA. If you have tens of thou‐
sands to millions of (instruction, response) pairs, you might want to attempt full
finetuning. If you have only a few hundred or a few thousand examples, PEFT
might work best.
Task complexity
A simple task, such as classifying whether a product review is positive or nega‐
tive, will require much less data than a complex task, such as a question answer‐
ing about financial filings.
Base model’s performance
The closer the base model is to the desirable performance, the fewer examples are
needed to get there. Assuming that bigger base models are better, you might need
fewer examples to finetune big models. This is the opposite of pre-training,
where bigger models need more training data.
OpenAI’s finetuning guide  shows that if you have fewer examples (100), more
advanced models give you better finetuning performance. This is likely because the
more advanced models already perform better out of the box. However, after finetun‐
ing on a lot of examples (550,000), all five models in the experiment performed simi‐
larly, as illustrated in Figure 8-2.
Data Curation | 373

[Visual content extracted via GLM-OCR]

You might wonder: if I have millions of examples, shouldn’t I just train a model from scratch? You can and should evaluate whether training a model from scratch would improve your performance. While finetuning on top of a pre-trained model is typically more efficient than training from scratch, there are situations when finetuning can be worse, especially when you have a lot of training data. This is due to a phenomenon called ossification, where pre-training can ossify (i.e., freeze) the model weights so that they don’t adapt as well to the finetuning data (Hernandez et al., 2021). Smaller models are more susceptible to ossification than larger models.

Other than data quality and data diversity, three other factors influence how much data you need:

**Finetuning techniques**
Full finetuning promises to give the best performance, but it requires orders of magnitude more data than PEFT methods like LoRA. If you have tens of thousands to millions of (instruction, response) pairs, you might want to attempt full finetuning. If you have only a few hundred or a few thousand examples, PEFT might work best.

**Task complexity**
A simple task, such as classifying whether a product review is positive or negative, will require much less data than a complex task, such as a question answering about financial filings.

**Base model’s performance**
The closer the base model is to the desirable performance, the fewer examples are needed to get there. Assuming that bigger base models are better, you might need fewer examples to finetune big models. This is the opposite of pre-training, where bigger models need more training data.

OpenAI’s finetuning guide shows that if you have fewer examples (100), more advanced models give you better finetuning performance. This is likely because the more advanced models already perform better out of the box. However, after finetuning on a lot of examples (550,000), all five models in the experiment performed similarly, as illustrated in Figure 8-2.

Figure 8-2. With 100 examples, more advanced models give much better performance
after finetuning. With 550,000 examples, all models give similar performance after
finetuning. Experiments done by Stanford Natural Language Inference (SNLI) Corpus.
In short, if you have a small amount of data, you might want to use PEFT methods on
more advanced models. If you have a large amount of data, use full finetuning with
smaller models.
Before investing in curating a large dataset, you might want to start with a small,
well-crafted dataset (e.g., 50 examples) to see if finetuning can improve the model. If
this small dataset is sufficient to achieve your desirable performance, that’s great.
Clear improvements suggest that more data will improve the performance even
more. If no improvement is observed with small data, a bigger dataset will rarely do
the trick.
However, be careful before concluding that finetuning with a small dataset doesn’t
improve a model. Many things, other than data, can impact finetuning’s results, such
as the choice of hyperparameters (e.g., the learning rate is too high or too low), data
quality, poorly crafted prompts, etc. In the vast majority of cases, you should see
improvements after finetuning with 50–100 examples.
374 | Chapter 8: Dataset Engineering

[Visual content extracted via GLM-OCR]

Figure 8-2. With 100 examples, more advanced models give much better performance after finetuning. With 550,000 examples, all models give similar performance after finetuning. Experiments done by Stanford Natural Language Inference (SNLI) Corpus.

In short, if you have a small amount of data, you might want to use PEFT methods on more advanced models. If you have a large amount of data, use full finetuning with smaller models.

Before investing in curating a large dataset, you might want to start with a small, well-crafted dataset (e.g., 50 examples) to see if finetuning can improve the model. If this small dataset is sufficient to achieve your desirable performance, that’s great. Clear improvements suggest that more data will improve the performance even more. If no improvement is observed with small data, a bigger dataset will rarely do the trick.

However, be careful before concluding that finetuning with a small dataset doesn’t improve a model. Many things, other than data, can impact finetuning’s results, such as the choice of hyperparameters (e.g., the learning rate is too high or too low), data quality, poorly crafted prompts, etc. In the vast majority of cases, you should see improvements after finetuning with 50–100 examples.

6 In Designing Machine Learning Systems, I also covered other techniques to reduce the demand for annotated
data, including weak supervision, semi-supervision, and active learning.
It’s possible to reduce the amount of high-quality data needed by
first finetuning your model using lower-quality or less-relevant
data. Here are three examples of this approach:
Self-supervised → supervised
You want to finetune a model to answer legal questions. Your
(question, answer) set is small, but you have many legal docu‐
ments. You can first finetune your model on legal documents
in a self-supervised manner, then further finetune the model
on (question, answer) pairs.
Less-relevant data → relevant data
You want to finetune a model to classify sentiments for prod‐
uct reviews, but you have little product sentiment data and
much more tweet sentiment data. You can first finetune your
model to classify tweet sentiments, then further finetune it to
classify product sentiments.
Synthetic data → real data
You want to finetune a model to predict medical conditions
from medical reports. Due to the sensitive nature of this task,
your data is limited. You can use AI models to synthesize a
large amount of data to finetune your model first, then further
finetune it on your real data. This approach is harder to get
right, as you’ll have to do two distinct finetuning jobs while
coordinating the transitioning between them. If you don’t
know what you’re doing, you might end up using more com‐
pute just to produce a model worse than what you would’ve
gotten by just finetuning with high-quality data.6
Experimenting with a small dataset can help you estimate how much more data you’ll
need. You can finetune a model on subsets of your current dataset—e.g., 25%, 50%,
100%—and plot how performance scales with dataset size. A steep performance gain
slope with increasing dataset size means that you can expect significant performance
improvement by doubling your data. A plateau slope means that doubling your data
will give only a small improvement. Figure 8-3 shows an example of this plot.
Data Curation | 375

[Visual content extracted via GLM-OCR]

It’s possible to reduce the amount of high-quality data needed by first finetuning your model using lower-quality or less-relevant data. Here are three examples of this approach:

Self-supervised → supervised
You want to finetune a model to answer legal questions. Your (question, answer) set is small, but you have many legal documents. You can first finetune your model on legal documents in a self-supervised manner, then further finetune the model on (question, answer) pairs.

Less-relevant data → relevant data
You want to finetune a model to classify sentiments for product reviews, but you have little product sentiment data and much more tweet sentiment data. You can first finetune your model to classify tweet sentiments, then further finetune it to classify product sentiments.

Synthetic data → real data
You want to finetune a model to predict medical conditions from medical reports. Due to the sensitive nature of this task, your data is limited. You can use AI models to synthesize a large amount of data to finetune your model first, then further finetune it on your real data. This approach is harder to get right, as you’ll have to do two distinct finetuning jobs while coordinating the transitioning between them. If you don’t know what you’re doing, you might end up using more compute just to produce a model worse than what you would’ve gotten by just finetuning with high-quality data.$^6$

Experimenting with a small dataset can help you estimate how much more data you’ll need. You can finetune a model on subsets of your current dataset—e.g., 25%, 50%, 100%—and plot how performance scales with dataset size. A steep performance gain slope with increasing dataset size means that you can expect significant performance improvement by doubling your data. A plateau slope means that doubling your data will give only a small improvement. Figure 8-3 shows an example of this plot.

$^6$ In *Designing Machine Learning Systems*, I also covered other techniques to reduce the demand for annotated data, including weak supervision, semi-supervision, and active learning.

Figure 8-3. The performance gain curve with different dataset sizes can help you esti‐
mate the impact of additional training examples on your model’s performance.
The performance gain curve shown in Figure 8-3 is fairly typical. In most cases, addi‐
tional training examples yield diminishing returns: the same number of examples
typically gives a lower performance boost as the dataset grows. For example, the first
1,000 examples might improve a model’s accuracy by ten percentage points, but the
next 1,000 examples might only improve it by five.
While a larger number of finetuning examples generally improves a model’s perfor‐
mance, the diversity of the examples matters, too. The paper “Scaling InstructionFinetuned Language Models” ( Chung et al., 2022 ) shows that model performance
increased significantly when the number of finetuning tasks increased from 9 to 282.
Beyond 282 tasks, the performance gains started to plateau, though there were still
positive but incremental improvements up to 1,836 tasks, as shown in Figure 8-4 .
This suggests that the model benefits greatly from exposure to a diverse set of tasks
during finetuning.
The diversity of data can be reflected in task types (such as summarization and ques‐
tion answering), topic diversity (such as fashion, finance, and technology), and the
expected output formats (such as JSON outputs or yes-or-no answers).
376 | Chapter 8: Dataset Engineering

[Visual content extracted via GLM-OCR]

The performance gain curve shown in Figure 8-3 is fairly typical. In most cases, additional training examples yield diminishing returns: the same number of examples typically gives a lower performance boost as the dataset grows. For example, the first 1,000 examples might improve a model’s accuracy by ten percentage points, but the next 1,000 examples might only improve it by five.

While a larger number of finetuning examples generally improves a model’s performance, the diversity of the examples matters, too. The paper “Scaling Instruction-Finetuned Language Models” (Chung et al., 2022) shows that model performance increased significantly when the number of finetuning tasks increased from 9 to 282. Beyond 282 tasks, the performance gains started to plateau, though there were still positive but incremental improvements up to 1,836 tasks, as shown in Figure 8-4. This suggests that the model benefits greatly from exposure to a diverse set of tasks during finetuning.

The diversity of data can be reflected in task types (such as summarization and question answering), topic diversity (such as fashion, finance, and technology), and the expected output formats (such as JSON outputs or yes-or-no answers).
