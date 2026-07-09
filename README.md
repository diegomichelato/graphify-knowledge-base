# graphify-knowledge-base

A persistent knowledge graph of [elbruno/graphify-dotnet](https://github.com/elbruno/graphify-dotnet), generated with [graphify-dotnet](https://www.nuget.org/packages/graphify-dotnet) v0.7.0. This repository is the **memory layer** for AI-assisted work on that codebase: instead of re-scanning the repository on every conversation, Claude (or any LLM agent) queries this graph first and only falls back to source files when the graph lacks the answer.

## Contents

| File / folder | What it is | How it's used |
|---|---|---|
| `graph.json` | The full knowledge graph: 1,620 nodes, 2,852 edges, 167 communities. Every node carries id, label, type, source file, and community assignment. | Primary machine-readable store. Query it with `jq` or any JSON tooling. |
| `wiki/` | 173 auto-generated Markdown articles: `index.md` plus one article per community and per highly-connected node. | Human- and LLM-readable entry point. Start at `wiki/index.md`. |
| `obsidian/` | An Obsidian vault with one note per node, cross-linked with `[[wiki-links]]`. | Open the folder as a vault in Obsidian to navigate the graph visually. |
| `graph.html` | Self-contained interactive visualization (vis.js). | Open in any browser; search, zoom, and click nodes to explore. |
| `GRAPH_REPORT.md` | Structural analysis: god nodes, communities with cohesion scores, knowledge gaps, suggested questions. | Quick orientation for a new contributor or a fresh LLM session. |

## Using the graph as Claude's memory layer

Paste this (or add it to your project's `CLAUDE.md` / system prompt) at the start of a session:

```
This project has a pre-built knowledge graph at <path-or-url-to>/graphify-knowledge-base.
For every request:
1. Query the knowledge graph FIRST (graph.json, or the wiki/ articles).
2. Only read source files when the graph lacks enough information.
3. If code changes, re-run `graphify run` on the changed project and update
   only the affected outputs — never rebuild everything unless asked.
Treat the graph as the primary source of truth; the repository is secondary.
```

### Example queries against `graph.json`

```bash
# Find a node by name
jq '.nodes[] | select(.label | test("PipelineRunner"))' graph.json

# Everything connected to a node
jq --arg id "pipelinerunner" '.edges[] | select(.source==$id or .target==$id)' graph.json

# All nodes in one community
jq '.nodes[] | select(.community==44) | .label' graph.json

# All files in the graph
jq -r '.nodes[] | select(.type=="file") | .label' graph.json | sort -u
```

### Why this saves tokens

Reading the full corpus costs ~108,000 tokens. A targeted graph query costs ~43 tokens — a **~2,500× reduction per question** (measured with `graphify benchmark graph.json`).

## Provenance and freshness

- **Source:** `elbruno/graphify-dotnet` @ commit `02b8276` (main, 2026-07-09)
- **Extraction mode:** AST-only (no AI provider). Structural facts — classes, methods, imports, file relationships — are 100% extracted, 0% inferred. Semantic enrichment (purpose, business logic, design decisions) requires re-running with an AI provider (`graphify run -p azureopenai|ollama|copilotsdk`).
- **Regenerating:** `dotnet tool install -g graphify-dotnet && graphify run <repo> -f json,html,wiki,report,obsidian`. The semantic cache means unchanged files are not reprocessed.

## Known gaps (from GRAPH_REPORT.md)

- `squad.config.ts` is isolated — no edges, undocumented.
- AST-only extraction does not resolve cross-file call graphs; test↔production and CLI↔pipeline relationships exist only semantically. Re-running with an AI provider fills this in.
- Community labels are auto-generated placeholders ("Entity (Community N)") until a semantic pass names them.

---

*Generated 2026-07-09. Contains only generated graph artifacts — no source code from the upstream repository, no secrets, no API keys.*
