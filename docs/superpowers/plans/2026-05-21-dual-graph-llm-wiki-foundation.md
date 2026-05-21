# Dual Graph LLM Wiki Foundation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the local foundation for the Dual Graph LLM Wiki: workspace folders, shared agent protocol, validation scripts, local engine preflight, Graphify command wrappers, and basic tests.

**Architecture:** This plan creates a small Python utility package under `tools/fde_brain` plus Markdown protocol files consumed by Claude Code and Codex. The utilities do not perform ingestion yet; they establish safe paths, environment checks, graph command construction, and workspace validation so later plans can implement OCR, ingestion, scheduling, and query-time promotion on top.

**Tech Stack:** Python standard library, PowerShell commands, git, Claude Code CLI, Codex CLI, Ollama, Graphify CLI, Obsidian Markdown conventions.

---

## Scope Check

The approved design covers multiple subsystems: workspace scaffolding, agent protocol, ingestion, OCR, Graphify, scheduled automation, query-time promotion, logs, git safety, and maintenance.

This plan intentionally implements **Foundation V1** only:

- deterministic workspace folder creation
- shared protocol docs for Claude and Codex
- local engine preflight checks
- Graphify command wrapper helpers
- workspace validation
- tests for path handling, preflight behavior, and command generation

Out of scope for this plan:

- full OCR normalization pipeline
- scheduled Windows Task Scheduler job
- automated ingestion from `pending`
- query-time promotion implementation
- Graphify extraction execution against real corpora
- Obsidian note authoring automation

Those should be separate plans after this foundation is in place.

## File Structure

- Create: `.gitattributes`
  - Normalizes text files to avoid noisy line-ending diffs.
- Create: `.gitignore`
  - Ignores Python cache, virtual environments, temp files, and local tool noise without ignoring `AI Space`, `FDE Brain`, logs, or Graphify outputs.
- Create: `AI Space/pending/.gitkeep`
  - Keeps the pending drop zone in git while allowing it to be empty.
- Create: `AI Space/raw/.gitkeep`
  - Keeps the raw archive folder in git.
- Create: `AI Space/normalized/.gitkeep`
  - Keeps the normalized sources folder in git.
- Create: `AI Space/graph/brain/.gitkeep`
  - Keeps the Brain Graph output folder in git.
- Create: `AI Space/graph/sources/.gitkeep`
  - Keeps the Source Graph output folder in git.
- Create: `AI Space/logs/runs/.gitkeep`
  - Keeps run logs folder in git.
- Create: `AI Space/logs/decisions/.gitkeep`
  - Keeps decision logs folder in git.
- Create: `AI Space/logs/errors/.gitkeep`
  - Keeps error logs folder in git.
- Create: `AI Space/logs/promotions/.gitkeep`
  - Keeps promotion logs folder in git.
- Create: `AI Space/review/ambiguous/.gitkeep`
  - Keeps ambiguous review folder in git.
- Create: `AI Space/review/conflicts/.gitkeep`
  - Keeps conflict review folder in git.
- Create: `AI Space/review/needs-human/.gitkeep`
  - Keeps human review folder in git.
- Create: `AI Space/review/low-confidence-normalization/.gitkeep`
  - Keeps low-confidence OCR/parser review folder in git.
- Create: `AI Space/failed/technical-failures/.gitkeep`
  - Keeps failed technical items folder in git.
- Create: `AI Space/system/AGENT_PROTOCOL.md`
  - Shared retrieval, citation, promotion, and safety protocol for Claude Code and Codex.
- Create: `AI Space/system/RUNBOOK.md`
  - Manual commands and operational checks for the workspace.
- Create: `AGENTS.md`
  - Codex entrypoint pointing to the shared protocol.
- Create: `CLAUDE.md`
  - Claude Code entrypoint pointing to the shared protocol.
- Create: `tools/fde_brain/__init__.py`
  - Python package marker.
- Create: `tools/fde_brain/paths.py`
  - Centralizes workspace paths and folder creation.
- Create: `tools/fde_brain/preflight.py`
  - Checks local engines: Claude Code, Codex, Ollama, GLM-OCR model, Graphify.
- Create: `tools/fde_brain/graphify.py`
  - Builds Graphify commands for Brain Graph and Source Graph without running them by default.
- Create: `tools/fde_brain/validate_workspace.py`
  - Validates required folders, protocol files, and graph stale markers.
- Create: `tests/test_paths.py`
  - Unit tests for path constants and folder creation.
- Create: `tests/test_preflight.py`
  - Unit tests for CLI and Ollama checks using mocks.
