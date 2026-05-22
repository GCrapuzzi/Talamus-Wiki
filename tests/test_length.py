import unittest
from types import SimpleNamespace
from unittest.mock import MagicMock

from tools.fde_brain.length import is_long_pdf


def _reader(*, outline_titles: list[str], num_pages: int):
    reader = MagicMock()
    reader.pages = [object()] * num_pages
    reader.outline = [SimpleNamespace(title=t, page=i + 1) for i, t in enumerate(outline_titles)]
    reader.get_destination_page_number = MagicMock(side_effect=lambda item: item.page - 1)
    return reader


class IsLongPdfTests(unittest.TestCase):
    def test_long_when_outline_meets_chapter_threshold(self) -> None:
        r = _reader(outline_titles=["A", "B", "C"], num_pages=10)
        self.assertTrue(is_long_pdf(r))

    def test_long_when_pages_exceed_threshold(self) -> None:
        r = _reader(outline_titles=[], num_pages=80)
        self.assertTrue(is_long_pdf(r))

    def test_short_when_few_chapters_and_few_pages(self) -> None:
        r = _reader(outline_titles=["A"], num_pages=10)
        self.assertFalse(is_long_pdf(r))

    def test_thresholds_are_overridable(self) -> None:
        r = _reader(outline_titles=["A", "B"], num_pages=30)
        self.assertTrue(is_long_pdf(r, min_chapters=2, min_pages=999))
        self.assertFalse(is_long_pdf(r, min_chapters=5, min_pages=999))

    def test_outline_threshold_uses_resolvable_entries_only(self) -> None:
        # 4 outline items but 2 fail to resolve -> only 2 valid chapters
        bad = SimpleNamespace(title="Bad", page=999)
        good_outline = [SimpleNamespace(title=f"Ch{i}", page=i + 1) for i in range(2)]
        outline = good_outline + [bad, bad]
        reader = MagicMock()
        reader.pages = [object()] * 10
        reader.outline = outline

        def _resolve(item):
            if item is bad:
                raise ValueError("nope")
            return item.page - 1

        reader.get_destination_page_number = MagicMock(side_effect=_resolve)

        self.assertFalse(is_long_pdf(reader, min_chapters=3, min_pages=20))


if __name__ == "__main__":
    unittest.main()
