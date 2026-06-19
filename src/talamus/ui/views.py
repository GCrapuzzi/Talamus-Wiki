"""Workbench views — pure builders over the SDK, testable without a window (M9/F9).

Every ``build_*`` function takes the brain paths (plus callbacks where needed) and
returns a Flet control tree. No business logic lives here: views call the same SDK
functions the CLI uses (F9 acceptance: no duplicated logic). Builders are
constructible headless, which is what the smoke tests exercise; rendering is
verified at runtime via ``talamus ui`` (desktop) or ``talamus ui --web``.
"""

from __future__ import annotations

import re
from collections.abc import Callable

import flet as ft

from talamus.domains import load_overview
from talamus.ontology import load_ontology, neighbors
from talamus.ontology_lab import load_schema, schema_status
from talamus.paths import TalamusPaths
from talamus.review import ReviewQueue
from talamus.services.readiness import EngineReadiness, NextAction, inspect_readiness
from talamus.store import load_notes
from talamus.temporal import note_timeline

_WIKILINK = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")
MD = ft.MarkdownExtensionSet.GITHUB_WEB

OpenNote = Callable[[str], None]


def wikilinks_to_md(text: str) -> str:
    """Turn Obsidian [[Target]] / [[Target|Label]] into clickable Markdown links."""
    return _WIKILINK.sub(lambda m: f"[{m.group(2) or m.group(1)}](<{m.group(1).strip()}>)", text)


def heading(text: str) -> ft.Control:
    return ft.Text(text, size=22, weight=ft.FontWeight.BOLD)


def subtle(text: str) -> ft.Control:
    return ft.Text(text, size=12, opacity=0.7)


# ------------------------------------------------------------------- home


def build_home(paths: TalamusPaths, on_action: Callable[[str], None] | None = None) -> ft.Control:
    from talamus.ui import theme

    report = inspect_readiness(root=str(paths.project_root))
    tiles = ft.Row(
        [
            theme.stat("notes", str(report.notes)),
            theme.stat("sources", str(report.sources)),
            theme.stat(
                "review",
                str(report.reviews_pending),
                color=theme.WARN if report.reviews_pending else theme.TEXT,
            ),
            theme.stat(
                "job",
                str(report.jobs_active),
                color=theme.WARN if report.jobs_active else theme.TEXT,
            ),
            theme.stat("index", report.index_backend, color=theme.ACCENT),
        ],
        wrap=True,
        spacing=theme.GAP,
    )
    rows: list[ft.Control] = [
        heading("Talamus"),
        theme.muted(report.root),
        tiles,
    ]
    if not report.config_exists:
        rows.append(
            theme.empty_state(
                ft.Icons.PSYCHOLOGY_ALT,
                "No brain selected",
                "Open an existing brain, try the demo, or create a new brain when you choose. "
                "This screen does not create files.",
            )
        )

    rows.append(theme.section("System status"))
    rows.extend(_engine_card(engine) for engine in report.engines)

    rows.append(theme.section("Next steps"))
    if report.next_actions:
        rows.extend(_next_action_card(action, on_action) for action in report.next_actions)
    else:
        rows.append(
            theme.card(
                ft.Column(
                    [
                        ft.Text("Ready", weight=ft.FontWeight.BOLD),
                        theme.muted("This brain is ready for questions."),
                    ],
                    spacing=4,
                ),
                padding=12,
            )
        )
    return ft.Column(rows, spacing=14)


def _engine_card(engine: EngineReadiness) -> ft.Control:
    from talamus.ui import theme

    marker = "selected" if engine.configured else engine.status
    return theme.card(
        ft.Column(
            [
                ft.Row(
                    [
                        ft.Text(engine.label, weight=ft.FontWeight.BOLD),
                        theme.muted(marker),
                    ],
                    spacing=8,
                    wrap=True,
                ),
                theme.muted(engine.detail),
            ],
            spacing=4,
        ),
        padding=12,
    )


def _next_action_card(
    action: NextAction, on_action: Callable[[str], None] | None = None
) -> ft.Control:
    from talamus.ui import theme

    controls: list[ft.Control] = [
        ft.Text(action.label, weight=ft.FontWeight.BOLD),
        theme.muted(action.detail),
    ]
    if on_action is not None:
        callback = on_action
        controls.append(
            ft.TextButton("Open", on_click=lambda e, target=action.target: callback(target))
        )
    return theme.card(
        ft.Column(
            controls,
            spacing=4,
        ),
        padding=12,
    )


