# Under-Digitized Workflows in U.S. Potable Water Treatment

**Market Research: 15 High-Value Workflow Gaps Ranked by Commercial Attractiveness**

April 2026 | Vertical SaaS Analysis for Drinking Water Utilities, Engineering Consultants, and Treatment Operations

---

## Ranking Methodology

Workflows are ranked by a composite score across six dimensions: market size (number of potential buyers and deal size), regulatory urgency (active or imminent compliance deadlines), pain intensity (cost of the current workaround and frequency of use), defensibility (how hard the workflow is to replicate without domain expertise), wedge potential (ability for modern software plus AI to deliver immediate, measurable improvement), and incumbent weakness (whether existing solutions are too expensive, too complex, or too slow for the addressable market).

---

## 1. CT Compliance Calculation and Documentation

**Buyer:** Plant operators, chief operators, compliance officers at surface water treatment plants. Roughly 10,000 surface water systems in the U.S., with SWTR obligations.

**Current workaround:** Operators calculate CT (disinfectant concentration x contact time) by hand or in Excel spreadsheets every shift, typically using lookup tables from EPA guidance, temperature/pH corrections, and manually entered residual and flow data. Results are logged on paper or in spreadsheet templates that vary by state. Colorado offers a state-hosted web calculator; most states provide nothing.

**Why it is still hard:** CT is not a single calculation. It requires pulling together real-time residual concentration, flow rate (to compute contact time through specific baffled volumes), water temperature, pH, and then looking up the correct inactivation ratio from EPA CT tables that differ by disinfectant type, target pathogen, and whether you are crediting Giardia vs. Crypto vs. viruses. Multiple disinfection stages (pre-ozone, post-chlorine, UV) require separate CT segments that must be summed. Baffling factors from tracer studies are plant-specific. When flow or residual changes mid-shift, the calculation changes. The cognitive load is real, and a wrong number is a regulatory violation, not just an inconvenience.

**Frequency:** Every operating shift, 2-3 times per day, 365 days per year.

**Dollar impact of getting it wrong:** A CT shortfall that goes undetected is an SWTR violation. Penalties range from $25,000/day for significant noncompliance. Worse, an actual disinfection failure is a public health emergency. Boil-water notices cost utilities $50,000-$500,000+ in direct costs and massive reputational damage.

**Regulatory urgency:** Continuous. CT compliance is a core SWTR requirement. State primacy agencies review CT records during sanitary surveys (every 3-5 years). Monthly operating reports must include CT data submitted within 10 days of month-end.

**Existing software/vendors:** State-provided Excel templates (inconsistent quality). OxMaint has CT fields in inspection checklists. Some SCADA historians can be configured to compute CT, but this requires custom PLC programming. Hach's WIMS (Water Information Management System) can log data but does not compute multi-segment CT. No standalone, affordable, real-time CT compliance tool exists for small/medium systems.

**Incumbent weakness:** Too complex (SCADA-based solutions require controls engineering to configure), too expensive (WIMS and similar platforms start at $15,000+/year), or too primitive (state Excel templates with no validation, no alerts, no integration).

**AI/modern UI wedge:** Strong. A mobile-first CT calculator that pulls plant-specific baffling factors, auto-selects the correct EPA table based on disinfectant and temperature, flags marginal compliance in real-time, and generates shift-ready documentation. AI layer can interpret trends ("your CT margin has been shrinking for three days, here is why") and pre-fill monthly operating report sections. This is the single highest-frequency, highest-stakes calculation in treatment operations with the weakest tooling.

---

## 2. Monthly Operating Report (MOR) Assembly and Submission

**Buyer:** Chief operators, compliance managers, and small-system operators at all 50,000+ community water systems.

**Current workaround:** Operators compile data from SCADA printouts, bench sheets, lab results, and handwritten logs into state-specific report templates (usually Excel or PDF). Every state has a different format. Some states have moved to electronic submission portals, but the data assembly remains manual. A typical MOR takes 4-8 hours per month at a medium plant, and 1-2 full days at a large plant.

**Why it is still hard:** Data lives in 5-10 different silos (SCADA historian, lab notebooks, chemical delivery receipts, distribution system sample results, operator bench sheets). State templates differ in field definitions, units, and reporting periods. The operator must compute averages, maximums, minimums, and percentiles manually. Cross-referencing turbidity exceedances against filter run logs requires human judgment about which events were reportable vs. instrument artifacts.

**Frequency:** Monthly, with a hard 10-day submission deadline.

**Dollar impact of getting it wrong:** Late or inaccurate MORs are independent compliance violations regardless of whether actual treatment was fine. Repeated reporting violations trigger formal enforcement. At systems with part-time operators, MOR assembly is often the single largest administrative burden.

**Regulatory urgency:** Continuous. Every state primacy agency requires MORs under delegated SDWA authority.

**Existing software/vendors:** Hach WIMS, AllMax Operator10, Klir, Locus Water, Utility Cloud. All can reduce the burden but require significant configuration, SCADA integration work, and ongoing maintenance. Pricing starts around $5,000-$25,000/year, putting them out of reach for the ~42,000 small systems serving under 10,000 people.

