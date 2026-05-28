# Kortex

Kortex is a local-first knowledge compiler with graph-first retrieval for AI
agents and humans.

It turns source material into source-grounded notes, builds a lightweight graph
as the routing index, and helps agents read the real Markdown files before
answering with citations.

## Status

Kortex is in early foundation development. The current code includes:

- project initialization
- canonical note/source models
- Obsidian Markdown rendering
- deterministic graph generation
- built-in BM25 fallback search
- graph-first context retrieval

Conversion, OCR, LLM note extraction, scheduling, and UI are planned after the
core foundation is stable.

## Development

Run tests:

```powershell
$env:PYTHONPATH="src"
python -m unittest discover -s tests -v
```

Smoke test the CLI:

```powershell
$tmp = Join-Path $env:TEMP "kortex-smoke"
Remove-Item -LiteralPath $tmp -Recurse -Force -ErrorAction SilentlyContinue
$env:PYTHONPATH="src"
python -m kortex.cli init --root $tmp
python -m kortex.cli status --root $tmp
python -m kortex.cli doctor --root $tmp
```

## Retrieval Principle

The graph is an index, not source truth. Kortex uses the graph to route a
question to candidate notes or sources, then reads the real Markdown files before
answering.

## License

Apache-2.0.
