# Plant Performance Screening Memo Template

Date: 2026-04-29
Status: Draft deliverable template for first pilot

## Purpose

This document is the working end-deliverable template for the first `Plant Performance Screening Pilot`.

It should be written before selling the first pilot because the artifact is the offer. The first customer conversation should be able to point to a concrete example and say:

> Here is the kind of screening memo you would receive. The example numbers are illustrative. The question is whether this would be useful if applied to your actual basin and current operating concern.

The template is designed for a fixed-scope sedimentation or design-vs-current screening engagement. It is not a stamped engineering report, a CFD report, a compliance determination, or an autonomous operating recommendation.

## Intended Reader

Primary readers:

- treatment superintendent
- plant manager
- engineering manager
- consulting engineer evaluating whether deeper study is warranted

Secondary readers:

- operations leadership
- utility general manager
- capital planning or maintenance leadership

The memo should be readable by a non-specialist decision-maker while still being technically clear enough that an engineer can see the assumptions and limitations.

## Recommended Length

Target length:

- 6 to 10 pages for the first external version
- short enough to be read before a review meeting
- complete enough to stand alone as a decision artifact

Appendices can hold detailed model inputs, scenario tables, and extracted notes.

## Front Matter

### Title

Use a plain title:

`Plant Performance Screening Memo: Design-vs-Current Sedimentation Review`

Subtitle:

`Prepared for [Plant / Utility / Consultant]`

Include:

- date
- prepared by Operational Inference
- status: `Screening draft`, `Client review draft`, or `Final screening memo`
- confidentiality note

Suggested confidentiality note:

`This memo is a screening deliverable prepared for the client named above. It is intended to support discussion, prioritization, and scoping of possible next steps. It is not a stamped engineering design document and should not be used as the sole basis for capital design, regulatory certification, or operational changes with material safety or compliance consequences.`

## 1. Executive Finding

Purpose:

- state the practical finding in one page
- make the decision value obvious
- avoid burying the conclusion in model mechanics

Content blocks:

- the plant question
- the design-vs-current comparison
- the likely interpretation
- what should happen next
- what should not be concluded from this screening

Suggested structure:

```text
Question screened:
[One sentence describing the concern.]

Screening result:
[Two to four sentences summarizing what changed between design intent and current condition.]

Likely implication:
[Two to four sentences connecting the hydraulic/process signal to operational concern.]

Recommended next step:
[One of: continue monitoring, field verification, operational trial, consultant study, CFD/tracer/detailed engineering review.]

Important limitation:
[One to three sentences naming the most important model or data boundary.]
```

Language pattern:

- use `suggests`, `is consistent with`, `is likely to`, and `warrants review`
- avoid `proves`, `predicts`, `guarantees`, and `optimizes`

Example wording:

`The screening comparison suggests that the current-state flow path is materially different from the design-intent condition. The strongest signal is not a precise predicted velocity value; it is the changed routing pattern and the increased likelihood of uneven approach conditions downstream of the transition area. This is a decision-useful screening result, but it should be treated as directional until the current-state bypass geometry is field-verified.`

## 2. Plant Question And Decision Context

Purpose:

- capture why the question matters now
- document the buyer's concern in their own operating terms
- turn the project into a decision-support engagement, not a model demonstration

Content blocks:

- what condition triggered the concern
- who is affected by the answer
- what decision is pending
- what has already been ruled out
- what would count as a useful result

Suggested prompts for intake:

- What made this issue worth revisiting now?
- What are operators seeing that does not match normal behavior?
- What have you already checked or ruled out?
- What would be the consequence of being wrong?
- What decision would this memo help you make?

Dataset capture note:

This section should preserve the operator or manager's decision framing. With permission, the intake conversation should be recorded and transcribed. The reusable asset is not the plant-specific fact pattern; it is the reasoning structure:

- cue that triggered concern
- hypotheses considered
- evidence already checked
- operational consequence of uncertainty
- decision the screening is meant to support

## 3. Scope Of Screening

Purpose:

- keep the pilot bounded
- reduce relationship risk
- make the deliverable defensible

Include:

- basin or process segment screened
- scenarios compared
- flow conditions considered
- data sources used
- outputs provided
- explicit exclusions

Recommended scope language:

`This engagement screens one sedimentation-related process question using a design-vs-current comparison. The screening focuses on relative changes in routing, redistribution, short-circuiting risk, plate-settler approach conditions, launder/upwelling risk, and related process implications. It does not provide final design recommendations, stamped engineering judgment, full CFD, full transient transport, or guaranteed water-quality prediction.`

