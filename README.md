# Potable

Potable is an open water-treatment AI project under Effective Intelligence focused on making expert drinking water treatment knowledge practically accessible.

The core asset is an expert-curated fine-tuning dataset for drinking water treatment operations. The long-term aim is to support two deployment tracks:

- Municipal track: an on-premises assistant for licensed operators at conventional treatment plants.
- Developing regions track: a fully open, offline-capable assistant for community water workers using low-cost Android devices.

Potable brings together the dataset, model, and workflow for capturing practical water-treatment expertise in a form that open models can learn from and people can use.

The dataset and model family under this project are expected to be published as the Potable Dataset and PotableLM.

## Why this exists

Critical operational judgment is often learned informally and can be lost as experienced operators retire. Potable is an attempt to preserve and distribute that judgment through carefully structured training data, open models, and deployment paths that do not require permanent cloud dependence.

The project is open by default and grounded in practical utility for real operators and water workers.

## Project scope

### 1. Dataset

The dataset is the durable asset. It uses a metadata envelope over chat-style training messages so examples can be filtered, audited, versioned, and exported into plain `messages` format for fine-tuning frameworks.

Planned example types:

- factual Q&A
- operational reasoning
- calculation walkthroughs
- troubleshooting scenarios
- regulatory interpretation
- multi-turn conversations

### 2. Models

Current planned model directions:

- Municipal track: Gemma 4 31B Dense fine-tuned with QLoRA
- Developing regions track: Gemma 4 E2B, with E4B as fallback if needed

The dataset is model-agnostic. If the base model changes, the data pipeline should not.

### 3. Deployment philosophy

- On-premises or local-first where possible
- Offline-capable capture workflow
- Open community tier
- Safety-conscious use in a critical infrastructure domain

## Current status

This repository is in the public setup phase.

Near-term goals:

1. Publish the public-facing project description.
2. Stand up Hugging Face dataset and model pages.
3. Create the first seed examples and style guide.
4. Build validation and export scripts.
5. Establish an initial golden evaluation set.

## Repository layout

```text
potable/
  README.md
  DEVLOG.md
  CHANGELOG.md
  SCHEMA.md
  TAXONOMY.md
  STYLE_GUIDE.md
  ANNOTATION_GUIDE.md
  Makefile
  .gitignore
  docs/
    PROJECT_OVERVIEW.md
    ROADMAP.md
    IDEAS.md
  hf-dataset-card/
    README.md
  hf-model-card/
    README.md
  data/
    raw/                     ← one .json record per file
    eval/                    ← golden evaluation cases
    seeds/                   ← batch scaffolding seed files
    exports/                 ← (gitignored) training JSONL output
    system_prompt.txt        ← canonical system prompt
  scripts/
    validate.py              ← schema validation + duplicate detection
    export.py                ← export clean training JSONL
    stats.py                 ← coverage and token stats
    eval.py                  ← golden eval scoring
    new_record.py            ← scaffold a single new record
    batch_scaffold.py        ← scaffold records from a seeds file
  .github/
    workflows/
      validate.yml           ← CI validation on push/PR
```

## Toolchain quickstart

```bash
make validate       # check all records against schema
make stats          # coverage report with gap detection
make export         # export approved records to JSONL
make eval           # run golden eval set
make new-record     # scaffold a blank record (interactive)
make scaffold S=data/seeds/municipal_starter.txt  # batch scaffold
```

## Planned taxonomy

Initial municipal categories:

- water_source
- coagulation_flocculation
- sedimentation
- filtration
- disinfection
- corrosion_control
- taste_and_odor
- plant_operations
- laboratory
- safety
- regulations
- math_and_calculations
- equipment_and_maintenance
- distribution
- troubleshooting
- emergency_response

Core reference documents:

- [SCHEMA.md](C:\Github\potable\SCHEMA.md)
- [TAXONOMY.md](C:\Github\potable\TAXONOMY.md)
- [STYLE_GUIDE.md](C:\Github\potable\STYLE_GUIDE.md)
- [ANNOTATION_GUIDE.md](C:\Github\potable\ANNOTATION_GUIDE.md)
- [CHANGELOG.md](C:\Github\potable\CHANGELOG.md)

## Release strategy

- Community dataset tier: planned public release on Hugging Face under an open license
- Production-oriented dataset tiers: possible future cost-recovery path
- Developing regions track: intended to remain fully open

## Who this is for

- licensed drinking water treatment operators
- utility staff and technical trainers
- researchers working on critical infrastructure AI
- public health and WASH partners
- grantmakers evaluating open, high-impact applied AI work

## Contributing

The initial phase is founder-led and focused on establishing data quality, schema discipline, and voice consistency. Public contribution guidelines will be added after the core format and review workflow stabilize.

If you are a water operator, regulator, WASH practitioner, or potential research partner, outreach is welcome.

## Contact

- Keith Wilkinson
- GitHub: [boxwrench](https://github.com/boxwrench)
- Writing: [title22.org](https://title22.org)
- Project umbrella: Effective Intelligence

## Dev Log

Ongoing project notes and milestone entries live in [DEVLOG.md](C:\Github\potable\DEVLOG.md).
