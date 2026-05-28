# Kortex Agent Tool Calling Guide

Kortex exposes simple CLI commands that agent frameworks can wrap as tools.

## Graph Routing

```powershell
kortex graph query "<question>"
```

Purpose: identify candidate notes or source sections. The graph is an index, not
the answer source.

## Note Reading

```powershell
kortex notes read <note-id-or-path>
```

Purpose: read real final note content before answering.

## Lexical Fallback

```powershell
kortex search "<query>"
```

Purpose: recover candidates when graph routing is insufficient.

## Source Reading

```powershell
kortex sources read <source-section-id-or-path>
```

Purpose: inspect normalized sources when final notes do not contain enough
information.

## Validation

```powershell
kortex validate
```

Purpose: check links, provenance, graph/index freshness, and project structure.

## Review Queue

```powershell
kortex review list
```

Purpose: inspect low-confidence conversion, missing concepts, and items needing
human judgment.
