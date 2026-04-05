# Ideas

Future directions and explorations worth tracking. Nothing here is committed — these are seeds.

## Facility-Owned Dataset Creation

A standalone project (or Potable extension) that lets individual water treatment facilities create their own training datasets. Each plant has unique source water, equipment, SOPs, and institutional knowledge. A tool that helps them capture that in a structured format — potentially compatible with the Potable schema — could be valuable both for local fine-tuning and for contributing back to the community dataset.

Key questions:
- What's the minimum viable capture workflow for a busy plant?
- How do you handle proprietary/confidential plant data vs. shareable knowledge?
- Could this feed into a federated dataset model?

## Gamified Knowledge Capture App

A mobile-friendly app where licensed operators and trades workers answer domain questions — essentially turning expert knowledge capture into a game. Operators earn recognition or progression by contributing high-quality answers in their area of expertise.

This could serve double duty:
- Produces structured training data (if answers follow a schema)
- Builds engagement and community around the project

Key questions:
- What game mechanics work for technical professionals? (Leaderboards? Peer review? Certification-adjacent badges?)
- How do you maintain quality when volume is gamified?
- Could this work across trades beyond water treatment?

## Agent Frameworks for PotableLM

Two repos worth evaluating for building specialized agents on top of PotableLM:

### AutoAgent
- Repo: https://github.com/kevinrgu/autoagent
- Framework for autonomous agent engineering — a meta-agent iteratively modifies system prompts, tools, and agent configuration to improve performance
- Single-file architecture: the entire agent harness lives in one `agent.py` with editable/fixed sections
- Score-driven optimization: hill-climbs on numeric benchmark scores (0.0–1.0)
- Docker-isolated execution for safe experimentation
- Harbor-compatible task format for standardized benchmarks

Potential Potable application: define water treatment tasks (troubleshooting, calculations, compliance) as benchmark suites, then let AutoAgent autonomously optimize the agent harness around PotableLM — tuning prompts, tool selection, and routing logic without manual trial-and-error.

### Meta-Harness
- Page: https://yoonholee.com/meta-harness/
- AI-driven optimization of "harnesses" — the prompts, tool definitions, and logic that guide how LLMs solve tasks
- Uses diagnostic analysis of execution traces and failure patterns to iteratively improve agent performance
- Proven gains: +8 points on text classification, +4.7 on math reasoning, top ranks on agentic coding benchmarks
- Reaches competitor performance with 10x fewer evaluations

Potential Potable application: once PotableLM is fine-tuned, Meta-Harness could automatically optimize the prompts and tool configurations for domain-specific tasks (troubleshooting, compliance checking, calculation walkthroughs) by analyzing where the model fails and evolving the harness to compensate.

### Combined vision

AutoAgent for building the agent scaffolding (task-specific agents with tool use), Meta-Harness for evolving the prompts and logic that drive those agents. Together they could produce agents that are both structured and self-improving.

Key questions:
- Which framework better supports offline/on-premises deployment?
- Can agents be composed with tool use (e.g., pulling SCADA data, querying lab results)?
- What's the minimum viable agent that would be useful to a real plant?
- How much task-specific evaluation data is needed before Meta-Harness optimization becomes worthwhile?

### Related: Karpathy's Autoresearch
- Worth tracking as the philosophical ancestor of this space — autonomous research loops that self-improve
- Revisit once PotableLM has a working eval set and the agent layer is closer to real
