# **High-Value Vertical SaaS Opportunities in U.S. Potable Water Operations: A Market Analysis of 15 Under-Digitized Workflows**

The United States drinking water and wastewater treatment sector is currently navigating an unprecedented structural transition, caught between an accelerating demographic crisis and a sharply tightening federal regulatory regime. Approximately one-third of the water sector's incumbent workforce—representing a vast repository of undocumented tribal knowledge—will reach retirement eligibility within the current decade.1 This "Silver Tide" is forcing utilities to grapple with succession planning and knowledge transfer precisely as the Environmental Protection Agency (EPA) introduces a new generation of data-intensive regulations.2 Facilities historically reliant on legacy control architectures, manual engineering calculations, and disconnected spreadsheets are fundamentally unequipped to handle the computational complexity required by modern compliance mandates.3

Concurrently, the broader enterprise software landscape is witnessing a structural shift toward industry-specific platforms. The vertical software-as-a-service (SaaS) market is expanding at an estimated compound annual growth rate (CAGR) of 18% to 22%, dramatically outperforming horizontal platforms.5 Investors and operators recognize that establishing a control point—embedding software directly into the core workflows of a specific industry—results in superior net revenue retention and structural defensibility.6 Within the municipal water sector, the gap between capital-intensive legacy automation hardware and modern, cloud-native analytics represents a multi-billion-dollar opportunity.7

This report identifies, analyzes, and ranks 15 high-value, under-digitized workflows in potable water treatment and distribution. These workflows are characterized by their persistent reliance on manual heuristics, isolated Laboratory Information Management Systems (LIMS), and aging Supervisory Control and Data Acquisition (SCADA) platforms that fail to provide actionable operational visibility.4 The workflows are ranked in descending order of commercial attractiveness for a venture-backed startup, weighted by regulatory urgency, total addressable dollar impact, and the vulnerability of incumbent software solutions.

## **1\. PFAS Monitoring, Remediation Planning, and Regulatory Compliance**

Per- and polyfluoroalkyl substances (PFAS) represent the most severe regulatory and capital expenditure challenge the water sector has faced since the inception of the Safe Drinking Water Act. In April 2024, the EPA finalized the National Primary Drinking Water Regulation (NPDWR), establishing an aggressive Maximum Contaminant Level (MCL) of 4.0 parts per trillion (ppt) for PFOA and PFOS.9 Crucially, the regulation also introduces a complex Hazard Index methodology to govern mixtures of various PFAS compounds, acknowledging that combined exposure yields additive health effects even if individual chemicals remain below singular limits.10

Historically, utilities tracked chemical sampling via manual uploads from LIMS directly into siloed Excel spreadsheets or static databases.7 This workflow is now computationally, operationally, and legally untenable. The NPDWR mandates strict multi-year retention and queryability for compliance reporting and Consumer Confidence Reports (CCR); however, standard cold archival storage, write-once tapes, and object storage systems lack the necessary query engines to satisfy modern compliance audits.7 Furthermore, traditional physical treatment technologies—such as granular activated carbon (GAC) or reverse osmosis—are easily exhausted by competing natural organic matter or present profound disposal challenges, forcing operators to conduct rigorous, continuous predictive sampling to determine media breakthrough thresholds.13

The incumbent software landscape remains deeply fragmented. Platforms like 120Water and Klir offer dedicated compliance modules, but utilities frequently rely on bespoke Excel trackers and disconnected SCADA networks that cannot natively correlate real-time hydrodynamic operational data with delayed LIMS laboratory results.3 Small and mid-sized systems are particularly burdened, drowning in paperwork and lacking the in-house engineering capacity to accurately calculate evolving mixture Hazard Indices.3 Furthermore, the EPA's concurrent announcement of $1 billion in infrastructure funding via the Bipartisan Infrastructure Law requires intense data substantiation for grant applications.10

A vertical SaaS startup could establish a dominant wedge by providing an AI-assisted compliance engine that automatically ingests LIMS PDFs and unstructured lab data via Natural Language Processing (NLP), structured into a relational time-series database.7 The platform would automatically calculate Hazard Indices, flag impending regulatory breaches, and seamlessly output compliant reports. By coupling this capability with an automated grant-writing assistance module, a platform could achieve negative effective churn by securing the funding necessary to pay for its own enterprise licensing.

| Workflow Attribute | Market Reality |
| :---- | :---- |
| **Buyer** | Utility Director / Chief Compliance Officer |
| **Current Workaround** | Fragmented Excel trackers; manual data entry from LIMS PDFs.7 |
| **Why it is still hard** | Complex mixture calculations; shifting multi-state primacy standards; LIMS/SCADA disconnect.11 |
| **Frequency of Use** | Weekly to monthly compliance sampling workflows.16 |
| **Dollar Impact of Error** | Millions in misallocated capital expenditures; EPA fines ranging from $2,500 to $100,000 per day.17 |
| **Urgency** | Critical. The April 2024 EPA mandate enforces a strict 3-to-5-year compliance and initial monitoring window.9 |
| **Existing Software** | 120Water, Klir, manual LIMS databases.3 |
| **Incumbent Flaws** | Enterprise pricing models price out smaller utilities; poor native integration between static LIMS and dynamic SCADA architectures.3 |
| **AI Wedge & UI** | NLP extraction of unstructured LIMS lab reports into structured databases, paired with algorithmic Hazard Index forecasting and a modern UI for grant applications. |

## **2\. Lead and Copper Rule Improvements (LCRI) Service Line Inventory Mapping**

The EPA's Lead and Copper Rule Improvements (LCRI) mandate that public water systems maintain a fully realized, exhaustive inventory of all service line materials connected to their distribution networks.19 The profound complexity of this workflow lies in the rigorous classification of "Galvanized Requiring Replacement" (GRR) lines. Identifying a GRR line depends entirely on establishing a historical chain of evidence regarding whether the galvanized pipe was *ever* situated downstream of a lead service line, requiring historical flow-direction tracing through aging infrastructure.20

Utilities currently manage this monumental data collection process using thousands of disparate spreadsheets that are heavily reliant on historical, often inaccurate, paper tap records.3 When digital tools are not employed, field technicians frequently struggle to map digital or paper records to physical geographic addresses. For example, contracted installation companies may be unable to locate meters if addresses have not been officially reconciled by county tax assessors; without digital mapping solutions, locating these endpoints manually can waste weeks of labor.3 For state primacy agencies attempting to visualize lead concentrations to distribute federal funding equitably, the lack of centralized data makes high-level resource prioritization functionally impossible.3 Furthermore, the LCRI requires a strict 24-hour Tier 1 public notification workflow for lead action level exceedances, compelling utilities to execute multi-channel alerts (radio, TV, hand delivery) manually within a critically tight window.3

While vendors like 120Water dominate the upper echelons of this space, their solutions are often priced and deployed as premium enterprise systems.3 A highly commercial SaaS startup can capture the long tail of the mid-market and small utilities by deploying a machine-learning model that predicts service line materials based on widely available municipal tax parcel data (e.g., year built), historical tap records, and neighboring parcel inferences. By accurately predicting lead probabilities, utilities can avoid the massive capital expense of physical potholing and exploratory excavation. Paired with a modern UI that automates the 24-hour Tier 1 notification engine, this creates an urgent, high-value software wedge.

| Workflow Attribute | Market Reality |
| :---- | :---- |
| **Buyer** | Operations Manager / GIS Coordinator |
| **Current Workaround** | Thousands of disparate spreadsheets; manual paper record reviews; physical potholing.3 |
| **Why it is still hard** | Deducing historical flow direction to classify GRR lines; parsing unstructured, decades-old handwritten tap cards.20 |
| **Frequency of Use** | High frequency during initial inventory development; continuous updating upon line replacements.22 |
| **Dollar Impact of Error** | Inefficient field deployments waste thousands of labor hours; misidentification leads to uncompensated capital replacements.3 |
| **Urgency** | Critical. October 2024 initiated the initial compliance deadlines.21 |
| **Existing Software** | 120Water, ESRI ArcGIS vertical solutions.3 |
| **Incumbent Flaws** | Prohibitive enterprise pricing; state agencies lack high-level aggregation visibility across fragmented utility data silos.3 |
| **AI Wedge & UI** | Predictive material modeling using tax assessor data to bypass expensive physical excavation, coupled with an automated Tier 1 public notification workflow. |

## **3\. SCADA Alarm Rationalization and Operator Fatigue Management**

Supervisory Control and Data Acquisition (SCADA) systems in water treatment plants are characterized by an ongoing "automation paradox." Automation intended to simplify operations has instead resulted in control architectures that few personnel truly understand, heavily burdened by decades of incremental additions and undocumented programmable logic controller (PLC) modifications.4 Design intent is frequently buried under successive software patches, producing opaque operating logic.4 Crucially, this results in severe alarm fatigue; facilities suffer from unrationalized alarm systems featuring default high/low configurations on every instrument, leading to hundreds of activations per shift.4

When operators face excessive alarm rates—sometimes exceeding 300 per hour—they stop responding, turning the SCADA system's last line of defense into meaningless background noise.4 Critical alarms are routinely ignored or routed to unmonitored generic email inboxes.8 Traditional SCADA alarm management places a heavy cognitive burden on field engineers, requiring them to aggregate isolated symptoms over time to determine a root cause diagnosis manually.24 When a catastrophic failure occurs (e.g., a lift station overflowing at 3 AM), the operational disconnect between the SCADA historian and the Computerized Maintenance Management System (CMMS) results in severe environmental and financial penalties.8

