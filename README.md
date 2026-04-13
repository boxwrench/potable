# Potable

**Expert-curated fine-tuning data and models for drinking water treatment operations**

Maintained by [Operational Inference](https://operationalinference.com) | Keith Wilkinson, T5 Certified Water Treatment Operator

---

## What this is

Potable is an open project building fine-tuning datasets and language models for drinking water treatment operations. The core asset is an expert-authored dataset that teaches models to reason through complex operational problems the way a licensed operator actually does — not the way a textbook describes it.

Every training example is authored or reviewed by a Class T5 certified operator with over 14 years of experience at a conventional surface water treatment facility. The gap between a plausible-sounding answer and an operationally correct answer is where public health risk lives. That gap is what this project exists to close.

---

## Why this matters

Critical operational judgment in water treatment is learned informally over years of plant floor experience. It lives in the heads of senior operators, not in manuals. Manuals document equipment in isolation. They do not document how a VFD running at 96% FLA on a cool night means something changed in the distribution system, not the pump. They do not document how a colorimetric chlorine test run in direct sunlight will read low regardless of actual residual. They do not document how a wildfire 40 miles away will change your coagulant demand before your jar test confirms it.

That knowledge is what retires when experienced operators retire. Potable is an attempt to capture it in a form that open models can learn from and people can use.

---

## Project components

| Component | Repo | Status |
|---|---|---|
| Dataset | [boxwrench/potable](https://github.com/boxwrench/potable) | Active development |
| Models | boxwrench/potable-lm | Coming |
| Agent | boxwrench/potable-agent | Planned |
| Eval harness | boxwrench/potable-harness | Planned |

---

## Two deployment tracks

### Municipal track

**Model:** Gemma 4 31B Dense, fine-tuned with QLoRA
**License:** CC-BY-NC-4.0 — non-commercial with attribution
**Deployment:** On-premises, approximately 20GB VRAM at Q4_K_M — no cloud dependency

Covers conventional surface water treatment, groundwater operations, and distribution system management. Designed for licensed operators at municipal water utilities who need expert-level responses on the first query without prompting skill.

### Developing regions track

**Model:** Gemma 4 E2B — 2.3B parameters, Android deployable, offline, 140 languages
**License:** CC-BY-4.0 — fully open
**Deployment:** Offline-capable on low-cost Android devices

Covers wells, handpumps, biosand filters, point-of-use chlorination, and WASH sanitation. Designed for community water workers in low-resource settings. Philanthropically funded. This track is the moral center of the project.

---

## The dataset

The dataset is the durable asset. The base model is documented plumbing — if a better model releases, the data pipeline does not change.

Each record uses a metadata envelope over OpenAI-compatible ChatML messages. At training time a script strips the metadata to produce plain `messages` format compatible with all major fine-tuning frameworks.

```json
{
  "messages": [
    {"role": "system", "content": "..."},
    {"role": "user", "content": "..."},
    {"role": "assistant", "content": "..."}
  ],
  "metadata": {
    "id": "wt-0001",
    "category": "disinfection_and_oxidation",
    "subcategory": "ct_compliance",
    "difficulty": "intermediate",
    "source_type": "expert_authored",
    "tags": ["chlorine", "CT", "SWTR", "residual"],
    "review_status": "approved",
    "created_date": "2026-04-01",
    "version": 1,
    "notes": ""
  }
}
```

### Reasoning framework

Every assistant response uses a structured seven-stage Chain-of-Thought framework:

1. **Assessment** — Situation characterization and urgency
2. **Information Gathering** — What additional data is needed and why
3. **Telemetry Review** — Specific parameters with values, units, and trend direction
4. **Hypothesis Formation** — Plausible causes ranked by likelihood
5. **Root Cause Analysis** — Differential diagnosis through elimination
6. **Action Plan** — Specific corrective actions with values and setpoints
7. **Verification** — How to confirm the action worked and what to monitor

### Quality standards

- Minimum 40% expert-authored examples
- Five-dimension rubric: technical accuracy, reasoning visibility, specificity, operator voice, logical completeness
- Minimum composite score of 20/25 for inclusion
- 100% human review of safety-critical content
- Held-out golden evaluation set used to measure improvement across training versions

---

## Taxonomy

16 categories organized by cognitive task and failure mode independence. A category earns its place when its failure modes are distinct from every other category and the operator's reasoning process is genuinely different.

| Category | Domain |
|---|---|
| `water_source_and_reservoir_management` | Raw water quality, watershed events, reservoir operations |
| `groundwater` | Well systems, aquifer behavior, GWUDI, groundwater chemistry |
| `coagulation_flocculation_and_sedimentation` | Jar testing, dose adjustment, polymer, basin management |
| `pH_and_alkalinity` | System-wide pH and alkalinity across coagulation, disinfection, corrosion |
| `filtration` | Filter run management, backwash, head loss, media, membrane |
| `disinfection_and_oxidation` | Chlorination, chloramination, UV, ozone, CT, DBP control |
| `distribution_nitrification_and_corrosion` | Pressure, storage, nitrification, LCR, main breaks |
| `regulations` | Compliance reasoning, public notification, violation response |
| `operational_procedure_and_process_management` | Startup, shutdown, chemical changeovers, shift handoff |
| `systems_integration_and_equipment_behavior` | Equipment telemetry in process context, cascade failures |
| `SCADA_and_controls_infrastructure` | PLC failures, network issues, HMI artifacts, alarm management |
| `analyzers_and_instrumentation` | Instrument failure modes, calibration drift, cross-checking |
| `measurement_reliability_and_field_analysis` | Colorimetric interference, sample handling, field testing |
| `chemical_feed_and_chemical_treatment` | Chemical quality, concentration verification, feed system failures |
| `emergency_response` | Source contamination, pressure loss, boil water advisory, notification |
| `external_events_and_non_routine_operations` | Wildfires, agricultural events, infrastructure failures, extreme weather |

Full definitions, subcategory targets, and inclusion rationale: [TAXONOMY.md](TAXONOMY.md)

---

## Data availability

Dataset files are withheld during active model development.

Planned release milestones:

- **v0.1** — ~50 seed examples, CC-BY-4.0, released on Hugging Face
- **v0.2** — ~100-200 examples, license determined at time of release
- **Developing regions content** — Fully open, CC-BY-4.0, released independently
- **Larger dataset tiers** — Licensed to support project funding

Hugging Face dataset page: [boxwrench/potable](https://huggingface.co/datasets/boxwrench/potable)

---

## Repository layout

```
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
    raw/                     <- one .json record per file
    eval/                    <- golden evaluation cases
    seeds/                   <- batch scaffolding seed files
    exports/                 <- gitignored, training JSONL output
    system_prompt.txt        <- canonical system prompt
  scripts/
    validate.py              <- schema validation and duplicate detection
    export.py                <- export clean training JSONL
    stats.py                 <- coverage and token stats
    eval.py                  <- golden eval scoring
    new_record.py            <- scaffold a single new record
    batch_scaffold.py        <- scaffold records from a seeds file
  .github/
    workflows/
      validate.yml           <- CI validation on push and PR
```

---

## Toolchain

```
make validate       # check all records against schema
make stats          # coverage report with gap detection
make export         # export approved records to JSONL
make eval           # run golden eval set
make new-record     # scaffold a blank record
make scaffold S=data/seeds/file.txt   # batch scaffold from seed file
```

---

## Reference documents

- [SCHEMA.md](SCHEMA.md) — Record format and metadata field definitions
- [TAXONOMY.md](TAXONOMY.md) — 16-category knowledge map with definitions
- [STYLE_GUIDE.md](STYLE_GUIDE.md) — Operator voice conventions and formatting rules
- [ANNOTATION_GUIDE.md](ANNOTATION_GUIDE.md) — QA rubric and review protocol
- [DEVLOG.md](DEVLOG.md) — Ongoing project notes and milestone entries
- [CHANGELOG.md](CHANGELOG.md) — Versioned dataset and schema changes

---

## Who this is for

- Licensed drinking water treatment operators
- Water utility staff and technical trainers
- Researchers working on critical infrastructure AI
- Public health and WASH partners in developing regions
- Grantmakers evaluating open, high-impact applied AI

---

## Support

Operational Inference and the Potable project are graciously supported by [Robot Garden](https://robotgarden.org), a community workshop and makerspace in Livermore, CA and a 501(c)(3) nonprofit organization. Robot Garden provides infrastructure so that people can engage in and collaborate on technology projects, promoting innovation and interest in science, technology, engineering, industrial arts, and math through robotics and creative projects.

Their support makes the open and philanthropic dimensions of this work possible.

---

## Contributing

The initial phase is founder-led and focused on establishing data quality, schema discipline, and voice consistency. Public contribution guidelines will be added after the core format and review workflow stabilize.

If you are a water operator, regulator, WASH practitioner, or potential research partner, outreach is welcome.

---

## License

Models (potable-lm): CC-BY-NC-4.0 — non-commercial with attribution
Dataset: See data availability section above
Developing regions content: CC-BY-4.0

---

## Contact

Keith Wilkinson
Operational Inference — [operationalinference.com](https://operationalinference.com)
GitHub: [boxwrench](https://github.com/boxwrench)
Writing: [title22.org](https://title22.org)
Hugging Face: [boxwrench](https://huggingface.co/boxwrench)
