# Project Overview

## Summary

Potable is a dataset-and-model project for drinking water treatment operations, developed under [Operational Inference](https://operationalinference.com).

The project begins with drinking water treatment because that is where the founder has direct operational expertise. The focus is on building a high-quality dataset that captures real operator judgment in a reusable, framework-agnostic format.

## What is being built

### Dataset

A fine-tuning dataset with:

- chat-style messages for broad framework compatibility
- metadata for filtering, review status, versioning, and auditability
- examples grounded in real plant-floor reasoning rather than textbook abstraction

### Models

Two planned tracks:

- Municipal track for licensed operators at treatment plants
- Developing regions track for offline use by community water workers

### Toolchain

A pure stdlib Python toolchain supporting the data lifecycle:

- schema validation
- clean JSONL export with filtering
- coverage reporting with taxonomy gap detection
- golden evaluation framework
- record scaffolding tools (interactive and batch)
- GitHub Actions CI for automated validation on every push

## Public artifacts

- GitHub: [boxwrench/potable](https://github.com/boxwrench/potable)
- Hugging Face dataset: [boxwrench/potable](https://huggingface.co/datasets/boxwrench/potable)
- Hugging Face model: [boxwrench/potable-lm](https://huggingface.co/boxwrench/potable-lm)

Naming: Project is **Potable**, dataset is **Potable Dataset**, models are **PotableLM**.
