# Decision Memo: Process-Screening First

Date: 2026-04-29
Status: Working recommendation

## Decision

Operational Inference should start with a **process-screening and engineering decision-support wedge**, not a compliance-first or regulatory-software-first wedge.

The current best expression of that wedge is:

- practical design-vs-current screening for sedimentation and related plant-performance problems
- transparent first-pass diagnosis of likely hydraulic and process failure modes
- structured outputs that support escalation to engineering review when warranted

This means the company should **not** begin by centering CT compliance, MOR tooling, or generalized regulatory reporting, even though those categories are commercially real.

## Short Version

The reason is not that compliance software is a bad business. The reason is that compliance software is **not the company only Keith is positioned to build**.

The strongest founder-specific advantage in the current project set is:

- operator-authored process understanding
- credible translation of old engineering methods into usable software
- practical judgment about what is screening, what is proxy, and what should still escalate to engineering review

That advantage is visible already in `sed_model22` and in the strategic posture documents. It is much less visible in a compliance-first product, where the company would compete more on template coverage, state-by-state formatting, and workflow maintenance than on uniquely hard domain insight.

## Why This Recommendation Fits The Existing Project

### 1. The current product work already points here

The clearest product-direction statement in [README.md](C:/Github/sed_model22/README.md) is not "build a compliance tool." It is:

- compare what a basin was designed to do versus what it is doing now
- stay technically honest and operationally legible
- become a transparent basin-screening workflow useful for real decisions

That is already the right shape.

The current repo language explicitly frames the product as:

- screening, not full CFD
- decision support, not autonomous control
- understandable to operators, engineers, and non-specialist decision-makers

That is exactly the commercial position most consistent with the external research.

### 2. The roadmap is already decision-support oriented

[V0_3_ROADMAP.md](C:/Github/sed_model22/docs/V0_3_ROADMAP.md) makes the next move explicit:

- move from pure hydraulic comparison toward decision-complete workflow
- connect hydraulic changes to likely solids-removal consequences
- preserve honesty about what is still proxy and what is not

This is the shape of a real product wedge:

- not more equations for their own sake
- not a premature digital twin
- not a generic AI wrapper
- a more decision-useful screening workflow

That is exactly the sort of wedge the strongest research report recommended, even when the reports disagreed on first category.

### 3. The dev log shows the right product instincts

[DEVLOG.md](C:/Github/sed_model22/docs/DEVLOG.md) repeatedly reinforces the most important commercial behavior:

- explicit caution language
- separation of directional signal from literal values
- focus on practical study outputs
- emphasis on leadership-facing and engineering-facing communication
- refusal to let visual sophistication outrun representational honesty

This matters commercially. In this market, trust is not built by sounding advanced. Trust is built by being clear about what the model can and cannot claim.

That instinct is stronger strategic raw material than a faster path into state-template compliance work.

### 4. The strategic posture document supports founder-specific differentiation

[STRATEGIC_POSTURE_April2026_v2.md](C:/Github/potable/docs/potable_project_files/STRATEGIC_POSTURE_April2026_v2.md) argues that the moat is the combination of:

- T5 operator credibility
- public writing
- live domain relationships
- research literacy
- ability to build on both sides of the water-AI bridge

That is not a generic compliance-software moat.
That is a moat for turning difficult, specialist-heavy process knowledge into usable tools.

If the moat is really "who Keith is," then the first product should spend that advantage where it matters most.

## What The Research Supports

### What the research agreed on

Across the combined research set, there was broad agreement on the following:

- water has real, expensive, under-digitized workflows
- black-box AI is a non-starter
- narrow workflow products are stronger than broad "water AI" positioning
- workflow packaging and explainability matter as much as raw technical logic
- human-in-the-loop decision support is the viable product form

These points are summarized in [COMBINED_RESEARCH_SYNTHESIS.md](C:/Github/potable/docs/new%20research/COMBINED_RESEARCH_SYNTHESIS.md).

### Where the research disagreed

The main disagreement was over the **first wedge**, not over the existence of opportunity.

The reports split into three camps:

1. process-screening and engineering decision support
2. compliance and reporting automation
3. operator knowledge / copilot systems

