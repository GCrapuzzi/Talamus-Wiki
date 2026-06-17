import tempfile
import unittest
from pathlib import Path

from talamus.paths import TalamusPaths
from talamus.review import ReviewQueue
from talamus.services.review import (
    apply_review_item,
    get_review_item,
    list_review_items,
    reject_review_item,
)


class ReviewServiceTests(unittest.TestCase):
    def test_list_show_apply_and_reject_review_items(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            queue = ReviewQueue(TalamusPaths(root))
            apply_item = queue.add("low_confidence_note", "Nota dubbia", {"why": "low"})
            reject_item = queue.add("scan_safety", "Secret candidate", {"path": "x"})

            listed = list_review_items(root)
            shown = get_review_item(root, apply_item.item_id)
            applied = apply_review_item(root, apply_item.item_id)
            rejected = reject_review_item(root, reject_item.item_id, "not a secret")
            pending_after = list_review_items(root)
            all_after = list_review_items(root, status=None)

        self.assertTrue(listed.success)
        self.assertIsNotNone(listed.data)
        self.assertEqual(2, len(listed.data))
        self.assertTrue(shown.success)
        self.assertEqual("Nota dubbia", shown.data.title)
        self.assertTrue(applied.success)
        self.assertEqual("applied", applied.data.status)
        self.assertTrue(rejected.success)
        self.assertEqual("rejected", rejected.data.status)
        self.assertEqual("not a secret", rejected.data.resolution)
        self.assertTrue(pending_after.success)
        self.assertEqual([], pending_after.data)
        self.assertTrue(all_after.success)
        self.assertEqual(2, len(all_after.data))

    def test_missing_and_non_pending_items_return_failed_results(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            queue = ReviewQueue(TalamusPaths(root))
            item = queue.add("stale_source", "Fonte cambiata", {})
            queue.reject(item.item_id)
            correction = queue.add("correction", "Already decided correction", {"title": "Missing"})
            queue.reject(correction.item_id)

            missing = get_review_item(root, "missing")
            not_pending = apply_review_item(root, item.item_id)
            not_pending_correction = apply_review_item(root, correction.item_id)

        self.assertFalse(missing.success)
        self.assertEqual("review_item_not_found", missing.code)
        self.assertFalse(not_pending.success)
        self.assertEqual("review_item_not_pending", not_pending.code)
        self.assertFalse(not_pending_correction.success)
        self.assertEqual("review_item_not_pending", not_pending_correction.code)

    def test_wrong_shaped_review_item_returns_failed_result(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            review_dir = TalamusPaths(root).cache / "review"
            review_dir.mkdir(parents=True)
            (review_dir / "bad.json").write_text("[]", encoding="utf-8")

            listed = list_review_items(root)
            shown = get_review_item(root, "bad")
            applied = apply_review_item(root, "bad")
            rejected = reject_review_item(root, "bad")

        self.assertFalse(listed.success)
        self.assertEqual("review_store_error", listed.code)
        self.assertFalse(shown.success)
        self.assertEqual("review_store_error", shown.code)
        self.assertFalse(applied.success)
        self.assertEqual("review_store_error", applied.code)
        self.assertFalse(rejected.success)
        self.assertEqual("review_store_error", rejected.code)

    def test_missing_correction_target_does_not_resolve_review_item(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            queue = ReviewQueue(TalamusPaths(root))
            item = queue.add("correction", "Missing note correction", {"title": "Missing"})

            result = apply_review_item(root, item.item_id)
            kept = queue.get(item.item_id)

        self.assertFalse(result.success)
        self.assertEqual("review_correction_target_missing", result.code)
        self.assertEqual("pending", kept.status)


if __name__ == "__main__":
    unittest.main()
