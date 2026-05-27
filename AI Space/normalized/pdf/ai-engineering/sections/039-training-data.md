---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 039
section-title: Training Data
source-location: pages 74-74
previous-section: AI Space/normalized/pdf/ai-engineering/sections/038-chapter-2.-understanding-foundation-models.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/040-multilingual-models.md
classification: reusable-knowledge-candidate
---
# Training Data

As mentioned in Chapter 1 , a model’s training process is often divided into pretraining and post-training. Pre-training makes a model capable, but not necessarily
safe or easy to use. This is where post-training comes in. The goal of post-training is
to align the model with human preferences. But what exactly is human preference ?
How can it be represented in a way that a model can learn? The way a model devel‐
oper aligns their model has a significant impact on the model’s usability, and will be
discussed in this chapter.
While most people understand the impact of training on a model’s performance, the
impact of sampling is often overlooked. Sampling is how a model chooses an output
from all possible options. It is perhaps one of the most underrated concepts in AI.
Not only does sampling explain many seemingly baffling AI behaviors, including hal‐
lucinations and inconsistencies, but choosing the right sampling strategy can also sig‐
nificantly boost a model’s performance with relatively little effort. For this reason,
sampling is the section that I was the most excited to write about in this chapter.
Concepts covered in this chapter are fundamental for understanding the rest of the
book. However, because these concepts are fundamental, you might already be famil‐
iar with them. Feel free free to skip any concept that you’re confident about. If you
encounter a confusing concept later on, you can revisit this chapter.
Training Data
An AI model is only as good as the data it was trained on. If there’s no Vietnamese in
the training data, the model won’t be able to translate from English into Vietnamese.
Similarly, if an image classification model sees only animals in its training set, it
won’t perform well on photos of plants.
If you want a model to improve on a certain task, you might want to include more
data for that task in the training data. However, collecting sufficient data for training
a large model isn’t easy, and it can be expensive. Model developers often have to rely
on available data, even if this data doesn’t exactly meet their needs.
For example, a common source for training data is Common Crawl , created by a
nonprofit organization that sporadically crawls websites on the internet. In 2022 and
2023, this organization crawled approximately 2–3 billion web pages each month.
Google provides a clean subset of Common Crawl called the Colossal Clean Crawled
Corpus, or C4 for short.
The data quality of Common Crawl, and C4 to a certain extent, is questionable—
think clickbait, misinformation, propaganda, conspiracy theories, racism, misogyny,
and every sketchy website you’ve ever seen or avoided on the internet. A study by the
Washington Post shows that the 1,000 most common websites in the dataset include
several media outlets that rank low on NewsGuard’s scale for trustworthiness . In lay
terms, Common Crawl contains plenty of fake news.
50 | Chapter 2: Understanding Foundation Models
