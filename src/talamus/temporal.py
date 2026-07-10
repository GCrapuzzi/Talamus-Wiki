"""Full bitemporal model: robust as-of parsing + valid-time claim overlay.

Two timelines, kept distinct:

- **transaction time** — when Talamus changed its records: note versions in
  ``.talamus/cache/history/`` (since B4), schema events in the Ontology Lab.
- **valid time** — when a claim was true in the represented world: the overlay in
  ``.talamus/cache/timeline/claims.jsonl``.

The overlay is **append-only** (the current state of a claim is its last record);
notes never move, contradictions close old claims instead of deleting anything.
``parse_when`` accepts year / year-month / date / datetime (with or without
timezone — naive datetimes are read as local time with an explicit warning) and
normalizes to a UTC instant comparable with the store's timestamps.
"""

from __future__ import annotations

import json
import re
import time
from dataclasses import asdict, dataclass, field
from datetime import UTC, datetime
from pathlib import Path

from talamus.errors import TalamusError
from talamus.paths import TalamusPaths


def timeline_dir(paths: TalamusPaths) -> Path:
    return paths.cache / "timeline"


def claims_path(paths: TalamusPaths) -> Path:
    return timeline_dir(paths) / "claims.jsonl"


def _now() -> str:
    return datetime.now(UTC).isoformat()


@dataclass(frozen=True)
class ParsedWhen:
    """A normalized as-of instant: end of the named period, in UTC."""

    instant_utc: str
    original: str
    warning: str | None = None


def parse_when(text: str) -> ParsedWhen:
    """Parse year / year-month / date / datetime into a UTC comparison instant (F6.5).

    Partial dates mean *end of that period* ("as of 2026-01" = state at the end of
    January 2026). Naive datetimes are interpreted in the local timezone, with a
    warning so traces stay honest.
    """
    raw = text.strip()
    local_tz = datetime.now().astimezone().tzinfo
    warning: str | None = None
    if re.fullmatch(r"\d{4}", raw):
        moment = datetime(int(raw), 12, 31, 23, 59, 59, tzinfo=local_tz)
    elif re.fullmatch(r"\d{4}-\d{2}", raw):
        year, month = int(raw[:4]), int(raw[5:7])
        if month == 12:
            next_month = datetime(year + 1, 1, 1, tzinfo=local_tz)
        else:
            next_month = datetime(year, month + 1, 1, tzinfo=local_tz)
        moment = datetime.fromtimestamp(next_month.timestamp() - 1, tz=local_tz)
    elif re.fullmatch(r"\d{4}-\d{2}-\d{2}", raw):
        base = datetime.fromisoformat(raw)
        moment = base.replace(hour=23, minute=59, second=59, tzinfo=local_tz)
    else:
        try:
            moment = datetime.fromisoformat(raw)
        except ValueError as exc:
            raise TalamusError(
                f"invalid as-of time {raw!r} (use 2026, 2026-01, 2026-01-15 or a full ISO datetime)"
            ) from exc
        if moment.tzinfo is None:
            moment = moment.replace(tzinfo=local_tz)
            warning = f"naive datetime {raw!r} interpreted as local time ({local_tz})"
    return ParsedWhen(instant_utc=moment.astimezone(UTC).isoformat(), original=raw, warning=warning)


@dataclass
class Claim:
    claim_id: str
    note_id: str
    text: str
    evidence: str = ""  # source ref
    confidence: float = 0.8
    valid_from: str = ""
    valid_to: str = ""
    observed_at: str = ""
    source_time: str = ""
    transaction_from: str = ""
    transaction_to: str = ""
    invalidated_by: str = ""
    detail: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        return asdict(self)


def _append(paths: TalamusPaths, claim: Claim) -> None:
    timeline_dir(paths).mkdir(parents=True, exist_ok=True)
    with claims_path(paths).open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(claim.to_dict(), ensure_ascii=False))
        handle.write("\n")


def _load_states(paths: TalamusPaths) -> dict[str, Claim]:
    """Current state per claim id (append-only log: last record wins)."""
    path = claims_path(paths)
    if not path.is_file():
        return {}
    states: dict[str, Claim] = {}
    known = {f for f in Claim.__dataclass_fields__}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        data = json.loads(line)
        claim = Claim(**{k: v for k, v in data.items() if k in known})
        states[claim.claim_id] = claim
    return states


def record_claim(
    paths: TalamusPaths,
    note_id: str,
    text: str,
    evidence: str = "",
    valid_from: str = "",
    source_time: str = "",
    confidence: float = 0.8,
) -> Claim:
    """Open a claim in the valid-time overlay. ``valid_from`` empty means
    "valid since observed" (derived from observation, stated explicitly)."""
    now = _now()
    claim = Claim(
        claim_id=f"claim-{note_id}-{time.strftime('%Y%m%d%H%M%S')}-{len(_load_states(paths))}",
        note_id=note_id,
        text=text,
        evidence=evidence,
        confidence=confidence,
        valid_from=valid_from or now,
        observed_at=now,
        source_time=source_time,
        transaction_from=now,
    )
    _append(paths, claim)
    return claim