Existing historian software from established automation vendors focuses heavily on site-level graphical displays rather than modern operational analytics or SQL-based queryability.7 A modern SaaS wedge would sit cleanly atop legacy SCADA systems via standard protocols, utilizing an AI-driven rules engine to suppress redundant, chattering alarms and aggregate related symptoms into a single, actionable diagnosis.23 Once the AI diagnoses the root cause, it can automatically trigger a structured work order in the facility's CMMS, providing a digital audit trail that reduces unscheduled pump downtime by up to 65%.8

| Workflow Attribute | Market Reality |
| :---- | :---- |
| **Buyer** | Plant Superintendent / Control Systems Engineer |
| **Current Workaround** | Operators physically ignoring alarms; manual aggregation of discrete symptoms; email routing.4 |
| **Why it is still hard** | Undocumented legacy PLC logic; fragmented control architectures spanning 30 to 50 years of hardware.4 |
| **Frequency of Use** | Continuous (24/7/365 monitoring). |
| **Dollar Impact of Error** | Catastrophic equipment destruction; sanitary sewer overflow violations; emergency premium labor repair costs.4 |
| **Urgency** | High. Directly mitigates immediate existential asset failure and environmental compliance violations.8 |
| **Existing Software** | Legacy SCADA Historians (Citect, Wonderware), eLynx, generic CMMS.24 |
| **Incumbent Flaws** | No modern API access; poor bidirectional CMMS integration; dense legacy UIs create visual fatigue.4 |
| **AI Wedge & UI** | Pattern-recognition algorithms that group chattering alarms into a single root-cause diagnosis, instantly generating a connected CMMS work order via a modern, dark-mode mobile UI. |

## **4\. Tribal Knowledge Digitization & Standard Operating Procedure (SOP) Generation**

The operational integrity of the municipal water sector relies profoundly on "tribal knowledge"—undocumented heuristics, unique troubleshooting skills, and physical intuition accumulated over decades by veteran operators.26 With approximately one-third of the workforce reaching retirement age within the next decade, this critical knowledge is evaporating rapidly.1 Complex manual processes, from identifying subtle auditory anomalies in turbine pumps to executing specific coagulation adjustments during sudden flash-flood events, exist almost entirely in the minds of these senior operators.26

When utilities attempt to document these processes to build resiliency, they rely on text-heavy manuals or disparate word documents. In a typical maintenance department boasting 300 years of combined experience, standard operating procedures (SOPs) and CMMS records generally capture a mere 30% of the actual operational realities.28 Maintaining these static documents is exceptionally time-consuming, rendering them obsolete almost as soon as they are printed. Furthermore, veteran operators frequently lack the administrative time or software proficiency to write detailed technical manuals.29

While horizontal connected-worker platforms like Augmentir and Dozuki exist and have seen success in discrete manufacturing 27, they often lack out-of-the-box vertical context for continuous water treatment processes. A highly attractive wedge is a mobile-first application utilizing computer vision and Large Language Models (LLMs). By simply having a junior technician film a veteran operator performing a complex maintenance task or chemical adjustment, the AI can automatically extract the steps, categorize the assets, and publish a structured, version-controlled SOP in over 50 languages without requiring the operator to type a single word.29 This entirely removes the friction of knowledge capture.

| Workflow Attribute | Market Reality |
| :---- | :---- |
| **Buyer** | Plant Manager / Human Resources Director |
| **Current Workaround** | Inefficient job shadowing; outdated 3-ring binders; reactive troubleshooting.27 |
| **Why it is still hard** | Veteran operators lack the time, incentive, and software proficiency to write exhaustive technical manuals.29 |
| **Frequency of Use** | High frequency for onboarding, daily troubleshooting, and preventive maintenance task execution. |
| **Dollar Impact of Error** | Approximately 73% of asset failures stem from poor or misunderstood operational procedures.31 |
| **Urgency** | High. The demographic retirement cliff is an accelerating, non-negotiable reality.1 |
| **Existing Software** | Dozuki, Augmentir, SOPX.27 |
| **Incumbent Flaws** | Horizontal tools require significant implementation and lack AWWA-standard compliance frameworks tailored to municipal water. |
| **AI Wedge & UI** | Video-to-text AI that watches an operator via tablet camera and auto-generates a structured, searchable SOP instantly.29 |

## **5\. Coagulant Dosage Optimization & Jar Testing Mathematics**

Coagulation and flocculation are pivotal unit operations in surface water treatment. To achieve strict regulatory turbidity targets and limit the passage of dissolved organic carbon (DOC)—which serves as a precursor to disinfection byproducts—operators must precisely add coagulants like aluminum sulfate (alum) or ferric chloride.33 These chemicals neutralize negatively charged particles, allowing them to bind into larger "flocs" for sedimentation.33 Because source water quality fluctuates wildly and nonlinearly in parameters such as pH, alkalinity, and temperature, determining the exact optimal dosage is a complex chemical engineering problem.34

Currently, operators rely heavily on manual "jar testing"—a scaled-down physical simulation of the treatment plant. Using 1- or 2-liter beakers, multi-station magnetic stirrers, and micropipettes, operators physically test varying chemical doses.36 They must then perform manual calculations on paper to scale the bench results to plant flow, utilizing specific gravity and concentration math (e.g., converting pounds dry/day based on MGD flow rates).37 This traditional method is highly susceptible to human mathematical error, is intensely time-consuming, and fundamentally fails to dynamically adapt to rapid raw water fluctuations.33 Consequently, plants routinely overdose chemicals simply to guarantee regulatory compliance, generating excessive, costly sludge and vastly inflating chemical budgets.35

An AI-assisted workflow represents a massive commercial opportunity. By feeding historical SCADA telemetry (influent turbidity, pH, temperature, flow rate) into an adaptive neuro-fuzzy inference system (ANFIS) or similar machine learning model, software can accurately predict optimal alum or polyaluminum chloride (PAC) dosages in real-time.34 Providing operators with a streamlined tablet app that replaces arduous physical jar tests with a highly accurate digital twin model would save tens of thousands of dollars in chemical costs annually per facility, ensuring immediate ROI.

| Workflow Attribute | Market Reality |
| :---- | :---- |
| **Buyer** | Chief Operator / Process Engineer |
| **Current Workaround** | Manual benchtop jar tests using physical beakers; paper-based specific gravity math.36 |
| **Why it is still hard** | Highly nonlinear, multivariable relationship between raw water chemistry and physical flocculation kinetics.34 |
| **Frequency of Use** | Daily, or multiple times per shift during weather events.39 |
| **Dollar Impact of Error** | Massive chemical waste from systemic overdosing; geometrically increased sludge disposal costs.35 |
| **Urgency** | High. Delivers immediate operating expense (OPEX) savings while ensuring continuous turbidity compliance.36 |
| **Existing Software** | None dominant; predominantly manual calculations or basic SCADA pacing.34 |
| **Incumbent Flaws** | Physical tests take too long to react to flash-flood source water changes; SCADA pacing relies on static ratios.34 |
| **AI Wedge & UI** | Predictive ML models replacing physical jar testing, validating recommended dose via historical correlation presented on a simple tablet interface.34 |

## **6\. Algal Bloom & Cyanotoxin Predictive Monitoring (PAC Dosing)**

Harmful algal blooms (HABs) in source water reservoirs produce potent secondary metabolites, most notably geosmin (GSM) and 2-methylisoborneol (2-MIB), which cause severe taste and odor events.40 Because human olfactory senses can detect these compounds at infinitesimal concentrations—as low as 4 to 10 ng/L for geosmin—conventional water treatment plants are completely ineffective at removing them.40 Utilities are thus forced to implement advanced, highly expensive treatments, primarily dosing massive quantities of powdered activated carbon (PAC) to adsorb the compounds.40

The current workflow is heavily reactive and analog. Utilities conduct manual microscopic analyses or, worse, rely on lagging indicators such as a sudden influx of customer complaints regarding earthy or musty water.42 By the time a bloom is visually detected or smelled, the required PAC dosage spikes astronomically, with monthly chemical costs at heavily impacted sites exceeding $122,000.44 While advanced flow imaging microscopy (e.g., FlowCam) exists to automate particle counting, it requires significant upfront capital expenditure and specialized laboratory expertise.42

A vertical SaaS startup could circumvent the need for laboratory hardware by aggregating high-resolution, near-daily satellite multispectral imagery with hydrodynamic modeling to forecast bloom trajectories before they reach utility intake structures.46 By combining this early-warning spatial data with an algorithmic cost-optimizer that calculates the exact required PAC dose based on the specific gravity and competitive adsorption of natural organic matter 40, utilities could proactively suppress blooms at a fraction of the reactive cost.

| Workflow Attribute | Market Reality |
| :---- | :---- |
| **Buyer** | Water Quality Manager / Treatment Director |
| **Current Workaround** | Manual microscopy; reactive PAC overdosing based strictly on customer taste-and-odor complaints.43 |
| **Why it is still hard** | Rapid bloom onset; GSM/MIB detectable at sub-nanogram levels requiring intense precision.40 |
| **Frequency of Use** | Seasonal, but highly active and critical throughout summer and fall.45 |
| **Dollar Impact of Error** | Up to $122,000/month in reactive chemical spending; severe reputational damage.40 |
| **Urgency** | Moderate to High. Driven by the immediate loss of public trust when tap water tastes foul.40 |
| **Existing Software** | FlowCam (Hardware-centric image analysis).42 |
| **Incumbent Flaws** | Capital-intensive hardware installations; does not provide predictive, macro-level watershed forecasting.43 |
| **AI Wedge & UI** | Satellite imagery analysis using ML to predict blooms hydrodynamically, paired with a chemical cost-optimization UI to recommend preemptive PAC dosing.46 |

## **7\. Disinfection Byproduct (DBP) Formation Prediction**

