# Business & Product Knowledge — graphify-dotnet

> Non-code knowledge layer. Source: project README, docs/, and session decisions.
> Extend this file (and siblings in `business/`) whenever business context is learned.

## Product purpose

Build AI-powered knowledge graphs from any codebase so developers navigate by
structure instead of keyword search. .NET 10 port of `safishamsi/graphify`,
inspired by Karpathy's LLM-personal-knowledge-base idea.

## Customer value

- Understand unfamiliar codebases quickly (interactive graph, wiki, communities).
- Slash LLM token costs: ~43 tokens per graph query vs ~108k for a full corpus read (~2,500×).
- Zero-config entry: AST-only extraction works with no AI provider, no account, no keys.

## Features

| Feature | Notes |
|---|---|
| Extraction pipeline | 6 stages: detect → extract (AST + optional AI) → build graph → detect communities → analyze → export |
| 28+ file types | code (18 languages), config (YAML/JSON/TOML/XML), docs (md/txt/rst/adoc), media (PDF/PNG/JPEG/WebP/GIF/SVG) |
| Export formats | json, html (interactive vis), svg, neo4j, ladybug, obsidian, wiki, report |
| AI providers | Azure OpenAI, Ollama (local), Copilot SDK — all optional |
| Watch mode | re-processes on file change with debounce |
| Benchmark | measures token reduction of graph-vs-corpus queries |
| MCP server | `Graphify.Mcp` exposes graph query tools to AI agents |
| Config wizard | `graphify config` — provider setup, folder defaults, secrets in user-secrets store |

## Deployment / distribution

- NuGet: `graphify-dotnet` (global tool `graphify`), `graphify-dotnet-core`, `graphify-dotnet-sdk`.
- Requires .NET 10 SDK (`global.json`: 10.0.100, rollForward latestMajor).
- CI: GitHub Actions (build.yml, publish.yml).

## Configuration knowledge

- Provider precedence: CLI args > local config > user secrets (see ConfigurationFactory tests).
- API keys go to the user-secrets store, never plain config files.
- Default Ollama endpoint: localhost; default Copilot model: gpt-4.1.

## Engineering standards (observed in the codebase)

- Heavy security posture: input validation, path-traversal blocks, Cypher/XSS
  sanitization in every exporter, LLM-response validation, private-IP URL blocking.
- Regression tests named for specific bugs (RegressionBug1–3: cache deadlock,
  label sanitization, test timeouts).
- Tests outnumber production code roughly 2:1; every exporter has a dedicated suite.

## Operational procedures (this knowledge system)

- Update after code changes: `tools/update_knowledge.sh <app-repo> "<note>"`, then push.
- Health check: `python3 tools/graph_health.py [--source <app-repo>]`.
- Impact analysis before changes: `python3 tools/graph_impact.py <node>`.
- Decisions → `adr/`; graph diffs → `CHANGELOG.md` (auto-generated).

## Roadmap items

- Upstream roadmap lives in ROADMAP.md of the application repo (not yet mirrored here — enrich on next read).
- This knowledge system: wire an AI provider for the semantic layer (see CLAUDE.md "Future AI provider").