def build_sources_panel(paths: TalamusPaths, title: str) -> ft.Control:
    """Provenance of one note, for the right inspector (PRD 14.2)."""
    for note in load_notes(paths):
        if note.title.lower() == title.strip().lower():
            if not note.sources:
                return subtle("no registered sources")
            return ft.Column(
                [subtle(f"{s.normalized_path}\n({s.locator})") for s in note.sources],
                spacing=6,
            )
    return subtle("note not found")


# ------------------------------------------------------------------- notes


def build_notes(paths: TalamusPaths, open_note: OpenNote) -> ft.Control:
    notes = sorted(load_notes(paths), key=lambda n: n.title.lower())
    if not notes:
        return ft.Column([heading("Notes"), ft.Text("No notes yet.")])
    tiles: list[ft.Control] = [
        ft.ListTile(
            title=ft.Text(note.title),
            subtitle=ft.Text(note.summary),
            on_click=lambda e, t=note.title: open_note(t),
        )
        for note in notes
    ]
    return ft.Column([heading(f"Notes ({len(notes)})"), *tiles], spacing=2)


# ------------------------------------------------------------------- graph


def build_graph(paths: TalamusPaths, title: str, open_note: OpenNote) -> ft.Control:
    """Functional graph view: the typed neighborhood of a note, navigable."""
    ontology = load_ontology(paths)
    rows: list[ft.Control] = [heading(f"Graph - {title}" if title else "Graph")]
    if not title:
        rows.append(ft.Text("Open a note from Notes or Search to explore its connections."))
        return ft.Column(rows, spacing=8)
    connected = neighbors(ontology, title)
    if not connected:
        rows.append(ft.Text("No typed connections for this note."))
        return ft.Column(rows, spacing=8)
    by_relation: dict[str, list[dict]] = {}
    for item in connected:
        by_relation.setdefault(str(item["relation"]), []).append(item)
    for relation, items in sorted(by_relation.items()):
        rows.append(ft.Text(relation, weight=ft.FontWeight.BOLD))
        for item in items:
            arrow = "->" if item["direction"] == "out" else "<-"
            rows.append(
                ft.TextButton(
                    f"{arrow} {item['title']}",
                    on_click=lambda e, t=str(item["title"]): open_note(t),
                )
            )
    return ft.Column(rows, spacing=4)


# ------------------------------------------------------------------- timeline


def build_timeline(paths: TalamusPaths, title: str) -> ft.Control:
    rows: list[ft.Control] = [heading(f"Timeline - {title}" if title else "Timeline")]
    if not title:
        rows.append(ft.Text("Open a note to see its two timelines."))
        return ft.Column(rows, spacing=8)
    data = note_timeline(paths, title)
    rows.append(
        ft.Text("Transactions (when Talamus changed the record)", weight=ft.FontWeight.BOLD)
    )
    if not data["transaction"]:
        rows.append(subtle("no versions"))
    for event in data["transaction"]:
        rows.append(subtle(f"[{event['at']}] {event['summary']}"))
    rows.append(ft.Text("Fact validity", weight=ft.FontWeight.BOLD))
    if not data["valid"]:
        rows.append(subtle("no registered claims"))
    for claim in data["valid"]:
        marker = f" (invalidated by: {claim['invalidated_by']})" if claim["invalidated_by"] else ""
        rows.append(subtle(f"[{claim['from']} -> {claim['to']}] {claim['text']}{marker}"))
    return ft.Column(rows, spacing=4)


# ------------------------------------------------------------------- domains


def build_domains(paths: TalamusPaths, open_note: OpenNote) -> ft.Control:
    overview = load_overview(paths)
    rows: list[ft.Control] = [heading("Domains")]
    if not overview:
        rows.append(ft.Text("No domains yet. Run `talamus overview`."))
    for domain in overview:
        label = f"{domain.get('name', '?')}  ({len(domain.get('members', []))} notes)"
        rows.append(ft.Text(label, size=16, weight=ft.FontWeight.BOLD))
        if domain.get("description"):
            rows.append(subtle(str(domain["description"])))
        for member in domain.get("members", []):
            rows.append(ft.TextButton(str(member), on_click=lambda e, t=str(member): open_note(t)))
    return ft.Column(rows, spacing=4)


