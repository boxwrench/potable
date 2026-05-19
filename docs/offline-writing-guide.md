# Offline Writing Guide

This guide is for turning rough source seeds into strong Potable training records.

The seed can be weak. The final record cannot be weak.

Use this when writing by hand, editing AI-assisted drafts, or reviewing synthetic variants. Do not edit raw ingestion artifacts, v1 LoRA files, T5 exports, keeper chains, inbox chains, or candidate rows while writing. Those remain source evidence and review inputs. The authored output is a separate training record derived from one or more seed IDs.

## Goal

Write operator-facing examples that teach practical drinking-water reasoning:

- what signal matters
- what it probably means
- what to check first
- what action follows
- what would change the decision
- when safety, compliance, or escalation matters

The model should learn judgment and response style from the final record, not from messy source text.

## Source Roles

Treat source material by role:

- Transcript excerpts are reasoning anchors. They are the best examples of how the answer should think.
- Dataset/docx items are scenario seeds. They usually need rewriting into a clearer operator question and answer.
- Keeper and inbox chains are incident seeds. They often contain useful facts mixed with email noise.
- T5/question chunks are topic prompts. They may help coverage, but they need heavy rewriting.
- Skipped rows should not be used unless deliberately revisited and reclassified.

The source seed gives the situation. The writer supplies the clean reasoning record.

## Do Not Disturb

Do not rewrite, delete, or normalize these while authoring:

- existing v1 LoRA training files
- `outputs/fine_tune/*`
- raw T5 question exports
- keeper chain exports
- inbox chain exports
- curation candidate rows
- importer scripts

If a seed is wrong or weak, mark that in notes or review status. Do not silently mutate source evidence to make a training record easier.

## Entry Format

Each finished entry should be written as a structured worksheet first. JSON conversion can happen later.

```text
Record ID:
Seed ID(s):
Seed lane(s):
Working title:
Category/subsystem:
Action type:
Difficulty:
Stakes:
Source strength:

Usable source facts:
- 
- 
- 

Noise or facts to ignore:
- 
- 

Operator question:

Ideal reasoning hints:
- First signal:
- Likely interpretation:
- First check:
- Second check:
- Action if confirmed:
- Action if disproven:
- Safety/compliance/escalation:
- Uncertainty or dependency:

Final answer:

Reviewer notes:
```

This form is intentionally restrictive. It forces the writer to separate source facts, reasoning structure, and final prose.

## Field Guidance

### Record ID

Leave blank if IDs are assigned by script. If writing manually, use the next stable project ID.

### Seed ID(s)

Always list the source candidate IDs. A record can use more than one seed only when the facts are compatible and the combination is intentional.

Bad:

```text
Seed ID(s): several emails about filters
```

Good:

```text
Seed ID(s): dataset-docx-004, may-7-at-7-06-pm-rtf-001
```

### Seed Lane(s)

Use the ingestion lane, such as:

- `transcript`
- `dataset_docx`
- `keeper_chain`
- `inbox_chain`
- `t5_question`

### Category/subsystem

Use the closest stable operating area. Examples:

- raw water intake
- chemical feed
- filtration/backwash
- disinfection
- controls/SCADA
- power systems
- plant evolutions
- compliance/reporting
- safety

### Action Type

Pick what the answer is mostly doing:

- troubleshooting
- scenario planning
- procedure/checklist
- compliance notification
- calculation
- handoff/explanation
- instrumentation verification

### Difficulty

Use difficulty to describe reasoning complexity, not topic importance.

- Basic: one symptom, direct answer, one or two checks.
- Intermediate: ordered checks, conditional branches, some tradeoff.
- Advanced: interacting causes, uncertainty, escalation logic, safety or regulatory pressure.

### Stakes

Use the highest relevant stakes:

- routine
- equipment risk
- water quality excursion
- public health or regulatory
- safety critical

Do not inflate stakes just to make the record feel important.

### Source Strength

Use this to protect quality:

- Strong: source already contains clear reasoning or a detailed incident.
- Medium: source contains a good situation but needs reasoning added.
- Weak: source is only directionally useful and must be rewritten heavily.

Weak seeds are allowed. Weak final answers are not.

## Writing Process

Use this sequence for every record:

1. Read the seed once for the situation.
2. Extract only the usable facts.
3. Write down what noise or uncertainty you are ignoring.
4. Decide the operational question the seed should elicit.
5. Fill in the reasoning hints before writing the answer.
6. Write the final answer in operator voice.
7. Check for invented facts.
8. Check that the answer teaches a reusable reasoning pattern.

