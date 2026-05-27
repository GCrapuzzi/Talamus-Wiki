---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 019
section-title: Foundation Model Use Cases
source-location: pages 40-43
previous-section: AI Space/normalized/pdf/ai-engineering/sections/018-from-foundation-models-to-ai-engineering.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/020-coding.md
classification: reusable-knowledge-candidate
---
# Foundation Model Use Cases

10 Fun fact: as of September 16, 2024, the website theresanaiforthat.com lists 16,814 AIs for 14,688 tasks and
4,803 jobs.
The rapidly expanding community of AI engineers has demonstrated remarkable
creativity with an incredible range of exciting applications. The next section will
explore some of the most common application patterns.
Foundation Model Use Cases
If you’re not already building AI applications, I hope the previous section has con‐
vinced you that now is a great time to do so. If you have an application in mind, you
might want to jump to “Planning AI Applications” on page 28. If you’re looking for
inspiration, this section covers a wide range of industry-proven and promising use
cases.
The number of potential applications that you could build with foundation models
seems endless. Whatever use case you think of, there’s probably an AI for that. 10 It’s
impossible to list all potential use cases for AI.
Even attempting to categorize these use cases is challenging, as different surveys use
different categorizations. For example, Amazon Web Services (AWS) has categorized
enterprise generative AI use cases into three buckets: customer experience, employee
productivity, and process optimization. A 2024 O’Reilly survey  categorized the use
cases into eight categories: programming, data analysis, customer support, marketing
copy, other copy, research, web design, and art.
Some organizations, like Deloitte, have categorized use cases by value capture, such
as cost reduction, process efficiency, growth, and accelerating innovation. For value
capture, Gartner has a category for business continuity , meaning an organization
might go out of business if it doesn’t adopt generative AI. Of the 2,500 executives
Gartner surveyed in 2023, 7% cited business continuity as the motivation for embrac‐
ing generative AI.
16 | Chapter 1: Introduction to Building AI Applications with Foundation Models

Eloundou et al. (2023)  has excellent research on how exposed different occupations
are to AI. They defined a task as exposed if AI and AI-powered software can reduce
the time needed to complete this task by at least 50%. An occupation with 80% expo‐
sure means that 80% of the occupation’s tasks are exposed. According to the study,
occupations with 100% or close to 100% exposure include interpreters and transla‐
tors, tax preparers, web designers, and writers. Some of them are shown in Table 1-2.
Not unsurprisingly, occupations with no exposure to AI include cooks, stonemasons,
and athletes. This study gives a good idea of what use cases AI is good for.
Table 1-2. Occupations with the highest exposure to AI as annotated by humans. α refers to
exposure to AI models directly, whereas β and ζ refer to exposures to AI-powered software.
Table from Eloundou et al. (2023).
Group Occupations with highest exposure % Exposure
Human αInterpreters and translators
Survey researchers
Poets, lyricists, and creative writers
Animal scientists
Public relations specialists
76.5
75.0
68.8
66.7
66.7
Human βSurvey researchers
Writers and authors
Interpreters and translators
Public relations specialists
Animal scientists
84.4
82.5
82.4
80.6
77.8
Human ζMathematicians
Tax preparers
Financial quantitative analysts
Writers and authors
Web and digital interface designers
Humans labeled 15 occupations as “fully exposed”.
100.0
100.0
100.0
100.0
100.0
Foundation Model Use Cases | 17

11 Exploring different AI applications is perhaps one of my favorite things about writing this book. It’s a lot of
fun seeing what people are building. You can find the list of open source AI applications that I track. The list
is updated every 12 hours.
When analyzing the use cases, I looked at both enterprise and consumer applications.
To understand enterprise use cases, I interviewed 50 companies on their AI strategies
and read over 100 case studies. To understand consumer applications, I examined
205 open source AI applications with at least 500 stars on GitHub. 11 I categorized
applications into eight groups, as shown in Table 1-3. The limited list here serves best
as a reference. As you learn more about how to build foundation models in Chapter 2
and how to evaluate them in Chapter 3, you’ll also be able to form a better picture of
what use cases foundation models can and should be used for.
Table 1-3. Common generative AI use cases across consumer and enterprise applications.
Category Examples of consumer use cases Examples of enterprise use cases
Coding Coding Coding
Image and video
production
Photo and video editing
Design
Presentation
Ad generation
Writing Email
Social media and blog posts
Copywriting, search engine optimization (SEO)
Reports, memos, design docs
Education Tutoring
Essay grading
Employee onboarding
Employee upskill training
Conversational bots General chatbot
AI companion
Customer support
Product copilots
Information aggregation Summarization
Talk-to-your-docs
Summarization
Market research
Data organization Image search
Memex
Knowledge management
Document processing
Workflow automation Travel planning
Event planning
Data extraction, entry, and annotation
Lead generation
Because foundation models are general, applications built on top of them can solve
many problems. This means that an application can belong to more than one cate‐
gory. For example, a bot can provide companionship and aggregate information. An
application can help you extract structured data from a PDF and answer questions
about that PDF.
Figure 1-7 shows the distribution of these use cases among the 205 open source appli‐
cations. Note that the small percentage of education, data organization, and writing
use cases doesn’t mean that these use cases aren’t popular. It just means that these
applications aren’t open source. Builders of these applications might find them more
suitable for enterprise use cases.
18 | Chapter 1: Introduction to Building AI Applications with Foundation Models

The enterprise world generally prefers applications with lower risks. For example, a 2024 a16z Growth report showed that companies are faster to deploy internal-facing applications (internal knowledge management) than external-facing applications (customer support chatbots), as shown in Figure 1-8. Internal applications help companies develop their AI engineering expertise while minimizing the risks associated with data privacy, compliance, and potential catastrophic failures. Similarly, while foundation models are open-ended and can be used for any task, many applications built on top of them are still close-ended, such as classification. Classification tasks are easier to evaluate, which makes their risks easier to estimate.

How willing are enterprises to use LLMs for different use cases?
(% of enterprises experimenting with given use case who have deployed to production)

Figure 1-8. Companies are more willing to deploy internal-facing applications
