# P7 — Web Workbench (foundation pivot) — Design + Walking Skeleton

- **Date:** 2026-06-26
- **Status:** approved (brainstorm), pre-implementation
- **Phase:** P7 in [dev/ROADMAP.md](../ROADMAP.md) — redefined from "finish the Flet UI" to "web workbench"
- **Branch:** `feat/p7-web-workbench`

## Decisions recorded (the brainstorm)

- **Goal:** the UI must be **viral** (screenshot/GIF/embed-worthy), **intuitive for a
  novice and complete for an expert**, with a reorganized navigation and an
  **IDE-grade workbench** (tabs, collapsible sidebars, panels) à la Cursor/VS Code.
- **Viral bet:** the **living graph as the hero** + a **distinctive brand identity**
  ("Aurora": electric indigo `#6E5BFF` + cyan `#4FC3F7` on near-black). Lightness
  first — the "wow" comes from composition/color/typography and at most one light
  animation, never GPU-heavy effects.
- **Foundation = a real local Web UI (option B):** the current Flet UI cannot deliver
  IDE-grade layouts cleanly, and Flutter-web screenshots poorly (a liability for a
  viral product). We rebuild the frontend as a **React + Vite + TypeScript SPA** on
  the **existing `services/` layer** (P1's seam makes this clean).
- **Plug-and-play preserved:** `talamus ui` opens a **native window via pywebview**
  (OS webview — no Chromium, no browser-localhost feel), serving **prebuilt** React
  assets from a local Python server. At release this packages into a **downloadable,
  double-click, desktop-icon app** (PyInstaller). The **CLI + MCP wedge stays 100%
  zero-setup** regardless — the GUI is an optional `[ui]` extra.

## Why this serves the strategy

Adoption is the north-star and the endgame is a beloved OSS tool. A distinctive,
screenshot-worthy workbench (graph hero + Aurora identity) is the viral surface; a
web frontend is the most capable and most shareable vehicle, and React brings the
largest contributor pool. The agent-memory wedge (CLI/MCP) is untouched, so nothing
about zero-setup is lost.

## What happens to the Flet work

- **Reused as-is:** the entire backend — SDK, `services/`, ask/recall/ingest/graph
  data, readiness, ontology. The React app is a thin client over the same services.
- **Reused (server-side):** `ui/physics.py` is pure-Python force layout — the graph
  layout is computed **server-side** (deterministic, testable) and the client only
  renders + pans/zooms.
- **Becomes the blueprint:** `ui/views.py`/`ui/app.py` and `tests/test_talamus_ui.py`
  encode the IA, copy, empty states, moat explanations and guardrails — the React
  port reuses those product decisions; the service-contract tests stay valid.
- **Retired only at parity:** the Flet rendering layer (Flet controls, `ui/theme.py`,
  the `app.py` shell, `ui/graph.py` canvas). Flet keeps working during the transition
  and is removed once the web workbench reaches parity. No gap for users.

## Architecture

```
React SPA (webui/)  ──HTTP/JSON──►  FastAPI bridge (src/talamus/webapi/)  ──►  services/  ──►  core
   (Vite, TS)                         1 service → 1 endpoint                    (unchanged)
   Aurora design tokens               ServiceResult{success,message,code,data} == response body
   graph: render server-laid-out      pywebview opens a native window over the local server
```

- **Bridge** (`src/talamus/webapi/`): a thin FastAPI app. Each endpoint calls a
  `services/` function and returns its `ServiceResult` as JSON (HTTP 200 with
  `success` in the body; the body shape is already public via `ServiceResult.to_dict`).
  Read endpoints are GET, actions are POST. No business logic in the bridge.
- **Frontend** (`webui/`): a Vite + React + TypeScript SPA, built to static assets
  that ship inside the Python package (the user never runs Node). Aurora theme as CSS
  variables. Workbench shell: **activity bar** (left icons) + **collapsible primary
  sidebar** + **tabbed center** + **right inspector panel** + **status bar**.
- **Graph hero**: `GET /api/graph` returns nodes (with server-computed `x,y` from
  `physics.py`) + typed edges; the client renders them on a `<canvas>` in the Aurora
  constellation style with pan/zoom and click-to-open. One light settle animation
  only.
- **Launch**: `talamus ui` starts uvicorn on a local port and opens a **pywebview**
  window pointing at it; `talamus ui --web` opens the default browser instead.

## Distribution & plug-and-play

- **Dev:** `pip install talamus[ui]` → `talamus ui` → native window (pywebview).
- **Release (later, P10/P11):** PyInstaller bundles Python + FastAPI + prebuilt React
  assets + pywebview into a per-OS **downloadable app with a desktop icon**
  (Windows `.exe/.msi`, macOS `.app/.dmg`, Linux AppImage). pywebview uses the OS
  webview so the binary stays light (~30–60 MB, no bundled Chromium).
- **Signing/notarization** (Apple/Windows certs) is a launch-polish decision (it costs
  money, tensions with €0) — deferred; OSS distribution via pip/winget/brew works
  unsigned in the meantime.
- **The wedge is never gated by the GUI:** `pip install talamus` + MCP/CLI stays
  zero-setup with no browser, no webview, no Node.

## Decomposition (sub-projects, sequenced)

1. **Walking skeleton** ← *this spec's build*: FastAPI bridge + a few endpoints +
   the React Aurora shell + two real views (Home/readiness + Graph hero), launched by
   `talamus ui` via pywebview. Flet untouched in parallel.
2. **Port the remaining views** with the new IA + explainability (Ask, Library,
   Import, Review, Ontology, Brains, System).
3. **Multi-tab / multi-sidebar / panels** polish; command palette.
4. **Onboarding & progressive disclosure** (novice ↔ expert).
5. **Packaging** (downloadable desktop-icon binary) and **Flet retirement** at parity.

## Walking skeleton — scope (the deliverable of this spec)

**Backend** (`src/talamus/webapi/`, optional `[ui]` extra: fastapi + uvicorn +
pywebview):
- `GET /api/readiness` → wraps `services.readiness.inspect_readiness`.
- `GET /api/graph` → wraps `services.graph.get_graph_snapshot`, augmented with
  server-side `physics.py` coordinates (a thin `webapi.graph_layout` helper).
- `GET /api/library` → wraps `services.library.list_library_notes` (proves a list view).
- Serves the built SPA static files at `/`.
- `talamus ui` (re-pointed): start uvicorn + open pywebview window; `--web` opens the
  browser; `--port` honored.

**Frontend** (`webui/`):
- Vite + React + TS project; Aurora design tokens (CSS variables) in one `theme.css`.
- Shell: activity bar + collapsible sidebar + tabbed center + status bar (inspector
  panel stub).
- **Home view**: renders `/api/readiness` (engine/brain/access/review + the moat
  summary) — proves a data view.
- **Graph hero view**: renders `/api/graph` on a canvas, Aurora constellation, pan/
  zoom, click-a-node logs/opens — proves the hero + the hardest path.

**Tests:**
- Python: endpoint tests for the bridge (status + `ServiceResult` shape on a demo
  brain) run in `python dev.py`.
- Frontend: a minimal Vitest smoke (shell renders, a view renders mock data) — or
  deferred to sub-project 2 if it slows the skeleton; the build must succeed in CI.
- The existing Flet UI + services tests stay green (services unchanged).

**Exit criteria (skeleton):** `talamus ui` opens a native Aurora window showing the
Home + Graph-hero views driven by the real local brain; the graph reads as a luminous
constellation worth screenshotting; `python dev.py` green; Flet still works.

## Out of scope (this spec)

The other seven views, multi-tab/command-palette polish, onboarding flows, the
packaged binary, code signing, and Flet retirement — each is a later sub-project.

## Testing strategy

- Backend bridge: standard Python unittests in the gate (the bridge is thin and
  deterministic on a demo brain).
- Frontend: Vitest + Testing Library for component/smoke tests; the Vite build runs in
  CI so a broken frontend fails the pipeline. Heavy/visual checks stay manual (pywebview
  / browser), like the Flet GUI today.
- Reuse `tests/test_talamus_ui.py` as the **behavioral/copy acceptance reference** when
  porting each view to React.

## Risks & mitigations

- **Two frontends during transition** (Flet + React): accepted and bounded — Flet is
  frozen (only kept working), React advances; retire Flet at parity.
- **OS webview dependency** (pywebview): present on modern Win/mac/Linux; `--web`
  fallback always works.
- **Frontend build pipeline** adds maintainer complexity (Node/Vite): hidden from
  users via prebuilt shipped assets; documented in CONTRIBUTING.
- **Scope creep**: the walking skeleton is deliberately two views; resist porting more
  until the skeleton proves the stack end-to-end.
- **Lightness**: React runtime + canvas graph must stay snappy on modest hardware —
  measure; server-side layout keeps the client cheap; no heavy effects.
