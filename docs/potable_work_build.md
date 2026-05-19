# potable work — Build Notes

`potable_work/` is a fork of [OpenWork](https://github.com/openwork-ai/openwork) (open-source Claude desktop alternative). It is gitignored in this repo — source lives inside the directory but build artifacts and node_modules are not tracked.

## Base repo

Clone from: https://github.com/openwork-ai/openwork  
Fork point: commit checked out ~2026-05-11 (no explicit tag pinned)

## Modifications made to the base repo

### Branding
- `apps/app/index.html` — title → "potable work", favicon → `oi-logo.svg`
- `apps/app/src/i18n/locales/en.ts` — welcome title → "potable work", subtitle → "Power to the Frontline"
- `apps/desktop/electron-builder.yml` — `productName` → "potable work", artifact name → `potable-work-${os}-...`
- Added to `apps/app/public/`: `oi-logo.png`, `oi-logo.svg`, `oi-mark.png`, `potable-mark.svg`

### Design system (`apps/app/src/app/index.css`)
- Added fonts: Sora Variable (display), Manrope Variable (UI)
- Full CSS variable retheme: teal/slate water palette
  - Light: surface `#edf3f4`, sidebar `#d6e3e7`, accent `#1d6d8c`, text `#162028`
  - Dark: surface `#0d1419`, sidebar `#18242d`, accent `#8dc6d6`
- Body font stack updated to include Manrope

### Welcome / onboarding (`apps/app/src/react-app/domains/onboarding/welcome-page.tsx`)
- Capabilities panel replaced: generic tool icons → water treatment domain cards
  - Basin Simulation, Training Games, Write SOPs, Build Tools, Monitor Data, PotableLM
- Removed `BrandIcon` component (was fetching from SimpleIcons CDN)
- Replaced lucide icons: `Waves`, `Brain`, `ClipboardList`, `Wrench`, `Activity`, `BookOpen`
- "Share / Provision team" cards removed, replaced with "Power to the Frontline" motto callout
- Panel header: "Operational Inference" label + "AI built for the water treatment floor."

### Messaging removed
- Deleted: `apps/app/src/react-app/domains/settings/pages/messaging-view.tsx` (~1069 lines)
- Deleted: `apps/app/src/react-app/domains/settings/state/messaging-view-state.ts` (~962 lines)
- `settings-route.tsx` — messaging route removed
- `settings-page.tsx` — messaging tab removed from settings shell

### Electron (`apps/desktop/electron/`)
- `main.mjs`, `browser-mcp.mjs`, `browser-native-tools.mjs` — minor modifications (not fully diffed; check git diff in potable_work)

### Workspace config
- `pnpm-workspace.yaml` — 2 lines removed (likely ee/ workspace entries)
- `apps/app/src/app/constants.ts` — duplicate import removed

## Runtime dependency — opencode binary

The app requires the opencode CLI backend. It looks in this order:
1. `resources/sidecars/` (bundled in packaged builds — gitignored, not in repo)
2. `~/.opencode/bin/opencode.exe`
3. PATH

**Install it once per machine:**
```
bash install_opencode.sh
```
Without this, the app loads a white screen (backend never starts).

## To run in dev mode (no full build needed)

Requires Visual Studio Build Tools with "Desktop development with C++" (for native Electron modules).

```
pnpm install
pnpm run dev:windows        # ARM64 host
pnpm run dev:windows:x64    # force x64
```

This starts both the Vite UI dev server and Electron together.

## To rebuild the packaged app from scratch

```
git clone https://github.com/openwork-ai/openwork potable_work
cd potable_work
# Apply modifications listed above
pnpm install
pnpm run build
```

Assets (logos etc.) are in `potable_work/apps/app/public/` — copy from a prior build or the OI style guide archive.
