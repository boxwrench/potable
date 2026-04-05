# Taxonomy

## Purpose

The taxonomy defines the knowledge map for the Potable Dataset. It serves four functions:

- keeps coverage balanced
- makes examples easier to review and retrieve
- helps identify underdeveloped areas
- supports evaluation by topic

The top-level municipal taxonomy is fixed. Subcategories will be expanded over time.

## Coverage Targets

General target:

- 10 to 15 examples per subcategory
- 50 or more examples per major category over time

These are planning targets, not release gates.

## Municipal Track Categories

### `water_source`

Raw water source conditions, source changes, watershed-related operating implications, and seasonal source behavior.

Possible subcategory directions:

- source_water_changes
- storm_impacts
- reservoir_turnover
- algae_and_source_quality

### `coagulation_flocculation`

Coagulant selection, dose adjustment, mixing, floc formation, jar-test reasoning, and response to raw water changes.

Possible subcategory directions:

- coagulant_dosing
- polymer_use
- mixing_and_floc_quality
- jar_test_interpretation

### `sedimentation`

Clarifier and basin performance, solids carryover, sludge blanket behavior, detention time issues, and settling performance.

Possible subcategory directions:

- clarifier_performance
- sludge_blanket_control
- solids_carryover
- settling_diagnostics

### `filtration`

Filter loading, headloss, turbidity, ripening, backwash decisions, filter-to-waste, and breakthrough response.

Possible subcategory directions:

- headloss_trends
- breakthrough_response
- backwash_triggers
- ripening_and_return_to_service

### `disinfection`

Primary and secondary disinfection, chlorine chemistry, residual management, CT concepts, and disinfection troubleshooting.

Possible subcategory directions:

- chlorine_residual
- ct_compliance
- dose_and_contact_time
- disinfectant_troubleshooting

### `corrosion_control`

pH, alkalinity, stability, corrosion indicators, treatment goals, and practical operating adjustments related to finished water stability.

Possible subcategory directions:

- ph_and_alkalinity_control
- finished_water_stability
- corrosion_indicators
- dose_adjustment_reasoning

### `taste_and_odor`

Taste and odor events, likely causes, operational response, source-water links, and treatment options.

Possible subcategory directions:

- geosmin_mib_response
- customer_complaints
- source_related_odor_events
- treatment_adjustments

### `plant_operations`

Routine operating judgment, shift decisions, process coordination, rounds, startup and shutdown logic, and process prioritization.

Possible subcategory directions:

- shift_handoffs
- startup_shutdown
- operating_priorities
- routine_rounds

### `laboratory`

Bench testing, sampling practice, instrument verification, result interpretation, and common lab-process feedback loops.

Possible subcategory directions:

- sampling_practice
- instrument_checks
- bench_testing
- result_interpretation

### `safety`

Chemical safety, confined space awareness, lockout-tagout context, PPE judgment, and operational safety decision-making.

Possible subcategory directions:

- chemical_handling
- ppe_selection
- confined_space_awareness
- loto_context

### `regulations`

Regulatory concepts, permit-driven operating implications, reporting context, and practical compliance interpretation.

Possible subcategory directions:

- turbidity_compliance
- residual_requirements
- reporting_and_documentation
- regulatory_interpretation

### `math_and_calculations`

Dose calculations, flow-based calculations, unit conversions, detention time, loading rates, and treatment math walkthroughs.

Possible subcategory directions:

- chemical_dose_calculations
- flow_and_volume
- detention_time
- unit_conversions

### `equipment_and_maintenance`

Pumps, valves, analyzers, feeders, motors, instrumentation, and the operating implications of equipment issues.

Possible subcategory directions:

- analyzer_issues
- chemical_feed_equipment
- pump_and_valve_behavior
- maintenance_coordination

### `distribution`

Finished water concerns after the plant, residual preservation, storage, field complaints, and coordination with distribution staff.

Possible subcategory directions:

- residual_management
- storage_tanks
- field_complaints
- cross_team_coordination

### `troubleshooting`

Multi-step diagnosis across processes, signals, symptoms, likely causes, and next checks.

Possible subcategory directions:

- abnormal_trend_diagnosis
- instrument_vs_process_fault
- process_upset_response
- escalation_logic

### `emergency_response`

Upset conditions, contamination concerns, severe weather, major equipment failure, and urgent operational response.

Possible subcategory directions:

- storm_response
- contamination_suspicions
- major_equipment_failure
- emergency_communications

## Developing Regions Track Categories

The developing regions taxonomy is separate and should not be merged casually with the municipal one.

Current top-level categories:

- handpumps_and_boreholes
- spring_and_well_protection
- small_piped_systems
- solar_pumping
- household_treatment
- point_of_use_chlorination
- rainwater_harvesting
- water_quality_field_testing
- sanitation_basics
- hygiene_promotion
- seasonal_operations
- emergency_response
- supply_chain_and_maintenance
- community_governance
- disease_and_health
- math_and_calculations

## Taxonomy Rules

- Each record gets one primary `category`.
- Each record gets one primary `subcategory`.
- Categories should be stable over time.
- Subcategories should be specific enough to support coverage tracking.
- If a record seems to span multiple categories, classify it by the main operational question being answered.

## Notes

The taxonomy should evolve slowly. Adding subcategories is expected. Frequent changes to top-level categories are not.
