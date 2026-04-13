#!/usr/bin/env python3
"""Validate Potable Dataset records against the schema."""

import argparse
import json
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Enum definitions — keep in sync with TAXONOMY.md and other scripts
# ---------------------------------------------------------------------------

REQUIRED_METADATA_FIELDS = [
    "id", "category", "subcategory", "difficulty",
    "source_type", "review_status", "created_date",
]

ALLOWED_CATEGORIES = {
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
}

ALLOWED_DIFFICULTIES = {"basic", "intermediate", "advanced"}
ALLOWED_SOURCE_TYPES = {
    "expert_authored", "ai_generated", "ai_assisted", "adapted_from_manual",
}
ALLOWED_REVIEW_STATUSES = {"draft", "reviewed", "approved", "rejected"}

# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------


def validate_record(data: dict) -> list[str]:
    errors: list[str] = []

    # --- messages -----------------------------------------------------------
    messages = data.get("messages")
    if not isinstance(messages, list) or len(messages) == 0:
        errors.append("'messages' must be a non-empty array")
        return errors

    roles = [m.get("role") for m in messages if isinstance(m, dict)]

    # Optional system message must be first
    idx = 0
    if roles and roles[0] == "system":
        idx = 1

    # Remaining messages must alternate user / assistant, starting with user
    expected = "user"
    for role in roles[idx:]:
        if role != expected:
            errors.append(
                f"messages: role order violation — got '{role}', expected '{expected}' "
                f"(must follow system / user / assistant pattern)"
            )
            break
        expected = "assistant" if expected == "user" else "user"

    if "user" not in roles:
        errors.append("messages: no 'user' message found")
    if "assistant" not in roles:
        errors.append("messages: no 'assistant' message found")

    for i, msg in enumerate(messages):
        if not isinstance(msg, dict):
            errors.append(f"messages[{i}]: must be an object")
            continue
        content = msg.get("content", "")
        if not isinstance(content, str) or content.strip() == "":
            errors.append(f"messages[{i}]: 'content' must be a non-empty string")

    # --- metadata -----------------------------------------------------------
    metadata = data.get("metadata")
    if not isinstance(metadata, dict):
        errors.append("'metadata' must be an object")
        return errors

    for field in REQUIRED_METADATA_FIELDS:
        val = metadata.get(field)
        if val is None or (isinstance(val, str) and val.strip() == ""):
            errors.append(f"metadata.{field}: required field is missing or empty")

    category = metadata.get("category", "")
    if category and category not in ALLOWED_CATEGORIES:
        errors.append(
            f"metadata.category: '{category}' is not a valid taxonomy category"
        )

    difficulty = metadata.get("difficulty", "")
    if difficulty and difficulty not in ALLOWED_DIFFICULTIES:
        errors.append(
            f"metadata.difficulty: '{difficulty}' must be one of {sorted(ALLOWED_DIFFICULTIES)}"
        )

    source_type = metadata.get("source_type", "")
    if source_type and source_type not in ALLOWED_SOURCE_TYPES:
        errors.append(
            f"metadata.source_type: '{source_type}' must be one of {sorted(ALLOWED_SOURCE_TYPES)}"
        )

    review_status = metadata.get("review_status", "")
    if review_status and review_status not in ALLOWED_REVIEW_STATUSES:
        errors.append(
            f"metadata.review_status: '{review_status}' must be one of {sorted(ALLOWED_REVIEW_STATUSES)}"
        )

    return errors


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Potable Dataset records")
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
    if not files:
        print(f"No .json files found in {data_dir}")
        return 0

    total_errors = 0

    for filepath in files:
        try:
            with open(filepath, encoding="utf-8") as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"ERROR {filepath.name}: invalid JSON — {e}")
            total_errors += 1
            continue

        errors = validate_record(data)
        for err in errors:
            print(f"ERROR {filepath.name}: {err}")
        total_errors += len(errors)

    print(f"\n--- Validation summary ---")
    print(f"Files checked : {len(files)}")
    print(f"Errors        : {total_errors}")

    return 1 if total_errors > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
