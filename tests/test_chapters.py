import unittest
from types import SimpleNamespace
from unittest.mock import MagicMock

from tools.fde_brain.chapters import Chapter, chapter_anchor, extract_chapters_from_pdf


def _outline_item(title: str, page: int) -> SimpleNamespace:
    return SimpleNamespace(title=title, page=page)


class ChapterAnchorTests(unittest.TestCase):
    def test_anchor_lowercases_and_dashes(self) -> None:
        self.assertEqual("chapter-3-replication", chapter_anchor("Chapter 3: Replication"))

    def test_anchor_strips_punctuation(self) -> None:
        self.assertEqual("foo-bar-baz", chapter_anchor("Foo, Bar; Baz!"))

    def test_anchor_collapses_whitespace(self) -> None:
        self.assertEqual("a-b-c", chapter_anchor("  a   b\tc  "))

    def test_anchor_keeps_alphanumeric_unicode(self) -> None:
        self.assertEqual("hello-world", chapter_anchor("Hello, World"))

    def test_anchor_empty_fallback(self) -> None:
        self.assertEqual("section", chapter_anchor("!!!"))


class ExtractChaptersTests(unittest.TestCase):
    def _make_reader(self, outline, num_pages: int) -> MagicMock:
        reader = MagicMock()
        reader.outline = outline
        reader.pages = [object()] * num_pages

        def _resolve(item):
            return item.page - 1  # pypdf returns 0-based

        reader.get_destination_page_number = MagicMock(side_effect=_resolve)
        return reader

    def test_flat_outline_returns_chapters_in_order(self) -> None:
        outline = [
            _outline_item("Introduction", 1),
            _outline_item("Chapter 1: Foo", 5),
            _outline_item("Chapter 2: Bar", 12),
        ]
        reader = self._make_reader(outline, num_pages=20)

        chapters = extract_chapters_from_pdf(reader)

        self.assertEqual(3, len(chapters))
        self.assertEqual("Introduction", chapters[0].title)
        self.assertEqual(1, chapters[0].page_start)
        self.assertEqual(4, chapters[0].page_end)
        self.assertEqual(5, chapters[1].page_start)
        self.assertEqual(11, chapters[1].page_end)
        self.assertEqual(12, chapters[2].page_start)
        self.assertEqual(20, chapters[2].page_end)

    def test_nested_outline_is_flattened_with_levels(self) -> None:
        sub_a = _outline_item("Section 1.1", 3)
        sub_b = _outline_item("Section 1.2", 7)
        outline = [
            _outline_item("Chapter 1", 1),
            [sub_a, sub_b],
            _outline_item("Chapter 2", 10),
        ]
        reader = self._make_reader(outline, num_pages=15)

        chapters = extract_chapters_from_pdf(reader)

        self.assertEqual(4, len(chapters))
        titles = [c.title for c in chapters]
        self.assertEqual(["Chapter 1", "Section 1.1", "Section 1.2", "Chapter 2"], titles)
        levels = [c.level for c in chapters]
        self.assertEqual([1, 2, 2, 1], levels)

    def test_empty_outline_returns_empty_list(self) -> None:
        reader = self._make_reader(outline=[], num_pages=5)
        self.assertEqual([], extract_chapters_from_pdf(reader))

    def test_chapter_anchor_field_is_set(self) -> None:
        outline = [_outline_item("Chapter 3: Replication", 1)]
        reader = self._make_reader(outline, num_pages=2)

        chapters = extract_chapters_from_pdf(reader)

        self.assertEqual("chapter-3-replication", chapters[0].anchor)

    def test_outline_items_with_unresolvable_page_are_skipped(self) -> None:
        good = _outline_item("Good", 1)
        bad = _outline_item("Bad", 99)
        outline = [good, bad]
        reader = MagicMock()
        reader.outline = outline
        reader.pages = [object()] * 5

        def _resolve(item):
            if item is bad:
                raise ValueError("no destination")
            return item.page - 1

        reader.get_destination_page_number = MagicMock(side_effect=_resolve)

        chapters = extract_chapters_from_pdf(reader)

        self.assertEqual(1, len(chapters))
        self.assertEqual("Good", chapters[0].title)


if __name__ == "__main__":
    unittest.main()
