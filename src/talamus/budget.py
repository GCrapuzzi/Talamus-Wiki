"""Context budgeting — keep the cost of answering flat as the brain grows.

Retrieval already caps the *number* of notes, but notes vary wildly in length, so
token cost still drifts with the brain. This caps the context by *estimated tokens*:
the reranked, best-first items are kept as a top-prefix that fits the budget. The
estimator is a cheap stdlib heuristic (no tiktoken — that stays an optional extra).
"""

from __future__ import annotations

import os

DEFAULT_CONTEXT_BUDGET = 6000


def estimate_tokens(text: str) -> int:
    """Rough token count without tiktoken: ~4 chars/token, with a word-count floor.

    Uses the max of the two estimates so we over- rather than under-count — safer for
    staying under a budget meant to protect the model's context window.
    """
    if not text:
        return 0
    return max(len(text) // 4, len(text.split()))


def context_budget(override: int | None = None) -> int:
    """Token budget for assembled context. Order: explicit override, env, default."""
    if override is not None:
        return override
    env = os.environ.get("TALAMUS_CONTEXT_BUDGET", "")
    if env.isdigit():
        return int(env)
    return DEFAULT_CONTEXT_BUDGET


def fit_to_budget(items: list[dict], budget: int, *, content_key: str = "content") -> list[dict]:
    """Keep the best-first prefix of items whose cumulative tokens stay within budget.

    Rank order is preserved (we keep a contiguous top-prefix, never reorder to pack).
    If the single top item already exceeds the budget, include a truncated head of it
    so the most relevant note is never dropped entirely.
    """
    if budget <= 0:
        return []
    kept: list[dict] = []
    used = 0
    for item in items:
        cost = estimate_tokens(str(item.get(content_key, "")))
        if used + cost <= budget:
            kept.append(item)
            used += cost
            continue
        if not kept:
            truncated = dict(item)
            truncated[content_key] = str(item.get(content_key, ""))[: budget * 4]
            kept.append(truncated)
        break
    return kept
