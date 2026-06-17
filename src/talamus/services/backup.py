from __future__ import annotations

import shutil
import zipfile
from dataclasses import asdict, dataclass
from pathlib import Path, PurePosixPath
from typing import Any, TypeVar

from talamus.paths import TalamusPaths
from talamus.services.result import ServiceResult

T = TypeVar("T")


@dataclass(frozen=True)
class BackupExportResult:
    root: str
    archive_path: str
    members: int

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class BackupImportResult:
    root: str
    archive_path: str
    members: int

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def export_brain(root: str | Path, out_file: str | Path) -> ServiceResult[BackupExportResult]:
    root_path = Path(root)
    paths = TalamusPaths(root_path)
    if not paths.config_path.exists():
        return ServiceResult(
            success=False,
            message=f"no brain at {root_path}",
            code="backup_no_brain",
        )
    archive_path = Path(out_file)
    try:
        members = _export_members(paths)
        archive_path.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_DEFLATED) as archive:
            for member in members:
                archive.write(member, member.relative_to(root_path).as_posix())
    except (OSError, TypeError, ValueError, AttributeError, zipfile.BadZipFile) as exc:
        return _backup_error(exc)
    return ServiceResult(
        success=True,
        message=f"exported brain to {archive_path}",
        code="backup_exported",
        data=BackupExportResult(
            root=str(root_path),
            archive_path=str(archive_path),
            members=len(members),
        ),
    )


def import_brain_archive(
    in_file: str | Path, root: str | Path
) -> ServiceResult[BackupImportResult]:
    archive_path = Path(in_file)
    root_path = Path(root)
    try:
        root_path.mkdir(parents=True, exist_ok=True)
        members = 0
        with zipfile.ZipFile(archive_path) as archive:
            for info in archive.infolist():
                if info.is_dir():
                    continue
                target = _safe_archive_target(root_path, info.filename)
                target.parent.mkdir(parents=True, exist_ok=True)
                with archive.open(info) as source, target.open("wb") as destination:
                    shutil.copyfileobj(source, destination)
                members += 1
    except ValueError as exc:
        return ServiceResult(
            success=False,
            message=f"Import rejected: {exc}",
            code="backup_import_rejected",
        )
    except (OSError, TypeError, AttributeError, zipfile.BadZipFile) as exc:
        return _backup_error(exc)
    return ServiceResult(
        success=True,
        message=f"imported brain into {root_path}",
        code="backup_imported",
        data=BackupImportResult(
            root=str(root_path),
            archive_path=str(archive_path),
            members=members,
        ),
    )


def _export_members(paths: TalamusPaths) -> list[Path]:
    members = [paths.config_path]
    if paths.notes.exists():
        members.extend(paths.notes.rglob("*"))
    if paths.talamus_dir.exists():
        members.extend(paths.talamus_dir.rglob("*"))
    return [member for member in members if member.is_file()]


def _safe_archive_target(root: Path, member_name: str) -> Path:
    normalized = member_name.replace("\\", "/")
    name = PurePosixPath(normalized)
    if name.is_absolute() or any(part in ("", "..") or part.endswith(":") for part in name.parts):
        raise ValueError(f"unsafe archive member: {member_name}")
    root_resolved = root.resolve()
    target = (root / Path(*name.parts)).resolve()
    try:
        target.relative_to(root_resolved)
    except ValueError as exc:
        raise ValueError(f"archive member escapes destination: {member_name}") from exc
    return target


def _backup_error(exc: Exception) -> ServiceResult[T]:
    return ServiceResult(
        success=False,
        message=f"Backup service error: {exc}",
        code="backup_service_error",
    )
