"""The engine fallback chain: when the configured engine hits its usage limit
(or its CLI is missing), the SAME request retries on the next provider in
`fallback_providers` — ollama last means work never fully stops. Generic
engine failures do NOT fall back: they usually mean a real bug worth seeing."""

from __future__ import annotations

import unittest
from dataclasses import replace
from unittest import mock

from talamus.config import TalamusConfig
from talamus.errors import EngineFailed, EngineLimitReached, EngineNotFound
from talamus.routing import EngineRouter, TaskClass


class LimitedProvider:
    def __init__(self) -> None:
        self.calls = 0

    def complete(self, prompt: str) -> str:
        self.calls += 1
        raise EngineLimitReached("claude-cli", "usage limit reached")


class BrokenProvider:
    def complete(self, prompt: str) -> str:
        raise EngineFailed("claude-cli", "malformed output")


class OkProvider:
    def __init__(self, answer: str = "ok") -> None:
        self.answer = answer
        self.calls = 0

    def complete(self, prompt: str) -> str:
        self.calls += 1
        return self.answer


def _config(*fallbacks: str) -> TalamusConfig:
    return replace(
        TalamusConfig.default(),
        llm_provider="claude-cli",
        fallback_providers=list(fallbacks),
    )


def _router_with(providers: dict[str, object], config: TalamusConfig) -> EngineRouter:
    """EngineRouter whose provider construction is table-driven for the test."""
    router = EngineRouter(config)

    def fake_build(name: str, _config: TalamusConfig, _tier: str, _effort: str) -> object:
        provider = providers.get(name)
        if provider is None:
            raise EngineNotFound(name)
        return provider

    patcher = mock.patch("talamus.routing.build_provider_for_task", side_effect=fake_build)
    patcher.start()
    return router, patcher  # type: ignore[return-value]


class FallbackChainTests(unittest.TestCase):
    def test_limit_on_primary_falls_back_to_the_next_engine(self) -> None:
        limited, backup = LimitedProvider(), OkProvider("from ollama")
        router, patcher = _router_with({"claude-cli": limited, "ollama": backup}, _config("ollama"))
        self.addCleanup(patcher.stop)

        answer = router.for_task(TaskClass.ASK_ANSWER).complete("hi")

        self.assertEqual("from ollama", answer)
        self.assertEqual(1, limited.calls)
        self.assertEqual(1, backup.calls)

    def test_every_engine_limited_raises_the_limit_error(self) -> None:
        router, patcher = _router_with(
            {"claude-cli": LimitedProvider(), "ollama": LimitedProvider()}, _config("ollama")
        )
        self.addCleanup(patcher.stop)

        with self.assertRaises(EngineLimitReached):
            router.for_task(TaskClass.ASK_ANSWER).complete("hi")

    def test_generic_failures_do_not_fall_back(self) -> None:
        backup = OkProvider()
        router, patcher = _router_with(
            {"claude-cli": BrokenProvider(), "ollama": backup}, _config("ollama")
        )
        self.addCleanup(patcher.stop)

        with self.assertRaises(EngineFailed):
            router.for_task(TaskClass.ASK_ANSWER).complete("hi")
        self.assertEqual(0, backup.calls)

    def test_missing_primary_cli_uses_the_chain(self) -> None:
        backup = OkProvider("backup")
        router, patcher = _router_with({"ollama": backup}, _config("ollama"))
        self.addCleanup(patcher.stop)

        answer = router.for_task(TaskClass.ASK_ANSWER).complete("hi")

        self.assertEqual("backup", answer)

    def test_no_chain_behaves_exactly_as_before(self) -> None:
        limited = LimitedProvider()
        router, patcher = _router_with({"claude-cli": limited}, _config())
        self.addCleanup(patcher.stop)

        with self.assertRaises(EngineLimitReached):
            router.for_task(TaskClass.ASK_ANSWER).complete("hi")
        self.assertEqual(1, limited.calls)


if __name__ == "__main__":
    unittest.main()
