# Taxonomy

## Purpose

The taxonomy defines the knowledge map for the Potable Dataset. It serves four functions:

- keeps coverage balanced across the full operational domain
- makes examples easier to review and retrieve
- identifies underdeveloped areas
- supports evaluation by topic

The municipal taxonomy has 16 categories. A category earns its place when its failure modes are genuinely distinct from every other category and the operator's reasoning process is meaningfully different.

## Coverage Targets

- 10 to 15 examples per subcategory
- 50 or more examples per major category over time

These are planning targets, not release gates.

---

## Municipal Track Categories

### `water_source_and_reservoir_management`

Raw water quality, watershed events, reservoir operations, turnover, and seasonal source behavior. Covers how changes at the source translate into plant operating implications before water enters the treatment process.

Possible subcategory directions:
- source_water_changes
- storm_impacts
- reservoir_turnover
- algae_and_taste_odor
- watershed_events

### `groundwater`

Well systems, aquifer behavior, GWUDI classification, groundwater chemistry, and the operating differences between groundwater and surface water treatment. Includes pump cycling, yield changes, and geochemical shifts.

Possible subcategory directions:
- well_performance
- aquifer_behavior
- gwudi_operations
- groundwater_chemistry
- pump_and_yield_issues

### `coagulation_flocculation_and_sedimentation`

Coagulant selection and dose adjustment, jar testing, polymer use, mixing energy, floc quality assessment, basin management, sludge blanket control, and solids carryover. Treated as a single process category because coag/floc decisions are inseparable from settling outcomes.

Possible subcategory directions:
- coagulant_dosing
- jar_test_interpretation
- polymer_use
- floc_quality
- clarifier_performance
- sludge_blanket_control
- solids_carryover

### `pH_and_alkalinity`

System-wide pH and alkalinity management spanning coagulation, disinfection, and corrosion control. Treated as a cross-cutting category because pH affects process chemistry in multiple treatment stages simultaneously.

Possible subcategory directions:
- ph_adjustment
- alkalinity_control
- buffering_capacity
- process_interactions

### `filtration`

Filter run management, headloss trends, turbidity response, backwash decisions, filter-to-waste, ripening, breakthrough response, media condition, and membrane systems where applicable.

Possible subcategory directions:
- headloss_trends
- effluent_turbidity_response
- backwash_triggers
- ripening_and_return_to_service
- breakthrough_response
- filter_to_waste

### `disinfection_and_oxidation`

Primary and secondary disinfection, chlorine chemistry, chloramination, UV, ozone, CT concepts and compliance, DBP formation and control, residual management, and disinfectant troubleshooting.

Possible subcategory directions:
- chlorine_residual
- ct_compliance
- chloramination
- disinfectant_troubleshooting
- dbp_control
- chemical_dose_calculation

### `distribution_nitrification_and_corrosion`

Finished water concerns after the plant gate: residual preservation, storage tank management, nitrification in distribution, lead and copper rule compliance, main breaks, pressure management, and cross-team coordination with distribution staff.

Possible subcategory directions:
- residual_management
- storage_tanks
- nitrification_response
- lead_copper_rule
- main_breaks
- pressure_management

### `regulations`

Compliance reasoning, permit-driven operating implications, public notification requirements, violation response, reporting and documentation, and practical interpretation of regulatory language in operating context.

Possible subcategory directions:
- turbidity_compliance
- residual_requirements
- reporting_and_documentation
- public_notification
- regulatory_interpretation
- violation_response

### `operational_procedure_and_process_management`

Routine operating judgment, shift decisions, startup and shutdown logic, chemical changeovers, process prioritization, shift handoff, and the coordination decisions that keep a plant running through transitions.

Possible subcategory directions:
- shift_handoffs
- startup_shutdown
- chemical_changeovers
- operating_priorities
- routine_rounds

### `systems_integration_and_equipment_behavior`

