import json
import tempfile
import unittest
from pathlib import Path

from talamus.registry import load_registry, register_brain
from talamus.services.brains import (
    get_brain,
    list_brains,
    register_existing_brain,
    rename_registered_brain,
    select_registered_brain,
    set_registered_brain_flags,
    unregister_registered_brain,
)


class BrainRegistryServiceTests(unittest.TestCase):
    def test_list_brains_reports_registered_and_unregistered_brains(self) -> None:
        with (
            tempfile.TemporaryDirectory() as home,
            tempfile.TemporaryDirectory() as registered_root,
        ):
            root = Path(registered_root)
            (root / "talamus.json").write_text("{}", encoding="utf-8")
            notes = root / "notes"
            notes.mkdir()
            (notes / "alpha.md").write_text("# Alpha", encoding="utf-8")
            register_brain(root, name="alpha", home=Path(home))
            unregistered = Path(home) / "loose"
            unregistered.mkdir()
            (unregistered / "talamus.json").write_text("{}", encoding="utf-8")

            report = list_brains(home=Path(home))

        self.assertTrue(report.success)
        self.assertIsNotNone(report.data)
        self.assertEqual("alpha", report.data.brains[0].name)
        self.assertTrue(report.data.brains[0].exists)
        self.assertEqual(1, report.data.brains[0].notes)
        self.assertEqual("loose", report.data.unregistered[0].name)
        self.assertIn("talamus brains register", report.data.unregistered[0].register_command)

    def test_register_select_rename_flags_unregister_flow_returns_results(self) -> None:
        with tempfile.TemporaryDirectory() as home, tempfile.TemporaryDirectory() as root:
            brain_root = Path(root)
            (brain_root / "talamus.json").write_text("{}", encoding="utf-8")

            registered = register_existing_brain(brain_root, name="alpha", home=Path(home))
            selected = select_registered_brain("alpha", home=Path(home))
            renamed = rename_registered_brain("alpha", "beta", home=Path(home))
            flagged = set_registered_brain_flags(
                "beta", federated=False, sensitive=True, home=Path(home)
            )
            info = get_brain("beta", home=Path(home))
            removed = unregister_registered_brain("beta", home=Path(home))
            registry = load_registry(Path(home))
            files_preserved = brain_root.exists()

        self.assertTrue(registered.success)
        self.assertEqual("brain_registered", registered.code)
        self.assertTrue(selected.success)
        self.assertEqual("brain_selected", selected.code)
        self.assertTrue(renamed.success)
        self.assertIsNotNone(renamed.data)
        self.assertEqual("beta", renamed.data.name)
        self.assertTrue(flagged.success)
        self.assertIsNotNone(flagged.data)
        self.assertFalse(flagged.data.federated)
        self.assertTrue(flagged.data.sensitive)
        self.assertTrue(info.success)
        self.assertTrue(removed.success)
        self.assertEqual([], registry.brains)
        self.assertTrue(files_preserved)

    def test_failures_are_service_results_and_do_not_mutate_registry(self) -> None:
        with (
            tempfile.TemporaryDirectory() as home,
            tempfile.TemporaryDirectory() as alpha_root,
            tempfile.TemporaryDirectory() as beta_root,
        ):
            register_brain(Path(alpha_root), name="alpha", home=Path(home))
            register_brain(Path(beta_root), name="beta", home=Path(home))
            before = (Path(home) / "registry.json").read_text(encoding="utf-8")

            missing = select_registered_brain("missing", home=Path(home))
            duplicate = rename_registered_brain("alpha", "beta", home=Path(home))
            invalid_type = register_existing_brain(
                alpha_root, name="gamma", brain_type="nonsense", home=Path(home)
            )
            empty_flags = set_registered_brain_flags("alpha", home=Path(home))
            after = (Path(home) / "registry.json").read_text(encoding="utf-8")

        self.assertFalse(missing.success)
        self.assertEqual("brain_not_found", missing.code)
        self.assertFalse(duplicate.success)
        self.assertEqual("brain_name_exists", duplicate.code)
        self.assertFalse(invalid_type.success)
        self.assertEqual("brain_type_invalid", invalid_type.code)
        self.assertFalse(empty_flags.success)
        self.assertEqual("brain_flags_empty", empty_flags.code)
        self.assertEqual(before, after)

    def test_wrong_shaped_registry_returns_failed_result(self) -> None:
        with tempfile.TemporaryDirectory() as home:
            registry_path = Path(home) / "registry.json"
            registry_path.write_text(json.dumps({"brains": [{"name": "broken"}]}), encoding="utf-8")

            report = list_brains(home=Path(home))
            info = get_brain("broken", home=Path(home))

        self.assertFalse(report.success)
        self.assertEqual("brain_registry_error", report.code)
        self.assertFalse(info.success)
        self.assertEqual("brain_registry_error", info.code)


if __name__ == "__main__":
    unittest.main()