- Create: `tests/test_graphify.py`
  - Unit tests for Graphify command construction.
- Create: `tests/test_validate_workspace.py`
  - Unit tests for workspace validation.

---

### Task 1: Repository Hygiene And Folder Scaffold

**Files:**
- Create: `.gitattributes`
- Create: `.gitignore`
- Create: `AI Space/pending/.gitkeep`
- Create: `AI Space/raw/.gitkeep`
- Create: `AI Space/normalized/.gitkeep`
- Create: `AI Space/graph/brain/.gitkeep`
- Create: `AI Space/graph/sources/.gitkeep`
- Create: `AI Space/logs/runs/.gitkeep`
- Create: `AI Space/logs/decisions/.gitkeep`
- Create: `AI Space/logs/errors/.gitkeep`
- Create: `AI Space/logs/promotions/.gitkeep`
- Create: `AI Space/review/ambiguous/.gitkeep`
- Create: `AI Space/review/conflicts/.gitkeep`
- Create: `AI Space/review/needs-human/.gitkeep`
- Create: `AI Space/review/low-confidence-normalization/.gitkeep`
- Create: `AI Space/failed/technical-failures/.gitkeep`

- [ ] **Step 1: Write repository hygiene files**

Create `.gitattributes`:

```gitattributes
* text=auto
*.md text eol=lf
*.py text eol=lf
*.json text eol=lf
*.ps1 text eol=crlf
```

Create `.gitignore`:

```gitignore
# Python
__pycache__/
*.py[cod]
.pytest_cache/
.mypy_cache/
.ruff_cache/

# Virtual environments
.venv/
venv/
env/

# Local temp files
*.tmp
*.temp
~$*
.DS_Store
Thumbs.db

# Editor folders outside Obsidian
.vscode/
.idea/

# Graphify transient internals
**/.graphify_chunk_*.json
**/.graphify_cached.json
**/.graphify_uncached.txt
**/.graphify_semantic_new.json
```

- [ ] **Step 2: Create required workspace folders**

Run:

```powershell
$folders = @(
  "AI Space/pending",
  "AI Space/raw",
  "AI Space/normalized",
  "AI Space/graph/brain",
  "AI Space/graph/sources",
  "AI Space/logs/runs",
  "AI Space/logs/decisions",
  "AI Space/logs/errors",
  "AI Space/logs/promotions",
  "AI Space/review/ambiguous",
  "AI Space/review/conflicts",
  "AI Space/review/needs-human",
  "AI Space/review/low-confidence-normalization",
  "AI Space/failed/technical-failures"
)
foreach ($folder in $folders) {
  New-Item -ItemType Directory -Force -Path $folder | Out-Null
  New-Item -ItemType File -Force -Path (Join-Path $folder ".gitkeep") | Out-Null
}
```

Expected: command exits with code `0`.

- [ ] **Step 3: Verify folders exist**

Run:

```powershell
$missing = @()
$folders = @(
  "AI Space/pending",
  "AI Space/raw",
  "AI Space/normalized",
  "AI Space/graph/brain",
  "AI Space/graph/sources",
  "AI Space/logs/runs",
  "AI Space/logs/decisions",
  "AI Space/logs/errors",
  "AI Space/logs/promotions",
  "AI Space/review/ambiguous",
  "AI Space/review/conflicts",
  "AI Space/review/needs-human",
  "AI Space/review/low-confidence-normalization",
  "AI Space/failed/technical-failures"
)
foreach ($folder in $folders) {
  if (-not (Test-Path $folder)) { $missing += $folder }
}
if ($missing.Count -gt 0) {
  Write-Error "Missing folders: $($missing -join ', ')"
  exit 1
}
Write-Output "workspace folders ok"
```

Expected output:

```text
workspace folders ok
```

- [ ] **Step 4: Commit scaffold**

Run:

```powershell
git add .gitattributes .gitignore "AI Space"
git commit -m "chore: scaffold ai space folders"
```

Expected: commit succeeds.

---

### Task 2: Python Path Utilities

**Files:**
- Create: `tools/fde_brain/__init__.py`
- Create: `tools/fde_brain/paths.py`
- Create: `tests/test_paths.py`

- [ ] **Step 1: Create package marker**

Create `tools/fde_brain/__init__.py`:

```python
"""Utilities for the local Dual Graph LLM Wiki workspace."""
```

- [ ] **Step 2: Write failing tests for path utilities**

Create `tests/test_paths.py`:

