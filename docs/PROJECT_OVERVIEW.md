# Project Overview

## Summary

Potable is a dataset-and-model project for drinking water treatment operations. It is being developed under Effective Intelligence, an umbrella identity for applied AI work that makes expert technical knowledge practically accessible in real-world domains.

The project begins with drinking water treatment because that is where the founder has direct operational expertise. It is structured around one core conviction: the durable asset is not a single model checkpoint, but a high-quality dataset that captures real operator judgment in a reusable format.

## Strategic framing

- Open by default
- Commercial only if needed for cost recovery
- Technical rigor over hype
- Operator voice as the differentiator
- Developing regions track as the highest-impact long-term application

## What is being built

### Dataset layer

A fine-tuning dataset with:

- chat-style messages for broad framework compatibility
- metadata for filtering, review status, versioning, and auditability
- examples grounded in real plant-floor reasoning rather than textbook abstraction

### Model layer

Two planned tracks:

- Municipal track for developed-world treatment plants
- Developing regions track for offline use by community water workers

### Workflow layer

- fast field capture
- lightweight desk structuring
- scripted export to JSONL
- validation, deduplication, and benchmark-driven iteration

## Intended public artifacts

- GitHub repository for methods, documentation, and scripts
- Hugging Face dataset page
- Hugging Face model page
- eventually: sample records, taxonomy docs, style guide, and benchmark notes

Public naming is expected to follow this pattern:

- Project: Potable
- Dataset: Potable Dataset
- Models: PotableLM
