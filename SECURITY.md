# Security Policy

Talamus is **local-first**: your brain (notes, sources, indexes) lives on your
machine, under your project directory. Nothing is sent anywhere except to the
**LLM engine you configure** (e.g. your local `claude` CLI, a local Ollama model,
or an API you opt into).

## Posture

- **No network by default.** The core does no network I/O. The only outbound
  calls are to the LLM engine you choose.
- **MCP exposure is local.** The MCP server runs over **stdio** by default. The
  optional HTTP transport binds to **`127.0.0.1`** (localhost) only — it is not
  exposed to your network or the internet.
- **No remote endpoint yet.** Exposing the brain to browser-based LLMs would
  require a remote endpoint; that is deliberately **out of scope** and, when
  built, will be **authenticated and read-only** (see the out-of-scope list in
  `dev/PRODUCT.md`).
- **Secrets.** Talamus does not store API keys in the brain. Provide engine
  credentials via environment variables; they are not written to logs.
- **Your data is yours.** Deleting the project directory deletes the brain.

## Reporting a vulnerability

Please open a private report (or email the maintainers) with steps to reproduce.
Do not file public issues for security-sensitive reports until a fix is available.
