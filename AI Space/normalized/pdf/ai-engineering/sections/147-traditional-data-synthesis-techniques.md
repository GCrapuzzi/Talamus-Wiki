---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 147
section-title: Traditional Data Synthesis Techniques
source-location: pages 407-409
previous-section: AI Space/normalized/pdf/ai-engineering/sections/146-why-data-synthesis.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/148-ai-powered-data-synthesis.md
classification: reusable-knowledge-candidate
---
# Traditional Data Synthesis Techniques

10 Many awesome games are possible only because of procedural generation. Games like Minecraft and No
Man’s Sky  use noise functions and fractal algorithms to create vast, immersive worlds. In Dungeons & Drag‐
ons, procedural generation can be used to create random dungeons, quests, and encounters, making the game
more appealing by adding an element of unpredictability and endless possibilities.
Traditional Data Synthesis Techniques
Data synthesis isn’t unique to AI. It has a long history in software testing, gaming,
and robotics. Using algorithms to generate data is also called procedural generation,
as opposed to manual generation. Procedural generation is commonly used in gam‐
ing to generate content such as levels, maps, items, and characters on the fly. 10 Most
data generation techniques used in these industries can be applied to AI.
Traditionally, two approaches for data synthesis and augmentation have been rulebased and simulation. A newer method made possible by advanced AI models is
using AI itself to synthesize data. This section gives a quick overview of these two tra‐
ditional techniques before moving on to AI-powered data synthesis in the next
section.
Rule-based data synthesis
The simplest way to generate data is to use predefined rules and templates. For exam‐
ple, to create a credit card transaction, start with a transaction template and use a
random generator like Faker to populate each field in this template:
An example of a transaction template.
Transaction ID: [Unique Identifier]
Date: [MM/DD/YYYY]
Time: [HH:MM:SS]
Amount: [Transaction Amount]
Merchant Name: [Merchant/Store Name]
Merchant Category: [Category Code]
Location: [City, State, Country]
Payment Method: [Credit Card/Debit Card/Cash/Online Payment]
Transaction Status: [Completed/Pending/Failed]
Description: [Transaction Description]
Due to the sensitivity of transaction data, many fraud detection models are first
trained on synthetic transaction data generated from templates like this to prove their
feasibility before being given access to real data.
Data Augmentation and Synthesis | 383

It’s common to use templates to generate documents that follow a specific structure,
such as invoices, resumes, tax forms, bank statements, event agendas, product cata‐
logs, contracts, configuration files, etc. Templates can also be used to generate data
that follows a certain grammar and syntax, such as regular expressions and math
equations. You can use templates to generate math equations for AI models to solve.
DeepMind trained an Olympiad-level geometry model, AlphaGeometry, using 100
million synthetic examples (Trinh et al., 2024).
You can procedurally generate new data from existing data by applying simple trans‐
formations. For images, you can randomly rotate, crop, scale, or erase part of an
image. A flipped image of a cat should still be a cat. A slightly cropped image of a
soccer game should still be a soccer game. Krizhevsky et al. (2012)  demonstrated in
their legendary AlexNet paper the usefulness of this technique by using it to augment
the ImageNet dataset (Deng et al., 2009).
For texts, you can randomly replace a word with a similar word, assuming that this
replacement wouldn’t change the meaning or the sentiment of the sentence. For
example, the original sentence “She’s a fantastic nurse” can generate a new example:
“She’s a great nurse”.
This approach can be used to mitigate potential biases in your data. If you’re con‐
cerned that there’s a gender bias in your data, where, for example, the word “nurse” is
associated with women while the word “doctor” is associated with men, you can
replace typically gendered words with their opposites, such as “she” with “he”, as
shown in Table 8-2.
Table 8-2. Data augmentation can help mitigate certain biases in your data.
Original data Augmented data
She’s a fantastic nurse. He’s a fantastic nurse.
She’s a fantastic doctor.
The CEO of the firm, Mr. Alex Wang, … The CEO of the firm, Ms. Alexa Wang, …
Today, my mom made a casserole for dinner. Today, my dad made a casserole for dinner.
Emily has always loved the violin. Mohammed has always loved the violin.
Similar words can be found either with a dictionary of synonymous words or by find‐
ing words whose embeddings are close to each other in a word embedding space. You
can go beyond simple word replacement by asking AI to rephrase or translate an
example, as we’ll discuss later.
384 | Chapter 8: Dataset Engineering

One interesting transformation is perturbation: adding noise to existing data to gen‐
erate new data. Initially, researchers discovered that perturbing a data sample slightly
can trick models into misclassifying it. For example, adding white noise to a picture
of a ship can cause the model to misclassify it as a car. The paper “One Pixel Attack
for Fooling Deep Neural Networks” ( Su et al., 2017) showed that 67.97% of the natu‐
ral images in the Kaggle CIFAR-10 test dataset and 16.04% of the ImageNet test
images could be misclassified by changing just one pixel. This poses a serious risk if
exploited. An attacker could trick an AI model into misidentifying them as an
authorized employee or make a self-driving car mistake a divider for a lane, leading
to accidents.
You can train your model on perturbed data. Perturbation can both improve the
model’s performance and make it more robust against attacks; see Goodfellow et al.,
2013 and Moosavi-Dezfooli et al., 2015 ). In 2019, Hendrycks and Dietterich created
ImageNet-C and ImageNet-P  by applying 15 common visual corruptions, such as
changing brightness, adding snow, changing contrast, and adding noises to ImageNet
images.
Perturbation can also be used for texts. For example, to train BERT, the authors
replaced 1.5% of the tokens with random words ( Devlin et al., 2018). They found this
perturbation led to a small performance boost.
Visual data can be augmented using more sophisticated algorithms. Snap (2022) has
a great case study on how they augment their assets to create unrepresented corner
cases and mitigate implicit biases in their data. Given a character, they synthesize
similar characters but with different skin colors, body types, hairstyles, clothes, and
even facial expressions. These augmented assets are then used to train AI models.
Simulation
Instead of running experiments to collect data in the real world, where it can be
expensive and dangerous, you can simulate these experiments virtually. For example,
to test how a self-driving car reacts when encountering a horse on the highway,
it’d be dangerous to release an actual horse on the highway. Instead, you simulate this
situation in a virtual environment. Examples of self-driving simulation engines
include CARLA (Dosovitskiy et al., 2017), Waymo’s SimulationCity , and Tesla’s sim‐
ulation of San Francisco.
Data Augmentation and Synthesis | 385
