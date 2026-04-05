#!/usr/bin/env python3
"""Export Potable Dataset records to clean training JSONL."""

import argparse
import json
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Tunable defaults
# ---------------------------------------------------------------------------

DEFAULT_DATA_DIR = Path("data/raw")
DEFAULT_OUTPUT = Path("data/exports/potable_train.jsonl")
DEFAULT_STATUS = "approved"  # only export approved records by default
SYSTEM_PROMPT_FILE = Path("data/system_prompt.txt")

# ---------------------------------------------------------------------------
# Export logic
# ---------------------------------------------------------------------------


def load_system_prompt(path: Path) -> str | None:
    """Load the canonical system prompt if the file exists."""
    if path.is_file():
        return path.read_text(encoding="utf-8").strip()
    return None


def ensure_system_message(messages: list[dict], system_prompt: str) -> list[dict]:
    """Prepend system message if the record doesn't already have one."""
    if messages and messages[0].get("role") == "system":
        return messages
    return [{"role": "system", "content": system_prompt}] + messages


def load_record(filepath: Path) -> dict | None:
    try:
        with open(filepath, encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        print(f"SKIP {filepath.name}: {e}", file=sys.stderr)
        return None


def matches_filters(
    metadata: dict,
    status: str | None,
    category: str | None,
    difficulty: str | None,
    min_version: int | None,
) -> bool:
    if status and metadata.get("review_status") != status:
        return False
    if category and metadata.get("category") != category:
        return False
    if difficulty and metadata.get("difficulty") != difficulty:
        return False
    if min_version is not None:
        v = metadata.get("version", 0)
        if not isinstance(v, int) or v < min_version:
            return False
    return True


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Export Potable records to clean training JSONL"
    )
    parser.add_argument(
        "--path",
        type=Path,
        default=DEFAULT_DATA_DIR,
        help=f"Directory containing .json record files (default: {DEFAULT_DATA_DIR})",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"Output JSONL file path (default: {DEFAULT_OUTPUT})",
    )
    parser.add_argument(
        "--status",
        default=DEFAULT_STATUS,
        help=f"Filter by review_status (default: {DEFAULT_STATUS}). Use 'any' to skip.",
    )
    parser.add_argument("--category", default=None, help="Filter by category")
    parser.add_argument("--difficulty", default=None, help="Filter by difficulty")
    parser.add_argument(
        "--min-version", type=int, default=None, help="Minimum version number"
    )
    parser.add_argument(
        "--inject-system-prompt", action="store_true",
        help="Inject canonical system prompt into records missing a system message",
    )
    args = parser.parse_args()

    data_dir: Path = args.path
    if not data_dir.is_dir():
        print(f"Error: directory not found: {data_dir}")
        return 1

    files = sorted(data_dir.glob("*.json"))
    if not files:
        print(f"No .json files found in {data_dir}")
        return 0

    status_filter = None if args.status == "any" else args.status

    system_prompt = None
    if args.inject_system_prompt:
        system_prompt = load_system_prompt(SYSTEM_PROMPT_FILE)
        if system_prompt is None:
            print(f"Error: --inject-system-prompt requires {SYSTEM_PROMPT_FILE}")
            return 1

    # Ensure output directory exists
    args.output.parent.mkdir(parents=True, exist_ok=True)

    exported = 0
    skipped = 0

    with open(args.output, "w", encoding="utf-8") as out:
        for filepath in files:
            record = load_record(filepath)
            if record is None:
                skipped += 1
                continue

            metadata = record.get("metadata", {})
            if not matches_filters(
                metadata, status_filter, args.category, args.difficulty, args.min_version
            ):
                skipped += 1
                continue

            messages = record.get("messages")
            if not isinstance(messages, list):
                skipped += 1
                continue

            if system_prompt:
                messages = ensure_system_message(messages, system_prompt)

            export_obj = {"messages": messages}
            out.write(json.dumps(export_obj, ensure_ascii=False) + "\n")
            exported += 1

    print(f"Exported: {exported}")
    print(f"Skipped:  {skipped}")
    print(f"Output:   {args.output}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
