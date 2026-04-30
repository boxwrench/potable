# Combined Research Synthesis

Date: 2026-04-29

## Purpose

This memo combines four research reports in `docs/new research/` and extracts:

- major ideas introduced by each report
- areas of consensus
- areas of disagreement
- strategic tensions that still need founder judgment

The goal is not to average the reports into mush. The goal is to preserve the strongest ideas while making the conflicts explicit.

## Source Reports

1. `Potable Water Treatment Software.md`
2. `UNDER_DIGITIZED_WORKFLOWS_POTABLE_WATER.md`
3. `Water Treatment Software Opportunity Analysis.md`
4. `Water Treatment Workflow Digitization Opportunities.md`
5. `# Software-eating water where the real wedges are.md`

## Executive Takeaway

Across all four reports, the market thesis is real: potable water has expensive, under-digitized workflows where software can replace manual spreadsheets, fragmented records, consultant-heavy screening, or operator memory.

The reports do not agree on the best initial wedge.

Three wedge theses emerged:

1. Narrow engineering screening for treatment-process problems, especially sedimentation, filtration, and coagulation.
2. Small-system compliance and administrative automation, especially CT, MOR, CCR, survey readiness, and regulatory workflow.
3. Operator knowledge, troubleshooting, and institutional-memory products built as copilots or structured knowledge systems.

The first thesis is the strongest fit for a differentiated, defensible product tied to your unique capability.
The second thesis is the strongest fit for broad buyer count and near-term operational pain.
The third thesis is the strongest fit for the workforce narrative and product breadth, but the weakest as a standalone moat unless grounded in specific workflows.

The fifth report materially sharpened the second thesis and added a more disciplined variant of it:

4. Regulatory-anchored plant-performance software, starting with CT/disinfection profiling, then PFSW reporting, then PFAS screening.

## Report-by-Report Extraction

### 1. Potable Water Treatment Software

Core position:
- Best first wedge is a narrow, explainable, first-pass engineering screening product.
- Sedimentation basin diagnosis and optimization is the best initial category.
- Filter troubleshooting and coagulation are the most natural adjacencies.
- Operator copilots and digital twins should not be the first company wedge.

Strongest ideas:
- The moat is not the equations alone; it is workflow productization, explainability, evidence traceability, and structured handoff to humans.
- The right product shape is screening, not autonomous optimization.
- Consultant-heavy process diagnosis is the best replacement pattern.
- Sedimentation has strong downstream adjacency into filters, chemistry, and scenario tools.

Risks called out:
- Small utilities are fragmented and capacity-constrained.
- Trust and liability kill black-box tools.
- Digital twin and simulator categories are real but too heavy for the first wedge.

### 2. UNDER_DIGITIZED_WORKFLOWS_POTABLE_WATER

Core position:
- The most commercially attractive workflows may be small-system compliance and operations software, not engineering modeling.
- CT compliance calculation is ranked first.
- MOR assembly, LCRR/LCRI inventory, coagulant optimization, and sanitary survey readiness are all high-value workflow gaps.

Strongest ideas:
- The small-system market is materially underserved by enterprise vendors.
- The same operator at a small plant often owns CT, MOR, survey prep, chemical logs, and compliance tracking.
- Workflows 1-5 form a natural operational/compliance bundle.
- Coagulant optimization is flagged as highly defensible because no strong software incumbent owns it.

Risks called out:
- Regulatory-wave products can be time-limited.
- Some administrative workflows are large but low-willingness-to-pay unless bundled.
- Knowledge transfer is strategically important but hard to monetize cleanly.

### 3. Water Treatment Software Opportunity Analysis

Core position:
- Operator knowledge retrieval and troubleshooting is the strongest long-term strategic path.
- A simpler screening tool such as PFAS or CT could serve as the initial commercial wedge.
- Sedimentation is attractive, but mainly as a consultant-facing screening tool rather than the top operating-system wedge.