When essential disinfectants like chlorine react with naturally occurring organic matter (NOM) in source water, they form carcinogenic Disinfection Byproducts (DBPs), most notably Trihalomethanes (TTHM) and Haloacetic acids (HAA5).49 Compliance with the EPA's Stage 2 DBP Rule is rigorously enforced at specific locational running annual averages (LRAA) throughout the distribution network, with knowing violations triggering federal penalties ranging between $50,000 and $100,000 per day.18

Predicting DBP formation is an immensely complex computational workflow. NOM lacks a defined molecular structure, meaning its reactivity varies constantly. Variables such as water age, pH, bromide concentration, Specific Ultraviolet Absorbance (SUVA), and temperature all dictate the final DBP yield.49 Furthermore, calculating the Bromine Substitution Factor (BSF) requires intricate molar concentration mathematics.54 Small and mid-sized utilities currently rely on rudimentary Excel spreadsheets or hire specialized engineering consultants to build custom empirical models.49 Traditional hydraulic modeling software like Bentley WaterGEMS or Innovyze InfoWater Pro are viewed as the legacy standards but are routinely criticized for having disjointed toolchains—forcing users through disconnected Domain Managers, DB Query Sets, and Facility Sets—and esoteric user interfaces laden with "secret little buttons that make no sense".57

A SaaS wedge involves deploying advanced non-parametric machine learning regression models, such as Support Vector Regression (SVR) or Gaussian Process Regression (GPR). These ML techniques have been scientifically proven to model the nonlinear connections in DBP formation far more accurately than legacy stepwise multiple linear regression.53 Integrating this modeling into a modern, cloud-native UI that does not require an engineering PhD to navigate would rapidly capture market share from legacy desktop platforms.

| Workflow Attribute | Market Reality |
| :---- | :---- |
| **Buyer** | Process Engineer / Regulatory Compliance Officer |
| **Current Workaround** | Expensive specialized consultants; basic linear Excel regressions.49 |
| **Why it is still hard** | Structural complexity of NOM precursors; intricate Bromine Substitution Factor (BSF) math; nonlinear variable interaction.53 |
| **Frequency of Use** | Weekly to monthly compliance modeling runs. |
| **Dollar Impact of Error** | $50,000 to $100,000 per day in EPA fines for knowing Stage 2 DBPR violations.18 |
| **Urgency** | High. Strict federal regulatory mandate governing human carcinogen exposure.50 |
| **Existing Software** | Bentley WaterGEMS, Innovyze InfoWater Pro.58 |
| **Incumbent Flaws** | Extremely complex, disjointed UI; exorbitant licensing costs for small utilities.57 |
| **AI Wedge & UI** | SVR and Random Forest ML models predicting DBPs based on simple real-time SCADA inputs, presented in a unified, modern web interface.53 |

## **8\. Pump Shutdown & Isolation Planning**

The failure to properly plan and execute pump shutdowns costs U.S. water utilities an estimated $2.8 billion annually in emergency repairs, regulatory penalties, and disruptions to customer service.31 Because pumping is critical to maintaining system pressure, AWWA standards and state drinking water programs dictate stringent isolation and lockout/tagout (LOTO) protocols prior to maintenance to prevent system damage and worker injury.31

Despite these high-stakes requirements, the prevailing workflow relies on archaic paper checklists, clipboards, and verbal coordination.31 Because traditional paper workflows are highly vulnerable to incomplete entries, supervisors lack real-time visibility into isolation statuses across the facility.31 Missing a single valve isolation sequence is identified as the leading cause of pump damage during maintenance, routinely escalating a standard 4-hour preventive job into a multi-day emergency crisis.31 Furthermore, during state audits, facilities are routinely cited not for equipment failure, but for documentation gaps regarding zero-energy state verification.31 In total, roughly 73% of asset failures are attributed to poor operational procedures rather than mechanical lifecycle exhaustion.31

While enterprise CMMS platforms (e.g., Fiix, Maximo) exist, they are often generic horizontal tools that lack deep integration with process control systems.8 A dedicated vertical workflow tool that automatically generates AWWA-compliant digital shutdown sequences, features dynamic risk-scoring to prioritize critical assets (e.g., high-service distribution pumps vs. utility pumps), and integrates directly with SCADA for return-to-service verification provides a compelling, defensible wedge.31

| Workflow Attribute | Market Reality |
| :---- | :---- |
| **Buyer** | Maintenance Manager / Plant Superintendent |
| **Current Workaround** | Paper checklists, vulnerable verbal coordination, physical binders.31 |
| **Why it is still hard** | Intricate valve sequencing logic and strict regulatory zero-energy state verification requirements.31 |
| **Frequency of Use** | Weekly, or per-maintenance event. |
| **Dollar Impact of Error** | $2.8 billion annually in unplanned outages and catastrophic asset destruction.31 |
| **Urgency** | Moderate to High. Driven by worker safety, asset liability, and stringent audit compliance.31 |
| **Existing Software** | Generic horizontal CMMS platforms.8 |
| **Incumbent Flaws** | Lack of native SCADA integration; generic non-water workflows that fail to account for hydraulic consequences.8 |
| **AI Wedge & UI** | Generative AI creating optimal LOTO sequences based on digital twin piping & instrumentation diagrams (P\&IDs) with a mobile-first field execution app. |

## **9\. Non-Revenue Water (NRW) / Water Loss Tracking**

Non-revenue water (NRW)—defined as the sum of real losses (physical pipe leaks) and apparent losses (meter inaccuracies, unauthorized consumption, and billing data errors)—costs U.S. utilities over $6.4 billion annually, representing roughly 19.5% of all treated drinking water.60 The scale of the infrastructure, encompassing 2.2 million miles of buried pipe nationwide, makes leak detection exceedingly difficult.61 Small systems are particularly devastated, frequently reporting losses exceeding 20% of total supply.62

Utilities currently approach water loss via the AWWA M36 manual audit process, utilizing cumbersome annual spreadsheets that rely on estimated, aggregated data rather than high-resolution telemetry.63 While many utilities deploy Advanced Metering Infrastructure (AMI), the sheer volume of data is paralyzing; a mid-size utility with 100,000 endpoints generates 2.4 million readings per day.7 Standard Meter Data Management (MDM) systems are architected for monthly billing cycles, not for the sub-hourly operational analytics required to conduct real-time mass balances and identify leaks.7 The Jackson, Mississippi crisis—where a broken mainline leaked 5 million gallons daily over seven years—exemplifies the consequence of undetected losses.64

Hardware vendors like Echologics provide acoustic leak detection, but deploying physical sensors is highly capital intensive and requires exhaustive proof-of-concept piloting.65 A purely software-based SaaS approach can leverage time-series databases (e.g., TimescaleDB) to ingest SCADA flow data and AMI consumption data at scale.7 Applying AI anomaly detection algorithms to this unified data stream can mathematically pinpoint district metered areas (DMAs) experiencing hidden real losses or under-registering meters, completely bypassing the need for new physical hardware deployments.7

| Workflow Attribute | Market Reality |
| :---- | :---- |
| **Buyer** | Finance Director / Utility Director |
| **Current Workaround** | AWWA M36 manual spreadsheets; reactive physical acoustic surveys.63 |
| **Why it is still hard** | Massive data volume limits of MDMs; mathematically parsing apparent vs. real loss from noisy data.7 |
| **Frequency of Use** | Monthly to quarterly reporting; real-time operational monitoring. |
| **Dollar Impact of Error** | $6.4 billion in uncaptured revenue annually across the U.S. sector.62 |
| **Urgency** | High. Financial survival is at stake, particularly for under-resourced small systems losing \>20% of water.62 |
| **Existing Software** | MDM Systems, Echologics (Hardware), Bentley WaterGEMS.7 |
| **Incumbent Flaws** | MDMs lack high-frequency operational analytics capabilities; acoustic sensors are prohibitively expensive.7 |
| **AI Wedge & UI** | Algorithmic mass-balance using existing AMI/SCADA data to isolate leakage zones virtually, displayed on a high-level GIS dashboard. |

## **10\. Filter Backwash Optimization**

Granular media filtration is a core physical barrier in water treatment, relying on sedimentation, interception, and diffusion to capture pathogens.67 As filters accumulate suspended solids, they must be periodically cleaned via a backwash process, which reverses the flow of clean, treated water to dislodge particles.68

Currently, operators rely heavily on manual timers or rudimentary visual turbidity checks to initiate and terminate backwashing.68 This manual paradigm leads to chronic over-washing and under-washing. Over-washing wastes millions of gallons of valuable potable water, expends significant pumping energy, and degrades the filter media; under-washing creates mud balls, shortens filter run times, and risks turbidity compliance violations.69 Furthermore, determining the optimal backwash flow rate requires complex manual adjustments for water viscosity, which changes dynamically with seasonal temperature fluctuations—colder, more viscous water requires lower flow rates to achieve identical bed expansion.71

While some incumbent vendors (e.g., Hach Claros) offer data management tools, they are often inextricably tied to proprietary hardware ecosystems.72 A hardware-agnostic SaaS wedge could ingest data from any existing continuous turbidity sensor and apply predictive analytics to calculate the ideal Uniform Filter Run Volume (UFRV).67 By automatically recommending precise start and stop times, and dynamically adjusting for seasonal viscosity, the software minimizes treated water waste and eliminates manual operator guesswork entirely.70

