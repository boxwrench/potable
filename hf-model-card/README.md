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

PotableLM is a planned domain-adapted model family for drinking water treatment operations. The initial municipal-track direction is a Gemma 4 31B Dense fine-tune built on the Potable Dataset, an expert-curated corpus of operational water treatment knowledge.

This page is being prepared before the first public checkpoint release so the project has a stable public reference during grant and partnership outreach.

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

Planned initial base model:

- Gemma 4 31B Dense

Rationale:

- permissive Apache 2.0 licensing
- dense architecture suitable for straightforward fine-tuning
- strong local deployment potential for evaluation and utility-facing use cases

The project may later add smaller models for offline deployment in low-resource contexts.

## Training Data

The model is intended to be trained on the Potable Dataset, an expert-curated corpus covering:

- treatment process knowledge
- plant operations
- troubleshooting scenarios
- calculations
- safety and regulatory context

The differentiator is not raw scale. It is operator-authored or operator-reviewed quality and voice.

## Training Procedure

Planned early procedure:

- parameter-efficient fine-tuning with QLoRA
- single-GPU training runs
- iterative evaluation against a fixed golden benchmark set

## Evaluation

Formal benchmark results are not yet published.

Planned evaluation dimensions:

- accuracy
- completeness
- specificity
- practical usefulness
- consistency of operator-style tone

## Risks and Limitations

- Water treatment advice is context-dependent and should not be generalized blindly across plants.
- Model outputs can be plausible and still wrong.
- The model must be treated as an assistant, not an authority.
- Current and local regulations always override model output.

## Model Release Status

No public model weights are released at this time.

This card is published in advance to establish the project's intended scope and operating constraints.

## License

The intended municipal-track base model path uses Apache 2.0-compatible foundations.

Any released checkpoint will clearly state:

- the exact base model used
- the license governing the released weights
- whether the release is research-only or general use

## Contact

- Project writing and context: [title22.org](https://title22.org)
- GitHub: [boxwrench](https://github.com/boxwrench)