The latest report, [# Software-eating water where the real wedges are.md](C:/Github/potable/docs/new%20research/%23%20Software-eating%20water%20where%20the%20real%20wedges%20are.md), makes the strongest case for CT/PFSW first and treats sedimentation as a later module.

That report is commercially serious and should not be dismissed. It sharpened the case for:

- recurring workflows
- cleaner procurement
- regulatory anchoring
- state-format deliverables as a practical entry path

But it does **not** overturn the founder-fit logic.

### Why I am not choosing the compliance path first

The compliance-first thesis is attractive because it offers:

- daily or monthly usage
- obvious pain
- known reporting obligations
- faster path to recurring workflow gravity

But it also creates three structural problems early:

1. It pushes the company toward state-by-state template maintenance and regulatory heterogeneity as a core operating burden.
2. It makes differentiation rely more on packaging discipline than on uniquely difficult domain insight.
3. It risks teaching the market that Operational Inference is a compliance vendor before it is known as a plant-performance and decision-support company.

That is the central reason to stay wary.

The process-screening thesis has the opposite profile:

- slower initial buying events
- higher trust burden
- more work to structure recurring value

But it better matches the deepest founder-specific advantage and better protects the long-term company identity.

## The Real Tradeoff

This is not "good business" versus "bad business."
It is:

- better immediate workflow frequency and easier buyer clarity
versus
- better differentiation and stronger founder-specific identity

If the company were being built by a generic software founder, I would probably lean much harder toward CT/PFSW or another compliance-adjacent product.

Because this company is being built by Keith, with the current project base, I lean toward process screening.

## The Correct Framing For The First Product

The product should **not** be framed as:

- CFD replacement
- basin design software
- autonomous plant optimization
- digital twin
- regulatory compliance platform

It should be framed as:

- first-pass plant performance diagnosis
- design-vs-current comparison
- practical screening for whether a condition warrants deeper engineering review
- transparent explanation of likely hydraulic and process consequences
- structured handoff for consultants, engineers, and internal plant leadership

That framing is already consistent with the `sed_model22` repo.

## How To Avoid The Biggest Weakness Of A Sedimentation-First Path

The main weakness of a sedimentation-first wedge is that basin studies can be episodic.

To avoid building a rare-event tool with weak ARR, the wedge has to be designed as the front door to a broader **plant-performance workflow**, not as a one-off modeling utility.

That means the likely expansion path should be:

1. sedimentation / design-vs-current screening
2. filter-performance interpretation
3. coagulation or floc screening support
4. continuous performance assessment
5. selected reporting or compliance-support layers later, only where they reinforce the plant-performance system

This is different from starting with compliance.
In this sequence, compliance becomes a support layer, not the company identity.

## What This Means For Product Strategy

### First product family

Build around:

- process diagnosis
- screening workflows
- auditable comparison outputs
- decision-support reports

### First buyer hypothesis

Best early buyer candidates are likely:

- treatment superintendent
- plant manager
- engineering manager
- consultant engineer for selected use cases

The product should not initially assume the solo small-system operator as the main buyer.

### Trust model

Trust should come from:

- visible assumptions
- visible geometry and scenario structure
- visible confidence / caution language
- side-by-side comparisons
- explicit statement of when to escalate

Again, this is already how the `sed_model22` docs are written.

## What Gets Deferred

The following should be treated as later, not first:

- standalone operator copilot
- broad knowledge system as the company identity
- full compliance platform
- state-by-state reporting automation as the core wedge
- full digital twin claims
- autonomous coagulation control

These may all become useful later.
None should define the first market identity.

## Recommendation

Operational Inference should proceed as a **water-treatment decision-support company** with a **process-screening-first** wedge.

The initial commercial identity should be:

- practical plant-performance diagnosis
- screening before full engineering review
- tools that make hard old methods usable

Not:

- generic AI for water
- compliance software for utilities
- reporting automation company

## Bottom Line

The company should start where the moat is strongest, not where the workflow is easiest to count.

The current project documents, especially [README.md](C:/Github/sed_model22/README.md), [V0_3_ROADMAP.md](C:/Github/sed_model22/docs/V0_3_ROADMAP.md), [DEVLOG.md](C:/Github/sed_model22/docs/DEVLOG.md), and [STRATEGIC_POSTURE_April2026_v2.md](C:/Github/potable/docs/potable_project_files/STRATEGIC_POSTURE_April2026_v2.md), all support the same conclusion:

the distinctive thing here is not compliance packaging alone.
The distinctive thing is operator-authored, technically honest, decision-useful process screening.

That is the wedge to protect.

