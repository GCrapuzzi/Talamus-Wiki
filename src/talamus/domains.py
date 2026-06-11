"""Domain induction (hybrid): structural clusters from the typed graph, then the LLM
names and refines them into thematic domains that cover every note.

The structural pass groups notes connected by typed relations; the LLM pass turns
those clusters into named domains and assigns the strays. The result is the
**overview**: a small, ~constant-size map the LLM can route over.
"""

from __future__ import annotations

import json
import re

from talamus.adapters.llm import LLMProvider
from talamus.models import CanonicalNote
from talamus.ontology import load_ontology, neighbors
from talamus.paths import TalamusPaths
from talamus.store import load_notes

_PROMPT = """You are a librarian. The NOTES are pre-grouped by connections (CLUSTERS).
Turn them into clear thematic DOMAINS covering ALL the notes.
- Give each domain a short name and a one-sentence description, in <LANGUAGE>.
- Assign each note to EXACTLY ONE domain (you may merge small clusters, or move a
  note to a different domain if it fits better thematically).
- Every note must end up in exactly one domain.

Return ONLY a JSON array:
[{"name": "<name>", "description": "<one sentence>", "members": ["<title>", "<title>"]}]

CLUSTERS (existing connections):
<CLUSTERS>

NOTES (title: summary):
<SUMMARIES>
"""


def _structural_clusters(notes: list[CanonicalNote], ontology: dict) -> list[list[str]]:
    titles = [note.title for note in notes]
    title_set = set(titles)
    parent: dict[str, str] = {title: title for title in titles}

    def find(node: str) -> str:
        while parent[node] != node:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node

    def union(a: str, b: str) -> None:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    for title in titles:
        for neighbor in neighbors(ontology, title):
            other = str(neighbor.get("title", ""))
            if other in title_set:
                union(title, other)

    clusters: dict[str, list[str]] = {}
    for title in titles:
        clusters.setdefault(find(title), []).append(title)
    return list(clusters.values())


def _name_domains(
    clusters: list[list[str]],
    summaries: dict[str, str],
    llm: LLMProvider,
    language: str = "English",
) -> list[dict]:
    cluster_text = "\n".join(f"- {', '.join(cluster)}" for cluster in clusters)
    summary_text = "\n".join(f"- {title}: {summary}" for title, summary in summaries.items())
    raw = llm.complete(
        _PROMPT.replace("<CLUSTERS>", cluster_text)
        .replace("<SUMMARIES>", summary_text)
        .replace("<LANGUAGE>", language)
    )
    start, end = raw.find("["), raw.rfind("]")
    parsed: list = []
    if start != -1 and end != -1 and end > start:
        try:
            parsed = json.loads(raw[start : end + 1])
        except json.JSONDecodeError:
            parsed = []

    domains: list[dict] = []
    assigned: set[str] = set()
    for entry in parsed:
        if not isinstance(entry, dict):
            continue
        members = [m for m in entry.get("members", []) if m in summaries and m not in assigned]
        if not members:
            continue
        assigned.update(members)
        domains.append(
            {
                "name": str(entry.get("name", "")).strip() or "Dominio",
                "description": str(entry.get("description", "")).strip(),
                "members": members,
            }
        )

    leftover = [title for title in summaries if title not in assigned]
    if leftover:
        domains.append(
            {"name": "Varie", "description": "Schede non ancora classificate.", "members": leftover}
        )
    return domains


def build_overview(paths: TalamusPaths, llm: LLMProvider) -> list[dict]:
    """Induce the domains and persist the overview. Returns the domain list."""
    from talamus.config import load_or_default, resolve_language

    notes = load_notes(paths)
    if not notes:
        return []
    clusters = _structural_clusters(notes, load_ontology(paths))
    summaries = {note.title: note.summary for note in notes}
    language = resolve_language(load_or_default(paths.config_path))
    domains = _name_domains(clusters, summaries, llm, language=language)
    save_overview(paths, domains)
    return domains


