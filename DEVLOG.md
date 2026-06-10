# Dev Log

## 2026-05-18 (later)

Starter cards were silently sabotaging the PotableLM persona. Trimmed them and noted the underlying portability problem.

- **What was wrong:** the "Build a Tool" and "Write a SOP" cards in `session-surface.tsx` were each dumping ~60 lines of intake-form prompt into the composer ("Step 1 — present the intake template below exactly as written..."). That prompt overrode `AGENTS.md`'s rewritten doctrine ("skip the intake form, use the profile, build in ~3 short messages"). End result: clicking a card looked indistinguishable from copy-pasting a template into a browser AI — none of the persona's value came through.
- **Fix:** card prompts are now terse triggers. Build a Tool → `"Help me build a plant tool."`; Write a SOP → `"Help me write an SOP."`. AGENTS.md (offer-menu → ONE question → build → confirm) runs unopposed.
- **Underlying issue — persona portability:** the PotableLM persona, plant profile, and tool catalog live in `~/.config/opencode/AGENTS.md` + `plant-profile.md` (loaded via `opencode.json` `instructions`). That's *user-global*, not app-bundled. Consequences:
  - On a fresh machine without the config restore, the cards become very thin triggers and the AI behaves like a generic assistant. The `config-snapshot/` README is the restore path for now.
  - Opening the `potable_work` source repo itself as a workspace double-loads the global AGENTS.md *and* the repo's dev-guide AGENTS.md — voice and rules conflict. Don't open it as an operator workspace.
  - If the user switches to a model that handles system prompts loosely, the doctrine softens. Haiku 4.5 has held it well in testing.
- **Followup options when ready to ship beyond this machine** (not done now): (a) bundle the persona + tool catalog as a workspace blueprint so any new workspace gets it without touching `~/.config/opencode/`; (b) inject it as an app-level system prompt in `apps/app/src/app/constants.ts` so it loads even with no AGENTS.md present; (c) ship a "first-run" copy of the three config files into `~/.config/opencode/` on install. (a) is the lightest, (b) is the most defensive, (c) plays nicest with users who already use opencode for other things.

## 2026-05-18

PotableLM persona, plant profile, and HTML tool auto-preview wired end-to-end. The app now opens with the operator's facility context already loaded and produces tools that pop straight into the browser.

- **Global system prompt — PotableLM persona:** `C:\Users\wests\.config\opencode\AGENTS.md` holds the operator-voice persona, answer-structure rules, conventions (no commercial brands, no em dashes, units mandatory), safety doctrine (supervisor verification for dosing / public health calls), and what PotableLM is not (not a substitute for a licensed operator, SOPs, primacy agency). opencode auto-loads global AGENTS.md into every session, every workspace, every model. Caveat: opening the `potable_work` source repo itself as a workspace double-loads with its repo AGENTS.md (OpenWork dev guide) — don't.
- **Plant profile auto-load:** `C:\Users\wests\.config\opencode\plant-profile.md` is the operator's facility reference (currently a 160 MGD CA conventional plant: 5 sed basins, 12 dual-media filters at 2,000 sf each, 0.7 MG clearwell + 2× 1.2 MG serpentine CT, chloraminated finished at 3.3 mg/L total Cl2, pH 8.9). Loaded into every session via `C:\Users\wests\.config\opencode\opencode.json` with `instructions: ["...plant-profile.md"]`.
- **Why not "ask first, then read at runtime":** tried that first. opencode's read tool aborted on a path outside the workspace, so the AI fell back to manually quizzing the operator. `instructions` auto-load is reliable and removes permission friction. AGENTS.md still teaches the AI to treat `(default, confirm)` entries as soft-assumed and `[TBD]` as real gaps to flag (never invent).
- **AGENTS.md tool-building doctrine:** skip the intake-form ritual. Skip the "review before I code" pause for compact tools. Profile values are built-in defaults, never user questions. Only expose real-time-variable inputs in tools (current flow, current headloss, current measurement) — static plant config stays baked in. HTML artifacts go to `tools/<name>.html`; SOPs go to `docs/<name>.md`.
- **HTML tool auto-preview watcher:** `electron/main.mjs` `setupToolsWatcher()` watches `<workspace>/tools/*.html`. On a new or overwritten file, `shell.openExternal('file:///...')` pops it open in the operator's default browser. Per-file 30 s debounce so AI iteration doesn't focus-steal. Registered on boot and on every workspace activation IPC. Reason: chat surface has no inline HTML rendering, and adding one means touching the markdown renderer we just stabilized. External-browser pop is the lowest-risk preview and matches the basin-sim launch pattern operators already know. Change is live for `demo-launch.ps1` (loads main.mjs from source); the packaged win-unpacked exe needs `pnpm package:electron:dir` to rebuild `app.asar` before it picks up.
- **AI streaming response — final fix:** earlier polling-gate workaround was scrapped. The real bug was `handleSend` in `session-surface.tsx` calling `setSending(false)` right after `onSendDraft` resolved — but that promise resolves on prompt-accept, not response-complete, so polling died before responses arrived. Fix: leave `sending` true after send and let the existing `liveStatus → idle` effect clear it. Added `snapshot` to that effect's deps so fast responses (busy window between polls) are also caught. Composer focus during AI streaming remains a known acceptable cost; structural / `React.memo` refactor deferred.
- **Tool catalog + design standards baked into AGENTS.md:** the global PotableLM prompt now carries the full operator-tool design spec (one-screen layout, fixed units with hidden conversion, Advanced toggle, traffic-light Pass/Fail at top, single Calculate, self-contained inline HTML, print stylesheet) and an 11-tool catalog (CT compliance / coagulant dose / lime-soda-ash & LSI/RSI/CCPP / chlorine demand-breakpoint / chlorine-chloramine dose / fluoride feed / filter loading-UFRV-backwash / basin detention-T10 / distribution decay-water age / Pb-Cu 90th percentile / daily MOR). Each catalog entry lists real-time inputs (exposed) vs profile-baked defaults (never asked). Operator-facing flow tightened to: offer menu if no tool named → ONE question ("use plant profile defaults? y/n") → build → one-line confirmation. No intake forms, no review-before-code pauses for compact tools. The big spec is internal to the AI; operator sees ~3 short messages start-to-artifact.

