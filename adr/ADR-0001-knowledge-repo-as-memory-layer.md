# ADR-0001: Use a Graphify knowledge repository as the permanent memory layer

- **Date:** 2026-07-09
- **Status:** Accepted
- **Deciders:** Diego Michelato

## Context

AI-assisted work on `elbruno/graphify-dotnet` re-read the repository on every
conversation (~108k tokens per full read). Sessions are ephemeral, so all
architectural understanding evaporated between conversations.

## Decision

Generate a knowledge graph of the codebase with `graphify-dotnet` (AST extraction,
1,620 nodes / 2,852 edges) and persist it — graph.json, interactive HTML, wiki,
Obsidian vault, and structural report — in a dedicated private repository
(`diegomichelato/graphify-knowledge-base`). All AI agents must query this graph
before reading source code, per `CLAUDE.md`.

## Consequences

- Per-question cost drops from ~108k tokens to ~43 tokens (~2,500× measured by `graphify benchmark`).
- Knowledge survives across sessions and machines.
- The graph must be kept in sync with code changes (see ADR-0002 and `tools/update_knowledge.sh`).
- AST-only extraction misses cross-file semantics until an AI provider is configured.

## Links

- **Affected modules:** entire graph
- **Business features:** business/product-knowledge.md
- **Implementation:** graph.json, wiki/, obsidian/, GRAPH_REPORT.md, tools/
- **Documentation:** README.md, CLAUDE.md