# ------------------------------------------------------------------- review


def build_review(paths: TalamusPaths, refresh: Callable[[], None]) -> ft.Control:
    queue = ReviewQueue(paths)
    pending = queue.list(status="pending")
    rows: list[ft.Control] = [heading(f"Review ({len(pending)} pending)")]
    if not pending:
        rows.append(ft.Text("Queue is empty: no decisions pending."))
        return ft.Column(rows, spacing=8)

    def _apply(item_id: str) -> None:
        entry = queue.get(item_id)
        if entry is not None and entry.kind == "correction":
            from talamus.correct import apply_proposed_correction

            apply_proposed_correction(paths, entry.detail)
        queue.apply(item_id)
        refresh()

    def _reject(item_id: str) -> None:
        queue.reject(item_id)
        refresh()

    for item in pending:
        rows.append(
            ft.Column(
                [
                    ft.Text(f"[{item.kind}] {item.title}", weight=ft.FontWeight.BOLD),
                    subtle(str(item.detail)),
                    ft.Row(
                        [
                            ft.TextButton("Apply", on_click=lambda e, i=item.item_id: _apply(i)),
                            ft.TextButton("Reject", on_click=lambda e, i=item.item_id: _reject(i)),
                        ]
                    ),
                    ft.Divider(),
                ],
                spacing=2,
            )
        )
    return ft.Column(rows, spacing=4)


# ------------------------------------------------------------------- ontology


def build_ontology_lab(paths: TalamusPaths, refresh: Callable[[], None]) -> ft.Control:
    schema = load_schema(paths)
    status = schema_status(paths)
    cov = status["coverage"]
    rows: list[ft.Control] = [
        heading("Ontology Lab"),
        ft.Text(f"Schema {status['schema_id']} (v{status['version']})"),
        ft.Text(
            f"Coverage: {cov['non_related']}/{cov['edges']} typed edges"
            f" ({cov['non_related_share']:.0%})"
            if cov["edges"]
            else "Coverage: no edges yet"
        ),
    ]

    def _promote(type_id: str) -> None:
        from talamus.ontology_lab import promote_candidate

        promote_candidate(paths, type_id, force=True)
        refresh()

    def _reject(type_id: str) -> None:
        from talamus.ontology_lab import reject_candidate

        reject_candidate(paths, type_id)
        refresh()

    for state in ("active", "candidate", "deprecated"):
        types = [t for t in schema.relation_types if t.status == state]
        if not types:
            continue
        rows.append(ft.Text(state.capitalize(), size=16, weight=ft.FontWeight.BOLD))
        for rel_type in types:
            detail = [
                ft.Text(f"{rel_type.name}  (support {rel_type.support})"),
                subtle(rel_type.definition or "(no definition)"),
            ]
            for example in rel_type.examples[:2]:
                detail.append(subtle(f"e.g. {example}"))
            if state == "candidate":
                detail.append(
                    ft.Row(
                        [
                            ft.TextButton("Promote", on_click=lambda e, i=rel_type.id: _promote(i)),
                            ft.TextButton("Reject", on_click=lambda e, i=rel_type.id: _reject(i)),
                        ]
                    )
                )
            detail.append(ft.Divider())
            rows.append(ft.Column(detail, spacing=2))
    return ft.Column(rows, spacing=4)


# ------------------------------------------------------------------- settings


