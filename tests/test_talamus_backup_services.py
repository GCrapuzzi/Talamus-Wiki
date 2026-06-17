import tempfile
import unittest
import zipfile
from pathlib import Path

from talamus.config import TalamusConfig, save_config
from talamus.demo import create_demo_brain
from talamus.paths import TalamusPaths
from talamus.services.backup import export_brain, import_brain_archive
from talamus.store import load_notes


class TalamusBackupServiceTests(unittest.TestCase):
    def test_export_and_import_brain_roundtrip(self) -> None:
        with tempfile.TemporaryDirectory() as a, tempfile.TemporaryDirectory() as b:
            source = Path(a)
            archive_path = Path(b) / "brain.zip"
            restored = Path(b) / "restored"
            paths = TalamusPaths(source)
            create_demo_brain(paths)
            save_config(paths.config_path, TalamusConfig.default())

            exported = export_brain(source, archive_path)
            imported = import_brain_archive(archive_path, restored)

            notes = load_notes(TalamusPaths(restored))

        self.assertTrue(exported.success, exported.message)
        self.assertIsNotNone(exported.data)
        self.assertGreater(exported.data.members, 0)
        self.assertTrue(imported.success, imported.message)
        self.assertIsNotNone(imported.data)
        self.assertGreater(imported.data.members, 0)
        self.assertEqual(3, len(notes))

    def test_import_rejects_zip_path_traversal(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            archive_path = root / "evil.zip"
            dest = root / "dest"
            escape = root / "escape.txt"
            with zipfile.ZipFile(archive_path, "w") as archive:
                archive.writestr("../escape.txt", "owned")

            result = import_brain_archive(archive_path, dest)

        self.assertFalse(result.success)
        self.assertEqual("backup_import_rejected", result.code)
        self.assertFalse(escape.exists())

    def test_export_missing_brain_returns_failed_result(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            result = export_brain(Path(tmp), Path(tmp) / "brain.zip")

        self.assertFalse(result.success)
        self.assertEqual("backup_no_brain", result.code)


if __name__ == "__main__":
    unittest.main()