Scenario table:

| Scenario | Description | Basis | Confidence |
|---|---|---|---|
| Design intent | Original or assumed intended condition | Drawings / design notes / client-provided basis | High / Medium / Low |
| Current condition | Observed or suspected current operating condition | Field notes / inspection / operator description | High / Medium / Low |
| Optional comparison | Proposed restoration or operating variant | Client-defined assumption | High / Medium / Low |

## 4. Data And Assumptions

Purpose:

- make the model inspectable
- protect against overconfidence
- show the buyer what uncertainty matters

Include:

- geometry inputs
- flow rates
- inlet/outlet assumptions
- baffle, wall, bypass, plate-settler, and launder assumptions
- water-quality or solids assumptions if included
- unavailable data
- assumptions that most affect interpretation

Recommended table:

| Input Area | What Was Used | Source | Screening Confidence | Why It Matters |
|---|---|---|---|---|
| Basin geometry | [dimensions] | [drawing / estimate / field note] | [tier] | Controls routing and detention proxies |
| Current bypass path | [openings / obstruction / path] | [inspection / assumed] | [tier] | Dominant uncertainty in current-state comparison |
| Flow rates | [low / typical / high] | [SCADA / operations estimate] | [tier] | Affects velocity, detention, and launder approach |
| Plate settlers | [proxy representation] | [drawing / assumption] | [tier] | Affects approach-condition interpretation |

Assumption language:

`The current-state geometry is the highest-leverage assumption in this screening. If the actual bypass opening dimensions differ materially from the assumed condition, the direction and magnitude of downstream redistribution may change. For that reason, this memo treats the result as a screening signal and recommends field verification before design or capital conclusions are made.`

## 5. Method Summary

Purpose:

- explain enough to build trust
- avoid turning the memo into a solver paper

Suggested text:

`Operational Inference used a transparent design-vs-current screening workflow to compare basin behavior under defined scenarios. The workflow uses simplified hydraulic representation and proxy metrics to identify material differences in routing, redistribution, short-circuiting risk, and downstream approach conditions. The goal is not to replace CFD, tracer testing, or engineering design review. The goal is to determine whether the observed or suspected condition is significant enough to warrant field verification, operational trial, or deeper engineering analysis.`

If using `sed_model22`, describe the boundary plainly:

- structured grid screening model
- deterministic steady comparison
- relative comparison between scenarios
- proxy RTD and hydraulic indicators
- explicit labeling of weak or non-discriminating metrics

Do not include internal repo names in a customer-facing memo unless useful. If mentioned, frame them as internal tooling:

`The screening was performed using Operational Inference's internal basin-screening workflow, which generates reproducible scenario runs, comparison artifacts, and visual outputs for review.`

## 6. Design-Vs-Current Comparison

Purpose:

- show the core result
- separate visual signal from numeric precision
- let the reader inspect what changed

Recommended figures:

- plan or longitudinal layout comparison
- velocity or routing comparison
- design/current side-by-side still
- highlighted transition, bypass, plate-settler, or launder zone
- optional low/typical/high flow comparison strip

Recommended text blocks:

```text
Design-intent condition:
[Describe expected routing and process function.]

Current-state condition:
[Describe changed routing, obstruction, bypass, or operating condition.]

Material difference:
[Name the strongest comparison signal.]

What this likely means:
[Connect the signal to process consequence.]

What this does not prove:
[Name the boundary.]
```

Interpretation rule:

- lead with comparison direction
- qualify metric strength
- call out saturated or non-discriminating metrics
- avoid treating proxy values as field-measured values

Example wording:

`The most useful signal is the relative change between scenarios, not the absolute velocity magnitude. The current-state scenario shows a different routing pattern through the transition area and a less uniform downstream distribution. That pattern is consistent with increased short-circuiting concern and less predictable plate-settler approach conditions. The result does not by itself quantify final solids removal or finished-water quality impact.`

## 7. Process Interpretation

Purpose:

- translate model output into plant meaning
- keep the memo from becoming a picture package

Recommended interpretation categories:

- hydraulics problem
- chemistry or coagulation problem
- operations problem
- instrumentation or measurement problem
- condition requiring field verification
- condition requiring engineering review

Suggested table:

| Possible Explanation | Supported By Screening? | Evidence | What Would Confirm Or Refute It |
|---|---|---|---|
| Hydraulic redistribution from current geometry | Strong / Moderate / Weak | [comparison signal] | Field dimensions, headloss, tracer, inspection |
| Coagulation or floc formation issue | Strong / Moderate / Weak | [process signal or lack thereof] | Jar testing, dose history, settled turbidity trends |
| Launder/upwelling concern | Strong / Moderate / Weak | [proxy signal] | Field velocity checks, visual observation, targeted study |
| Instrument artifact | Strong / Moderate / Weak | [data issue] | Analyzer checks, grab samples, trend review |

Language pattern:

`The screening supports [hypothesis] more strongly than [alternative] because [evidence]. However, [uncertainty] remains unresolved, so the next practical check is [action].`

## 8. Confidence And Caution

Purpose:

- make trust visible
- prevent internal embarrassment for the warm-relationship buyer
- create a repeatable language system for future pilots

Recommended confidence tiers:

| Tier | Meaning | Use In Memo |
|---|---|---|
| Credible screening signal | Input quality and model boundary are adequate for directional decision support | Can support field verification, operational review, or scoped engineering follow-up |
| Directional only | The comparison is useful, but one or more major assumptions could change interpretation | Should not be used for design or management decision without verification |
| Weak / insufficient | Input quality, model fit, or metric behavior does not support a useful conclusion | Report as inconclusive and identify missing data |

Recommended caution blocks:

### Screening Boundary

`This result is a screening conclusion. It identifies a likely process concern and helps prioritize the next investigation step. It is not a final engineering determination.`

### Proxy Boundary

`Some outputs are proxy indicators. They are useful for comparing scenarios and identifying directionally important changes, but they should not be read as field-measured values.`

### Geometry Boundary

`The current-state geometry should be verified before capital or design decisions are made. The comparison is most sensitive to [specific geometry feature].`

### Operations Boundary

`No operational change with safety, compliance, or finished-water implications should be made from this memo alone. Any trial should be reviewed through the plant's normal operating authority and engineering process.`

## 9. Recommended Next Step

Purpose:

- make the memo actionable
- avoid vague "further study recommended" language
- tell the buyer what to do next Monday

Use one primary recommendation and no more than three secondary recommendations.

Recommendation types:

- continue monitoring
- field verification
- operational trial
- consultant study
- CFD or tracer study
- geometry restoration review
- data collection before repeating screening

Recommended structure:

```text
Primary recommendation:
[One action.]

Reason:
[Why this action matches the screening result.]

What to collect:
[Specific data or observations.]

Decision after that step:
[What the next branch would be.]
```

Example:

`Primary recommendation: Verify the current-state bypass geometry before commissioning a deeper engineering study. The screening suggests that the bypass path is the dominant driver of the changed hydraulic behavior, but the actual opening dimensions are still the highest-leverage uncertainty. If field verification confirms the assumed condition, the next defensible step is a targeted engineering review or tracer/CFD scoping study. If field verification contradicts the assumption, the screening should be rerun before any downstream conclusion is made.`

## 10. Review Session Notes

Purpose:

- capture customer reaction
- capture expert reasoning for Potable-style dataset development
- convert the memo into a learning system

Include after the review call:

- outputs the client trusted immediately
- outputs the client questioned
- outputs the client rejected
- plant facts that changed interpretation
- next action the client actually intends to take
- unresolved questions

Review prompts:

- Which part of the comparison matches your experience?
- Which part does not match what you would expect?
- What would you want verified before sharing this internally?
- What action, if any, would this memo change?
- If you had to explain this to leadership, what would you say?

Dataset capture note:

The review session is the highest-value cognition capture point. The client reaction should be structured as labeled reasoning:

- trusted on first read
- needs verification
- rejected by domain judgment
- changed decision
- did not change decision

This is more valuable than synthetic Q&A because it records how a real operator or manager evaluates a technical screening artifact.

## 11. Appendix A: Scenario Inputs

Include:

- scenario descriptions
- flow rates
- model assumptions
- geometry basis
- excluded conditions
- output file or run identifiers if relevant

Keep it short. The appendix should support auditability without overwhelming the buyer.

## 12. Appendix B: Figures And Output Notes

Include:

- figure captions
- what each figure shows
- what each figure does not show
- whether the figure is design-facing, operations-facing, or leadership-facing

Caption pattern:

