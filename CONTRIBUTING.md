# Contributing to Talamus

Thanks for your interest! Talamus is local-first and stdlib-only at the core, with
optional adapters behind extras.

## Setup

```bash
pip install -e ".[dev,mcp]"
```

## The quality gate

One command runs everything (lint, format, types, tests):

```bash
python dev.py            # check
python dev.py --fix      # autofix lint + format, then check
```

This must be green before a change is merged. CI runs the same gate on
Windows / macOS / Linux across Python 3.11–3.13.

- **Lint & format**: `ruff` (line length 100).
- **Types**: `mypy` (the core is fully typed).
- **Tests**: `python -m unittest discover -s tests`. Add a focused test with each change.

## Conventions

- Core (`src/talamus/`) stays **Python stdlib-only**; new dependencies go behind an
  optional extra and an adapter.
- The graph is an **index, not the truth**; notes (Markdown + cache JSON) are the truth.
- Keep modules small and single-purpose; follow the existing patterns.

## Docs

```bash
pip install -e ".[docs]"
mkdocs serve            # preview the docs site at http://127.0.0.1:8000
```

## Pull requests

Keep changes focused, explain the *why*, and make sure the gate is green.

## Releases

PyPI publishing uses Trusted Publishing, not repository secrets. To publish a
release:

1. Update `version` in `pyproject.toml`.
2. Run `python dev.py`.
3. Commit and push the version change.
4. Create a GitHub release tagged `vX.Y.Z`, matching the exact
   `pyproject.toml` version.

The `Publish to PyPI` workflow builds the package, checks the distributions,
and uploads them to PyPI through the `pypi` GitHub environment. Configure the
PyPI Trusted Publisher for project `talamus` with owner `GCrapuzzi`, repository
`Talamus-Wiki`, workflow `publish.yml`, and environment `pypi`.

## Where the project truth lives

Start from [AGENTS.md](AGENTS.md) (yes, even as a human — it is the entry
point for everyone), then the developer canon in `dev/`:
[CONSTRAINTS.md](dev/CONSTRAINTS.md) (binding rules and why),
[ARCHITECTURE.md](dev/ARCHITECTURE.md) (how every part works),
[STATE.md](dev/STATE.md) (what is built, measured, rejected — and the open
queue), [PRODUCT.md](dev/PRODUCT.md) (the final product definition).
