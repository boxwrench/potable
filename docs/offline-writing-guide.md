# Offline Writing Guide — First 50 Entries

Potable Dataset, April 2026. Print this and bring it to the cabin.

---

## What you're writing

50 raw Q&A entries for the Potable fine-tuning dataset. Each entry is one question and one answer. No JSON, no metadata, no formatting. Just operator questions and operator answers in a notebook or text file.

---

## Format

```
Q: [Question as someone would actually ask you at the plant]

A: [Your answer as you'd actually give it to a coworker]
```

Number them 1–50 so you can reference them later.

---

## Voice rules

- You are a senior operator talking to a capable coworker
- Lead with the answer, not background
- Show your diagnostic thinking — sequential, conditional
- Use real units: NTU, mg/L, gpm, MGD, psi, minutes, feet
- Use real terminology: turbidity not cloudiness, headloss not pressure drop
- Say "check X before Y" not "there are several factors"
- Acknowledge uncertainty where it exists — "depends on your source" is honest
- Include safety or compliance notes only when they genuinely matter
- No AI phrasing, no textbook introductions, no filler

---

## What makes an entry good

Ask yourself:

1. Could this answer have come from a Wikipedia article? If yes, rewrite it.
2. Does it show a reasoning chain, not just a conclusion?
3. Would you actually say this to someone on your crew?
4. Is the sequence of checks ordered by what matters most?
5. Does it respect what's conditional vs. what's universal?

---

## Depth targets

**Basic** (3–5 sentences): Single question, direct answer, one or two checks.

**Intermediate** (6–12 sentences): Some complexity, ordered reasoning, conditional branches, maybe a safety note.

**Advanced** (12–20 sentences): Multi-factor diagnosis, interacting causes, tradeoffs, escalation logic, uncertainty acknowledged.

Don't inflate to hit a length. A sharp 4-sentence answer is better than a padded 12-sentence one.

---

## Coverage plan — 50 entries across 16 categories

Write at least one entry per category. Fill the seeds list first (28 topics), then add 22 more in categories where you have the richest memory.

### Water Source (3 entries)
1. Responding to rapid raw water turbidity increase after rain [intermediate]
2. Recognizing and responding to fall reservoir turnover [intermediate]
3. Your choice — seasonal source behavior, algae, watershed event

### Coagulation / Flocculation (4 entries)
4. How to adjust coagulant dose when raw turbidity doubles [basic]
5. Reading jar test results and translating to plant-scale dose [intermediate]
6. Your choice — polymer use, mixing energy, coag chemistry shift
7. Your choice — cold water coagulation, pH/alkalinity interaction

### Sedimentation (3 entries)
8. What settled water turbidity tells you about clarifier performance [basic]
9. Managing sludge blanket depth during high-flow events [intermediate]
10. Your choice — solids carryover, settling diagnostics

### Filtration (4 entries)
11. When to initiate a backwash based on headloss and run time [basic]
12. Managing filter ripening after backwash before returning to service [intermediate]
13. Your choice — filter-to-waste decisions, breakthrough response
14. Your choice — loading rate changes, media issues, underdrain problems

### Disinfection (4 entries)
15. How to verify CT compliance at your plant [intermediate]
16. Troubleshooting unexplained chlorine demand increase [advanced]
17. Your choice — chloramine chemistry, residual management at scale
18. Your choice — breakpoint, seasonal demand patterns, UV considerations

### Corrosion Control (3 entries)
19. Why pH and alkalinity matter for corrosion control [basic]
20. Interpreting Langelier Saturation Index results [intermediate]
21. Your choice — finished water stability, dose adjustment reasoning

### Taste and Odor (2 entries)
22. Operational response to geosmin detection in source water [intermediate]
23. Your choice — customer complaints, treatment adjustments

### Plant Operations (4 entries)
24. What to include in an effective shift handoff [basic]
25. Prioritizing actions during simultaneous process upsets [advanced]
26. Your choice — startup/shutdown, routine rounds
27. Your choice — process coordination, flow management

