# Software-eating water: where the real wedges are

The single best wedge for an operator-founded startup in U.S. drinking water is **CT/disinfection compliance and Partnership for Safe Water (PFSW) plant performance reporting**, expanded into **PFAS treatment screening** within 12 months. These two anchor a credible 3-year path that compounds operator credibility into a defensible plant-performance platform. Avoid leading with autonomous coagulation control, full digital twins, sedimentation CFD-killers, or a standalone operator copilot — those are graveyards in this market for reasons documented below.

Drinking water software is a sleepy oligopoly at the top (Autodesk Innovyze, Veralto/Hach/Aquatic Informatics, Bentley, Trimble, AVEVA) with most innovation crowded into compliance windows (LCRR/LCRI: BlueConduit, 120Water, Trinnex) and customer engagement (WaterSmart/VertexOne). Inside the treatment plant fence — chemistry, hydraulics, filter physics, operator decisions — productized software is genuinely thin. Autodesk killed Info360 Plant in December 2025 after only ~3 years, which is the clearest signal that the inside-the-fence opportunity is real **and** unforgiving. The founder's 14-year senior operator credibility is the rarest input in this market and should be spent precisely, not sprayed.

What follows is concrete, skeptical, and tries to keep "intellectually interesting" separate from "sells."

---

## Section 1: Market map — 15 under-digitized workflows

The table below is the heart of the analysis. AI helpfulness is rated as low/med/high based on whether modern software materially compresses the workflow versus whether spreadsheets are already adequate.

| # | Workflow | Buyer | User | Current workaround | Why it's still hard | Frequency | Cost of error | Urgency | Alternatives | AI/SW helps? | Commercial note |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **Daily CT compliance + LT1 disinfection profiling** | Plant Mgr / Compliance Mgr | Lead operator | TCEQ-style macro Excel, state-specific MOR templates | Multi-zone summation, state format heterogeneity, brittle macros, audit risk | Daily calc, periodic profile | Boil-water notice, SDWA violation | High (continuous) | EPA SWAT, Hach Claros RTC-C/DC | High — pure data engineering | Cleanest Excel→SaaS play in the stack |
| 2 | **PFSW Phase III/IV plant performance reporting** (sedimentation + filter goals) | Plant Mgr / Engineering Mgr | Plant engineer | AWWA locked Excel templates, 40–80 hr/yr engineer effort | Manual filter profiling, ripening/UFRV trend analysis, narrative writeup | Annual + 5-yr deep dive | Loss of recognition, capital project pretext | Medium (voluntary but career-marker) | Consultant @ $40–150K | High | ~250 PFSW utilities + ~1,000 candidates; founder-fit is exceptional |
| 3 | **PFAS treatment alternatives screening (GAC vs IX vs RO)** | GM + Engineering Mgr | Consulting engineer or in-house engineer | EPA AdDesignS / PSDM Python (UX-hostile), Carollo Blue Plan-it (proprietary), Hazen internal tools | Pore-surface diffusion physics, regen/disposal economics, vendor-neutral comparison | One-time per source 2024–2031 | $5–75M wrong capital decision | Very high (NPDWR) | $100–500K consultant study | High — wrap free EPA models in clean UI | Highest urgency window in entire stack |
| 4 | **Coagulant selection and jar-test interpretation** | Plant Mgr | Lead operator / lab tech | Phipps & Bird jar tests, Edzwald diagram, M37 manual | Operator distrust of black-box dosing (Pluto AI graveyard), seasonal NOM shifts | Weekly + seasonal | DBP exceedance, filter run loss | Med-high | Hach RTC-COAG, SCDs | Med — selection screening yes, autonomous control no | Founder-fit; avoid autonomous control framing |
| 5 | **Filter performance / UFRV / backwash troubleshooting** | Plant Mgr | Plant operator | SCADA dashboards (PI Vision custom), AWWA M37, Excel | Filter profiling is manual; ripening/breakthrough analysis ad hoc | Continuous + assessments every 5 yrs | Filter failure, IFE turbidity violation | Med (continuous) | Consultant CPE/eval @ $40–150K | High | Severely underserved; no dominant vendor |
| 6 | **Sedimentation basin diagnosis (pre-CFD screening)** | Engineering Mgr | Process engineer | Camp-Hazen + L:W tables in Excel, then $50–300K CFD | CFD requires PhD users; tracer studies $15–60K each | Episodic; 5–10 yrs between studies | Capital misallocation, CT failure | Med | Consultant CFD studies | Med — ROM + RTD library yes, full CFD no | Real gap but rare buying event; better as platform module |
| 7 | **DBP (TTHM/HAA5) Stage 2 LRAA forecasting** | Compliance Mgr | Compliance analyst | EPA WTP Model 2.0 (2001 Excel), Carollo Blue Plan-it | Empirical models, locational running avg, treatment what-if | Episodic + monthly monitoring | LRAA exceedance, public notice | Med | Consultant DBP study $60–250K | Med-high | EPA model is free IP; UX wrap is the play |
| 8 | **Continuous CPE / Composite Correction self-assessment** | GM / Plant Mgr | Plant team | EPA AWOP CPE delivered free by state contractor or $30–80K private | Methodology is public but tedious; PLF analysis takes 3-person team 2–4 days | Every 3–5 yrs ideal, rarely done | $5M unnecessary capital project | Med | Process Applications Inc. (EPA prime) | High | Underrated wedge — public method, captive data |
| 9 | **OCCT corrosion-control re-optimization (LCRI)** | Compliance Mgr / Eng Mgr | Engineer | EPA spreadsheets, RTW Model, harvested-pipe scale analysis | Schock lead solubility, DIC/Ca/orthophosphate speciation | Per AL exceedance + Nov 2027 LCRI | $50–500K consultant + LCRI noncompliance | High | Corona, Hazen, B&V, CDM, Arcadis | Med | Niche but real budget |
| 10 | **HAB / cyanotoxin response playbook** | Plant Mgr | Operator | EPA CyAN free, NOAA forecast, Hach phycocyanin, ad hoc PAC dosing | Source-specific risk thresholds, treatment-decision rules | Seasonal at HAB-prone sources | Toledo 2014 scale event | High during bloom season | EPA CyAN + utility ad hoc | Med | ~100 utilities; low TAM, high pain |
| 11 | **Reservoir intake selection / depth-stratified WQ** | Plant Mgr / Source Water Mgr | Engineer | CE-QUAL-W2 (free, $80–300K consultant calibration) | 2D reservoir hydro/WQ; intake switching decisions | Daily/seasonal at stratified reservoirs | DBP precursors, taste/odor events | Med | USGS gauges + USACE model + judgment | Med | Niche, sticky once deployed |
| 12 | **Backwash hydraulic and recovery-water optimization** | Plant Mgr | Plant operator | Cleasby-Fan textbook math, SCADA trending | No commercial product; backwash strategy is tribal knowledge | Daily | Filter fouling, recycle stream issues | Low-med | None | Med | Module within filter-analytics product |
| 13 | **Source-water turbidity event prediction (storm response)** | Plant Mgr | Operator | USGS NWIS, NOAA NWS, ad hoc operator rules | Watershed-specific, requires sensor history | Episodic (storms) | Filter ripening failure, raw-water bypass | Med | Custom utility-built models | Med | Best as feature, not standalone product |
| 14 | **Hydraulic transient / surge analysis** | Engineering Mgr | Specialist consultant | Bentley HAMMER, AFT Impulse, KYPipe | Method-of-characteristics physics, infrequent | Per major capital change | Pipe failure, $1M+ damage | Low (event-driven) | Mature commercial | Low | Mature; not a wedge |
| 15 | **Plant-wide what-if scenario / capacity rerating** | Engineering Mgr / GM | Engineer | Hydromantis MantisPW, BioWin (WW), Carollo Blue Plan-it, spreadsheets | Multi-unit-process integration, cost layer | Every 5–10 yrs (master plan) | $200K–$5M study + downstream capital | Med | Consultant master plan $200K–$1.5M | Med-high | Long-term platform play |

