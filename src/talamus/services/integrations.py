from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, TypeVar

from talamus.services.result import ServiceResult

T = TypeVar("T")


@dataclass(frozen=True)
class IntegrationReport:
    root: str
    mcp_config_path: str
    mcp_installed: bool
    hook_command: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class McpInstallResult:
    config_path: str
    server_name: str
    command: str
    args: list[str]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class HookSnippet:
    command: str
    settings: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def inspect_integrations(root: str | Path) -> ServiceResult[IntegrationReport]:
    root_path = Path(root)
    try:
        report = IntegrationReport(
            root=str(root_path),
            mcp_config_path=str(_mcp_config_path(root_path)),
            mcp_installed=_mcp_installed(root_path),
            hook_command=_hook_command(root_path),
        )
    except (OSError, TypeError, ValueError, AttributeError, json.JSONDecodeError) as exc:
        return _integration_error(exc)
    return ServiceResult(
        success=True,
        message="Integration status loaded",
        code="integrations_status_loaded",
        data=report,
    )


def install_mcp_config(root: str | Path) -> ServiceResult[McpInstallResult]:
    root_path = Path(root)
    config_path = _mcp_config_path(root_path)
    args = ["--root", str(root_path)]
    try:
        data = _read_mcp_config(config_path)
        servers = data.get("mcpServers")
        if not isinstance(servers, dict):
            servers = {}
            data["mcpServers"] = servers
        servers["talamus"] = {
            "command": "talamus-mcp",
            "args": args,
        }
        config_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    except (OSError, TypeError, ValueError, AttributeError, json.JSONDecodeError) as exc:
        return _integration_error(exc)
    return ServiceResult(
        success=True,
        message=f"wrote talamus MCP server to {config_path}",
        code="mcp_config_installed",
        data=McpInstallResult(
            config_path=str(config_path),
            server_name="talamus",
            command="talamus-mcp",
            args=args,
        ),
    )


def build_hook_snippet(root: str | Path) -> ServiceResult[HookSnippet]:
    root_path = Path(root)
    command = _hook_command(root_path)
    settings = {
        "hooks": {
            "SessionEnd": [
                {
                    "hooks": [
                        {
                            "type": "command",
                            "command": command,
                        }
                    ]
                }
            ]
        }
    }
    return ServiceResult(
        success=True,
        message="Hook snippet built",
        code="hook_snippet_built",
        data=HookSnippet(command=command, settings=settings),
    )


def _mcp_config_path(root: Path) -> Path:
    return root / ".mcp.json"


def _hook_command(root: Path) -> str:
    return f"talamus hook-run --root {root}"


def _read_mcp_config(config_path: Path) -> dict[str, Any]:
    if not config_path.exists():
        return {}
    try:
        data = json.loads(config_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    return data if isinstance(data, dict) else {}


def _mcp_installed(root: Path) -> bool:
    data = _read_mcp_config(_mcp_config_path(root))
    servers = data.get("mcpServers")
    if not isinstance(servers, dict):
        return False
    talamus = servers.get("talamus")
    return isinstance(talamus, dict) and talamus.get("command") == "talamus-mcp"


def _integration_error(exc: Exception) -> ServiceResult[T]:
    return ServiceResult(
        success=False,
        message=f"Integration service error: {exc}",
        code="integration_service_error",
    )
