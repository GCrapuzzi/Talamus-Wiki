---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 152
section-title: Deduplicate Data
source-location: pages 423-424
previous-section: AI Space/normalized/pdf/ai-engineering/sections/151-inspect-data.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/153-clean-and-filter-data.md
classification: reusable-knowledge-candidate
---
# Deduplicate Data

There are many data exploration tools you should use, but they won’t be replace‐
ments for manual data inspection. In every project I’ve worked on, staring at data
for just  15 minutes usually gives me some insight that could save me hours of head‐
aches. Greg Brockman, an OpenAI co-founder , tweeted: “Manual inspection of data
has probably the highest value-to-prestige ratio of any activity in machine learning.”
Look at your data to see if the examples make sense. If it’s annotated data, pick out a
few queries and try to annotate them yourself to see if your annotations match the
given annotations. This will give you a sense of how trustworthy the annotations are.
Fact-check the responses. How unique are the examples? Are there any examples
with the same query but with different responses? Are there any examples with the
same responses but with different queries?
Deduplicate Data
Duplicated data can skew the data distribution and introduce biases into your model.
Imagine a dataset that looks like Table 8-3 . The duplicated entries might lead the
model to the wrong conclusion that all red-colored items should be expensive. Dupli‐
cations can cause test set contamination. When splitting duplicated data into train
and test sets, one example might be in the train set and its duplicate in the test set.
Table 8-3. A toy dataset with duplicate examples in grey cells.
Input (Product description) Output (Price)
1 {item: pencil, color: red} $20
2 {item: compass, color: green} $2
3 {item: pencil, color: red} $20
4 {item: pencil, color: red} $20
5 {item: pencil, color: green} $1
Multiple studies have shown the negative impact of training data duplications on
model performance; see Lee et al. (2021)  and Tirumala et al. (2023) . An Anthropic
study demonstrated that repeating 0.1% of the data 100 times can cause an 800M
parameter model’s performance to degrade to that of a 400M parameter model
despite the other 90% of the training tokens remaining unique ( Hernandez et al.,
2022). Even when duplications don’t hurt your model’s performance, they can waste
your time and compute.
Depending on the data, there are many forms of duplication, some of which are
harder to detect. For example, here are a few types of duplications in a dataset of
documents:
Data Processing | 399

16 One of my open source libraries, lazyNLP, also supports overlap estimation and deduplication using Bloom
filter.
• Whole document duplications: the same document appearing more than once.
• Intra-document duplications: e.g., the same paragraph appears twice in one
document.
• Cross-document duplications: e.g., the same popular quote appears in multiple
documents.
What can be considered duplications also depends on your definition. For example,
do you want to deal with duplications at the document level, paragraph level, sen‐
tence level, or token level? Would two texts have to match exactly to be considered
duplicates, or would an 80% overlap be sufficient? Are two lists considered duplicates
if they have the same items but in different order?
The task of deduplication can leverage the same techniques used for similarity meas‐
urements (discussed in Chapter 3). Data deduplication is also used for identity reso‐
lution, determining whether two identities (e.g., two social media profiles) are the
same. Here are some concrete ways you can deduplicate data:
Pairwise comparison
Compute the similarity score of each example to every other example in the data‐
set, using exact match, n-gram match, fuzzy match, or semantic similarity score,
as discussed in Chapter 3 . This approach can be expensive with large datasets,
however.
Hashing
Hash examples into different buckets and check only among examples that fall
into the same bucket. Hash-related deduplication methods include MinHash and
Bloom filter.
Dimensionality reduction
Use a dimensionality reduction technique to first reduce the dimensions of your
data and then do a pairwise comparison. Many techniques used for vector
search, as discussed in Chapter 6, can be used for this.
A quick search will return many libraries that help with deduplication. Some of them
are dupeGuru, Dedupe, datasketch, TextDistance, TheFuzz, and deduplicate-textdatasets.16
400 | Chapter 8: Dataset Engineering