Equipment telemetry interpreted in process context, cascade failures, interactions between treatment stages, and situations where a reading in one part of the plant means something has changed elsewhere. Distinguished from SCADA/controls because the reasoning is about process physics, not software or network state.

Possible subcategory directions:
- cascade_failure_diagnosis
- cross_process_interactions
- equipment_telemetry_interpretation
- vfd_and_motor_behavior
- maintenance_coordination

### `SCADA_and_controls_infrastructure`

PLC failures, network issues, HMI artifacts, alarm management, control loop behavior, and situations where the question is about the control system rather than the physical process. Requires different diagnostic reasoning than process troubleshooting.

Possible subcategory directions:
- plc_and_hmi_issues
- alarm_management
- control_loop_behavior
- network_and_communication
- scada_data_reliability

### `analyzers_and_instrumentation`

Instrument failure modes, calibration drift, cross-checking readings against bench samples, turbidimeter behavior, chlorine analyzer issues, and the judgment of when to trust or distrust a reading.

Possible subcategory directions:
- turbidimeter_issues
- chlorine_analyzer_issues
- calibration_and_drift
- cross_checking_readings
- instrument_selection

### `measurement_reliability_and_field_analysis`

Colorimetric interference, sample handling errors, field testing technique, light and temperature effects on readings, and the reliability of measurements taken outside the lab. Distinct from instrument category because the question is about chemistry and technique, not equipment.

Possible subcategory directions:
- colorimetric_interference
- sample_handling
- field_testing_technique
- temperature_and_light_effects
- bench_vs_field_reconciliation

### `chemical_feed_and_chemical_treatment`

Chemical quality verification, concentration and strength issues, feed system failures, day tank management, feeder calibration, and chemical delivery and storage concerns. Covers the physical and chemical integrity of treatment inputs.

Possible subcategory directions:
- chemical_strength_verification
- feed_system_failures
- day_tank_management
- feeder_calibration
- chemical_delivery_and_storage

### `emergency_response`

Upset conditions, source contamination events, pressure loss, boil water advisories, public notification, major equipment failure, and urgent operational response requiring immediate action or escalation.

Possible subcategory directions:
- source_contamination
- boil_water_advisory
- pressure_loss_response
- major_equipment_failure
- emergency_communications
- escalation_logic

### `external_events_and_non_routine_operations`

Wildfires and smoke, agricultural runoff events, upstream industrial incidents, extreme weather, infrastructure failures outside the plant boundary, and other non-routine conditions that require adapted operations. Distinct from emergency_response because the driver is an external event, not an internal plant failure.

Possible subcategory directions:
- wildfire_impacts
- agricultural_events
- extreme_weather_operations
- upstream_industrial_incidents
- infrastructure_failures

---

## Taxonomy Rules

- Each record gets one primary `category` and one primary `subcategory`.
- Categories are stable. Adding subcategories is expected. Frequent changes to categories are not.
- If a record spans multiple categories, classify by the main operational question being answered.
- Subcategories must be snake_case.
- Subcategories not listed above are allowed — the lists above are directions, not constraints.

---

## Notes on Category Design

**Why coagulation and sedimentation are combined:** Operators make coag/floc decisions with settling outcomes in mind. Separating them creates artificial boundaries around a tightly coupled process.

**Why pH and alkalinity is its own category:** pH affects coagulation efficiency, disinfection byproduct formation, and corrosion control simultaneously. Questions in this space require system-level reasoning that doesn't fit cleanly into any single process category.

**Why SCADA and instrumentation are separate:** SCADA questions are about control system state — PLCs, networks, HMI — and require IT/OT reasoning. Instrumentation questions are about measurement devices and their physical failure modes. Different knowledge domain.

**Why external events is separate from emergency response:** Emergency response is triggered by internal plant conditions. External events require adapted operations but often aren't emergencies in the plant-response sense. The reasoning pattern is different.