**Incumbent weakness:** Too expensive for small systems. Too much implementation effort (3-6 month onboarding). State format changes require vendor updates that lag. Most small systems cannot justify the IT overhead.

**AI/modern UI wedge:** Very strong. A tool that ingests a few standard data exports (CSV from SCADA, photos of bench sheets via OCR, lab result PDFs) and auto-populates the correct state template, flagging missing data and anomalies. AI can learn each state's format and handle the translation. The 42,000 small systems are a massive underserved market where a $50-200/month tool displaces hours of manual work.

---

## 3. Lead Service Line Inventory Management and LCRR/LCRI Compliance

**Buyer:** Utility directors, asset managers, compliance officers, and GIS analysts at all community water systems and non-transient non-community systems (schools, daycares).

**Current workaround:** Initial inventories were due October 2024. Most systems assembled them from tap cards, plumbing permits, meter installation records, and field investigations, tracked in Excel spreadsheets or Access databases. Many systems categorized thousands of lines as "unknown" because historical records are incomplete. Ongoing updates, consumer notifications, and replacement tracking are now required.

**Why it is still hard:** The data problem is fundamentally messy. Records span decades of inconsistent formats: handwritten tap cards from the 1950s, permit databases from the 1990s, GIS layers from the 2010s. Ownership splits (system-side vs. customer-side) complicate classification. Field verification requires potholing or predictive modeling. The LCRI (compliance date November 2027) adds mandatory 10-year replacement timelines, baseline inventory updates, annual reporting, and consumer notification in multiple languages.

**Frequency:** Continuous inventory updates, annual reporting, plus event-driven notifications (every service line disturbance triggers notification and flushing instructions).

**Dollar impact of getting it wrong:** Lead action level exceedances now require Tier 1 public notification within 24 hours. The LCRI drops the action level from 15 ppb to 10 ppb. Failure to maintain the inventory or meet replacement rates triggers EPA enforcement. Political and legal exposure is enormous given the post-Flint environment.

**Regulatory urgency:** Acute. Initial inventories were due October 2024 (many systems are still catching up). Baseline inventories due November 2027. 10-year full replacement mandate under LCRI. This is the largest regulatory overhaul most utility directors have seen.

**Existing software/vendors:** 120Water (dominant in this niche, purpose-built for LCRR compliance), TruePani (technical assistance provider contracted by states), BlueConduit (predictive modeling for unknown lines). Some GIS vendors (Esri, Sedaru) have added service line inventory modules. State templates exist (Excel-based).

**Incumbent weakness:** 120Water is well-positioned but expensive for small systems. GIS-based solutions require existing GIS infrastructure most small utilities lack. State templates are primitive. The gap is widest at systems serving 3,300-25,000 people: too large for a simple spreadsheet, too small for enterprise GIS.

**AI/modern UI wedge:** Strong. AI can classify unknown service lines from historical records (OCR on tap cards, predictive modeling from construction-era data, permit cross-referencing). Mobile-first field verification workflows replace clipboard-and-camera processes. Automated consumer notification generation in multiple languages is a direct LCRI requirement that screams for templated automation. The regulatory deadline creates urgency that compresses sales cycles.

---

## 4. Coagulant Dose Optimization and Jar Test Interpretation

**Buyer:** Plant operators and process engineers at conventional surface water treatment plants (roughly 8,000-10,000 facilities).

**Current workaround:** Operators run jar tests on bench-top equipment, visually assess floc formation, and measure settled turbidity. Results are logged in paper notebooks or unstructured spreadsheets. Dose adjustments are made based on experience, intuition, and informal rules of thumb passed between operators. When source water quality changes rapidly (storm events, turnover, algae blooms), operators increase jar test frequency and make best guesses. Engineering consultants are hired at $200-400/hour for process optimization studies.

**Why it is still hard:** Coagulation is the most experience-dependent process in conventional treatment. Optimal dose depends on raw water turbidity, temperature, pH, alkalinity, NOM character, competing ions, and coagulant chemistry. The interaction effects are nonlinear. Jar test results must be translated to full-scale performance, which requires understanding of mixing energy, hydraulic retention time, and sedimentation basin geometry. A new operator without a mentor can take years to develop reliable dosing judgment.

**Frequency:** Daily to multiple times per shift during source water events. Jar tests are routine at well-run plants (weekly to daily) and emergency-driven at others.

**Dollar impact of getting it wrong:** Coagulant is typically the largest chemical cost at a treatment plant ($100,000-$2,000,000/year at medium to large plants). Overdosing wastes chemical, increases sludge production, and can cause aluminum/iron carryover. Underdosing causes turbidity breakthrough, potential filter loading, and regulatory risk. A 10-15% chemical cost reduction from better dosing pays for a lot of software.

**Regulatory urgency:** Indirect. No regulation says "optimize your coagulant dose." But turbidity limits are regulatory (0.3 NTU combined filter effluent, 1.0 NTU individual filter), and failing to coagulate properly is the fastest path to a turbidity violation.

