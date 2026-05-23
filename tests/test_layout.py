import unittest
from types import SimpleNamespace
from unittest.mock import MagicMock

from tools.fde_brain.layout import page_has_visual_content


class PageHasVisualContentTests(unittest.TestCase):
    def test_returns_true_when_page_images_iterable_yields(self) -> None:
        page = MagicMock()
        page.images = [SimpleNamespace(name="im1")]  # truthy list

        self.assertTrue(page_has_visual_content(page))

    def test_returns_false_when_page_images_empty_list(self) -> None:
        page = MagicMock()
        page.images = []

        # Also no /XObject in resources
        page.get = MagicMock(return_value={})

        self.assertFalse(page_has_visual_content(page))

    def test_falls_back_to_xobject_dict_when_images_attr_missing(self) -> None:
        page = {}  # plain dict-like

        class PageDict(dict):
            pass

        page = PageDict()
        page["/Resources"] = {"/XObject": {"/Im1": {"/Subtype": "/Image"}}}

        self.assertTrue(page_has_visual_content(page))

    def test_xobject_form_subtype_also_counts(self) -> None:
        page = {"/Resources": {"/XObject": {"/F1": {"/Subtype": "/Form"}}}}
        self.assertTrue(page_has_visual_content(page))

    def test_xobject_unknown_subtype_does_not_count(self) -> None:
        page = {"/Resources": {"/XObject": {"/Other": {"/Subtype": "/PostScript"}}}}
        self.assertFalse(page_has_visual_content(page))

    def test_resources_missing_returns_false(self) -> None:
        page = {}
        self.assertFalse(page_has_visual_content(page))

    def test_swallows_exceptions_and_returns_false(self) -> None:
        page = MagicMock()
        # Make page.images raise
        type(page).images = property(lambda _self: (_ for _ in ()).throw(RuntimeError("boom")))
        page.get = MagicMock(side_effect=RuntimeError("also fails"))

        self.assertFalse(page_has_visual_content(page))


if __name__ == "__main__":
    unittest.main()
