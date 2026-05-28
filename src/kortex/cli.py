from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from kortex.ask import build_context_bundle
from kortex.config import KortexConfig, load_config, save_config
from kortex.graph import load_graph, query_graph
from kortex.paths import KortexPaths
from kortex.search import BM25Index


def _cmd_init(root: Path) -> int:
    paths = KortexPaths(root)
    paths.ensure_directories()
    if not paths.config_path.exists():
        save_config(paths.config_path, KortexConfig.default())
    print(f"initialized kortex project at {root}")
    return 0


def _cmd_status(root: Path) -> int:
    paths = KortexPaths(root)
    missing = [p for p in paths.required_directories() if not p.exists()]
    not_directories = [p for p in paths.required_directories() if p.exists() and not p.is_dir()]
    config_exists = paths.config_path.exists()
    if missing or not_directories or not config_exists:
        if not config_exists:
            print(f"missing config: {paths.config_path}", file=sys.stderr)
        for path in missing:
            print(f"missing directory: {path}", file=sys.stderr)
        for path in not_directories:
            print(f"not a directory: {path}", file=sys.stderr)
        return 1
    print("kortex project status ok")
    return 0


def _cmd_doctor(root: Path) -> int:
    paths = KortexPaths(root)
    if not paths.config_path.exists():
        print("kortex project is not initialized; run `kortex init`", file=sys.stderr)
        return 1
    try:
        config = load_config(paths.config_path)
    except Exception as exc:
        print(f"config error: {paths.config_path}: {exc}", file=sys.stderr)
        return 1
    print(f"storage: {config.storage_provider}")
    print(f"pdf converter: {config.pdf_converter}")
    print(f"ocr: {config.ocr_provider}/{config.ocr_model}")
    print(f"llm: {config.llm_provider}")
    print(f"graph: {config.graph_provider}")
    print(f"search: {config.search_provider}")
    return 0


def _load_required_graph(paths: KortexPaths) -> dict | None:
    graph_path = paths.graph / "graph.json"
    if not graph_path.is_file():
        print(f"missing graph: {graph_path}", file=sys.stderr)
        return None
    return load_graph(graph_path)


def _load_optional_search(paths: KortexPaths) -> BM25Index:
    index_path = paths.index / "bm25.json"
    if not index_path.is_file():
        return BM25Index()
    return BM25Index.load(index_path)


def _cmd_graph_query(root: Path, question: str) -> int:
    paths = KortexPaths(root)
    graph = _load_required_graph(paths)
    if graph is None:
        return 1
    print(json.dumps(query_graph(graph, question), indent=2))
    return 0


def _cmd_search(root: Path, query: str) -> int:
    paths = KortexPaths(root)
    index_path = paths.index / "bm25.json"
    if not index_path.is_file():
        print(f"missing search index: {index_path}", file=sys.stderr)
        return 1
    print(json.dumps(BM25Index.load(index_path).search(query), indent=2))
    return 0


def _cmd_ask_context(root: Path, question: str) -> int:
    paths = KortexPaths(root)
    graph = _load_required_graph(paths)
    if graph is None:
        return 1
    bundle = build_context_bundle(paths, graph, _load_optional_search(paths), question)
    if not bundle.items:
        print("no context found", file=sys.stderr)
        return 1
    print(bundle.render())
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="kortex", description="Local-first knowledge compiler.")
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("init", "status", "doctor"):
        cmd = sub.add_parser(name)
        cmd.add_argument("--root", default=".", help="Project root. Defaults to current directory.")

    ask = sub.add_parser("ask")
    ask_sub = ask.add_subparsers(dest="ask_command", required=True)
    ask_context = ask_sub.add_parser("context")
    ask_context.add_argument("question")
    ask_context.add_argument("--root", default=".")

    graph = sub.add_parser("graph")
    graph_sub = graph.add_subparsers(dest="graph_command", required=True)
    graph_query = graph_sub.add_parser("query")
    graph_query.add_argument("question")
    graph_query.add_argument("--root", default=".")

    search = sub.add_parser("search")
    search.add_argument("query")
    search.add_argument("--root", default=".")

    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = Path(args.root).resolve()
    if args.command == "init":
        return _cmd_init(root)
    if args.command == "status":
        return _cmd_status(root)
    if args.command == "doctor":
        return _cmd_doctor(root)
    if args.command == "graph" and args.graph_command == "query":
        return _cmd_graph_query(root, args.question)
    if args.command == "search":
        return _cmd_search(root, args.query)
    if args.command == "ask" and args.ask_command == "context":
        return _cmd_ask_context(root, args.question)
    raise ValueError(f"unknown command {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