If the reasoning hints are hard to fill in, the seed is probably not ready for a training record.

## Reasoning Pattern

Most records should follow this internal logic:

```text
signal -> interpretation -> verification -> action -> follow-up
```

Example:

```text
Filter effluent turbidity is rising after a backwash.
That could be ripening, a bad return-to-service decision, media disturbance, or an instrument issue.
Verify run time, filter-to-waste status, recent valve sequence, and whether the turbidimeter agrees with grab samples.
Keep the filter out of service or return to waste if the trend is real.
Escalate if the trend threatens plant effluent or compliance limits.
```

The final answer should not mechanically label those steps, but the reasoning should be visible.

## Ideal Reasoning Hints

Use these hints to shape answers.

### Troubleshooting

- What changed first?
- Is the signal real or instrumentation?
- What is the fastest safe check?
- What check separates process cause from equipment cause?
- What action protects water quality while diagnosis continues?
- What finding would change your conclusion?

### Scenario Planning

- What has to be true before the evolution starts?
- What is the weak point in the plan?
- What should be verified before committing?
- What should operators watch during the change?
- What is the rollback or stop condition?

### Chemical Feed

- Is the issue dose, demand, concentration, feed equipment, or control logic?
- What confirms actual feed, not just commanded feed?
- Are residual, pH, flow, and analyzer readings consistent?
- Does the answer distinguish short-term control from root cause?

### Filtration and Backwash

- Is the concern headloss, turbidity, ripening, breakthrough, valve sequence, or backwash effectiveness?
- What does run time say?
- What does the trend say compared with one grab sample?
- Should the filter stay out, return to waste, or continue under watch?

### Raw Water and Source Changes

- Is the change seasonal, storm-driven, operational, or measurement-related?
- What upstream or reservoir signal supports the interpretation?
- What treatment response should be staged rather than rushed?
- What needs tighter monitoring during the transition?

### Controls and Instrumentation

- Does the field condition agree with SCADA?
- Did a mode, setpoint, permissive, or interlock change?
- What can be verified locally?
- What should be documented for controls staff?

### Compliance and Notification

- What requirement or operating limit might be implicated?
- Is this already a reportable event or only a condition to watch?
- What facts need to be preserved?
- Who needs notification according to plant procedure?
- Avoid legal certainty unless the seed clearly supports it.

### Safety

- What immediate hazard exists?
- What action makes the area or equipment safe?
- What procedure controls the work?
- What should not be done until the hazard is isolated?

## Final Answer Structure

Default structure:

1. Direct practical answer.
2. Why that answer fits the signal.
3. Ordered checks.
4. Conditional actions.
5. Safety, compliance, or escalation note if relevant.

Do not use section headings inside most answers unless the record is intentionally a checklist.

Good operator answers sound like:

```text
I would treat that as a real process risk until you prove it is an instrument problem.
Start by checking whether the trend is showing up anywhere else...
```

Weak answers sound like:

```text
There are several possible causes that should be considered...
```

## Question Writing

The user question should sound like something a plant operator, lead, engineer, or trainee would actually ask.

Good question:

```text
Filter 6 came back from backwash and its effluent turbidity is still climbing after the normal ripening period. What should I check before I put it fully back online?
```

Weak question:

```text
Explain filter ripening and turbidity management in drinking water treatment.
```

Prefer situation-based questions over textbook prompts.

## Answer Voice

Write like a senior operator talking to a capable coworker:

- direct
- specific
- calm
- technically grounded
- conditional where needed
- practical before theoretical

Use real terms and units when the source supports them:

- NTU
- mg/L
- gpm
- MGD
- psi
- minutes
- residual
- headloss
- filter-to-waste
- permissive
- interlock
- analyzer
- grab sample

Do not invent numeric thresholds. If a number is plant-specific, say so.

## Handling Weak Seeds

Weak seeds are useful if they point toward a real reasoning pattern.

When a seed is weak:

- keep only the situation
- remove email noise
- avoid names and irrelevant scheduling details
- write the question around the operational decision
- make the answer conservative and verification-heavy
- do not add unsupported technical claims

If the seed cannot support at least one concrete signal and one concrete decision, do not write a training record from it yet.

## Handling Transcripts

Transcripts are valuable because they contain reasoning style, not because every sentence is clean.

When adapting a transcript:

