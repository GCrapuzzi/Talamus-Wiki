# Controlled Rollout Pattern for Local-First LLM Wikis

The controlled rollout pattern is an operational pattern for evolving a local-first LLM wiki without letting a single large source dominate the system before the ingestion pipeline is proven.

The pattern has four steps:

1. First, checkpoint the current workspace state so existing notes, raw sources, normalized packages, and graph artifacts are not silently overwritten.
2. Second, run a tiny known source through the full ingestion path: pending capture, raw archival, normalized Markdown package creation, local section-level distillation, Obsidian note validation, and graph stale marking.
3. Third, inspect the artifacts before processing a large book or course: pending must be empty, the raw original must be preserved, normalized sections must contain provenance, and promoted notes must cite both raw and normalized sources.
4. Fourth, only after the tiny run passes, re-ingest the large source with the same pipeline.

The key decision rule is that graph output is never treated as source truth. Graphify is used for routing: it stores concept labels, aliases, relation hints, confidence, community, source file, source location, and a short summary. The answering agent then reads the actual Markdown files in the Obsidian vault or normalized source packages before drafting an answer.

This pattern is useful for Forward Deployed AI Engineering because implementation work often combines customer-specific material, reusable AI engineering concepts, and operational playbooks. Controlled rollout keeps the workspace auditable while still allowing new reusable knowledge to be promoted quickly into the final Obsidian vault.

If the Brain Graph cannot answer a question and the Source Graph surfaces a stable reusable section, the agent should promote that knowledge into FDE Brain in the same turn unless the user explicitly requested read-only behavior.