**Existing software/vendors:** DuPont WAVE (membrane design, not coagulation). No commercial software product specifically addresses jar test logging, interpretation, and dose recommendation for conventional coagulation. Some academic ML models exist (e.g., the AO-ELM model from recent research) but none are productized. Xylem and Hach have online streaming current monitors that provide real-time feedback, but these are $15,000+ instruments, not software.

**Incumbent weakness:** No real incumbent exists for the software layer. The instrument vendors (Hach, Xylem) sell hardware. Engineering consultants sell time. Nobody sells an affordable, continuously learning coagulant optimization tool.

**AI/modern UI wedge:** Very strong. A tool that logs jar test results with structured data entry (dose, pH, temperature, settled turbidity, floc description), builds a plant-specific dose-response model over time, and recommends starting doses based on current raw water conditions. This is exactly the kind of experience-dependent, data-rich workflow where AI provides the most value. The knowledge transfer angle (retiring operators' dosing intuition captured in the model) is a powerful sales narrative.

---

## 5. Sanitary Survey Preparation and Response

**Buyer:** Chief operators, compliance managers, and utility directors at all community water systems. State primacy agencies conduct sanitary surveys every 3-5 years.

**Current workaround:** When a survey is scheduled, operators spend 2-6 weeks pulling together maintenance logs, calibration records, CT documentation, chemical feed records, operator certifications, emergency plans, and cross-connection control records from scattered locations. Paper files are organized into binders. Staff rehearse answers. The process is stressful, disruptive, and entirely manual. Survey deficiencies often stem from documentation gaps rather than actual operational failures.

**Why it is still hard:** Sanitary surveys evaluate eight elements (source, treatment, distribution, finished water storage, pumps, monitoring/reporting, management/operations, operator compliance). Each element requires specific documentation spanning years. Records are distributed across filing cabinets, SCADA historians, lab databases, and individual operators' notebooks. There is no single system of record at most small/medium utilities.

**Frequency:** Every 3-5 years per system, but the preparation burden is front-loaded into 2-6 weeks.

**Dollar impact of getting it wrong:** Survey deficiencies require formal corrective action plans. Significant deficiencies (SDs) can trigger enforcement. The soft cost is enormous: operator time diverted from operations for weeks, and the institutional stress of regulatory scrutiny.

**Regulatory urgency:** Continuous. EPA requires states to conduct sanitary surveys on a defined cycle. AWIA (2018) added cybersecurity review components.

**Existing software/vendors:** OxMaint markets a "sanitary survey package" export feature. Hach WIMS can generate some compliance reports. No product is purpose-built for sanitary survey readiness as a continuous state rather than a periodic scramble.

**Incumbent weakness:** Existing tools address pieces of the puzzle (maintenance records, water quality data) but none assemble the complete eight-element survey package. The integration problem is the core difficulty.

**AI/modern UI wedge:** Strong. A continuous compliance dashboard that tracks survey readiness across all eight elements, flags documentation gaps before they become deficiencies, and generates a survey-ready package on demand. AI can parse uploaded records, classify them by survey element, and identify what is missing. The value proposition is "never scramble for a sanitary survey again."

---

## 6. Shift Turnover and Operator Knowledge Transfer

**Buyer:** Chief operators, plant managers, and training coordinators at treatment plants with multiple shifts.

**Current workaround:** Shift turnover happens verbally, supplemented by handwritten logs or a shared Word document/whiteboard. Critical information (ongoing process adjustments, equipment issues, pending lab results, unusual source water conditions) transfers imperfectly between shifts. When an experienced operator retires, decades of plant-specific knowledge disappear.

**Why it is still hard:** The information that matters at turnover is contextual and judgment-laden. It is not just "the turbidity was 0.8 NTU." It is "turbidity has been climbing since 2 AM, I bumped coag dose to 45 mg/L, Basin 3 rake is making a noise, and the state inspector called about our last MOR." Existing SCADA systems record data points but not the operator's interpretation or intent. No commercial tool captures this operational narrative layer.

**Frequency:** 2-3 times daily at every staffed treatment plant.

**Dollar impact of getting it wrong:** Failed information transfer causes repeated process upsets, chemical waste, equipment damage, and at the extreme, treatment failures. The knowledge transfer crisis (aging workforce, 30-50% of operators eligible to retire within 5 years) is an industry-wide emergency.

**Regulatory urgency:** Indirect but real. AWWA and state agencies increasingly cite workforce development and knowledge retention as critical infrastructure concerns.

**Existing software/vendors:** Some CMMS platforms (Maximo, Cityworks) have shift log modules. OperatorLogbook exists as a niche product. Most solutions are generic industrial shift management tools not designed for water treatment context.

**Incumbent weakness:** Generic. Not built for treatment plant workflows. No awareness of process context (what does it mean that filter 4 just went offline during a high-turbidity event?). No AI-assisted summarization of SCADA trends for the incoming operator.

**AI/modern UI wedge:** Very strong. An AI-assisted turnover tool that summarizes SCADA trends from the outgoing shift, highlights anomalies, prompts the outgoing operator with structured questions ("any equipment concerns? process adjustments? pending items?"), and generates a readable turnover report. Over time, it builds an institutional knowledge base. This is the PotableLM use case made tangible as a product.

---

## 7. DBP (Disinfection Byproduct) Formation Prediction and Control

**Buyer:** Process engineers, compliance managers, and chief operators at systems with THM or HAA5 compliance challenges. Roughly 5,000-8,000 systems have DBP levels above 50% of the MCL and must actively manage formation.

**Current workaround:** Quarterly compliance samples reveal DBP levels after the fact. Utilities monitor TOC removal ratios and adjust treatment (enhanced coagulation, GAC, moving the point of chlorination) based on seasonal patterns and historical data. Engineering consultants build DBP formation models for $50,000-$200,000 per study. Day-to-day, operators have limited tools to predict how today's treatment decisions will affect next quarter's DBP results.

**Why it is still hard:** DBP formation is a delayed outcome of treatment decisions made weeks earlier. THMs and HAAs form in the distribution system over days as chlorine reacts with natural organic matter. The variables (NOM character, chlorine dose, temperature, pH, residence time in distribution) interact in ways that are plant- and system-specific. Regulatory compliance is measured as a locational running annual average (LRAA), which means a single high quarter can take a year to age out.

**Frequency:** Treatment decisions are daily. Compliance samples are quarterly. The mismatch between decision frequency and feedback frequency is the core problem.

**Dollar impact of getting it wrong:** Stage 2 DBP Rule violations require public notification and corrective action. Systems that cannot control DBPs face capital expenditures of $1M-$50M+ (GAC contactors, ozone systems, alternative disinfection). A software tool that delays or avoids that capital spend is worth $50,000-$500,000 to the utility.

**Regulatory urgency:** High. Stage 2 DBPR is active law. LRAA compliance requires continuous management. EPA is actively considering tightening THM and HAA5 MCLs.

**Existing software/vendors:** No commercial product specifically predicts DBP formation from current treatment parameters and forecasts LRAA compliance trajectories. Engineering firms build custom models. Some academic tools exist (EPANET-MSX can model DBP formation in distribution networks, but requires PhD-level expertise to configure).

**Incumbent weakness:** Consultant-dependent. Academic tools are research-grade, not operator-grade. No affordable, continuously running predictive tool exists.

**AI/modern UI wedge:** Strong. A tool that correlates historical treatment data (TOC, UV254, chlorine dose, temperature, pH) with DBP results, learns the plant-specific formation dynamics, and forecasts LRAA trends. "Your current treatment approach puts you at 72 ug/L TTHM by Q3" is enormously valuable when it comes with actionable recommendations. This requires domain expertise to build correctly, which is a defensibility advantage.

---

## 8. Chemical Feed System Calibration and Dose Verification

**Buyer:** Operators and maintenance staff at all treatment plants using chemical addition (nearly universal). Includes coagulant, caustic/lime, polymer, chlorine, fluoride, corrosion inhibitor, and potassium permanganate feeds.

**Current workaround:** Operators perform drawdown tests (measuring chemical level drop over a timed interval) or gravimetric checks, then compare to the SCADA-indicated feed rate. Results are recorded on paper logs or in spreadsheets. Calibration curves are maintained in binders. When a pump is replaced or rebuilt, the curve must be re-established.

**Why it is still hard:** Chemical feed accuracy depends on pump condition, chemical concentration (which varies between deliveries), tubing wear, back-pressure, and temperature. The math (converting drawdown volume and time to dose in mg/L at a given plant flow) is straightforward but error-prone when done mentally or on paper. Most importantly, verification frequency is driven by regulation and best practice but the records are rarely auditable in a structured format.

**Frequency:** Daily to weekly for critical chemicals (chlorine, fluoride). Monthly for others. Always after pump maintenance.

**Dollar impact of getting it wrong:** Fluoride underfeed fails the community. Fluoride overfeed (above 4.0 mg/L MCL) is a health violation. Chlorine feed errors affect CT compliance. Coagulant feed errors affect treatment performance. Corrosion inhibitor feed errors affect Lead and Copper Rule compliance.

**Regulatory urgency:** Fluoride and chlorine feed accuracy are directly regulated. Sanitary surveys review calibration records. The revised LCR makes corrosion inhibitor dosing accuracy a higher-stakes compliance item.

**Existing software/vendors:** No purpose-built chemical feed calibration tool exists. SCADA can display feed rates but cannot verify them against independent measurements. CMMS platforms can schedule calibration tasks but do not perform the calculations.

**Incumbent weakness:** No incumbent. This workflow lives entirely on paper and in operator expertise.

**AI/modern UI wedge:** Strong. A mobile tool where the operator enters drawdown test data, selects the pump and chemical, and gets instant dose verification against SCADA readings with variance flagging. Historical calibration curves track pump degradation. Regulatory-ready records are generated automatically. Simple to build, high frequency of use, clear value.

---

## 9. Filter Performance Trending and Backwash Optimization

**Buyer:** Operators and process engineers at conventional filtration plants. Roughly 8,000-10,000 surface water systems.

**Current workaround:** SCADA logs turbidity, head loss, and flow for each filter. Operators watch trends on HMI screens and initiate backwash based on time, head loss, or effluent turbidity triggers. Filter run analysis (run time vs. unit filter run volume, effluent quality profile, breakthrough patterns) is done manually if it is done at all. Most plants backwash on conservative timers rather than optimizing for run length.

**Why it is still hard:** Each filter behaves differently based on media condition, underdrain geometry, surface loading rate, and pre-treatment effectiveness. Optimizing backwash means balancing water production (longer runs = more water), filter effluent quality (longer runs risk breakthrough), and backwash water consumption (3-5% of production). The data exists in the SCADA historian, but extracting it and performing the analysis requires either a controls engineer or a process consultant.

**Frequency:** Filters run continuously. Backwash events occur every 24-96 hours per filter. Optimization reviews should happen monthly but often happen only when a consultant visits.

**Dollar impact of getting it wrong:** Suboptimal backwash wastes 1-3% of treated water production (worth $10,000-$100,000+ annually). Filter breakthrough causes turbidity violations. Media degradation from poor backwash shortens media life (replacement cost: $50,000-$200,000 per filter cell).

**Regulatory urgency:** Individual filter effluent turbidity monitoring is required under the IESWTR/LT1ESWTR. Regulatory trend: states are increasing scrutiny of filter performance data.

**Existing software/vendors:** SCADA historians (OSIsoft PI, Wonderware, GE Proficy) store the data but do not analyze it. Some consultant firms offer filter assessments as a service. No commercial product provides continuous filter performance analytics for operators.

**Incumbent weakness:** SCADA historians are raw data stores, not analytical tools. Consultants are episodic and expensive. The data-to-insight gap is wide.

**AI/modern UI wedge:** Strong. A tool that reads filter data from the SCADA historian (via standard export or API), computes filter performance metrics automatically, identifies degradation trends, and recommends backwash timing adjustments. AI can detect subtle early indicators of media problems (gradual turbidity creep, changing head loss profiles) that operators miss on an HMI screen with 20 other things competing for attention.

---

## 10. Consumer Confidence Report (CCR) Generation

**Buyer:** Compliance staff, utility managers, and in many small systems, the operator who wears every hat. All community water systems are required to produce and distribute an annual CCR.

**Current workaround:** Operators manually compile water quality data from lab results, state compliance databases, and internal records. They populate a Word or Publisher template with mandatory health effects language, source water descriptions, detected contaminants, and system-specific information. Many small systems copy last year's report and update the numbers, risking errors when regulatory language changes (which it does: LCRR requires updated lead and copper language, PFAS rule requires new contaminant reporting).

**Why it is still hard:** The CCR has specific EPA content requirements that change with new rules. Mandatory health effects language must be word-for-word per regulation. Data must be correctly converted between units and reporting formats. The report must be delivered to all customers (mailing, posting, electronic distribution) by July 1 each year. For systems serving diverse populations, translation is now expected. Many small systems treat this as an annual ordeal.

**Frequency:** Annual, but the data compilation and formatting effort spans 2-4 weeks.

**Dollar impact of getting it wrong:** Failure to produce or distribute a CCR is a compliance violation. Inaccurate health effects language creates legal exposure. The reputational risk of a poorly produced CCR (or one that omits a detected contaminant) is significant.

**Regulatory urgency:** Continuous. New PFAS MCLs and LCRR changes are actively changing what CCRs must contain in 2026 and 2027.

**Existing software/vendors:** Locus Water offers CCR generation. Some state drinking water programs provide templates. A few small companies offer CCR-as-a-service for $500-$2,000 per report. No tool auto-populates from compliance data with current regulatory language.

**Incumbent weakness:** Existing CCR services are either consultant-delivered (expensive, slow) or static templates (no auto-population, no regulatory language updates).

**AI/modern UI wedge:** Moderate to strong. A tool that pulls compliance data from state databases (many are public via SDWIS), auto-generates the CCR with current regulatory language, handles translation, and produces print-ready and web-ready outputs. AI can flag when regulatory language has changed and update templates automatically. The market is large (50,000+ systems) but willingness to pay at small systems is low ($50-200/year), so this works best bundled with other compliance tools.

---

## 11. PFAS Monitoring, Reporting, and Treatment Decision Support

**Buyer:** Utility directors, compliance managers, process engineers, and consulting engineers at all community water systems (phased monitoring requirements began 2025).

**Current workaround:** Utilities are sending samples to contract labs for PFAS analysis (costs $300-$700 per sample). Results arrive 2-4 weeks later. Compliance tracking against the new MCLs (4 ppt for PFOS, 4 ppt for PFOA, hazard index for mixtures) is done in spreadsheets. Treatment technology selection (GAC, ion exchange, high-pressure membranes) requires engineering studies costing $50,000-$500,000.

**Why it is still hard:** PFAS compliance involves a hazard index calculation for mixtures that is more complex than any previous MCL determination. The universe of PFAS compounds is large and growing. Treatment effectiveness depends on specific compound profiles, background water quality, and contact time. Lab turnaround creates a 2-4 week feedback loop. Most operators have never dealt with PFAS before.

**Frequency:** Initial monitoring is quarterly (three years), then annual or reduced depending on results.

**Dollar impact of getting it wrong:** PFAS treatment systems cost $2M-$50M+ to install and $200,000-$1M/year to operate. Selecting the wrong technology or over-designing treatment wastes millions. Under-responding risks MCL violations and public health consequences. Rate increases to fund PFAS treatment are politically explosive.

**Regulatory urgency:** Acute. The final PFAS NPDWR was published April 2024. Initial monitoring deadlines are active. The hazard index approach is new and unfamiliar to most utility staff.

**Existing software/vendors:** No purpose-built PFAS compliance management tool dominates. Locus and Klir have added PFAS tracking features. Engineering firms are the primary providers of treatment technology evaluation. EPA's PFAS Treatment Cost Estimator exists as a web tool but is designed for planning, not operations.

**Incumbent weakness:** Engineering consultants own this space but are expensive and slow. The monitoring-tracking-reporting workflow has no affordable automated solution. Small systems (85% of U.S. community water systems serve under 3,300 people) have the least capacity to navigate this.

**AI/modern UI wedge:** Moderate. A tool that tracks PFAS monitoring results, auto-computes hazard index values, projects compliance trajectory, and provides treatment technology comparison based on the system's specific compound profile. The challenge is that this market is evolving rapidly and the regulatory framework is still being litigated (judicial challenges to the PFAS rule are active).

---

## 12. Corrosion Control Treatment Optimization and LCR Compliance

**Buyer:** Process engineers, compliance officers, and operators at systems with lead and copper compliance obligations (virtually all community water systems).

**Current workaround:** Corrosion control treatment (orthophosphate, pH/alkalinity adjustment, silicate) is set based on an initial desktop or pipe loop study, often conducted by an engineering consultant 5-20 years ago. Ongoing optimization requires monitoring pH, alkalinity, temperature, orthophosphate residual, and metals at multiple points. Lead and copper tap sample results arrive quarterly, providing delayed feedback. Langelier Saturation Index and other corrosion indices are calculated manually or not at all.

**Why it is still hard:** Corrosion chemistry is affected by seasonal temperature swings, source water blending changes, and treatment process adjustments. The relationship between treatment plant chemistry and tap lead levels is mediated by distribution system age, pipe materials, and hydraulic conditions. When a system switches sources, blends supplies, or changes disinfectants, corrosion control can destabilize. The 2024 LCRI drops the action level to 10 ppb, which means systems that were previously compliant may suddenly be at risk.

**Frequency:** Water quality monitoring for corrosion parameters is continuous. Tap sampling is semi-annual to triennial depending on system history. Optimization reviews should be ongoing but typically happen only in response to compliance problems.

**Dollar impact of getting it wrong:** Lead action level exceedances under the LCRI require Tier 1 public notification within 24 hours, corrosion control optimization or re-optimization, accelerated service line replacement, and public education campaigns. The total cost of a compliance failure easily reaches $500,000-$5M+ in direct costs, with political and legal exposure on top.

**Regulatory urgency:** High and rising. LCRI compliance date is November 2027. The tightened action level will push more systems into non-compliance.

**Existing software/vendors:** No commercial tool provides continuous corrosion control monitoring with predictive modeling. Engineering consultants perform pipe loop studies ($50,000-$200,000). RTW (Research Triangle Water) and a few labs offer desktop corrosion evaluations. SCADA can log parameters but does not compute corrosion indices or flag trends.

**Incumbent weakness:** Entirely consultant-dependent. No continuous monitoring tool exists. By the time quarterly tap samples reveal a problem, the damage is done.

**AI/modern UI wedge:** Strong. A tool that continuously computes corrosion indices from plant and distribution data, correlates treatment adjustments with tap sample outcomes over time, and alerts operators to conditions that historically precede lead exceedances. The LCRI deadline creates urgency. Defensible because the chemistry and regulatory knowledge required to build this correctly is deep.

---

## 13. Emergency Response Plan Execution and Incident Documentation

**Buyer:** Chief operators, utility directors, and emergency management coordinators at all community water systems.

**Current workaround:** Emergency response plans (ERPs) exist as PDF documents in binders, often produced by consultants during AWIA compliance. When an actual emergency occurs (source contamination, main break, treatment failure, power outage, cyberattack), operators pull out the binder and work through procedures. Incident documentation is assembled after the fact from operator memory, SCADA snapshots, and phone logs. Notifications to state agencies, EPA, and the public are handled manually.

**Why it is still hard:** Emergencies are high-stress, low-frequency events. The ERP binder is static and overwhelming during a crisis. Operators need immediate access to the right procedure, the right notification contacts, and the right regulatory reporting requirements for the specific type of event. Post-incident documentation must reconstruct a timeline of actions, decisions, and communications that was not captured in real time.

**Frequency:** Actual emergencies are infrequent (a few per year). But emergency plan updates are required every 5 years under AWIA, and exercise/drill documentation is increasingly expected.

**Dollar impact of getting it wrong:** An improperly managed boil-water notice costs $50,000-$500,000+ in direct costs. Failure to notify the state within required timeframes (typically 24 hours for acute violations) is an independent regulatory violation. Post-Flint, the legal and political exposure of a mishandled water quality emergency is existential for utility leadership.

**Regulatory urgency:** AWIA (2018) requires ERPs and Risk and Resilience Assessments. EPA is adding cybersecurity review to sanitary surveys. State notification requirements are strict and time-bound.

**Existing software/vendors:** Veoci and WebEOC are enterprise emergency management platforms used by some large utilities but priced for government agencies ($50,000+/year). No water-specific emergency response tool exists for small/medium systems.

**Incumbent weakness:** Enterprise platforms are too expensive and too generic. The ERP-in-a-binder approach is universal but useless under stress.

**AI/modern UI wedge:** Moderate. A mobile-first incident management tool that presents the right procedure for the specific event type, auto-populates notification checklists (who to call, in what order, within what timeframe), logs actions in real time for post-incident documentation, and generates the required regulatory reports. AI can suggest actions based on the type and severity of the event. Adoption challenge: utilities buy emergency tools when nothing is on fire, then forget about them until something is.

---

## 14. Distribution System Water Quality Modeling and Water Age Management

**Buyer:** Process engineers, distribution system managers, and consulting engineers at medium to large water systems (serving 10,000+ people).

**Current workaround:** Hydraulic models (EPANET, InfoWater, WaterGEMS) are built by engineering consultants for capital planning. These models are expensive ($50,000-$500,000 to build and calibrate), maintained episodically, and rarely used for operational decisions. Water age and residual decay in the distribution system are understood qualitatively by experienced operators ("the south end always has low residual in summer") but not quantitatively managed.

**Why it is still hard:** Distribution system hydraulic models require accurate pipe data, demand patterns, pump curves, tank operating levels, and valve positions. Keeping a model calibrated to current conditions is labor-intensive. EPANET is free but requires engineering expertise to use. Commercial tools (Bentley WaterGEMS, Innovyze InfoWater) cost $10,000-$50,000/year in licenses. The gap between the model (maintained by a consultant) and the operator (who makes daily decisions about tank levels, pump schedules, and flushing) is wide.

**Frequency:** Operational distribution decisions (tank cycling, pump scheduling, flushing) are daily. Model updates are annual at best. The mismatch is the problem.

**Dollar impact of getting it wrong:** Poor water age management leads to disinfectant residual loss, nitrification episodes (in chloraminated systems), DBP formation, taste and odor complaints, and potential coliform violations. Nitrification events cost $10,000-$100,000+ to remediate.

**Regulatory urgency:** Moderate. Total coliform rule and disinfectant residual requirements are active. Distribution system water quality is increasingly scrutinized by state regulators.

**Existing software/vendors:** Bentley WaterGEMS/OpenFlows, Innovyze InfoWater, EPANET (free). Digital twin vendors (Xylem, Idrica) are building operational distribution models but pricing is enterprise ($100,000+/year).

**Incumbent weakness:** Too expensive and too consultant-dependent for operational use. Models are built for capital planning, not daily operations. Digital twins are nascent and priced for large utilities.

**AI/modern UI wedge:** Moderate. A simplified distribution quality model that takes SCADA data (tank levels, pump status, residual readings) and estimates water age and residual at key system points without requiring a full hydraulic model. AI can learn system behavior from historical data. The challenge is that this competes with well-funded digital twin vendors, but those vendors are selling to the top 200 utilities, leaving the next 5,000 unserved.

---

## 15. Regulatory Change Tracking and Compliance Calendar Management

**Buyer:** Compliance managers, utility directors, and chief operators at all community water systems.

**Current workaround:** Operators track compliance deadlines using Outlook calendars, wall charts, or spreadsheet-based compliance calendars. New regulatory changes are communicated via state primacy agency emails, AWWA publications, and EPA Federal Register notices. Most small system operators learn about regulatory changes from their state inspector during the next sanitary survey, which is often too late for proactive compliance.

**Why it is still hard:** The regulatory landscape for drinking water is genuinely complex: SDWA, SWTR suite, LCR/LCRR/LCRI, Stage 2 DBPR, PFAS NPDWR, Total Coliform Rule, GWR, FBRR, plus state-specific requirements. Each rule has different monitoring schedules, reporting deadlines, and triggering conditions. A medium-sized utility may have 50-100 discrete compliance deadlines per year. When rules change (LCRR, PFAS), the entire calendar shifts.

**Frequency:** Continuous. New federal or state regulatory actions occur monthly.

**Dollar impact of getting it wrong:** Missing a reporting deadline is an independent violation. Missing a monitoring period invalidates the compliance determination. At the extreme, failure to track regulatory changes results in non-compliance discovered during enforcement rather than proactively addressed.

**Regulatory urgency:** Continuous and accelerating. The pace of regulatory change (PFAS rule, LCRI, potential DBP MCL revision, cybersecurity guidance) is faster than at any point in the past decade.

**Existing software/vendors:** Locus Water, Klir, and Utility Cloud include compliance calendar features. The Water Research Foundation and AWWA provide regulatory tracking resources for members. No AI-driven regulatory intelligence tool exists specifically for water utilities.

**Incumbent weakness:** Generic calendar features in existing platforms do not auto-update when regulations change. AWWA resources require membership and manual monitoring. State agency communications are inconsistent.

**AI/modern UI wedge:** Moderate. An AI-powered regulatory tracker that monitors Federal Register notices, state agency communications, and EPA guidance documents, then auto-updates a utility-specific compliance calendar with new deadlines and requirements. The value is clear but willingness to pay as a standalone product is limited; this works best as a feature within a broader compliance platform.

---

## Summary Rankings

| Rank | Workflow | Regulatory Heat | Market Size | Wedge Strength | Incumbent Gap |
|------|----------|----------------|-------------|----------------|---------------|
| 1 | CT Compliance Calculation | Very High | ~10,000 plants | Very Strong | Wide open |
| 2 | Monthly Operating Report Assembly | High | 50,000+ systems | Very Strong | Price gap |
| 3 | Lead Service Line Inventory (LCRR/LCRI) | Acute | 50,000+ systems | Strong | Size gap |
| 4 | Coagulant Dose Optimization | Moderate | ~10,000 plants | Very Strong | No incumbent |
| 5 | Sanitary Survey Preparation | High | 50,000+ systems | Strong | No incumbent |
| 6 | Shift Turnover / Knowledge Transfer | Low-Moderate | ~15,000 staffed plants | Very Strong | Generic tools only |
| 7 | DBP Formation Prediction | High | ~8,000 systems | Strong | Consultant-only |
| 8 | Chemical Feed Calibration | Moderate | ~40,000 plants | Strong | No incumbent |
| 9 | Filter Performance Trending | Moderate | ~10,000 plants | Strong | Data gap |
| 10 | CCR Generation | Moderate | 50,000+ systems | Moderate-Strong | Fragmented |
| 11 | PFAS Monitoring and Compliance | Acute | 50,000+ systems | Moderate | Evolving fast |
| 12 | Corrosion Control Optimization | High (rising) | ~30,000 systems | Strong | Consultant-only |
| 13 | Emergency Response Plan Execution | Moderate | 50,000+ systems | Moderate | Price gap |
| 14 | Distribution System Water Quality | Moderate | ~5,000 systems | Moderate | Price/complexity |
| 15 | Regulatory Change Tracking | Moderate | 50,000+ systems | Moderate | Feature, not product |

---

## Strategic Observations

**The small-system wedge is the real opportunity.** 42,000 of the roughly 50,000 U.S. community water systems serve fewer than 10,000 people. They are priced out of enterprise platforms, underserved by consultants, and under-equipped for accelerating regulatory complexity. A $100-300/month compliance and operations platform that starts with CT calculation, MOR assembly, and compliance calendar management could capture this market before enterprise vendors move downmarket.

**Workflows 1-5 form a natural product bundle.** CT compliance, MOR assembly, sanitary survey readiness, chemical feed calibration, and compliance calendar management all share the same buyer (the chief operator or solo operator at a small system) and the same data sources (SCADA exports, lab results, chemical logs). Building any one of them well creates a natural pathway to the others.

**Coagulant optimization (#4) is the highest-defensibility wedge.** It has no incumbent, requires deep domain expertise to build correctly, and delivers immediate, measurable ROI through chemical cost reduction. It is also the hardest to build, which is why nobody has built it.

**LCRR/LCRI (#3) and PFAS (#11) are time-limited regulatory opportunities.** Both have hard compliance deadlines that compress sales cycles. But both will mature into steady-state compliance management within 3-5 years, and the initial inventory/monitoring wave is a one-time event. A startup that enters on the regulatory wave needs a product strategy for what comes after.

**The knowledge transfer problem (#6) is the existential one.** The water industry loses experienced operators faster than it replaces them. Any product that captures and systematizes operator judgment has a structural tailwind that grows every year. This is the most defensible long-term position but the hardest to monetize as a standalone product.

**Where AI specifically matters vs. where it is table stakes.** AI is transformative for workflows 4 (coagulant optimization), 6 (knowledge transfer), 7 (DBP prediction), and 12 (corrosion control) because these workflows depend on expert judgment that can be modeled. For workflows 1 (CT), 2 (MOR), 8 (calibration), and 10 (CCR), the primary value is modern UI and workflow automation; AI adds incremental value (anomaly detection, auto-population) but is not the core differentiator.
