#!/usr/bin/env python3
"""Scaffold a batch of blank records from a seeds file.

Seeds file format (one per line):
  category | subcategory | difficulty | topic description

Example seeds.txt:
  filtration | backwash_triggers | basic | When to initiate a backwash
  disinfection | chlorine_residual | intermediate | Dropping residual after storm
  safety | chemical_handling | basic | Chlorine gas leak response

Lines starting with # are ignored. Blank lines are ignored.
"""

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

# ---------------------------------------------------------------------------
# Tunable defaults
# ---------------------------------------------------------------------------

DEFAULT_DATA_DIR = Path("data/raw")
SYSTEM_PROMPT_FILE = Path("data/system_prompt.txt")
ID_PREFIX = "wt"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

ID_PATTERN = re.compile(rf"^{re.escape(ID_PREFIX)}-(\d+)$")


def current_max_id(data_dir: Path) -> int:
    """Find the highest existing wt-NNNN number."""
    max_num = 0
    for filepath in data_dir.glob("*.json"):
        try:
            with open(filepath, encoding="utf-8") as f:
                data = json.load(f)
            record_id = data.get("metadata", {}).get("id", "")
            match = ID_PATTERN.match(record_id)
            if match:
                max_num = max(max_num, int(match.group(1)))
        except (json.JSONDecodeError, OSError):
            continue
    return max_num


def load_system_prompt() -> str:
    if SYSTEM_PROMPT_FILE.is_file():
        return SYSTEM_PROMPT_FILE.read_text(encoding="utf-8").strip()
    return "You are an experienced drinking water treatment plant operator."


def parse_seed_line(line: str) -> tuple[str, str, str, str] | None:
    """Parse a seed line into (category, subcategory, difficulty, topic)."""
    line = line.strip()
    if not line or line.startswith("#"):
        return None

    parts = [p.strip() for p in line.split("|")]
    if len(parts) < 3:
        return None

    category = parts[0]
    subcategory = parts[1]
    difficulty = parts[2] if parts[2] in ("basic", "intermediate", "advanced") else "intermediate"
    topic = parts[3] if len(parts) >= 4 else ""

    return category, subcategory, difficulty, topic


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Scaffold blank records from a seeds file"
    )
    parser.add_argument(
        "seeds_file",
        type=Path,
        help="Path to seeds file (one seed per line: category | subcategory | difficulty | topic)",
    )
    parser.add_argument(
        "--path",
        type=Path,
        default=DEFAULT_DATA_DIR,
        help=f"Output directory for records (default: {DEFAULT_DATA_DIR})",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Print what would be created without writing files",
    )
    args = parser.parse_args()

    if not args.seeds_file.is_file():
        print(f"Error: seeds file not found: {args.seeds_file}")
        return 1

    args.path.mkdir(parents=True, exist_ok=True)

    lines = args.seeds_file.read_text(encoding="utf-8").splitlines()
    seeds = [s for s in (parse_seed_line(l) for l in lines) if s is not None]

    if not seeds:
        print("No valid seeds found in file")
        return 0

    system_prompt = load_system_prompt()
    next_num = current_max_id(args.path) + 1
    today = date.today().isoformat()
    created = 0

    for category, subcategory, difficulty, topic in seeds:
        record_id = f"{ID_PREFIX}-{next_num:04d}"

        record = {
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": ""},
                {"role": "assistant", "content": ""},
            ],
            "metadata": {
                "id": record_id,
                "category": category,
                "subcategory": subcategory,
                "difficulty": difficulty,
                "tone": "operator",
                "source_type": "expert_authored",
                "tags": [],
                "review_status": "draft",
                "created_date": today,
                "version": 1,
                "notes": topic,
            },
        }

        filepath = args.path / f"{record_id}.json"

        if args.dry_run:
            print(f"  [dry-run] {record_id}: {category}/{subcategory} ({difficulty}) -- {topic}")
        else:
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(record, f, indent=2, ensure_ascii=False)
                f.write("\n")
            print(f"  Created {filepath.name}: {category}/{subcategory} ({difficulty})")

        next_num += 1
        created += 1

    print(f"\n{'Would create' if args.dry_run else 'Created'}: {created} records")
    return 0


if __name__ == "__main__":
    sys.exit(main())
