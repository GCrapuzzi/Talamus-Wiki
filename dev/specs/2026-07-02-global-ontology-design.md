# One ontology across all brains — design

**Decision (maintainer-directed, 2026-07-02):** the learned relation-type SCHEMA
becomes **machine-wide** — one ontology shared by every brain — instead of one
per brain. The ontology is the user's personal semantic layer: a type learned
while reading a book should immediately improve edge typing in the project
brain that uses the same surface. This is the "self-emerging ontology" quid
compounding across everything the user knows.

## What moves, what stays

| Artifact | Before | After (scope=global, the default) |
|---|---|---|
| Schema (`RelationType` list, candidate/active/deprecated, history of the schema) | `.talamus/cache/ontology/schema.json` per brain | `TALAMUS_HOME/ontology/schema.json` + `history.jsonl` beside it |
| Evidence (`evidence.jsonl` — per-note observations) | per brain | **stays per brain** (observations belong to their corpus) |
| Induction / promotion mechanics | per brain | unchanged mechanics; candidates and promotions WRITE to the shared schema |
| Runtime `build_ontology` (surface→type map) | reads the brain schema | reads the shared schema → a type promoted anywhere re-types matching surfaces everywhere |

## Config

`ontology_scope: "global" | "brain"` on `TalamusConfig`, default **"global"**.
`"brain"` keeps the historical per-brain isolation (opt-out for users who want
separate semantic worlds). Old configs without the field get the default.

## Migration (automatic, no command)

On the first `load_schema` in global scope: if the global schema does not exist
but the brain has a local one, the local schema **seeds** the global file (and
the event is logged). If BOTH exist, the global one wins and the local file is
left untouched (it simply stops being read) — no destructive merge.

## Cross-domain pollution risk (assessed)

A type only ever applies where its **surfaces match** (stemmed surface keys).
A gardening "feeds" type touches a code brain only if that brain actually uses
the surface "feeds" — in which case the semantic intent is the same. Promotion
thresholds (support ≥ 8, ≥ 3 notes) still gate activation. Residual risk is
accepted; `ontology_scope: "brain"` is the escape hatch.

## Out of scope (this pass)

Cross-brain SUPPORT aggregation for promotion (candidates still earn support
inside one brain at a time); a UI to browse "where does this type come from".
