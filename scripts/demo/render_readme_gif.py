from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

WIDTH = 1200
HEIGHT = 675
BACKGROUND = "#0A0E14"
PANEL = "#101722"
PANEL_EDGE = "#283245"
TEXT = "#EAEFF7"
MUTED = "#8390A5"
VIOLET = "#8C7CFF"
CYAN = "#4FC3F7"
GREEN = "#7BD389"
AMBER = "#F4C36A"


@dataclass(frozen=True)
class TerminalLine:
    text: str
    color: str = TEXT


@dataclass(frozen=True)
class Scene:
    eyebrow: str
    title: str
    lines: tuple[TerminalLine, ...]
    hold_frames: int = 7


SCENES = (
    Scene(
        "01 / INSTALL",
        "Give the project a memory.",
        (
            TerminalLine('$ pipx install "talamus[mcp]"', CYAN),
            TerminalLine("  Successfully installed talamus", GREEN),
            TerminalLine(""),
            TerminalLine("$ talamus setup", CYAN),
            TerminalLine("  engine: codex-cli (found)", MUTED),
            TerminalLine("  MCP connected · capture requires consent", GREEN),
            TerminalLine("  Done. Your local memory is alive.", TEXT),
        ),
    ),
    Scene(
        "02 / CAPTURE",
        "The agent session ends.",
        (
            TerminalLine("agent › We chose SQLite FTS5 with the porter tokenizer.", TEXT),
            TerminalLine("agent › Exact technical terms ranked above fuzzy matches.", TEXT),
            TerminalLine("agent › Keep the decision and the reason for the next session.", TEXT),
            TerminalLine(""),
            TerminalLine("session ended", AMBER),
            TerminalLine("  transcript + git diff passed the worth-remembering gate", MUTED),
            TerminalLine("  capture: 1 source-grounded Markdown note", GREEN),
        ),
    ),
    Scene(
        "03 / RECALL",
        "A fresh session remembers.",
        (
            TerminalLine('$ talamus recall "why did we choose FTS5?"', CYAN),
            TerminalLine(""),
            TerminalLine("SQLite FTS5 Porter Search Decision", VIOLET),
            TerminalLine("  Chosen because the trigram index misranked exact", TEXT),
            TerminalLine("  English terms. FTS5 improved measured retrieval quality.", TEXT),
            TerminalLine(""),
            TerminalLine("source  notes/SQLite-FTS5-Porter-Search-Decision.md", GREEN),
            TerminalLine("claim   linked to the captured session transcript", MUTED),
        ),
        hold_frames=10,
    ),
    Scene(
        "04 / LOCAL-FIRST",
        "Memory that survives the session.",
        (
            TerminalLine("✓ Markdown stays the source of truth", GREEN),
            TerminalLine("✓ Search and graph stay on your machine", GREEN),
            TerminalLine("✓ No hosted account or required embeddings", GREEN),
            TerminalLine("✓ Claude · Codex · Ollama · OpenCode", GREEN),
            TerminalLine(""),
            TerminalLine("Your agent remembered. Locally.", VIOLET),
            TerminalLine("github.com/ampres-ai/talamus", CYAN),
        ),
        hold_frames=14,
    ),
)


def _font(candidates: tuple[str, ...], size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for candidate in candidates:
        path = Path(candidate)
        if path.is_file():
            return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


def _fonts() -> tuple[ImageFont.ImageFont, ImageFont.ImageFont, ImageFont.ImageFont]:
    mono_candidates = (
        "C:/Windows/Fonts/CascadiaMono.ttf",
        "C:/Windows/Fonts/consola.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
    )
    bold_candidates = (
        "C:/Windows/Fonts/segoeuib.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    )
    return (
        _font(mono_candidates, 22),
        _font(bold_candidates, 35),
        _font(bold_candidates, 19),
    )


def _draw_brand_mark(draw: ImageDraw.ImageDraw) -> None:
    x, y = 70, 56
    draw.rounded_rectangle((x, y, x + 36, y + 36), radius=9, fill=VIOLET)
    draw.line((x + 10, y + 18, x + 17, y + 25, x + 28, y + 10), fill=TEXT, width=4)


def _render_scene(
    scene: Scene,
    scene_index: int,
    visible_lines: int,
    cursor_on: bool,
    fonts: tuple[ImageFont.ImageFont, ImageFont.ImageFont, ImageFont.ImageFont],
) -> Image.Image:
    mono, title_font, label_font = fonts
    image = Image.new("RGB", (WIDTH, HEIGHT), BACKGROUND)
    draw = ImageDraw.Draw(image)

    _draw_brand_mark(draw)
    draw.text((120, 59), "TALAMUS", font=label_font, fill=TEXT)
    draw.text((120, 84), "LOCAL-FIRST AGENT MEMORY", font=mono, fill=MUTED)
    draw.text((935, 65), scene.eyebrow, font=label_font, fill=VIOLET)

    draw.text((70, 130), scene.title, font=title_font, fill=TEXT)
    draw.rounded_rectangle(
        (70, 194, 1130, 600),
        radius=16,
        fill=PANEL,
        outline=PANEL_EDGE,
        width=2,
    )

    for offset, color in ((0, "#FF6B6B"), (22, AMBER), (44, GREEN)):
        draw.ellipse((94 + offset, 216, 106 + offset, 228), fill=color)
    draw.text((920, 212), "talamus · demo", font=mono, fill=MUTED)
    draw.line((94, 246, 1106, 246), fill=PANEL_EDGE, width=1)

    y = 273
    for line in scene.lines[:visible_lines]:
        draw.text((102, y), line.text, font=mono, fill=line.color)
        y += 38

    if cursor_on and visible_lines < len(scene.lines):
        draw.rounded_rectangle((102, y + 2, 116, y + 28), radius=2, fill=CYAN)

    progress_left, progress_right = 70, 1130
    draw.rounded_rectangle(
        (progress_left, 632, progress_right, 638),
        radius=3,
        fill=PANEL_EDGE,
    )
    progress = (scene_index + 1) / len(SCENES)
    draw.rounded_rectangle(
        (progress_left, 632, progress_left + int((progress_right - progress_left) * progress), 638),
        radius=3,
        fill=VIOLET,
    )
    return image


def render(output: Path) -> None:
    fonts = _fonts()
    frames: list[Image.Image] = []
    durations: list[int] = []

    for scene_index, scene in enumerate(SCENES):
        for visible_lines in range(len(scene.lines) + 1):
            frames.append(
                _render_scene(
                    scene,
                    scene_index,
                    visible_lines,
                    cursor_on=visible_lines % 2 == 0,
                    fonts=fonts,
                )
            )
            durations.append(320 if visible_lines else 480)
        for hold_index in range(scene.hold_frames):
            frames.append(
                _render_scene(
                    scene,
                    scene_index,
                    len(scene.lines),
                    cursor_on=hold_index % 2 == 0,
                    fonts=fonts,
                )
            )
            durations.append(380)

    output.parent.mkdir(parents=True, exist_ok=True)
    first, *rest = frames
    first.save(
        output,
        save_all=True,
        append_images=rest,
        duration=durations,
        disposal=2,
        loop=0,
        optimize=True,
    )


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Render the README demo as an animated GIF.")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("docs/assets/talamus-demo.gif"),
        help="output GIF path",
    )
    return parser


def main() -> int:
    args = _parser().parse_args()
    render(args.output)
    print(f"rendered {args.output} ({args.output.stat().st_size:,} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
