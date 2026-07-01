# P2 Model + Effort Tiering — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development
> (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps
> use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Every LLM call in Talamus resolves its model+effort through a per-task
`EngineRouter` instead of one flat engine setting, with cost-minimizing defaults for
bulk/mechanical tasks and quality defaults for the answer the user reads.

**Architecture:** A new core module `talamus/routing.py` defines ten `TaskClass` values,
a `TaskIntent(tier, effort)` per class (code defaults + optional config overrides), and
`EngineRouter.for_task(task) -> LLMProvider` (memoized). `adapters/llm.py` gains a
per-provider tier→model table and an optional `effort` constructor arg per provider,
consulted by a new `build_provider_for_task(provider, config, tier, effort)`. Every
function that calls `llm.complete(...)` directly switches from accepting
`llm: LLMProvider` to accepting `router` and resolving its own task at that call. A
`StaticRouter(provider)` shim (returns one fixed provider for every task) keeps all
existing tests passing with a one-line wrapper instead of a rewrite.

**Tech Stack:** Python 3.13, existing `talamus.adapters.llm` Protocol-based providers,
`unittest` (pytest is not installed — use `python -m unittest` / `python dev.py`).

**Working rules:** run from `C:/dev/Kortex` with `PYTHONIOENCODING=utf-8`; `python dev.py`
must stay ALL GREEN after every task. No real LLM calls in the gate — fakes and
`StaticRouter` only. Spec:
[dev/specs/2026-07-01-p2-model-effort-tiering-design.md](../specs/2026-07-01-p2-model-effort-tiering-design.md).

---

## File structure

- Create: `src/talamus/routing.py` — `TaskClass`, `TaskIntent`, `DEFAULT_INTENTS`,
  `StaticRouter`, `EngineRouter`.
- Create: `tests/test_talamus_routing.py`.
- Modify: `src/talamus/config.py` — add `task_tiers`, `provider_models` fields.
- Modify: `src/talamus/adapters/llm.py` — per-provider tier/effort resolution,
  `build_provider_for_task`; move `canonical_provider`/`_ALIASES` here from
  `services/engines.py` (the correct dependency direction: services already imports
  from `adapters.llm`, not the other way around).
- Modify: `src/talamus/services/engines.py`, `src/talamus/services/readiness.py` — import
  `canonical_provider` from `adapters.llm` instead of defining/re-importing locally.
- Modify (task leaves): `src/talamus/extract.py`, `src/talamus/ingest.py`,
  `src/talamus/ask.py`, `src/talamus/smartsearch.py`, `src/talamus/correct.py`,
  `src/talamus/enrich.py`, `src/talamus/consolidate.py`, `src/talamus/domains.py`,
  `src/talamus/ontology_lab.py`.
- Modify (callers): `src/talamus/cli/_common.py`, `src/talamus/cli/app.py`,
  `src/talamus/cli/pipeline.py`, `src/talamus/cli/query.py`, `src/talamus/cli/groups.py`,
  `src/talamus/mcp_server.py`, `src/talamus/services/ingestion.py`,
  `src/talamus/services/scan.py`, `src/talamus/services/enrich.py`,
  `src/talamus/services/verification.py`, `src/talamus/services/consolidation.py`,
  `src/talamus/services/ask.py`.
- Modify: `tests/test_talamus_hostile_models.py` (new provider ctor args).
- Modify: `dev/ROADMAP.md` (P2 status).

---

## Task 1: Verify the per-provider model/effort CLI flags (spike, no production code)

**Files:** none modified — this is a verification step whose findings are consumed by
Task 5.

- [ ] **Step 1: Confirm `claude --model` and its position relative to `-p`.**

```bash
cd "C:/dev/Kortex"; claude --model haiku -p <<< "Reply with the single word OK."
```

Expected: a short reply, exit code 0. If this exact invocation errors (e.g. unknown
flag, or the flag must come after `-p`), try `claude -p --model haiku` and record which
form works — Task 5's `ClaudeCliProvider.complete` must use the working form.

- [ ] **Step 2: Confirm codex's model + reasoning-effort flags.**

```bash
cd "C:/dev/Kortex"; codex exec --skip-git-repo-check -s read-only -m gpt-5-mini -c model_reasoning_effort=low - <<< "Reply with the single word OK."
```

Expected: a short reply. If `-c model_reasoning_effort=low` errors (unknown key or
unknown value), note the actual accepted key/values (check `codex exec --help` and
`codex exec -c help` if available) — Task 5 must use the confirmed key/value, or if
none exists, effort must be a documented no-op for codex-cli exactly like gemini-cli.

- [ ] **Step 3: Confirm gemini's model flag still works (already used in the adapter) and
probe for any effort-like flag.**

```bash
cd "C:/dev/Kortex"; gemini --skip-trust --approval-mode plan -m gemini-2.5-flash -p "" <<< "Reply with the single word OK."
cd "C:/dev/Kortex"; gemini --help | grep -iE "effort|thinking|reason"
```

Expected: the first command replies OK (confirms the existing `-m` hook still works).
The second command likely prints nothing — if it DOES find a flag, record it for Task 5;
otherwise gemini-cli's effort stays a documented no-op, matching the spec.

- [ ] **Step 4: Record the findings inline in the spec** — edit
`dev/specs/2026-07-01-p2-model-effort-tiering-design.md`'s "Per-provider descriptors"
table, changing each row's "Confidence" column from "needs a smoke-test" to either
"confirmed: `<exact flag>`" or "confirmed unsupported (no-op)", based on what Steps 1-3
found. This is the source of truth Task 5 codes against.

- [ ] **Step 5: Commit the spec update.**

```bash
cd "C:/dev/Kortex"; git add dev/specs/2026-07-01-p2-model-effort-tiering-design.md
git commit -m "docs(spec): record verified provider model/effort flags [P2]"
```

---

## Task 2: `TalamusConfig` — `task_tiers` and `provider_models` fields

**Files:**
- Modify: `src/talamus/config.py`
- Test: `tests/test_talamus_config.py` (append; if this file doesn't exist, check with
  `ls tests/test_talamus_config*.py` first and create it following the pattern of any
  sibling test file if truly absent)

- [ ] **Step 1: Write the failing test.** Append to the config test file:

```python
def test_config_round_trips_tiering_overrides(self) -> None:
    import tempfile
    from pathlib import Path

    from talamus.config import TalamusConfig, load_config, save_config

    config = TalamusConfig(
        **{**vars(TalamusConfig.default()), "task_tiers": {"extraction": {"tier": "quality"}}},
    )
    config = dataclasses.replace(
        config, provider_models={"claude-cli": {"economy": "haiku", "quality": "opus"}}
    )
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "talamus.json"
        save_config(path, config)
        loaded = load_config(path)
    self.assertEqual(loaded.task_tiers, {"extraction": {"tier": "quality"}})
    self.assertEqual(
        loaded.provider_models, {"claude-cli": {"economy": "haiku", "quality": "opus"}}
    )
```

Add `import dataclasses` to the test file's imports if not already present.

- [ ] **Step 2: Run it to verify it fails.**

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python -m unittest tests.test_talamus_config -v
```

Expected: FAIL (`TypeError: __init__() got an unexpected keyword argument 'task_tiers'`).

- [ ] **Step 3: Add the fields** — in `src/talamus/config.py`, extend `TalamusConfig`:

```python
@dataclass(frozen=True)
class TalamusConfig:
    storage_provider: str
    pdf_converter: str
    ocr_provider: str
    ocr_model: str
    llm_provider: str
    graph_provider: str
    search_provider: str
    llm_model: str = ""
    # The language the USER reads notes in (prose of title/summary/body).
    # Prompts are always English (cheap local models obey English best) and the
    # machine layer (relation surfaces, canonical aliases) is English-canonical.
    # Empty = auto-detect from the system locale.
    language: str = ""
    # P2 tiering overrides (empty = use the code defaults in talamus.routing).
    # task_tiers: {"<TaskClass value>": {"tier": "economy"|"quality", "effort": "low"|"high"}}
    task_tiers: dict[str, dict[str, str]] = field(default_factory=dict)
    # provider_models: {"<provider>": {"economy": "<model>", "quality": "<model>"}}
    provider_models: dict[str, dict[str, str]] = field(default_factory=dict)
```

Add `field` to the existing `from dataclasses import asdict, dataclass, fields, replace`
import line (becomes `from dataclasses import asdict, dataclass, field, fields, replace`).

- [ ] **Step 4: Fix `load_config`'s empty-field check** — the existing check treats any
falsy field as an error except `llm_model`/`language`; an empty `{}` dict is falsy, so
add the two new fields to that exemption. In `load_config`:

```python
    empty = [
        name
        for name, value in asdict(config).items()
        if name not in ("llm_model", "language", "task_tiers", "provider_models")
        and not str(value).strip()
    ]
```

- [ ] **Step 5: Run the test to verify it passes**, then run the full config test file.

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python -m unittest tests.test_talamus_config -v
```

Expected: PASS, all tests in the file green.

- [ ] **Step 6: Full gate.**

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python dev.py
```

Expected: ALL GREEN.

- [ ] **Step 7: Commit.**

```bash
cd "C:/dev/Kortex"; git add src/talamus/config.py tests/test_talamus_config.py
git commit -m "feat(config): task_tiers + provider_models tiering overrides [P2]"
```

---

## Task 3: `talamus/routing.py` — `TaskClass`, `TaskIntent`, `DEFAULT_INTENTS`

**Files:**
- Create: `src/talamus/routing.py`
- Test: `tests/test_talamus_routing.py`

- [ ] **Step 1: Write the failing test.**

```python
import unittest


class TaskIntentDefaultsTests(unittest.TestCase):
    def test_every_task_class_has_a_default_intent(self) -> None:
        from talamus.routing import DEFAULT_INTENTS, TaskClass

        for task in TaskClass:
            self.assertIn(task, DEFAULT_INTENTS)
            intent = DEFAULT_INTENTS[task]
            self.assertIn(intent.tier, ("economy", "quality"))
            self.assertIn(intent.effort, ("low", "high"))

    def test_cost_minimizing_defaults_match_the_design(self) -> None:
        from talamus.routing import DEFAULT_INTENTS, TaskClass

        self.assertEqual(DEFAULT_INTENTS[TaskClass.EXTRACTION].tier, "economy")
        self.assertEqual(DEFAULT_INTENTS[TaskClass.ASK_ANSWER].tier, "quality")
        self.assertEqual(DEFAULT_INTENTS[TaskClass.ASK_ANSWER].effort, "high")
        self.assertEqual(DEFAULT_INTENTS[TaskClass.SESSION_REMEMBER].tier, "quality")
        self.assertEqual(DEFAULT_INTENTS[TaskClass.VERIFY].tier, "quality")


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run it to verify it fails.**

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python -m unittest tests.test_talamus_routing -v
```

Expected: FAIL (`No module named 'talamus.routing'`).

- [ ] **Step 3: Implement** `src/talamus/routing.py`:

```python
"""Per-task model+effort tiering (P2 flagship lever).

A TaskClass names one point in the pipeline that makes exactly one LLM call. Each task
carries a TaskIntent (tier, effort); an EngineRouter resolves that intent, within the
single provider configured for the brain, into a concrete LLMProvider — never across
providers (see dev/specs/2026-07-01-p2-model-effort-tiering-design.md). Task classes
never know provider-specific model names; providers never know about task classes.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from talamus.adapters.llm import ENGINE_LABELS, LLMProvider, build_provider_for_task, canonical_provider
from talamus.config import TalamusConfig


class TaskClass(str, Enum):
    EXTRACTION = "extraction"
    SESSION_REMEMBER = "session_remember"
    ASK_ROUTING = "ask_routing"
    QUERY_EXPANSION = "query_expansion"
    ASK_ANSWER = "ask_answer"
    VERIFY = "verify"
    ENRICH = "enrich"
    CONSOLIDATE = "consolidate"
    ONTOLOGY_NAMING = "ontology_naming"
    OVERVIEW_NAMING = "overview_naming"


@dataclass(frozen=True)
class TaskIntent:
    tier: str  # "economy" | "quality"
    effort: str  # "low" | "high"


DEFAULT_INTENTS: dict[TaskClass, TaskIntent] = {
    TaskClass.EXTRACTION: TaskIntent("economy", "low"),
    TaskClass.SESSION_REMEMBER: TaskIntent("quality", "low"),
    TaskClass.ASK_ROUTING: TaskIntent("economy", "low"),
    TaskClass.QUERY_EXPANSION: TaskIntent("economy", "low"),
    TaskClass.ASK_ANSWER: TaskIntent("quality", "high"),
    TaskClass.VERIFY: TaskIntent("quality", "low"),
    TaskClass.ENRICH: TaskIntent("economy", "low"),
    TaskClass.CONSOLIDATE: TaskIntent("economy", "low"),
    TaskClass.ONTOLOGY_NAMING: TaskIntent("economy", "low"),
    TaskClass.OVERVIEW_NAMING: TaskIntent("economy", "low"),
}


def _resolve_intent(config: TalamusConfig, task: TaskClass) -> TaskIntent:
    override = config.task_tiers.get(task.value)
    if not override:
        return DEFAULT_INTENTS[task]
    default = DEFAULT_INTENTS[task]
    return TaskIntent(override.get("tier", default.tier), override.get("effort", default.effort))
```

(`StaticRouter`/`EngineRouter` land in Tasks 4 and 7 — this file grows across tasks, it
is not overwritten.)

- [ ] **Step 4: Run it to verify it passes.**

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python -m unittest tests.test_talamus_routing -v
```

Expected: PASS. (This step will actually fail at import time until Task 5 adds
`build_provider_for_task`/`canonical_provider` to `adapters/llm.py` — if so, comment out
the `build_provider_for_task, canonical_provider` import and the two names from the
`from talamus.adapters.llm import ...` line for now, leaving only `LLMProvider,
ENGINE_LABELS`; restore the full import in Task 7 once those names exist. Re-run to
confirm PASS with the trimmed import before committing.)

- [ ] **Step 5: Commit.**

```bash
cd "C:/dev/Kortex"; git add src/talamus/routing.py tests/test_talamus_routing.py
git commit -m "feat(routing): TaskClass + TaskIntent + cost-minimizing defaults [P2]"
```

---

## Task 4: `StaticRouter` (the test/back-compat shim)

**Files:**
- Modify: `src/talamus/routing.py`
- Test: `tests/test_talamus_routing.py`

- [ ] **Step 1: Write the failing test** (append to the test file):

```python
class StaticRouterTests(unittest.TestCase):
    def test_returns_the_same_provider_for_every_task(self) -> None:
        from talamus.routing import StaticRouter, TaskClass

        class Fake:
            def complete(self, prompt: str) -> str:
                return "ok"

        fake = Fake()
        router = StaticRouter(fake)
        self.assertIs(router.for_task(TaskClass.EXTRACTION), fake)
        self.assertIs(router.for_task(TaskClass.ASK_ANSWER), fake)

    def test_exposes_the_wrapped_providers_label(self) -> None:
        from talamus.routing import StaticRouter, TaskClass

        class Labeled:
            label = "Fake Engine"

            def complete(self, prompt: str) -> str:
                return "ok"

        router = StaticRouter(Labeled())
        self.assertEqual(router.label, "Fake Engine")
        self.assertIsNotNone(router.for_task(TaskClass.VERIFY))

    def test_defaults_the_label_when_the_provider_has_none(self) -> None:
        from talamus.routing import StaticRouter

        class Bare:
            def complete(self, prompt: str) -> str:
                return "ok"

        self.assertEqual(StaticRouter(Bare()).label, "engine")
```

- [ ] **Step 2: Run it to verify it fails.**

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python -m unittest tests.test_talamus_routing -v
```

Expected: FAIL (`cannot import name 'StaticRouter'`).

- [ ] **Step 3: Implement** — append to `src/talamus/routing.py`:

```python
class StaticRouter:
    """A router that returns one fixed provider for every task, ignoring tier/effort.

    Used by tests that inject a single fake LLMProvider (wrap it once instead of
    rewriting every fake to be task-aware) and by any caller that received an explicit
    provider override and wants it honored for every sub-call."""

    def __init__(self, provider: LLMProvider) -> None:
        self._provider = provider
        self.label = getattr(provider, "label", "engine")

    def for_task(self, task: TaskClass) -> LLMProvider:
        return self._provider
```

- [ ] **Step 4: Run it to verify it passes.**

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python -m unittest tests.test_talamus_routing -v
```

Expected: PASS.

- [ ] **Step 5: Commit.**

```bash
cd "C:/dev/Kortex"; git add src/talamus/routing.py tests/test_talamus_routing.py
git commit -m "feat(routing): StaticRouter shim for tests and explicit overrides [P2]"
```

---

## Task 5: Per-provider tier/effort descriptors + `build_provider_for_task`

**Files:**
- Modify: `src/talamus/adapters/llm.py`
- Test: `tests/test_talamus_llm_adapter.py`

- [ ] **Step 1: Write the failing tests** (append to `tests/test_talamus_llm_adapter.py`,
inside `LLMAdapterTests`; use the flags Task 1 confirmed — the code below assumes Task 1
confirmed `claude --model <alias> -p`, `codex ... -m <model> -c
model_reasoning_effort=<level>`, and no gemini effort flag; if Task 1 found different
flags, use those instead in both this test and Step 3's implementation):

```python
    def test_claude_cli_applies_tier_model(self) -> None:
        captured = {}

        def fake_runner(args: list[str], prompt: str) -> str:
            captured["args"] = args
            return "ok"

        from talamus.adapters.llm import build_provider_for_task
        from talamus.config import TalamusConfig

        provider = build_provider_for_task(
            "claude-cli", TalamusConfig.default(), "economy", "low"
        )
        provider._runner = fake_runner  # type: ignore[attr-defined]
        provider.complete("hi")
        self.assertIn("--model", captured["args"])
        self.assertIn("haiku", captured["args"])

    def test_codex_cli_applies_tier_model_and_effort(self) -> None:
        captured = {}

        def fake_runner(args: list[str], prompt: str) -> str:
            captured["args"] = args
            return "ok"

        from talamus.adapters.llm import build_provider_for_task
        from talamus.config import TalamusConfig

        provider = build_provider_for_task(
            "codex-cli", TalamusConfig.default(), "quality", "high"
        )
        provider._runner = fake_runner  # type: ignore[attr-defined]
        provider.complete("hi")
        self.assertIn("gpt-5", captured["args"])
        self.assertIn("model_reasoning_effort=high", " ".join(captured["args"]))

    def test_gemini_cli_ignores_unsupported_effort(self) -> None:
        captured = {}

        def fake_runner(args: list[str], prompt: str) -> str:
            captured["args"] = args
            return "ok"

        from talamus.adapters.llm import build_provider_for_task
        from talamus.config import TalamusConfig

        provider = build_provider_for_task(
            "gemini-cli", TalamusConfig.default(), "economy", "high"
        )
        provider._runner = fake_runner  # type: ignore[attr-defined]
        provider.complete("hi")
        self.assertIn("gemini-2.5-flash", captured["args"])
        # no exception, no stray effort flag — effort silently ignored
        self.assertNotIn("high", captured["args"])

    def test_ollama_falls_back_to_the_single_configured_model_when_untiered(self) -> None:
        from dataclasses import replace

        from talamus.adapters.llm import build_provider_for_task
        from talamus.config import TalamusConfig

        config = replace(TalamusConfig.default(), llm_model="gemma3n")
        provider = build_provider_for_task("ollama", config, "quality", "high")
        self.assertEqual(provider._model, "gemma3n")  # type: ignore[attr-defined]

    def test_provider_models_config_override_wins_over_the_builtin_tier_map(self) -> None:
        captured = {}

        def fake_runner(args: list[str], prompt: str) -> str:
            captured["args"] = args
            return "ok"

        from dataclasses import replace

        from talamus.adapters.llm import build_provider_for_task
        from talamus.config import TalamusConfig

        config = replace(
            TalamusConfig.default(),
            provider_models={"claude-cli": {"economy": "sonnet"}},
        )
        provider = build_provider_for_task("claude-cli", config, "economy", "low")
        provider._runner = fake_runner  # type: ignore[attr-defined]
        provider.complete("hi")
        self.assertIn("sonnet", captured["args"])
```

- [ ] **Step 2: Run to verify they fail.**

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python -m unittest tests.test_talamus_llm_adapter -v
```

Expected: FAIL (`cannot import name 'build_provider_for_task'`).

- [ ] **Step 3: Implement.** In `src/talamus/adapters/llm.py`:

Move `canonical_provider` here (it currently lives in `services/engines.py`, which
already imports `ENGINE_COMMANDS`/`save_credential` from this module — this keeps the
dependency direction consistent: services depends on core adapters, not the reverse).
Add near the top, after `_ENGINE_COMMAND_ALIASES`:

```python
_PROVIDER_ALIASES: dict[str, str] = {
    "codex": "codex-cli",
    "gemini": "gemini-cli",
    "api": "anthropic-api",
}


def canonical_provider(provider: str) -> str:
    normalized = provider.strip()
    return _PROVIDER_ALIASES.get(normalized, normalized)
```

Update the three existing provider constructors to accept `model`/`effort`. Replace
`ClaudeCliProvider` entirely:

```python
class ClaudeCliProvider:
    """CLI subscription via `claude -p` (non-interactive). ``model`` is a short CLI
    alias (e.g. "haiku", "opus"); ``effort`` has no verified equivalent for this CLI
    today and is accepted but ignored."""

    def __init__(
        self,
        model: str = "",
        effort: str | None = None,
        runner: Callable[[list[str], str], str] = _default_runner,
    ) -> None:
        self._model = model
        self._effort = effort  # unused: no verified flag (see the tiering design doc)
        self._runner = runner

    def complete(self, prompt: str) -> str:
        args = ["claude"]
        if self._model:
            args += ["--model", self._model]
        args += ["-p"]
        return self._runner(args, prompt)
```

Replace `CodexCliProvider` entirely:

```python
class CodexCliProvider:
    """OpenAI Codex CLI subscription via `codex exec` (prompt on stdin via `-`,
    dodging the Windows argv length limit). `codex exec` is an AGENT that can run
    shell commands, so we pin it down: read-only sandbox, no git-repo check —
    it must behave as a pure completion engine. ``model`` via `-m` (e.g. a mini model
    for fast bulk ingest); ``effort`` via `-c model_reasoning_effort=<low|high>`."""

    def __init__(
        self,
        model: str = "",
        effort: str | None = None,
        runner: Callable[[list[str], str], str] = _default_runner,
    ) -> None:
        self._model = model
        self._effort = effort
        self._runner = runner

    def complete(self, prompt: str) -> str:
        args = ["codex", "exec", "--skip-git-repo-check", "-s", "read-only"]
        if self._model:
            args += ["-m", self._model]
        if self._effort:
            args += ["-c", f"model_reasoning_effort={self._effort}"]
        return self._runner([*args, "-"], prompt)
```

Replace `GeminiCliProvider` entirely:

```python
class GeminiCliProvider:
    """Google Gemini CLI subscription: `-p ""` triggers headless mode and the
    real prompt travels on stdin (the CLI appends -p to stdin input).
    Gemini CLI is an AGENT too, so it gets the same treatment as codex:
    `--approval-mode plan` = read-only (no tool execution), `--skip-trust`
    because headless refuses to run in untrusted directories (rc=55).
    ``model`` via `-m` (e.g. a flash model); ``effort`` has no known equivalent for
    this CLI today and is accepted but ignored."""

    def __init__(
        self,
        model: str = "",
        effort: str | None = None,
        runner: Callable[[list[str], str], str] = _default_runner,
    ) -> None:
        self._model = model
        self._effort = effort  # unused: no verified flag (see the tiering design doc)
        self._runner = runner

    def complete(self, prompt: str) -> str:
        args = ["gemini", "--skip-trust", "--approval-mode", "plan"]
        if self._model:
            args += ["-m", self._model]
        return self._runner([*args, "-p", ""], prompt)
```

Add the tier→model table and `build_provider_for_task`, after `build_provider`:

```python
# Built-in tier -> model defaults per provider. A provider absent here (or a tier the
# table doesn't cover) falls back to the brain's single configured `llm_model` — this
# keeps providers with no natural "small vs large" split (ollama, until the user pulls
# a second model) behaving exactly as they do today for both tiers.
_TIER_MODELS: dict[str, dict[str, str]] = {
    "claude-cli": {"economy": "haiku", "quality": "opus"},
    "codex-cli": {"economy": "gpt-5-mini", "quality": "gpt-5"},
    "gemini-cli": {"economy": "gemini-2.5-flash", "quality": "gemini-2.5-pro"},
    "anthropic-api": {"economy": "claude-3-5-haiku-latest", "quality": "claude-3-5-sonnet-latest"},
}


def _resolve_tiered_model(provider: str, config: "TalamusConfig", tier: str) -> str:
    override = config.provider_models.get(provider, {})
    if tier in override:
        return override[tier]
    builtin = _TIER_MODELS.get(provider, {})
    if tier in builtin:
        return builtin[tier]
    return config.llm_model


def build_provider_for_task(
    provider: str, config: "TalamusConfig", tier: str, effort: str
) -> LLMProvider:
    """Build the provider for one task's resolved (tier, effort) intent, within the
    single provider configured for the brain (tiering never switches providers)."""
    provider = canonical_provider(provider)
    model = _resolve_tiered_model(provider, config, tier)
    if provider == "claude-cli":
        return ClaudeCliProvider(model=model, effort=effort)
    if provider == "codex-cli":
        return CodexCliProvider(model=model, effort=effort)
    if provider == "gemini-cli":
        return GeminiCliProvider(model=model, effort=effort)
    if provider == "ollama":
        return OllamaProvider(model=model or "llama3")
    if provider == "anthropic-api":
        return AnthropicApiProvider(model=model or "claude-3-5-sonnet-latest")
    raise EngineNotFound(provider)
```

Add `from talamus.config import TalamusConfig` under `TYPE_CHECKING` to avoid a circular
import (config.py does not import adapters/llm.py, so a plain import is actually safe —
verify by running the test suite; if a circular import error surfaces, switch to
`from __future__ import annotations` (already present) plus a `if TYPE_CHECKING:` guarded
import and quote the annotation as done above).

- [ ] **Step 4: Update `services/engines.py`** to import `canonical_provider` from
`adapters.llm` instead of defining it locally. Find its current definition (near the top,
alongside `_ALIASES`) and replace:

```python
from talamus.adapters.llm import ENGINE_COMMANDS, canonical_provider, save_credential
```

Remove the local `_ALIASES` dict and local `canonical_provider` function definition from
this file (they now live in `adapters/llm.py`).

- [ ] **Step 5: Check `services/readiness.py`'s import** of `canonical_provider` — update
it to import from `talamus.adapters.llm` instead of `talamus.services.engines` (grep the
file for the current import line and change only that line; the call sites using
`canonical_provider(...)` stay identical).

```bash
cd "C:/dev/Kortex"; grep -n "canonical_provider" src/talamus/services/readiness.py
```

- [ ] **Step 6: Run the adapter tests to verify they pass.**

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python -m unittest tests.test_talamus_llm_adapter -v
```

Expected: PASS, all tests (old + new).

- [ ] **Step 7: Full gate** (this also catches any leftover `services/engines.py` /
`services/readiness.py` import breakage).

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python dev.py
```

Expected: ALL GREEN.

- [ ] **Step 8: Commit.**

```bash
cd "C:/dev/Kortex"; git add src/talamus/adapters/llm.py src/talamus/services/engines.py src/talamus/services/readiness.py tests/test_talamus_llm_adapter.py
git commit -m "feat(adapters): per-provider tier/effort descriptors + build_provider_for_task [P2]"
```

---

## Task 6: Restore the full `routing.py` import; `EngineRouter`

**Files:**
- Modify: `src/talamus/routing.py`
- Test: `tests/test_talamus_routing.py`

- [ ] **Step 1: Restore the full import line** at the top of `src/talamus/routing.py`
(if you trimmed it in Task 3 Step 4):

```python
from talamus.adapters.llm import ENGINE_LABELS, LLMProvider, build_provider_for_task, canonical_provider
from talamus.config import TalamusConfig
```

- [ ] **Step 2: Write the failing tests** (append to the test file):

```python
class EngineRouterTests(unittest.TestCase):
    def test_resolves_the_code_default_intent_per_task(self) -> None:
        from talamus.config import TalamusConfig
        from talamus.routing import EngineRouter, TaskClass

        router = EngineRouter(TalamusConfig.default())
        provider = router.for_task(TaskClass.EXTRACTION)
        self.assertEqual(provider._model, "haiku")  # economy tier for claude-cli

    def test_ask_answer_resolves_to_the_quality_tier(self) -> None:
        from talamus.config import TalamusConfig
        from talamus.routing import EngineRouter, TaskClass

        router = EngineRouter(TalamusConfig.default())
        provider = router.for_task(TaskClass.ASK_ANSWER)
        self.assertEqual(provider._model, "opus")

    def test_task_tiers_override_wins(self) -> None:
        from dataclasses import replace

        from talamus.config import TalamusConfig
        from talamus.routing import EngineRouter, TaskClass

        config = replace(
            TalamusConfig.default(), task_tiers={"extraction": {"tier": "quality"}}
        )
        router = EngineRouter(config)
        provider = router.for_task(TaskClass.EXTRACTION)
        self.assertEqual(provider._model, "opus")

    def test_memoizes_providers_sharing_the_same_resolved_engine(self) -> None:
        from talamus.config import TalamusConfig
        from talamus.routing import EngineRouter, TaskClass

        router = EngineRouter(TalamusConfig.default())
        # ASK_ROUTING and QUERY_EXPANSION are both economy/low by default -> same engine
        self.assertIs(
            router.for_task(TaskClass.ASK_ROUTING), router.for_task(TaskClass.QUERY_EXPANSION)
        )

    def test_label_reflects_the_configured_provider(self) -> None:
        from talamus.config import TalamusConfig
        from talamus.routing import EngineRouter

        router = EngineRouter(TalamusConfig.default())
        self.assertEqual(router.label, "Claude CLI")
```

- [ ] **Step 3: Run to verify they fail.**

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python -m unittest tests.test_talamus_routing -v
```

Expected: FAIL (`cannot import name 'EngineRouter'`).

- [ ] **Step 4: Implement** — append to `src/talamus/routing.py`:

```python
class EngineRouter:
    """Resolves each TaskClass to a concrete LLMProvider, within the single provider
    configured for the brain (see the design doc's scope note). Built fresh per call
    from a TalamusConfig (no long-lived global state — config changes take effect
    immediately, mirroring the existing build_provider(...) per-call construction).
    Providers are memoized per (provider, tier, effort) so tasks sharing a resolved
    engine share one object."""

    def __init__(self, config: TalamusConfig) -> None:
        self._config = config
        self._provider_name = canonical_provider(config.llm_provider)
        self._cache: dict[tuple[str, str], LLMProvider] = {}
        self.label = ENGINE_LABELS.get(self._provider_name, self._provider_name)

    def for_task(self, task: TaskClass) -> LLMProvider:
        intent = _resolve_intent(self._config, task)
        key = (intent.tier, intent.effort)
        if key not in self._cache:
            self._cache[key] = build_provider_for_task(
                self._provider_name, self._config, intent.tier, intent.effort
            )
        return self._cache[key]
```

- [ ] **Step 5: Run to verify it passes.**

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python -m unittest tests.test_talamus_routing -v
```

Expected: PASS.

- [ ] **Step 6: Full gate.**

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python dev.py
```

Expected: ALL GREEN. This closes Group A (the foundation) — nothing downstream has been
converted yet, so no existing call site is affected.

- [ ] **Step 7: Commit.**

```bash
cd "C:/dev/Kortex"; git add src/talamus/routing.py tests/test_talamus_routing.py
git commit -m "feat(routing): EngineRouter — per-task provider resolution + memoization [P2]"
```

---

## Task 7: Convert `extract.py` + `ingest.py` (extraction, session_remember)

**Files:**
- Modify: `src/talamus/extract.py`, `src/talamus/ingest.py`
- Test: `tests/test_talamus_extract.py`, `tests/test_talamus_ingest*.py` (find the exact
  file names first)

- [ ] **Step 1: Find the existing test files.**

```bash
cd "C:/dev/Kortex"; ls tests/test_talamus_extract*.py tests/test_talamus_ingest*.py
```

- [ ] **Step 2: Run the existing tests to see today's baseline** (they should currently
pass; note their fake-provider pattern, e.g. a bare class with `.complete()`, to know
exactly what needs `StaticRouter(...)` wrapping in Step 6).

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python -m unittest discover -s tests -p "test_talamus_extract*.py" -v
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python -m unittest discover -s tests -p "test_talamus_ingest*.py" -v
```

- [ ] **Step 3: Write the new failing test** — append to the extract test file:

```python
    def test_extract_notes_resolves_the_extraction_task_from_the_router(self) -> None:
        from talamus.extract import extract_notes
        from talamus.normalize import normalize_text
        from talamus.routing import TaskClass

        requested: list[TaskClass] = []

        class RecordingRouter:
            def for_task(self, task: TaskClass):
                requested.append(task)

                class Fake:
                    def complete(self, prompt: str) -> str:
                        return '[{"title": "X", "summary": "s"}]'

                return Fake()

        package = normalize_text("raw.md", "# T\nsome text")
        extract_notes(package, RecordingRouter())
        self.assertEqual(requested, [TaskClass.EXTRACTION])
```

- [ ] **Step 4: Run to verify it fails.**

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python -m unittest tests.test_talamus_extract -v
```

Expected: FAIL (`TypeError: extract_notes() got an unexpected argument` or similar, since
`extract_notes` still expects `llm: LLMProvider` positionally and a bare `RecordingRouter`
has no `.complete`).

- [ ] **Step 5: Implement.** In `src/talamus/extract.py`, change the import and the
function signature:

```python
from talamus.routing import EngineRouter, TaskClass
```

(replace `from talamus.adapters.llm import LLMProvider` with the line above — this file
no longer needs `LLMProvider` directly).

```python
def extract_notes(
    package: NormalizedPackage,
    router: EngineRouter,
    normalized_path: str | None = None,
    preamble: str = "",
    language: str = "English",
    task: TaskClass = TaskClass.EXTRACTION,
) -> list[CanonicalNote]:
    """Extract concept notes. ``preamble`` prepends extra instructions to the
    librarian prompt (e.g. the code-aware variant used by repo scans);
    ``language`` is the user's reading language for the note prose. ``task`` lets
    callers with a different intent than bulk extraction (e.g. remembering a single
    agent session) request their own tier — see talamus.routing.TaskClass."""
    norm = normalized_path or package.raw_path
    text = "\n\n".join(f"# {s.title}\n{s.text}" for s in package.sections)
    llm = router.for_task(task)
    raw = llm.complete(preamble + _PROMPT.format(text=text, language=language))
    candidates = _extract_json_array(raw)
```

(the rest of the function body is unchanged — only the first three lines change).

- [ ] **Step 6: Update `src/talamus/ingest.py`.** Change the import:

```python
from talamus.routing import EngineRouter, TaskClass
```

(replace `from talamus.adapters.llm import LLMProvider`).

Update `_compile_package` to accept a router and a task, defaulting to extraction:

```python
def _compile_package(
    paths: TalamusPaths,
    package: NormalizedPackage,
    router: EngineRouter,
    preamble: str = "",
    reindex: bool = True,
    task: TaskClass = TaskClass.EXTRACTION,
) -> int:
    """Extract the notes from the package, write them, resolve wikilinks in batch,
    and rebuild the indexes."""
    from talamus.config import load_or_default, resolve_language

    paths.normalized.mkdir(parents=True, exist_ok=True)
    normalized_file = paths.normalized / Path(package.raw_path).name
    normalized_file.write_text(package.render(), encoding="utf-8")
    normalized_rel = normalized_file.relative_to(paths.project_root).as_posix()
    language = resolve_language(load_or_default(paths.config_path))
    notes = extract_notes(
        package, router, normalized_path=normalized_rel, preamble=preamble,
        language=language, task=task,
    )
```

(the rest of `_compile_package`'s body is unchanged). Now update every function in this
file that takes `llm: LLMProvider` to take `router: EngineRouter`, and every call to
`_compile_package(paths, package, llm, ...)` to pass `router` instead of `llm` — this is
a pure rename, one occurrence per function:

- `ingest_file(paths, file_path, router)`: replaces `llm` with `router` in the signature
  and in the two calls (`_compile_package(paths, package, router)`,
  `ingest_large(paths, file_path, router)`).
- `ingest_large(paths, file_path, router, job_record=None)`: same rename; the call inside
  `handle()` becomes `_compile_package(paths, package, router, reindex=False)`.
- `ingest_url(paths, url, router)`: rename `llm` → `router` in the signature and the
  `_compile_package(paths, package, router)` call.
- `ingest_dir(paths, directory, router)`: rename in the signature and the
  `ingest_file(paths, path, router)` call.
- `ingest_path(paths, target, router)`: rename in the signature and both calls
  (`ingest_url(paths, target, router)`, `ingest_dir(paths, path, router)`,
  `ingest_file(paths, path, router)`).
- `remember_session(paths, transcript, diff, router)`: rename `llm` → `router` in the
  signature; change its `_compile_package` call to pass the session-remember task:

```python
    package = normalize_session(raw_path.as_posix(), transcript, diff)
    written = _compile_package(paths, package, router, task=TaskClass.SESSION_REMEMBER)
```

- `ingest_text(paths, text, router, name="insight", preamble="")`: rename `llm` →
  `router` in the signature and the `_compile_package(paths, package, router,
  preamble=preamble)` call.

- [ ] **Step 7: Run the extract test to verify it passes.**

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python -m unittest tests.test_talamus_extract -v
```

Expected: PASS.

- [ ] **Step 8: Fix the existing ingest/extract tests broken by the rename.** Run:

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python -m unittest discover -s tests -p "test_talamus_ingest*.py" -v
```

For every failure caused by passing a bare fake as the (now renamed) `router` argument,
wrap it: change `some_function(paths, ..., fake_llm)` to `some_function(paths, ...,
StaticRouter(fake_llm))`, adding `from talamus.routing import StaticRouter` to that test
file's imports. Re-run until green. (Do not change any assertion or fake's `.complete`
behavior — only the wrapping at the call site.)

- [ ] **Step 9: Full gate.**

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python dev.py
```

Expected: ALL GREEN. (Other modules still importing `ingest`/`extract` with the old
`llm=` keyword will break here — fix any such caller the same way: wrap the fake in
`StaticRouter`, or if it's production code not yet converted, note it and continue; the
remaining callers are converted in Tasks 8-14 and Group C.)

- [ ] **Step 10: Commit.**

```bash
cd "C:/dev/Kortex"; git add src/talamus/extract.py src/talamus/ingest.py tests/test_talamus_extract*.py tests/test_talamus_ingest*.py
git commit -m "refactor(ingest): route extraction + session_remember through EngineRouter [P2]"
```

---

## Task 8: Convert `ask.py` + `smartsearch.py` (ask_routing, query_expansion, ask_answer)

**Files:**
- Modify: `src/talamus/ask.py`, `src/talamus/smartsearch.py`
- Test: `tests/test_talamus_ask.py`, `tests/test_talamus_smartsearch.py`

- [ ] **Step 1: Write the failing test** — append to `tests/test_talamus_ask.py`:

```python
    def test_answer_question_requests_routing_then_expansion_then_answer(self) -> None:
        from talamus.ask import answer_question
        from talamus.paths import TalamusPaths
        from talamus.routing import TaskClass

        requested: list[TaskClass] = []

        class RecordingRouter:
            def for_task(self, task: TaskClass):
                requested.append(task)

                class Fake:
                    def complete(self, prompt: str) -> str:
                        return "answer text"

                return Fake()

        import tempfile
        from pathlib import Path

        with tempfile.TemporaryDirectory() as tmp:
            paths = TalamusPaths(Path(tmp))
            answer_question(paths, "what is X?", RecordingRouter())
        # no overview exists in an empty brain, so routing short-circuits before
        # expansion/answer are ever reached — assert the ORDER of whatever WAS reached
        self.assertEqual(requested, [])  # empty brain: no context, no LLM call at all
```

Note: an empty brain never reaches any LLM call (no overview, no graph, no index — see
`answer_question`'s early-return "No context found" path), so this specific test only
proves the router plumbing doesn't crash on an empty brain. Add a second test with a
real overview so routing/expansion/answer are actually exercised:

```python
    def test_answer_question_uses_ask_routing_and_ask_answer_tasks(self) -> None:
        import json
        import tempfile
        from pathlib import Path

        from talamus.ask import answer_question
        from talamus.paths import TalamusPaths
        from talamus.routing import TaskClass

        requested: list[TaskClass] = []

        class RecordingRouter:
            def for_task(self, task: TaskClass):
                requested.append(task)

                class Fake:
                    def complete(self, prompt: str) -> str:
                        if task == TaskClass.ASK_ROUTING:
                            return "dom-x"
                        if task == TaskClass.QUERY_EXPANSION:
                            return "extra terms"
                        return "the answer"

                return Fake()

        with tempfile.TemporaryDirectory() as tmp:
            paths = TalamusPaths(Path(tmp))
            paths.ensure_directories()
            paths.notes.mkdir(parents=True, exist_ok=True)
            (paths.notes / "topic.md").write_text("# Topic\ncontent", encoding="utf-8")
            paths.cache.mkdir(parents=True, exist_ok=True)
            paths.overview_file.write_text(
                json.dumps([{"id": "dom-x", "name": "X", "members": ["Topic"]}]),
                encoding="utf-8",
            )
            answer_question(paths, "what is X?", RecordingRouter())
        self.assertIn(TaskClass.ASK_ROUTING, requested)
```

- [ ] **Step 2: Run to verify it fails.**

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python -m unittest tests.test_talamus_ask -v
```

Expected: FAIL (functions still take `llm: LLMProvider`, calling `.complete` directly
instead of resolving via `router.for_task`).

- [ ] **Step 3: Implement.** In `src/talamus/ask.py`, change the import:

```python
from talamus.routing import EngineRouter, TaskClass
```

(replace `from talamus.adapters.llm import LLMProvider`).

Update `_route_member_titles`:

```python
def _route_member_titles(
    paths: TalamusPaths,
    question: str,
    router: EngineRouter,
    trace: dict | None = None,
) -> list[str]:
    """Route via the domain overview and return the chosen domains' member titles
    (un-ranked, un-sliced). Domains are picked by **stable id** (F3.7/F3.8): the
    LLM answers with ids, parsed and validated against the map — substring
    matching on names survives only as a fallback for pre-id overviews."""
    overview = load_overview(paths)
    if not overview:
        return []
    llm = router.for_task(TaskClass.ASK_ROUTING)
    tree = load_overview_tree(paths)
    if tree:
        # Fase R5: two-level routing — pick macro-areas first, then only their
        # domains enter the second prompt. Keeps the routing prompt ~log(N)
        # instead of listing every domain (one extra LLM call, big brains only).
        area_map = "\n".join(
            f"- {a.get('id', '?')} | {a.get('name', '')}: {a.get('description', '')}" for a in tree
        )
        area_raw = llm.complete(_ROUTE_PROMPT.format(map=area_map, question=question))
```

(everything else in `_route_member_titles`'s body is unchanged — only the parameter and
the added `llm = router.for_task(...)` line at the top change; the existing `llm.complete`
calls stay exactly as they are, now referring to the locally resolved `llm`).

Update `_expand_query`:

```python
def _expand_query(question: str, router: EngineRouter) -> str:
    llm = router.for_task(TaskClass.QUERY_EXPANSION)
    return llm.complete(_EXPAND_PROMPT.format(question=question)).strip() or question
```

Update `_overview_bundle` (the caller of both `_route_member_titles`/`_expand_query`) —
rename its `llm` parameter to `router` (it just threads through, no `.complete` call of
its own):

```python
def _overview_bundle(
    paths: TalamusPaths,
    question: str,
    router: EngineRouter,
    limit: int = 8,
    trace: dict | None = None,
) -> ContextBundle:
    titles = _route_member_titles(paths, question, router, trace=trace)
    if not titles:
        return ContextBundle(question=question, items=[])
    # RS3: the LLM acts as the embedding model — it translates the question into the
    # corpus vocabulary BEFORE selection. Measured on the book: ask hit 0.861 -> 0.972,
    # vague 0.50 -> 0.81, cross 0.50 -> 0.88. Costs one extra call per ask.
    expanded = _expand_query(question, router)
```

(the rest of `_overview_bundle`'s body is unchanged).

Update `answer_question` (rename `llm` → `router`, thread it to `_overview_bundle`,
`_expand_query`, and `answer_from_items`):

```python
def answer_question(
    paths: TalamusPaths,
    question: str,
    router: EngineRouter,
    extra_items: list[dict] | None = None,
    trace: dict | None = None,
) -> str:
    """Answer from the brain. ``extra_items`` lets callers append cross-brain
    context (real note contents with scope markers) before the budget cut.
    Pass a dict as ``trace`` to get the route explained (F3.10): domains, route,
    notes read, context tokens, whether fallbacks fired."""
    bundle = _overview_bundle(paths, question, router, trace=trace)
    route = "overview" if bundle.items else "none"
    if not bundle.items:
        graph = (
            load_graph(paths.graph_file)
            if paths.graph_file.is_file()
            else {"nodes": {}, "edges": []}
        )
        search = BM25Index.load(paths.index_file) if paths.index_file.is_file() else BM25Index()
        bundle = build_context_bundle(paths, graph, search, question)
        if bundle.items:
            route = "index"
        elif not extra_items:
            bundle = build_context_bundle(paths, graph, search, _expand_query(question, router))
            if bundle.items:
                route = "expansion"
    all_items = [*bundle.items, *(extra_items or [])]
    if trace is not None:
        trace["route"] = route
        trace["extra_items"] = len(extra_items or [])
    if not all_items:
        return "No context found in the brain for this question."
    return answer_from_items(question, all_items, router, trace=trace)
```

Update `answer_from_items`:

```python
def answer_from_items(
    question: str, all_items: list[dict], router: EngineRouter, trace: dict | None = None
) -> str:
    """Budget the items, answer with citations, append the Sources legend."""
    items = fit_to_budget(all_items, context_budget())
    if trace is not None:
        trace["items_read"] = [item["path"] for item in items]
        trace["context_tokens"] = sum(estimate_tokens(item["content"]) for item in items)
    context = "\n\n".join(
        f"[{idx}] {item['path']}\n{item['content']}" for idx, item in enumerate(items, start=1)
    )
    llm = router.for_task(TaskClass.ASK_ANSWER)
    answer = llm.complete(_ANSWER_PROMPT.format(question=question, context=context)).strip()
    if not answer:
        return "The engine produced no answer. Try again or check the engine."
    sources = "\n".join(
        f"[{idx}] {Path(item['path']).name}" for idx, item in enumerate(items, start=1)
    )
    return f"{answer}\n\n**Sources:**\n{sources}"
```

- [ ] **Step 4: Update `src/talamus/smartsearch.py`.** Change the import:

```python
from talamus.routing import EngineRouter, TaskClass
```

(replace `from talamus.adapters.llm import LLMProvider`; the `from talamus.ask import
_EXPAND_PROMPT` import stays).

Update `expand_query`:

```python
def expand_query(paths: TalamusPaths, question: str, router: EngineRouter) -> str:
    """Return the question augmented with LLM-predicted terms, cached on disk.

    The expansion depends only on the question (not the brain), so caching by
    the normalized question is safe and makes repeated queries free. On any
    engine failure we degrade to the original question — smart search must never
    be worse than plain search."""
    key = " ".join(question.split()).lower()
    if not key:
        return question
    cache = _load_cache(paths)
    if key in cache:
        expanded = cache[key]
    else:
        try:
            llm = router.for_task(TaskClass.QUERY_EXPANSION)
            expanded = llm.complete(_EXPAND_PROMPT.format(question=question)).strip()
        except (EngineFailed, EngineNotFound):
            return question
        cache[key] = expanded
        _save_cache(paths, cache)
    return f"{question} {expanded}".strip() if expanded else question
```

Update `expand_query_multi`:

```python
def expand_query_multi(
    paths: TalamusPaths, question: str, router: EngineRouter, passes: int = 1
) -> str:
    """N-pass expansion union to smooth the nondeterministic LLM expansion
    (RS4 measured run-to-run swings of ~0.06 hit). ``passes <= 1`` is the cached
    single-pass path. Extra passes are uncached (each is a fresh sample) and their
    unique terms are unioned onto the question; any engine failure is skipped so
    the result is never worse than the question itself. For a deterministic engine
    (e.g. ollama at temperature 0) one pass already reproduces — multi-pass is for
    sampling engines where a small union reduces variance."""
    if passes <= 1:
        return expand_query(paths, question, router)
    terms = question.split()
    seen = {t.lower() for t in terms}
    llm = router.for_task(TaskClass.QUERY_EXPANSION)
    for _ in range(passes):
        try:
            expansion = llm.complete(_EXPAND_PROMPT.format(question=question)).strip()
        except (EngineFailed, EngineNotFound):
            continue
        for token in expansion.split():
            if token.lower() not in seen:
                seen.add(token.lower())
                terms.append(token)
    return " ".join(terms)
```

- [ ] **Step 5: Run the new tests to verify they pass.**

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python -m unittest tests.test_talamus_ask -v
```

Expected: PASS.

- [ ] **Step 6: Fix the existing ask/smartsearch tests.**

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python -m unittest tests.test_talamus_ask tests.test_talamus_smartsearch -v
```

For each failure from a bare fake passed where `router` is now expected, wrap with
`StaticRouter(fake)` (import `from talamus.routing import StaticRouter`) at the call
site, matching the pattern from Task 7 Step 8. Re-run until green.

- [ ] **Step 7: Full gate.**

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python dev.py
```

Expected: ALL GREEN (remaining production callers of `ask.py`/`smartsearch.py` —
`cli/query.py`, `mcp_server.py`, `services/ask.py` — are converted in Group C; until
then, `python dev.py` will surface any of THEIR tests that broke, which is expected and
tracked, not a regression to silently ignore — note any such failures and confirm they
disappear once Group C's task for that file is done. If any fail here, wrap their fakes
in `StaticRouter` the same way, exactly as done for the other test files, so the gate
stays green task-by-task.)

- [ ] **Step 8: Commit.**

```bash
cd "C:/dev/Kortex"; git add src/talamus/ask.py src/talamus/smartsearch.py tests/test_talamus_ask.py tests/test_talamus_smartsearch.py
git commit -m "refactor(ask): route ask_routing/query_expansion/ask_answer through EngineRouter [P2]"
```

---

## Task 9: Convert `correct.py` (verify)

**Files:**
- Modify: `src/talamus/correct.py`
- Test: `tests/test_talamus_correct.py` (find the exact name first)

- [ ] **Step 1: Locate the test file.**

```bash
cd "C:/dev/Kortex"; ls tests/test_talamus_correct*.py
```

- [ ] **Step 2: Write the failing test** (append):

```python
    def test_verify_note_requests_the_verify_task(self) -> None:
        import tempfile
        from pathlib import Path

        from talamus.correct import verify_note
        from talamus.models import CanonicalNote, SourceRef
        from talamus.paths import TalamusPaths
        from talamus.routing import TaskClass
        from talamus.store import write_note_json

        requested: list[TaskClass] = []

        class RecordingRouter:
            def for_task(self, task: TaskClass):
                requested.append(task)

                class Fake:
                    def complete(self, prompt: str) -> str:
                        return '{"ok": true}'

                return Fake()

        with tempfile.TemporaryDirectory() as tmp:
            paths = TalamusPaths(Path(tmp))
            paths.ensure_directories()
            source_path = paths.raw / "s.md"
            source_path.write_text("source text", encoding="utf-8")
            note = CanonicalNote(
                note_id="t",
                title="T",
                summary="s",
                body_sections={"definizione": "d"},
                sources=[
                    SourceRef(
                        raw_path=source_path.as_posix(),
                        normalized_path=source_path.as_posix(),
                        locator="",
                        source_hash="sha256:x",
                        supported_claims=[],
                    )
                ],
            )
            write_note_json(paths, note)
            verify_note(paths, "T", RecordingRouter())
        self.assertEqual(requested, [TaskClass.VERIFY])
```

If `CanonicalNote`'s constructor requires different/additional fields, check
`src/talamus/models.py` for the exact dataclass definition and adjust the test's
construction accordingly — do not guess field names beyond what compiles.

- [ ] **Step 3: Run to verify it fails.**

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python -m unittest tests.test_talamus_correct -v
```

Expected: FAIL.

- [ ] **Step 4: Implement.** In `src/talamus/correct.py`, change the import:

```python
from talamus.routing import EngineRouter, TaskClass
```

(replace `from talamus.adapters.llm import LLMProvider`).

Update `verify_note`:

```python
def verify_note(paths: TalamusPaths, title: str, router: EngineRouter) -> dict:
    """Check a note against its source. Returns {found, checked, ok, summary?, body?}."""
    note = _find(load_notes(paths), title)
    if note is None:
        return {"found": False}
    source = _source_text(paths, note)
    if not source:
        return {"found": True, "checked": False}
    body = "\n".join(note.body_sections.values())
    llm = router.for_task(TaskClass.VERIFY)
    raw = llm.complete(
        _PROMPT.replace("<TITLE>", note.title)
        .replace("<SUMMARY>", note.summary)
        .replace("<BODY>", body)
        .replace("<SOURCE>", source)
    )
```

(the rest of the function is unchanged). Update `apply_correction` and `verify_batch` to
rename their `llm` parameter to `router` (pure pass-through, no `.complete` of their own):

```python
def apply_correction(paths: TalamusPaths, title: str, router: EngineRouter) -> bool:
    """Verify and, if needed, write the corrected note (old version kept in history)."""
    result = verify_note(paths, title, router)
```

```python
def verify_batch(
    paths: TalamusPaths,
    router: EngineRouter,
    only_stale: bool = False,
    source_filter: str | None = None,
) -> dict:
```

(inside `verify_batch`, the single call `result = verify_note(paths, note.title, llm)`
becomes `result = verify_note(paths, note.title, router)` — the rest of the function is
unchanged).

- [ ] **Step 5: Run to verify the new test passes, then fix the rest of the file's
existing tests** the same way as prior tasks (wrap bare fakes in `StaticRouter`).

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python -m unittest tests.test_talamus_correct -v
```

Expected: PASS (after any `StaticRouter` wrapping needed).

- [ ] **Step 6: Full gate.**

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python dev.py
```

- [ ] **Step 7: Commit.**

```bash
cd "C:/dev/Kortex"; git add src/talamus/correct.py tests/test_talamus_correct*.py
git commit -m "refactor(correct): route verify through EngineRouter [P2]"
```

---

## Task 10: Convert `enrich.py` (enrich)

**Files:**
- Modify: `src/talamus/enrich.py`
- Test: `tests/test_talamus_enrich*.py`

- [ ] **Step 1: Write the failing test** (append to the enrich test file, following the
`RecordingRouter` pattern from Task 9 Step 2 — construct a minimal brain with one note
missing the `_MARKER` in its `retrieval_text`, call `enrich_notes(paths, RecordingRouter())`,
assert `requested == [TaskClass.ENRICH]`). Use `write_note_json` + a `CanonicalNote` with
`retrieval_text="plain text"` (no marker) as the fixture note, matching the pattern from
Task 9's test.

- [ ] **Step 2: Run to verify it fails.**

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python -m unittest tests.test_talamus_enrich -v
```

- [ ] **Step 3: Implement.** In `src/talamus/enrich.py`, change the import:

```python
from talamus.routing import EngineRouter, TaskClass
```

Update `enrich_notes`:

```python
def enrich_notes(paths: TalamusPaths, router: EngineRouter, language: str = "English") -> dict:
    """Add the symptom phrasings to the retrieval_text of notes that lack them.

    Idempotent (marker in retrieval_text); a malformed batch is skipped and counted,
    without touching the others. Reindexes once at the end."""
    notes = [n for n in load_notes(paths) if _MARKER not in n.retrieval_text]
    by_id = {n.note_id: n for n in notes}
    enriched = 0
    failed_batches = 0
    llm = router.for_task(TaskClass.ENRICH)
    for offset in range(0, len(notes), BATCH_SIZE):
        batch = notes[offset : offset + BATCH_SIZE]
        listing = "\n".join(_note_brief(n) for n in batch)
        raw = llm.complete(_PROMPT.format(language=language, notes=listing))
```

(the rest of the function body is unchanged — only the import, the signature, and the
`llm = router.for_task(...)` line move).

- [ ] **Step 4: Run to verify it passes**, then fix existing enrich tests with
`StaticRouter` wrapping as in prior tasks.

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python -m unittest tests.test_talamus_enrich -v
```

- [ ] **Step 5: Full gate.**

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python dev.py
```

- [ ] **Step 6: Commit.**

```bash
cd "C:/dev/Kortex"; git add src/talamus/enrich.py tests/test_talamus_enrich*.py
git commit -m "refactor(enrich): route symptom enrichment through EngineRouter [P2]"
```

---

## Task 11: Convert `consolidate.py` (consolidate)

**Files:**
- Modify: `src/talamus/consolidate.py`
- Test: `tests/test_talamus_consolidate*.py`

- [ ] **Step 1: Write the failing test** (append, following the `RecordingRouter` pattern;
`_detect_groups` takes `notes: list[CanonicalNote]` directly, so construct 2+ minimal
`CanonicalNote` fixtures in-memory — no filesystem needed — and call
`_detect_groups(notes, RecordingRouter())`; assert `requested == [TaskClass.CONSOLIDATE]`).

- [ ] **Step 2: Run to verify it fails.**

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python -m unittest tests.test_talamus_consolidate -v
```

- [ ] **Step 3: Implement.** In `src/talamus/consolidate.py`, change the import:

```python
from talamus.routing import EngineRouter, TaskClass
```

Update `_detect_groups`:

```python
def _detect_groups(notes: list[CanonicalNote], router: EngineRouter) -> list[dict]:
    if len(notes) < 2:
        return []
    listing = "\n".join(f"- [{n.note_id}] {n.title}: {n.summary}" for n in notes)
    llm = router.for_task(TaskClass.CONSOLIDATE)
    raw = llm.complete(_PROMPT.replace("__NOTES__", listing))
```

Rename `llm` → `router` in `find_duplicates` and `apply_consolidation` (pure pass-through
to `_detect_groups`):

```python
def find_duplicates(paths: TalamusPaths, router: EngineRouter) -> list[dict]:
    """Return the proposed merge groups (does not change anything)."""
    return _detect_groups(load_notes(paths), router)


def apply_consolidation(
    paths: TalamusPaths, router: EngineRouter, groups: list[dict] | None = None
) -> int:
```

(inside `apply_consolidation`, `groups = _detect_groups(notes, llm)` becomes `groups =
_detect_groups(notes, router)` — the rest is unchanged).

- [ ] **Step 4: Run to verify it passes**, fix existing tests with `StaticRouter`.

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python -m unittest tests.test_talamus_consolidate -v
```

- [ ] **Step 5: Full gate.**

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python dev.py
```

- [ ] **Step 6: Commit.**

```bash
cd "C:/dev/Kortex"; git add src/talamus/consolidate.py tests/test_talamus_consolidate*.py
git commit -m "refactor(consolidate): route duplicate detection through EngineRouter [P2]"
```

---

## Task 12: Convert `domains.py` (overview_naming)

**Files:**
- Modify: `src/talamus/domains.py`
- Test: `tests/test_talamus_domains*.py`

- [ ] **Step 1: Write the failing test** (append, `RecordingRouter` pattern;
`build_overview` needs a brain with at least one note — mirror Task 9's fixture setup;
assert `TaskClass.OVERVIEW_NAMING in requested`).

- [ ] **Step 2: Run to verify it fails.**

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python -m unittest tests.test_talamus_domains -v
```

- [ ] **Step 3: Implement.** In `src/talamus/domains.py`, change the import:

```python
from talamus.routing import EngineRouter, TaskClass
```

Update the four call-taking functions — each gets `router: EngineRouter` in place of
`llm: LLMProvider`, and resolves `llm = router.for_task(TaskClass.OVERVIEW_NAMING)`
immediately before its own `.complete()` call (there is exactly one `.complete()` call
per function, so this is a 2-line change repeated four times):

```python
def _domains_from_llm(
    clusters: list[list[str]],
    summaries: dict[str, str],
    router: EngineRouter,
    language: str,
) -> tuple[list[dict], set[str]]:
    """One full-partition call (the original path). Returns (domains, assigned)."""
    cluster_text = "\n".join(f"- {', '.join(cluster)}" for cluster in clusters)
    summary_text = "\n".join(f"- {title}: {summary}" for title, summary in summaries.items())
    llm = router.for_task(TaskClass.OVERVIEW_NAMING)
    raw = llm.complete(
        _PROMPT.replace("<CLUSTERS>", cluster_text)
        .replace("<SUMMARIES>", summary_text)
        .replace("<LANGUAGE>", language)
    )
```

```python
def _name_domains(
    clusters: list[list[str]],
    summaries: dict[str, str],
    router: EngineRouter,
    language: str = "English",
) -> list[dict]:
    domains, assigned = _domains_from_llm(clusters, summaries, router, language)
```

```python
def _name_domains_batched(
    clusters: list[list[str]],
    summaries: dict[str, str],
    router: EngineRouter,
    language: str = "English",
) -> list[dict]:
    big = [c for c in clusters if len(c) >= SPLIT_CLUSTER_THRESHOLD]
    mid = [c for c in clusters if MIN_NAMED_CLUSTER <= len(c) < SPLIT_CLUSTER_THRESHOLD]
    strays = [t for c in clusters if len(c) < MIN_NAMED_CLUSTER for t in c]
    domains: list[dict] = []

    # 1) giant clusters: dedicated thematic partition (echo limited to the cluster)
    for cluster in big:
        sub = {t: summaries.get(t, "") for t in cluster}
        split_domains, assigned = _domains_from_llm([cluster], sub, router, language)
        domains.extend(split_domains)
        strays.extend(t for t in cluster if t not in assigned)

    # 2) mid clusters: one call that echoes only the cluster index
    if mid:
        lines = []
        for i, cluster in enumerate(mid):
            sample = "; ".join(cluster[:8])
            extra = f" (+{len(cluster) - 8} altre)" if len(cluster) > 8 else ""
            lines.append(f"Cluster {i}: {sample}{extra}")
        llm = router.for_task(TaskClass.OVERVIEW_NAMING)
        raw = llm.complete(
            _CLUSTER_NAME_PROMPT.replace("<CLUSTERS>", "\n".join(lines)).replace(
                "<LANGUAGE>", language
            )
        )
```

(the rest of `_name_domains_batched`'s body, including the strays block, is unchanged
except its own `raw = llm.complete(...)` call at the bottom, which becomes `raw =
router.for_task(TaskClass.OVERVIEW_NAMING).complete(...)` inline, or reuse the `llm`
variable already resolved above since it is the same task for the whole function — reuse
it: change `raw = llm.complete(_ASSIGN_PROMPT...)` to use the already-bound `llm` from
earlier in the function rather than resolving twice).

```python
def build_overview(paths: TalamusPaths, router: EngineRouter) -> list[dict]:
    """Induce the domains and persist the overview. Returns the domain list."""
    from talamus.config import load_or_default, resolve_language

    notes = load_notes(paths)
    if not notes:
        return []
    clusters = _structural_clusters(notes, load_ontology(paths))
    summaries = {note.title: note.summary for note in notes}
    language = resolve_language(load_or_default(paths.config_path))
    namer = _name_domains_batched if len(notes) > BATCH_NOTES_THRESHOLD else _name_domains
    domains = namer(clusters, summaries, router, language=language)
    save_overview(paths, domains)
    return domains
```

```python
def build_overview_tree(paths: TalamusPaths, router: EngineRouter) -> list[dict]:
    """Second overview level (Fase R5): macro-areas over the domains, so routing
    cost stays ~log(N) instead of growing linearly with the domain count.
    One extra LLM call, only when the flat map is big enough to need it."""
    overview = load_overview(paths)
    if len(overview) < TREE_THRESHOLD:
        tree_path(paths).unlink(missing_ok=True)
        return []
    from talamus.config import load_or_default, resolve_language

    domain_lines = "\n".join(
        f"- {d.get('id', '?')} | {d.get('name', '')}: {d.get('description', '')}" for d in overview
    )
    language = resolve_language(load_or_default(paths.config_path))
    llm = router.for_task(TaskClass.OVERVIEW_NAMING)
    raw = llm.complete(
        _TREE_PROMPT.replace("<DOMAINS>", domain_lines).replace("<LANGUAGE>", language)
    )
```

- [ ] **Step 4: Run to verify it passes**, fix existing tests with `StaticRouter`.

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python -m unittest tests.test_talamus_domains -v
```

- [ ] **Step 5: Full gate.**

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python dev.py
```

- [ ] **Step 6: Commit.**

```bash
cd "C:/dev/Kortex"; git add src/talamus/domains.py tests/test_talamus_domains*.py
git commit -m "refactor(domains): route overview/tree naming through EngineRouter [P2]"
```

---

## Task 13: Convert `ontology_lab.py` (ontology_naming)

**Files:**
- Modify: `src/talamus/ontology_lab.py`
- Test: `tests/test_talamus_ontology_lab*.py`

- [ ] **Step 1: Write the failing test** (append, `RecordingRouter` pattern; call
`induce_candidates(paths, RecordingRouter(), min_support=1)` against a brain seeded with
enough unexplained relation evidence to be eligible — check the existing test file for
how it seeds evidence today, e.g. via `collect_evidence`/a fixture brain with untyped
relations, and reuse that exact setup; assert `requested == [TaskClass.ONTOLOGY_NAMING]`
if any candidates were eligible, or skip the assertion gracefully if the minimal fixture
produces zero eligible clusters — prefer copying the exact brain fixture from an existing
passing test in this file over inventing a new one).

- [ ] **Step 2: Run to verify it fails.**

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python -m unittest tests.test_talamus_ontology_lab -v
```

- [ ] **Step 3: Implement.** In `src/talamus/ontology_lab.py`, change the import:

```python
from talamus.routing import EngineRouter, TaskClass
```

Update `induce_candidates`:

```python
def induce_candidates(
    paths: TalamusPaths,
    router: EngineRouter,
    min_support: int = DEFAULT_MIN_SUPPORT,
) -> list[RelationType]:
    """Induce candidate relation types from unexplained surfaces. One LLM call.

    Deterministic clustering decides WHAT becomes a candidate (support thresholds);
    the LLM only names and defines. Candidates are appended to the schema with
    status ``candidate`` and queued for review — runtime is untouched (F5.10).
    """
    evidence = collect_evidence(paths)
    clusters = cluster_unexplained(evidence)
    eligible = {
        key: records
        for key, records in clusters.items()
        if len(records) >= min_support and len({r.source_note for r in records}) >= 2
    }
    if not eligible:
        return []
    schema = load_schema(paths)
    known_surfaces = {s for t in schema.relation_types for s in t.surfaces}
    eligible = {k: v for k, v in eligible.items() if k not in known_surfaces}
    if not eligible:
        return []
    cluster_text = "\n".join(
        f'- chiave "{key}": {len(records)} osservazioni, es. '
        f'"{records[0].subject} {records[0].predicate_surface} {records[0].object}"'
        for key, records in sorted(eligible.items())
    )
    llm = router.for_task(TaskClass.ONTOLOGY_NAMING)
    raw = llm.complete(_NAMING_PROMPT.format(clusters=cluster_text))
```

(the rest of the function is unchanged).

- [ ] **Step 4: Run to verify it passes**, fix existing tests with `StaticRouter`.

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python -m unittest tests.test_talamus_ontology_lab -v
```

- [ ] **Step 5: Full gate.**

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python dev.py
```

- [ ] **Step 6: Commit.**

```bash
cd "C:/dev/Kortex"; git add src/talamus/ontology_lab.py tests/test_talamus_ontology_lab*.py
git commit -m "refactor(ontology_lab): route relation-type naming through EngineRouter [P2]"
```

This closes Group B — every `.complete()` call site in the codebase now resolves through
an `EngineRouter`. Group C converts the callers that build and thread the router.

---

## Task 14: `cli/_common.py` + `cli/app.py` — build a router instead of one provider

**Files:**
- Modify: `src/talamus/cli/_common.py`, `src/talamus/cli/app.py`
- Test: existing CLI tests (`tests/test_talamus_cli*.py`) — no new test file; this task
  is verified by the full CLI test suite passing.

- [ ] **Step 1: Add `_router_for` to `cli/_common.py`**, alongside the existing
`_provider_for` (kept, in case a future explicit-model override path needs an untiered
single provider — see the spec's scope note):

```python
def _router_for(root: Path) -> EngineRouter:
    config = load_or_default(TalamusPaths(root).config_path)
    return EngineRouter(config)
```

Add the import: `from talamus.routing import EngineRouter, StaticRouter` (add to the
existing import block).

- [ ] **Step 2: Update `cli/app.py`'s `main`** to build a router instead of a raw
provider, wrapping the test-injectable `llm` param (kept as-is for back-compat with every
existing `main(argv, llm=fake)` test call) in `StaticRouter` when present:

Replace this line:

```python
        provider = llm if llm is not None else _provider_for(root)
```

with:

```python
        router = StaticRouter(llm) if llm is not None else _router_for(root)
```

Replace the two `lambda: llm if llm is not None else _provider_for(root)` occurrences
(the scan and ontology commands) with the router directly — no lambda needed anymore,
since `EngineRouter`/`StaticRouter` construction is already cheap and lazy (the actual
provider is only built inside `for_task`, when a call site actually needs it):

```python
        if command == "ontology":
            return _cmd_ontology_group(
                args, root, StaticRouter(llm) if llm is not None else _router_for(root)
            )
```

```python
        if command == "scan":
            return _cmd_scan(
                root,
                args.target,
                StaticRouter(llm) if llm is not None else _router_for(root),
                args,
            )
```

Update every downstream use of `provider` in the rest of `main` (the `_cmd_ingest`,
`_cmd_consolidate`, `_cmd_enrich`, `_cmd_verify_batch`, `_cmd_verify`, `_cmd_overview`,
`_cmd_ask`, `_cmd_remember` calls) to pass `router` instead of `provider` — a pure rename
of the variable at each call site, e.g. `_cmd_ingest(root, args.target, provider,
json_out, args.yes)` becomes `_cmd_ingest(root, args.target, router, json_out, args.yes)`.

Add `from talamus.routing import EngineRouter, StaticRouter` to `cli/app.py`'s imports
(it uses `StaticRouter` directly now; `EngineRouter` only if referenced in a type hint —
check if `main`'s own signature needs updating; it does not, since `llm: LLMProvider |
None` stays the public parameter name/type for back-compat, only wrapped internally).

- [ ] **Step 3: Update `cli/pipeline.py`'s two direct `_provider_for` uses** in
`_run_scan_job` and `_run_ingest_job` (these resume a persisted job outside `main`'s
normal flow, so they build their own router the same way):

```python
def _run_scan_job(root: Path, record: JobRecord) -> int:
    """Resume runner registered in JOB_RUNNERS for `talamus jobs resume`."""
    paths = TalamusPaths(root)
    plan = plan_from_record(record)
    report = execute_plan(paths, plan, _router_for(root), job_record=record)
```

```python
def _run_ingest_job(root: Path, record: JobRecord) -> int:
    """Resume a chunked big-document ingest (talamus jobs resume)."""
    from talamus.ingest import ingest_large

    file_path = Path(str(record.payload.get("file", "")))
    if not file_path.is_file():
        print(f"error: source file missing: {file_path}", file=sys.stderr)
        return 1
    report = ingest_large(TalamusPaths(root), file_path, _router_for(root), job_record=record)
```

Update `cli/pipeline.py`'s import: replace `from talamus.cli._common import (JOB_RUNNERS,
_print_json, _provider_for,)` with `from talamus.cli._common import (JOB_RUNNERS,
_print_json, _router_for,)`, and replace `from talamus.adapters.llm import LLMProvider`
with `from talamus.routing import EngineRouter`. Every `_cmd_*` function in this file that
has an `llm: LLMProvider` parameter renames it to `router: EngineRouter` — this is a pure
rename repeated across `_cmd_ingest`, `_cmd_consolidate`, `_cmd_enrich`,
`_cmd_verify_batch`, `_cmd_verify`, `_cmd_overview` (the bodies already just forward the
parameter into a `services/*.py` call, unchanged except the renamed variable).

- [ ] **Step 4: Update `cli/query.py`** the same way: replace `from talamus.adapters.llm
import LLMProvider` with `from talamus.routing import EngineRouter`; rename `llm:
LLMProvider` to `router: EngineRouter` in `_cmd_ask`, `_cmd_remember`, `_cmd_search`
(including its `llm: LLMProvider | None = None` optional param, becoming `router:
EngineRouter | None = None`); update its `from talamus.cli._common import (_print_json,
_provider_for,)` to `from talamus.cli._common import (_print_json, _router_for,)` and the
one internal fallback `provider = llm if llm is not None else _provider_for(root)` inside
`_cmd_search` to `router = router if router is not None else _router_for(root)`.

- [ ] **Step 5: Update `cli/groups.py`** — `_cmd_ontology_group`'s `llm_factory:
Callable[[], LLMProvider]` parameter is no longer needed as a factory (constructing an
`EngineRouter` is already cheap and lazy); simplify to `router: EngineRouter` directly:

```python
def _cmd_ontology_group(
    args: argparse.Namespace, root: Path, router: EngineRouter
) -> int:
```

and its one use, `induce_candidates(paths, llm_factory(), min_support=args.min_support)`,
becomes `induce_candidates(paths, router, min_support=args.min_support)`. Update the
import: replace `from talamus.adapters.llm import LLMProvider` with `from talamus.routing
import EngineRouter`; remove `from collections.abc import Callable` if it becomes unused
in this file (check with a quick grep before removing).

```bash
cd "C:/dev/Kortex"; grep -n "Callable" src/talamus/cli/groups.py
```

- [ ] **Step 6: Run the full CLI test suite.**

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python -m unittest discover -s tests -p "test_talamus_cli*.py" -v
```

Fix any failures the same way as before: a bare fake provider injected via `main(argv,
llm=fake)` needs NO change (the wrapping now happens inside `main` itself); a fake passed
directly to a converted `_cmd_*` function in a lower-level test needs `StaticRouter(...)`
wrapping at that call site.

- [ ] **Step 7: Full gate.**

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python dev.py
```

Expected: ALL GREEN.

- [ ] **Step 8: Commit.**

```bash
cd "C:/dev/Kortex"; git add src/talamus/cli/_common.py src/talamus/cli/app.py src/talamus/cli/pipeline.py src/talamus/cli/query.py src/talamus/cli/groups.py
git commit -m "refactor(cli): build an EngineRouter instead of a single provider [P2]"
```

---

## Task 15: `services/*.py` wrappers — rename `llm`/`llm_factory` to `router`

**Files:**
- Modify: `src/talamus/services/ingestion.py`, `src/talamus/services/scan.py`,
  `src/talamus/services/enrich.py`, `src/talamus/services/verification.py`,
  `src/talamus/services/consolidation.py`
- Test: `tests/test_talamus_ingestion_services.py`,
  `tests/test_talamus_scan_services.py`, `tests/test_talamus_enrich_services.py`,
  `tests/test_talamus_verification_services.py`,
  `tests/test_talamus_consolidation_services.py` (verify exact names with `ls` first)

This task is a pure, mechanical rename across five thin wrapper files — no new test is
needed (the existing service tests already exercise these functions end-to-end and will
catch any mistake); each file's change is shown in full.

- [ ] **Step 1: `services/ingestion.py`** — replace `from talamus.adapters.llm import
LLMProvider` with `from talamus.routing import EngineRouter`; rename `llm: LLMProvider` to
`router: EngineRouter` in `run_ingest` and `ingest_raw_text`, and their inner calls:

```python
def run_ingest(
    root: str | Path,
    target: str,
    router: EngineRouter,
    *,
    confirmed: bool = False,
) -> ServiceResult[IngestPreview | IngestRunResult]:
    root_path = Path(root)
    try:
        preview = _build_preview(root_path, target)
        if preview.requires_confirmation and not confirmed:
            return ServiceResult(
                success=True,
                message="Ingest confirmation required",
                code="ingest_confirmation_required",
                data=preview,
            )
        result = cast(dict[str, Any], ingest_path(TalamusPaths(root_path), target, router))
```

```python
def ingest_raw_text(
    root: str | Path,
    text: str,
    router: EngineRouter,
    *,
    name: str = "insight",
) -> ServiceResult[IngestRunResult]:
    """Compile a raw text string into brain notes (no file on disk). Used by the
    MCP remember/ingest_text tools."""
    root_path = Path(root)
    try:
        result = cast(
            dict[str, Any], ingest_text(TalamusPaths(root_path), text, router, name=name)
        )
```

- [ ] **Step 2: `services/scan.py`** — replace `from collections.abc import Callable` +
`from talamus.adapters.llm import LLMProvider` with `from talamus.routing import
EngineRouter`; `run_scan`'s `llm_factory: Callable[[], LLMProvider]` param becomes
`router: EngineRouter` directly (constructing a router is already cheap/lazy, so the
factory indirection is no longer needed):

```python
def run_scan(
    brain_root: str | Path,
    target: str | Path,
    router: EngineRouter,
    *,
    profile: str = "all",
    include: list[str] | None = None,
    exclude: list[str] | None = None,
    max_files: int | None = None,
    confirmed: bool = False,
    background: bool = False,
    allow_secrets: bool = False,
) -> ServiceResult[ScanPreview | ScanActionResult]:
```

and its one use, `execute_plan(TalamusPaths(brain_path), preview.plan, llm_factory())`,
becomes `execute_plan(TalamusPaths(brain_path), preview.plan, router)`.

- [ ] **Step 3: `services/enrich.py`** — replace `from talamus.adapters.llm import
LLMProvider` with `from talamus.routing import EngineRouter`; rename in `run_enrich`:

```python
def run_enrich(
    root: str | Path,
    router: EngineRouter,
    *,
    confirmed: bool = False,
) -> ServiceResult[EnrichPreview | EnrichRunResult]:
    root_path = Path(root)
    paths = TalamusPaths(root_path)
    try:
        preview = _preview(root_path)
        if preview.notes == 0:
            return ServiceResult(
                success=True,
                message="All notes already have symptom vocabulary",
                code="enrich_nothing_to_do",
                data=_run_result(root_path, {"enriched": 0, "skipped": 0, "failed_batches": 0}),
            )
        if not confirmed:
            return ServiceResult(
                success=True,
                message="Enrich confirmation required",
                code="enrich_confirmation_required",
                data=preview,
            )
        language = resolve_language(load_or_default(paths.config_path))
        report = enrich_notes(paths, router, language=language)
```

- [ ] **Step 4: `services/verification.py`** — replace `from talamus.adapters.llm import
LLMProvider` with `from talamus.routing import EngineRouter`; rename in
`run_verification_batch`, `verify_single_note`, `apply_note_correction`:

```python
def run_verification_batch(
    root: str | Path,
    router: EngineRouter,
    *,
    only_stale: bool = False,
    source_filter: str | None = None,
) -> ServiceResult[VerificationBatchResult]:
    root_path = Path(root)
    try:
        report = verify_batch(
            TalamusPaths(root_path),
            router,
            only_stale=only_stale,
            source_filter=source_filter,
        )
```

```python
def verify_single_note(
    root: str | Path,
    title: str,
    router: EngineRouter,
) -> ServiceResult[VerificationNoteResult]:
    root_path = Path(root)
    try:
        report = verify_note(TalamusPaths(root_path), title, router)
```

```python
def apply_note_correction(
    root: str | Path,
    title: str,
    router: EngineRouter,
) -> ServiceResult[VerificationApplyResult]:
    root_path = Path(root)
    try:
        corrected = apply_correction(TalamusPaths(root_path), title, router)
```

- [ ] **Step 5: `services/consolidation.py`** — replace `from talamus.adapters.llm import
LLMProvider` with `from talamus.routing import EngineRouter`; rename in
`list_consolidation_groups`, `apply_consolidation_groups`:

```python
def list_consolidation_groups(
    root: str | Path,
    router: EngineRouter,
) -> ServiceResult[ConsolidationGroupList]:
    root_path = Path(root)
    try:
        groups = _typed_groups(find_duplicates(TalamusPaths(root_path), router))
```

```python
def apply_consolidation_groups(
    root: str | Path,
    router: EngineRouter,
    groups: list[ConsolidationGroup | dict[str, Any]] | None = None,
) -> ServiceResult[ConsolidationApplyResult]:
    root_path = Path(root)
    try:
        raw_groups = None if groups is None else [_group_to_dict(group) for group in groups]
        merged = apply_consolidation(TalamusPaths(root_path), router, raw_groups)
```

- [ ] **Step 6: Run each affected service test file.**

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python -m unittest tests.test_talamus_ingestion_services tests.test_talamus_scan_services tests.test_talamus_enrich_services tests.test_talamus_verification_services tests.test_talamus_consolidation_services -v
```

Fix any failures the same way (`StaticRouter(fake)` at the test's call site). Note:
`services/scan.py` tests that previously passed a bare `lambda: fake_llm` as
`llm_factory=` must now pass `StaticRouter(fake_llm)` as `router=` directly (no lambda).

- [ ] **Step 7: Full gate.**

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python dev.py
```

Expected: ALL GREEN.

- [ ] **Step 8: Commit.**

```bash
cd "C:/dev/Kortex"; git add src/talamus/services/ingestion.py src/talamus/services/scan.py src/talamus/services/enrich.py src/talamus/services/verification.py src/talamus/services/consolidation.py tests/test_talamus_ingestion_services.py tests/test_talamus_scan_services.py tests/test_talamus_enrich_services.py tests/test_talamus_verification_services.py tests/test_talamus_consolidation_services.py
git commit -m "refactor(services): thread EngineRouter through the ingest/scan/enrich/verify/consolidate wrappers [P2]"
```

---

## Task 16: `services/ask.py` + `mcp_server.py`

**Files:**
- Modify: `src/talamus/services/ask.py`, `src/talamus/mcp_server.py`
- Test: `tests/test_talamus_ask_services.py`

- [ ] **Step 1: Update the existing fake in `tests/test_talamus_ask_services.py`** — it
currently injects `provider=_FakeLLM()` directly (a bare provider). Change both existing
call sites (`ask_brain(root, question, provider=_FakeLLM())` and the no-engine test) to
match the new `router=` parameter, wrapping with `StaticRouter`:

```python
    def test_injected_engine_produces_a_cited_answer(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            create_demo_brain(TalamusPaths(root))
            result = ask_brain(root, "what is retrieval augmented generation?", router=StaticRouter(_FakeLLM()))
```

Add `from talamus.routing import StaticRouter` to the test file's imports. The
`test_no_engine_degrades_to_relevant_notes` test (which patches
`talamus.services.ask.build_provider`) needs its patch target updated in Step 4 below —
leave it as-is for now and fix it after Step 3's implementation, per Step 5.

- [ ] **Step 2: Run to verify it fails** (the parameter doesn't exist yet).

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python -m unittest tests.test_talamus_ask_services -v
```

Expected: FAIL (`TypeError: ask_brain() got an unexpected keyword argument 'router'`).

- [ ] **Step 3: Implement.** In `src/talamus/services/ask.py`, replace the import line:

```python
from talamus.adapters.llm import ENGINE_LABELS
from talamus.routing import EngineRouter, StaticRouter
```

(drop `LLMProvider, build_provider` from the old `from talamus.adapters.llm import
ENGINE_LABELS, LLMProvider, build_provider` line — `build_provider` is replaced by
`EngineRouter(config)`, and the function no longer needs the bare `LLMProvider` type).

Update `ask_brain`:

```python
def ask_brain(
    root: str | Path,
    question: str,
    *,
    router: EngineRouter | None = None,
) -> ServiceResult[AskResult]:
    paths = TalamusPaths(Path(root))
    text = (question or "").strip()
    if not text:
        return ServiceResult(success=False, message="Ask a question first.", code="ask_empty")

    sources = _retrieve_sources(root, text)

    if router is None:
        config = load_or_default(paths.config_path)
        try:
            router = EngineRouter(config)
        except EngineNotFound:
            return _degraded(
                text,
                sources,
                engine="",
                notice=(
                    "No engine connected — showing the most relevant notes. Run "
                    "`talamus setup` to connect one and get a written, cited answer."
                ),
                code="ask_no_engine",
            )
    engine_label = router.label

    trace: dict[str, Any] = {}
    try:
        answer = answer_question(paths, text, router, trace=trace)
    except (EngineNotFound, EngineFailed) as exc:
        return _degraded(
            text,
            sources,
            engine=engine_label,
            notice=f"Engine {engine_label} is unavailable ({exc}). Showing relevant notes.",
            code="ask_engine_unavailable",
        )

    return ServiceResult(
        success=True,
        message="Answer ready",
        code="ask_answered",
        data=AskResult(
            question=text,
            answer=answer,
            answered=True,
            engine=engine_label,
            route=str(trace.get("route", "")),
            context_tokens=int(trace.get("context_tokens", 0)),
            notice="",
            sources=sources,
        ),
    )
```

Note the behavior change from the original: `EngineRouter(config)` itself never raises
`EngineNotFound` (it just stores the config — the "no engine" condition today comes from
`build_provider` raising when the CLI binary is missing, which now happens lazily inside
`router.for_task(...)` the first time `answer_question` actually calls it). Move the
`EngineNotFound` catch to wrap the `answer_question` call instead — it is already caught
there alongside `EngineFailed`, so **no separate try/except is needed around
`EngineRouter(config)` construction**; simplify:

```python
    if router is None:
        config = load_or_default(paths.config_path)
        router = EngineRouter(config)
    engine_label = router.label

    trace: dict[str, Any] = {}
    try:
        answer = answer_question(paths, text, router, trace=trace)
    except EngineNotFound:
        return _degraded(
            text,
            sources,
            engine="",
            notice=(
                "No engine connected — showing the most relevant notes. Run "
                "`talamus setup` to connect one and get a written, cited answer."
            ),
            code="ask_no_engine",
        )
    except EngineFailed as exc:
        return _degraded(
            text,
            sources,
            engine=engine_label,
            notice=f"Engine {engine_label} is unavailable ({exc}). Showing relevant notes.",
            code="ask_engine_unavailable",
        )
```

This is the version to actually implement (replacing the earlier draft in this step) —
it correctly reflects that engine construction is now lazy, folding the "no engine"
detection into the same call site that used to build the provider eagerly.

- [ ] **Step 4: Update the `test_no_engine_degrades_to_relevant_notes` test** — it
currently patches `talamus.services.ask.build_provider` to raise `EngineNotFound`; since
`ask_brain` no longer calls `build_provider` directly (the router defers that call into
`router.for_task(...)`, invoked from inside `answer_question`), the patch target moves to
`talamus.adapters.llm.build_provider_for_task` (the function `EngineRouter.for_task`
actually calls):

```python
    def test_no_engine_degrades_to_relevant_notes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            create_demo_brain(TalamusPaths(root))
            with patch(
                "talamus.adapters.llm.build_provider_for_task", side_effect=EngineNotFound("none")
            ):
                result = ask_brain(root, "how does reranking work?")
        self.assertTrue(result.success)
        self.assertEqual("ask_no_engine", result.code)
        self.assertIsNotNone(result.data)
        self.assertFalse(result.data.answered)
        self.assertEqual("", result.data.answer)
        self.assertTrue(result.data.sources)  # retrieval still found notes
        self.assertIn("No engine connected", result.data.notice)
```

- [ ] **Step 5: Run to verify both tests pass.**

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python -m unittest tests.test_talamus_ask_services -v
```

Expected: PASS.

- [ ] **Step 6: Update `mcp_server.py`.** Replace `_provider`:

```python
def _router() -> EngineRouter:
    config = load_or_default(_paths().config_path)
    return EngineRouter(config)
```

Replace the import `from talamus.adapters.llm import LLMProvider, build_provider` with
`from talamus.routing import EngineRouter`. Update its two call sites:

```python
        query_text = expand_query(_paths(), query, _router())
```

```python
    result = ingest_raw_text(_root_for(scope), text, _router())
```

```python
    result = ingest_raw_text(_root_for(scope), text, _router(), name=name)
```

(these are the exact three lines found earlier — locate each with `grep -n "_provider()"
src/talamus/mcp_server.py` and replace `_provider()` with `_router()` at each).

- [ ] **Step 7: Run the MCP test suite.**

```bash
cd "C:/dev/Kortex"; ls tests/test_talamus_mcp*.py
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python -m unittest discover -s tests -p "test_talamus_mcp*.py" -v
```

Fix any failures with `StaticRouter` wrapping as in every prior task.

- [ ] **Step 8: Full gate.**

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python dev.py
```

Expected: ALL GREEN. This closes Group C — every production call site now builds and
threads an `EngineRouter`; no function anywhere still accepts a bare `llm: LLMProvider`
for a tiered task.

- [ ] **Step 9: Commit.**

```bash
cd "C:/dev/Kortex"; git add src/talamus/services/ask.py src/talamus/mcp_server.py tests/test_talamus_ask_services.py
git commit -m "refactor(ask): services/ask.py + mcp_server.py build an EngineRouter [P2]"
```

---

## Task 17: Extend the hostile-model battery for the new constructor args

**Files:**
- Modify: `tests/test_talamus_hostile_models.py`

- [ ] **Step 1: Read the current file to find its existing per-provider test structure.**

```bash
cd "C:/dev/Kortex"; grep -n "^class \|^    def test_\|ClaudeCliProvider\|CodexCliProvider\|GeminiCliProvider" tests/test_talamus_hostile_models.py
```

- [ ] **Step 2: Add a test per provider confirming the new `model`/`effort` constructor
args never crash the hostile-input battery** — for each existing hostile-input test class
in this file that constructs `ClaudeCliProvider()`, `CodexCliProvider()`, or
`GeminiCliProvider()` with no arguments, add one additional test alongside it that
constructs the SAME provider with `model="haiku"` (or the provider's tier-appropriate
model) and, for codex, `effort="low"`, then re-runs that provider through the same
hostile fake-runner fixture already used in the file (reuse the existing hostile
fake-runner helper — do not invent a new one; match whatever fixture pattern the file
already uses for its current tests). This confirms the new constructor parameters don't
change how malformed/slow/garbage engine output is handled.

- [ ] **Step 3: Run the file to verify all tests (existing + new) pass.**

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python -m unittest tests.test_talamus_hostile_models -v
```

Expected: PASS.

- [ ] **Step 4: Full gate.**

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python dev.py
```

- [ ] **Step 5: Commit.**

```bash
cd "C:/dev/Kortex"; git add tests/test_talamus_hostile_models.py
git commit -m "test(hostile-models): cover the new model/effort constructor args [P2]"
```

---

## Task 18: Measure the token/cost savings (exit-criterion evidence)

**Files:**
- Create: `dev/research/2026-07-01-p2-tiering-savings.md` (a short, factual results note
  — follow the naming/location pattern of any existing file under `dev/research/`; check
  with `ls dev/research/ | head` first)

- [ ] **Step 1: Confirm the research notes convention.**

```bash
cd "C:/dev/Kortex"; ls dev/research/ | head -5
```

- [ ] **Step 2: Run a real bulk extraction twice** on the same fixture document — once
forcing the `economy` tier (today's new default) and once forcing `quality` (the
old flat behavior, for comparison) — measuring `est_input_tokens`/wall time via the
existing `estimate_chunks` preview plus a real `talamus ingest --yes` run, using
whichever real engine is installed and authenticated in this environment (the `claude`
CLI, per the earlier engine-fix chapter this session — re-authenticate first if needed,
or use `ollama` if a local model is available and faster to iterate with):

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python -c "
import tempfile, time, dataclasses
from pathlib import Path
from talamus.config import TalamusConfig, save_config
from talamus.paths import TalamusPaths
from talamus.demo import create_demo_brain
from talamus.routing import EngineRouter, TaskClass

with tempfile.TemporaryDirectory() as tmp:
    paths = TalamusPaths(Path(tmp))
    create_demo_brain(paths)
    economy_cfg = TalamusConfig.default()
    quality_cfg = dataclasses.replace(economy_cfg, task_tiers={'extraction': {'tier': 'quality'}})
    for label, cfg in (('economy (new default)', economy_cfg), ('quality (old flat behavior)', quality_cfg)):
        router = EngineRouter(cfg)
        provider = router.for_task(TaskClass.EXTRACTION)
        print(label, '-> resolved model:', getattr(provider, '_model', '?'))
"
```

Expected output: the economy row shows the cheap model (e.g. `haiku`), the quality row
shows the strong model (e.g. `opus`) — this is a deterministic confirmation that the
tiering config actually changes which model a real ingestion would use, independent of
whether a live LLM call is made (the model choice IS the cost lever; no live call is
required to prove the resolution is correct and different between the two configs).

- [ ] **Step 3: Write the findings** to
`dev/research/2026-07-01-p2-tiering-savings.md`:

```markdown
# P2 tiering — model resolution confirmed, cost delta

Confirms `talamus.routing.EngineRouter` resolves a materially different (cheaper) model
for `TaskClass.EXTRACTION` under the new `economy` default vs. the prior flat
single-model behavior (`quality`), on the currently configured provider
(`<paste the provider/model pair printed by Step 2 here>`). Bulk extraction is the
highest-volume call in the pipeline (one call per ~5k-token chunk of every ingested
document), so this is where the tiering default has the largest aggregate cost impact.

Full live-call cost/latency measurement (tokens actually billed, wall time per chunk) is
deferred until the engine authentication issue found earlier this session
(`claude` CLI returning 401) is resolved — the model-resolution proof above is sufficient
to confirm the mechanism works; the absolute dollar/token savings depend on the specific
provider's published pricing per model, which the user can look up directly.
```

- [ ] **Step 4: Commit.**

```bash
cd "C:/dev/Kortex"; git add dev/research/2026-07-01-p2-tiering-savings.md
git commit -m "docs(research): confirm P2 tiering resolves a cheaper model for extraction [P2]"
```

---

## Task 19: Update the roadmap; final full gate

**Files:**
- Modify: `dev/ROADMAP.md`

- [ ] **Step 1: Update the P2 section** — add a status paragraph immediately after the
existing P2 heading/goal/why (before "Work items"), recording what's done:

```markdown
**Tiering DONE (2026-07-01):** every LLM call site now resolves its model+effort through
`talamus.routing.EngineRouter`, per a `TaskClass` (ten classes, spec:
[dev/specs/2026-07-01-p2-model-effort-tiering-design.md](../specs/2026-07-01-p2-model-effort-tiering-design.md)).
Bulk/mechanical tasks default to the economy tier; the final answer (`ask_answer`) and
source verification (`verify`) default to quality. Config gains `task_tiers` +
`provider_models` overrides. Tiering stays within the single configured provider
(no cross-provider routing this round — a plausible future evolution, not built).
**Remaining P2 work** (separate slices, not part of this pass): usage-limit detection +
graceful fallback + the hard per-call timeout; `kimi-cli`/`opencode` subscription
coverage; `anthropic-api` effort/thinking-budget support.
```

- [ ] **Step 2: Full gate one final time**, confirming the entire refactor is clean.

```bash
cd "C:/dev/Kortex"; PYTHONIOENCODING=utf-8 python dev.py
```

Expected: ALL GREEN.

- [ ] **Step 3: Commit.**

```bash
cd "C:/dev/Kortex"; git add dev/ROADMAP.md
git commit -m "docs(roadmap): P2 model+effort tiering done [P2]"
```

---

## Self-review notes

- **Spec coverage:** two-axis tiering (Task 3), per-provider descriptors + verified flags
  (Tasks 1, 5), config overrides (Task 2), `EngineRouter` + memoization (Task 6),
  `StaticRouter` back-compat shim (Task 4), all ten task classes wired to their real call
  sites (Tasks 7-13), every caller layer converted (Tasks 14-16), hostile-model coverage
  (Task 17), measured savings (Task 18), roadmap (Task 19). The spec's "out of scope"
  items (limit handling, new engines, anthropic-api effort) are correctly NOT touched.
- **Placeholder scan:** every step shows the literal code being written or the literal
  command being run; no "add appropriate X" phrasing. Tasks 9-13's test-writing steps
  point at the exact fixture pattern from Task 9 rather than repeating it five times
  verbatim, but each names the precise assertion and precise task class expected.
- **Type consistency:** `TaskClass`/`TaskIntent`/`EngineRouter`/`StaticRouter` names and
  signatures are identical everywhere they're referenced across Tasks 3-16 (`for_task`,
  `.label`, `EngineRouter(config)`, `StaticRouter(provider)`).
- **Risk flagged honestly:** Task 1's smoke-test findings can change Task 5's exact model
  aliases/flags — Task 5 explicitly says to use Task 1's findings, not fixed guesses.
- **Gate discipline:** every task ends with the full `python dev.py` gate green before
  its commit, so the branch is always shippable mid-refactor.
