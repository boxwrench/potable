# Annotation Guide

## Purpose

This guide describes how records should be created, reviewed, and classified for the Potable Dataset.

It is intended for the founder first and for future contributors or reviewers later.

## Guiding Principle

The goal is not to maximize record count. The goal is to produce useful, reviewable, operator-grade training data.

## Record Creation Workflow

### Step 1: Capture the kernel

Capture a real question, scenario, judgment call, or explanation worth preserving.

Good kernels often come from:

- actual operating questions
- unusual plant conditions
- troubleshooting moments
- repeated explanations given to coworkers
- common mistakes or misconceptions

### Step 2: Choose the category

Assign one primary `category` and one primary `subcategory`.

Use the category that best reflects the main operational question being answered, not every topic mentioned in the response.

### Step 3: Draft the interaction

Create the `messages` array:

- `system` sets the assistant role
- `user` states the question or scenario
- `assistant` gives the answer

Prefer realistic prompts over artificial benchmark phrasing.

### Step 4: Fill metadata

Every record should include the full metadata object with consistent values.

Minimum required care points:

- unique `id`
- correct `category`
- stable `subcategory`
- accurate `source_type`
- honest `review_status`

### Step 5: Review before approval

Check the response against the style guide, schema, and taxonomy.

## Classification Rules

### Category selection

- choose one primary category
- do not multi-label categories in the canonical record
- if torn between two categories, classify by the main thing the answer helps the user do

### Subcategory selection

- use the most specific stable subcategory available
- if no good subcategory exists yet, create a candidate only if it is likely to recur
- avoid one-off subcategories with only a single example unless clearly justified

### Difficulty selection

Use:

- `basic` for straightforward factual or simple operational records
- `intermediate` for records requiring interpretation or multi-step reasoning
- `advanced` for records involving tradeoffs, interacting causes, or complex diagnosis

### Source type selection

Use:

- `expert_authored` when written directly from human expertise
- `ai_assisted` when AI helped draft but the content was materially shaped by human review
- `ai_generated` only when the example originated from AI generation
- `adapted_from_manual` when based substantially on source documents or manuals

Do not label AI-assisted records as expert-authored unless the AI contribution was negligible.

## Review Checklist

Before approval, confirm:

- the record follows the schema
- the answer is technically plausible
- the answer sounds like operator voice when `tone=operator`
- terminology and units are correct
- no empty padding or generic filler remains
- safety or compliance caveats are present where needed
- the example is not a near-duplicate of an existing record

## Rejection Reasons

Reject or return for revision if the record is:

- technically weak
- too vague to be useful
- overconfident where the answer is conditional
- mislabeled in category or source type
- overly textbook-like
- mostly duplicate content
- missing important safety framing

## Review Status Meanings

- `draft`: newly created, not yet reviewed
- `reviewed`: checked and improved, but not final
- `approved`: ready for inclusion in release or training export
- `rejected`: not suitable in current form

## Duplicate and Similar Records

Near-duplicates reduce dataset quality. If two records teach the same core lesson in almost the same way:

- keep the better one
- merge useful details if needed
- preserve variation only when it teaches meaningfully different reasoning

## Multi-Turn Records

Use multi-turn format when follow-up information changes the reasoning. Do not create multi-turn examples just to make the dataset look more sophisticated.

## Grounding Standard

Prefer examples grounded in:

- realistic plant conditions
- realistic operator questions
- practical response sequences
- credible numbers and units

Do not invent unnecessary specifics just to make an example sound realistic.

## Final Standard

An approved record should be something you would be comfortable showing as a reference example for future contributors.
