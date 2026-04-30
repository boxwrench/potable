# Potable Toolchain v1 — Design Spec

## Overview

Build the validation, export, and reporting toolchain for the Potable Dataset, plus CI and test fixtures. Pure stdlib Python 3.10+, no external dependencies.

## Scripts

### `scripts/validate.py`

Validates all `.json` record files in `data/raw/` (or a specified path) against SCHEMA.md rules.

**Checks:**
- Valid JSON
- Top-level `messages` array present
- `messages` contains at least one `user` and one `assistant` message
- Each message has `role` (one of: system, user, assistant) and non-empty `content`
- Top-level `metadata` object present
- Required metadata fields: `id`, `category`, `subcategory`, `created_date`, `version`
- `id` is a non-empty string, unique across the entire dataset
- `category` is one of the allowed taxonomy values
- `difficulty` is one of: basic, intermediate, advanced
- `tone` is one of: formal, operator, conversational
- `source_type` is one of: expert_authored, ai_generated, ai_assisted, adapted_from_manual
- `review_status` is one of: draft, reviewed, approved, rejected
- `created_date` matches ISO 8601 date format (YYYY-MM-DD)
- `version` is a positive integer
- `tags` is an array of strings (if present)
- `notes` is a string (if present)
- Token-length heuristic: warn if total message content < 50 estimated tokens, error if > 4096

**Token heuristic:** `len(text) / 4` — rough char-to-token approximation. *Tunable default.*

**Output:** Per-file errors and warnings. Exit code 0 if no errors, 1 if any errors. Warnings do not cause failure.

**CLI:** `python scripts/validate.py [--path DATA_DIR]`

### `scripts/export.py`

Reads validated records and produces clean training JSONL (metadata stripped).

**Behavior:**
- Reads all `.json` files from `data/raw/` (or specified path)
- Strips `metadata`, outputs `{"messages": [...]}` lines
- Only exports records with `review_status: "approved"` by default
- Output file: `data/exports/potable_train.jsonl` (or specified path)

**Filter flags:**
- `--status STATUS` — filter by review_status (default: approved)
- `--category CATEGORY` — filter by category
- `--difficulty DIFFICULTY` — filter by difficulty
- `--min-version N` — minimum version number

**CLI:** `python scripts/export.py [--path DATA_DIR] [--output FILE] [--status STATUS] [--category CAT] [--difficulty DIFF] [--min-version N]`

### `scripts/stats.py`

Reads all records and prints a coverage report.

**Output sections:**
- Total record count and breakdown by review_status
- Counts by category (sorted, with zero-count categories from taxonomy shown)
- Counts by subcategory (grouped under category)
- Counts by difficulty
- Counts by source_type
- Coverage gaps: categories with 0 records flagged

**CLI:** `python scripts/stats.py [--path DATA_DIR]`

## Test Fixtures

Located in `data/raw/`:
- 2-3 valid records: minimal but schema-compliant, `review_status: "draft"`, `source_type: "ai_generated"`, placeholder content (not real operator data)
- Purpose: prove the toolchain works end-to-end

## CI Workflow

**`.github/workflows/validate.yml`**
- Triggers on push and pull_request
- Runs `python scripts/validate.py`
- Fails the check if validation returns non-zero

## Conventions

- Pure stdlib Python 3.10+
- All tunable defaults as named constants at top of each script with comments
- One record per `.json` file in `data/raw/`
- Snake_case filenames, standard argparse CLI

## Tunable Defaults (noted for future adjustment)

| Default | Value | Location |
|---------|-------|----------|
| Min token estimate | 50 | validate.py |
| Max token estimate | 4096 | validate.py |
| Token heuristic | len/4 | validate.py |
| Default export status | approved | export.py |
| Data directory | data/raw | all scripts |
| Export output | data/exports/potable_train.jsonl | export.py |