Strongest ideas:
- The strongest copilot opportunity is grounded RAG over plant manuals, logs, and SCADA context.
- Corrosion-control desktop studies and source-water blending are strong neglected technical workflows.
- Trust depends on explicit citations, visible math, and avoidance of PE-stamp liability claims.
- There is a real category of "modernizing old engineering desktop tools" such as RTW/STASOFT-type chemistry tools.

Risks called out:
- Coagulant/jar testing may face free-tool competition from chemical vendors.
- Copilot categories are under-served but rapidly commoditizing.
- Buyers reject anything that looks like black-box plant design.

### 4. Water Treatment Workflow Digitization Opportunities

Core position:
- The biggest software opportunities extend beyond treatment-process screening into compliance, SCADA, SOP capture, asset workflows, and broader utility operations.
- PFAS compliance, lead service line workflows, alarm rationalization, SOP generation, and coagulant optimization are all top opportunities.

Strongest ideas:
- Workforce loss plus regulatory complexity is the macro driver.
- AI can convert unstructured plant records, video, and lab outputs into structured operational systems.
- SOP capture from video is an unusually strong knowledge-transfer concept.
- SCADA alarm fatigue and operator overload are real workflow problems with large practical cost.

Risks called out:
- Some opportunities pull the company toward broader utility software rather than treatment-specific depth.
- Several categories require deeper integration, longer deployment, or competition with large incumbents.
- Venture framing can push the scope too wide too early.

### 5. Software-eating water: where the real wedges are

Core position:
- The single best wedge is CT/disinfection compliance plus PFSW reporting, expanded into PFAS screening within 12 months.
- Sedimentation is real but should be a platform module, not the first standalone company wedge.
- Standalone operator copilots, full digital twins, and autonomous coagulation control are all poor first moves.

Strongest ideas:
- The founder's rare asset is operator credibility, and it should be spent on workflows with clear budget, recurring relevance, and public methodology.
- The best packaging plays are EPA-published methods and state-format deliverables that no one wants to commercialize cleanly.
- PFSW is a high-signal, founder-fit niche with recurring ritual value and credibility compounding.
- The best 3-year sequence is CT -> PFSW -> PFAS -> continuous CPE -> filter analytics -> DBP -> copilot layer.
- The company advantage may come less from "vertical AI" and more from doing the painful state-by-state regulatory packaging work that others avoid.

Risks called out:
- State-template heterogeneity can become a treadmill.
- OT/SCADA integration and cybersecurity requirements are hard gates.
- Rare-event engineering studies do not automatically translate into recurring ARR.
- Operator copilot has no clean budget code and weak initial procurement fit.

## Consensus

### Market-level consensus

- The potable water market contains real, expensive, under-digitized workflows.
- Workforce retirement and knowledge loss are major structural drivers.
- Regulatory complexity is accelerating, especially around PFAS and lead/copper.
- Public-method workflows with bad packaging are unusually attractive product territory.
- Existing software is fragmented, expensive, legacy, hardware-tied, or badly matched to the practical workflow.
- Utilities do not want black-box AI making uncontrolled treatment decisions.
- Human-in-the-loop, explainable products are the viable path.

### Product-form consensus

- Narrow workflow tools are stronger than broad "water AI platform" positioning.
- Packaging, usability, and workflow design matter as much as underlying technical logic.
- The product has to show its work.
- The first useful category is decision support, not autonomous control.
- Good UI is a meaningful wedge because current tools are often poor or nonexistent.
- A product tied to a regulatory deliverable has a cleaner buyer and validation story than a vague productivity or insight product.

### Defensibility consensus

- Defensibility will come from workflow integration, validation, structured case libraries, and accumulated plant-specific context.
- Generic copilots alone are weak moats.
- Deep domain framing is required to avoid commoditization.

## Disagreements

### Best first wedge

`Potable Water Treatment Software.md` says:
- start with sedimentation screening

`UNDER_DIGITIZED_WORKFLOWS_POTABLE_WATER.md` says:
- start with CT, MOR, or other small-system compliance workflows

