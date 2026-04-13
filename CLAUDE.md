# Potable — Project Instructions for Claude Code

## What this project is

Potable is an open water-treatment AI project. The core asset is an expert-curated fine-tuning dataset for drinking water treatment operations. The dataset trains PotableLM, a domain-adapted model family.

Two tracks: municipal (licensed plant operators, Gemma 4 31B Dense) and developing regions (community water workers, small models, offline).

## Key files

- `SCHEMA.md` — canonical record shape, field definitions, validation rules
- `TAXONOMY.md` — allowed categories and subcategories (municipal + developing regions)
- `STYLE_GUIDE.md` — operator voice principles, response patterns, what to avoid
- `ANNOTATION_GUIDE.md` — record creation workflow, classification rules, quality bar
- `data/system_prompt.txt` — canonical system prompt used in all records

Read these before creating or editing dataset records.

## Dataset record format

One `.json` file per record in `data/raw/`. Shape:

```json
{
  "messages": [
    {"role": "system", "content": "..."},
    {"role": "user", "content": "..."},
    {"role": "assistant", "content": "..."}
  ],
  "metadata": {
    "id": "wt-0001",
    "category": "filtration",
    "subcategory": "effluent_turbidity_response",
    "difficulty": "intermediate",
    "tone": "operator",
    "source_type": "expert_authored",
    "tags": ["turbidity", "filter"],
    "review_status": "draft",
    "created_date": "2026-04-05",
    "version": 1,
    "notes": ""
  }
}
```

## Conventions

- Pure stdlib Python 3.10+, no external dependencies
- IDs follow `wt-NNNN` pattern, auto-incremented by scripts
- One record per file, filename matches ID (e.g., `wt-0001.json`)
- Subcategory values must be snake_case; categories follow TAXONOMY.md exactly (two use mixed case)
- Dates are ISO 8601 (YYYY-MM-DD)
- System prompt comes from `data/system_prompt.txt` — do not hardcode different versions in records

## Toolchain

| Command | Purpose |
|---------|---------|
| `python scripts/validate.py` | Validate all records against schema |
| `python scripts/export.py` | Export approved records to training JSONL |
| `python scripts/stats.py` | Coverage report with gap detection |
| `python scripts/eval.py -v` | Run golden eval set |
| `python scripts/new_record.py` | Scaffold a new blank record (interactive) |
| `python scripts/batch_scaffold.py <seeds>` | Batch scaffold from seeds file |

Always run `validate.py` after creating or editing records.

## Enum values

### Categories (municipal — 16 total)
water_source_and_reservoir_management, groundwater, coagulation_flocculation_and_sedimentation, pH_and_alkalinity, filtration, disinfection_and_oxidation, distribution_nitrification_and_corrosion, regulations, operational_procedure_and_process_management, systems_integration_and_equipment_behavior, SCADA_and_controls_infrastructure, analyzers_and_instrumentation, measurement_reliability_and_field_analysis, chemical_feed_and_chemical_treatment, emergency_response, external_events_and_non_routine_operations

Note: `pH_and_alkalinity` and `SCADA_and_controls_infrastructure` use mixed case intentionally. All other categories and all subcategories are snake_case.

### Other enums
- difficulty: basic, intermediate, advanced
- tone: formal, operator, conversational (default: operator)
- source_type: expert_authored, ai_generated, ai_assisted, adapted_from_manual
- review_status: draft, reviewed, approved, rejected

## Writing assistant responses

Follow the style guide. Key rules:
- Lead with the answer, not background
- Sound like a senior operator talking to a coworker
- Be specific — concrete checks, likely causes, next actions
- Respect uncertainty — say when it depends on plant config or local rules
- Include safety/compliance notes where relevant
- No generic AI phrasing ("As an AI", "It is important to note", "There are several factors")

## When editing scripts

- Keep the taxonomy and enum sets in sync across `validate.py`, `new_record.py`, `batch_scaffold.py`, and `stats.py` if categories change
- CI runs `validate.py` on push/PR — don't break it

## Golden eval cases

Eval cases live in `data/eval/` as JSON files. They test model output quality, not training data. Do not mix eval cases with training records. Eval cases use `must_contain` and `must_not_contain` keyword checks.
