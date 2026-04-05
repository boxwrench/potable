# Schema

## Purpose

Potable records are designed to be:

- easy to author and review
- easy to validate automatically
- easy to export into standard fine-tuning formats
- portable across training frameworks and base models

The canonical source format is a metadata envelope wrapped around chat-style messages.

## Canonical Record Shape

```json
{
  "messages": [
    {"role": "system", "content": "You are an experienced drinking water treatment plant operator..."},
    {"role": "user", "content": "How should I respond to rising filter effluent turbidity?"},
    {"role": "assistant", "content": "Start by confirming the trend, checking recent loading changes, and verifying instrument performance..."}
  ],
  "metadata": {
    "id": "wt-0042",
    "category": "filtration",
    "subcategory": "effluent_turbidity_response",
    "difficulty": "intermediate",
    "tone": "operator",
    "source_type": "expert_authored",
    "tags": ["turbidity", "filter", "diagnostics"],
    "review_status": "approved",
    "created_date": "2026-04-03",
    "version": 1,
    "notes": ""
  }
}
```

## Top-Level Fields

### `messages`

Array of chat messages used for training.

Requirements:

- must be an array
- must contain at least one `user` message and one `assistant` message
- usually begins with a `system` message
- each item must include `role` and `content`
- `content` must be a non-empty string

Allowed roles:

- `system`
- `user`
- `assistant`

### `metadata`

Structured fields used for filtering, review, coverage tracking, and versioning.

All records must include a `metadata` object.

## Metadata Fields

### `id`

Unique record identifier.

Rules:

- required
- string
- unique across the dataset
- recommended pattern: `wt-0001`, `wt-0002`, etc.

### `category`

Top-level knowledge area.

Rules:

- required
- string
- must match an allowed taxonomy category

### `subcategory`

More specific topic within a category.

Rules:

- required
- string
- should be stable and snake_case
- should map cleanly to one category

### `difficulty`

Expected complexity of the example.

Recommended values:

- `basic`
- `intermediate`
- `advanced`

### `tone`

Writing style for the assistant response.

Allowed values:

- `formal`
- `operator`
- `conversational`

Default target:

- `operator`

### `source_type`

How the example originated.

Allowed values:

- `expert_authored`
- `ai_generated`
- `ai_assisted`
- `adapted_from_manual`

### `tags`

Keyword list for search, filtering, and later analysis.

Rules:

- array of strings
- use concise technical tags
- prefer lowercase snake_case or simple lowercase terms

### `review_status`

Review state for the record.

Recommended values:

- `draft`
- `reviewed`
- `approved`
- `rejected`

### `created_date`

Date the record was created.

Rules:

- required
- ISO 8601 date format: `YYYY-MM-DD`

### `version`

Record revision number.

Rules:

- required
- integer
- start at `1`
- increment when the record is materially revised

### `notes`

Optional editor or reviewer notes.

Rules:

- string
- may be empty
- not intended for model training

## Example Shape Guidance

Potable supports several example types:

- factual Q&A
- operational reasoning
- calculation walkthroughs
- troubleshooting scenarios
- regulatory interpretation
- multi-turn conversations

Most early records should remain short enough to be reviewed quickly while still preserving reasoning quality.

## Validation Rules

Automated validation should eventually check:

- valid JSON
- required fields present
- `messages` array structure is valid
- allowed `role` values only
- no empty content strings
- valid category enum
- unique `id`
- token length bounds
- allowed values for `tone` and `source_type`

## Export Format

The working format includes metadata. Export scripts should strip metadata when needed and produce plain training examples such as:

```json
{
  "messages": [
    {"role": "system", "content": "..."},
    {"role": "user", "content": "..."},
    {"role": "assistant", "content": "..."}
  ]
}
```

This keeps the authoring format rich while preserving compatibility with common fine-tuning toolchains.
