# Changelog

All notable dataset-documentation changes should be recorded here.

## 2026-04-13

- Restructured municipal taxonomy to 16 domain-organized categories (see TAXONOMY.md for full definitions and design rationale)
- Rewrote `validate.py`, `stats.py`, `new_record.py`, `batch_scaffold.py` to use new taxonomy
- Rewrote `TAXONOMY.md` with category definitions, subcategory directions, and design notes
- Updated `README.md`: new taxonomy table, two-track model plan, sponsor acknowledgment (Robot Garden)
- Updated `CLAUDE.md`: new category enum list, removed stale script notes
- Reclassified wt-0002: `math_and_calculations` → `disinfection_and_oxidation`
- Reclassified wt-0003: `taste_and_odor` → `water_source_and_reservoir_management`

## 2026-04-05

- Added dataset toolchain: `validate.py`, `export.py`, `stats.py`, `eval.py`, `new_record.py`, `batch_scaffold.py`
- Added `data/system_prompt.txt` (canonical minimal system prompt)
- Added `data/seeds/municipal_starter.txt` (26 seed topics across 16 categories)
- Added 8 golden eval cases covering filtration, math, disinfection, safety, regulations, troubleshooting, plant ops, emergency response
- Added 3 test fixture records in `data/raw/`
- Added GitHub Actions CI workflow (`validate.yml`)
- Added `Makefile` with targets for all common operations
- Added `.editorconfig` for consistent formatting
- Added `CLAUDE.md` for Claude Code session context
- Added `docs/IDEAS.md` for future exploration directions
- Updated `README.md` with repo layout and toolchain quickstart
- Updated `docs/ROADMAP.md` with Phase 0 complete, Phase 1 progress
- Updated `docs/PROJECT_OVERVIEW.md` with toolchain layer

## 2026-04-04

- Added initial project scaffold
- Added `SCHEMA.md`
- Added `TAXONOMY.md`
- Added `STYLE_GUIDE.md`
- Added `ANNOTATION_GUIDE.md`
- Added `CHANGELOG.md`
