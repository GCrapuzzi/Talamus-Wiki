"""Talamus design system — dark-first, dense, calm (Fase R1, PRD 14.3).

One place for palette, spacing and reusable surfaces (cards, stat tiles, empty
states), so every view looks like the same product. Principles from the llm_wiki
study: quiet professional density, clear typographic hierarchy, restrained
accents, no decorative filler.
"""

from __future__ import annotations

from collections.abc import Callable

import flet as ft

# palette — charcoal base, readable text, one cool accent
BG = "#14181C"
SURFACE = "#1B2127"
SURFACE_2 = "#222A32"
BORDER = "#2C353E"
TEXT = "#E6EDF3"
MUTED = "#94A3B0"
ACCENT = "#4FC3F7"
WARN = "#FFB74D"
OK = "#81C784"

PAD = 16
GAP = 12


def apply(page: ft.Page) -> None:
    """Page-level look: dark theme, charcoal background, no default padding."""
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = BG
    page.padding = 0


def title(text: str) -> ft.Control:
    return ft.Text(text, size=22, weight=ft.FontWeight.BOLD, color=TEXT)


def section(text: str) -> ft.Control:
    return ft.Text(text.upper(), size=11, weight=ft.FontWeight.BOLD, color=MUTED)


def muted(text: str, size: int = 12) -> ft.Control:
    return ft.Text(text, size=size, color=MUTED)


def card(content: ft.Control, padding: int = PAD) -> ft.Control:
    return ft.Container(
        content=content,
        bgcolor=SURFACE,
        border=ft.Border.all(1, BORDER),
        border_radius=10,
        padding=padding,
    )


def stat(label: str, value: str, color: str = TEXT) -> ft.Control:
    """A compact stat tile for dashboards."""
    return card(
        ft.Column(
            [
                ft.Text(value, size=24, weight=ft.FontWeight.BOLD, color=color),
                muted(label),
            ],
            spacing=2,
            tight=True,
        ),
        padding=14,
    )


def empty_state(
    icon: ft.IconData,
    headline: str,
    hint: str,
    action_label: str = "",
    on_action: Callable[[], None] | None = None,
) -> ft.Control:
    """A cared-for empty view: never just blank space (PRD 13.1/14.3)."""
    rows: list[ft.Control] = [
        ft.Icon(icon, size=44, color=MUTED),
        ft.Text(headline, size=16, weight=ft.FontWeight.BOLD, color=TEXT),
        muted(hint),
    ]
    if action_label and on_action is not None:
        rows.append(ft.FilledButton(action_label, on_click=lambda e: on_action()))
    return ft.Container(
        content=ft.Column(
            rows,
            spacing=10,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        alignment=ft.Alignment.CENTER,
        padding=48,
    )
