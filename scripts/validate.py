#!/usr/bin/env python3
"""Validate Potable Dataset records against the schema."""

import argparse
import json
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Tunable defaults — adjust these as the project evolves
# ---------------------------------------------------------------------------

MIN_TOKEN_ESTIMATE = 50       # warn below this (chars / 4 heuristic)
MAX_TOKEN_ESTIMATE = 4096     # error above this
TOKEN_DIVISOR = 4             # rough chars-to-tokens approximation
DEFAULT_DATA_DIR = Path("data/raw")

# ---------------------------------------------------------------------------
# Allowed enum values (from SCHEMA.md and TAXONOMY.md)
# ---------------------------------------------------------------------------

ALLOWED_ROLES = {"system", "user", "assistant"}

ALLOWED_CATEGORIES = {
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
}

ALLOWED_DIFFICULTIES = {"basic", "intermediate", "advanced"}
ALLOWED_TONES = {"formal", "operator", "conversational"}
ALLOWED_SOURCE_TYPES = {
    "expert_authored",
    "ai_generated",
    "ai_assisted",
    "adapted_from_manual",
}
ALLOWED_REVIEW_STATUSES = {"draft", "reviewed", "approved", "rejected"}

ISO_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

# ---------------------------------------------------------------------------
# Validation logic
# ---------------------------------------------------------------------------


def estimate_tokens(char_count: int) -> int:
    return char_count // TOKEN_DIVISOR


def validate_record(filepath: Path, data: dict, seen_ids: set[str]) -> tuple[list[str], list[str]]:
    """Return (errors, warnings) for a single record."""
    errors: list[str] = []
    warnings: list[str] = []

    # --- messages -----------------------------------------------------------
    messages = data.get("messages")
    if not isinstance(messages, list):
        errors.append("'messages' must be an array")
        return errors, warnings

    if len(messages) == 0:
        errors.append("'messages' array is empty")
        return errors, warnings

    has_user = False
    has_assistant = False
    total_chars = 0

    for i, msg in enumerate(messages):
        prefix = f"messages[{i}]"
        if not isinstance(msg, dict):
            errors.append(f"{prefix}: must be an object")
            continue

        role = msg.get("role")
        if role not in ALLOWED_ROLES:
            errors.append(f"{prefix}: invalid role '{role}' (allowed: {sorted(ALLOWED_ROLES)})")
        else:
            if role == "user":
                has_user = True
            elif role == "assistant":
                has_assistant = True

        content = msg.get("content")
        if not isinstance(content, str) or content.strip() == "":
            errors.append(f"{prefix}: 'content' must be a non-empty string")
        else:
            total_chars += len(content)

    if not has_user:
        errors.append("'messages' must contain at least one 'user' message")
    if not has_assistant:
        errors.append("'messages' must contain at least one 'assistant' message")

    token_est = estimate_tokens(total_chars) if total_chars else 0
    if total_chars and token_est < MIN_TOKEN_ESTIMATE:
        warnings.append(
            f"estimated {token_est} tokens (below minimum {MIN_TOKEN_ESTIMATE})"
        )
    if token_est > MAX_TOKEN_ESTIMATE:
        errors.append(
            f"estimated {token_est} tokens (exceeds maximum {MAX_TOKEN_ESTIMATE})"
        )

    # --- metadata -----------------------------------------------------------
    metadata = data.get("metadata")
    if not isinstance(metadata, dict):
        errors.append("'metadata' must be an object")
        return errors, warnings

    # Required fields
    record_id = metadata.get("id")
    if not isinstance(record_id, str) or record_id.strip() == "":
        errors.append("metadata.id: must be a non-empty string")
    else:
        if record_id in seen_ids:
            errors.append(f"metadata.id: duplicate id '{record_id}'")
        seen_ids.add(record_id)

    category = metadata.get("category")
    if not isinstance(category, str) or category.strip() == "":
        errors.append("metadata.category: required")
    elif category not in ALLOWED_CATEGORIES:
        errors.append(
            f"metadata.category: '{category}' not in allowed categories"
        )

    subcategory = metadata.get("subcategory")
    if not isinstance(subcategory, str) or subcategory.strip() == "":
        errors.append("metadata.subcategory: required")

    created_date = metadata.get("created_date")
    if not isinstance(created_date, str) or created_date.strip() == "":
        errors.append("metadata.created_date: required")
    elif not ISO_DATE_RE.match(created_date):
        errors.append(
            f"metadata.created_date: '{created_date}' is not YYYY-MM-DD"
        )

    version = metadata.get("version")
    if not isinstance(version, int) or version < 1:
        errors.append("metadata.version: must be a positive integer")

    # Optional enum fields
    difficulty = metadata.get("difficulty")
    if difficulty is not None and difficulty not in ALLOWED_DIFFICULTIES:
        errors.append(
            f"metadata.difficulty: '{difficulty}' not in {sorted(ALLOWED_DIFFICULTIES)}"
        )

    tone = metadata.get("tone")
    if tone is not None and tone not in ALLOWED_TONES:
        errors.append(
            f"metadata.tone: '{tone}' not in {sorted(ALLOWED_TONES)}"
        )

    source_type = metadata.get("source_type")
    if source_type is not None and source_type not in ALLOWED_SOURCE_TYPES:
        errors.append(
            f"metadata.source_type: '{source_type}' not in {sorted(ALLOWED_SOURCE_TYPES)}"
        )

    review_status = metadata.get("review_status")
    if review_status is not None and review_status not in ALLOWED_REVIEW_STATUSES:
        errors.append(
            f"metadata.review_status: '{review_status}' not in {sorted(ALLOWED_REVIEW_STATUSES)}"
        )

    tags = metadata.get("tags")
    if tags is not None:
        if not isinstance(tags, list):
            errors.append("metadata.tags: must be an array")
        else:
            for j, tag in enumerate(tags):
                if not isinstance(tag, str):
                    errors.append(f"metadata.tags[{j}]: must be a string")

    notes = metadata.get("notes")
    if notes is not None and not isinstance(notes, str):
        errors.append("metadata.notes: must be a string")

    return errors, warnings


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Potable Dataset records")
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

    seen_ids: set[str] = set()
    total_errors = 0
    total_warnings = 0

    for filepath in files:
        try:
            with open(filepath, encoding="utf-8") as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"ERROR {filepath.name}: invalid JSON — {e}")
            total_errors += 1
            continue

        errors, warnings = validate_record(filepath, data, seen_ids)

        for err in errors:
            print(f"ERROR {filepath.name}: {err}")
        for warn in warnings:
            print(f"WARN  {filepath.name}: {warn}")

        total_errors += len(errors)
        total_warnings += len(warnings)

    print(f"\n--- Validation summary ---")
    print(f"Files checked: {len(files)}")
    print(f"Errors: {total_errors}")
    print(f"Warnings: {total_warnings}")

    return 1 if total_errors > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
