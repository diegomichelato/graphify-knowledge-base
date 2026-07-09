# ADR-0002: Dual-repository strategy with incremental synchronization

- **Date:** 2026-07-09
- **Status:** Accepted
- **Deciders:** Diego Michelato

## Context

The application repository (`elbruno/graphify-dotnet`, upstream — not ours to
modify) and the knowledge artifacts must evolve together without pushing
generated output into the application repo or rebuilding the graph from scratch
on every change.

## Decision

Maintain two synchronized repositories: the application repo holds source code,
tests, and docs; this knowledge repo holds the graph, wiki, Obsidian vault,
reports, ADRs, business knowledge, and changelog. Updates are incremental:
detect changed files → re-run graphify (semantic cache skips unchanged files) →
sync artifacts → auto-generate a changelog entry from the graph diff → commit →
push. Full rebuilds only on explicit request. Implemented in
`tools/update_knowledge.sh` and `tools/graph_changelog.py`.

## Consequences

- Upstream repo stays untouched; knowledge repo carries all derived knowledge.
- Every graph update is documented in CHANGELOG.md automatically.
- Node identifiers must remain stable across updates so ADR/business links don't break.
- Requires push credentials (short-lived PAT) at sync time.

## Links

- **Affected modules:** tools/
- **Business features:** business/product-knowledge.md
- **Implementation:** tools/update_knowledge.sh, tools/graph_changelog.py
- **Documentation:** CLAUDE.md (Knowledge graph maintenance)