def invalidate_claim(
    paths: TalamusPaths, claim_id: str, invalidated_by: str, valid_to: str = ""
) -> Claim | None:
    """Close a claim (contradiction/correction): the world stopped matching it.

    Nothing is deleted: a closing record is appended; the old text stays readable
    and queryable as-of any time inside its validity window (F6.6)."""
    states = _load_states(paths)
    claim = states.get(claim_id)
    if claim is None or claim.valid_to:
        return None
    now = _now()
    claim.valid_to = valid_to or now
    claim.invalidated_by = invalidated_by
    claim.transaction_to = now
    _append(paths, claim)
    return claim


def current_claims(paths: TalamusPaths, note_id: str | None = None) -> list[Claim]:
    """Claims valid NOW: open valid window, not invalidated."""
    return [
        claim
        for claim in _load_states(paths).values()
        if not claim.valid_to and (note_id is None or claim.note_id == note_id)
    ]


def claims_by_note(paths: TalamusPaths) -> dict[str, list[Claim]]:
    """Every claim ever recorded (open AND closed), grouped by note, newest
    first — the read feed for surfacing fact validity inside answers."""
    grouped: dict[str, list[Claim]] = {}
    for claim in _load_states(paths).values():
        grouped.setdefault(claim.note_id, []).append(claim)
    for claims in grouped.values():
        claims.sort(key=lambda c: c.valid_from, reverse=True)
    return grouped


def record_supersedes(
    paths: TalamusPaths, old_title: str, new_title: str, evidence: str = ""
) -> dict:
    """The bitemporal handover: NEW supersedes OLD. Nothing is deleted.

    The old note keeps its prose, its sources and its full history — it stays
    readable and reachable as-of any past instant. What changes is its place
    in time: every open claim on it is closed (invalidated by the successor),
    the handover itself is recorded as a claim naming the successor, and a
    typed `supersedes` edge (new → old) enters the graph so default answers
    prefer the successor."""
    import dataclasses

    from talamus.linking import NoteRegistry
    from talamus.models import Relation
    from talamus.store import load_notes, overwrite_note_json, rebuild_indexes

    notes = load_notes(paths)
    registry = NoteRegistry.from_notes(notes)
    old_canonical = registry.resolve(old_title)
    new_canonical = registry.resolve(new_title)
    if old_canonical is None:
        raise ValueError(f"note not found: {old_title!r}")
    if new_canonical is None:
        raise ValueError(f"note not found: {new_title!r}")
    if old_canonical == new_canonical:
        raise ValueError("a note cannot supersede itself")
    by_title = {note.title: note for note in notes}
    old, new = by_title[old_canonical], by_title[new_canonical]

    closed: list[str] = []
    for claim in current_claims(paths, old.note_id):
        got = invalidate_claim(paths, claim.claim_id, f"superseded by '{new.title}'")
        if got is not None:
            closed.append(got.claim_id)
    marker = record_claim(
        paths,
        old.note_id,
        f"Superseded by '{new.title}'",
        evidence=evidence,
        confidence=0.95,
    )
    if not any(r.relation == "supersedes" and r.target == old.title for r in new.relations):
        relation = Relation(
            source=new.title, relation="supersedes", target=old.title, confidence=0.95
        )
        overwrite_note_json(paths, dataclasses.replace(new, relations=[*new.relations, relation]))
        rebuild_indexes(paths)
    return {
        "old": old.title,
        "new": new.title,
        "claims_closed": closed,
        "claim": marker.claim_id,
    }


def claims_as_of(paths: TalamusPaths, when: ParsedWhen, note_id: str | None = None) -> list[Claim]:
    """Claims valid AT the given instant — including ones invalidated later."""
    instant = when.instant_utc
    results = []
    for claim in _load_states(paths).values():
        if note_id is not None and claim.note_id != note_id:
            continue
        if claim.valid_from and claim.valid_from > instant:
            continue
        if claim.valid_to and claim.valid_to <= instant:
            continue
        results.append(claim)
    return results


def note_timeline(paths: TalamusPaths, title: str) -> dict:
    """Both timelines for one note (F6.3): transaction history of the record,
    valid-time claim events, kept clearly apart."""
    from talamus.timeline import note_history

    versions = note_history(paths, title)
    note_id = ""
    if versions:
        note_id = str(versions[-1].get("note_id", ""))
    states = [c for c in _load_states(paths).values() if not note_id or c.note_id == note_id]
    transaction = [
        {"at": v.get("updated_at", ""), "event": "version", "summary": v.get("summary", "")}
        for v in versions
    ]
    valid: list[dict] = []
    for claim in states:
        valid.append(
            {
                "from": claim.valid_from,
                "to": claim.valid_to or "(corrente)",
                "text": claim.text,
                "invalidated_by": claim.invalidated_by,
            }
        )
    return {"title": title, "transaction": transaction, "valid": valid}