`Water Treatment Software Opportunity Analysis.md` says:
- long-term winner is operator knowledge copilot
- initial wedge could be PFAS or CT

`Water Treatment Workflow Digitization Opportunities.md` says:
- PFAS, LCRI, alarm rationalization, SOP generation, and coagulant optimization are all top-tier candidates

`# Software-eating water where the real wedges are.md` says:
- start with CT/disinfection compliance
- pair it with PFSW performance reporting
- expand into PFAS
- treat sedimentation as a later module, not the wedge

### Best buyer

Competing buyer hypotheses:
- treatment superintendent / process engineer
- small-system chief operator
- utility compliance manager
- consultant engineer
- utility operations director

This matters because product shape, pricing, data access, and sales motion all change with the buyer.

### Daily workflow vs episodic high-value workflow

Some reports prefer:
- daily-use tools with high frequency and lower ticket size

Others prefer:
- episodic but high-value technical screening tied to major engineering or compliance decisions

This is a core business-model disagreement, not a minor ranking difference.

The fifth report strengthens the argument that recurring daily or annual compliance/performance rituals beat rare-event engineering tools as a company entry point.

### Utility-first vs consultant-first go-to-market

Some reports imply:
- sell directly to utilities as a recurring software product

Others imply:
- start with consultants or engineer-adjacent users who already perform the hard analysis and can tolerate more technical products

### Copilot as company vs copilot as feature

Some reports treat knowledge systems as:
- the company thesis

Others treat them as:
- a later layer that becomes more valuable after workflow engines exist

The latest report is the strongest push yet toward "copilot as capstone, not wedge."

## Strategic Tensions

### Tension 1: Differentiation vs market size

Sedimentation and engineering screening are more differentiated and more founder-specific.
CT, MOR, and compliance assembly may have larger buyer counts and simpler pain.

This is a tension between:
- unique wedge with stronger moat
- broader market with easier immediate problem statements

The new report refines this tension:
- CT/PFSW may not be broader only in buyer count; they may also create better recurring usage and cleaner procurement than sedimentation.

### Tension 2: Daily usage vs hard-to-replicate value

Compliance tools can be used frequently, but may be easier to copy and harder to defend.
Engineering screening may be used less often, but can anchor stronger trust and deeper product identity.

### Tension 3: Operator product vs engineer product

Operator-facing products need extreme simplicity, trust, and fast onboarding.
Engineer-facing products can tolerate more technical complexity and may justify higher pricing.

Choosing one changes the company voice and product architecture.

The fifth report proposes a hybrid answer:
- sell a compliance/performance workflow first
- use that installed base and trust to add deeper engineering modules later

### Tension 4: Workflow automation vs expert reasoning

Administrative compliance products win on automation.
Engineering/process products win on reasoning and diagnosis.

These are different product muscles. Trying to do both too early will blur the company.

### Tension 5: Venture-scale platform vs disciplined wedge

Some reports drift toward a broad utility platform.
The strongest ideas in the full set still support a disciplined first wedge followed by adjacencies.

## Cross-Report Opportunity Clusters

### Cluster A: Engineering screening and scenario tools

Repeated ideas:
- sedimentation screening
- filter troubleshooting
- coagulation optimization
- corrosion-control desktop tools
- source-water blending modeling
- DBP forecasting
- continuous CPE / plant performance self-assessment

Interpretation:
- This is the highest-fit cluster for your domain depth and for the "used to be hard, so people paid consultants" thesis.

### Cluster B: Compliance and administrative workflow automation

Repeated ideas:
- CT calculation
- MOR assembly
- CCR generation
- sanitary survey readiness
- PFAS tracking
- LCRR/LCRI workflows
- disinfection profiling
- state-format reporting
- PFSW reporting

Interpretation:
- This is the clearest small-system SaaS cluster.
- It is practical and monetizable, but it is less uniquely yours unless you build an unusually good product system.

The fifth report upgrades this cluster by arguing that some of these are not just admin tasks but entry points into a deeper plant-performance platform.

