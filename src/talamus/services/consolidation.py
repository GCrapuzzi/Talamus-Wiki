from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, TypeVar

from talamus.adapters.llm import LLMProvider
from talamus.consolidate import apply_consolidation, find_duplicates
from talamus.paths import TalamusPaths
from talamus.services.result import ServiceResult

T = TypeVar("T")


@dataclass(frozen=True)
class ConsolidationGroup:
    canonical: str
    members: tuple[str, ...]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class ConsolidationGroupList:
    root: str
    groups: tuple[ConsolidationGroup, ...]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class ConsolidationApplyResult:
    root: str
    merged: int

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def list_consolidation_groups(
    root: str | Path,
    llm: LLMProvider,
) -> ServiceResult[ConsolidationGroupList]:
    root_path = Path(root)
    try:
        groups = _typed_groups(find_duplicates(TalamusPaths(root_path), llm))
    except (OSError, TypeError, ValueError, AttributeError) as exc:
        return _consolidation_error(exc)
    return ServiceResult(
        success=True,
        message="Consolidation groups loaded",
        code="consolidation_groups_loaded",
        data=ConsolidationGroupList(root=str(root_path), groups=groups),
    )


def apply_consolidation_groups(
    root: str | Path,
    llm: LLMProvider,
    groups: list[ConsolidationGroup | dict[str, Any]] | None = None,
) -> ServiceResult[ConsolidationApplyResult]:
    root_path = Path(root)
    try:
        raw_groups = None if groups is None else [_group_to_dict(group) for group in groups]
        merged = apply_consolidation(TalamusPaths(root_path), llm, raw_groups)
    except (OSError, TypeError, ValueError, AttributeError) as exc:
        return _consolidation_error(exc)
    return ServiceResult(
        success=True,
        message="Consolidation applied",
        code="consolidation_applied",
        data=ConsolidationApplyResult(root=str(root_path), merged=merged),
    )


def _typed_groups(groups: list[dict]) -> tuple[ConsolidationGroup, ...]:
    return tuple(_group_from_dict(group) for group in groups)


def _group_from_dict(group: dict[str, Any]) -> ConsolidationGroup:
    members = tuple(str(member) for member in group.get("members", []))
    return ConsolidationGroup(canonical=str(group.get("canonical", "")), members=members)


def _group_to_dict(group: ConsolidationGroup | dict[str, Any]) -> dict[str, Any]:
    if isinstance(group, ConsolidationGroup):
        return {"canonical": group.canonical, "members": list(group.members)}
    return dict(group)


def _consolidation_error(exc: Exception) -> ServiceResult[T]:
    return ServiceResult(
        success=False,
        message=f"Consolidation service error: {exc}",
        code="consolidation_service_error",
    )