### Startup-attractiveness ranking (1 = most attractive)

1. **CT compliance + LT1 profiling SaaS** — daily pain, public methodology, brittle Excel incumbents, low scientific risk
2. **PFAS GAC/IX screening tool** — highest urgency, highest consultant fees, free EPA model to wrap, time-bounded but real
3. **PFSW Phase III/IV plant performance reporting** — narrow buyer set but exceptional founder-fit and recurring use
4. **Continuous CPE / self-assessment** — public method, displaces $30–80K consultant, expands into a true plant-performance platform
5. **Filter performance / UFRV / backwash analytics** — severely underserved, daily relevance, natural pairing with CPE
6. **DBP Stage 2 LRAA forecasting** — wraps EPA WTP Model, fits inside CT/PFSW platform
7. **Coagulant selection screening (not autonomous control)** — pre-jar-test decision support, avoids Pluto graveyard
8. **OCCT corrosion-control re-optimization** — LCRI tailwind, smaller TAM, real consultant fees
9. **Sedimentation basin pre-CFD screening** — real gap, rare buying event; module within platform, not standalone
10. **Plant-wide what-if / capacity rerating** — large fees but long sales cycles
11. **HAB response playbook** — high pain, low TAM, regional
12. **Reservoir intake / depth-stratified WQ** — sticky niche
13. **Backwash optimization** — feature, not company
14. **Turbidity event prediction** — feature, not company
15. **Hydraulic surge** — mature, do not enter

---

## Section 2: Existing solutions — category heat map

| Category | Major vendors | What they really do | Sell to | Pricing | Strengths | Weaknesses | Startup room | Crowding verdict |
|---|---|---|---|---|---|---|---|---|
| **Sedimentation basin screening** | ANSYS Fluent, Flow-3D, OpenFOAM, COMSOL; Carollo Blue Plan-it (proprietary) | Custom CFD for one-off basin studies | Engineering firms | $30–100K/yr per CFD seat; $50–300K per study | Physics rigor | PhD users; rare buying events | Empirical ROM + RTD library + clean UI | **Under-served — only superficially served** |
| **Filter troubleshooting/optimization** | Hach Claros (data only), AVEVA PI Vision custom, AWWA M37 + Excel | Generic dashboards; manual UFRV/profiling | Plant Mgr | n/a productized | None purpose-built | No dedicated commercial product | Filter analytics SaaS with PFSW outputs | **Severely under-served** |
| **Chemical feed optimization** | Hach Claros RTC, Veolia Hubgrade Performance, Pani Energy, Aquasight APOLLO, ChemScan/ProMinent/Grundfos hardware | Mostly feedforward + light ML; hardware-tethered | Plant Mgr / Eng Mgr | Hach RTC modules ~$25–100K all-in; Pani 6-figure ACVs | Real deployments at WW/desal | Operator skepticism; thin DW municipal track record | **Decision support yes, autonomous no** | **Marketing-heavy, thinly delivered** |
| **Coagulation/flocculation decision support** | Chemtrac/Micrometrix SCDs; Hach RTC-COAG; AWWA M37 manual | Hardware controllers + textbook | Plant Mgr | Hardware $5–25K + service | Operator-trusted hardware | No SaaS layer | Coag selection + DBP precursor screening | **Niche, under-served** |
| **Operator copilot / knowledge retrieval** | Aquasight AVA (launched WEFTEC Sept 2025), generic Microsoft Copilot, ChatGPT Enterprise pilots | LLM/RAG over plant data and SOPs | Utility leadership (not operators directly) | Bundled in larger platform deals | First-mover (Aquasight) | No proven standalone ARR | Domain-tuned RAG with state regulatory corpus | **First-mover window still open** |
| **Treatment process digital twins** | Innovyze Info360 (Plant retired Dec 2025), Veolia Hubgrade Performance, Pani Energy, Aquasight APOLLO | Mostly dashboards or hydraulic models with sensor overlay; few real predictive twins | GM / Eng Mgr | $100K–$2M ACV | Marketing reach | Reality lags marketing | True calibrated process twins for DWTPs | **Mostly marketing — real twins rare** |
| **Compliance/reporting** | Hach WIMS/Claros (dominant), Aquatic Informatics WaterTrax, Klir, 120Water, Trinnex leadCAST, Innovyze MyDMR | DMR/MOR/SDWIS reporting + audit trails | Compliance Mgr | $5–25K WIMS small site; Klir $50–300K; 120Water $25–250K | Owns systems-of-record | Dated UX (WIMS); narrow scope (120Water) | LLM copilot **above** WIMS for state-specific MOR formatting | **Crowded for storage; thin for AI/copilot layer** |
| **Source water change forecasting** | EPA CyAN (free), NOAA, USGS NWIS, CE-QUAL-W2 (free), academic models | Fragmented free tools + utility-built ML | Source Water Mgr | n/a | Free | No commercial integration | Reservoir/intake decision dashboard | **Research-heavy, productization thin** |
| **Training simulators** | Sacramento State OWP textbooks (de facto standard), AWWA WSO videos, TLC/360water/American Water College CEU; Hydromantis SimuWorks (high-fidelity, project-based) | Paper + video courseware dominates; high-fidelity OTS rare in DW | Utilities + individual operators | $20–200/CEU; OTS $50–250K project | Established CEU channels | No web-native DWTP simulator | Web sim with state CEU credit | **Crowded courseware; sparse high-fidelity for DW** |
| **What-if/scenario tools** | Hydromantis MantisPW (DW add-on to GPS-X), BioWin (WW), Carollo Blue Plan-it, Innovyze Info360 (network only) | Process modeling + design what-if | Eng firms + large utilities | $3–15K/seat/yr commercial | Domain-deep | Engineer tool, not operator tool | Operator-facing what-if for daily decisions | **Under-served for drinking water inside-fence** |