### Laboratory (3 entries)
28. How to verify a turbidimeter is reading correctly [basic]
29. Running and interpreting a jar test [intermediate]
30. Your choice — bench testing, sampling practice, result interpretation

### Safety (3 entries)
31. Safe procedures for switching out a chlorine cylinder [basic]
32. What makes a space confined and what that means for entry [intermediate]
33. Your choice — chemical handling, PPE decisions, LOTO

### Regulations (2 entries)
34. Understanding the turbidity requirements under the IESWTR [intermediate]
35. Your choice — residual requirements, reporting, regulatory interpretation

### Math and Calculations (4 entries)
36. Calculating detention time from basin volume and flow rate [basic]
37. Calculating chemical feed rate from desired dose and flow [intermediate]
38. Your choice — CT calculation walkthrough
39. Your choice — unit conversion, loading rate, other treatment math

### Equipment and Maintenance (3 entries)
40. Troubleshooting a chlorine analyzer reading erratically [intermediate]
41. Your choice — chemical feed equipment, pump behavior
42. Your choice — maintenance coordination, instrumentation issues

### Distribution (2 entries)
43. Maintaining chlorine residual in a long dead-end main [intermediate]
44. Your choice — storage tanks, field complaints, cross-team coordination

### Troubleshooting (3 entries)
45. How to tell if a turbidity spike is real or an instrument problem [advanced]
46. Your choice — abnormal trend diagnosis, process upset response
47. Your choice — multi-process interaction, escalation logic

### Emergency Response (2 entries)
48. Initial response steps when a contamination event is suspected [advanced]
49. Your choice — storm response, major equipment failure
50. Your choice — emergency communications, anything high-stakes

---

## Session rhythm

- Write in bursts of 4–6 entries, then take a break
- Start each burst from the list above — knock out the named topic, then write the "your choice" entries while you're in that category
- Keep a parking lot on a separate page — when a topic comes to mind mid-entry, jot it down and come back later
- If you're unsure about an entry, mark it with a ? and move on — don't let perfectionism slow the session
- If an entry starts feeling like a textbook answer, stop and ask yourself: "what would I actually say?"

---

## Difficulty mix target

Aim for roughly:

- 15 basic
- 25 intermediate
- 10 advanced

Don't force it. If something naturally comes out advanced, let it. If a topic is genuinely basic, keep it basic.

---

## Kernel sources — where good entries come from

- Things you've explained to a new operator more than once
- Judgment calls you've made under uncertainty
- Times the obvious answer was wrong
- Moments where sequence mattered
- Regulatory pressure meeting operational reality
- Scenarios specific to SFPUC scale that most operators never see

---

## One example to calibrate against

```
Q: Settled water turbidity has been creeping up over the last two
shifts but raw water looks the same. What am I looking at?

A: Most likely your coagulant dose drifted or your coag chemistry
shifted. Check your coagulant feed rate first — if the pump is
pacing off flow and flow changed even slightly, your dose may be
off. If feed rate looks right, pull a raw water sample and check
alkalinity and pH. A drop in alkalinity can wreck your coag
performance even if turbidity hasn't moved. Run a jar test before
you chase it with dose bumps. If the jars confirm your current
dose is wrong, adjust and give it a couple hours to show up in
settled water. If the jars look fine at current dose, then your
problem isn't chemical — look at your flocculator mixing energy
and your clarifier sludge blanket. A rising blanket will push
carryover before you see it in the effluent launder.
```

That's intermediate. Sequential reasoning, conditional branches, specific checks, operator voice. That's the bar.

---

## What to avoid

- "There are several factors to consider"
- "It is important to note"
- "You should always"
- Answers that are all background and no action
- Invented numbers you wouldn't actually say
- Entries that would get the same answer as another entry you already wrote
- Multi-turn entries unless the follow-up truly changes the reasoning

---

## When you get back

Hand off the raw text. We'll:
1. Convert each entry to JSON with proper metadata
2. Assign IDs (wt-0004 through wt-0053)
3. Tag categories, subcategories, difficulty, source_type
4. Run validation
5. Review against the style guide
6. Run eval to see the effect

The structuring is the easy part. The writing is what matters.
