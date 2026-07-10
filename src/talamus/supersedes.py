"""Supersedes detection at ingest — the temporal graph populates itself.

After new notes are compiled, each one is checked against its closest existing
neighbor (deterministic prefilter: top index hits sharing title vocabulary).
When the model is confident the new note REPLACES the old one, the bitemporal
handover (`temporal.record_supersedes`) is applied automatically and reported;
when it is unsure, the handover is proposed to the review queue instead.
Either way nothing is deleted: the old note keeps its prose and history and
stays reachable as-of the past. Detection adds at most one LLM call per new
note with a plausible neighbor; disable with TALAMUS_SUPERSEDES_DETECTION=0.
"""

from __future__ import annotations

import os

from talamus.errors import EngineFailed, EngineNotFound
from talamus.model_json import json_object
from talamus.models import CanonicalNote
from talamus.paths import TalamusPaths
from talamus.routing import Router, TaskClass
from talamus.textutil import tokens

AUTO_APPLY_CONFIDENCE = 0.8

_JUDGE_PROMPT = """Two notes from the same knowledge base may describe the same subject at
different times. Decide whether the NEW note REPLACES the OLD one: same
subject, but updated, revised or contradicting content (a newer version of a
procedure, policy, decision or fact). Notes that are merely related are NOT a
replacement.
Return ONLY JSON: {{"supersedes": true|false, "confidence": 0.0-1.0, "reason": "<short>"}}

OLD: {old_title}
{old_summary}

NEW: {new_title}
{new_summary}
"""


def detection_enabled() -> bool:
    return os.environ.get("TALAMUS_SUPERSEDES_DETECTION", "1") != "0"


def _candidate(paths: TalamusPaths, note: CanonicalNote, exclude_ids: set[str]) -> dict | None:
    """The closest existing note that plausibly covers the same subject:
    a top index hit outside the new batch whose TITLE shares vocabulary with
    the new title. Deterministic, zero LLM calls."""
    from talamus.indexes import search_index

    title_tokens = set(tokens(note.title))
    if not title_tokens:
        return None
    for hit in search_index(paths, f"{note.title} {note.summary}", limit=4):
        if str(hit.get("note_id", "")) in exclude_ids:
            continue
        if not title_tokens & set(tokens(str(hit.get("title", "")))):
            continue
        return hit
    return None


def detect_supersedes(paths: TalamusPaths, new_notes: list[CanonicalNote], router: Router) -> dict:
    """Check each new note against its closest neighbor; apply confident
    handovers, propose uncertain ones. Returns {"applied": [...], "proposed": [...]}.
    Engine trouble never fails the ingest that already succeeded."""
    applied: list[dict] = []
    proposed: list[dict] = []
    if not detection_enabled() or not new_notes:
        return {"applied": applied, "proposed": proposed}
    from talamus.review import ReviewQueue
    from talamus.temporal import record_supersedes

    exclude = {note.note_id for note in new_notes}
    llm = None
    for note in new_notes:
        hit = _candidate(paths, note, exclude)
        if hit is None:
            continue
        if llm is None:
            llm = router.for_task(TaskClass.CONSOLIDATE)
        try:
            raw = llm.complete(
                _JUDGE_PROMPT.format(
                    old_title=str(hit.get("title", "")),
                    old_summary=str(hit.get("summary", "")),
                    new_title=note.title,
                    new_summary=note.summary,
                )
            )
        except (EngineFailed, EngineNotFound):
            break  # the ingest already succeeded; detection can wait for a retry
        try:
            verdict = json_object(raw)
        except ValueError:  # hostile/empty model output: detection is best-effort
            continue
        if not verdict.get("supersedes"):
            continue
        try:
            confidence = float(verdict.get("confidence", 0.0))
        except (TypeError, ValueError):
            confidence = 0.0
        old_title = str(hit.get("title", ""))
        reason = str(verdict.get("reason", ""))
        entry = {"old": old_title, "new": note.title, "confidence": round(confidence, 2)}
        if confidence >= AUTO_APPLY_CONFIDENCE:
            try:
                record_supersedes(paths, old_title, note.title, evidence=reason)
            except ValueError:
                continue
            applied.append(entry)
        else:
            ReviewQueue(paths).add(
                "supersedes",
                f"'{note.title}' may supersede '{old_title}'",
                detail={**entry, "reason": reason},
            )
            proposed.append(entry)
    return {"applied": applied, "proposed": proposed}
