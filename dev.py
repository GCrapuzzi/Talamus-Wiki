"""Dev checks for Talamus: lint, format, type-check, tests.

Usage:
    python dev.py          run all checks (lint, format, types, tests)
    python dev.py --fix    autofix lint + format first, then run all checks
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"


def _env() -> dict[str, str]:
    env = os.environ.copy()
    pythonpath = env.get("PYTHONPATH")
    env["PYTHONPATH"] = str(SRC) if not pythonpath else f"{SRC}{os.pathsep}{pythonpath}"
    return env


def run(cmd: list[str]) -> int:
    print(f"\n$ {' '.join(cmd)}", flush=True)
    return subprocess.call(cmd, cwd=ROOT, env=_env())


def main() -> int:
    if "--fix" in sys.argv:
        run(["ruff", "check", "--fix", "src", "tests"])
        run(["ruff", "format", "src", "tests"])

    checks = [
        ["ruff", "check", "src", "tests"],
        ["ruff", "format", "--check", "src", "tests"],
        ["mypy", "src"],
        [sys.executable, "-m", "unittest", "discover", "-s", "tests"],
    ]
    failed = 0
    for cmd in checks:
        if run(cmd) != 0:
            failed = 1
    print("\nALL GREEN" if failed == 0 else "\nFAILED", flush=True)
    return failed


if __name__ == "__main__":
    raise SystemExit(main())
