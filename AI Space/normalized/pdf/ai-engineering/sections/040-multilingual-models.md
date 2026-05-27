---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 040
section-title: Multilingual Models
source-location: pages 75-79
previous-section: AI Space/normalized/pdf/ai-engineering/sections/039-training-data.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/041-domain-specific-models.md
classification: reusable-knowledge-candidate
---
# Multilingual Models

Yet, simply because Common Crawl is available, variations of it are used in most
foundation models that disclose their training data sources, including OpenAI’s
GPT-3 and Google’s Gemini. I suspect that Common Crawl is also used in models
that don’t disclose their training data. To avoid scrutiny from both the public and
competitors, many companies have stopped disclosing this information.
Some teams use heuristics to filter out low-quality data from the internet. For exam‐
ple, OpenAI used only the Reddit links that received at least three upvotes to train
GPT-2. While this does help screen out links that nobody cares about, Reddit isn’t
exactly the pinnacle of propriety and good taste.
The “use what we have, not what we want” approach may lead to models that per‐
form well on tasks present in the training data but not necessarily on the tasks you
care about. To address this issue, it’s crucial to curate datasets that align with your
specific needs. This section focuses on curating data for specific languages and
domains, providing a broad yet specialized foundation for applications within those
areas. Chapter 8 explores data strategies for models tailored to highly specific tasks.
While language- and domain-specific foundation models can be trained from
scratch, it’s also common to finetune them on top of general-purpose models.
Some might wonder, why not just train a model on all data available, both general
data and specialized data, so that the model can do everything? This is what many
people do. However, training on more data often requires more compute resources
and doesn’t always lead to better performance. For example, a model trained with a
smaller amount of high-quality data might outperform a model trained with a large
amount of low-quality data. Using 7B tokens of high-quality coding data, Gunasekar
et al. (2023) were able to train a 1.3B-parameter model that outperforms much larger
models on several important coding benchmarks. The impact of data quality is dis‐
cussed more in Chapter 8.
Multilingual Models
English dominates the internet. An analysis of the Common Crawl dataset shows that
English accounts for almost half of the data (45.88%), making it eight times more
prevalent than the second-most common language, Russian (5.97%) (Lai et al., 2023).
See Table 2-1 for a list of languages with at least 1% in Common Crawl. Languages
with limited availability as training data—typically languages not included in this list
—are considered low-resource.
Training Data | 51

Table 2-1. The most common languages in Common Crawl, a popular dataset for training
LLMs. Source: Lai et al. (2023).
Language Code Pop. CC size
  (M) (%) Cat.
English en 1,452 45.8786 H
Russian ru 258 5.9692 H
German de 134 5.8811 H
Chinese zh 1,118 4.8747 H
Japanese jp 125 4.7884 H
French fr 274 4.7254 H
Spanish es 548 4.4690 H
Italian it 68 2.5712 H
Dutch nl 30 2.0585 H
Polish pl 45 1.6636 H
Portuguese pt 257 1.1505 H
Vietnamese vi 85 1.0299 H
Many other languages, despite having a lot of speakers today, are severely underrepresented in Common Crawl. Table 2-2 shows some of these languages. Ideally, the
ratio between world population representation and Common Crawl representation
should be 1. The higher this ratio, the more under-represented this language is in
Common Crawl.
Table 2-2. Examples of under-represented languages in Common Crawl. The last row,
English, is for comparison. The numbers for % in Common Crawl are taken from Lai et al.
(2023).
Language Speakers (million) % world population a % in Common Crawl World: Common Crawl Ratio
Punjabi 113 1.41% 0.0061% 231.56
Swahili 71 0.89% 0.0077% 115.26
Urdu 231 2.89% 0.0274% 105.38
Kannada 64 0.80% 0.0122% 65.57
Telugu 95 1.19% 0.0183% 64.89
Gujarati 62 0.78% 0.0126% 61.51
Marathi 99 1.24% 0.0213% 58.10
Bengali 272 3.40% 0.0930% 36.56
English 1452 18.15% 45.88% 0.40
a A world population of eight billion was used for this calculation.
52 | Chapter 2: Understanding Foundation Models

Given the dominance of English in the internet data, it’s not surprising that generalpurpose models work much better for English than other languages, according to
multiple studies. For example, on the MMLU benchmark, a suite of 14,000 multiplechoice problems spanning 57 subjects, GPT-4 performed much better in English than
under-represented languages like Telugu, as shown in Figure 2-1 (OpenAI, 2023).
Figure 2-1. On the MMLU benchmark, GPT-4 performs better in English than in any
other language. To obtain MMLU in other languages, OpenAI translated the questions
using Azure AI Translator.
Training Data | 53

[Visual content extracted via GLM-OCR]

