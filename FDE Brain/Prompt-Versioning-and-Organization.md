---
type: pattern
tags: [prompt-engineering, versioning, prompt-management, MLOps]
sources:
  - AI Space/normalized/pdf/ai-engineering.md#organize-and-version-prompts
captured-at: 2026-05-26T08:07:41.859415+00:00
ingestion-run: 82c4eb8c
---

# Prompt Versioning and Organization

Separate prompts from application code for reusability, testability, readability, and cross-functional collaboration.

### Basic pattern
```python
# prompts.py
GPT4o_ENTITY_EXTRACTION_PROMPT = "..."

# application.py
from prompts import GPT4o_ENTITY_EXTRACTION_PROMPT
```

### Prompt metadata (Pydantic example)
```python
class Prompt(BaseModel):
    model_name: str
    date_created: datetime
    prompt_text: str
    application: str
    creator: str
```

Optional metadata: model endpoint URL, sampling parameters (temperature, top-p), input/output schemas.

### Dedicated prompt file formats
Tools like Firebase Dotprompt, Humanloop, Continue Dev define `.prompt` files with YAML frontmatter + template body.

### Git-versioned vs. Prompt Catalog
- **Git-versioned:** Simple but forces all dependent applications to use the latest prompt version.
- **Prompt catalog:** Explicitly versions each prompt; different apps can pin to different versions. Should support metadata, search, and dependency notifications.

A well-implemented catalog tracks which applications depend on each prompt and notifies owners of updates.