| Workflow Attribute | Market Reality |
| :---- | :---- |
| **Buyer** | Plant Operator / Operations Manager |
| **Current Workaround** | Manual static timers; rigid SOPs that ignore water viscosity changes.69 |
| **Why it is still hard** | Constant seasonal temperature adjustments; balancing media expansion against particle conditioning requirements.67 |
| **Frequency of Use** | Daily or weekly per filter unit.68 |
| **Dollar Impact of Error** | Excessive loss of finished, treated water; premature filter media replacement; wasted pumping energy.69 |
| **Urgency** | Moderate. Driven by OPEX optimization, asset preservation, and water conservation goals.69 |
| **Existing Software** | SCADA static timers; Hach Claros.69 |
| **Incumbent Flaws** | Timers are blind to actual media conditions; severe vendor lock-in with proprietary hardware providers.69 |
| **AI Wedge & UI** | ML optimization of Uniform Filter Run Volumes (UFRV) to dynamically adjust backwash durations and flow rates, overriding static timers.67 |

## **11\. Capital Improvement Plan (CIP) Scenario Modeling**

Capital Improvement Plans (CIP) govern the strategic allocation of millions—often billions—of dollars toward infrastructure rehabilitation and expansion. Creating a CIP requires modeling long-term funding scenarios over 20-year horizons, assessing asset condition, prioritizing replacements, and calculating the resultant impact on consumer rate tariffs and financial reserves.73

Astonishingly, the vast majority of utilities manage this highly technical, high-stakes workflow in fragile Excel spreadsheets.74 When variables inevitably change—such as receiving a sudden infrastructure grant or facing an emergency main break that reshuffles priorities—the static spreadsheet "blows up in your face like an aggressively shaken bottle of Coke," forcing engineers to manually recalculate rate impacts and project timelines.74 This reliance on manual data entry and experience-based intuition results in severe inaccuracies; globally, 64% of megaprojects face cost overruns.76 Furthermore, utility executives require extreme precision; a mere 0.01% deviation in portfolio estimates can heavily distort regulatory rate cases when aggregated across billions in capital spending.77

Incumbent software falls into two unhelpful extremes: overly simplistic database tools like Plan-It that merely digitize the spreadsheet, or massive, complex enterprise project controls like InEight built for tier-one global construction firms.75 A vertical SaaS startup could introduce an AI-driven cost estimation and scenario modeling tool aligned with AACE International standards.77 By embedding machine learning to detect historical cost outliers and internal inconsistencies in bid data, utilities could instantly generate 20-year rate scenarios with high statistical confidence.73

| Workflow Attribute | Market Reality |
| :---- | :---- |
| **Buyer** | City Engineer / Finance Director |
| **Current Workaround** | Fragile, manually updated Excel spreadsheets; reactive reprioritization.74 |
| **Why it is still hard** | Constant timeline shifting; complex rate-impact modeling; integrating disparate reserve funds.73 |
| **Frequency of Use** | Annual baseline planning; highly disruptive quarterly revisions.74 |
| **Dollar Impact of Error** | 50%+ cost overruns on major projects; regulatory rate case denials; chronic underfunding.76 |
| **Urgency** | Moderate. Features a long enterprise sales cycle, but remains critical for municipal financial survival. |
| **Existing Software** | Plan-It, InEight, EPA NSWC.75 |
| **Incumbent Flaws** | Spreadsheets lack auditability; InEight is too complex and expensive for mid-market utilities.75 |
| **AI Wedge & UI** | ML-driven cost estimation utilizing historical bid data to auto-detect pricing anomalies, allowing dynamic drag-and-drop scenario modeling.77 |

## **12\. Consumer Confidence Report (CCR) Aggregation**

Under the Safe Drinking Water Act, 50,000 U.S. water utilities are mandated to produce an annual Consumer Confidence Report (CCR) detailing water quality, source information, and compliance violations.80

This regulatory requirement demands a massive manual aggregation of data from disparate SCADA historians and LIMS databases.7 Because these systems do not natively interface, environmental compliance staff spend hundreds of labor hours copying data, validating formatting, and fighting broken spreadsheet formulas.12 Furthermore, utilities face a significant public communications challenge: the EPA requires these reports to be transparent and accessible, yet standard templates result in documents reading at an 11th-grade level, filled with impenetrable abbreviations that alienate the public.80

Incumbents like Hach WIMS promise data integration, but often require heavy IT support to build custom reporting modules and maintain ongoing database development, leaving smaller, resource-constrained utilities stranded.15 Klir offers an alternative cloud operating system, but the market remains highly under-penetrated.15 A lightweight SaaS application leveraging Large Language Models (LLMs) could automatically ingest the raw LIMS/SCADA outputs, translate the technical jargon into an engaging, 8th-grade reading level narrative, and instantly generate multi-lingual, compliant digital reports, radically reducing administrative burden and building community trust.12

| Workflow Attribute | Market Reality |
| :---- | :---- |
| **Buyer** | Water Quality Manager / Public Relations |
| **Current Workaround** | Manual copy-pasting from LIMS into Word/PDF templates; broken Excel formulas.12 |
| **Why it is still hard** | Translating highly technical contaminant data into public-friendly metrics without violating EPA rigid formatting.80 |
| **Frequency of Use** | Annually (July 1st strict distribution deadline).83 |
| **Dollar Impact of Error** | High internal labor costs; severe erosion of public trust leading to bond measure failures if communication is opaque.80 |
| **Urgency** | Moderate. Predictable annual deadline, but compliance is strictly enforced.83 |
| **Existing Software** | Klir, Hach WIMS.15 |
| **Incumbent Flaws** | WIMS requires intense IT overhead; standard EPA templates are unreadable by the general public.25 |
| **AI Wedge & UI** | LLMs converting raw chemical data into accessible, multi-lingual public health narratives with one-click web publishing. |

## **13\. Cybersecurity Vulnerability Assessment (AWWA J100)**

Water infrastructure is increasingly a prime target for nation-state actors and ransomware syndicates seeking to disrupt critical civil services.84 While Section 2013 of America's Water Infrastructure Act (AWIA) requires utilities to assess cyber risks, the technical gap between enterprise IT networks and operational technology (OT) networks leaves utilities profoundly vulnerable.84 Legacy PLCs are rarely patched, and many systems have unnecessary, poorly secured internet exposure.85

To comply with frameworks like AWWA J100 and NIST, utilities typically rely on expensive third-party engineering consultants or utilize manual, spreadsheet-based assessment tools provided voluntarily by the EPA or AWWA.88 This static approach dictates that compliance is merely a snapshot in time rather than continuous, zero-trust protection.90

Enterprise platforms like Dragos provide deep OT cybersecurity monitoring, but are priced and scaled well beyond the reach of mid-market and small utilities, which average only about 6% of IT budgets spent on cybersecurity.91 A vertical SaaS startup could offer an automated, lightweight vulnerability scanning and policy-generation platform tailored specifically to water OT protocols (e.g., Modbus, DNP3). While existential risk is extremely high, this workflow ranks slightly lower on commercial attractiveness due to recent legal pushback that resulted in the pausing of the EPA's mandatory cybersecurity regulatory enforcement, which temporarily softens the urgency for immediate procurement.93

| Workflow Attribute | Market Reality |
| :---- | :---- |
| **Buyer** | IT Director / General Manager |
| **Current Workaround** | Expensive consultants; AWWA spreadsheet checklists; manual fallback procedures.88 |
| **Why it is still hard** | Bridging the massive technical divide between modern enterprise IT and decades-old legacy plant OT.84 |
| **Frequency of Use** | Annual compliance audits; continuous threat monitoring.87 |
| **Dollar Impact of Error** | Catastrophic ransomware payouts; total operational shutdown and loss of SCADA telemetry.84 |
| **Urgency** | Mixed. The existential threat is critical, but the EPA regulatory mandate is currently paused due to litigation.93 |
| **Existing Software** | Dragos, AWWA Cybersecurity Tool.89 |
| **Incumbent Flaws** | Dragos is enterprise-focused and expensive; the AWWA tool is purely manual and static.89 |
| **AI Wedge & UI** | Automated policy generation and network scanning mapped directly to AWWA J100 and NIST frameworks, outputting continuous risk scores.88 |

## **14\. Pump Energy Management & Tariff Optimization**

Providing safe drinking water is exceptionally energy-intensive. Pumping operations account for 90% to 99% of a water utility’s energy consumption, representing up to 40% of a municipality's entire energy bill and consuming 56 billion kilowatt hours (kWh) annually in the U.S..96 Energy tariffs negotiated with power providers are highly complex, involving time-of-use block rates, variable demand charges, and peak pricing schedules.97

Operators attempt to manually control pump on/off cycles to avoid peak energy tariffs, but doing so while respecting rigid hydraulic constraints—such as maintaining minimum storage tank levels, system pressure limits, and chemical contact times—is a mathematically daunting task.98 Current hydraulic modeling software like Bentley WaterGEMS provides an Energy Management module, but it requires highly complex configurations involving digital "Power Meters" and manual scenario aggregations over billing periods that fail to react autonomously to real-time grid conditions.97 Spreadsheets are frequently used but are wholly inadequate for long-term analytics.100

A specialized AI optimization layer, utilizing methodologies such as the Artificial Electric Field Algorithm (AEFA), could continuously pull real-time tariff data via API, process the EPANet hydraulic constraints, and automatically schedule optimal pump runtimes.98 While the OPEX savings are massive, this opportunity ranks lower because it requires deep, read/write integration with legacy SCADA control systems, significantly extending the technical deployment and sales cycle.

