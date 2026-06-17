from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import TypeVar

from talamus.registry import (
    BRAIN_TYPES,
    BrainInfo,
    Registry,
    load_registry,
    register_brain,
    registry_path,
    rename_brain,
    select_brain,
    set_brain_flag,
    talamus_home,
    unregister_brain,
)
from talamus.services.result import ServiceResult

T = TypeVar("T")


@dataclass(frozen=True)
class BrainItem:
    id: str
    name: str
    path: str
    type: str
    federated: bool
    sensitive: bool
    selected: bool
    exists: bool
    notes: int
    created_at: str = ""
    updated_at: str = ""
    last_accessed_at: str = ""
    project: dict | None = None


@dataclass(frozen=True)
class UnregisteredBrain:
    name: str
    path: str
    register_command: str


@dataclass(frozen=True)
class BrainListReport:
    registry_path: str
    selected: str
    brains: list[BrainItem]
    unregistered: list[UnregisteredBrain]


def list_brains(home: Path | None = None) -> ServiceResult[BrainListReport]:
    registry: Registry | ServiceResult[BrainListReport] = _load_registry(home)
    if isinstance(registry, ServiceResult):
        return registry
    root = _home(home)
    registered = [_brain_item(brain, registry.selected) for brain in registry.brains]
    return ServiceResult(
        success=True,
        message="Brain registry loaded",
        code="brain_registry_loaded",
        data=BrainListReport(
            registry_path=str(registry_path(root)),
            selected=registry.selected,
            brains=registered,
            unregistered=_discover_unregistered(root, registry),
        ),
    )


def get_brain(name: str, home: Path | None = None) -> ServiceResult[BrainItem]:
    registry: Registry | ServiceResult[BrainItem] = _load_registry(home)
    if isinstance(registry, ServiceResult):
        return registry
    brain = registry.by_name(name)
    if brain is None:
        return _not_found(name)
    return ServiceResult(
        success=True,
        message=f"Brain {name!r} loaded",
        code="brain_loaded",
        data=_brain_item(brain, registry.selected),
    )


def register_existing_brain(
    root: str | Path,
    name: str | None = None,
    brain_type: str = "project",
    home: Path | None = None,
) -> ServiceResult[BrainItem]:
    if brain_type not in BRAIN_TYPES:
        return ServiceResult(
            success=False,
            message=f"Brain type must be one of {BRAIN_TYPES}, got {brain_type!r}",
            code="brain_type_invalid",
        )
    try:
        info = register_brain(Path(root).resolve(), name=name, brain_type=brain_type, home=home)
        registry = load_registry(home)
    except (OSError, TypeError, ValueError, AttributeError) as exc:
        return _registry_error(exc)
    return ServiceResult(
        success=True,
        message=f"Brain {info.name!r} registered",
        code="brain_registered",
        data=_brain_item(info, registry.selected),
    )


def select_registered_brain(name: str, home: Path | None = None) -> ServiceResult[dict[str, str]]:
    try:
        ok = select_brain(name, home=home)
    except (OSError, TypeError, ValueError, AttributeError) as exc:
        return _registry_error(exc)
    if not ok:
        return _not_found(name)
    return ServiceResult(
        success=True,
        message=f"Brain {name!r} selected",
        code="brain_selected",
        data={"name": name},
    )


def rename_registered_brain(
    old: str, new: str, home: Path | None = None
) -> ServiceResult[BrainItem]:
    try:
        ok = rename_brain(old, new, home=home)
    except ValueError as exc:
        return ServiceResult(success=False, message=str(exc), code="brain_name_exists")
    except (OSError, TypeError, AttributeError) as exc:
        return _registry_error(exc)
    if not ok:
        return _not_found(old)
    return get_brain(new, home=home)


def unregister_registered_brain(
    name: str, home: Path | None = None
) -> ServiceResult[dict[str, str]]:
    try:
        ok = unregister_brain(name, home=home)
    except (OSError, TypeError, ValueError, AttributeError) as exc:
        return _registry_error(exc)
    if not ok:
        return _not_found(name)
    return ServiceResult(
        success=True,
        message=f"Brain {name!r} unregistered",
        code="brain_unregistered",
        data={"name": name},
    )


def set_registered_brain_flags(
    name: str,
    *,
    federated: bool | None = None,
    sensitive: bool | None = None,
    home: Path | None = None,
) -> ServiceResult[BrainItem]:
    if federated is None and sensitive is None:
        return ServiceResult(
            success=False,
            message="Nothing to set",
            code="brain_flags_empty",
        )
    try:
        if federated is not None and not set_brain_flag(name, "federated", federated, home=home):
            return _not_found(name)
        if sensitive is not None and not set_brain_flag(name, "sensitive", sensitive, home=home):
            return _not_found(name)
    except (OSError, TypeError, ValueError, AttributeError) as exc:
        return _registry_error(exc)
    return get_brain(name, home=home)


def _home(home: Path | None) -> Path:
    return home or talamus_home()


def _load_registry(home: Path | None) -> Registry | ServiceResult[T]:
    try:
        return load_registry(home)
    except (OSError, TypeError, ValueError, AttributeError) as exc:
        return _registry_error(exc)


def _brain_item(brain: BrainInfo, selected: str) -> BrainItem:
    root = brain.root()
    return BrainItem(
        id=brain.id,
        name=brain.name,
        path=brain.path,
        type=brain.type,
        federated=brain.federated,
        sensitive=brain.sensitive,
        selected=brain.name == selected,
        exists=(root / "talamus.json").exists(),
        notes=_count_notes(root),
        created_at=brain.created_at,
        updated_at=brain.updated_at,
        last_accessed_at=brain.last_accessed_at,
        project=brain.project,
    )


def _count_notes(root: Path) -> int:
    notes = root / "notes"
    if not notes.exists():
        return 0
    return sum(1 for path in notes.glob("*.md") if path.is_file())


def _discover_unregistered(home: Path, registry: Registry) -> list[UnregisteredBrain]:
    if not home.exists():
        return []
    found: list[UnregisteredBrain] = []
    for directory in sorted(home.iterdir()):
        if not directory.is_dir() or not (directory / "talamus.json").exists():
            continue
        if registry.by_path(directory) is not None:
            continue
        found.append(
            UnregisteredBrain(
                name=directory.name,
                path=str(directory.resolve()),
                register_command=f"talamus brains register {directory}",
            )
        )
    return found


def _not_found(name: str) -> ServiceResult[T]:
    return ServiceResult(
        success=False,
        message=f"No brain named {name!r}",
        code="brain_not_found",
    )


def _registry_error(exc: Exception) -> ServiceResult[T]:
    return ServiceResult(
        success=False,
        message=f"Brain registry error: {exc}",
        code="brain_registry_error",
    )