### Cluster C: Knowledge systems and workforce continuity

Repeated ideas:
- troubleshooting copilot
- shift turnover
- SOP generation
- knowledge retrieval
- training support

Interpretation:
- This is a powerful narrative and strong long-term layer.
- On its own it risks becoming a generic AI wrapper unless tied to specific workflows and validation.

## Current Best Synthesis

The strongest integrated interpretation of the four reports is:

1. The company should start in a narrow water-treatment decision-support wedge, not as a generic AI company.
2. The highest-fit wedge for founder differentiation remains engineering screening, especially sedimentation plus adjacent treatment-process diagnostics.
3. The product should be explicitly framed as first-pass screening and handoff, not autonomous design or autonomous control.
4. Knowledge-system features are valuable, but they become much stronger after a workflow product exists.
5. Compliance and small-system workflows may be a second product family or a separate line, but they should not automatically displace the more differentiated wedge unless customer interviews prove much stronger pull.

After adding the fifth report, the strongest integrated interpretation changes slightly:

1. The company should still start in a narrow water-treatment decision-support wedge, not as a generic AI company.
2. There are now two serious candidates for the first wedge:
   - sedimentation-led engineering screening
   - CT/disinfection-led regulatory plant-performance software
3. The new strongest alternative to sedimentation is not generic compliance SaaS; it is a more specialized regulatory/performance platform built around CT, PFSW, and then PFAS.
4. Knowledge-system features remain a later layer, not the initial company identity.
5. The central open question is now whether founder differentiation is better expressed through:
   - technical process diagnosis first
   - or operator-credible regulatory/performance packaging first

## Where The Reports Changed Or Improved The Thesis

- The small-system angle is more important than earlier intuition suggested.
- CT and MOR are real commercial opportunities even if they are not the most differentiated opportunities.
- Corrosion-control desktop studies and source-water blending deserve more attention than they had initially.
- Consultant-facing products may be a more realistic early channel than previously assumed.
- Knowledge capture from operator behavior, logs, and video is a stronger long-term concept than a generic chatbot.
- PFSW and continuous CPE emerged as stronger founder-fit opportunities than they appeared in the first pass.
- CT is now the most repeated candidate for "best first wedge" across the non-sedimentation reports.
- Sedimentation still looks strategically strong, but less obviously the best first ARR engine than before.

## Working Decision Framework

Use these tests when deciding the first product:

1. Is this a workflow you are unusually qualified to build correctly?
2. Is the buyer pain strong enough to pay before perfect validation?
3. Does the product need to be used daily, or is episodic high-value acceptable?
4. Can the UI make the task materially easier than the current workaround?
5. Does trust come from visible physics, visible citations, or visible workflow control?
6. Can this wedge expand naturally into adjacent modules?

## Provisional Recommendation

Based on the combined set, the most coherent current thesis is:

- Parent thesis: operational decision-support for water treatment
- Initial wedge options now narrow to two:
  - CT/disinfection compliance and plant-performance reporting
  - engineering screening for treatment-process diagnosis
- Strongest initial candidate by differentiation: sedimentation screening with explicit path into filtration and coagulation
- Strongest initial candidate by recurring workflow and procurement clarity: CT/disinfection compliance with path into PFSW and PFAS
- Secondary opportunity family: compliance and small-system workflow automation beyond the first wedge
- Long-term layer: knowledge systems, troubleshooting support, and training/continuity features built on top of real workflow products

## Next Founder Questions

1. Do you want the first buyer to be a utility operator, a treatment superintendent, or a consulting engineer?
2. Are you optimizing for daily usage or highest defensibility?
3. Do you want a wedge that is strongly founder-specific or a wedge with broader immediate TAM?
4. Would you rather sell a screening report workflow first or a compliance automation workflow first?
5. Is `Potable` the knowledge/data layer while `Operational Inference` becomes the product/company layer?
6. Is PFSW a better credibility and revenue bridge than sedimentation as the first public product story?
7. Do you want to win first on plant-performance reporting or on hard process diagnosis?
