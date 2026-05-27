# Core Graph-First Foundation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Introduce the generic open-source core for a local-first knowledge pipeline: project initialization, canonical note models, Obsidian rendering, deterministic graph generation, graph-first retrieval, BM25 fallback, and agent-facing guidance.

**Architecture:** Add a new generic package under `src/brain/` while leaving the existing `tools/fde_brain/` workspace-specific code intact during migration. The new package owns product-level concepts (`knowledge/raw`, `knowledge/normalized`, `knowledge/notes`, `knowledge/graph`, `knowledge/index`) and exposes a beginner CLI named `brain`. This plan implements the working core retrieval foundation; conversion adapters and LLM note extraction are handled by separate follow-up implementation plans.

**Tech Stack:** Python 3.13 standard library, `unittest`, Markdown, JSON, Apache-2.0 licensing, Obsidian Markdown rendering, deterministic JSON graph, built-in BM25 fallback.

---

## Scope Check

The approved design covers multiple independent subsystems:

- source conversion and OCR
- LLM note extraction
- storage adapters
- deterministic graph
- lexical fallback search
- ask/retrieval
- agent skills and tool calling
- beginner CLI and update infrastructure

This implementation plan intentionally covers **Foundation V1** only:

- Apache-2.0 project packaging
- generic `brain` package under `src/brain/`
- `brain init`, `brain status`, and `brain doctor`
- generic project paths and config
- canonical note/source models
- Obsidian rendering adapter
- same-batch wikilink resolution
- deterministic graph builder and graph query
- built-in BM25 fallback index
- `brain ask context` graph-first context bundle
- agent skill and tool-calling documentation

Deferred from this foundation plan:

- Docling PDF conversion
- OCR/VLM adapters
- LLM note extraction prompts
- ingestion from arbitrary `pending` files
- migration or removal of the legacy `tools/fde_brain` prototype
- final packaging release to PyPI
- UI

Next implementation plans should cover:

1. Conversion adapters and validated normalized packages.
2. Rich canonical note extraction and validation.
3. Workspace migration or retirement of `tools/fde_brain` after `src/brain` is stable.
4. Update infrastructure and release automation.

## File Structure

- Create: `LICENSE`
  - Apache-2.0 license for the open-source core.
- Create: `pyproject.toml`
  - Package metadata, console script, test discovery, optional adapter extras.
- Modify: `.gitignore`
  - Ignore local package/build artifacts while preserving knowledge folders.
- Create: `src/brain/__init__.py`
  - Package marker and version.
- Create: `src/brain/paths.py`
  - Generic product path model for `knowledge/*`.
- Create: `src/brain/config.py`
  - JSON config load/save with beginner defaults.
- Create: `src/brain/cli.py`
  - Beginner CLI entrypoint with `init`, `status`, `doctor`, `graph`, `search`, `ask`.
- Create: `src/brain/models.py`
  - Canonical source, claim, relation, link, and note dataclasses.
- Create: `src/brain/linking.py`
  - Same-batch and existing-note link registry/resolution.
- Create: `src/brain/storage/__init__.py`
  - Storage adapter package marker.
- Create: `src/brain/storage/obsidian.py`
  - Deterministic Obsidian Markdown renderer.
- Create: `src/brain/graph.py`
  - Deterministic graph build/query from canonical notes.
- Create: `src/brain/search.py`
  - Built-in BM25 fallback index.
- Create: `src/brain/ask.py`
  - Graph-first context bundle builder; answers still come from real note files.
- Create: `skills/brain-knowledge/SKILL.md`
  - Agent-facing skill for using the knowledge base.
- Create: `docs/agent-tool-calling.md`
  - Tool-calling guide for agents and future MCP integration.
- Create: `tests/test_brain_paths_config.py`
  - Tests for config and paths.
- Create: `tests/test_brain_models.py`
  - Tests for canonical model validation helpers.
- Create: `tests/test_brain_obsidian_renderer.py`
  - Tests for Markdown rendering and wikilinks.
- Create: `tests/test_brain_graph.py`
  - Tests for graph build/query.
- Create: `tests/test_brain_search.py`
  - Tests for BM25 fallback.
- Create: `tests/test_brain_ask.py`
  - Tests for graph-first context bundles.
- Create: `tests/test_brain_cli.py`
  - Tests for beginner CLI commands.

---

### Task 1: Apache-2.0 Packaging Foundation

**Files:**
- Create: `LICENSE`
- Create: `pyproject.toml`
- Modify: `.gitignore`
- Create: `src/brain/__init__.py`

- [ ] **Step 1: Write the Apache-2.0 license file**

Create `LICENSE` with the standard Apache License 2.0 text from the Apache Software Foundation.

Verification command:

```powershell
Select-String -Path LICENSE -Pattern "Apache License", "Version 2.0", "limitations under the License"
```

Expected: all three phrases are found.

- [ ] **Step 2: Create package metadata**

Create `pyproject.toml`:

```toml
[build-system]
requires = ["setuptools>=69", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "local-knowledge-brain"
version = "0.1.0"
description = "Local-first knowledge compiler with graph-first retrieval for AI agents."
readme = "README.md"
requires-python = ">=3.11"
license = { text = "Apache-2.0" }
authors = [
  { name = "Local Knowledge Brain Contributors" }
]
dependencies = []

[project.optional-dependencies]
docling = ["docling>=2.0"]
dev = []

[project.scripts]
brain = "brain.cli:main"

[tool.setuptools.packages.find]
where = ["src"]

[tool.unittest]
start-dir = "tests"
```

- [ ] **Step 3: Extend `.gitignore` safely**

If `.gitignore` does not exist, create it. Ensure it contains these entries without removing existing project-specific entries:

```gitignore
# Python packaging
build/
dist/
*.egg-info/

# Python caches
__pycache__/
*.py[cod]

# Local virtual environments
.venv/
venv/
```

- [ ] **Step 4: Create package marker**

Create `src/brain/__init__.py`:

```python
"""Local-first knowledge compiler core."""

__version__ = "0.1.0"
```

- [ ] **Step 5: Verify package metadata**

Run:

```powershell
python -c "import tomllib; print(tomllib.load(open('pyproject.toml','rb'))['project']['name'])"
```

Expected output:

```text
local-knowledge-brain
```

- [ ] **Step 6: Commit packaging foundation**

Run:

```powershell
git add LICENSE pyproject.toml .gitignore src/brain/__init__.py
git commit -m "chore: add apache licensed brain package foundation"
```

Expected: commit succeeds.

---

### Task 2: Generic Project Paths And Config