| Workflow Attribute | Market Reality |
| :---- | :---- |
| **Buyer** | Operations Director / Finance Director |
| **Current Workaround** | Manual scheduling based on static spreadsheets and operator intuition regarding tank levels.100 |
| **Why it is still hard** | Balancing complex multi-tier tariffs against strict hydraulic network constraints (pressures, levels).97 |
| **Frequency of Use** | Daily, real-time operational scheduling. |
| **Dollar Impact of Error** | Pumping consumes 56 billion kWh annually nationwide; inefficient scheduling wastes millions of OPEX dollars.96 |
| **Urgency** | Low regulatory urgency; driven purely by financial OPEX reduction mandates.96 |
| **Existing Software** | Bentley WaterGEMS Energy Management.97 |
| **Incumbent Flaws** | Not built for autonomous, real-time SCADA integration; highly cumbersome and manual setup.97 |
| **AI Wedge & UI** | Predictive machine learning to forecast tank demand and algorithmically actuate pumps at the lowest-cost hours without operator intervention. |

## **15\. Fire Flow Testing & Hydraulic Model Updating**

Fire flow testing is vital to verify that the municipal distribution system can supply adequate water for fire suppression capabilities. This data is rigorously analyzed by the Insurance Services Office (ISO) to establish a community’s Public Protection Classification (PPC); a poor ISO rating dramatically increases commercial and residential insurance premiums across the entire municipality.101

The workflow is highly manual and prone to environmental error. Field technicians utilize physical pitot gauges and cap gauges to measure static, residual, and flow pressures across two hydrants.101 They must manually apply the empirical Freeman Flow Formula (Q formula) and the Hazen-Williams equation to evaluate water flow through pipes, while meticulously correcting for hydraulic grade line (HGL) elevation head differences to determine available flow at a 20 psi residual threshold.101 Engineering consultants then manually input these findings back into desktop hydraulic models to recalibrate the overarching system design.57

While economically essential for a community, this workflow ranks lowest due to its infrequent nature per asset and the highly niche buyer profile. However, an accessible mobile application that utilizes native GPS to calculate elevation deltas automatically, runs the complex Freeman formulas on-site, and pushes the standardized data via API directly to GIS and hydraulic modeling software would eliminate significant administrative lag and math errors.105

| Workflow Attribute | Market Reality |
| :---- | :---- |
| **Buyer** | Field Technician / Engineering Consultant |
| **Current Workaround** | Manual pitot gauges; hand calculations of the Freeman formula; manual desktop entry.101 |
| **Why it is still hard** | Complex hydraulic grade line (HGL) elevation corrections; determining Hazen-Williams friction coefficients.104 |
| **Frequency of Use** | Periodic. Typically performed per new commercial development or based on the ISO 10-year audit schedule.101 |
| **Dollar Impact of Error** | Poor data leads to downgraded ISO ratings, unnecessarily inflating community insurance premiums by hundreds of dollars per household.102 |
| **Urgency** | Low daily operational urgency; high long-term community financial impact. |
| **Existing Software** | Innovyze InfoWater Pro (for the modeling component).57 |
| **Incumbent Flaws** | Desktop-bound legacy software; lacks modern mobile field-data collection synergy and fluid UI.57 |
| **AI Wedge & UI** | Mobile app utilizing GPS and ML to instantly calculate HGL deltas and auto-update network models via API. |

## **Strategic Conclusion**

The U.S. potable water sector represents a profound, yet largely overlooked, vertical SaaS opportunity. Legacy software platforms have systematically failed the mid-market and small utility segments through exorbitant enterprise pricing, disjointed legacy architectures, and a stubborn reliance on manual data entry bridging disjointed systems.25 As federal mandates—such as the LCRI and the PFAS NPDWR—force an unprecedented data-reporting burden onto a shrinking, retiring workforce, software adoption is no longer an optional optimization; it is an existential requirement.1

Startups that deploy artificial intelligence not merely as a generative novelty, but as a core analytical engine—whether predicting complex DBP chemistry 53, translating tribal knowledge into structured SOPs 29, or algorithmically diagnosing SCADA alarm floods 24—will establish dominant, sticky control points. By focusing on workflows that deliver immediate regulatory compliance and hard OPEX reduction, modern SaaS vendors can bypass the long, consultant-heavy sales cycles of the past and rapidly capture market share in a highly lucrative industry.5

#### **Works cited**

