from __future__ import annotations

import json
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

REGISTRY_VERSION = "1.0"


@dataclass(frozen=True)
class RegistryEntry:
    raw_path: str
    raw_hash: str
    raw_size: int
    normalized_paths: list[str]
    category: str
    parser: str
    captured_at: str
    ingestion_run: str
    promoted_to: list[str] = field(default_factory=list)


def _entry_from_dict(data: dict) -> RegistryEntry:
    return RegistryEntry(
        raw_path=data["raw_path"],
        raw_hash=data["raw_hash"],
        raw_size=data["raw_size"],
        normalized_paths=list(data.get("normalized_paths", [])),
        category=data["category"],
        parser=data["parser"],
        captured_at=data["captured_at"],
        ingestion_run=data["ingestion_run"],
        promoted_to=list(data.get("promoted_to", [])),
    )


def load_registry(registry_path: Path) -> list[RegistryEntry]:
    if not registry_path.exists():
        return []
    data = json.loads(registry_path.read_text(encoding="utf-8"))
    return [_entry_from_dict(item) for item in data.get("entries", [])]


def save_registry(registry_path: Path, entries: list[RegistryEntry]) -> None:
    registry_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "version": REGISTRY_VERSION,
        "entries": [asdict(entry) for entry in entries],
    }
    registry_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


def append_entry(registry_path: Path, entry: RegistryEntry) -> None:
    entries = load_registry(registry_path)
    entries.append(entry)
    save_registry(registry_path, entries)
