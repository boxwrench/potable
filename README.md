# Potable

**Expert-curated fine-tuning data and models for drinking water treatment operations**

Maintained by [Operational Inference](https://operationalinference.com) | Keith Wilkinson, T5 Certified Water Treatment Operator

---

## What this is

Potable is an open project building fine-tuning datasets and language models for drinking water treatment operations. Every training example is authored or reviewed by a Class T5 certified operator with over 14 years of experience at a conventional surface water treatment facility.

The goal is to teach models to reason through operational problems the way a licensed operator actually does — not the way a textbook describes it.

---

## Why this matters

Critical operational judgment in water treatment is learned informally over years of plant floor experience. It lives in the heads of senior operators, not in manuals. Manuals document equipment in isolation. They do not document how a VFD running at 96% FLA on a cool night means something changed in the distribution system, not the pump. They do not document how a colorimetric chlorine test run in direct sunlight will read low regardless of actual residual. They do not document how a wildfire 40 miles away will change your coagulant demand before your jar test confirms it.

That knowledge is what retires when experienced operators retire. Potable is an attempt to capture it in a form that open models can learn from and people can use.

---

## Project direction

**Municipal track** — Conventional surface water treatment, groundwater operations, and distribution system management. Designed for licensed operators at municipal water utilities. On-premises deployable, no cloud dependency.

**Developing regions track** — Wells, handpumps, biosand filters, point-of-use chlorination, and WASH sanitation. Designed for community water workers in low-resource settings. Offline-capable, fully open.

| Component | Location | Status |
|---|---|---|
| Dataset | [boxwrench/potable](https://github.com/boxwrench/potable) | Active development |
| Models | [boxwrench/potable-lm](https://huggingface.co/boxwrench/potable-lm) | Planned |

---

## The dataset

Each record uses a metadata envelope over OpenAI-compatible ChatML messages. At training time a script strips the metadata to produce plain `messages` format for fine-tuning.

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

Assistant responses use structured Chain-of-Thought reasoning — assessment, hypothesis formation, root cause analysis, action planning, and verification — so that each step in the operator's diagnostic process is visible and independently evaluable.

---

## Taxonomy

16 categories organized by cognitive task and failure mode independence.

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

Full definitions and design rationale: [TAXONOMY.md](TAXONOMY.md)

---

## Data availability

The dataset is in active development. Initial examples will be released on Hugging Face as the project matures. Developing regions content will be fully open under CC-BY-4.0.

Hugging Face dataset page: [boxwrench/potable](https://huggingface.co/datasets/boxwrench/potable)

---

## Reference documents

- [SCHEMA.md](SCHEMA.md) — Record format and metadata field definitions
- [TAXONOMY.md](TAXONOMY.md) — Category definitions and design rationale
- [STYLE_GUIDE.md](STYLE_GUIDE.md) — Operator voice conventions and formatting rules
- [ANNOTATION_GUIDE.md](ANNOTATION_GUIDE.md) — QA rubric and review protocol

---

## Who this is for

- Licensed drinking water treatment operators
- Water utility staff and technical trainers
- Researchers working on critical infrastructure AI
- Public health and WASH partners in developing regions

---

## Support

Operational Inference and the Potable project are graciously supported by [Robot Garden](https://robotgarden.org), a community workshop and makerspace in Livermore, CA and a 501(c)(3) nonprofit organization. Robot Garden provides infrastructure so that people can engage in and collaborate on technology projects, promoting innovation and interest in science, technology, engineering, industrial arts, and math through robotics and creative projects.

Their support makes the open and philanthropic dimensions of this work possible.

---

## Contributing

The initial phase is founder-led and focused on establishing data quality and voice consistency. Contribution guidelines will follow once the core format stabilizes.

If you are a water operator, regulator, WASH practitioner, or potential research partner, outreach is welcome.

---

## License

Dataset: License varies by release — see data availability above
Developing regions content: CC-BY-4.0
Models: License will be specified with each release

---

## Contact

Keith Wilkinson
Operational Inference — [operationalinference.com](https://operationalinference.com)
GitHub: [boxwrench](https://github.com/boxwrench)
Writing: [title22.org](https://title22.org)
Hugging Face: [boxwrench](https://huggingface.co/boxwrench)
