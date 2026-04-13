# Dev Log

## 2026-04-13

Restructured the municipal taxonomy to 16 domain-organized categories. Updated all toolchain scripts, reference documents, and existing records to match.

- Replaced the previous 16-category flat taxonomy with a new set organized by cognitive task and failure mode independence. Full rationale in TAXONOMY.md.
- Rewrote `validate.py`: checks required metadata fields, validates category against the 16 new values, enforces system/user/assistant message role order, exits non-zero on any error for CI.
- Rewrote `stats.py`: approved-records-only coverage report with per-category counts, below-target flags, source type and difficulty breakdown.
- Rewrote `new_record.py`: interactive numbered category picker, subcategory/difficulty/tags prompts.
- Rewrote `batch_scaffold.py`: reads a seeds file (one scenario description per line), prompts once for category and difficulty for the whole batch.
- Rewrote `TAXONOMY.md`: full definitions, subcategory directions, and design rationale for each category.
- Updated `README.md`: new taxonomy table, two-track model plan, project structure, sponsor section.
- Updated `CLAUDE.md`: new category enum list, removed stale references to Jaccard duplicate detection.
- Reclassified wt-0002 from `math_and_calculations` to `disinfection_and_oxidation`.
- Reclassified wt-0003 from `taste_and_odor` to `water_source_and_reservoir_management`.
- Added sponsor acknowledgment: Robot Garden, Livermore CA (robotgarden.org).
- Decision: `pH_and_alkalinity` and `SCADA_and_controls_infrastructure` use mixed case intentionally. All other categories and all subcategories remain snake_case.

## 2026-04-05

Built the complete dataset toolchain. The project now has working infrastructure for authoring, validating, exporting, and evaluating training data.

- Added `validate.py`: schema validation against all SCHEMA.md rules, token-length heuristic, unique ID checks, Jaccard similarity duplicate detection on user prompts.
- Added `export.py`: strips metadata to produce clean training JSONL. Filters by status, category, difficulty, version. Optional system prompt injection.
- Added `stats.py`: coverage report by category, subcategory, difficulty, source type, review status. Token estimate stats (min/max/mean/median). Gap detection against full taxonomy.
- Added `eval.py`: golden evaluation framework with must_contain/must_not_contain checks. Three starter eval cases (filtration, calculations, disinfection).
- Added `new_record.py`: interactive CLI scaffolder with auto-incrementing IDs and canonical system prompt injection.
- Added `batch_scaffold.py`: batch record creation from a seeds file. Dry-run mode for planning.
- Created `data/system_prompt.txt`: minimal canonical system prompt (two sentences).
- Created `data/seeds/municipal_starter.txt`: 26 planned records across all 16 municipal categories.
- Added GitHub Actions CI workflow (`validate.yml`) to run validation on push/PR.
- Added Makefile with targets for all common operations.
- Added `docs/IDEAS.md` for future exploration directions (facility dataset creation, gamified capture, AutoAgent/Meta-Harness agent frameworks).
- Three test fixture records in `data/raw/` (draft, ai_generated) to prove the toolchain.
- Updated README with current repo layout and toolchain quickstart.
- Added CLAUDE.md with full project instructions for Claude Code sessions.
- Added `.editorconfig` for consistent line endings and indentation.
- Expanded golden eval set to 8 cases covering: filtration, math/calculations, disinfection, safety (confined space entry), regulations (IESWTR turbidity), troubleshooting (multi-filter pattern), plant operations (shift recovery), emergency response (contamination suspicion).
- Decision: one record per `.json` file (better for git diffs and review).
- Decision: pure stdlib Python 3.10+, no external dependencies.
- Decision: minimal system prompt — let fine-tuning internalize voice rather than overloading the system message.
- Decision: eval cases use keyword checks (must_contain/must_not_contain) as the initial scoring method. Semantic scoring deferred until inference pipeline exists.
- Pushed all work to GitHub.
- Next: author real operator content using the seeds file as a guide. Run `python scripts/batch_scaffold.py data/seeds/municipal_starter.txt` to create blank records.

## 2026-04-04

Established the initial public project scaffold for Potable.

- Created the GitHub repository structure.
- Drafted the main project README.
- Drafted a Hugging Face dataset card for Potable Dataset.
- Drafted a Hugging Face model card for PotableLM.
- Added overview and roadmap documents.
- Added dataset reference docs: schema, taxonomy, style guide, annotation guide, and changelog.
- Standardized naming around:
  Project: Potable
  Dataset: Potable Dataset
  Models: PotableLM

## Log Format

Add new entries at the top using this structure:

```md
## YYYY-MM-DD

Short summary sentence.

- concrete change or decision
- concrete change or decision
- open question or next step
```
