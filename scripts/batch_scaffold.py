#!/usr/bin/env python3
"""Scaffold a batch of records from a seeds file.

Seeds file format: one scenario description per line.
Lines starting with # and blank lines are skipped.
One .json record is created per scenario. The scenario description
is stored in metadata.notes as a writing prompt for the author.

Usage:
    python scripts/batch_scaffold.py data/seeds/my_seeds.txt
    python scripts/batch_scaffold.py data/seeds/my_seeds.txt --dry-run
"""

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

# ---------------------------------------------------------------------------
# Defaults
# ---------------------------------------------------------------------------

DEFAULT_DATA_DIR = Path("data/raw")
SYSTEM_PROMPT_FILE = Path("data/system_prompt.txt")
ID_PREFIX = "wt"

ALLOWED_CATEGORIES = [
    "water_source_and_reservoir_management",
    "groundwater",
    "coagulation_flocculation_and_sedimentation",
    "pH_and_alkalinity",
    "filtration",
    "disinfection_and_oxidation",
    "distribution_nitrification_and_corrosion",
    "regulations",
    "operational_procedure_and_process_management",
    "systems_integration_and_equipment_behavior",
    "SCADA_and_controls_infrastructure",
    "analyzers_and_instrumentation",
    "measurement_reliability_and_field_analysis",
    "chemical_feed_and_chemical_treatment",
    "emergency_response",
    "external_events_and_non_routine_operations",
]

ALLOWED_DIFFICULTIES = ["basic", "intermediate", "advanced"]

ID_PATTERN = re.compile(rf"^{re.escape(ID_PREFIX)}-(\d+)$")

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def current_max_id(data_dir: Path) -> int:
    max_num = 0
    for filepath in data_dir.glob("*.json"):
        try:
            with open(filepath, encoding="utf-8") as f:
                data = json.load(f)
            record_id = data.get("metadata", {}).get("id", "")
            m = ID_PATTERN.match(record_id)
            if m:
                max_num = max(max_num, int(m.group(1)))
        except (json.JSONDecodeError, OSError):
            continue
    return max_num


def load_system_prompt() -> str:
    if SYSTEM_PROMPT_FILE.is_file():
        return SYSTEM_PROMPT_FILE.read_text(encoding="utf-8").strip()
    return "You are an experienced drinking water treatment plant operator."


def pick(prompt: str, options: list[str]) -> str:
    print(f"\n{prompt}")
    for i, opt in enumerate(options, 1):
        print(f"  {i:>2}. {opt}")
    while True:
        raw = input(f"\nEnter number (1-{len(options)}): ").strip()
        if raw.isdigit() and 1 <= int(raw) <= len(options):
            return options[int(raw) - 1]
        print("Invalid choice. Try again.")

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Batch scaffold records from a seeds file"
    )
    parser.add_argument(
        "seeds_file", type=Path,
        help="Path to seeds file (one scenario description per line)",
    )
    parser.add_argument(
        "--path", type=Path, default=DEFAULT_DATA_DIR,
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

    lines = args.seeds_file.read_text(encoding="utf-8").splitlines()
    scenarios = [
        l.strip() for l in lines
        if l.strip() and not l.strip().startswith("#")
    ]

    if not scenarios:
        print("No scenarios found in seeds file.")
        return 0

    print(f"Found {len(scenarios)} scenario(s).")

    category = pick("Select category for this batch:", ALLOWED_CATEGORIES)
    difficulty = pick("Select difficulty for this batch:", ALLOWED_DIFFICULTIES)

    args.path.mkdir(parents=True, exist_ok=True)
    system_prompt = load_system_prompt()
    next_num = current_max_id(args.path) + 1
    today = date.today().isoformat()
    created = 0

    for scenario in scenarios:
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
                "subcategory": "SUBCATEGORY_HERE",
                "difficulty": difficulty,
                "tone": "operator",
                "source_type": "expert_authored",
                "tags": [],
                "review_status": "draft",
                "created_date": today,
                "version": 1,
                "notes": scenario,
            },
        }

        filepath = args.path / f"{record_id}.json"

        if args.dry_run:
            print(f"  [dry-run] {record_id}: {scenario[:70]}")
        else:
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(record, f, indent=2, ensure_ascii=False)
                f.write("\n")
            print(f"  {record_id}: {scenario[:70]}")

        next_num += 1
        created += 1

    print(f"\n{'Would create' if args.dry_run else 'Created'}: {created} record(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