```python
import tempfile
import unittest
from pathlib import Path

from tools.fde_brain.paths import WorkspacePaths


class WorkspacePathsTests(unittest.TestCase):
    def test_paths_are_derived_from_root(self) -> None:
        root = Path("C:/workspace")
        paths = WorkspacePaths(root)

        self.assertEqual(paths.ai_space, root / "AI Space")
        self.assertEqual(paths.fde_brain, root / "FDE Brain")
        self.assertEqual(paths.pending, root / "AI Space" / "pending")
        self.assertEqual(paths.raw, root / "AI Space" / "raw")
        self.assertEqual(paths.normalized, root / "AI Space" / "normalized")
        self.assertEqual(paths.brain_graph, root / "AI Space" / "graph" / "brain")
        self.assertEqual(paths.source_graph, root / "AI Space" / "graph" / "sources")
        self.assertEqual(paths.agent_protocol, root / "AI Space" / "system" / "AGENT_PROTOCOL.md")

    def test_required_directories_lists_operational_folders(self) -> None:
        paths = WorkspacePaths(Path("C:/workspace"))

        required = {p.as_posix() for p in paths.required_directories()}

        self.assertIn("C:/workspace/AI Space/pending", required)
        self.assertIn("C:/workspace/AI Space/logs/runs", required)
        self.assertIn("C:/workspace/AI Space/review/conflicts", required)
        self.assertIn("C:/workspace/AI Space/failed/technical-failures", required)
        self.assertIn("C:/workspace/FDE Brain", required)

    def test_ensure_directories_creates_all_required_directories(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            paths = WorkspacePaths(root)

            created = paths.ensure_directories()

            self.assertGreater(len(created), 0)
            for directory in paths.required_directories():
                self.assertTrue(directory.exists(), f"missing {directory}")


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 3: Run tests to verify they fail**

Run:

```powershell
python -m unittest tests.test_paths -v
```

Expected: FAIL with `ModuleNotFoundError` or `cannot import name 'WorkspacePaths'`.

- [ ] **Step 4: Implement path utilities**

Create `tools/fde_brain/paths.py`:

```python
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class WorkspacePaths:
    """Central path map for the Dual Graph LLM Wiki workspace."""

    root: Path

    @property
    def ai_space(self) -> Path:
        return self.root / "AI Space"

    @property
    def fde_brain(self) -> Path:
        return self.root / "FDE Brain"

    @property
    def pending(self) -> Path:
        return self.ai_space / "pending"

    @property
    def raw(self) -> Path:
        return self.ai_space / "raw"

    @property
    def normalized(self) -> Path:
        return self.ai_space / "normalized"

    @property
    def graph_root(self) -> Path:
        return self.ai_space / "graph"

    @property
    def brain_graph(self) -> Path:
        return self.graph_root / "brain"

    @property
    def source_graph(self) -> Path:
        return self.graph_root / "sources"

    @property
    def logs(self) -> Path:
        return self.ai_space / "logs"

    @property
    def review(self) -> Path:
        return self.ai_space / "review"

    @property
    def failed(self) -> Path:
        return self.ai_space / "failed"

    @property
    def system(self) -> Path:
        return self.ai_space / "system"

    @property
    def agent_protocol(self) -> Path:
        return self.system / "AGENT_PROTOCOL.md"

    @property
    def runbook(self) -> Path:
        return self.system / "RUNBOOK.md"

    @property
    def claude_entrypoint(self) -> Path:
        return self.root / "CLAUDE.md"

    @property
    def codex_entrypoint(self) -> Path:
        return self.root / "AGENTS.md"

    def required_directories(self) -> list[Path]:
        return [
            self.pending,
            self.raw,
            self.normalized,
            self.brain_graph,
            self.source_graph,
            self.logs / "runs",
            self.logs / "decisions",
            self.logs / "errors",
            self.logs / "promotions",
            self.review / "ambiguous",
            self.review / "conflicts",
            self.review / "needs-human",
            self.review / "low-confidence-normalization",
            self.failed / "technical-failures",
            self.system,
            self.fde_brain,
        ]

    def ensure_directories(self) -> list[Path]:
        created: list[Path] = []
        for directory in self.required_directories():
            if not directory.exists():
                directory.mkdir(parents=True, exist_ok=True)
                created.append(directory)
            gitkeep = directory / ".gitkeep"
            if directory != self.fde_brain and not gitkeep.exists():
                gitkeep.write_text("", encoding="utf-8")
        return created
