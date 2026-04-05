---
pretty_name: Potable Dataset
license: cc-by-4.0
task_categories:
- text-generation
- question-answering
language:
- en
tags:
- water-treatment
- drinking-water
- critical-infrastructure
- llm-fine-tuning
- operations
size_categories:
- n<1K
---

# Potable Dataset

## Dataset Summary

Potable Dataset is an expert-curated fine-tuning dataset for drinking water treatment operations. It is designed to capture practical operator knowledge in a structured format that can be used to fine-tune open language models for water-sector applications.

The project is part of Effective Intelligence, an applied AI initiative focused on making expert technical knowledge more accessible in real-world domains.

This page is being published early so funders, collaborators, and researchers can evaluate the project direction before the first public dataset release.

## Supported Use Cases

- fine-tuning domain-specific assistants for drinking water treatment
- evaluation of model behavior on operational and troubleshooting tasks
- research on preserving expert judgment in critical infrastructure settings
- educational and training-adjacent experimentation, with appropriate caution

## Out-of-Scope Use

- direct autonomous plant control
- unsupervised safety-critical decision-making
- replacement for licensed operators, engineers, or regulatory review
- use as a sole authority in emergency or compliance situations

## Dataset Structure

Each record is built around chat-style messages and paired with metadata for filtering and governance. The intended export path is framework-agnostic JSONL.

Illustrative structure:

```json
{
  "messages": [
    {"role": "system", "content": "You are an experienced drinking water treatment plant operator..."},
    {"role": "user", "content": "How would you respond to rising settled water turbidity after a storm?"},
    {"role": "assistant", "content": "Start by checking raw water change rate, coagulant feed, and upstream observations..."}
  ],
  "metadata": {
    "id": "wt-0001",
    "category": "coagulation_flocculation",
    "difficulty": "intermediate",
    "tone": "operator",
    "source_type": "expert_authored",
    "review_status": "approved",
    "version": 1
  }
}
```

## Planned Content Areas

- coagulation and flocculation
- sedimentation
- filtration
- disinfection
- corrosion control
- laboratory work
- troubleshooting
- safety
- regulations
- operational math
- distribution and field response

## Data Creation

The data is being developed through a two-step workflow:

1. Fast field capture of scenario kernels, questions, or judgment calls.
2. Structured desk review into schema-compliant training examples.

The intent is to preserve real operator voice rather than produce generic textbook summaries.

## Quality and Review

Planned controls include:

- schema validation
- category and metadata checks
- token-length checks
- duplicate detection
- manual review against a style guide
- targeted evaluation against a golden benchmark set

## Bias, Risks, and Limitations

- The early dataset will reflect the experience and judgment of a limited initial author pool.
- Water treatment practices vary by plant design, source water, regulation, and local operating culture.
- Regulatory and compliance guidance must always be verified against current authoritative sources.
- The dataset is intended to support human operators, not replace them.

## Licensing

The planned public community release is under CC-BY-4.0.

Future production-oriented dataset tiers may use separate commercial licensing, but the project is open by default and the developing regions track is intended to remain fully open.

## Citation

If you use this dataset page in research or grant materials, cite the project as:

**Potable Dataset, Effective Intelligence, Keith Wilkinson.**

## Contact

- Project writing and context: [title22.org](https://title22.org)
- GitHub: [boxwrench](https://github.com/boxwrench)
