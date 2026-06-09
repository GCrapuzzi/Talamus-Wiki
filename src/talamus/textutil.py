"""Light text utilities: tokenization with a small Italian stemmer.

Retrieval tokenized on raw words misses inflections: a query for "spezzare" would
not match a note that says "spezza". A light suffix-stripping stemmer collapses the
common Italian (and incidentally English) inflections so the two meet. It is applied
symmetrically to both the indexed text and the query.
"""

from __future__ import annotations

import re

_TOKEN = re.compile(r"[a-z0-9][a-z0-9-]{2,}")

# Tried longest-first; never strips below a 3-character stem.
_SUFFIXES = (
    "amento",
    "azione",
    "zione",
    "mente",
    "abile",
    "ibile",
    "ista",
    "ismo",
    "are",
    "ere",
    "ire",
    "ato",
    "ata",
    "ati",
    "ate",
    "ito",
    "ita",
    "iti",
    "ite",
    "oso",
    "osa",
    "osi",
    "ose",
    "ico",
    "ica",
    "ici",
    "iche",
    "che",
    "ghe",
    "i",
    "e",
    "o",
    "a",
)


def _stem(word: str) -> str:
    for suffix in _SUFFIXES:
        if word.endswith(suffix) and len(word) - len(suffix) >= 3:
            return word[: -len(suffix)]
    return word


def tokens(text: str) -> list[str]:
    """Lowercase word tokens, lightly stemmed."""
    return [_stem(match) for match in _TOKEN.findall(text.lower())]
