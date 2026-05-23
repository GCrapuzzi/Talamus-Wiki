from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))


_VISUAL_SUBTYPES = {"/Image", "/Form"}


def _has_images_attr(page: Any) -> bool:
    images_attr = getattr(page, "images", None)
    if images_attr is None:
        return False
    try:
        return any(True for _ in images_attr)
    except TypeError:
        return bool(images_attr)


def _has_visual_xobject(page: Any) -> bool:
    try:
        resources = page.get("/Resources") if hasattr(page, "get") else page["/Resources"]
    except (KeyError, AttributeError, TypeError):
        return False
    if not resources:
        return False
    try:
        xobjects = resources.get("/XObject") if hasattr(resources, "get") else resources["/XObject"]
    except (KeyError, AttributeError, TypeError):
        return False
    if not xobjects:
        return False
    try:
        for _key, value in xobjects.items():
            subtype = None
            if hasattr(value, "get"):
                subtype = value.get("/Subtype")
            elif isinstance(value, dict):
                subtype = value.get("/Subtype")
            if subtype in _VISUAL_SUBTYPES:
                return True
    except (AttributeError, TypeError):
        return False
    return False


def page_has_visual_content(page: Any) -> bool:
    try:
        if _has_images_attr(page):
            return True
    except Exception:
        pass
    try:
        return _has_visual_xobject(page)
    except Exception:
        return False