def _domain_id(name: str, taken: set[str]) -> str:
    base = "dom-" + (re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-") or "x")
    candidate = base
    suffix = 2
    while candidate in taken:
        candidate = f"{base}-{suffix}"
        suffix += 1
    return candidate


def save_overview(paths: TalamusPaths, domains: list[dict]) -> None:
    """Persist the overview, ensuring every domain carries a stable ``id`` (F3.8)
    separate from its human name — routing talks ids, never substring-matched names."""
    taken: set[str] = {str(d["id"]) for d in domains if d.get("id")}
    for domain in domains:
        if not domain.get("id"):
            domain["id"] = _domain_id(str(domain.get("name", "")), taken)
            taken.add(domain["id"])
    paths.cache.mkdir(parents=True, exist_ok=True)
    paths.overview_file.write_text(
        json.dumps(domains, indent=2, ensure_ascii=False), encoding="utf-8"
    )


def load_overview(paths: TalamusPaths) -> list[dict]:
    if not paths.overview_file.is_file():
        return []
    return json.loads(paths.overview_file.read_text(encoding="utf-8"))


# ---------------------------------------------------------- hierarchical tree

TREE_THRESHOLD = 12  # below this many domains, flat routing is already cheap

_TREE_PROMPT = """You are a librarian. Group the DOMAINS into 3-9 thematic MACRO-AREAS.
Every domain must belong to exactly one macro-area. Name and describe each area in
<LANGUAGE>. Return ONLY a JSON array:
[{"name": "<short name>", "description": "<one sentence>", "children": ["<domain id>", ...]}]

DOMAINS (id | name: description):
<DOMAINS>
"""


def tree_path(paths: TalamusPaths):
    return paths.cache / "overview-tree.json"


def build_overview_tree(paths: TalamusPaths, llm: LLMProvider) -> list[dict]:
    """Second overview level (Fase R5): macro-areas over the domains, so routing
    cost stays ~log(N) instead of growing linearly with the domain count.
    One extra LLM call, only when the flat map is big enough to need it."""
    overview = load_overview(paths)
    if len(overview) < TREE_THRESHOLD:
        tree_path(paths).unlink(missing_ok=True)
        return []
    from talamus.config import load_or_default, resolve_language

    domain_lines = "\n".join(
        f"- {d.get('id', '?')} | {d.get('name', '')}: {d.get('description', '')}" for d in overview
    )
    language = resolve_language(load_or_default(paths.config_path))
    raw = llm.complete(
        _TREE_PROMPT.replace("<DOMAINS>", domain_lines).replace("<LANGUAGE>", language)
    )
    start, end = raw.find("["), raw.rfind("]")
    parsed: list = []
    if start != -1 and end != -1 and end > start:
        try:
            parsed = json.loads(raw[start : end + 1])
        except json.JSONDecodeError:
            parsed = []
    valid_ids = {str(d["id"]) for d in overview if d.get("id")}
    areas: list[dict] = []
    assigned: set[str] = set()
    taken: set[str] = set()
    for entry in parsed:
        if not isinstance(entry, dict):
            continue
        children = [c for c in entry.get("children", []) if c in valid_ids and c not in assigned]
        if not children:
            continue
        assigned.update(children)
        slug = re.sub(r"[^a-z0-9]+", "-", str(entry.get("name", "")).lower()).strip("-") or "x"
        area_id = f"area-{slug}"
        suffix = 2
        while area_id in taken:
            area_id = f"area-{slug}-{suffix}"
            suffix += 1
        taken.add(area_id)
        areas.append(
            {
                "id": area_id,
                "name": str(entry.get("name", "")).strip() or "Area",
                "description": str(entry.get("description", "")).strip(),
                "children": children,
            }
        )
    leftover = [str(d["id"]) for d in overview if d.get("id") and d["id"] not in assigned]
    if leftover:
        altro_id = "area-altro"
        suffix = 2
        while altro_id in taken:
            altro_id = f"area-altro-{suffix}"
            suffix += 1
        areas.append(
            {
                "id": altro_id,
                "name": "Altro",
                "description": "Domini non ancora raggruppati.",
                "children": leftover,
            }
        )
    paths.cache.mkdir(parents=True, exist_ok=True)
    tree_path(paths).write_text(json.dumps(areas, indent=2, ensure_ascii=False), encoding="utf-8")
    return areas


def load_overview_tree(paths: TalamusPaths) -> list[dict]:
    path = tree_path(paths)
    if not path.is_file():
        return []
    return json.loads(path.read_text(encoding="utf-8"))
