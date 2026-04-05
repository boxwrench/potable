#!/usr/bin/env python3
"""Run golden evaluation set against model outputs.

This script defines the evaluation framework. It does not call a model
directly — instead it compares pre-generated model outputs against
reference answers using configurable criteria.

Workflow:
  1. Author eval cases in data/eval/ (one JSON file per case)
  2. Generate model outputs (manually or via a separate inference script)
     and place them in the eval case under "model_output"
  3. Run this script to score and summarize results

Eval case schema:
  {
    "id": "eval-0001",
    "category": "filtration",
    "question": "...",
    "reference_answer": "...",
    "must_contain": ["keyword1", "keyword2"],
    "must_not_contain": ["banned_phrase"],
    "difficulty": "intermediate",
    "notes": "",
    "model_output": ""       <-- filled after inference
  }
"""

import argparse
import json
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Tunable defaults
# ---------------------------------------------------------------------------

DEFAULT_EVAL_DIR = Path("data/eval")
MIN_OUTPUT_LENGTH = 20        # characters — flag suspiciously short outputs

# ---------------------------------------------------------------------------
# Scoring logic
# ---------------------------------------------------------------------------


def score_case(case: dict) -> dict:
    """Score a single eval case. Returns a result dict."""
    case_id = case.get("id", "unknown")
    question = case.get("question", "")
    reference = case.get("reference_answer", "")
    output = case.get("model_output", "")
    must_contain = case.get("must_contain", [])
    must_not_contain = case.get("must_not_contain", [])

    result = {
        "id": case_id,
        "category": case.get("category", ""),
        "has_output": bool(output.strip()),
        "checks": [],
        "pass_count": 0,
        "fail_count": 0,
        "skip": False,
    }

    if not output.strip():
        result["skip"] = True
        result["checks"].append(("no_output", "SKIP", "No model output provided"))
        return result

    output_lower = output.lower()

    # Length check
    if len(output.strip()) < MIN_OUTPUT_LENGTH:
        result["checks"].append(("min_length", "FAIL", f"Output too short ({len(output.strip())} chars)"))
        result["fail_count"] += 1
    else:
        result["checks"].append(("min_length", "PASS", ""))
        result["pass_count"] += 1

    # Must-contain checks
    for keyword in must_contain:
        if keyword.lower() in output_lower:
            result["checks"].append(("must_contain", "PASS", keyword))
            result["pass_count"] += 1
        else:
            result["checks"].append(("must_contain", "FAIL", f"missing: {keyword}"))
            result["fail_count"] += 1

    # Must-not-contain checks
    for phrase in must_not_contain:
        if phrase.lower() in output_lower:
            result["checks"].append(("must_not_contain", "FAIL", f"found: {phrase}"))
            result["fail_count"] += 1
        else:
            result["checks"].append(("must_not_contain", "PASS", phrase))
            result["pass_count"] += 1

    return result


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Score model outputs against golden eval cases"
    )
    parser.add_argument(
        "--path",
        type=Path,
        default=DEFAULT_EVAL_DIR,
        help=f"Directory containing eval case .json files (default: {DEFAULT_EVAL_DIR})",
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true",
        help="Show per-check details",
    )
    args = parser.parse_args()

    eval_dir: Path = args.path
    if not eval_dir.is_dir():
        print(f"Error: directory not found: {eval_dir}")
        return 1

    files = sorted(eval_dir.glob("*.json"))
    if not files:
        print(f"No .json files found in {eval_dir}")
        return 0

    results = []
    load_errors = 0

    for filepath in files:
        try:
            with open(filepath, encoding="utf-8") as f:
                case = json.load(f)
        except (json.JSONDecodeError, OSError) as e:
            print(f"ERROR {filepath.name}: {e}")
            load_errors += 1
            continue

        result = score_case(case)
        results.append(result)

    # --- Summary ---
    total = len(results)
    skipped = sum(1 for r in results if r["skip"])
    scored = total - skipped
    total_passes = sum(r["pass_count"] for r in results)
    total_fails = sum(r["fail_count"] for r in results)
    total_checks = total_passes + total_fails
    all_passing = sum(1 for r in results if not r["skip"] and r["fail_count"] == 0)

    print("=" * 50)
    print("  Potable -- Golden Eval Results")
    print("=" * 50)

    # Per-case results
    for r in results:
        status = "SKIP" if r["skip"] else ("PASS" if r["fail_count"] == 0 else "FAIL")
        print(f"\n  [{status}] {r['id']} ({r['category']})")

        if args.verbose or r["fail_count"] > 0:
            for check_type, check_status, detail in r["checks"]:
                if check_status != "PASS" or args.verbose:
                    print(f"         {check_status} {check_type}: {detail}")

    # Summary
    print(f"\n{'=' * 50}")
    print(f"  Cases: {total} total, {scored} scored, {skipped} skipped")
    if scored > 0:
        print(f"  Checks: {total_passes}/{total_checks} passed")
        print(f"  Cases passing all checks: {all_passing}/{scored}")
    if load_errors:
        print(f"  Load errors: {load_errors}")
    print(f"{'=' * 50}")

    # Exit non-zero if any scored case has failures
    return 1 if total_fails > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
