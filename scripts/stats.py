#!/usr/bin/env python3
"""Print coverage statistics for the Potable Dataset."""

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

# ---------------------------------------------------------------------------
# Tunable defaults
# ---------------------------------------------------------------------------

DEFAULT_DATA_DIR = Path("data/raw")

# Full taxonomy for gap detection (from TAXONOMY.md)
ALL_CATEGORIES = [
    # Municipal track
    "water_source",
    "coagulation_flocculation",
    "sedimentation",
    "filtration",
    "disinfection",
    "corrosion_control",
    "taste_and_odor",
    "plant_operations",
    "laboratory",
    "safety",
    "regulations",
    "math_and_calculations",
    "equipment_and_maintenance",
    "distribution",
    "troubleshooting",
    "emergency_response",
    # Developing regions track
    "handpumps_and_boreholes",
    "spring_and_well_protection",
    "small_piped_systems",
    "solar_pumping",
    "household_treatment",
    "point_of_use_chlorination",
    "rainwater_harvesting",
    "water_quality_field_testing",
    "sanitation_basics",
    "hygiene_promotion",
    "seasonal_operations",
    "supply_chain_and_maintenance",
    "community_governance",
    "disease_and_health",
]

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def print_table(title: str, counts: dict[str, int], all_keys: list[str] | None = None) -> None:
    """Print a simple key-value table with optional zero-fill from all_keys."""
    keys = all_keys if all_keys else sorted(counts.keys())
    if not keys:
        return

    print(f"\n{title}")
    print("-" * (len(title) + 4))

    max_key_len = max(len(k) for k in keys)
    for key in keys:
        count = counts.get(key, 0)
        marker = " <-- gap" if count == 0 and all_keys else ""
        print(f"  {key:<{max_key_len}}  {count:>4}{marker}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Print Potable Dataset coverage statistics"
    )
    parser.add_argument(
        "--path",
        type=Path,
        default=DEFAULT_DATA_DIR,
        help=f"Directory containing .json record files (default: {DEFAULT_DATA_DIR})",
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

    category_counts: Counter[str] = Counter()
    subcategory_counts: Counter[str] = Counter()
    difficulty_counts: Counter[str] = Counter()
    status_counts: Counter[str] = Counter()
    source_counts: Counter[str] = Counter()
    cat_sub_map: dict[str, Counter[str]] = {}
    total = 0
    load_errors = 0

    for filepath in files:
        try:
            with open(filepath, encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, OSError):
            load_errors += 1
            continue

        metadata = data.get("metadata", {})
        total += 1

        cat = metadata.get("category", "unknown")
        sub = metadata.get("subcategory", "unknown")
        category_counts[cat] += 1
        subcategory_counts[sub] += 1
        difficulty_counts[metadata.get("difficulty", "unset")] += 1
        status_counts[metadata.get("review_status", "unset")] += 1
        source_counts[metadata.get("source_type", "unset")] += 1

        if cat not in cat_sub_map:
            cat_sub_map[cat] = Counter()
        cat_sub_map[cat][sub] += 1

    # --- Summary ---
    print("=" * 50)
    print("  Potable Dataset -- Coverage Report")
    print("=" * 50)
    print(f"\nTotal records: {total}")
    if load_errors:
        print(f"Load errors:   {load_errors}")

    # --- By review status ---
    print_table("By Review Status", status_counts)

    # --- By category (with gap detection) ---
    print_table("By Category", category_counts, ALL_CATEGORIES)

    # --- Subcategories grouped by category ---
    print(f"\nBy Subcategory (grouped)")
    print("-" * 30)
    for cat in sorted(cat_sub_map.keys()):
        subs = cat_sub_map[cat]
        print(f"\n  [{cat}]")
        for sub in sorted(subs.keys()):
            print(f"    {sub:<40}  {subs[sub]:>4}")

    # --- By difficulty ---
    print_table("By Difficulty", difficulty_counts)

    # --- By source type ---
    print_table("By Source Type", source_counts)

    # --- Coverage gaps ---
    gaps = [c for c in ALL_CATEGORIES if category_counts.get(c, 0) == 0]
    if gaps:
        print(f"\nCoverage Gaps ({len(gaps)} categories with 0 records)")
        print("-" * 50)
        for g in gaps:
            print(f"  - {g}")

    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
