#!/usr/bin/env python3
"""Scaffold a new blank Potable Dataset record interactively."""

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

# Keep in sync with TAXONOMY.md and validate.py
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


def next_id(data_dir: Path) -> str:
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
    return f"{ID_PREFIX}-{max_num + 1:04d}"


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
    parser = argparse.ArgumentParser(description="Scaffold a new Potable record")
    parser.add_argument(
        "--path", type=Path, default=DEFAULT_DATA_DIR,
        help=f"Directory for record files (default: {DEFAULT_DATA_DIR})",
    )
    args = parser.parse_args()

    data_dir: Path = args.path
    data_dir.mkdir(parents=True, exist_ok=True)

    category = pick("Select category:", ALLOWED_CATEGORIES)

    subcategory = input("\nSubcategory (snake_case): ").strip()
    if not subcategory:
        subcategory = "SUBCATEGORY_HERE"

    difficulty = pick("Select difficulty:", ALLOWED_DIFFICULTIES)

    tags_raw = input("\nTags (comma-separated, or enter to skip): ").strip()
    tags = [t.strip() for t in tags_raw.split(",") if t.strip()] if tags_raw else []

    record_id = next_id(data_dir)
    system_prompt = load_system_prompt()

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
            "tags": tags,
            "review_status": "draft",
            "created_date": date.today().isoformat(),
            "version": 1,
            "notes": "",
        },
    }

    filepath = data_dir / f"{record_id}.json"
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(record, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"\nCreated : {filepath}")
    print(f"ID      : {record_id}")
    print(f"Next    : fill in the user and assistant message content, then run make validate")
    return 0


if __name__ == "__main__":
    sys.exit(main())