1. The workforce is changing – will your utility change with it? \- Arcadis, accessed April 29, 2026, [https://www.arcadis.com/en-us/insights/blog/united-states/zakiya-seymour/2023/the-workforce-is-changing-will-your-utility-change-with-it](https://www.arcadis.com/en-us/insights/blog/united-states/zakiya-seymour/2023/the-workforce-is-changing-will-your-utility-change-with-it)  
2. Under the Surface: Hidden Workforce Challenges Facing Public Water Workers, accessed April 29, 2026, [https://efcnetwork.org/under-the-surface-hidden-workforce-challenges-facing-public-water-workers/](https://efcnetwork.org/under-the-surface-hidden-workforce-challenges-facing-public-water-workers/)  
3. Starting Your LCRI Journey \- 120Water, accessed April 29, 2026, [https://www.120water.com/blog/starting-your-lcri-journey](https://www.120water.com/blog/starting-your-lcri-journey)  
4. When Automation Outpaces Understanding: Alarm Management ..., accessed April 29, 2026, [https://controlassociatesinc.com/blog/automation-vs-operational-understanding](https://controlassociatesinc.com/blog/automation-vs-operational-understanding)  
5. Why Vertical SaaS Is Outperforming Horizontal Platforms in 2026, accessed April 29, 2026, [https://www.saasmag.com/vertical-saas-outperforming-horizontal-2026/](https://www.saasmag.com/vertical-saas-outperforming-horizontal-2026/)  
6. 2025 Vertical & SMB SaaS Benchmark Report \- Tidemark, accessed April 29, 2026, [https://www.tidemarkcap.com/vskp-chapter/2025-vertical-smb-saas-benchmark-report](https://www.tidemarkcap.com/vskp-chapter/2025-vertical-smb-saas-benchmark-report)  
7. Water Utilities Database: Store and Query SCADA, AMI & Quality ..., accessed April 29, 2026, [https://www.tigerdata.com/learn/water-utilities-database-how-to-store-query-scada-ami-quality-data-at-scale](https://www.tigerdata.com/learn/water-utilities-database-how-to-store-query-scada-ami-quality-data-at-scale)  
8. SCADA Integration with CMMS for Water and Wastewater Utilities \- Oxmaint, accessed April 29, 2026, [https://oxmaint.com/industries/government/scada-integration-cmms-water-wastewater-utilities](https://oxmaint.com/industries/government/scada-integration-cmms-water-wastewater-utilities)  
9. Key EPA Actions to Address PFAS | US EPA, accessed April 29, 2026, [https://www.epa.gov/pfas/key-epa-actions-address-pfas](https://www.epa.gov/pfas/key-epa-actions-address-pfas)  
10. Per- and Polyfluoroalkyl Substances (PFAS) | US EPA, accessed April 29, 2026, [https://www.epa.gov/sdwa/and-polyfluoroalkyl-substances-pfas](https://www.epa.gov/sdwa/and-polyfluoroalkyl-substances-pfas)  
11. Questions & Answers: PFAS National Primary Drinking Water Regulation (April 2024\) \- EPA, accessed April 29, 2026, [https://www.epa.gov/system/files/documents/2024-04/pfas-npdwr\_qa\_general\_4.9.24v1.pdf](https://www.epa.gov/system/files/documents/2024-04/pfas-npdwr_qa_general_4.9.24v1.pdf)  
12. LIMS and SCADA Combine to Meet Regulatory Requirements for Direct Potable Reuse, accessed April 29, 2026, [https://atlab.com/2023/11/29/lims-and-scada-combine-to-meet-regulatory-requirements-for-direct-potable-reuse/](https://atlab.com/2023/11/29/lims-and-scada-combine-to-meet-regulatory-requirements-for-direct-potable-reuse/)  
13. Cross-national challenges and strategies for PFAS regulatory compliance in water infrastructure \- Haley Aldrich, accessed April 29, 2026, [https://www.haleyaldrich.com/resources/publications/cross-national-challenges-and-strategies-for-pfas-regulatory-compliance-in-water-infrastructure/](https://www.haleyaldrich.com/resources/publications/cross-national-challenges-and-strategies-for-pfas-regulatory-compliance-in-water-infrastructure/)  
14. Overview of Drinking Water Treatment Technologies | US EPA, accessed April 29, 2026, [https://www.epa.gov/sdwa/overview-drinking-water-treatment-technologies](https://www.epa.gov/sdwa/overview-drinking-water-treatment-technologies)  
15. Klir vs. Hach WIMS: Choosing a Water Data Management Platform That Makes Sense for You, accessed April 29, 2026, [https://www.klir.com/resources/klir-vs-hach-wims-choosing-a-water-data-management-platform-that-makes-sense-for-you](https://www.klir.com/resources/klir-vs-hach-wims-choosing-a-water-data-management-platform-that-makes-sense-for-you)  
16. EPA Sets First-Time Limits for Six PFAS in Drinking Water \- Stinson LLP, accessed April 29, 2026, [https://www.stinson.com/newsroom-publications-epa-sets-first-time-limits-for-six-pfas-in-drinking-water](https://www.stinson.com/newsroom-publications-epa-sets-first-time-limits-for-six-pfas-in-drinking-water)  
17. Polyfluoroalkyl Substances (PFAS) and Lead Service Lines (LSL) Compliance in Virginia – 2025 \- Reports to the General Assembly, accessed April 29, 2026, [https://rga.lis.virginia.gov/Published/2025/RD114/PDF](https://rga.lis.virginia.gov/Published/2025/RD114/PDF)  
18. Criminal Provisions of Water Pollution | US EPA, accessed April 29, 2026, [https://www.epa.gov/enforcement/criminal-provisions-water-pollution](https://www.epa.gov/enforcement/criminal-provisions-water-pollution)  
19. Revised Lead and Copper Rule | US EPA, accessed April 29, 2026, [https://www.epa.gov/ground-water-and-drinking-water/revised-lead-and-copper-rule](https://www.epa.gov/ground-water-and-drinking-water/revised-lead-and-copper-rule)  
20. EPA's Final Lead and Copper Rule Improvements Technical Fact Sheet: Service-Line Inventory and Replacement Requirements, accessed April 29, 2026, [https://www.epa.gov/system/files/documents/2024-10/final\_lcri\_fact-sheet\_service-line-inventory.pdf](https://www.epa.gov/system/files/documents/2024-10/final_lcri_fact-sheet_service-line-inventory.pdf)  
21. Lead and Copper Rule Implementation Tools | US EPA, accessed April 29, 2026, [https://www.epa.gov/dwreginfo/lead-and-copper-rule-implementation-tools](https://www.epa.gov/dwreginfo/lead-and-copper-rule-implementation-tools)  
22. Lead Service Line Inventory—EPA's Lead and Copper Rule Revisions | Washington State Department of Health, accessed April 29, 2026, [https://doh.wa.gov/community-and-environment/drinking-water/contaminants/lead/lead-and-copper-rule-revisions](https://doh.wa.gov/community-and-environment/drinking-water/contaminants/lead/lead-and-copper-rule-revisions)  
23. The Ultimate Guide to Alarm Management for Field Engineers in the Water Industry, accessed April 29, 2026, [https://www.racoman.com/blog/the-ultimate-guide-to-alarm-management-for-field-engineers-in-the-water-industry](https://www.racoman.com/blog/the-ultimate-guide-to-alarm-management-for-field-engineers-in-the-water-industry)  
24. Bridge the Gap Between SCADA and Data Analytics \- eLynx Technologies, accessed April 29, 2026, [https://www.elynxtech.com/post/elynx-historian-solution](https://www.elynxtech.com/post/elynx-historian-solution)  
25. HACH WATER INFORMATION MANAGEMENT SOLUTION (WIMS), accessed April 29, 2026, [https://www.opssys.com/InstantKB/attachments/Water%20Information%20Management%20Solution%20(WIMS)%20%20Accurate%20information%20%20%20informed%20decisions%20(2)-GUID058a2f9b2202478c923e0d2446788c76.pdf](https://www.opssys.com/InstantKB/attachments/Water%20Information%20Management%20Solution%20\(WIMS\)%20%20Accurate%20information%20%20%20informed%20decisions%20\(2\)-GUID058a2f9b2202478c923e0d2446788c76.pdf)  
26. How to Document Tribal Knowledge Before Expert Employees Retire \- Viewpointsystem, accessed April 29, 2026, [https://viewpointsystem.com/en/documenting-tribal-knowledge/](https://viewpointsystem.com/en/documenting-tribal-knowledge/)  
27. What is Tribal Knowledge and How Do You Capture It? \- Augmentir, accessed April 29, 2026, [https://www.augmentir.com/glossary/what-is-tribal-knowledge](https://www.augmentir.com/glossary/what-is-tribal-knowledge)  
28. Capturing Tribal Knowledge Before Your Best Technicians Retire | Dovient Learning, accessed April 29, 2026, [https://dovient.com/learning/capturing-tribal-knowledge](https://dovient.com/learning/capturing-tribal-knowledge)  
29. Tribal Knowledge Capture Software \- SOPX, accessed April 29, 2026, [https://sopx.io/use-cases/tribal-knowledge-capture/](https://sopx.io/use-cases/tribal-knowledge-capture/)  
30. Digital Work Instruction Software for Manufacturing | Dozuki, accessed April 29, 2026, [https://www.dozuki.com/digital-work-instructions-dozuki-knowledge-management](https://www.dozuki.com/digital-work-instructions-dozuki-knowledge-management)  
31. Shutdown Plans Workflow for Water Treatment Pump Teams \- Oxmaint, accessed April 29, 2026, [https://oxmaint.com/industries/government/shutdown-plans-water-treatment-pump-workflow](https://oxmaint.com/industries/government/shutdown-plans-water-treatment-pump-workflow)  
32. Turn Power and Utilities Talent Gaps into Opportunities \- Moss Adams, accessed April 29, 2026, [https://www.mossadams.com/articles/2025/08/labor-opportunities-in-power-and-utilities](https://www.mossadams.com/articles/2025/08/labor-opportunities-in-power-and-utilities)  
33. Jar Testing Made Easy \- California State Water Resources Control Board, accessed April 29, 2026, [https://www.waterboards.ca.gov/drinking\_water/programs/districts/docs/mendocino/jar\_testing\_made\_easy\_aug7\_2020.pdf](https://www.waterboards.ca.gov/drinking_water/programs/districts/docs/mendocino/jar_testing_made_easy_aug7_2020.pdf)  
34. Prediction of the optimal dosage of coagulants in water treatment plants through developing models based on artificial neural network fuzzy inference system (ANFIS) \- PMC, accessed April 29, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC8617213/](https://pmc.ncbi.nlm.nih.gov/articles/PMC8617213/)  
35. The Overuse of Chemicals in Water Treatment Facilities \- Kraken Sense, accessed April 29, 2026, [https://krakensense.com/blog/the-overuse-of-chemicals-in-water-treatment-facilities](https://krakensense.com/blog/the-overuse-of-chemicals-in-water-treatment-facilities)  
36. Jar Testing for Wastewater Process Optimization \- Environmental Finance Center Network, accessed April 29, 2026, [https://efcnetwork.org/jar-testing-for-wastewater-process-optimization/](https://efcnetwork.org/jar-testing-for-wastewater-process-optimization/)  
37. Jar Testing of Chemical Dosages \- Michigan.gov, accessed April 29, 2026, [https://www.michigan.gov/-/media/Project/Websites/egle/Documents/Programs/WRD/Operator-Certification/jar-testing.ppt?rev=39854e2e0a264ba99fc812b1e98c01ad](https://www.michigan.gov/-/media/Project/Websites/egle/Documents/Programs/WRD/Operator-Certification/jar-testing.ppt?rev=39854e2e0a264ba99fc812b1e98c01ad)  
38. Class Outline \- Oregon.gov, accessed April 29, 2026, [https://www.oregon.gov/oha/PH/HEALTHYENVIRONMENTS/DRINKINGWATER/OPERATIONS/TREATMENT/Documents/swcf/CFDF-3-2024/CFDF-b-6pp.pdf](https://www.oregon.gov/oha/PH/HEALTHYENVIRONMENTS/DRINKINGWATER/OPERATIONS/TREATMENT/Documents/swcf/CFDF-3-2024/CFDF-b-6pp.pdf)  
39. water treatment manuals \- EPA, accessed April 29, 2026, [https://www.epa.ie/publications/compliance--enforcement/drinking-water/advice--guidance/EPA\_water\_treatment\_mgt\_coag\_flocc\_clar2.pdf](https://www.epa.ie/publications/compliance--enforcement/drinking-water/advice--guidance/EPA_water_treatment_mgt_coag_flocc_clar2.pdf)  
40. Geosmin and 2-methylisoborneol removal in drinking water ..., accessed April 29, 2026, [https://iwaponline.com/wpt/article/18/1/159/92609/Geosmin-and-2-methylisoborneol-removal-in-drinking](https://iwaponline.com/wpt/article/18/1/159/92609/Geosmin-and-2-methylisoborneol-removal-in-drinking)  
41. THESIS MEASURING AND MODELING GEOSMIN REMOVAL FROM HORSETOOTH RESERVOIR WATER BY POWDERED ACTIVATED CARBON FOR SELECTED CONTACT \- Mountain Scholar, accessed April 29, 2026, [https://mountainscholar.org/bitstreams/5a64307f-4f48-4f62-a527-943263201819/download](https://mountainscholar.org/bitstreams/5a64307f-4f48-4f62-a527-943263201819/download)  
42. Water Quality Analysis & Monitoring | FlowCam \- Fluid Imaging Technologies, accessed April 29, 2026, [https://www.fluidimaging.com/applications/aquatic/water-quality-monitoring](https://www.fluidimaging.com/applications/aquatic/water-quality-monitoring)  
43. FlowCam Improves Water Quality Monitoring & Early Algal Bloom Detection, accessed April 29, 2026, [https://www.fluidimaging.com/blog/water-quality-monitoring-detect-harmful-algal-blooms](https://www.fluidimaging.com/blog/water-quality-monitoring-detect-harmful-algal-blooms)  
44. Estimating Operational Costs of Activated Carbon for Water Treatment Plants by Predicting the Rise of Harmful Algal Blooms Under Climate Change in Korea Using Machine Learning \- PMC, accessed April 29, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC12976194/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12976194/)  
45. Water Taste & Odor \- Alliance, OH, accessed April 29, 2026, [https://www.cityofalliance.com/CivicAlerts.asp?AID=17\&ARC=28](https://www.cityofalliance.com/CivicAlerts.asp?AID=17&ARC=28)  
46. Technology Advances Help Track and Predict Harmful Algal Blooms (Video) \- NCCOS, accessed April 29, 2026, [https://coastalscience.noaa.gov/news/technology-advances-help-track-and-predict-harmful-algal-blooms/](https://coastalscience.noaa.gov/news/technology-advances-help-track-and-predict-harmful-algal-blooms/)  
47. Sensors for algae risk in water bodies \- Global Infrastructure Hub, accessed April 29, 2026, [https://www.gihub.org/infrastructure-technology-use-cases/case-studies/sensors-for-algae-risk-in-water-bodies/](https://www.gihub.org/infrastructure-technology-use-cases/case-studies/sensors-for-algae-risk-in-water-bodies/)  
48. Sec. B.1.1 Performance Based Evaluation for the Removal of MIB and Geosmin \- Fairfax Water, accessed April 29, 2026, [https://www.fairfaxwater.org/sites/default/files/solicitations/Attachment%203%20Simpson%20Macleod%20Test%20Method.pdf](https://www.fairfaxwater.org/sites/default/files/solicitations/Attachment%203%20Simpson%20Macleod%20Test%20Method.pdf)  
49. Disinfection By-Products Study for New York City Water System \- Hazen and Sawyer, accessed April 29, 2026, [https://www.hazenandsawyer.com/projects/dbp-for-nyc](https://www.hazenandsawyer.com/projects/dbp-for-nyc)  
50. Stage 1 and Stage 2 Disinfectants and Disinfection Byproducts Rules | US EPA, accessed April 29, 2026, [https://www.epa.gov/dwreginfo/stage-1-and-stage-2-disinfectants-and-disinfection-byproducts-rules](https://www.epa.gov/dwreginfo/stage-1-and-stage-2-disinfectants-and-disinfection-byproducts-rules)  
51. Stage 2 Disinfectants and Disinfection Byproducts Rule \- Illinois EPA, accessed April 29, 2026, [https://epa.illinois.gov/content/dam/soi/en/web/epa/documents/compliance-enforcement/drinking-water/sample-collectors-handbook/ch-10-dbps.pdf](https://epa.illinois.gov/content/dam/soi/en/web/epa/documents/compliance-enforcement/drinking-water/sample-collectors-handbook/ch-10-dbps.pdf)  
52. Report of the Microbial and Disinfection Byproducts Rule Revisions Working Group | EPA, accessed April 29, 2026, [https://www.epa.gov/system/files/documents/2023-11/report-of-the-mdbp-rule-revisions-working-group-to-the-ndwac-november-2023\_0.pdf](https://www.epa.gov/system/files/documents/2023-11/report-of-the-mdbp-rule-revisions-working-group-to-the-ndwac-november-2023_0.pdf)  
53. Innovative Approaches for Minimizing Disinfection Byproducts ..., accessed April 29, 2026, [https://www.mdpi.com/2076-3417/14/18/8153](https://www.mdpi.com/2076-3417/14/18/8153)  
54. Comparison of Disinfection By-Product Formation and Distribution during Breakpoint Chlorination and Chlorine-Based Disinfection in Drinking Water \- MDPI, accessed April 29, 2026, [https://www.mdpi.com/2073-4441/14/9/1372](https://www.mdpi.com/2073-4441/14/9/1372)  
55. Predictive models for the formation of emerging disinfection by-products \- RSC Publishing, accessed April 29, 2026, [https://pubs.rsc.org/en/content/articlehtml/2026/ew/d5ew01176k](https://pubs.rsc.org/en/content/articlehtml/2026/ew/d5ew01176k)  
56. Disinfection Profiling and Benchmarking: Technical Guidance \- EPA, accessed April 29, 2026, [https://www.epa.gov/sites/default/files/2020-06/documents/disprof\_bench\_3rules\_final\_508.pdf](https://www.epa.gov/sites/default/files/2020-06/documents/disprof_bench_3rules_final_508.pdf)  
57. What Hydraulics Softwares is everyone using? : r/civilengineering \- Reddit, accessed April 29, 2026, [https://www.reddit.com/r/civilengineering/comments/1mih0wf/what\_hydraulics\_softwares\_is\_everyone\_using/](https://www.reddit.com/r/civilengineering/comments/1mih0wf/what_hydraulics_softwares_is_everyone_using/)  
58. What is WaterGEMS? Competitors, Complementary Techs & Usage \- Sumble, accessed April 29, 2026, [https://sumble.com/tech/watergems](https://sumble.com/tech/watergems)  
59. Potable water distribution systems : r/civilengineering \- Reddit, accessed April 29, 2026, [https://www.reddit.com/r/civilengineering/comments/qvbw8b/potable\_water\_distribution\_systems/](https://www.reddit.com/r/civilengineering/comments/qvbw8b/potable_water_distribution_systems/)  
60. A review of nonrevenue water assessment software tools \- PMC, accessed April 29, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC7074021/](https://pmc.ncbi.nlm.nih.gov/articles/PMC7074021/)  
61. Tackling The Trillion-Gallon Problem Water Loss Reduction Initiatives Benefit Utilities And Consumers Alike, accessed April 29, 2026, [https://www.wateronline.com/doc/tackling-the-trillion-gallon-problem-water-loss-reduction-initiatives-benefit-utilities-and-consumers-alike-0001](https://www.wateronline.com/doc/tackling-the-trillion-gallon-problem-water-loss-reduction-initiatives-benefit-utilities-and-consumers-alike-0001)  
62. Water Losses Cost U.S. Utilities US$6.4 Billion Annually \- Bluefield Research, accessed April 29, 2026, [https://www.bluefieldresearch.com/ns/water-losses-cost-u-s-utilities-us6-4-billion-annually/](https://www.bluefieldresearch.com/ns/water-losses-cost-u-s-utilities-us6-4-billion-annually/)  
63. Report \- Shorewood, WI, accessed April 29, 2026, [https://www.villageofshorewood.org/DocumentCenter/View/5579](https://www.villageofshorewood.org/DocumentCenter/View/5579)  
64. Tackling the Trillion-Gallon Problem: Water Loss Reduction Initiatives Benefit Utilities and Consumers Alike \- Bluefield Research, accessed April 29, 2026, [https://www.bluefieldresearch.com/tackling-the-trillion-gallon-problem-water-loss-reduction-initiatives-benefit-utilities-and-consumers-alike/](https://www.bluefieldresearch.com/tackling-the-trillion-gallon-problem-water-loss-reduction-initiatives-benefit-utilities-and-consumers-alike/)  
65. Cost-Effective Tools for Reducing Non-Revenue Water Loss (Leak Detection, Condition Assessment, and Pressure Management), accessed April 29, 2026, [https://muellerwaterproducts.com/news/cost-effective-tools-reducing-non-revenue-water-loss-leak-detection-condition-assessment-and](https://muellerwaterproducts.com/news/cost-effective-tools-reducing-non-revenue-water-loss-leak-detection-condition-assessment-and)  
66. Evaluating Acoustic vs. AI-Based Satellite Leak Detection in Aging US Water Infrastructure: A Cost and Energy Savings Analysis \- MDPI, accessed April 29, 2026, [https://www.mdpi.com/2624-6511/8/4/122](https://www.mdpi.com/2624-6511/8/4/122)  
67. New Filter Optimization Guidance Article in AWWA Opflow \- Hazen and Sawyer, accessed April 29, 2026, [https://www.hazenandsawyer.com/news/new-filter-optimization-guidance-article-in-awwa-opflow](https://www.hazenandsawyer.com/news/new-filter-optimization-guidance-article-in-awwa-opflow)  
68. Filter Backwashing \- Oregon.gov, accessed April 29, 2026, [https://www.oregon.gov/oha/PH/HEALTHYENVIRONMENTS/DRINKINGWATER/OPERATIONS/TREATMENT/Documents/Backwash.pdf](https://www.oregon.gov/oha/PH/HEALTHYENVIRONMENTS/DRINKINGWATER/OPERATIONS/TREATMENT/Documents/Backwash.pdf)  
69. Using turbidity sensors to optimize filter backwashing | Drinking water \- YSI, accessed April 29, 2026, [https://www.ysi.com/ysi-blog/water-blogged-blog/2025/04/using-turbidity-sensors-to-optimize-filter-backwashing-drinking-water](https://www.ysi.com/ysi-blog/water-blogged-blog/2025/04/using-turbidity-sensors-to-optimize-filter-backwashing-drinking-water)  
70. Optimizing Filter Performance in Drinking Water Treatment \- Badger Meter, accessed April 29, 2026, [https://www.badgermeter.com/blog/optimizing-filter-performance/](https://www.badgermeter.com/blog/optimizing-filter-performance/)  
71. Optimizing Backwash and Filter to Waste for Rapid Rate Filtration \- Washington State Department of Health, accessed April 29, 2026, [https://doh.wa.gov/sites/default/files/2022-02/331-624.pdf](https://doh.wa.gov/sites/default/files/2022-02/331-624.pdf)  
72. Claros Solutions for Regulatory Compliance \- Hach, accessed April 29, 2026, [https://www.hach.com/digital-solutions/claros/industry-challenges/regulatory-compliance](https://www.hach.com/digital-solutions/claros/industry-challenges/regulatory-compliance)  
73. Scenarios to Fund your Capital Improvement Plan \- Environmental Finance Center Network, accessed April 29, 2026, [https://efcnetwork.org/tools-publications/user-friendly-capital-improvement-plan-cip-tool-for-water-wastewater-utilities/](https://efcnetwork.org/tools-publications/user-friendly-capital-improvement-plan-cip-tool-for-water-wastewater-utilities/)  
74. Capital Improvement Plans (CIPs) Made Easier \- Moore Engineering, Inc., accessed April 29, 2026, [https://www.mooreengineeringinc.com/capital-improvement-plans-cips-made-easy/](https://www.mooreengineeringinc.com/capital-improvement-plans-cips-made-easy/)  
75. Capital Improvement Plan Software CIP | Plan It, accessed April 29, 2026, [https://www.cipsoftware.com/](https://www.cipsoftware.com/)  
76. Enabling Better Project Outcomes: Six Tips for Faster, More Accurate Cost Estimates \- AspenTech, accessed April 29, 2026, [https://www.aspentech.com/-/media/aspentech/home/resources/white-papers/pdfs/fy17/q4/11-8229-wp-enabling-better-project-outcomes.pdf?sc\_lang=en](https://www.aspentech.com/-/media/aspentech/home/resources/white-papers/pdfs/fy17/q4/11-8229-wp-enabling-better-project-outcomes.pdf?sc_lang=en)  
77. Improving Early-Stage Cost Estimates for Utility Projects \- Exponent, accessed April 29, 2026, [https://www.exponent.com/article/improving-early-stage-cost-estimates-utility-projects](https://www.exponent.com/article/improving-early-stage-cost-estimates-utility-projects)  
78. InfoWater Pro vs. OpenFlows WaterGEMS Comparison \- SourceForge, accessed April 29, 2026, [https://sourceforge.net/software/compare/InfoWater-vs-OpenFlows-WaterGEMS/](https://sourceforge.net/software/compare/InfoWater-vs-OpenFlows-WaterGEMS/)  
79. Estimating Regionalized Planning Costs of Green Infrastructure and Low-Impact Development Stormwater Management Practices \- PMC, accessed April 29, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC7898140/](https://pmc.ncbi.nlm.nih.gov/articles/PMC7898140/)  
80. Reimagining the CCR: A Simple Way to Build Trust in Our Water ..., accessed April 29, 2026, [https://uswateralliance.org/reimagining-the-ccr-a-simple-way-to-build-trust-in-our-water/](https://uswateralliance.org/reimagining-the-ccr-a-simple-way-to-build-trust-in-our-water/)  
81. Consumer Confidence Report (CCR) | Pure Water Matters \- Your Essential Guide to Drinking Water Quality\! \- UC Agriculture and Natural Resources, accessed April 29, 2026, [https://ucanr.edu/blog/pure-water-matters-your-essential-guide-drinking-water-quality/article/consumer-confidence](https://ucanr.edu/blog/pure-water-matters-your-essential-guide-drinking-water-quality/article/consumer-confidence)  
82. Key Considerations for Water Utilities Selecting Environmental Compliance Software, accessed April 29, 2026, [https://www.locustec.com/key-considerations-water-utilities-environmental-compliance-software/](https://www.locustec.com/key-considerations-water-utilities-environmental-compliance-software/)  
83. Consumer Confidence Reports (CCRs) \- California State Water Resources Control Board, accessed April 29, 2026, [https://www.waterboards.ca.gov/drinking\_water/certlic/drinkingwater/CCR.html](https://www.waterboards.ca.gov/drinking_water/certlic/drinkingwater/CCR.html)  
84. A Guide to Utility Cybersecurity \- Oracle, accessed April 29, 2026, [https://www.oracle.com/utilities/customer-experience/utility-cybersecurity/](https://www.oracle.com/utilities/customer-experience/utility-cybersecurity/)  
85. Cybersecurity in the Water Sector, accessed April 29, 2026, [https://cdn.ymaws.com/www.tawwa.org/resource/resmgr/CYBER/Cyber\_Security\_Presentation.pdf](https://cdn.ymaws.com/www.tawwa.org/resource/resmgr/CYBER/Cyber_Security_Presentation.pdf)  
86. AWWA Cybersecurity Assessment Tool \- American Water Works Association, accessed April 29, 2026, [https://cybersecurity.awwa.org/](https://cybersecurity.awwa.org/)  
87. Water Utilities: Congress Temporarily Extends Cyber Laws, EPA Releases New Guidance, accessed April 29, 2026, [https://www.nossaman.com/newsroom-insights-water-utilities-congress-temporarily-extends-cyber-laws-epa-releases-new-guidance](https://www.nossaman.com/newsroom-insights-water-utilities-congress-temporarily-extends-cyber-laws-epa-releases-new-guidance)  
88. Water Sector Cybersecurity Risk Management Guidance Version 4.0, accessed April 29, 2026, [https://dem.ri.gov/sites/g/files/xkgbur861/files/2025-10/Water-Sector-Cybersecurity-Risk-Managmenet-Guidance-V4.0.pdf](https://dem.ri.gov/sites/g/files/xkgbur861/files/2025-10/Water-Sector-Cybersecurity-Risk-Managmenet-Guidance-V4.0.pdf)  
89. Toolbox \- American Water Works Association, accessed April 29, 2026, [https://www.awwa.org/toolbox/](https://www.awwa.org/toolbox/)  
90. Modernizing Cybersecurity in Utilities: How AI, Compliance, and Zero Trust are Reshaping Risk Management \- Capco, accessed April 29, 2026, [https://www.capco.com/intelligence/capco-intelligence/modernizing-cybersecurity-in-utilities](https://www.capco.com/intelligence/capco-intelligence/modernizing-cybersecurity-in-utilities)  
91. Water Utility's Success Story with Dragos OT Cybersecurity Platform, accessed April 29, 2026, [https://dragos.brightspotcdn.com/fc/23/99d8f31e477d8d02733a8d6497a0/water-utility-success-dragos-platform-case-study-04-24.pdf](https://dragos.brightspotcdn.com/fc/23/99d8f31e477d8d02733a8d6497a0/water-utility-success-dragos-platform-case-study-04-24.pdf)  
92. Poor Cybersecurity Makes Water a Weak Link in Critical Infrastructure \- FDD, accessed April 29, 2026, [https://www.fdd.org/analysis/2021/11/18/poor-cybersecurity-makes-water-a-weak-link-in-critical-infrastructure/](https://www.fdd.org/analysis/2021/11/18/poor-cybersecurity-makes-water-a-weak-link-in-critical-infrastructure/)  
93. Water Utilities & Cybersecurity | South Carolina Department of Environmental Services, accessed April 29, 2026, [https://des.sc.gov/programs/bureau-water/water-utilities-cybersecurity](https://des.sc.gov/programs/bureau-water/water-utilities-cybersecurity)  
94. 7 Cost-Effective Cybersecurity Strategies for Water Systems \- VC3, accessed April 29, 2026, [https://www.vc3.com/guide/cybersecurity-strategies-water-systems](https://www.vc3.com/guide/cybersecurity-strategies-water-systems)  
95. The Cybersecurity State of the Water Sector \- U.S. Senate Committee on Environment and Public Works, accessed April 29, 2026, [https://www.epw.senate.gov/public/\_cache/files/5/3/53d93dfe-ed8c-4e48-b705-0b16cb92c90a/FA38A32EE48D7F3D4B0C069FDC08A69E6327376EB85838A03310B2E91C8582C1.02-04-2026-dr.-simonton-testimony.pdf](https://www.epw.senate.gov/public/_cache/files/5/3/53d93dfe-ed8c-4e48-b705-0b16cb92c90a/FA38A32EE48D7F3D4B0C069FDC08A69E6327376EB85838A03310B2E91C8582C1.02-04-2026-dr.-simonton-testimony.pdf)  
96. Strategies For Saving Energy At Public Water Systems (EPA 816-F-13-004), accessed April 29, 2026, [https://www.epa.gov/sites/default/files/2015-04/documents/epa816f13004.pdf](https://www.epa.gov/sites/default/files/2015-04/documents/epa816f13004.pdf)  
97. Energy Management and Scenario Energy Cost Calculations \- Bentley Software Documentation, accessed April 29, 2026, [https://docs.bentley.com/LiveContent/web/Bentley%20WaterGEMS%20SS6-v1/en/GUID-EFB10E18-CB68-493A-9E37-BEB14E65C9F6.html](https://docs.bentley.com/LiveContent/web/Bentley%20WaterGEMS%20SS6-v1/en/GUID-EFB10E18-CB68-493A-9E37-BEB14E65C9F6.html)  
98. Energy saving and management of water pumping networks \- PMC \- NIH, accessed April 29, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC8379678/](https://pmc.ncbi.nlm.nih.gov/articles/PMC8379678/)  
99. EVALUATION OF WATER PUMPING SYSTEMS \- IADB Publications, accessed April 29, 2026, [https://publications.iadb.org/publications/english/document/Evaluation-of-Water-Pumping-Systems-Energy-Efficiency-Assessment-Manual.pdf](https://publications.iadb.org/publications/english/document/Evaluation-of-Water-Pumping-Systems-Energy-Efficiency-Assessment-Manual.pdf)  
100. Step 5\. Leverage Data Management Tools \- Office of Critical Minerals and Energy Innovation, accessed April 29, 2026, [https://eere.energy.gov/energydataguide/step5.shtml](https://eere.energy.gov/energydataguide/step5.shtml)  
101. Conducting a Fire Flow Test | MTAS \- Serving Tennessee City Officials, accessed April 29, 2026, [https://www.mtas.tennessee.edu/reference/conducting-fire-flow-test](https://www.mtas.tennessee.edu/reference/conducting-fire-flow-test)  
102. ISO RATING IMPACT ON INSURANCE PREMIUMS, accessed April 29, 2026, [https://msfes.net/unionvfd/wp-content/uploads/2022/05/ISO-Insurance-Impacts.pdf](https://msfes.net/unionvfd/wp-content/uploads/2022/05/ISO-Insurance-Impacts.pdf)  
103. ISO Rating Information \- Foothills Fire & Rescue, accessed April 29, 2026, [https://www.foothillsfire.org/iso-rating-information](https://www.foothillsfire.org/iso-rating-information)  
104. US Fire Administration \- Water Supply Systems and Evaluation Methods \- FEMA, accessed April 29, 2026, [https://www.usfa.fema.gov/downloads/pdf/publications/water\_supply\_systems\_volume\_ii.pdf](https://www.usfa.fema.gov/downloads/pdf/publications/water_supply_systems_volume_ii.pdf)  
105. Adjust for Elevation in Freeman Flow Equation? \- MeyerFire, accessed April 29, 2026, [https://www.meyerfire.com/daily/adjust-for-elevation-in-freeman-flow-equation](https://www.meyerfire.com/daily/adjust-for-elevation-in-freeman-flow-equation)