**Files:**
- Create: `src/brain/paths.py`
- Create: `src/brain/config.py`
- Create: `tests/test_brain_paths_config.py`

- [ ] **Step 1: Write failing tests for generic paths and config**

Create `tests/test_brain_paths_config.py`:

```python
import tempfile
import unittest
from pathlib import Path

from brain.config import BrainConfig, load_config, save_config
from brain.paths import BrainPaths


class BrainPathsConfigTests(unittest.TestCase):
    def test_default_paths_are_generic(self) -> None:
        paths = BrainPaths(Path("C:/project"))

        self.assertEqual(paths.project_root, Path("C:/project"))
        self.assertEqual(paths.knowledge, Path("C:/project") / "knowledge")
        self.assertEqual(paths.raw, Path("C:/project") / "knowledge" / "raw")
        self.assertEqual(paths.normalized, Path("C:/project") / "knowledge" / "normalized")
        self.assertEqual(paths.notes, Path("C:/project") / "knowledge" / "notes")
        self.assertEqual(paths.graph, Path("C:/project") / "knowledge" / "graph")
        self.assertEqual(paths.index, Path("C:/project") / "knowledge" / "index")

    def test_ensure_directories_creates_beginner_layout(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            paths = BrainPaths(Path(tmp))

            created = paths.ensure_directories()

            self.assertTrue(created)
            for directory in paths.required_directories():
                self.assertTrue(directory.is_dir(), directory)

    def test_default_config_is_beginner_friendly(self) -> None:
        config = BrainConfig.default()

        self.assertEqual("obsidian", config.storage_provider)
        self.assertEqual("docling", config.pdf_converter)
        self.assertEqual("ollama", config.ocr_provider)
        self.assertEqual("deterministic-json", config.graph_provider)
        self.assertEqual("builtin-bm25", config.search_provider)

    def test_config_round_trip(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "brain.json"
            config = BrainConfig.default()

            save_config(path, config)
            loaded = load_config(path)

            self.assertEqual(config, loaded)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run tests and confirm failure**

Run:

```powershell
python -m unittest tests.test_brain_paths_config -v
```

Expected: FAIL because `brain.paths` and `brain.config` do not exist.

- [ ] **Step 3: Implement generic paths**

Create `src/brain/paths.py`:

```python
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class BrainPaths:
    project_root: Path

    @property
    def config_path(self) -> Path:
        return self.project_root / "brain.json"

    @property
    def knowledge(self) -> Path:
        return self.project_root / "knowledge"

    @property
    def pending(self) -> Path:
        return self.knowledge / "pending"

    @property
    def raw(self) -> Path:
        return self.knowledge / "raw"

    @property
    def normalized(self) -> Path:
        return self.knowledge / "normalized"

    @property
    def notes(self) -> Path:
        return self.knowledge / "notes"

    @property
    def graph(self) -> Path:
        return self.knowledge / "graph"

    @property
    def index(self) -> Path:
        return self.knowledge / "index"

    @property
    def logs(self) -> Path:
        return self.knowledge / "logs"

    @property
    def review(self) -> Path:
        return self.knowledge / "review"

    @property
    def failed(self) -> Path:
        return self.knowledge / "failed"

    @property
    def skills(self) -> Path:
        return self.knowledge / "skills"

    def required_directories(self) -> list[Path]:
        return [
            self.pending,
            self.raw,
            self.normalized,
            self.notes,
            self.graph,
            self.index,
            self.logs / "runs",
            self.logs / "decisions",
            self.logs / "errors",
            self.logs / "retrieval",
            self.review / "needs-human",
            self.review / "low-confidence-normalization",
            self.review / "missing-concepts",
            self.failed / "technical-failures",
            self.skills,
        ]

    def ensure_directories(self) -> list[Path]:
        created: list[Path] = []
        for directory in self.required_directories():
            if not directory.exists():
                directory.mkdir(parents=True, exist_ok=True)
                created.append(directory)
            gitkeep = directory / ".gitkeep"
            if not gitkeep.exists():
                gitkeep.write_text("", encoding="utf-8")
        return created
```

- [ ] **Step 4: Implement config model**

Create `src/brain/config.py`:

```python
from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass(frozen=True)
class BrainConfig:
    storage_provider: str
    pdf_converter: str
    ocr_provider: str
    ocr_model: str
    llm_provider: str
    graph_provider: str
    search_provider: str

    @classmethod
    def default(cls) -> "BrainConfig":
        return cls(
            storage_provider="obsidian",
            pdf_converter="docling",
            ocr_provider="ollama",
            ocr_model="glm-ocr",
            llm_provider="claude-cli",
            graph_provider="deterministic-json",
            search_provider="builtin-bm25",
        )


def save_config(path: Path, config: BrainConfig) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(asdict(config), indent=2), encoding="utf-8")


def load_config(path: Path) -> BrainConfig:
    data = json.loads(path.read_text(encoding="utf-8"))
    return BrainConfig(**data)
```

- [ ] **Step 5: Run path/config tests**

Run:

```powershell
$env:PYTHONPATH="src"
python -m unittest tests.test_brain_paths_config -v
```

Expected: PASS.

- [ ] **Step 6: Commit paths and config**

Run:

```powershell
git add src/brain/paths.py src/brain/config.py tests/test_brain_paths_config.py
git commit -m "feat: add generic brain paths and config"
```

Expected: commit succeeds.

---

### Task 3: Beginner CLI Init, Status, Doctor

**Files:**
- Create: `src/brain/cli.py`
- Create: `tests/test_brain_cli.py`

- [ ] **Step 1: Write failing CLI tests**

Create `tests/test_brain_cli.py`:

```python
import tempfile
import unittest
from pathlib import Path

from brain.cli import main


