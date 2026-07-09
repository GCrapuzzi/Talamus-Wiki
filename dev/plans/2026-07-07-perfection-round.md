# Perfection round — maintainer-ordered (2026-07-07 evening)

Giovanni's ruling: do not stop at the launch minimum. Four fronts, in parallel
where files are independent. Every number re-measured lands in STATE; every
front ends gate-green.

## F1 — Benchmarks, hyper-fresh (all metrics on TODAY's code)

The one-screen artifacts date 2026-06-15/17 (pre-RS8-refactor code). Re-run:

- [x] shootout book (claude-cli expansion): talamus-smart 0.929/0.847/0.865/
      0.971 — leads multilingual-e5 on all four; search unchanged (no regression)
- [x] shootout scifact (full set): talamus-search beats BM25 on all four
      (RS8 confirmed post-refactor, now artifact-backed)
- [x] token consumption re-measured: −97.7% recall / −99.8% search
      (2026-07-08-token-efficiency.md)
- [x] one_screen.py + one-screen.md + docs/benchmarks.md regenerated from the
      fresh artifacts (two-faced honest row: quality tracks the expansion
      engine); STATE dashboard + build-history rows refreshed
- DONE (F1 DELIVERED 2026-07-09)
- SKIPPED with reason: (a) 100k scale re-run — index code path + CACHE_VERSION
  untouched since 2026-07-02. (b) ask-eval full re-run — ask path unchanged and
  retrieval proven identical to June by the shootouts; the 2026-06-17 ask-eval
  artifacts stay valid. Both stated honestly in STATE.

## F2 — The ontology level-jump (RULED 2026-07-07: A + B + C, all three)

Execution order: B first (the substance, measured), A on top of B (the
insights UI/MCP exposes include what inference found), C last (cross-brain).

## The three options (context)

A. **Visible moat**: ontology insights surfaced in UI + MCP (surprising
   links, coverage gaps, domain map as interactive navigation). Low risk,
   demoable, serves U2.
B. **Inference layer**: typed-relation closure (inverse/transitive) feeding
   ask routing and neighbors; ships ONLY on a two-corpora measured win (the
   ON/OFF ablation already shows the ontology lifts answers 0.886→0.957).
C. **Cross-brain schema analytics**: support aggregation across brains
   (pulled forward from post-launch backlog).

Recommendation: B (the substance) + A (the visibility), C stays post-launch.

## F3 — UI: CLI parity + 20k-stars quality

Parity gaps named by the maintainer: MCP configuration from the UI (install
per agent + status), engine/provider switching (service exists — surface it),
provider usage/limits view (surface EngineLimitReached state + last-seen
limits per provider), Home redesign (today it is "terrible": next-actions,
brain stats, recent captures, first-run experience). Then the aesthetic/UX
pass (graph stays the hero). Method: audit CLI-vs-UI parity first, codex for
webapi endpoints + view scaffolds, taste pass by hand, Giovanni's eye last
(U1 sign-off). Toolchain verified: node 24 / npm 11 / webui deps installed.

## F4 — Repo exemplary

README to exemplary (hero, the one-screen table, honest comparison, 3-line
quickstart, demo gif once recorded), docs coherence pass, CONTRIBUTING
refresh, CHANGELOG stamped at 1.0.0 in L3. Delegable sweep, editorial
direction and final cut by hand.

## Standing constraints

Two-corpora law for any retrieval/quality change; numbers only from artifacts;
codex jobs in dedicated worktrees with targeted tests; watch for the codex
mojibake trap (grep `â€` after every write job).