**Where a startup still has room (synthesized):** filter analytics, CT compliance, PFAS screening, continuous CPE, PFSW reporting, coag selection (not autonomous), and an LLM compliance copilot above WIMS. These are the categories where the founder's domain credibility maps onto products that no incumbent has shipped well.

---

## Section 3: Consultant-heavy opportunity pattern

Drinking water has many useful analyses utilities skip because the consultant fee dwarfs the perceived value. Five strongest examples:

**1. Comprehensive Performance Evaluation (CPE) / Composite Correction Program.** Public EPA methodology that turns SCADA + lab data into a Performance Potential Graph and Performance Limiting Factors list. Done routinely it would prevent unnecessary capital. Done rarely because it requires a 3-person team for 2–4 days; private fee $30–80K. Buyer: GM or Plant Manager. A continuous-CPE SaaS displaces the methodology, not the people; trust evidence required is side-by-side comparisons with state-program CPE outputs at 3–5 reference plants, ideally with an EPA-recognized practitioner co-signing.

**2. PFAS treatment alternatives screening.** The 2024 NPDWR is now the largest single consultant gold rush in drinking water — typical study $150–750K, and 4,100–6,700 utilities need one before 2029 (or 2031 under the May 2025 reconsideration). Carollo's Blue Plan-it and Hazen's internal tools are proprietary and gated. Buyer: GM with council approval. A first-pass screening tool wrapping EPA's free PSDM/AdDesignS could legitimately displace the **first $30–80K** of every study while leaving pilot RSSCTs and PE-stamped design to consultants. Trust evidence: agreement with published RSSCT data on 5+ source waters; review by an academic credible on PFAS sorption (Knappe at NCSU, Westerhoff at ASU).

**3. Sedimentation basin CFD diagnostic study.** $50–300K per study; 1–2× per plant lifetime; only large utilities can afford. Most plants never check whether their settled-water performance gap is hydraulics, chemistry, or load. A pre-CFD screening tool using Camp-Hazen + RTD library + 1D advection-dispersion ROM would tell a plant whether CFD is even warranted. Trust evidence: validation against the Porter et al. 2019 32-plant tracer dataset and 2–3 retrospective basin diagnoses.

**4. Disinfection profiling / baffling-factor / CT recalc study.** $30–150K per study; required by LT1ESWTR before any disinfection change; many utilities defer changes (chloramine conversion, ozone addition) because the study cost gates the project. Trust evidence: state-format MOR generation matching TCEQ/CO/PA/KS templates exactly, plus tracer-data ingestion that aligns with EPA Appendix E regression.

**5. DBP Stage 2 LRAA forecasting / treatment-change studies.** $60–250K per study to evaluate chloramines vs. enhanced coagulation vs. GAC. EPA's WTP Model 2.0 from 2001 is functional but UX-hostile. Trust evidence: replicating WTP Model outputs to within ±10% on ICR data, plus retrospective LRAA prediction at 3 utilities that already changed treatment.

Other examples worth flagging but lower-ranked: OCCT re-optimization, manganese/iron treatment evaluations, ozone/UV alternatives studies, AWIA risk and resilience assessments (largely already free via EPA tools), and reservoir intake / source-water vulnerability assessments.

---

## Section 4: Simplified screening thesis — verdict and rationale

The proposition "help utilities and consultants quickly determine whether a condition warrants deeper engineering review" is **a plausible but narrow wedge**, on the strength side of plausible-but-narrow. It is strong in three specific cases (CT/disinfection profiling, PFAS treatment screening, PFSW/CPE plant performance) and weak as a general thesis.

**Willingness to pay.** Real but bounded. A first-pass screening tool sells against $30–80K consultant fees; mid-market ACVs of $15–60K/yr for a single-workflow screening product are achievable, with engineering-firm seat licenses at $5–15K/seat/yr. The fee compression is real but capped — a screening tool cannot capture the $300K PE-stamped study fee.

**Trust barriers.** Significant. Operators and engineers must believe the model produces results within ±10–20% of an established method; the market punishes plausible-looking outputs that are subtly wrong. Side-by-side validation against 3–5 reference plants and retrospective consulting reports is table stakes. Endorsement from a WRF project, an AWWA committee, or a credible academic moves the buyer line meaningfully.

**Legal and liability.** This is where the screening framing is actually a feature, not a bug. Software cannot replace a PE-stamped engineering recommendation in any state — this constrains incumbents (Transcend deliberately positions as decision support; Innovyze never crosses the line). A screening tool that outputs "this site likely needs deeper review" or "current performance is consistent with PFSW goals" stays cleanly inside decision support. Terms must explicitly disclaim engineering judgment, the way Transcend does.

