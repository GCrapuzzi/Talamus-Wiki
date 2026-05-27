---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 009
section-title: Conventions Used in This Book
source-location: pages 19-19
previous-section: AI Space/normalized/pdf/ai-engineering/sections/008-navigating-this-book.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/010-using-code-examples.md
classification: reusable-knowledge-candidate
---
# Conventions Used in This Book

production. On the other hand, while the agentic pattern promises to be much more
powerful, it’s also more complex and is still being explored.
Chapter 7 is about how to adapt a model to an application by changing the model
itself with finetuning. Due to the scale of foundation models, native model finetuning
is memory-intensive, and many techniques are developed to allow finetuning better
models with less memory. The chapter covers different finetuning approaches, sup‐
plemented by a more experimental approach: model merging. This chapter contains
a more technical section that shows how to calculate the memory footprint of a
model.
Due to the availability of many finetuning frameworks, the finetuning process itself is
often straightforward. However, getting data for finetuning is hard. The next chapter
is all about data, including data acquisition, data annotations, data synthesis, and data
processing. Many of the topics discussed in Chapter 8 are relevant beyond finetuning,
including the question of what data quality means and how to evaluate the quality of
your data.
If Chapters 5 to 8 are about improving a model’s quality, Chapter 9 is about making
its inference cheaper and faster. It discusses optimization both at the model level and
inference service level. If you’re using a model API—i.e., someone else hosts your
model for you—this API will likely take care of inference optimization for you. How‐
ever, if you host the model yourself—either an open source model or a model devel‐
oped in-house—you’ll need to implement many of the techniques discussed in this
chapter.
The last chapter in the book brings together the different concepts from this book to
build an application end-to-end. The second part of the chapter is more productfocused, with discussions on how to design a user feedback system that helps you col‐
lect useful feedback while maintaining a good user experience.
I often use “we” in this book to mean you (the reader) and I. It’s a
habit I got from my teaching days, as I saw writing as a shared
learning experience for both the writer and the readers.
Conventions Used in This Book
The following typographical conventions are used in this book:
Italic
Indicates new terms, URLs, email addresses, filenames, and file extensions.
Preface | xvii

[Visual content extracted via GLM-OCR]

production. On the other hand, while the agentic pattern promises to be much more powerful, it’s also more complex and is still being explored.

Chapter 7 is about how to adapt a model to an application by changing the model itself with finetuning. Due to the scale of foundation models, native model finetuning is memory-intensive, and many techniques are developed to allow finetuning better models with less memory. The chapter covers different finetuning approaches, supplemented by a more experimental approach: model merging. This chapter contains a more technical section that shows how to calculate the memory footprint of a model.

Due to the availability of many finetuning frameworks, the finetuning process itself is often straightforward. However, getting data for finetuning is hard. The next chapter is all about data, including data acquisition, data annotations, data synthesis, and data processing. Many of the topics discussed in Chapter 8 are relevant beyond finetuning, including the question of what data quality means and how to evaluate the quality of your data.

If Chapters 5 to 8 are about improving a model’s quality, Chapter 9 is about making its inference cheaper and faster. It discusses optimization both at the model level and inference service level. If you’re using a model API—i.e., someone else hosts your model for you—this API will likely take care of inference optimization for you. However, if you host the model yourself—either an open source model or a model developed in-house—you’ll need to implement many of the techniques discussed in this chapter.

The last chapter in the book brings together the different concepts from this book to build an application end-to-end. The second part of the chapter is more product-focused, with discussions on how to design a user feedback system that helps you collect useful feedback while maintaining a good user experience.

I often use “we” in this book to mean you (the reader) and I. It’s a habit I got from my teaching days, as I saw writing as a shared learning experience for both the writer and the readers.

Conventions Used in This Book

The following typographical conventions are used in this book:

Italic
Indicates new terms, URLs, email addresses, filenames, and file extensions.
