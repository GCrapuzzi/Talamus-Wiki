from __future__ import annotations

import json
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from tools.fde_brain.paths import WorkspacePaths


@dataclass
class FileOutcome:
    pending_name: str
    raw_path: str | None
    normalized_path: str | None
    routed_to: str
    category: str
    error: str | None = None
    promoted_to: list[str] = field(default_factory=list)


@dataclass
class RunLog:
    run_id: str
    started_at: str
    finished_at: str | None = None
    files: list[FileOutcome] = field(default_factory=list)
    commit_hash: str | None = None
    overall_ok: bool = True


def _safe_started_at(started_at: str) -> str:
    return started_at.replace(":", "").split("+")[0].split(".")[0]


def write_run_log(paths: WorkspacePaths, log: RunLog) -> Path:
    paths.logs_runs.mkdir(parents=True, exist_ok=True)
    filename = f"{_safe_started_at(log.started_at)}-{log.run_id}.json"
    out = paths.logs_runs / filename
    out.write_text(json.dumps(asdict(log), indent=2, ensure_ascii=False), encoding="utf-8")
    return out