## 2026-05-14

Fixed `potable_work` chat UI not showing AI responses until a manual refresh. Most of the debugging time was wasted on a stale bundle — read this before touching it again.

- **Real time-sink — stale bundle:** Electron was loading a pre-built `dist/` bundle, not the Vite dev server, so every code change appeared to "do nothing." Spot it in DevTools → Network: a hashed JS file like `index-CsJB8kwj.js` + `file:///` `index.html` = stale build; raw `.tsx` source files + `@react-refresh` + `index.html` from `http://localhost:5173/` = dev server (correct).
- **Correct startup order:** start Vite *first* (`potable_work/apps/app`: set `$env:OPENWORK_DEV_MODE = "1"` then `pnpm dev:windows` — plain `pnpm dev` uses Unix env-var syntax and fails on Windows), wait for `Local: http://localhost:5173/`, *then* run `demo-launch.ps1`. If Vite isn't up when Electron starts, Electron silently falls back to the built bundle.
- **Actual bug:** opencode's SSE event stream is unreliable here (goes quiet after initial events; known upstream issue), so live UI updates never arrive. Fixes work around it via snapshot polling.
- Fix 1 — `session-render-state.ts`: removed the `messageListContainsAll` shortcut in `deriveRenderedSessionMessages` that preferred empty live SSE stubs over real snapshot text. Now always merges.
- Fix 2 — `session-surface.tsx`: `sseStuck` check (trust polled snapshot status when SSE is stuck on "busy") + 1s `setInterval` polling of `snapshotQuery.refetch()` (React Query's `refetchInterval` doesn't fire reliably in Electron).
- Dead ends removed, do not re-add: `refetchInterval`/`refetchIntervalInBackground`, `structuralSharing: false`/`gcTime: 0`/`notifyOnChangeProps: "all"`, a `renderTick` re-render counter (made the composer stutter), and a `_t=Date.now()` URL cache-buster (never the problem). Also deleted now-dead `hydratedKeyRef` and a duplicate `seedSessionState` effect.
- Lesson: before debugging "my change had no effect," confirm the running app is actually loading your code.
- **Permanent fix (later same day):** `electron/main.mjs` now defaults `startUrl` to `http://localhost:5173` whenever `OPENWORK_DEV_MODE=1` and not packaged — previously it only used the dev server if `OPENWORK_ELECTRON_START_URL` was explicitly set (only `demo-launch.ps1` did that). Launching Electron any other way fell back to the stale `app/dist` build. Now dev mode can't load the stale bundle; if Vite isn't up it fails loudly instead. Still: start Vite before Electron.
- **Use mode vs dev mode (final setup):** `demo-launch.ps1` no longer sets `OPENWORK_DEV_MODE` — it loads the prebuilt `apps/app/dist` bundle via `loadFile`, no dev server needed, seamless for normal use. After changing UI code, rebuild that bundle: from `apps/app`, `OPENWORK_ELECTRON_BUILD=1 pnpm build` (the env var sets Vite `base: "./"` for relative asset paths — `loadFile` uses `file://`, so absolute `/assets/...` paths white-screen). Plain `pnpm build:ui` from root omits that env var — don't use it for the demo-launch bundle. For active development: run the Vite dev server + `OPENWORK_DEV_MODE=1` (hot reload).

