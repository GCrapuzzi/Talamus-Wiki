import importlib.util
import tempfile
import unittest
from pathlib import Path

_HAS_FLET = importlib.util.find_spec("flet") is not None


@unittest.skipUnless(_HAS_FLET, "flet not installed (ui extra)")
class WikilinkConversionTests(unittest.TestCase):
    """Pure conversion logic of the Flet UI — no window needed."""

    def _convert(self, text: str) -> str:
        from talamus.ui.views import wikilinks_to_md

        return wikilinks_to_md(text)

    def test_plain_wikilink_becomes_angle_bracketed_link(self) -> None:
        self.assertEqual(self._convert("see [[Embedding]]"), "see [Embedding](<Embedding>)")

    def test_aliased_wikilink_uses_label_and_target(self) -> None:
        self.assertEqual(
            self._convert("[[Embedding|gli embedding]]"), "[gli embedding](<Embedding>)"
        )

    def test_target_with_spaces_stays_one_url(self) -> None:
        self.assertEqual(self._convert("[[Vector Store]]"), "[Vector Store](<Vector Store>)")

    def test_text_without_wikilinks_is_unchanged(self) -> None:
        self.assertEqual(self._convert("nessun link qui"), "nessun link qui")


@unittest.skipUnless(_HAS_FLET, "flet not installed (ui extra)")
class WorkbenchBuildersSmokeTests(unittest.TestCase):
    """F9.14: every view builds headless on a demo brain AND on an empty brain —
    Flet controls are constructible without a window; rendering stays a runtime check."""

    def _builders(self, paths):
        from talamus.ui import views

        noop = lambda *_args: None  # noqa: E731
        return {
            "home": lambda: views.build_home(paths),
            "note": lambda: views.build_notes(paths, noop),
            "domini": lambda: views.build_domains(paths, noop),
            "grafo_unfocused": lambda: views.build_graph(paths, "", noop),
            "grafo_focused": lambda: views.build_graph(paths, "Reranking", noop),
            "timeline": lambda: views.build_timeline(paths, "Reranking"),
            "review": lambda: views.build_review(paths, noop),
            "ontologia": lambda: views.build_ontology_lab(paths, noop),
            "impostazioni": lambda: views.build_settings(paths),
        }

    def test_all_views_build_on_demo_brain(self) -> None:
        import flet as ft

        from talamus.demo import create_demo_brain
        from talamus.paths import TalamusPaths

        with tempfile.TemporaryDirectory() as tmp:
            paths = TalamusPaths(Path(tmp))
            create_demo_brain(paths)
            for name, builder in self._builders(paths).items():
                control = builder()
                self.assertIsInstance(control, ft.Control, name)

    def test_all_views_build_on_empty_brain(self) -> None:
        import flet as ft

        from talamus.paths import TalamusPaths

        with tempfile.TemporaryDirectory() as tmp:
            paths = TalamusPaths(Path(tmp))
            paths.ensure_directories()
            for name, builder in self._builders(paths).items():
                control = builder()
                self.assertIsInstance(control, ft.Control, name)

    def test_run_app_signature_supports_web_mode(self) -> None:
        import inspect

        from talamus.ui.app import run_app

        parameters = inspect.signature(run_app).parameters
        self.assertIn("web", parameters)
        self.assertIn("port", parameters)


if __name__ == "__main__":
    unittest.main()