class BrainCliTests(unittest.TestCase):
    def test_init_creates_project_layout_and_config(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            code = main(["init", "--root", tmp])

            self.assertEqual(0, code)
            self.assertTrue((Path(tmp) / "brain.json").is_file())
            self.assertTrue((Path(tmp) / "knowledge" / "raw").is_dir())
            self.assertTrue((Path(tmp) / "knowledge" / "notes").is_dir())

    def test_status_returns_zero_after_init(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(0, main(["init", "--root", tmp]))

            code = main(["status", "--root", tmp])

            self.assertEqual(0, code)

    def test_doctor_returns_zero_with_config_present(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(0, main(["init", "--root", tmp]))

            code = main(["doctor", "--root", tmp])

            self.assertEqual(0, code)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run tests and confirm failure**

Run:

```powershell
$env:PYTHONPATH="src"
python -m unittest tests.test_brain_cli -v
```

Expected: FAIL because `brain.cli` does not exist.

- [ ] **Step 3: Implement CLI**

Create `src/brain/cli.py`:

```python
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from brain.config import BrainConfig, load_config, save_config
from brain.paths import BrainPaths


def _cmd_init(root: Path) -> int:
    paths = BrainPaths(root)
    paths.ensure_directories()
    if not paths.config_path.exists():
        save_config(paths.config_path, BrainConfig.default())
    print(f"initialized brain project at {root}")
    return 0


def _cmd_status(root: Path) -> int:
    paths = BrainPaths(root)
    missing = [p for p in paths.required_directories() if not p.exists()]
    config_exists = paths.config_path.exists()
    if missing or not config_exists:
        if not config_exists:
            print(f"missing config: {paths.config_path}", file=sys.stderr)
        for path in missing:
            print(f"missing directory: {path}", file=sys.stderr)
        return 1
    print("brain project status ok")
    return 0


def _cmd_doctor(root: Path) -> int:
    paths = BrainPaths(root)
    if not paths.config_path.exists():
        print("brain project is not initialized; run `brain init`", file=sys.stderr)
        return 1
    config = load_config(paths.config_path)
    print(f"storage: {config.storage_provider}")
    print(f"pdf converter: {config.pdf_converter}")
    print(f"ocr: {config.ocr_provider}/{config.ocr_model}")
    print(f"llm: {config.llm_provider}")
    print(f"graph: {config.graph_provider}")
    print(f"search: {config.search_provider}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="brain", description="Local-first knowledge compiler.")
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("init", "status", "doctor"):
        cmd = sub.add_parser(name)
        cmd.add_argument("--root", default=".", help="Project root. Defaults to current directory.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = Path(args.root).resolve()
    if args.command == "init":
        return _cmd_init(root)
    if args.command == "status":
        return _cmd_status(root)
    if args.command == "doctor":
        return _cmd_doctor(root)
    raise ValueError(f"unknown command {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Run CLI tests**

Run:

```powershell
$env:PYTHONPATH="src"
python -m unittest tests.test_brain_cli -v
```

Expected: PASS.

- [ ] **Step 5: Smoke-test CLI manually**

Run:

```powershell
$tmp = New-Item -ItemType Directory -Force "$env:TEMP\brain-cli-smoke"
$env:PYTHONPATH="src"
python -m brain.cli init --root $tmp.FullName
python -m brain.cli status --root $tmp.FullName
python -m brain.cli doctor --root $tmp.FullName
```

Expected: all commands exit `0`; output includes `brain project status ok`.

- [ ] **Step 6: Commit CLI**

Run:

```powershell
git add src/brain/cli.py tests/test_brain_cli.py
git commit -m "feat: add beginner brain cli foundation"
```

Expected: commit succeeds.

---

### Task 4: Canonical Note Models

**Files:**
- Create: `src/brain/models.py`
- Create: `tests/test_brain_models.py`

- [ ] **Step 1: Write failing model tests**

Create `tests/test_brain_models.py`:

```python
import unittest

from brain.models import CanonicalNote, ProposedLink, Relation, SourceRef


class BrainModelsTests(unittest.TestCase):
    def test_canonical_note_requires_source_for_supported_claims(self) -> None:
        note = CanonicalNote(
            note_id="rag",
            title="Retrieval-Augmented Generation",
            aliases=["RAG"],
            folder="Retrieval",
            tags=["retrieval"],
            summary="Human summary.",
            retrieval_text="rag retrieval augmented generation external knowledge",
            body_sections={"core_idea": "RAG retrieves context before generation."},
            proposed_links=[],
            relations=[],
            sources=[],
            confidence=0.9,
        )

        self.assertEqual(["note has no sources"], note.validation_errors())

    def test_canonical_note_validates_confidence_range(self) -> None:
        note = CanonicalNote.minimal("RAG", confidence=1.5)

        self.assertIn("confidence must be between 0 and 1", note.validation_errors())

    def test_canonical_note_serializes_to_dict(self) -> None:
        source = SourceRef(
            raw_path="knowledge/raw/pdf/book.pdf",
            normalized_path="knowledge/normalized/pdf/book/sections/001.md",
            locator="pages 1-2",
            source_hash="sha256:abc",
            supported_claims=["RAG retrieves context."],
        )
        note = CanonicalNote.minimal("RAG", sources=[source])

        data = note.to_dict()

        self.assertEqual("RAG", data["title"])
        self.assertEqual("knowledge/raw/pdf/book.pdf", data["sources"][0]["raw_path"])


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run tests and confirm failure**

Run:

```powershell
$env:PYTHONPATH="src"
python -m unittest tests.test_brain_models -v
```

Expected: FAIL because `brain.models` does not exist.

- [ ] **Step 3: Implement canonical models**

Create `src/brain/models.py`:

```python
from __future__ import annotations

from dataclasses import asdict, dataclass, field


@dataclass(frozen=True)
class SourceRef:
    raw_path: str
    normalized_path: str
    locator: str
    source_hash: str
    supported_claims: list[str]


@dataclass(frozen=True)
class ProposedLink:
    anchor: str
    target: str
    reason: str


@dataclass(frozen=True)
class Relation:
    source: str
    relation: str
    target: str
    confidence: float


@dataclass(frozen=True)
class CanonicalNote:
    note_id: str
    title: str
    aliases: list[str]
    folder: str
    tags: list[str]
    summary: str
    retrieval_text: str
    body_sections: dict[str, str]
    proposed_links: list[ProposedLink]
    relations: list[Relation]
    sources: list[SourceRef]
    confidence: float

    @classmethod
    def minimal(
        cls,
        title: str,
        *,
        confidence: float = 0.8,
        sources: list[SourceRef] | None = None,
    ) -> "CanonicalNote":
        note_id = title.lower().replace(" ", "-")
        return cls(
            note_id=note_id,
            title=title,
            aliases=[],
            folder="",
            tags=[],
            summary=f"{title}.",
            retrieval_text=title,
            body_sections={"summary": f"{title}."},
            proposed_links=[],
            relations=[],
            sources=sources or [],
            confidence=confidence,
        )

    def validation_errors(self) -> list[str]:
        errors: list[str] = []
        if not self.title.strip():
            errors.append("title is required")
        if not self.retrieval_text.strip():
            errors.append("retrieval_text is required")
        if not self.sources:
            errors.append("note has no sources")
        if self.confidence < 0 or self.confidence > 1:
            errors.append("confidence must be between 0 and 1")
        return errors

    def to_dict(self) -> dict:
        return asdict(self)
```

- [ ] **Step 4: Run model tests**

Run:

```powershell
$env:PYTHONPATH="src"
python -m unittest tests.test_brain_models -v
```

Expected: PASS.

- [ ] **Step 5: Commit models**

Run:

```powershell
git add src/brain/models.py tests/test_brain_models.py
git commit -m "feat: add canonical note models"
```

Expected: commit succeeds.

---

### Task 5: Obsidian Renderer And Same-Batch Link Resolution

**Files:**
- Create: `src/brain/linking.py`
- Create: `src/brain/storage/__init__.py`
- Create: `src/brain/storage/obsidian.py`
- Create: `tests/test_brain_obsidian_renderer.py`

- [ ] **Step 1: Write failing renderer tests**

Create `tests/test_brain_obsidian_renderer.py`:

```python
import unittest

from brain.linking import NoteRegistry, resolve_links
from brain.models import CanonicalNote, ProposedLink, SourceRef
from brain.storage.obsidian import render_obsidian_note


def source_ref() -> SourceRef:
    return SourceRef(
        raw_path="knowledge/raw/pdf/book.pdf",
        normalized_path="knowledge/normalized/pdf/book/sections/001.md",
        locator="pages 1-2",
        source_hash="sha256:abc",
        supported_claims=["RAG retrieves context."],
    )


class ObsidianRendererTests(unittest.TestCase):
    def test_same_batch_alias_link_resolves(self) -> None:
        rag = CanonicalNote.minimal("Retrieval-Augmented Generation", sources=[source_ref()])
        dependent = CanonicalNote(
            note_id="agent-memory",
            title="Agent Memory",
            aliases=[],
            folder="Agents",
            tags=["agents"],
            summary="Agent memory stores useful context.",
            retrieval_text="agent memory rag retrieval",
            body_sections={"core_idea": "Agent memory can use RAG."},
            proposed_links=[ProposedLink(anchor="RAG", target="RAG", reason="RAG is a memory pattern.")],
            relations=[],
            sources=[source_ref()],
            confidence=0.9,
        )
        registry = NoteRegistry.from_notes([rag, dependent], extra_aliases={"RAG": rag.title})

        resolved = resolve_links(dependent, registry)

        self.assertEqual("[[Retrieval-Augmented Generation|RAG]]", resolved["RAG"])

    def test_renderer_includes_frontmatter_sources_and_body_link(self) -> None:
        note = CanonicalNote(
            note_id="agent-memory",
            title="Agent Memory",
            aliases=["Memory for Agents"],
            folder="Agents",
            tags=["agents"],
            summary="Agent memory stores useful context.",
            retrieval_text="agent memory rag retrieval",
            body_sections={"core_idea": "Agent memory can use RAG."},
            proposed_links=[ProposedLink(anchor="RAG", target="Retrieval-Augmented Generation", reason="RAG is relevant.")],
            relations=[],
            sources=[source_ref()],
            confidence=0.9,
        )
        registry = NoteRegistry.from_notes([note, CanonicalNote.minimal("Retrieval-Augmented Generation", sources=[source_ref()])])

        markdown = render_obsidian_note(note, registry)

        self.assertIn("aliases:", markdown)
        self.assertIn("Memory for Agents", markdown)
        self.assertIn("sources:", markdown)
        self.assertIn("## Core Idea", markdown)
        self.assertIn("[[Retrieval-Augmented Generation|RAG]]", markdown)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run tests and confirm failure**

Run:

```powershell
$env:PYTHONPATH="src"
python -m unittest tests.test_brain_obsidian_renderer -v
```

Expected: FAIL because `brain.linking` and `brain.storage.obsidian` do not exist.

- [ ] **Step 3: Implement link registry**

Create `src/brain/linking.py`:

```python
from __future__ import annotations

from dataclasses import dataclass

from brain.models import CanonicalNote


@dataclass(frozen=True)
class NoteRegistry:
    title_by_key: dict[str, str]

    @staticmethod
    def _key(value: str) -> str:
        return value.strip().lower()

    @classmethod
    def from_notes(
        cls,
        notes: list[CanonicalNote],
        extra_aliases: dict[str, str] | None = None,
    ) -> "NoteRegistry":
        title_by_key: dict[str, str] = {}
        for note in notes:
            title_by_key[cls._key(note.title)] = note.title
            for alias in note.aliases:
                title_by_key[cls._key(alias)] = note.title
        for alias, title in (extra_aliases or {}).items():
            title_by_key[cls._key(alias)] = title
        return cls(title_by_key)

    def resolve(self, target: str) -> str | None:
        return self.title_by_key.get(self._key(target))


def resolve_links(note: CanonicalNote, registry: NoteRegistry) -> dict[str, str]:
    resolved: dict[str, str] = {}
    for proposed in note.proposed_links:
        title = registry.resolve(proposed.target)
        if title is None:
            continue
        resolved[proposed.anchor] = f"[[{title}|{proposed.anchor}]]"
    return resolved
```

- [ ] **Step 4: Implement Obsidian renderer**

Create `src/brain/storage/__init__.py`:

```python
"""Storage adapters for rendered knowledge notes."""
```

Create `src/brain/storage/obsidian.py`:

```python
from __future__ import annotations

import re

from brain.linking import NoteRegistry, resolve_links
from brain.models import CanonicalNote


def _yaml_list(values: list[str], indent: int = 2) -> str:
    prefix = " " * indent
    if not values:
        return f"{prefix}[]"
    return "\n".join(f"{prefix}- {value}" for value in values)


def _heading(name: str) -> str:
    words = re.sub(r"[_-]+", " ", name).split()
    return " ".join(word.capitalize() for word in words)


def _apply_links(text: str, links: dict[str, str]) -> str:
    linked = text
    for anchor, wikilink in sorted(links.items(), key=lambda item: len(item[0]), reverse=True):
        linked = re.sub(rf"\b{re.escape(anchor)}\b", wikilink, linked, count=1)
    return linked


def render_obsidian_note(note: CanonicalNote, registry: NoteRegistry) -> str:
    links = resolve_links(note, registry)
    lines = [
        "---",
        f"title: {note.title}",
        "aliases:",
        _yaml_list(note.aliases),
        "tags:",
        _yaml_list(note.tags),
        f"confidence: {note.confidence}",
        "sources:",
    ]
    for source in note.sources:
        lines.extend(
            [
                f"  - raw_path: {source.raw_path}",
                f"    normalized_path: {source.normalized_path}",
                f"    locator: {source.locator}",
                f"    source_hash: {source.source_hash}",
                "    supported_claims:",
                _yaml_list(source.supported_claims, indent=6),
            ]
        )
    lines.extend(["---", "", f"# {note.title}", "", "## Summary", "", note.summary, ""])
    for section_name, section_text in note.body_sections.items():
        lines.extend([f"## {_heading(section_name)}", "", _apply_links(section_text, links), ""])
    if links:
        lines.extend(["## Related", ""])
        for wikilink in sorted(set(links.values())):
            lines.append(f"- {wikilink}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"
```

- [ ] **Step 5: Run renderer tests**

Run:

```powershell
$env:PYTHONPATH="src"
python -m unittest tests.test_brain_obsidian_renderer -v
```

Expected: PASS.

- [ ] **Step 6: Commit renderer and link resolver**

Run:

```powershell
git add src/brain/linking.py src/brain/storage/__init__.py src/brain/storage/obsidian.py tests/test_brain_obsidian_renderer.py
git commit -m "feat: add obsidian renderer and batch link resolution"
```

Expected: commit succeeds.

---

### Task 6: Deterministic Graph Builder

**Files:**
- Create: `src/brain/graph.py`
- Create: `tests/test_brain_graph.py`

- [ ] **Step 1: Write failing graph tests**

Create `tests/test_brain_graph.py`:

```python
import tempfile
import unittest
from pathlib import Path

from brain.graph import build_graph, load_graph, query_graph, save_graph
from brain.models import CanonicalNote, Relation, SourceRef


def source_ref() -> SourceRef:
    return SourceRef(
        raw_path="knowledge/raw/pdf/book.pdf",
        normalized_path="knowledge/normalized/pdf/book/sections/001.md",
        locator="pages 1-2",
        source_hash="sha256:abc",
        supported_claims=["RAG retrieves context."],
    )


class BrainGraphTests(unittest.TestCase):
    def test_build_graph_contains_note_alias_tag_and_source_nodes(self) -> None:
        note = CanonicalNote(
            note_id="rag",
            title="Retrieval-Augmented Generation",
            aliases=["RAG"],
            folder="Retrieval",
            tags=["retrieval"],
            summary="Human summary.",
            retrieval_text="rag external knowledge retrieval",
            body_sections={"core_idea": "RAG retrieves context."},
            proposed_links=[],
            relations=[],
            sources=[source_ref()],
            confidence=0.9,
        )

        graph = build_graph([note])

        self.assertIn("note:rag", graph["nodes"])
        self.assertIn("alias:rag", graph["nodes"])
        self.assertIn("tag:retrieval", graph["nodes"])
        self.assertIn("source:knowledge/normalized/pdf/book/sections/001.md", graph["nodes"])
        self.assertTrue(any(edge["type"] == "has_alias" for edge in graph["edges"]))

    def test_query_graph_routes_by_retrieval_text_and_aliases(self) -> None:
        rag = CanonicalNote.minimal("Retrieval-Augmented Generation", sources=[source_ref()])
        memory = CanonicalNote(
            note_id="agent-memory",
            title="Agent Memory",
            aliases=[],
            folder="Agents",
            tags=["agents"],
            summary="Memory for agents.",
            retrieval_text="agent memory long term context",
            body_sections={"core_idea": "Memory stores context."},
            proposed_links=[],
            relations=[Relation("Agent Memory", "uses", "Retrieval-Augmented Generation", 0.8)],
            sources=[source_ref()],
            confidence=0.8,
        )
        graph = build_graph([rag, memory])

        results = query_graph(graph, "How do agents remember context?", limit=2)

        self.assertEqual("note:agent-memory", results[0]["id"])

    def test_graph_round_trips_to_json(self) -> None:
        note = CanonicalNote.minimal("Retrieval-Augmented Generation", sources=[source_ref()])
        graph = build_graph([note])

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "graph.json"
            save_graph(path, graph)
            loaded = load_graph(path)

        self.assertEqual(graph, loaded)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run tests and confirm failure**

Run:

```powershell
$env:PYTHONPATH="src"
python -m unittest tests.test_brain_graph -v
```

Expected: FAIL because `brain.graph` does not exist.

- [ ] **Step 3: Implement deterministic graph**

Create `src/brain/graph.py`:

```python
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

from brain.models import CanonicalNote


def _node_id(kind: str, value: str) -> str:
    slug = re.sub(r"[^a-z0-9._/-]+", "-", value.lower()).strip("-")
    return f"{kind}:{slug}"


def build_graph(notes: list[CanonicalNote]) -> dict:
    nodes: dict[str, dict] = {}
    edges: list[dict] = []

    def add_node(node_id: str, **attrs: object) -> None:
        nodes[node_id] = {"id": node_id, **attrs}

    def add_edge(source: str, target: str, edge_type: str, **attrs: object) -> None:
        edges.append({"source": source, "target": target, "type": edge_type, **attrs})

    for note in notes:
        note_id = _node_id("note", note.note_id)
        add_node(
            note_id,
            kind="note",
            label=note.title,
            aliases=note.aliases,
            tags=note.tags,
            summary=note.summary,
            retrieval_text=note.retrieval_text,
            confidence=note.confidence,
        )
        for alias in note.aliases:
            alias_id = _node_id("alias", alias)
            add_node(alias_id, kind="alias", label=alias)
            add_edge(note_id, alias_id, "has_alias")
        for tag in note.tags:
            tag_id = _node_id("tag", tag)
            add_node(tag_id, kind="tag", label=tag)
            add_edge(note_id, tag_id, "tagged")
        for source in note.sources:
            source_id = _node_id("source", source.normalized_path)
            add_node(source_id, kind="source", label=source.normalized_path, raw_path=source.raw_path)
            add_edge(source_id, note_id, "supports", locator=source.locator)
        for relation in note.relations:
            target_id = _node_id("concept", relation.target)
            add_node(target_id, kind="concept", label=relation.target)
            add_edge(note_id, target_id, relation.relation, confidence=relation.confidence)

    return {"nodes": nodes, "edges": edges}


def _terms(text: str) -> Counter[str]:
    return Counter(re.findall(r"[a-z0-9][a-z0-9-]{2,}", text.lower()))


def query_graph(graph: dict, question: str, limit: int = 5) -> list[dict]:
    q_terms = _terms(question)
    scored: list[tuple[int, dict]] = []
    for node in graph["nodes"].values():
        if node.get("kind") != "note":
            continue
        haystack = " ".join(
            [
                str(node.get("label", "")),
                " ".join(node.get("aliases", [])),
                " ".join(node.get("tags", [])),
                str(node.get("summary", "")),
                str(node.get("retrieval_text", "")),
            ]
        )
        score = sum(_terms(haystack).get(term, 0) * count for term, count in q_terms.items())
        if score > 0:
            scored.append((score, node))
    return [node for _score, node in sorted(scored, key=lambda item: item[0], reverse=True)[:limit]]


def save_graph(path: Path, graph: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(graph, indent=2, sort_keys=True), encoding="utf-8")


def load_graph(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))
```

- [ ] **Step 4: Run graph tests**

Run:

```powershell
$env:PYTHONPATH="src"
python -m unittest tests.test_brain_graph -v
```

Expected: PASS.

- [ ] **Step 5: Commit graph builder**

Run:

```powershell
git add src/brain/graph.py tests/test_brain_graph.py
git commit -m "feat: add deterministic graph builder"
```

Expected: commit succeeds.

---

### Task 7: Built-In BM25 Fallback Search

**Files:**
- Create: `src/brain/search.py`
- Create: `tests/test_brain_search.py`

- [ ] **Step 1: Write failing BM25 tests**

Create `tests/test_brain_search.py`:

```python
import tempfile
import unittest
from pathlib import Path

from brain.search import BM25Index


class BrainSearchTests(unittest.TestCase):
    def test_bm25_returns_best_matching_document(self) -> None:
        index = BM25Index()
        index.add("rag", "retrieval augmented generation external knowledge documents")
        index.add("finetuning", "training model weights supervised examples")

        results = index.search("external documents retrieval", limit=1)

        self.assertEqual("rag", results[0]["id"])
        self.assertGreater(results[0]["score"], 0)

    def test_empty_index_returns_no_results(self) -> None:
        self.assertEqual([], BM25Index().search("anything"))

    def test_bm25_round_trips_to_json(self) -> None:
        index = BM25Index()
        index.add("rag", "retrieval augmented generation external knowledge")

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bm25.json"
            index.save(path)
            loaded = BM25Index.load(path)

        self.assertEqual("rag", loaded.search("external knowledge", limit=1)[0]["id"])


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run tests and confirm failure**

Run:

```powershell
$env:PYTHONPATH="src"
python -m unittest tests.test_brain_search -v
```

Expected: FAIL because `brain.search` does not exist.

- [ ] **Step 3: Implement BM25 fallback**

Create `src/brain/search.py`:

```python
from __future__ import annotations

import json
import math
import re
from collections import Counter
from pathlib import Path


def _terms(text: str) -> list[str]:
    return re.findall(r"[a-z0-9][a-z0-9-]{2,}", text.lower())


class BM25Index:
    def __init__(self, k1: float = 1.5, b: float = 0.75) -> None:
        self.k1 = k1
        self.b = b
        self._docs: dict[str, Counter[str]] = {}
        self._lengths: dict[str, int] = {}
        self._df: Counter[str] = Counter()

    def add(self, doc_id: str, text: str) -> None:
        counts = Counter(_terms(text))
        self._docs[doc_id] = counts
        self._lengths[doc_id] = sum(counts.values())
        for term in counts:
            self._df[term] += 1

    def search(self, query: str, limit: int = 5) -> list[dict]:
        if not self._docs:
            return []
        q_terms = _terms(query)
        avgdl = sum(self._lengths.values()) / len(self._lengths)
        results: list[dict] = []
        total_docs = len(self._docs)
        for doc_id, counts in self._docs.items():
            score = 0.0
            doc_len = self._lengths[doc_id]
            for term in q_terms:
                tf = counts.get(term, 0)
                if tf == 0:
                    continue
                df = self._df.get(term, 0)
                idf = math.log(1 + (total_docs - df + 0.5) / (df + 0.5))
                denom = tf + self.k1 * (1 - self.b + self.b * doc_len / avgdl)
                score += idf * (tf * (self.k1 + 1)) / denom
            if score > 0:
                results.append({"id": doc_id, "score": score})
        return sorted(results, key=lambda item: item["score"], reverse=True)[:limit]

    def to_dict(self) -> dict:
        return {
            "k1": self.k1,
            "b": self.b,
            "docs": {doc_id: dict(counts) for doc_id, counts in self._docs.items()},
            "lengths": self._lengths,
            "df": dict(self._df),
        }

    @classmethod
    def from_dict(cls, data: dict) -> "BM25Index":
        index = cls(k1=float(data["k1"]), b=float(data["b"]))
        index._docs = {doc_id: Counter(counts) for doc_id, counts in data["docs"].items()}
        index._lengths = {doc_id: int(length) for doc_id, length in data["lengths"].items()}
        index._df = Counter(data["df"])
        return index

    def save(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(self.to_dict(), indent=2, sort_keys=True), encoding="utf-8")

    @classmethod
    def load(cls, path: Path) -> "BM25Index":
        return cls.from_dict(json.loads(path.read_text(encoding="utf-8")))
```

- [ ] **Step 4: Run BM25 tests**

Run:

```powershell
$env:PYTHONPATH="src"
python -m unittest tests.test_brain_search -v
```

Expected: PASS.

- [ ] **Step 5: Commit BM25 fallback**

Run:

```powershell
git add src/brain/search.py tests/test_brain_search.py
git commit -m "feat: add builtin bm25 fallback search"
```

Expected: commit succeeds.

---

### Task 8: Graph-First Ask Context Builder

**Files:**
- Create: `src/brain/ask.py`
- Modify: `src/brain/cli.py`
- Create: `tests/test_brain_ask.py`

- [ ] **Step 1: Write failing ask tests**

Create `tests/test_brain_ask.py`:

```python
import tempfile
import unittest
from pathlib import Path

from brain.ask import build_context_bundle
from brain.cli import main
from brain.graph import build_graph, save_graph
from brain.models import CanonicalNote, SourceRef
from brain.paths import BrainPaths
from brain.search import BM25Index


def source_ref() -> SourceRef:
    return SourceRef(
        raw_path="knowledge/raw/pdf/book.pdf",
        normalized_path="knowledge/normalized/pdf/book/sections/001.md",
        locator="pages 1-2",
        source_hash="sha256:abc",
        supported_claims=["RAG retrieves context."],
    )


class BrainAskTests(unittest.TestCase):
    def test_context_uses_graph_before_bm25(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            paths = BrainPaths(Path(tmp))
            paths.ensure_directories()
            note = CanonicalNote(
                note_id="rag",
                title="Retrieval-Augmented Generation",
                aliases=["RAG"],
                folder="Retrieval",
                tags=["retrieval"],
                summary="RAG connects models to external knowledge.",
                retrieval_text="external documents retrieval augmented generation",
                body_sections={"core_idea": "RAG retrieves context."},
                proposed_links=[],
                relations=[],
                sources=[source_ref()],
                confidence=0.9,
            )
            note_path = paths.notes / "Retrieval-Augmented-Generation.md"
            note_path.write_text("# Retrieval-Augmented Generation\n\nRAG retrieves context.", encoding="utf-8")
            graph = build_graph([note])
            search = BM25Index()
            search.add("wrong", "external documents")

            bundle = build_context_bundle(paths, graph, search, "How do I use external documents?", limit=1)

            self.assertEqual("graph", bundle.items[0]["route"])
            self.assertIn("Retrieval-Augmented-Generation.md", bundle.items[0]["path"])
            self.assertIn("RAG retrieves context", bundle.items[0]["content"])

    def test_ask_context_cli_reads_real_note_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            paths = BrainPaths(Path(tmp))
            paths.ensure_directories()
            note = CanonicalNote(
                note_id="rag",
                title="Retrieval-Augmented Generation",
                aliases=["RAG"],
                folder="Retrieval",
                tags=["retrieval"],
                summary="RAG connects models to external knowledge.",
                retrieval_text="external documents retrieval augmented generation",
                body_sections={"core_idea": "RAG retrieves context."},
                proposed_links=[],
                relations=[],
                sources=[source_ref()],
                confidence=0.9,
            )
            (paths.notes / "Retrieval-Augmented-Generation.md").write_text(
                "# Retrieval-Augmented Generation\n\nRAG retrieves context.",
                encoding="utf-8",
            )
            save_graph(paths.graph / "graph.json", build_graph([note]))
            search = BM25Index()
            search.save(paths.index / "bm25.json")

            code = main(["ask", "context", "How do I use external documents?", "--root", tmp])

            self.assertEqual(0, code)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run tests and confirm failure**

Run:

```powershell
$env:PYTHONPATH="src"
python -m unittest tests.test_brain_ask -v
```

Expected: FAIL because `brain.ask` does not exist.

- [ ] **Step 3: Implement ask context builder**

Create `src/brain/ask.py`:

```python
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from brain.graph import query_graph
from brain.paths import BrainPaths
from brain.search import BM25Index


@dataclass(frozen=True)
class ContextBundle:
    question: str
    items: list[dict]

    def render(self) -> str:
        lines = [f"Question: {self.question}", ""]
        for idx, item in enumerate(self.items, start=1):
            lines.extend([f"[{idx}] {item['path']} ({item['route']})", item["content"], ""])
        return "\n".join(lines).strip() + "\n"


def _note_path(paths: BrainPaths, label: str) -> Path:
    filename = label.replace(" ", "-") + ".md"
    return paths.notes / filename


def build_context_bundle(
    paths: BrainPaths,
    graph: dict,
    search_index: BM25Index,
    question: str,
    limit: int = 5,
) -> ContextBundle:
    items: list[dict] = []
    for node in query_graph(graph, question, limit=limit):
        path = _note_path(paths, str(node["label"]))
        if not path.is_file():
            continue
        items.append({"route": "graph", "path": path.as_posix(), "content": path.read_text(encoding="utf-8")})
    if items:
        return ContextBundle(question=question, items=items)

    for result in search_index.search(question, limit=limit):
        path = paths.notes / f"{result['id']}.md"
        if not path.is_file():
            continue
        items.append({"route": "bm25", "path": path.as_posix(), "content": path.read_text(encoding="utf-8")})
    return ContextBundle(question=question, items=items)
```

- [ ] **Step 4: Run ask tests**

Run:

```powershell
$env:PYTHONPATH="src"
python -m unittest tests.test_brain_ask -v
```

Expected: PASS.

- [ ] **Step 5: Add working CLI commands for graph/search/ask context**

Modify `src/brain/cli.py`:

- Import `json`, `build_context_bundle`, `load_graph`, `query_graph`, and `BM25Index`.
- Add subcommands `ask context`, `graph query`, and `search`.
- `graph query` reads `knowledge/graph/graph.json` and prints JSON candidates.
- `search` reads `knowledge/index/bm25.json` and prints JSON candidates.
- `ask context` uses the graph first, reads real Markdown note files, and falls back to BM25 only when graph context is empty.
- Missing graph/index files return `1` with an explicit error.
- Keep `init`, `status`, and `doctor` behavior unchanged.

Add these imports near the top:

```python
import json

from brain.ask import build_context_bundle
from brain.graph import load_graph, query_graph
from brain.search import BM25Index
```

Add this parser extension inside `build_parser()` after the existing `init/status/doctor` setup:

```python
    ask = sub.add_parser("ask")
    ask_sub = ask.add_subparsers(dest="ask_command", required=True)
    ask_context = ask_sub.add_parser("context")
    ask_context.add_argument("question")
    ask_context.add_argument("--root", default=".")

    graph = sub.add_parser("graph")
    graph_sub = graph.add_subparsers(dest="graph_command", required=True)
    graph_query = graph_sub.add_parser("query")
    graph_query.add_argument("question")
    graph_query.add_argument("--root", default=".")

    search = sub.add_parser("search")
    search.add_argument("query")
    search.add_argument("--root", default=".")
```

Add these helpers before `build_parser()`:

```python
def _load_required_graph(paths: BrainPaths) -> dict | None:
    graph_path = paths.graph / "graph.json"
    if not graph_path.is_file():
        print(f"missing graph: {graph_path}", file=sys.stderr)
        return None
    return load_graph(graph_path)


def _load_optional_search(paths: BrainPaths) -> BM25Index:
    index_path = paths.index / "bm25.json"
    if not index_path.is_file():
        return BM25Index()
    return BM25Index.load(index_path)


def _cmd_graph_query(root: Path, question: str) -> int:
    paths = BrainPaths(root)
    graph = _load_required_graph(paths)
    if graph is None:
        return 1
    print(json.dumps(query_graph(graph, question), indent=2))
    return 0


def _cmd_search(root: Path, query: str) -> int:
    paths = BrainPaths(root)
    index_path = paths.index / "bm25.json"
    if not index_path.is_file():
        print(f"missing search index: {index_path}", file=sys.stderr)
        return 1
    print(json.dumps(BM25Index.load(index_path).search(query), indent=2))
    return 0


def _cmd_ask_context(root: Path, question: str) -> int:
    paths = BrainPaths(root)
    graph = _load_required_graph(paths)
    if graph is None:
        return 1
    bundle = build_context_bundle(paths, graph, _load_optional_search(paths), question)
    if not bundle.items:
        print("no context found", file=sys.stderr)
        return 1
    print(bundle.render())
    return 0
```

Add these branches inside `main()` before the final `raise`:

```python
    if args.command == "graph" and args.graph_command == "query":
        return _cmd_graph_query(root, args.question)
    if args.command == "search":
        return _cmd_search(root, args.query)
    if args.command == "ask" and args.ask_command == "context":
        return _cmd_ask_context(root, args.question)
```

- [ ] **Step 6: Run CLI and ask tests**

Run:

```powershell
$env:PYTHONPATH="src"
python -m unittest tests.test_brain_cli tests.test_brain_ask -v
```

Expected: PASS.

- [ ] **Step 7: Commit ask foundation**

Run:

```powershell
git add src/brain/ask.py src/brain/cli.py tests/test_brain_ask.py
git commit -m "feat: add graph-first ask context foundation"
```

Expected: commit succeeds.

---

### Task 9: Agent Skill And Tool Calling Docs

**Files:**
- Create: `skills/brain-knowledge/SKILL.md`
- Create: `docs/agent-tool-calling.md`

- [ ] **Step 1: Create the agent skill**

Create `skills/brain-knowledge/SKILL.md`:

```markdown
---
name: brain-knowledge
description: Use when answering questions against a local Brain knowledge project or when modifying rendered knowledge notes.
---

# Brain Knowledge Skill

Use this protocol when working with a Brain knowledge project.

## Core Rule

The graph is the primary index. It is not source truth.

Use the graph to decide which notes or normalized source sections to read. Then
answer from the real files with citations.

## Retrieval Order

1. Run `brain graph query "<question>"`.
2. Read selected final notes with `brain notes read <id-or-path>` or direct file reads.
3. Follow validated wikilinks when the selected notes point to necessary context.
4. If the graph is insufficient, run `brain search "<query>"`.
5. If final notes are insufficient, inspect normalized source sections.
6. Cite final notes and their precompiled source references.

## Authoring Rules

- Do not create broken wikilinks.
- Do not cite graph metadata as source truth.
- Do not copy raw source dumps into final notes.
- Preserve raw and normalized provenance.
- Use aliases, tags, and retrieval text to improve future routing.
```

- [ ] **Step 2: Create tool-calling guide**

Create `docs/agent-tool-calling.md`:

```markdown
# Agent Tool Calling Guide

Brain exposes simple CLI commands that agent frameworks can wrap as tools.

## Graph Routing

```powershell
brain graph query "<question>"
```

Purpose: identify candidate notes or source sections. The graph is an index, not
the answer source.

## Note Reading

```powershell
brain notes read <note-id-or-path>
```

Purpose: read real final note content before answering.

## Lexical Fallback

```powershell
brain search "<query>"
```

Purpose: recover candidates when graph routing is insufficient.

## Source Reading

```powershell
brain sources read <source-section-id-or-path>
```

Purpose: inspect normalized sources when final notes do not contain enough
information.

## Validation

```powershell
brain validate
```

Purpose: check links, provenance, graph/index freshness, and project structure.

## Review Queue

```powershell
brain review list
```

Purpose: inspect low-confidence conversion, missing concepts, and items needing
human judgment.
```

- [ ] **Step 3: Verify docs mention graph as index**

Run:

```powershell
rg -n "graph is the primary index|not source truth|brain graph query|brain search" skills/brain-knowledge/SKILL.md docs/agent-tool-calling.md
```

Expected: output includes all core phrases.

- [ ] **Step 4: Commit agent docs**

Run:

```powershell
git add skills/brain-knowledge/SKILL.md docs/agent-tool-calling.md
git commit -m "docs: add brain agent skill and tool guide"
```

Expected: commit succeeds.

---

### Task 10: Full Foundation Verification

**Files:**
- Modify: none unless verification reveals a defect.

- [ ] **Step 1: Run the new brain package tests**

Run:

```powershell
$env:PYTHONPATH="src"
python -m unittest tests.test_brain_paths_config tests.test_brain_cli tests.test_brain_models tests.test_brain_obsidian_renderer tests.test_brain_graph tests.test_brain_search tests.test_brain_ask -v
```

Expected: PASS.

- [ ] **Step 2: Run the full existing suite**

Run:

```powershell
$env:PYTHONPATH="src"
python -m unittest discover -s tests -v
```

Expected: PASS. Existing `tools/fde_brain` tests must keep passing.

- [ ] **Step 3: Verify beginner smoke flow**

Run:

```powershell
$tmp = Join-Path $env:TEMP "brain-foundation-smoke"
Remove-Item -LiteralPath $tmp -Recurse -Force -ErrorAction SilentlyContinue
$env:PYTHONPATH="src"
python -m brain.cli init --root $tmp
python -m brain.cli status --root $tmp
python -m brain.cli doctor --root $tmp
```

Expected:

- `init` exits `0`
- `status` exits `0`
- `doctor` exits `0`
- `$tmp/brain.json` exists
- `$tmp/knowledge/notes` exists

- [ ] **Step 4: Verify no unintended files were staged**

Run:

```powershell
git status --short
```

Expected: only files intentionally changed by the current task are dirty. Do not stage `.claude/`, `.obsidian/`, partial Graphify output, or unrelated legacy workspace files.

- [ ] **Step 5: Commit verification fixes only if needed**

If verification required code changes, commit them:

```powershell
git add <changed-code-or-test-files>
git commit -m "test: verify brain core foundation"
```

If no files changed, do not create an empty commit.

---

## Self-Review Checklist

Spec coverage:

- Generic open-source product boundary: Task 1, Task 2.
- Beginner-first UX: Task 3.
- Canonical note objects: Task 4.
- Obsidian as first storage adapter: Task 5.
- Same-batch wikilink resolution: Task 5.
- Deterministic graph-first index: Task 6 and Task 8.
- BM25 fallback: Task 7 and Task 8.
- Agent skills and tool calling: Task 9.
- Graph is index, not source truth: Task 8 and Task 9.

Known gaps intentionally deferred:

- Docling conversion.
- OCR adapters.
- LLM note extraction.
- Resume/progress infrastructure for long conversions.
- Packaging release and update command.

Placeholder scan:

- No unresolved marker tokens or open-ended deferrals are used as task steps.
- Each code-creating step includes concrete code content.
- Each verification step includes an exact command and expected result.

Type consistency:

- `BrainPaths`, `BrainConfig`, `CanonicalNote`, `SourceRef`, `ProposedLink`, and `Relation` are introduced before dependent tasks use them.
- Graph query and ask context both use note labels and deterministic note filenames consistently.
- The CLI uses the same beginner command names from the approved design.
