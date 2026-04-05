#!/usr/bin/env python3
"""Scaffold a new blank Potable Dataset record."""

import argparse
import json
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Tunable defaults
# ---------------------------------------------------------------------------

DEFAULT_DATA_DIR = Path("data/raw")
ID_PREFIX = "wt"                    # prefix for auto-generated IDs
SYSTEM_PROMPT_FILE = Path("data/system_prompt.txt")

# Allowed values (from TAXONOMY.md / SCHEMA.md)
ALLOWED_CATEGORIES = sorted([
    "water_source", "coagulation_flocculation", "sedimentation", "filtration",
    "disinfection", "corrosion_control", "taste_and_odor", "plant_operations",
    "laboratory", "safety", "regulations", "math_and_calculations",
    "equipment_and_maintenance", "distribution", "troubleshooting",
    "emergency_response", "handpumps_and_boreholes", "spring_and_well_protection",
    "small_piped_systems", "solar_pumping", "household_treatment",
    "point_of_use_chlorination", "rainwater_harvesting",
    "water_quality_field_testing", "sanitation_basics", "hygiene_promotion",
    "seasonal_operations", "supply_chain_and_maintenance",
    "community_governance", "disease_and_health",
])

ALLOWED_DIFFICULTIES = ["basic", "intermediate", "advanced"]

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

ID_PATTERN = re.compile(rf"^{re.escape(ID_PREFIX)}-(\d+)$")


def next_id(data_dir: Path) -> str:
    """Find the highest existing wt-NNNN id and return the next one."""
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
    return f"{ID_PREFIX}-{max_num + 1:04d}"


def load_system_prompt() -> str:
    """Load the canonical system prompt, or return a placeholder."""
    if SYSTEM_PROMPT_FILE.is_file():
        return SYSTEM_PROMPT_FILE.read_text(encoding="utf-8").strip()
    return "You are an experienced drinking water treatment plant operator."


def pick_from_list(prompt: str, options: list[str]) -> str:
    """Interactive picker for a list of options."""
    print(f"\n{prompt}")
    for i, opt in enumerate(options, 1):
        print(f"  {i:>2}. {opt}")
    while True:
        choice = input(f"\nEnter number (1-{len(options)}): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]
        print("Invalid choice, try again.")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(description="Scaffold a new Potable record")
    parser.add_argument(
        "--path",
        type=Path,
        default=DEFAULT_DATA_DIR,
        help=f"Directory for record files (default: {DEFAULT_DATA_DIR})",
    )
    parser.add_argument("--category", choices=ALLOWED_CATEGORIES, help="Category")
    parser.add_argument("--subcategory", help="Subcategory (snake_case)")
    parser.add_argument("--difficulty", choices=ALLOWED_DIFFICULTIES, help="Difficulty")
    parser.add_argument(
        "--non-interactive", action="store_true",
        help="Skip interactive prompts, use defaults for missing fields",
    )
    args = parser.parse_args()

    data_dir: Path = args.path
    data_dir.mkdir(parents=True, exist_ok=True)

    record_id = next_id(data_dir)
    system_prompt = load_system_prompt()

    # Category
    if args.category:
        category = args.category
    elif not args.non_interactive:
        category = pick_from_list("Select category:", ALLOWED_CATEGORIES)
    else:
        category = "CATEGORY_HERE"

    # Subcategory
    if args.subcategory:
        subcategory = args.subcategory
    elif not args.non_interactive:
        subcategory = input("\nSubcategory (snake_case): ").strip()
        if not subcategory:
            subcategory = "SUBCATEGORY_HERE"
    else:
        subcategory = "SUBCATEGORY_HERE"

    # Difficulty
    if args.difficulty:
        difficulty = args.difficulty
    elif not args.non_interactive:
        difficulty = pick_from_list("Select difficulty:", ALLOWED_DIFFICULTIES)
    else:
        difficulty = "intermediate"

    # Build record
    from datetime import date
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
            "created_date": date.today().isoformat(),
            "version": 1,
            "notes": "",
        },
    }

    filename = f"{record_id}.json"
    filepath = data_dir / filename
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(record, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"\nCreated: {filepath}")
    print(f"ID:      {record_id}")
    print(f"Next:    fill in the user and assistant message content")

    return 0


if __name__ == "__main__":
    sys.exit(main())
