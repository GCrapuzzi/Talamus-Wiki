# Release checklist

Run before tagging a release. Nothing ships with a red gate.

## Quality

- [ ] `python dev.py` green (ruff + mypy + unittest) on the release commit
- [ ] CI green on Windows / macOS / Linux (including the `extras` job: ui+pdf)
- [ ] `python -m mkdocs build --strict` clean
- [ ] Fresh venv install: `pip install -e ".[dev,mcp]"` then `talamus --version`,
      `talamus demo`, `talamus search "embedding"`

## Measurement (PRD §17.2)

- [ ] `talamus eval --cases examples/eval-cases-real.json` run and recorded
- [ ] `talamus eval --scale --sizes 100,1000,10000` meets latency targets (11.1)
- [ ] Benchmark artifacts updated under `docs/benchmarks/`

## Claims & docs

- [ ] README claims match reality, each labelled shipped / experimental / roadmap
- [ ] CHANGELOG updated; commands in docs match `talamus --help`
- [ ] Cache migrations documented (current: v2 — migrate with `talamus reindex`)

## Safety (PRD §17.4)

- [ ] No `.claude/`, caches or brains committed (`git status` clean of them)
- [ ] Scan defaults still exclude secret-like files; redaction tests green
- [ ] Destructive commands still require confirmation or explicit flags

## Runtime (manual, needs a display)

- [ ] `talamus ui` opens; Chat / Cerca / Note / Review / Ontologia render
- [ ] `talamus ui --web --port 8550` serves in a browser; narrow width readable
- [ ] MCP handshake with a real client (`talamus mcp install` + `/mcp`)
