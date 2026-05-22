import json
import tempfile
import unittest
from pathlib import Path

from tools.fde_brain.registry import RegistryEntry, append_entry, load_registry, save_registry


def _entry(raw_path: str = "AI Space/raw/markdown/2026-05-22-x.md") -> RegistryEntry:
    return RegistryEntry(
        raw_path=raw_path,
        raw_hash="sha256:abc",
        raw_size=123,
        normalized_paths=["AI Space/normalized/markdown/x.md"],
        category="markdown",
        parser="passthrough",
        captured_at="2026-05-22T12:00:00+00:00",
        ingestion_run="run-1",
    )


class RegistryTests(unittest.TestCase):
    def test_load_missing_file_returns_empty(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            entries = load_registry(Path(tmp) / "nonexistent.json")
            self.assertEqual([], entries)

    def test_append_creates_file_with_single_entry(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            registry = Path(tmp) / "registry.json"
            entry = _entry()

            append_entry(registry, entry)

            self.assertTrue(registry.exists())
            entries = load_registry(registry)
            self.assertEqual(1, len(entries))
            self.assertEqual(entry, entries[0])

    def test_append_preserves_existing_entries(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            registry = Path(tmp) / "registry.json"
            first = _entry(raw_path="AI Space/raw/markdown/first.md")
            second = _entry(raw_path="AI Space/raw/text/second.txt")

            append_entry(registry, first)
            append_entry(registry, second)

            entries = load_registry(registry)
            self.assertEqual([first, second], entries)

    def test_save_roundtrip(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            registry = Path(tmp) / "registry.json"
            entries = [_entry(raw_path=f"AI Space/raw/markdown/{i}.md") for i in range(3)]

            save_registry(registry, entries)
            loaded = load_registry(registry)

            self.assertEqual(entries, loaded)

    def test_file_has_version_field(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            registry = Path(tmp) / "registry.json"
            append_entry(registry, _entry())

            data = json.loads(registry.read_text(encoding="utf-8"))
            self.assertEqual("1.0", data["version"])
            self.assertIsInstance(data["entries"], list)

    def test_promoted_to_defaults_to_empty_list(self) -> None:
        entry = _entry()
        self.assertEqual([], entry.promoted_to)


if __name__ == "__main__":
    unittest.main()