```

- [ ] **Step 5: Run tests to verify they pass**

Run:

```powershell
python -m unittest tests.test_paths -v
```

Expected: PASS, 3 tests.

- [ ] **Step 6: Commit path utilities**

Run:

```powershell
git add tools/fde_brain/__init__.py tools/fde_brain/paths.py tests/test_paths.py
git commit -m "feat: add workspace path utilities"
```

Expected: commit succeeds.

---

### Task 3: Workspace Validator

**Files:**
- Create: `tools/fde_brain/validate_workspace.py`
- Create: `tests/test_validate_workspace.py`

- [ ] **Step 1: Write failing tests for validation**

Create `tests/test_validate_workspace.py`:

```python
import tempfile
import unittest
from pathlib import Path

from tools.fde_brain.paths import WorkspacePaths
from tools.fde_brain.validate_workspace import ValidationIssue, validate_workspace


class ValidateWorkspaceTests(unittest.TestCase):
    def test_reports_missing_required_directories(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            issues = validate_workspace(Path(tmp))

            codes = {issue.code for issue in issues}

            self.assertIn("missing-directory", codes)

    def test_reports_missing_protocol_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            paths = WorkspacePaths(root)
            paths.ensure_directories()

            issues = validate_workspace(root)

            missing_files = [issue for issue in issues if issue.code == "missing-file"]
            self.assertTrue(any("AGENT_PROTOCOL.md" in issue.path for issue in missing_files))
            self.assertTrue(any("CLAUDE.md" in issue.path for issue in missing_files))
            self.assertTrue(any("AGENTS.md" in issue.path for issue in missing_files))

    def test_clean_workspace_has_no_issues(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            paths = WorkspacePaths(root)
            paths.ensure_directories()
            paths.agent_protocol.write_text("# Protocol\n", encoding="utf-8")
            paths.runbook.write_text("# Runbook\n", encoding="utf-8")
            paths.claude_entrypoint.write_text("# Claude\n", encoding="utf-8")
            paths.codex_entrypoint.write_text("# Codex\n", encoding="utf-8")

            issues = validate_workspace(root)

            self.assertEqual([], issues)

    def test_validation_issue_formats_as_text(self) -> None:
        issue = ValidationIssue("missing-file", "AGENTS.md", "Create AGENTS.md")

        self.assertEqual("missing-file: AGENTS.md - Create AGENTS.md", str(issue))


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run tests to verify they fail**

Run:

```powershell
python -m unittest tests.test_validate_workspace -v
```

Expected: FAIL with `ModuleNotFoundError` for `tools.fde_brain.validate_workspace`.

- [ ] **Step 3: Implement validator**

Create `tools/fde_brain/validate_workspace.py`:

```python
from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path

from tools.fde_brain.paths import WorkspacePaths


@dataclass(frozen=True)
class ValidationIssue:
    code: str
    path: str
    message: str

    def __str__(self) -> str:
        return f"{self.code}: {self.path} - {self.message}"


def validate_workspace(root: Path) -> list[ValidationIssue]:
    paths = WorkspacePaths(root)
    issues: list[ValidationIssue] = []

    for directory in paths.required_directories():
        if not directory.is_dir():
            issues.append(
                ValidationIssue(
                    "missing-directory",
                    str(directory),
                    "Create this required workspace directory.",
                )
            )

    required_files = [
        paths.agent_protocol,
        paths.runbook,
        paths.claude_entrypoint,
        paths.codex_entrypoint,
    ]
    for file_path in required_files:
        if not file_path.is_file():
            issues.append(
                ValidationIssue(
                    "missing-file",
                    str(file_path),
                    "Create this required protocol or entrypoint file.",
                )
            )

    return issues


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate the FDE Brain workspace foundation.")
    parser.add_argument("--root", default=".", help="Workspace root. Defaults to current directory.")
    args = parser.parse_args(argv)

    issues = validate_workspace(Path(args.root).resolve())
    if not issues:
        print("workspace validation ok")
        return 0

    for issue in issues:
        print(issue, file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Run validator tests**

Run:

```powershell
python -m unittest tests.test_validate_workspace -v
```

Expected: PASS, 4 tests.

- [ ] **Step 5: Run validator against current workspace**

Run:

```powershell
python -m tools.fde_brain.validate_workspace --root .
```

Expected before Task 6 protocol files exist: non-zero exit with missing-file issues for protocol files.

- [ ] **Step 6: Commit validator**

Run:

```powershell
git add tools/fde_brain/validate_workspace.py tests/test_validate_workspace.py
git commit -m "feat: add workspace validator"
```

Expected: commit succeeds.

---

### Task 4: Local Engine Preflight

**Files:**
- Create: `tools/fde_brain/preflight.py`
- Create: `tests/test_preflight.py`

- [ ] **Step 1: Write failing tests for preflight**

Create `tests/test_preflight.py`:

```python
import subprocess
import unittest
from unittest.mock import patch

from tools.fde_brain.preflight import CheckResult, check_cli, check_ollama_model


class PreflightTests(unittest.TestCase):
    @patch("tools.fde_brain.preflight.shutil.which", return_value="C:/bin/claude.cmd")
    def test_check_cli_reports_present_command(self, _which) -> None:
        result = check_cli("Claude Code", "claude")

        self.assertEqual(CheckResult("Claude Code", True, "C:/bin/claude.cmd"), result)

    @patch("tools.fde_brain.preflight.shutil.which", return_value=None)
    def test_check_cli_reports_missing_command(self, _which) -> None:
        result = check_cli("Graphify", "graphify")

        self.assertEqual("Graphify", result.name)
        self.assertFalse(result.ok)
        self.assertEqual("graphify not found on PATH", result.detail)

    @patch("tools.fde_brain.preflight.subprocess.run")
    def test_check_ollama_model_reports_present_model(self, run) -> None:
        run.return_value = subprocess.CompletedProcess(
            args=["ollama", "list"],
            returncode=0,
            stdout="NAME ID SIZE MODIFIED\nglm-ocr:latest abc 1 GB today\n",
            stderr="",
        )

        result = check_ollama_model("glm-ocr")

        self.assertTrue(result.ok)
        self.assertEqual("GLM-OCR model", result.name)
        self.assertEqual("glm-ocr found in ollama list", result.detail)

    @patch("tools.fde_brain.preflight.subprocess.run")
    def test_check_ollama_model_reports_missing_model(self, run) -> None:
        run.return_value = subprocess.CompletedProcess(
            args=["ollama", "list"],
            returncode=0,
            stdout="NAME ID SIZE MODIFIED\nllama3 abc 1 GB today\n",
            stderr="",
        )

        result = check_ollama_model("glm-ocr")

        self.assertFalse(result.ok)
        self.assertEqual("glm-ocr not found in ollama list", result.detail)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run tests to verify they fail**

Run:

```powershell
python -m unittest tests.test_preflight -v
```

Expected: FAIL with `ModuleNotFoundError` for `tools.fde_brain.preflight`.

- [ ] **Step 3: Implement preflight module**

Create `tools/fde_brain/preflight.py`:

```python
from __future__ import annotations

import argparse
import shutil
import subprocess
from dataclasses import dataclass


@dataclass(frozen=True)
class CheckResult:
    name: str
    ok: bool
    detail: str

    def status_text(self) -> str:
        status = "OK" if self.ok else "MISSING"
        return f"{status}: {self.name} - {self.detail}"


def check_cli(name: str, command: str) -> CheckResult:
    found = shutil.which(command)
    if found:
        return CheckResult(name, True, found)
    return CheckResult(name, False, f"{command} not found on PATH")


def check_ollama_model(model_name: str = "glm-ocr") -> CheckResult:
    try:
        result = subprocess.run(
            ["ollama", "list"],
            check=False,
            capture_output=True,
            text=True,
            timeout=15,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return CheckResult("GLM-OCR model", False, f"could not run ollama list: {exc}")

    if result.returncode != 0:
        detail = result.stderr.strip() or f"ollama list exited with {result.returncode}"
        return CheckResult("GLM-OCR model", False, detail)

    if model_name.lower() in result.stdout.lower():
        return CheckResult("GLM-OCR model", True, f"{model_name} found in ollama list")
    return CheckResult("GLM-OCR model", False, f"{model_name} not found in ollama list")


def run_preflight(glm_ocr_model: str = "glm-ocr") -> list[CheckResult]:
    return [
        check_cli("Claude Code", "claude"),
        check_cli("Codex CLI", "codex"),
        check_cli("Ollama", "ollama"),
        check_ollama_model(glm_ocr_model),
        check_cli("Graphify", "graphify"),
        check_cli("Git", "git"),
    ]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check local engines for the FDE Brain pipeline.")
    parser.add_argument("--glm-ocr-model", default="glm-ocr", help="Ollama model name for GLM-OCR.")
    args = parser.parse_args(argv)

    results = run_preflight(args.glm_ocr_model)
    for result in results:
        print(result.status_text())

    return 0 if all(result.ok for result in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Run preflight tests**

Run:

```powershell
python -m unittest tests.test_preflight -v
```

Expected: PASS, 4 tests.

- [ ] **Step 5: Run real preflight**

Run:

```powershell
python -m tools.fde_brain.preflight
```

Expected on the current machine before installing Graphify/Ollama model:

```text
OK: Claude Code - ...
OK: Codex CLI - ...
MISSING: Ollama - ollama not found on PATH
MISSING: GLM-OCR model - could not run ollama list: ...
MISSING: Graphify - graphify not found on PATH
OK: Git - ...
```

If Ollama is installed before execution, the Ollama and GLM-OCR lines may be `OK`.

- [ ] **Step 6: Commit preflight**

Run:

```powershell
git add tools/fde_brain/preflight.py tests/test_preflight.py
git commit -m "feat: add local engine preflight"
```

Expected: commit succeeds.

---

### Task 5: Graphify Command Wrapper Helpers

**Files:**
- Create: `tools/fde_brain/graphify.py`
- Create: `tests/test_graphify.py`

- [ ] **Step 1: Write failing tests for Graphify helpers**

Create `tests/test_graphify.py`:

```python
import unittest
from pathlib import Path

from tools.fde_brain.graphify import GraphifyCommand, brain_graph_extract, source_graph_extract


class GraphifyTests(unittest.TestCase):
    def test_brain_graph_extract_uses_fde_brain_input_and_brain_output(self) -> None:
        command = brain_graph_extract(Path("C:/workspace"))

        self.assertEqual(
            GraphifyCommand(
                args=[
                    "graphify",
                    "extract",
                    "C:/workspace/FDE Brain",
                    "--backend",
                    "claude-cli",
                    "--out",
                    "C:/workspace/AI Space/graph/brain",
                ]
            ),
            command,
        )

    def test_source_graph_extract_uses_normalized_input_and_source_output(self) -> None:
        command = source_graph_extract(Path("C:/workspace"))

        self.assertEqual(
            [
                "graphify",
                "extract",
                "C:/workspace/AI Space/normalized",
                "--backend",
                "claude-cli",
                "--out",
                "C:/workspace/AI Space/graph/sources",
            ],
            command.args,
        )

    def test_command_formats_for_powershell(self) -> None:
        command = GraphifyCommand(["graphify", "query", "hello world", "--budget", "1500"])

        self.assertEqual('graphify query "hello world" --budget 1500', command.to_powershell())


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run tests to verify they fail**

Run:

```powershell
python -m unittest tests.test_graphify -v
```

Expected: FAIL with `ModuleNotFoundError` for `tools.fde_brain.graphify`.

- [ ] **Step 3: Implement Graphify helpers**

Create `tools/fde_brain/graphify.py`:

```python
from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path

from tools.fde_brain.paths import WorkspacePaths


@dataclass(frozen=True)
class GraphifyCommand:
    args: list[str]

    def to_powershell(self) -> str:
        rendered: list[str] = []
        for arg in self.args:
            if any(char.isspace() for char in arg):
                escaped = arg.replace('"', '`"')
                rendered.append(f'"{escaped}"')
            else:
                rendered.append(arg)
        return " ".join(rendered)


def _as_posix_string(path: Path) -> str:
    return path.as_posix()


def brain_graph_extract(root: Path, backend: str = "claude-cli") -> GraphifyCommand:
    paths = WorkspacePaths(root)
    return GraphifyCommand(
        [
            "graphify",
            "extract",
            _as_posix_string(paths.fde_brain),
            "--backend",
            backend,
            "--out",
            _as_posix_string(paths.brain_graph),
        ]
    )


def source_graph_extract(root: Path, backend: str = "claude-cli") -> GraphifyCommand:
    paths = WorkspacePaths(root)
    return GraphifyCommand(
        [
            "graphify",
            "extract",
            _as_posix_string(paths.normalized),
            "--backend",
            backend,
            "--out",
            _as_posix_string(paths.source_graph),
        ]
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Print Graphify commands for this workspace.")
    parser.add_argument("target", choices=["brain", "sources"], help="Graph to update.")
    parser.add_argument("--root", default=".", help="Workspace root. Defaults to current directory.")
    parser.add_argument("--backend", default="claude-cli", help="Graphify backend. Defaults to claude-cli.")
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    command = brain_graph_extract(root, args.backend) if args.target == "brain" else source_graph_extract(root, args.backend)
    print(command.to_powershell())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Run Graphify tests**

Run:

```powershell
python -m unittest tests.test_graphify -v
```

Expected: PASS, 3 tests.

- [ ] **Step 5: Print real commands**

Run:

```powershell
python -m tools.fde_brain.graphify brain --root .
python -m tools.fde_brain.graphify sources --root .
```

Expected: prints two PowerShell-safe `graphify extract ... --backend claude-cli --out ...` commands.

- [ ] **Step 6: Commit Graphify helpers**

Run:

```powershell
git add tools/fde_brain/graphify.py tests/test_graphify.py
git commit -m "feat: add graphify command helpers"
```

Expected: commit succeeds.

---

### Task 6: Shared Agent Protocol And Entrypoints

**Files:**
- Create: `AI Space/system/AGENT_PROTOCOL.md`
- Create: `AI Space/system/RUNBOOK.md`
- Create: `AGENTS.md`
- Create: `CLAUDE.md`

- [ ] **Step 1: Write shared agent protocol**

Create `AI Space/system/AGENT_PROTOCOL.md`:

```markdown
# Agent Protocol

This workspace is a Dual Graph LLM Wiki for Forward Deployed AI Engineering.

## Roles

- `FDE Brain/` is the final Obsidian vault.
- `AI Space/` is the AI operating area.
- Claude Code is the scheduled pipeline runner.
- Codex is the manual development and maintenance agent.
- Both Claude Code and Codex can answer questions against the knowledge base.

## Non-Negotiable Rules

- Do not treat Graphify output as source truth.
- Use Graphify to find candidate files, then read the real Markdown files.
- Do not write generated Graphify Obsidian exports into `FDE Brain/`.
- Do not put drafts, temporary notes, or raw dumps in `FDE Brain/`.
- Every knowledge-base answer must cite sources.
- If a query uses `AI Space/normalized/`, promote stable/reusable knowledge into `FDE Brain/` in the same turn.
- Never permanently delete originals.
- Do not clean `AI Space/pending/` unless items were safely archived, reviewed, or failed.

## Retrieval Order

1. Query Brain Graph in `AI Space/graph/brain/`.
2. Read the relevant notes in `FDE Brain/`.
3. Answer with citations from the note and its precompiled sources.
4. If Brain Graph is insufficient, query Source Graph in `AI Space/graph/sources/`.
5. Read relevant files in `AI Space/normalized/`.
6. Answer with citations.
7. Promote stable/reusable knowledge into `FDE Brain/` before finishing the turn.
8. Update Brain Graph or mark it stale.
9. Log and commit the promotion.

## Citation Rules

Prefer the finest available locator:

- final note and heading
- normalized source file and heading, chapter, section, page, or line
- raw source and page or chapter
- URL and access date for web sources

If a locator is coarse, say so.

## FDE Brain Authoring

`FDE Brain/` must be Obsidian-native Markdown:

- use Properties/frontmatter
- use wikilinks
- use aliases
- use tags
- link to headings when useful
- keep provenance inside the note

Use `kepano/obsidian-skills@obsidian-markdown` as the authoring reference.

## Graphify

Use two graphs:

- Brain Graph: `AI Space/graph/brain/`
- Source Graph: `AI Space/graph/sources/`

Preferred backend:

```powershell
graphify extract <input> --backend claude-cli --out <output>
```

## Review And Failure Routing

- Ambiguous content: `AI Space/review/ambiguous/`
- Conflicts: `AI Space/review/conflicts/`
- Human judgment needed: `AI Space/review/needs-human/`
- Low-confidence OCR or parsing: `AI Space/review/low-confidence-normalization/`
- Technical failures: `AI Space/failed/technical-failures/`

## Git

Commit after successful ingestion runs and query-driven promotions.

Use focused commit messages:

```text
chore(ai-pipeline): ingest pending batch YYYY-MM-DD
docs(fde-brain): promote source knowledge from query
chore(graph): refresh brain and source graphs
```
```

- [ ] **Step 2: Write runbook**

Create `AI Space/system/RUNBOOK.md`:

```markdown
# FDE Brain Runbook

## Validate Workspace

```powershell
python -m tools.fde_brain.validate_workspace --root .
```

Expected when foundation is complete:

```text
workspace validation ok
```

## Check Local Engines

```powershell
python -m tools.fde_brain.preflight
```

Expected required tools:

- Claude Code
- Codex CLI
- Git
- Ollama
- GLM-OCR model in Ollama
- Graphify

## Print Graphify Commands

```powershell
python -m tools.fde_brain.graphify brain --root .
python -m tools.fde_brain.graphify sources --root .
```

## Manual Brain Graph Refresh

Print command:

```powershell
python -m tools.fde_brain.graphify brain --root .
```

Copy and run the printed command after confirming Graphify is installed.

## Manual Source Graph Refresh

Print command:

```powershell
python -m tools.fde_brain.graphify sources --root .
```

Copy and run the printed command after confirming Graphify is installed.

## Pending Folder Contract

`AI Space/pending/` is a temporary drop zone. It can contain arbitrary files and notes. It should be empty after a successful scheduled ingestion run, but only after files are safely archived, reviewed, or failed.
```

- [ ] **Step 3: Write Codex entrypoint**

Create `AGENTS.md`:

```markdown
# Codex Workspace Instructions

This workspace is the Dual Graph LLM Wiki for Forward Deployed AI Engineering.

Before answering knowledge-base questions or modifying `FDE Brain/`, read:

```text
AI Space/system/AGENT_PROTOCOL.md
```

Operational commands are documented in:

```text
AI Space/system/RUNBOOK.md
```

`FDE Brain/` is the final Obsidian vault. `AI Space/` is the AI operating area.
```

- [ ] **Step 4: Write Claude entrypoint**

Create `CLAUDE.md`:

```markdown
# Claude Code Workspace Instructions

This workspace is the Dual Graph LLM Wiki for Forward Deployed AI Engineering.

Before running scheduled ingestion, answering knowledge-base questions, or modifying `FDE Brain/`, read:

```text
AI Space/system/AGENT_PROTOCOL.md
```

Operational commands are documented in:

```text
AI Space/system/RUNBOOK.md
```

Claude Code is the preferred scheduled runner. Codex is the manual development and maintenance agent.
```

- [ ] **Step 5: Run validator**

Run:

```powershell
python -m tools.fde_brain.validate_workspace --root .
```

Expected output:

```text
workspace validation ok
```

- [ ] **Step 6: Verify protocol mentions required rules**

Run:

```powershell
rg -n "Query uses|Graphify|Source Graph|Brain Graph|kepano/obsidian-skills|Every knowledge-base answer" "AI Space/system/AGENT_PROTOCOL.md"
```

Expected: output includes all searched concepts except `Query uses`; the required phrase is represented as `If a query uses`.

- [ ] **Step 7: Commit protocol files**

Run:

```powershell
git add "AI Space/system/AGENT_PROTOCOL.md" "AI Space/system/RUNBOOK.md" AGENTS.md CLAUDE.md
git commit -m "docs: add shared agent protocol"
```

Expected: commit succeeds.

---

### Task 7: End-To-End Foundation Verification

**Files:**
- Modify: none

- [ ] **Step 1: Run all unit tests**

Run:

```powershell
python -m unittest discover -s tests -v
```

Expected: all tests pass.

- [ ] **Step 2: Run workspace validator**

Run:

```powershell
python -m tools.fde_brain.validate_workspace --root .
```

Expected output:

```text
workspace validation ok
```

- [ ] **Step 3: Run local engine preflight**

Run:

```powershell
python -m tools.fde_brain.preflight
```

Expected:

- `Claude Code` should be `OK`.
- `Codex CLI` should be `OK`.
- `Git` should be `OK`.
- `Ollama`, `GLM-OCR model`, and `Graphify` may be `MISSING` until installed.

The command may exit with code `1` when optional local engines are missing. That is acceptable for this foundation plan if the output clearly identifies missing tools.

- [ ] **Step 4: Confirm no accidental files in pending**

Run:

```powershell
Get-ChildItem -Force "AI Space/pending" | Where-Object { $_.Name -ne ".gitkeep" }
```

Expected: no output.

- [ ] **Step 5: Review git status**

Run:

```powershell
git status --short
```

Expected: either clean, or only intended files from the current task.

- [ ] **Step 6: Commit final verification note if needed**

If no files changed during verification, do not commit.

If a log or small doc note was intentionally created during verification, run:

```powershell
git add <changed-file>
git commit -m "test: verify foundation setup"
```

Expected: commit succeeds only if there are intentional changes.

---

## Self-Review Checklist

- Spec coverage:
  - Workspace folders are covered by Task 1.
  - Shared multi-agent protocol is covered by Task 6.
  - Obsidian guidance is covered by Task 6.
  - Graphify routing design is covered by Task 5 and Task 6.
  - Local-engine preference is covered by Task 4.
  - Git safety starts with Task 1 and per-task commits.
  - Full ingestion, OCR normalization, scheduling, and query-time promotion are intentionally out of scope for Foundation V1 and require later plans.

- Placeholder scan:
  - No task uses forbidden empty-detail instructions.
  - Code snippets are complete for files created in this plan.
  - Commands include expected outcomes.

- Type consistency:
  - `WorkspacePaths` is used consistently by validator and Graphify helpers.
  - `CheckResult` and `ValidationIssue` have stable fields used by tests.
  - Graphify helper names match tests: `brain_graph_extract`, `source_graph_extract`.