- preserve the causal chain
- remove filler words and false starts
- keep the operational sequence
- keep uncertainty if it affected the decision
- turn rambling explanation into a clean answer
- do not over-polish into textbook voice

Transcript-derived records should be the style anchor for AI-assisted generation.

## AI-Assisted Drafting

AI can help draft records, but it must be constrained.

Use this instruction:

```text
Use only the provided source facts. Do not invent procedures, thresholds, regulations, equipment, or outcomes.
Write one operator-facing training record in the Potable style.
The answer must show signal, interpretation, verification, action, and escalation where relevant.
If the source is too weak, say that no record should be written.
```

Require the draft to return:

```text
Unsupported claims:
- none
```

If unsupported claims are present, either edit them out or reject the draft.

## Synthetic Variants

Synthetic variants are allowed only after a canonical record exists.

Allowed variants:

- prompt rewrite: same answer, different realistic question
- shorter field answer: same reasoning compressed
- checklist version: same facts in ordered steps
- bad instinct correction: user proposes a tempting but wrong action
- what changed: same scenario with one new observation that changes the next step

Not allowed:

- new plant facts
- invented regulatory thresholds
- invented equipment behavior
- changed outcome
- variants that split one source into contradictory lessons

Every variant must point back to the canonical seed ID and record ID.

## Review Checklist

Before approving a record, answer yes to all of these:

- Does the question sound like a real operator question?
- Does the answer lead with useful action?
- Does the answer show reasoning, not just conclusion?
- Are checks ordered by operational priority?
- Are uncertainty and dependencies handled honestly?
- Are safety or compliance issues included only when relevant?
- Are all factual claims supported by the seed or general operator judgment?
- Does this record teach something different from nearby records?
- Would this be safe to show a competent operator as training style?

If any answer is no, keep it as draft.

## Example Worksheet

```text
Record ID: wt-draft-001
Seed ID(s): may-7-at-7-06-pm-rtf-001
Seed lane(s): transcript
Working title: Manual backwash as automation training
Category/subsystem: filtration/backwash
Action type: scenario planning
Difficulty: intermediate
Stakes: routine
Source strength: strong

Usable source facts:
- Facility has automatic filter backwashing.
- Operators should understand manual backwash steps before relying on automation.
- Manual operation helps reveal what each automated step is doing.

Noise or facts to ignore:
- Transcript filler and repeated phrases.
- Personal timing details that do not affect the lesson.

Operator question:
Our filters backwash automatically. Why should a new operator still learn to run a manual backwash?

Ideal reasoning hints:
- First signal: Operator is relying on automation without understanding sequence.
- Likely interpretation: Automation hides valves, timing, permissives, and failure points.
- First check: Make sure training is done under supervision and normal conditions.
- Second check: Walk through each step and what the system is trying to accomplish.
- Action if confirmed: Have the operator perform or shadow manual backwash.
- Action if disproven: If conditions are abnormal, defer training and use SOP/lead guidance.
- Safety/compliance/escalation: Do not use training to risk filter performance or water quality.
- Uncertainty or dependency: Exact steps depend on plant SOP and control system.

Final answer:
Even with automatic backwash, a new operator should understand the manual sequence because automation hides the reasoning. You need to know which valves move, when the wash starts, what permissives have to be satisfied, and what the filter should look like when it is ready to return to service. That is how you catch a failed step instead of just trusting the screen.

I would train it under normal conditions with an experienced operator watching, not during an upset. Walk through the sequence slowly: take the filter out, confirm the right valves and status indications, watch the wash stages, and verify the return-to-service condition. The point is not to bypass automation. The point is to understand what the automation is doing so that when it fails, you can tell whether the problem is the filter, the valve sequence, the instrument, or the control logic.

Reviewer notes:
Good transcript-derived reasoning anchor. Keep as canonical before making variants.
```

## Session Rhythm

For hand writing:

1. Pick 5 to 10 seeds.
2. Fill only source facts and noise first.
3. Then write questions for the whole batch.
4. Then write reasoning hints.
5. Only then write final answers.

This avoids turning the first rough interpretation into final prose too early.

## When You Get Back Online

Convert approved worksheets into canonical records:

1. Assign stable IDs.
2. Preserve seed IDs in metadata.
3. Convert question and answer into `messages`.
4. Set review status to `draft` or `reviewed`.
5. Validate schema.
6. Split train/eval by seed ID, not by rendered row.
7. Keep held-out golden seeds out of training and synthetic variants.

The ingestion tools collect candidates. This guide turns candidates into training data.
