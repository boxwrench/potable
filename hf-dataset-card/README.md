---
license: other
task_categories:
- text-generation
language:
- en
tags:
- water-treatment
- fine-tuning
- chain-of-thought
- drinking-water
- SCADA
- operator-knowledge
- critical-infrastructure
- domain-adaptation
pretty_name: Potable Dataset
size_categories:
- n<1K
---

# Potable Dataset

**Expert-curated fine-tuning data for drinking water treatment operations**

Maintained by [Operational Inference](https://operationalinference.com) | Keith Wilkinson, T5 Certified Water Treatment Operator

---

## Dataset description

The Potable Dataset is a fine-tuning dataset for language models in the drinking water treatment domain. Every example is authored or reviewed by a licensed water treatment operator with Class T5 certification — the highest treatment license issued in California — with over 14 years of operational experience.

The dataset teaches models to reason through operational problems using structured Chain-of-Thought prompting: how a senior operator sequences observations, weighs evidence, eliminates alternatives, and commits to action under uncertainty.

Part of the [Potable project](https://github.com/boxwrench/potable).

---

## Project direction

**Municipal track** — Conventional surface water treatment, groundwater operations, and distribution system management. Designed for licensed operators at municipal water utilities. On-premises deployable, no cloud dependency.

**Developing regions track (WASH)** — Wells, handpumps, biosand filters, point-of-use chlorination, and WASH sanitation. Designed for community water workers in low-resource settings. Offline-capable, fully open under CC-BY-4.0.

---

## Dataset structure

Each record uses a metadata envelope over OpenAI-compatible ChatML messages. At training time, a script strips the metadata to produce plain `messages` format compatible with standard fine-tuning frameworks.

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

Assistant responses use structured reasoning — assessment, hypothesis formation, root cause analysis, action planning, and verification — so that each diagnostic step is visible and independently evaluable.

---

## Taxonomy: 16 categories

Categories are organized by cognitive task and failure mode independence.

| Category | Description |
|---|---|
| `water_source_and_reservoir_management` | Raw water quality, watershed events, reservoir operations, algae, seasonal variation |
| `groundwater` | Well systems, aquifer behavior, GWUDI, groundwater-specific chemistry and treatment |
| `coagulation_flocculation_and_sedimentation` | Jar testing, dose adjustment, polymer, sedimentation basin management |
| `pH_and_alkalinity` | System-wide pH and alkalinity as they affect coagulation, disinfection, and corrosion |
| `filtration` | Filter run management, backwash, head loss, media problems, membrane filtration |
| `disinfection_and_oxidation` | Chlorination, chloramination, UV, ozone, CT compliance, DBP control |
| `distribution_nitrification_and_corrosion` | Pressure management, storage, nitrification, LCR monitoring, main breaks |
| `regulations` | Compliance reasoning, public notification, violation response, regulatory frameworks |
| `operational_procedure_and_process_management` | Startup/shutdown, chemical changeovers, shift handoff, reduced redundancy operations |
| `systems_integration_and_equipment_behavior` | Equipment telemetry in process context, cascade failures, system interaction effects |
| `SCADA_and_controls_infrastructure` | PLC failures, network issues, HMI artifacts, remote telemetry, alarm management |
| `analyzers_and_instrumentation` | Instrument-specific failure modes, calibration drift, cross-checking analyzers |
| `measurement_reliability_and_field_analysis` | Colorimetric interference, sample handling, field testing reliability, lab QC |
| `chemical_feed_and_chemical_treatment` | Chemical quality, concentration verification, feed system failures, batch errors |
| `emergency_response` | Source contamination, pressure loss, boil water advisory, treatment loss, notification |
| `external_events_and_non_routine_operations` | Wildfires, agricultural events, infrastructure failures, extreme weather, pandemics |

Full taxonomy: [TAXONOMY.md](https://github.com/boxwrench/potable/blob/main/TAXONOMY.md)

---

## Data availability

The dataset is in active development. Examples will be released on Hugging Face as the project matures. Developing regions content will be fully open under CC-BY-4.0.

Research partners and WASH organizations interested in early access are welcome to reach out.

---

## Intended use

**Appropriate uses:**
- Fine-tuning open language models for water treatment operations support
- Research on domain adaptation and expert knowledge capture
- Training tools for water operators and utility staff
- WASH program support in developing regions

**Out-of-scope uses:**
- Autonomous control of water treatment processes without human oversight
- Replacing licensed operator judgment on compliance decisions
- Any application where a model error could directly affect public health without a human review layer

---

## Licensing

Dataset: License terms vary by release. Developing regions content is CC-BY-4.0.

---

## Citation

```
@dataset{wilkinson2026potable,
  author    = {Wilkinson, Keith},
  title     = {Potable Dataset: Expert-Curated Fine-Tuning Data for Drinking Water Treatment Operations},
  year      = {2026},
  publisher = {Operational Inference},
  url       = {https://huggingface.co/datasets/boxwrench/potable}
}
```

---

## Related

- [boxwrench/potable](https://github.com/boxwrench/potable) — Main project repo
- [boxwrench/potable-lm](https://huggingface.co/boxwrench/potable-lm) — Model weights (planned)
- [title22.org](https://title22.org) — Maintainer writing and project notes

---

## Contact

Keith Wilkinson
Operational Inference — [operationalinference.com](https://operationalinference.com)
GitHub: [boxwrench](https://github.com/boxwrench)