Given the dominance of English in the internet data, it’s not surprising that general-purpose models work much better for English than other languages, according to multiple studies. For example, on the MMLU benchmark, a suite of 14,000 multiple-choice problems spanning 57 subjects, GPT-4 performed much better in English than under-represented languages like Telugu, as shown in Figure 2-1 (OpenAI, 2023).

Figure 2-1. On the MMLU benchmark, GPT-4 performs better in English than in any other language. To obtain MMLU in other languages, OpenAI translated the questions using Azure AI Translator.

1 “GPT-4 Can Solve Math Problems—but Not in All Languages”  by Yennie Jun. You can verify the study using
OpenAI’s Tokenizer .
Similarly, when tested on six math problems on Project Euler, Yennie Jun found that
GPT-4 was able to solve problems in English more than three times as often com‐
pared to Armenian or Farsi. 1 GPT-4 failed in all six questions for Burmese and
Amharic, as shown in Figure 2-2.
Figure 2-2. GPT-4 is much better at math in English than in other languages.
Under-representation is a big reason for this underperformance. The three languages
that have the worst performance on GPT-4’s MMLU benchmarks—Telugu, Marathi,
and Punjabi—are also among the languages that are most under-represented in
Common Crawl. However, under-representation isn’t the only reason. A language’s
structure and the culture it embodies can also make a language harder for a model to
learn.
Given that LLMs are generally good at translation, can we just translate all queries
from other languages into English, obtain the responses, and translate them back into
the original language? Many people indeed follow this approach, but it’s not ideal.
First, this requires a model that can sufficiently understand under-represented lan‐
guages to translate. Second, translation can cause information loss. For example,
some languages, like Vietnamese, have pronouns to denote the relationship between
the two speakers. When translating into English, all these pronouns are translated
into I and you, causing the loss of the relationship information.
54 | Chapter 2: Understanding Foundation Models

[Visual content extracted via GLM-OCR]

Similarly, when tested on six math problems on Project Euler, Yennie Jun found that GPT-4 was able to solve problems in English more than three times as often compared to Armenian or Farsi. GPT-4 failed in all six questions for Burmese and Amharic, as shown in Figure 2-2.

Figure 2-2. GPT-4 is much better at math in English than in other languages.

Under-representation is a big reason for this underperformance. The three languages that have the worst performance on GPT-4’s MMLU benchmarks—Telugu, Marathi, and Punjabi—are also among the languages that are most under-represented in Common Crawl. However, under-representation isn’t the only reason. A language’s structure and the culture it embodies can also make a language harder for a model to learn.

Given that LLMs are generally good at translation, can we just translate all queries from other languages into English, obtain the responses, and translate them back into the original language? Many people indeed follow this approach, but it’s not ideal. First, this requires a model that can sufficiently understand under-represented languages to translate. Second, translation can cause information loss. For example, some languages, like Vietnamese, have pronouns to denote the relationship between the two speakers. When translating into English, all these pronouns are translated into I and you, causing the loss of the relationship information.

1 “GPT-4 Can Solve Math Problems—but Not in All Languages” by Yennie Jun. You can verify the study using OpenAI’s Tokenizer.

2 It might be because of some biases in pre-training data or alignment data. Perhaps OpenAI just didn’t include
as much data in the Chinese language or China-centric narratives to train their models.
Models can also have unexpected performance challenges in non-English languages.
For example, NewsGuard found that ChatGPT is more willing to produce misinfor‐
mation in Chinese than in English. In April 2023, NewsGuard asked ChatGPT-3.5 to
produce misinformation articles about China in English, simplified Chinese, and tra‐
ditional Chinese. For English, ChatGPT declined to produce false claims for six out
of seven prompts. However, it produced false claims in simplified Chinese and tradi‐
tional Chinese all seven times. It’s unclear what causes this difference in behavior. 2
Other than quality issues, models can also be slower and more expensive for nonEnglish languages. A model’s inference latency and cost is proportional to the num‐
ber of tokens in the input and response. It turns out that tokenization can be much
more efficient for some languages than others. Benchmarking GPT-4 on MASSIVE, a
dataset of one million short texts translated across 52 languages, Yennie Jun found
that, to convey the same meaning, languages like Burmese and Hindi require a lot
more tokens than English or Spanish. For the MASSIVE dataset, the median token
length in English is 7, but the median length in Hindi is 32, and in Burmese, it’s a
whopping 72, which is ten times longer than in English.
Assuming that the time it takes to generate a token is the same in all languages,
GPT-4 takes approximately ten times longer in Burmese than in English for the same
content. For APIs that charge by token usage, Burmese costs ten times more than
English.
To address this, many models have been trained to focus on non-English languages.
The most active language, other than English, is undoubtedly Chinese, with
ChatGLM, YAYI, Llama-Chinese, and others. There are also models in French
(CroissantLLM), Vietnamese (PhoGPT), Arabic (Jais), and many more languages.
Training Data | 55
