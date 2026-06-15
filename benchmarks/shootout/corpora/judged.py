"""Adapt a BEIR dataset into our JudgedCorpus. Network access is isolated in
load_beir; beir_to_corpus is pure and unit-tested."""

from __future__ import annotations

import json
import urllib.request
import zipfile
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class JudgedCorpus:
    docs: list[tuple[str, str, str]]  # (doc_id, title, text)
    queries: dict[str, str]  # query_id -> text
    qrels: dict[str, dict[str, int]]  # query_id -> {doc_id: grade}

    @property
    def n_docs(self) -> int:
        return len(self.docs)

    def as_docs(self) -> list:
        from benchmarks.shootout.systems.base import Doc  # late import: stay dep-free

        return [Doc(doc_id, title, text) for doc_id, title, text in self.docs]


def corpus_from_brain(brain_path: str, eval_path: str) -> JudgedCorpus:
    """Build a JudgedCorpus from a real Talamus brain + an eval-cases file.

    Each note becomes one doc (id = title) carrying its enriched search text
    (title + summary + retrieval_text, which includes symptom phrasings), so
    every system retrieves over IDENTICAL content — this isolates the retrieval
    method on Talamus's own turf (cross-language + vague queries). Relevance =
    the eval cases' relevant titles. Copyright-safe: only used locally; reports
    publish aggregates, never the text."""
    import json as _json
    from pathlib import Path as _Path

    from talamus.paths import TalamusPaths
    from talamus.store import load_notes

    notes = load_notes(TalamusPaths(_Path(brain_path)))
    docs = [(n.title, n.title, f"{n.title} {n.summary} {n.retrieval_text}".strip()) for n in notes]
    titles = {n.title for n in notes}
    data = _json.loads(_Path(eval_path).read_text(encoding="utf-8"))
    cases = data["cases"] if isinstance(data, dict) else data
    queries: dict[str, str] = {}
    qrels: dict[str, dict[str, int]] = {}
    for case in cases:
        relevant = [t for t in case.get("relevant", []) if t in titles]
        if not relevant:  # negatives or unmatched titles can't be scored for recall
            continue
        qid = str(case.get("id") or case.get("question", ""))
        queries[qid] = case["question"]
        qrels[qid] = dict.fromkeys(relevant, 1)
    return JudgedCorpus(docs=docs, queries=queries, qrels=qrels)


def beir_to_corpus(
    corpus: dict[str, dict], queries: dict[str, str], qrels: dict[str, dict[str, int]]
) -> JudgedCorpus:
    """Pure adapter from BEIR's in-memory shape to JudgedCorpus. Drops queries
    that have no relevance judgments (they cannot be scored)."""
    judged_q = {qid: text for qid, text in queries.items() if qrels.get(qid)}
    docs = [(doc_id, d.get("title", ""), d.get("text", "")) for doc_id, d in corpus.items()]
    return JudgedCorpus(docs=docs, queries=judged_q, qrels={q: qrels[q] for q in judged_q})


_BEIR_URL = "https://public.ukp.informatik.tu-darmstadt.de/thakur/BEIR/datasets/{name}.zip"


def _download_beir(name: str, root: Path) -> Path:
    """Download + unzip a BEIR dataset (once). Returns the dataset folder."""
    data_path = root / name
    if data_path.is_dir():
        return data_path
    root.mkdir(parents=True, exist_ok=True)
    zip_path = root / f"{name}.zip"
    urllib.request.urlretrieve(_BEIR_URL.format(name=name), zip_path)  # noqa: S310 (trusted host)
    with zipfile.ZipFile(zip_path) as zf:
        zf.extractall(root)
    zip_path.unlink(missing_ok=True)
    return data_path


def _read_jsonl(path: Path) -> dict[str, dict]:
    out: dict[str, dict] = {}
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                row = json.loads(line)
                out[str(row["_id"])] = row
    return out


def load_beir(
    name: str = "scifact", data_root: str = ".bench-data", split: str = "test"
) -> JudgedCorpus:
    """Download (once) and load a BEIR dataset as a JudgedCorpus.

    Lightweight: reads the BEIR file format (corpus.jsonl, queries.jsonl,
    qrels/<split>.tsv) directly with the stdlib — no torch / beir package."""
    data_path = _download_beir(name, Path(data_root))
    corpus_rows = _read_jsonl(data_path / "corpus.jsonl")
    corpus = {
        doc_id: {"title": row.get("title", ""), "text": row.get("text", "")}
        for doc_id, row in corpus_rows.items()
    }
    query_rows = _read_jsonl(data_path / "queries.jsonl")
    queries = {qid: row.get("text", "") for qid, row in query_rows.items()}
    qrels: dict[str, dict[str, int]] = {}
    qrels_file = data_path / "qrels" / f"{split}.tsv"
    with qrels_file.open(encoding="utf-8") as handle:
        next(handle)  # header: query-id\tcorpus-id\tscore
        for line in handle:
            parts = line.split()
            if len(parts) >= 3:
                qid, doc_id, score = parts[0], parts[1], int(parts[2])
                if score > 0:
                    qrels.setdefault(qid, {})[doc_id] = score
    return beir_to_corpus(corpus, queries, qrels)
