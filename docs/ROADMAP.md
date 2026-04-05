# Roadmap

## Phase 0: Public setup — COMPLETE

- ~~Publish GitHub README~~
- ~~Publish Hugging Face dataset card~~
- ~~Publish Hugging Face model card~~
- ~~Decide initial repository and namespace conventions~~

## Phase 1: Seed dataset — IN PROGRESS

Infrastructure complete. Content authoring is the remaining work.

Done:
- ~~Draft system prompt~~ (`data/system_prompt.txt`)
- ~~Write `STYLE_GUIDE.md`~~
- ~~Write taxonomy and schema docs~~
- ~~Add basic validation script~~ (`scripts/validate.py` — full schema validation, duplicate detection, token bounds)
- ~~Add export script~~ (`scripts/export.py` — clean JSONL with filters)
- ~~Add coverage reporting~~ (`scripts/stats.py` — gap detection, token stats)
- ~~Add golden eval framework~~ (`scripts/eval.py` — 8 eval cases across 8 categories)
- ~~Add record scaffolding tools~~ (`scripts/new_record.py`, `scripts/batch_scaffold.py`)
- ~~Add CI~~ (`.github/workflows/validate.yml`)
- ~~Plan first batch of seed topics~~ (`data/seeds/municipal_starter.txt` — 26 topics across all 16 municipal categories)

Remaining:
- Create first 10 to 25 seed examples (author content from seeds file)
- Review and approve initial records

## Phase 2: Minimum viable dataset

- Reach 200 to 500 examples
- Establish weekly capture and review workflow
- ~~Add automated validation in GitHub Actions~~ (done early — moved to Phase 1)
- ~~Build first golden test set~~ (done early — 8 eval cases, expandable)
- ~~Add coverage analysis and duplicate detection~~ (done early — moved to Phase 1)
- Run first municipal fine-tune

## Phase 3: Public release baseline

- Release community dataset tier
- Publish model evaluation notes
- Prepare documentation for external users and reviewers

## Phase 4: Developing regions track

- Finalize separate taxonomy
- Create seed WASH examples
- Evaluate small-model performance on offline hardware targets
- Prepare philanthropic funding applications around the fully open deployment path
