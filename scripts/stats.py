#!/usr/bin/env python3
"""Print coverage statistics for the Potable Dataset (approved records only)."""

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

# ---------------------------------------------------------------------------
# Taxonomy — keep in sync with TAXONOMY.md and validate.py
# ---------------------------------------------------------------------------

ALL_CATEGORIES = [
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

COVERAGE_TARGET = 10   # flag categories below this count

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Potable Dataset coverage report (approved records)"
    )
    parser.add_argument(
        "--path", type=Path, default=Path("data/raw"),
        help="Directory containing .json record files",
    )
    args = parser.parse_args()

    data_dir: Path = args.path
    if not data_dir.is_dir():
        print(f"Error: directory not found: {data_dir}")
        return 1

    files = sorted(data_dir.glob("*.json"))

    category_counts: Counter[str] = Counter()
    source_counts: Counter[str] = Counter()
    difficulty_counts: Counter[str] = Counter()
    total = 0
    non_approved = 0

    for filepath in files:
        try:
            with open(filepath, encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, OSError):
            continue

        metadata = data.get("metadata", {})
        if metadata.get("review_status") != "approved":
            non_approved += 1
            continue

        total += 1
        category_counts[metadata.get("category", "unknown")] += 1
        source_counts[metadata.get("source_type", "unknown")] += 1
        difficulty_counts[metadata.get("difficulty", "unknown")] += 1

    # --- Header ---
    print("=" * 54)
    print("  Potable Dataset — Coverage Report (approved only)")
    print("=" * 54)
    print(f"\n  Approved records : {total}")
    print(f"  Non-approved     : {non_approved} (draft/reviewed/rejected)")

    # --- By category ---
    print("\nBy Category")
    print("-" * 54)
    col = max(len(c) for c in ALL_CATEGORIES)
    for cat in ALL_CATEGORIES:
        count = category_counts.get(cat, 0)
        flag = "  *** below target" if count < COVERAGE_TARGET else ""
        print(f"  {cat:<{col}}  {count:>4}{flag}")

    # --- By source type ---
    print("\nBy Source Type")
    print("-" * 34)
    for src in ["expert_authored", "ai_assisted", "adapted_from_manual", "ai_generated"]:
        print(f"  {src:<25}  {source_counts.get(src, 0):>4}")

    # --- By difficulty ---
    print("\nBy Difficulty")
    print("-" * 26)
    for diff in ["basic", "intermediate", "advanced"]:
        print(f"  {diff:<15}  {difficulty_counts.get(diff, 0):>4}")

    # --- Gap summary ---
    gaps = [c for c in ALL_CATEGORIES if category_counts.get(c, 0) < COVERAGE_TARGET]
    print(f"\nCategories below target ({COVERAGE_TARGET}): {len(gaps)} of {len(ALL_CATEGORIES)}")
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
