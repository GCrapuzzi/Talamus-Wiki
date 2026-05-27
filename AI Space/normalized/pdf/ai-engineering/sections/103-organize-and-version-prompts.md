---
source-path: AI Space/raw/pdf/2026-05-26-AI-Engineering.pdf
source-type: pdf
source-hash: sha256:9abebdd89b8af99937dc91d5be8c366b7dce449dfbdcef570277604b01bcbf40
captured-at: 2026-05-26T14:33:37.604511+00:00
parser: pypdf
parser-confidence: 1.0
section-id: 103
section-title: Organize and Version Prompts
source-location: pages 257-258
previous-section: AI Space/normalized/pdf/ai-engineering/sections/102-evaluate-prompt-engineering-tools.md
next-section: AI Space/normalized/pdf/ai-engineering/sections/104-defensive-prompt-engineering.md
classification: reusable-knowledge-candidate
---
# Organize and Version Prompts

11 Hamel Husain codified this philosophy wonderfully in his blog post “Show Me the Prompt”  (February 14,
2024).
On top of that, any prompt engineering tool can change without warning. They
might switch to different prompt templates or rewrite their default prompts. The
more tools you use, the more complex your system becomes, increasing the potential
for errors.
Following the keep-it-simple principle, you might want to start by writing your own
prompts without any tool. This will give you a better understanding of the underlying
model and your requirements.
If you use a prompt engineering tool, always inspect the prompts produced by that
tool to see whether these prompts make sense and track how many API calls it gener‐
ates.11 No matter how brilliant tool developers are, they can make mistakes, just like
everyone else.
Organize and Version Prompts
It’s good practice to separate prompts from code—you’ll see why in a moment. For
example, you can put your prompts in a file prompts.py and reference these prompts
when creating a model query. Here’s an example of what this might look like:
file: prompts.py
GPT4o_ENTITY_EXTRACTION_PROMPT = [YOUR PROMPT]
file: application.py
from prompts import GPT4o_ENTITY_EXTRACTION_PROMPT
def query_openai(model_name, user_prompt):
    completion = client.chat.completions.create(
    model=model_name,
    messages=[
        {"role": "system", "content": GPT4o_ENTITY_EXTRACTION_PROMPT},
        {"role": "user", "content": user_prompt}
    ]
)
This approach has several advantages:
Reusability
Multiple applications can reuse the same prompt.
Testing
Code and prompts can be tested separately. For example, code can be tested with
different prompts.
Readability
Separating prompts from code makes both easier to read.
Prompt Engineering Best Practices | 233

Collaboration
This allows subject matter experts to collaborate and help with devising prompts
without getting distracted by code.
If you have a lot of prompts across multiple applications, it’s useful to give each
prompt metadata so that you know what prompt and use case it’s intended for. You
might also want to organize your prompts in a way that makes it possible to search
for prompts by models, applications, etc. For example, you can wrap each prompt in
a Python object as follows:
from pydantic import BaseModel
class Prompt(BaseModel):
    model_name: str
    date_created: datetime
    prompt_text: str
    application: str
    creator: str
Your prompt template might also contain other information about how the prompt
should be used, such as the following:
• The model endpoint URL
• The ideal sampling parameters, like temperature or top-p
• The input schema
• The expected output schema (for structured outputs)
Several tools have proposed special .prompt file formats to store prompts. See Google
Firebase’s Dotprompt , Humanloop, Continue Dev, and Promptfile. Here’s an exam‐
ple of Firebase Dotprompt file:
---
model: vertexai/gemini-1.5-flash
input:
  schema:
    theme: string
output:
  format: json
  schema:
    name: string
    price: integer
    ingredients(array): string
---
Generate a menu item that could be found at a {{theme}} themed restaurant.
If the prompt files are part of your git repository, these prompts can be versioned
using git. The downside of this approach is that if multiple applications share the
same prompt and this prompt is updated, all applications dependent on this prompt
234 | Chapter 5: Prompt Engineering