**Positioning relative to consultants.** Adversarial framing fails — consultants are gatekeepers, sit on AWWA committees, and influence procurement. The right framing is **"this lets your consultant start the deep work faster"** plus **"this lets the utility know whether to call a consultant at all."** Carollo's Blue Plan-it shows consultants will build proprietary screening tools rather than buy them; the founder's leverage is operator credibility plus vendor neutrality, neither of which a consultant can authentically claim.

**Ideal first customer.** A 50–200 MGD surface water utility, municipally-owned, with a Plant Manager who is a Class IV/Grade IV operator, a participating PFSW member, and a serving population of 100K–500K. Not a tiny system (no budget). Not a top-10 utility (procurement is too slow and incumbents are entrenched). The founder's own former employer or peer network is the ideal first customer.

**Ideal initial use case.** CT/disinfection profiling SaaS or PFAS GAC screening — both are time-bounded, regulatory-driven, and have clear "right answer" benchmarks. PFSW reporting is the second-best initial wedge.

**Best pricing model.** Per-plant subscription, $15–60K/yr, with module add-ons. Avoid per-seat for operators (they don't have purchasing authority). Avoid usage-based (water utility CFOs hate variability). Engineering firms should be sold as multi-seat enterprise licenses at $30–150K/yr for a regional firm.

**Strongest objections from buyers.**
- "Will this hold up in front of the state regulator?"
- "Who is liable if the screening misses something?"
- "We already have a consultant we trust."
- "Our IT/OT won't allow cloud SCADA access."
- "We tried [Pluto AI / generic AI] and the operators ignored it."

**Evidence that overcomes objections.** State-by-state regulatory deliverable templates pre-approved by primacy agencies; SOC 2 + on-prem agent / data-diode architecture; published validation studies; co-marketing with 1–2 established consulting firms; operator-led product development (the founder personally on every implementation for the first 12 months); Sourcewell or OMNIA cooperative purchasing contract.

**Verdict: strong wedge specifically for CT compliance, PFAS screening, and PFSW/CPE plant performance. Weak wedge as a general "screening tool for any consultant analysis" thesis.** The market wants specific, regulation-anchored deliverables, not generic engineering screening.

---

## Section 5: Product candidate ranking

The 10 best next product candidates for this founder, scored 1–10 across six dimensions and an overall startup-attractiveness score.

| # | Product | Engine | MLP | Buyer | Trust burden | Time to first paid pilot | Moat | Commod risk | Score |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **CT compliance & LT1 profiling SaaS** | Multi-zone CT calc engine + state-MOR formatters + SCADA ingest | Daily CT calc with TX SWMOR-format export, 3 state templates, audit log | Plant Mgr / Compliance Mgr | Med — must match state templates exactly | **3–6 months** | State-template library + SCADA integrations | Med (Hach Claros could clone) | **9.0** |
| 2 | **PFAS treatment screening** | Wrapped EPA PSDM + IX models + cost layer | GAC vs IX EBCT/use-rate screening for 1 utility's source water with 3-year cost NPV | GM + Eng Mgr | High — must align with RSSCT data | **6–9 months** | Domain-tuned cost & residual data + academic endorsements | High if EPA refreshes AdDesignS (Jan 2026 archive) | **8.5** |
| 3 | **PFSW Phase III/IV plant performance reporting** | SCADA filter profile analytics + sedimentation goal trending + auto-narrative | Auto-generated PFSW Phase III submission for 1 plant | Plant Mgr / PFSW participant | Med — peer-reviewed by AWWA committee | **4–8 months** | Founder credibility + AWWA relationship | Low (narrow buyer set, sticky) | **8.5** |
| 4 | **Continuous CPE / self-assessment** | Performance Potential Graph engine + PLF analyzer | Continuous CPE dashboard for 1 plant matching state-program CPE output | GM / Plant Mgr | High — must match Process Applications Inc. methodology | **6–12 months** | Public methodology + founder credibility + state-AWOP partnerships | Low | **8.0** |
| 5 | **Filter performance & backwash analytics** | UFRV/headloss/ripening ML + backwash effectiveness scoring | Filter analytics SaaS for 1 plant with auto-PFSW Phase IV outputs | Plant Mgr | Med | **4–8 months** | Filter-specific data assets + integration breadth | Med | **8.0** |
| 6 | **DBP Stage 2 LRAA forecasting** | Modernized EPA WTP Model + lab/SCADA ingest + scenario engine | LRAA forecasting at 1 utility with treatment-change what-if | Compliance Mgr | Med | **6–9 months** | EPA model UX wrap + utility-specific calibration | Med (Carollo Blue Plan-it competition) | **7.5** |
| 7 | **Coagulant selection screening (decision support, not control)** | Edzwald diagram + DBP precursor predictions + cost curves + jar-test data manager | Coagulant alternatives screening for 1 utility's seasonal NOM | Plant Mgr / Lead Operator | High — operator distrust risk | **6–9 months** | Founder operator credibility + jar-test dataset | High (autonomous control vendors expand into screening) | **7.0** |
| 8 | **OCCT corrosion re-optimization** | Schock lead solubility + DIC/Ca/orthophosphate speciation + RTW indices | OCCT re-optimization screening for 1 LCRI-triggered utility | Compliance Mgr / Eng Mgr | High — corrosion is high-stakes science | **9–12 months** | Chemistry library + corrosion academic endorsements | Low | **6.5** |
| 9 | **Sedimentation basin pre-CFD screening** | Camp-Hazen + RTD library + 1D advection-dispersion ROM | Basin diagnostic for 1 utility benchmarked against tracer data | Eng Mgr | High — must validate against CFD/tracer | **9–12 months** | RTD/tracer dataset + Porter-style validation | Low | **6.0** |
| 10 | **Operator copilot / LLM SOP retrieval** | RAG over utility SOPs + state regs + plant data | Plant-specific LLM Q&A for 1 utility | Plant Mgr / GM | Very high — black-box risk | **6–12 months** | Domain-tuned corpus + integrations | Very high (Aquasight AVA, Microsoft Copilot, generic LLMs) | **5.5** |

### Ranking (most attractive first)
1. CT compliance & LT1 profiling SaaS
2. PFSW Phase III/IV plant performance reporting (tied)
2. PFAS treatment screening (tied)
4. Continuous CPE / self-assessment (tied)
4. Filter performance & backwash analytics (tied)
6. DBP Stage 2 LRAA forecasting
7. Coagulant selection screening
8. OCCT corrosion re-optimization
9. Sedimentation basin pre-CFD screening
10. Operator copilot / LLM SOP retrieval

The top four cluster into a coherent **plant-performance platform** that the founder can ship over 24–36 months. The bottom three are interesting standalone candidates that work better as later modules.

---

## Section 6: Moat analysis

**Where defensibility actually comes from in U.S. drinking water software, ranked from most to least durable:**

1. **Trust/validation assets** — published validation studies, AWWA committee endorsements, WRF project participation, state-primacy-agency template approvals, NSF/ANSI 60/61 certifications where applicable. These compound slowly and are hard for incumbents to fast-follow.
2. **Workflow design** — embedding into a utility's daily/monthly/annual rhythm (PFSW reporting cycles, monthly MORs, annual capital planning). Once a utility's compliance calendar runs through your product, replacement risk drops sharply.
3. **Domain-specific dataset** — RTD libraries from tracer studies, jar-test result archives, PFAS RSSCT comparisons, calibrated DBP formation parameters per source water. The founder's 14 years of operational data (with permission) is a credible cold-start asset.
4. **Distribution** — Sourcewell/OMNIA cooperative purchasing contracts, state-AWOP partnerships, engineering-firm channel deals (the Trinnex/CDM Smith model, the Hydromantis/Hatch model). Distribution moats are very real in water and very underused by startups.
5. **Integration footprint** — AVEVA PI Web API, OPC UA, Hach WIMS, LIMS, common SCADA stacks. Integrations are hard, painful, and lock-in producing.
6. **Services layer** — implementation services, calibration services, expert-on-staff time. Strong revenue but weak moat — services scale linearly and create ceiling on growth.
7. **UI/UX** — meaningful in a market dominated by macro-Excel and 1990s thick clients, but easily fast-followed by a determined incumbent.
8. **Proprietary model** — weakest moat. Most underlying science is in EPA spreadsheets, AWWA manuals, or peer-reviewed papers. Carollo's Blue Plan-it is proprietary but only because it's coupled to Carollo services. A novel coagulation model, jar-test ML, or PFAS isotherm refinement is a poor moat — academia will publish your science within 18 months.

### Applied to the five candidate directions

**Basin modeling tools.** Real moat is **trust assets** (Porter-style tracer-dataset validation, AWWA M37 alignment) and **dataset** (RTD library). UI moat exists but is shallow. Proprietary model moat is weak. **Verdict: moat is real but takes 18–24 months to build; rare buying event hurts repeat revenue.**

**Operator knowledge copilots.** Real moat is **domain-specific dataset** (the utility's own SOPs, plant-specific tribal knowledge). Workflow moat is fragile because no clear daily ritual yet. Distribution moat is everything — Aquasight AVA wins because they're already inside 120+ utilities. **Verdict: moat is weak for a startup without prior platform deployment; do not lead with this.**

**Troubleshooting advisors.** Same diagnosis as copilots, but with one possible exception: a **filter or coagulation troubleshooting** advisor tied to a specific data signature (UFRV trends, jar-test outcomes) can build a real dataset moat over time. **Verdict: moat is medium, only if anchored to a specific recurring workflow.**

**Treatment scenario / what-if tools.** Real moat is **integration footprint** (LIMS/SCADA/historian ingest at scale) plus **calibration data**. Hydromantis MantisPW has a 30-year head start on the engineering-firm side; on the operator-facing side the field is open. **Verdict: moat is real but requires 3–5 years of deployments.**

**Training simulators.** Real moat is **distribution** (state CEU approvals — this is a multi-year, multi-state regulatory grind that is hard to replicate) plus **content library**. Sacramento State OWP has owned this for 30 years on textbook content. **Verdict: distribution moat is real but slow; not a fast-growth category.**

The pattern: moats in this market are built from **regulatory deliverables, validation evidence, and integration depth**, not from algorithms. The founder's operator credibility helps with all three but is not a moat by itself.

---

## Section 7: Packaging-not-science opportunities

Workflows where the technical core already exists — in EPA spreadsheets, AWWA manuals, peer-reviewed regressions, or internal consulting practice — and the commercial gap is packaging, integration, and trust.

**EPA WTP Model 2.0 (DBP formation modeling).** Core exists since 2001 in spreadsheet/standalone form. Missing: SCADA/LIMS ingestion, locational LRAA forecasting, what-if treatment-change UI, modern reporting. No one packaged it well because EPA can't sell SaaS, consulting firms keep it proprietary (Carollo Blue Plan-it), and the modeling is unsexy. Buyer: Compliance Manager + Engineering Manager. **Bootstrap SaaS to good-VC scale; not pure venture.**

**EPA AdDesignS / PSDM (PFAS adsorption sizing).** Core exists in EPA Python repo. Missing: vendor-neutral cost layer, residual disposal options, NSF media filter, clean operator UI, RSSCT calibration help. Not packaged because EPA archived the original repo (Jan 2026), academic users tolerate UX pain, and vendors (Calgon, Cyclopure, Purolite) prefer opacity. Buyer: GM + Engineering Manager. **Venture-scale within the 2024–2031 PFAS compliance window.**

**Composite Correction Program (CPE) methodology.** Core exists in EPA Headworks Performance Manual and 1998 CPE guidance. Missing: continuous SCADA-driven version, automated PLF analysis, side-by-side benchmarking, Performance Potential Graph generation. Not packaged because Process Applications Inc. (EPA's prime contractor) operates it as a services business, not software. Buyer: GM + Plant Manager. **Bootstrap-to-venture; founder-fit is exceptional.**

**Partnership for Safe Water Phase III/IV reporting.** Core exists in AWWA member-only Excel templates and the AWWA Self-Assessment Guide. Missing: SCADA integration, automated narrative generation, year-over-year trend analytics, peer benchmarking. Not packaged because AWWA is a non-profit standards body that doesn't ship software. Buyer: Plant Manager. **Bootstrap SaaS; ~250 utilities + ~1,000 candidates is a small but sticky base.**

**RTW Model + EPA OCCT spreadsheets (corrosion control).** Core exists. Missing: integrated lead solubility modeling (Schock), DIC/Ca/orthophosphate Pourbaix-style speciation, source-specific calibration. Not packaged because corrosion chemistry is hard, the buyer is small (LCRI-triggered utilities), and consultants (Corona Environmental, Hazen) keep their tools proprietary. Buyer: Compliance Manager. **Services-enabled software, $5–15M ARR ceiling.**

**Smith et al. baffling factor regressions + LT1 profiling spreadsheets.** Core exists in EPA Appendix E and state CT helper spreadsheets. Missing: multi-zone summation, state-specific MOR formatting, SCADA-driven daily computation, audit trail. Not packaged because every state has a different MOR format and software vendors avoid the certification headache. Buyer: Plant Manager + Compliance Manager. **Bootstrap-to-venture; the cleanest of the packaging plays.**

**Camp-Hazen + Yao plate-settler equations + Porter et al. tracer dataset.** Core exists in textbooks and the 2019 AWWA paper. Missing: ROM hydraulic engine, RTD library, sensitivity analysis UI. Not packaged because the buying event is rare. Buyer: Engineering Manager. **Module within a plant-performance platform, not standalone.**

**EPA CyAN + NOAA HAB forecasts + utility-specific PAC dosing rules.** Core exists. Missing: utility-specific risk dashboard, treatment-decision playbook integration. Not packaged because TAM is ~100 utilities. Buyer: Plant Manager / Source Water Manager. **Services-enabled software, niche.**

**Cleasby-Fan backwash hydraulics + filter media textbook math.** Core exists. Missing: SCADA-driven application, recovery-stream analytics. Not packaged because it's seen as a feature, not a product. **Module, not standalone.**

The pattern: in drinking water, the most attractive packaging plays are **EPA-published methods that EPA has no incentive to commercialize and that consultants prefer to keep proprietary.** The founder's edge is operator credibility plus willingness to navigate state-by-state regulatory format heterogeneity — a moat-building activity most VC-backed software founders find unattractive.

---

## Section 8: Direction comparison

Three directions: engineering screening tools, operator/copilot knowledge systems, training/simulator products.

| Dimension | Engineering screening | Operator/copilot KM | Training/simulators |
|---|---|---|---|
| **Buyer clarity** | Strong — Compliance Mgr / Eng Mgr / Plant Mgr depending on workflow | Weak — no dedicated budget category in water | Medium — utility training coordinator (real but small budget) |
| **Urgency** | Very high (PFAS 2029, LCRI 2027, ongoing CT/PFSW) | Low — operator KM is universally agreed-on but unfunded | Medium — driven by silver-tsunami narrative, not state mandates yet |
| **Sales cycle** | 6–12 months (regulatory-anchored) | 12–24 months (no budget code, must reframe) | 12–24 months (state CEU approval per state) |
| **Validation burden** | Medium-high (must match consultant outputs) | Very high (LLM hallucination, public health) | Medium (must match certification curriculum) |
| **Implementation complexity** | Medium — SCADA + state-MOR templates | High — RAG over utility-specific SOPs | Medium-high — content authoring + state CEU paperwork |
| **Data dependency** | Medium — utility SCADA/lab data | Very high — utility SOPs, runbooks, internal docs | Low — content is created, not extracted |
| **Moat durability** | High — regulatory deliverables + validation | Low — fast-follow risk from Aquasight AVA, Microsoft Copilot | Medium — state CEU approvals are slow but durable |
| **Expansion potential** | High — modules across PFSW, PFAS, DBP, OCCT, basin, filters | Medium — copilot can wrap any module but doesn't drive new revenue | Low — training is narrow CEU TAM (~$100–250M total) |
| **Founder-market fit** | Exceptional for plant-performance modules | Strong but generic | Strong but distribution-heavy |
| **Speed to first revenue** | 3–6 months for CT or PFSW | 9–18 months | 12–24 months |

**Recommendation: pursue engineering screening first, anchored to a regulatory deliverable.** Specifically CT/disinfection profiling SaaS as the wedge, expanded into PFAS screening and PFSW/CPE platform within 18 months. Reasons:

- Buyer is identifiable; budget exists; sales cycle is the shortest of the three.
- Validation burden is high but bounded — replicate state templates, match Smith regressions, ship.
- Founder credibility maps cleanly onto plant-performance reporting; the founder's name on a PFSW Phase III/IV product is more valuable than on an LLM copilot.
- Moat is the most durable of the three.

Operator copilot is the wrong first move because there is no purchase code, the validation burden is highest, and Aquasight AVA already has the first-mover advantage at 120+ utilities. Training/simulator is the wrong first move because state CEU approvals are a 2–4 year regulatory grind for a $100–250M TAM ceiling. Both are credible **second-or-third products** layered onto a plant-performance platform.

---

## Section 9: Sedimentation wedge expansion path

The original prompt assumes a sedimentation-first wedge. **This recommendation modifies the assumption.** Sedimentation basin screening is a real gap but a rare buying event with a small repeat-revenue profile — a standalone basin-screening product would struggle to reach $5M ARR. A better-sequenced 3-year path uses sedimentation as **module #2 or #3**, not the wedge.

But if the founder is committed to leading with sedimentation, here is the sharpest path.

**Year 1, Months 0–6 — sedimentation basin pre-CFD screening (the wedge).** Camp-Hazen + Yao plate-settler engine, RTD library indexed by basin geometry from Porter et al. 2019, 1D advection-dispersion ROM, sensitivity-slider UI. First paid pilots at 3–5 mid-large utilities, ideally PFSW members. Engagement model: $25–40K/yr per plant, with a $15K validation engagement that compares screening output to historical CFD or tracer studies.

**Year 1, Months 6–12 — PFSW Phase III sedimentation goal reporting.** Auto-generated sedimentation goal compliance reports tied to the basin-screening engine. This is the natural pivot from "rare basin study" to "annual reporting deliverable" and turns the customer relationship recurring. Pricing tier upgrade to $40–60K/yr.

**Year 2, Months 12–18 — PFSW Phase IV filter goal reporting (the multiplier).** Filter analytics, UFRV trending, ripening curve analysis, IFE/CFE goal compliance. This is the same buyer (Plant Manager / participating PFSW utility), the same SCADA integration, and roughly doubles the daily-relevance of the product. ACV expansion to $60–100K/yr.

**Year 2, Months 18–24 — Continuous CPE / Performance Potential Graph module.** Adds the Performance Limiting Factors analysis to the platform. Credibility-multiplier: positions the company as the EPA AWOP-aligned tool for plant performance. Pursue formal partnerships with 2–3 state AWOP programs (Arkansas, Kansas, North Carolina) and ideally an MOU with Process Applications Inc.

**Year 3, Months 24–30 — CT / disinfection profiling module.** This is where the platform earns its keep on daily relevance — every surface water plant runs CT calculations daily. State-MOR template library across 5–10 states. ACV expansion to $80–150K/yr.

**Year 3, Months 30–36 — PFAS treatment screening module.** Plug into the existing customer base, ride the 2029/2031 compliance window. Premium module pricing $25–50K/yr add-on.

**What infrastructure gets reused:** SCADA/historian ingest agents, state-template library, audit-log architecture, on-prem agent / data-diode deployment, AWWA M37-aligned terminology and reporting conventions, the operator-credible UI vocabulary (the founder's voice).

**How credibility compounds:** basin tracer/RTD validation → PFSW participation → state-AWOP partnership → published WRF or AWWA case study → academic endorsement → AWWA committee participation → state regulatory acceptance → cooperative purchasing contract (Sourcewell or OMNIA). Each step makes the next sale faster.

**Adjacent modules that become natural:** DBP Stage 2 LRAA forecasting (ties to CT and disinfection), OCCT corrosion control (ties to lead/copper compliance reporting), backwash and recovery-stream analytics (ties to filter module), HAB / source water risk (ties to PFSW source-water goal).

**Cross-sell:** engineering firms (Carollo, Hazen, Brown and Caldwell, Stantec, HDR) for multi-utility seat licenses; state primacy agencies for statewide dashboards; OEMs (Hach, Xylem, Veolia) for embedded modules.

**Sequence rationale:** Year 1 establishes operator-credibility and a recurring revenue ritual (PFSW). Year 2 adds the daily-relevance ritual (filter performance, CT). Year 3 captures the urgency-driven ACV uplift (PFAS). Revenue and defensibility compound because every module reuses SCADA integrations and state-template work.

**A more pragmatic alternative to the sedimentation-first wedge:** lead with CT/disinfection profiling (Year 1 months 0–6) and add sedimentation as the Year 2 anchor module. This produces faster first revenue, less validation burden, and more recurring-revenue gravity from day one. **The decision memo below recommends this alternative.**

---

## Section 10: Thesis attack — both sides, unsparing

### The bull case

The founder has 14 years as a senior operator at a 160 MGD surface water plant — a credibility profile virtually no other water-software founder has. The U.S. has ~50,000 community water systems, a $11.5B → $23.8B digital-water market, and a structurally under-invested IT/OT spend (~1–3% of revenue versus ~10% in banking). Inside-the-fence treatment software is genuinely thin: Autodesk Innovyze retired Info360 Plant in December 2025 after only ~3 years, validating the gap. Transcend has raised ~$35M and is the only credible engineering-automation startup in water — leaving operator-facing screening and plant-performance reporting essentially uncontested. Regulatory tailwinds are real and time-bounded: PFAS 2029/2031, LCRI Nov 2027, ongoing PFSW/Stage 2 D/DBP. EPA owns the underlying IP for most of the workflows but cannot ship SaaS, and consultants prefer their tools proprietary — which means a vendor-neutral packager wins. Veeva and nCino are predictive analogs: regulated, slow, conservative, modular, $500K+ ACV at scale. Burnt Island Ventures + Echo River + Imagine H2O have a real if small ecosystem, with Xylem anchoring BIV Fund II in 2025.

### The bear case

Drinking water utilities buy software like they buy dredging services: slowly, by RFP, after a 12–24 month committee process, against an existing consultant relationship. Federal money flows to pipes and engineering firms, not to SaaS ARR — the IIJA's $55B is largely unaddressable. Pluto AI is the cautionary tale: smart team, real algorithms, reasonable funding, dead by 2019 because operator trust did not materialize at the speed of capital. The market has a graveyard of "AI for water" startups for one reason: utility GMs are politically liable for boil-water notices and won't bet careers on a 5-person startup. Operator copilot has no budget code in water utility procurement. Training simulators face a state-by-state CEU approval grind for a $100–250M TAM. Sedimentation, hydraulic surge, and most "consultant-heavy" workflows are rare buying events — a $40K consultant fee every 5 years is not a $40K/yr SaaS replacement. The most attractive workflows (CT, PFSW, PFAS) require state-template work that is infinitely tedious and unfun. The 14-year operator credibility advantage is real but does not replace 5 years of state-by-state regulatory paperwork. And the mid-market sweet spot (50–200 MGD) is exactly where Hach Claros, Aquasight, Klir, and 120Water already sit; the founder will have to take share, not create it.

### The most dangerous assumptions

1. **"Operators want better software."** Operators want fewer alarms and a quieter life. They distrust black-box recommendations and have been burned by vendors before. Selling to operators is a slower path than selling above operators (Plant Manager, Compliance Manager, Engineering Manager).
2. **"Consultant fees are addressable."** Some are; most are not. PE-stamped engineering work is legally protected; what is addressable is the **first $30–80K** of any study, not the full fee. Consulting partial-displacement is a lower ceiling than founders typically model.
3. **"Vertical AI for water" is a coherent thesis.** It is not. Water has at least four distinct buying centers (compliance, operations, engineering, IT/OT) with different budgets, different procurement paths, and different validation burdens. A coherent product strategy must pick one.
4. **"Federal infrastructure dollars will fund software."** Almost none of it will, directly. Software gets funded via engineering firms billing it through their fees. A direct-to-utility SaaS founder must build a real GTM, not ride the IIJA.
5. **"Time-bounded regulatory windows (PFAS 2029/2031) create durable revenue."** They create 5–7 year revenue spikes that fade. 120Water's challenge is exactly this: post-LCRI, the platform has to broaden or shrink.

### Evidence that would validate the thesis quickly

Three operator-led utilities pay $15–40K each within 6 months for a CT/disinfection or PFSW pilot. AWWA committee or PFSW program agrees to co-market. A WRF subgrant or pilot grant is awarded to validate the core engine. Two of the top-tier engineering firms (Carollo, Hazen, Brown and Caldwell, Stantec) sign a non-exclusive partnership for engineering-firm seat licenses. State primacy agencies in 2 states (TX, CO, PA, KS, CA are the highest-leverage) accept the product's MOR output format. Founder is invited to publish in *AWWA Journal* or present at ACE.

### Evidence that would falsify the thesis quickly

Three or more pilot conversations stall at the IT/OT cybersecurity gate even with on-prem agent architecture. State primacy agencies decline to accept the product's reporting format and require manual reformatting. PFSW members say "we already have AWWA Excel templates and our consultant does the rest." The founder's former employer or peer utility declines to be a reference customer. Aquasight, 120Water, or Hach Claros announce a competing module within 9 months at materially lower price. Six months in, no utility has paid a deposit or signed an LOI for $25K+/yr. EPA refreshes its own PSDM/AdDesignS UX and effectively eats the PFAS screening wedge.

---

## Decision memo

**Top 3 product opportunities** (in order):
1. **CT compliance & LT1 disinfection profiling SaaS** — daily relevance, public methodology, brittle Excel incumbents, 3–6 months to first revenue, founder-fit excellent.
2. **PFAS treatment screening tool** — highest-urgency window, free EPA model to wrap, $100–500K consultant fees to partial-displace, time-bounded but real through 2031.
3. **Partnership for Safe Water Phase III/IV plant performance reporting** — narrow buyer set (~250 active + ~1,000 candidates), exceptional founder-fit, recurring annual ritual, low fast-follow risk.

**The one best starting wedge: CT compliance & LT1 disinfection profiling SaaS.** Build state-specific MOR formatters for TX, CO, PA, KS, and CA in that order. Daily-relevance creates usage frequency that PFSW and PFAS cannot match. Validation burden is bounded (Smith regressions are public, state templates are public). It establishes the SCADA/historian integration footprint that every subsequent module reuses. PFSW and PFAS become Year 1 Q3 and Year 2 modules.

**Biggest commercialization risk:** state-template heterogeneity becomes a treadmill. Each new state takes 3–6 months of regulatory paperwork; if the company tries to expand too fast it bleeds energy on paperwork. Mitigate by anchoring the first 18 months to 3 states and one cooperative purchasing contract (Sourcewell preferred).

**Biggest product risk:** SCADA/OT integration friction at mid-large utilities. Cloud-only architecture is dead on arrival post-Oldsmar; an on-prem agent with one-way data diode push is table stakes. Build this from day one or accept a 24+ month sales cycle.

**Biggest trust/adoption risk:** operator and engineer skepticism that the screening output is "good enough" for state regulators. Mitigate by publishing 3 retrospective validation studies in the first 12 months, by recruiting an AWWA committee member as a paid advisor, and by offering a free side-by-side comparison with the utility's existing MOR/CT spreadsheet for the first 60 days.

**First 10 customer discovery questions to ask in interviews:**
1. Walk me through how your team produced last month's CT compliance report. How many people, how many hours, what software?
2. When did your CT spreadsheet template last break or produce a wrong number? What did it cost to fix?
3. What does your state primacy agency reject most often in your monthly operating report?
4. The last time you considered changing disinfection chemistry (chloramines, ozone, UV), what stopped you, and what did the disinfection profile study cost?
5. If a PFAS treatment screening tool gave you a defensible GAC vs IX recommendation in 2 weeks instead of 6 months, would your GM accept it as a budget input — or would they still require a Carollo/Hazen study?
6. Are you a Partnership for Safe Water member? Why or why not? How many hours did your last Phase III/IV submission take?
7. What budget line item would a $25–50K/yr CT and PFSW reporting platform come out of? Operations, compliance, engineering, IT?
8. Who in your organization has signing authority at $25K, $100K, $250K?
9. What does your IT/OT team require for any cloud connection to your historian or SCADA? On-prem agent, data diode, what specifically?
10. Which consulting firm would you trust to validate the output of a screening tool, and would you pay them $10–15K to do that validation?

**First 3 pilot offers to test:**

| Pilot | Offer | Price | Goal |
|---|---|---|---|
| **A** | Free 90-day CT compliance side-by-side: we ingest your SCADA data, we compute daily CT, we generate your state-format MOR, you compare to your existing process | $0, founder personally on-site for week 1 | 3 LOIs for $25K/yr, 1 paid contract within 90 days |
| **B** | Paid PFSW Phase III/IV submission for current cycle: we automate the data assembly and goal compliance narrative for one annual submission | $20K fixed-fee one-time | 1 paid customer; case study; AWWA presentation slot |
| **C** | PFAS GAC/IX screening engagement: 60-day evaluation of treatment alternatives for 1 source water, deliverable benchmarked against EPA PSDM | $35K fixed-fee | 1 paid customer; published validation against RSSCT data; engineering-firm partnership conversation |

**Strongest "do not build this first" warning: do not build a standalone operator copilot or LLM knowledge system as the wedge product.** Aquasight AVA has the first-mover advantage at 120+ utilities; Microsoft Copilot, Glean, and generic LLMs are eating the broader category; there is no purchase code in water utility procurement for "operator copilot"; validation burden is the highest of any direction (LLM hallucination + public health liability); and the moat is the weakest. Build the copilot in Year 2 or Year 3 as a layer on top of a plant-performance platform that already owns the data, the workflow, and the trust. The path that works is **CT compliance → PFSW → PFAS → continuous CPE → filter analytics → DBP forecasting → operator copilot as the natural capstone.** The path that fails is leading with the copilot.

A final word on framing. The founder's edge is not vertical AI. It is **vertical credibility plus willingness to do the unfun regulatory packaging work that consultants and big vendors avoid.** Lead with that, and the AI follows. Lead with the AI, and the credibility burns.