---
license: apache-2.0
language:
- en
pipeline_tag: text-generation
tags:
- water-treatment
- drinking-water
- critical-infrastructure
- gemma
- fine-tuning
---

# PotableLM

## Model Summary

PotableLM is a planned domain-adapted model family for drinking water treatment operations, built on the [Potable Dataset](https://huggingface.co/datasets/boxwrench/potable) — an expert-curated corpus of operational water treatment knowledge.

Two tracks are planned: a municipal track for licensed plant operators (on-premises deployable) and a developing regions track for community water workers (offline-capable, fully open).

No model weights have been released yet. This page establishes the project's intended scope while development continues.

## Intended Use

The model is intended as a technical assistant for:

- licensed operators
- utility staff
- trainers and technical reviewers
- researchers evaluating domain adaptation in critical infrastructure

Primary target behaviors:

- practical operational reasoning
- troubleshooting support
- calculation walkthroughs
- technically grounded explanations in operator voice

## Out-of-Scope Use

- direct control of treatment processes
- fully autonomous safety-critical decision-making
- compliance interpretation without human review
- replacement for plant procedures, regulations, or licensed judgment

## Base Model

Base model selection is ongoing. The project prioritizes permissive licensing, local deployment potential, and strong fine-tuning characteristics.

## Training Data

The model will be trained on the [Potable Dataset](https://huggingface.co/datasets/boxwrench/potable), an expert-curated corpus covering treatment process knowledge, plant operations, troubleshooting, calculations, and regulatory context. Every example is authored or reviewed by a licensed operator.

## Training Procedure

Training procedure will be documented with the first checkpoint release.

## Evaluation

No benchmark results are published yet. Evaluation details will accompany each released checkpoint.

## Risks and Limitations

- Water treatment advice is context-dependent and should not be generalized blindly across plants.
- Model outputs can be plausible and still wrong.
- The model must be treated as an assistant, not an authority.
- Current and local regulations always override model output.

## License

License will be specified with each released checkpoint.

## Contact

Keith Wilkinson
Operational Inference — [operationalinference.com](https://operationalinference.com)
GitHub: [boxwrench](https://github.com/boxwrench)
Writing: [title22.org](https://title22.org)