`Figure X compares [scenario A] and [scenario B] under [flow condition]. The figure is intended to show relative routing and distribution differences. It should not be read as a calibrated CFD prediction of local turbulence or measured velocity.`

## 13. Appendix C: Research And Dataset Use Permission

This section should be reviewed by counsel or a trusted legal advisor before first use.

Core principle:

- client findings remain confidential
- generalized methodology and anonymized reasoning structures may be reused only if permission is explicit
- public dataset use must be opt-in or clearly disclosed with an opt-out mechanism before money changes hands

Draft engagement language for legal review:

`Client-specific findings, plant identity, operating data, and non-public materials will remain confidential to the client. Operational Inference may use generalized methodology, anonymized decision-reasoning patterns, and non-identifying screening structures for internal research, product improvement, and public educational or dataset work, unless the client opts out in writing. Any public case study or public dataset record derived from this engagement will remove client identity, plant identity, and sensitive operational details unless separate written permission is obtained.`

Stronger version for case-study rights:

`In exchange for pilot pricing, the client grants Operational Inference permission to publish an anonymized case study based on the engagement. The case study will not identify the client, plant, staff, location, or sensitive operating details without separate written approval. The client may review the anonymized case study before publication for confidentiality concerns.`

## First Pilot Pricing And Value Exchange

The first pilot does not have to optimize for cash. It should optimize for proof, feedback, reference value, and reusable learning.

Use a simple tradeoff:

- if the client allows structured feedback, recorded intake/review sessions, anonymized research use, and possible anonymized case-study use, the first pilot can be free or nominal cost
- if the client wants fully private work with no research, dataset, reference, or case-study value, it should be a paid pilot

Recommended pilot options:

| Option | Price | Client Gets | Operational Inference Gets | When To Use |
|---|---:|---|---|---|
| Validation pilot | `$0` | Full screening memo and review session | structured feedback, recorded calls with permission, anonymized research/case-study rights, reference potential | first 1-2 trusted validation partners |
| Nominal-cost pilot | `$1,500-$3,500` | Full screening memo and review session | same as validation pilot, plus some buyer commitment | when free feels too casual but procurement friction should stay low |
| Paid pilot | `$7,500+` | Full screening memo and review session | normal commercial learning, no automatic discount expectation | when confidentiality is tighter or the buyer is already serious |

Suggested language:

`I am doing one or two validation pilots before this becomes a standard paid screening engagement. I can do the first version at no fee or nominal cost if we structure it as a learning pilot: you get the memo and review session, and I get permission to record the intake/review calls, use anonymized reasoning patterns for research and dataset development, and potentially prepare an anonymized case study for your review. If you prefer the work to remain entirely private with no research or case-study use, I would treat it as a paid pilot.`

The first validation pilot should still produce:

- one polished deliverable
- one credible anonymized case package
- one tested scope boundary
- three to five strong expert-reasoning records if capture works
- a clearer answer on whether screening pilots and Potable-style dataset growth can run in parallel

Do not present a free pilot as a favor or apology. Present it as a defined value exchange.

## Pre-Sale Checklist

Before the first customer conversation, prepare:

- one completed mock memo using real or plausible stand-in geometry
- one clean one-page scope summary
- one standard intake questionnaire
- one review-session note template
- one draft confidentiality and research-use clause for legal review
- one clear pilot option sheet explaining free / nominal / paid tradeoffs
- one statement of what the pilot will not promise

Do not begin with a pitch deck. Begin with the deliverable artifact.

## First Conversation Script

Use plain language:

`I am testing a fixed-scope plant-performance screening engagement for sedimentation-related questions. The point is to compare design intent against current behavior and produce a short memo that helps decide whether the issue is hydraulic, operational, chemistry-related, or worth deeper engineering review. I built a sample memo so you can see exactly what the deliverable would look like. The numbers here are illustrative. If this would be useful, I would like to do one real version at pilot pricing and use your feedback to tighten the workflow.`

Then ask:

- Does this memo format answer a question you actually have?
- What would make it safer or more useful to share internally?
- What part would you distrust or need verified?
- Is there one basin or process question where this would be worth trying?

## Quality Bar For Pilot One

Pilot one is successful only if:

- the buyer can explain the result to someone else
- the memo does not overclaim
- the next-step recommendation is specific
- the scope does not expand into open-ended consulting
- the review session produces usable feedback
- the engagement strengthens, rather than spends down, the warm relationship

Revenue is secondary. The real output is a trusted case artifact and a tested delivery system.
