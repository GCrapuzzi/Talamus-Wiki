"""Time the local judge on THIS machine, then recommend judge roles.

Run BEFORE committing to local-primary vs invert (the brainstorm 'calibrate
then decide' gate). Each call mimics a real one-word faithfulness verdict."""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

_PROMPT = (
    "You are a strict fact-checker. Reply with ONE word: GROUNDED or HALLUCINATED.\n\n"
    "CONTEXT:\nThe sky scatters blue light.\n\nANSWER:\nThe sky is blue."
)


def calibrate(judge_llm, n: int = 5, threshold_s: float = 8.0) -> dict:
    start = time.perf_counter()
    for _ in range(n):
        judge_llm.complete(_PROMPT)
    elapsed = time.perf_counter() - start
    per_call = elapsed / max(n, 1)
    return {
        "calls": n,
        "seconds_per_call": round(per_call, 2),
        "threshold_s": threshold_s,
        "recommend": "local-primary" if per_call < threshold_s else "invert",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Calibrate the local judge")
    parser.add_argument("--model", default="gemma4:e4b")
    parser.add_argument("--n", type=int, default=5)
    parser.add_argument("--threshold", type=float, default=8.0)
    args = parser.parse_args(argv)
    from talamus.adapters.llm import OllamaProvider

    judge = OllamaProvider(args.model, options={"num_predict": 5, "temperature": 0.0})
    out = calibrate(judge, n=args.n, threshold_s=args.threshold)
    print(
        f"gemma judge: {out['seconds_per_call']}s/call over {out['calls']} calls "
        f"→ recommend {out['recommend']} (threshold {out['threshold_s']}s)",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
