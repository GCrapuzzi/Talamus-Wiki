from __future__ import annotations

import argparse
import shutil
import subprocess
from dataclasses import dataclass


@dataclass(frozen=True)
class CheckResult:
    name: str
    ok: bool
    detail: str

    def status_text(self) -> str:
        status = "OK" if self.ok else "MISSING"
        return f"{status}: {self.name} - {self.detail}"


def check_cli(name: str, command: str) -> CheckResult:
    found = shutil.which(command)
    if found:
        return CheckResult(name, True, found)
    return CheckResult(name, False, f"{command} not found on PATH")


def check_ollama_model(model_name: str = "glm-ocr") -> CheckResult:
    try:
        result = subprocess.run(
            ["ollama", "list"],
            check=False,
            capture_output=True,
            text=True,
            timeout=15,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return CheckResult("GLM-OCR model", False, f"could not run ollama list: {exc}")

    if result.returncode != 0:
        detail = result.stderr.strip() or f"ollama list exited with {result.returncode}"
        return CheckResult("GLM-OCR model", False, detail)

    if model_name.lower() in result.stdout.lower():
        return CheckResult("GLM-OCR model", True, f"{model_name} found in ollama list")
    return CheckResult("GLM-OCR model", False, f"{model_name} not found in ollama list")


def run_preflight(glm_ocr_model: str = "glm-ocr") -> list[CheckResult]:
    return [
        check_cli("Claude Code", "claude"),
        check_cli("Codex CLI", "codex"),
        check_cli("Ollama", "ollama"),
        check_ollama_model(glm_ocr_model),
        check_cli("Graphify", "graphify"),
        check_cli("Git", "git"),
    ]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check local engines for the FDE Brain pipeline.")
    parser.add_argument("--glm-ocr-model", default="glm-ocr", help="Ollama model name for GLM-OCR.")
    args = parser.parse_args(argv)

    results = run_preflight(args.glm_ocr_model)
    for result in results:
        print(result.status_text())

    return 0 if all(result.ok for result in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
