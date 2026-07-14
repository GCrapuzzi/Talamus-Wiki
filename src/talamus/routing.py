"""Per-task model+effort tiering.

A TaskClass names one point in the pipeline that makes exactly one LLM call. Each task
carries a TaskIntent (tier, effort); an EngineRouter resolves that intent, within the
single provider configured for the brain, into a concrete LLMProvider. Task classes
never know provider-specific model names; providers never know about task classes.
The one sanctioned cross-provider path is the FALLBACK CHAIN: when the engine
signals it cannot serve right now (usage limit exhausted, CLI missing), the same
request retries on the next provider in config.fallback_providers.
"""

from __future__ import annotations

import sys
from collections.abc import Callable
from dataclasses import dataclass
from enum import StrEnum
from typing import Protocol

from talamus.adapters.llm import (
    ENGINE_LABELS,
    LLMProvider,
    build_provider_for_task,
    canonical_provider,
)
from talamus.config import TalamusConfig
from talamus.errors import EngineLimitReached, EngineNotFound


class TaskClass(StrEnum):
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


class Router(Protocol):
    """The interface leaf functions depend on: resolve a TaskClass to a provider.

    Both EngineRouter (real per-task tiering) and StaticRouter (one fixed engine)
    satisfy it structurally, so a leaf annotated ``router: Router`` accepts either —
    production code passes an EngineRouter, tests and single-engine callers a
    StaticRouter, with no leaf-side change."""

    label: str

    def for_task(self, task: TaskClass) -> LLMProvider: ...


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


def _fallback_chain(config: TalamusConfig, primary: str) -> list[str]:
    """The configured chain, normalized: canonical names, no dupes, no primary.
    Accepts a comma-separated string too (a TALAMUS_FALLBACK_PROVIDERS env
    override arrives as a raw string)."""
    raw = getattr(config, "fallback_providers", []) or []
    if isinstance(raw, str):
        raw = [part for part in raw.split(",")]
    chain: list[str] = []
    for entry in raw:
        name = canonical_provider(str(entry).strip())
        if name and name != primary and name not in chain:
            chain.append(name)
    return chain


class FallbackProvider:
    """The engine chain. Tries the primary; when it signals "cannot serve right
    now" (EngineLimitReached, EngineNotFound) the SAME prompt retries on the
    next engine, with a loud stderr notice naming the switch. Generic
    EngineFailed does NOT fall back — that usually means a real bug, and
    silently retrying elsewhere would hide it (and double-spend)."""

    def __init__(
        self,
        primary_name: str,
        primary: LLMProvider,
        alternates: list[tuple[str, Callable[[], LLMProvider]]],
    ) -> None:
        self._primary_name = primary_name
        self._primary = primary
        self._alternates = alternates

    def complete(self, prompt: str) -> str:
        failed_name = self._primary_name
        try:
            return self._primary.complete(prompt)
        except (EngineLimitReached, EngineNotFound) as exc:
            last: Exception = exc
        for name, build in self._alternates:
            print(
                f"warning: engine '{failed_name}' unavailable ({last}) — falling back to '{name}'",
                file=sys.stderr,
            )
            failed_name = name
            try:
                provider = build()
                return provider.complete(prompt)
            except (EngineLimitReached, EngineNotFound) as exc:
                last = exc
        raise last


class EngineRouter:
    """Resolves each TaskClass to a concrete LLMProvider, within the single provider
    configured for the brain (see the design doc's scope note). Built fresh per call
    from a TalamusConfig (no long-lived global state — config changes take effect
    immediately, mirroring the existing build_provider(...) per-call construction).
    Providers are memoized per (tier, effort) so tasks sharing a resolved engine share
    one object."""

    def __init__(self, config: TalamusConfig) -> None:
        self._config = config
        self._provider_name = canonical_provider(config.llm_provider)
        self._cache: dict[tuple[str, str], LLMProvider] = {}
        self.label = ENGINE_LABELS.get(self._provider_name, self._provider_name)

    def for_task(self, task: TaskClass) -> LLMProvider:
        intent = _resolve_intent(self._config, task)
        key = (intent.tier, intent.effort)
        if key not in self._cache:
            self._cache[key] = self._build_with_chain(intent.tier, intent.effort)
        return self._cache[key]

    def _build_with_chain(self, tier: str, effort: str) -> LLMProvider:
        chain = _fallback_chain(self._config, self._provider_name)
        names = [self._provider_name, *chain]
        primary: LLMProvider | None = None
        primary_name = self._provider_name
        rest: list[str] = []
        last: Exception | None = None
        for index, name in enumerate(names):
            try:
                primary = build_provider_for_task(name, self._config, tier, effort)
            except EngineNotFound as exc:
                last = exc
                if index < len(names) - 1:
                    print(
                        f"warning: engine '{name}' unavailable ({exc}) — "
                        f"falling back to '{names[index + 1]}'",
                        file=sys.stderr,
                    )
                continue
            primary_name = name
            rest = names[index + 1 :]
            break
        if primary is None:
            raise last if last is not None else EngineNotFound(self._provider_name)
        if not rest:
            return primary
        config = self._config

        def _alternate(name: str) -> Callable[[], LLMProvider]:
            def build() -> LLMProvider:
                return build_provider_for_task(name, config, tier, effort)

            return build

        alternates = [(name, _alternate(name)) for name in rest]
        return FallbackProvider(primary_name, primary, alternates)
