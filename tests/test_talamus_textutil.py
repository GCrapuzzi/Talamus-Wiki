import unittest

from talamus.textutil import tokens


class TextUtilTests(unittest.TestCase):
    def test_stemming_unifies_italian_inflections(self) -> None:
        self.assertEqual(tokens("spezzare"), tokens("spezza"))
        self.assertEqual(tokens("documenti"), tokens("documento"))
        self.assertEqual(tokens("piccoli"), tokens("piccole"))

    def test_keeps_short_or_unsuffixed_words(self) -> None:
        self.assertEqual(["rag"], tokens("RAG"))
        self.assertEqual(["vector"], tokens("vector"))


if __name__ == "__main__":
    unittest.main()