def build_settings(paths: TalamusPaths, notify: Callable[[str], None] | None = None) -> ft.Control:
    """Everything configurable in-app (Phase R3): engine, model, API key, MCP,
    brain registry flags. Saves go to talamus.json / TALAMUS_HOME - the same
    files the CLI uses (no duplicated logic, just thin wiring)."""
    import dataclasses
    import os

    from talamus.adapters.llm import detect_engines, save_credential
    from talamus.config import load_or_default, save_config
    from talamus.indexes import backend_info
    from talamus.registry import load_registry, set_brain_flag
    from talamus.ui import theme

    def _notify(message: str) -> None:
        if notify is not None:
            notify(message)

    config = load_or_default(paths.config_path)
    info = backend_info(paths)

    engines = detect_engines()
    if config.llm_provider not in engines:
        engines.insert(0, config.llm_provider)
    engine_dd = ft.Dropdown(
        label="LLM engine",
        value=config.llm_provider,
        options=[ft.DropdownOption(key=name, text=name) for name in engines],
        width=320,
    )
    model_tf = ft.TextField(
        label="Model (optional, e.g. llama3)",
        value=config.llm_model,
        width=320,
    )
    language_tf = ft.TextField(
        label="Note language (empty = system auto-detect)",
        value=config.language,
        hint_text="e.g. Italian, English, German",
        width=320,
    )

    def save_engine(_e: object) -> None:
        current = load_or_default(paths.config_path)
        updated = dataclasses.replace(
            current,
            llm_provider=engine_dd.value or current.llm_provider,
            llm_model=model_tf.value or "",
            language=language_tf.value or "",
        )
        save_config(paths.config_path, updated)
        _notify(f"Engine saved: {updated.llm_provider}")

    key_set = bool(os.environ.get("ANTHROPIC_API_KEY"))
    key_tf = ft.TextField(
        label="Anthropic API key (anthropic-api engine)",
        password=True,
        can_reveal_password=True,
        width=320,
        hint_text="already set via env" if key_set else "empty",
    )

    def save_key(_e: object) -> None:
        if key_tf.value:
            save_credential("anthropic_api_key", key_tf.value)
            key_tf.value = ""
            _notify("Key saved in TALAMUS_HOME/credentials.json (the env var always wins)")

    def install_mcp(_e: object) -> None:
        import json as _json

        config_file = paths.project_root / ".mcp.json"
        data: dict = {}
        if config_file.exists():
            try:
                data = _json.loads(config_file.read_text(encoding="utf-8"))
            except _json.JSONDecodeError:
                data = {}
        data.setdefault("mcpServers", {})["talamus"] = {
            "command": "talamus-mcp",
            "args": ["--root", str(paths.project_root)],
        }
        config_file.write_text(_json.dumps(data, indent=2), encoding="utf-8")
        _notify(f"MCP configured: {config_file} (restart your agent)")

    registry = load_registry()
    brain_rows: list[ft.Control] = []
    for brain in registry.brains:

        def _toggle(name: str, flag: str) -> Callable[[ft.Event[ft.Switch]], None]:
            def handler(e: ft.Event[ft.Switch]) -> None:
                set_brain_flag(name, flag, bool(e.control.value))
                _notify(f"{name}: {flag} = {e.control.value}")

            return handler

        brain_rows.append(
            theme.card(
                ft.Column(
                    [
                        ft.Text(f"{brain.name}  ({brain.type})", weight=ft.FontWeight.BOLD),
                        theme.muted(brain.path),
                        ft.Row(
                            [
                                ft.Switch(
                                    label="federated",
                                    value=brain.federated,
                                    on_change=_toggle(brain.name, "federated"),
                                ),
                                ft.Switch(
                                    label="sensitive",
                                    value=brain.sensitive,
                                    on_change=_toggle(brain.name, "sensitive"),
                                ),
                            ]
                        ),
                    ],
                    spacing=4,
                ),
                padding=12,
            )
        )
    if not brain_rows:
        brain_rows.append(theme.muted("no brains in the registry (`talamus init` registers one)"))

    budget = os.environ.get("TALAMUS_CONTEXT_BUDGET", "6000 (default)")
    return ft.Column(
        [
            heading("Settings"),
            theme.section("Engine"),
            theme.card(
                ft.Column(
                    [
                        engine_dd,
                        model_tf,
                        language_tf,
                        ft.FilledButton("Save engine", on_click=save_engine),
                    ],
                    spacing=10,
                )
            ),
            theme.section("API key"),
            theme.card(
                ft.Column([key_tf, ft.FilledButton("Save key", on_click=save_key)], spacing=10)
            ),
            theme.section("Agent integrations"),
            theme.card(
                ft.Column(
                    [
                        ft.FilledButton("Install MCP in this project", on_click=install_mcp),
                        theme.muted(
                            "Capture hook: `talamus hook` prints the snippet for "
                            ".claude/settings.json"
                        ),
                    ],
                    spacing=10,
                )
            ),
            theme.section("Registered brains"),
            *brain_rows,
            theme.section("System"),
            theme.card(
                ft.Column(
                    [
                        theme.muted(f"Index: {info['backend']} ({info['bytes']:,} bytes)"),
                        theme.muted(f"Context budget: {budget} tokens (TALAMUS_CONTEXT_BUDGET)"),
                    ],
                    spacing=4,
                )
            ),
        ],
        spacing=10,
    )