## 2026-04-13

Restructured the municipal taxonomy to 16 domain-organized categories. Updated all toolchain scripts, reference documents, and existing records to match.

- Replaced the previous 16-category flat taxonomy with a new set organized by cognitive task and failure mode independence. Full rationale in TAXONOMY.md.
- Rewrote `validate.py`: checks required metadata fields, validates category against the 16 new values, enforces system/user/assistant message role order, exits non-zero on any error for CI.
- Rewrote `stats.py`: approved-records-only coverage report with per-category counts, below-target flags, source type and difficulty breakdown.
- Rewrote `new_record.py`: interactive numbered category picker, subcategory/difficulty/tags prompts.
- Rewrote `batch_scaffold.py`: reads a seeds file (one scenario description per line), prompts once for category and difficulty for the whole batch.
- Rewrote `TAXONOMY.md`: full definitions, subcategory directions, and design rationale for each category.
- Updated `README.md`: new taxonomy table, two-track model plan, project structure, sponsor section.
- Updated `CLAUDE.md`: new category enum list, removed stale references to Jaccard duplicate detection.
- Reclassified wt-0002 from `math_and_calculations` to `disinfection_and_oxidation`.
- Reclassified wt-0003 from `taste_and_odor` to `water_source_and_reservoir_management`.
- Added sponsor acknowledgment: Robot Garden, Livermore CA (robotgarden.org).
- Decision: `pH_and_alkalinity` and `SCADA_and_controls_infrastructure` use mixed case intentionally. All other categories and all subcategories remain snake_case.

## 2026-04-05

Built the complete dataset toolchain. The project now has working infrastructure for authoring, validating, exporting, and evaluating training data.

- Added `validate.py`: schema validation against all SCHEMA.md rules, token-length heuristic, unique ID checks, Jaccard similarity duplicate detection on user prompts.
- Added `export.py`: strips metadata to produce clean training JSONL. Filters by status, category, difficulty, version. Optional system prompt injection.
- Added `stats.py`: coverage report by category, subcategory, difficulty, source type, review status. Token estimate stats (min/max/mean/median). Gap detection against full taxonomy.
- Added `eval.py`: golden evaluation framework with must_contain/must_not_contain checks. Three starter eval cases (filtration, calculations, disinfection).
- Added `new_record.py`: interactive CLI scaffolder with auto-incrementing IDs and canonical system prompt injection.
- Added `batch_scaffold.py`: batch record creation from a seeds file. Dry-run mode for planning.
- Created `data/system_prompt.txt`: minimal canonical system prompt (two sentences).
- Created `data/seeds/municipal_starter.txt`: 26 planned records across all 16 municipal categories.
- Added GitHub Actions CI workflow (`validate.yml`) to run validation on push/PR.
- Added Makefile with targets for all common operations.
- Added `docs/IDEAS.md` for future exploration directions (facility dataset creation, gamified capture, AutoAgent/Meta-Harness agent frameworks).
- Three test fixture records in `data/raw/` (draft, ai_generated) to prove the toolchain.
- Updated README with current repo layout and toolchain quickstart.
- Added CLAUDE.md with full project instructions for Claude Code sessions.
- Added `.editorconfig` for consistent line endings and indentation.
- Expanded golden eval set to 8 cases covering: filtration, math/calculations, disinfection, safety (confined space entry), regulations (IESWTR turbidity), troubleshooting (multi-filter pattern), plant operations (shift recovery), emergency response (contamination suspicion).
- Decision: one record per `.json` file (better for git diffs and review).
- Decision: pure stdlib Python 3.10+, no external dependencies.
- Decision: minimal system prompt — let fine-tuning internalize voice rather than overloading the system message.
- Decision: eval cases use keyword checks (must_contain/must_not_contain) as the initial scoring method. Semantic scoring deferred until inference pipeline exists.
- Pushed all work to GitHub.
- Next: author real operator content using the seeds file as a guide. Run `python3 scripts/batch_scaffold.py data/seeds/municipal_starter.txt` to create blank records.

## 2026-04-04

Established the initial public project scaffold for Potable.

- Created the GitHub repository structure.
- Drafted the main project README.
- Drafted a Hugging Face dataset card for Potable Dataset.
- Drafted a Hugging Face model card for PotableLM.
- Added overview and roadmap documents.
- Added dataset reference docs: schema, taxonomy, style guide, annotation guide, and changelog.
- Standardized naming around:
  Project: Potable
  Dataset: Potable Dataset
  Models: PotableLM

## Log Format

Add new entries at the top using this structure:

```md
## YYYY-MM-DD

Short summary sentence.

- concrete change or decision
- concrete change or decision
- open question or next step
```
