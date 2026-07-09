# Graphify Operating Instructions

This repository is the **primary source of truth** for understanding the
[elbruno/graphify-dotnet](https://github.com/elbruno/graphify-dotnet) project.
Any AI agent (Claude or otherwise) working on that project must follow these rules.

## Operating rules — for every request

1. Query the Graphify knowledge graph (`graph.json`) first.
2. Search the generated wiki (`wiki/`) and documentation before reading source code.
3. Use `graph.json` and its semantic relationships to understand architecture.
4. Only inspect source files if the knowledge graph does not contain enough information.
5. If source files are read, update the knowledge graph incrementally after completing the task
   (re-run `graphify run` on changed paths only; the semantic cache skips unchanged files).
6. Never perform a full repository scan unless explicitly requested.
7. Preserve and improve the knowledge graph after every significant code change.
8. Record architectural decisions, new modules, APIs, business logic, and implementation notes in the graph.
9. Keep documentation synchronized with the graph.
10. Minimize token usage by retrieving only the smallest relevant context required.

## Priority order for answering questions

1. Graphify MCP (if connected — the upstream project ships `Graphify.Mcp`)
2. Knowledge graph (`graph.json`)
3. Generated wiki (`wiki/`)
4. Graph report (`GRAPH_REPORT.md`)
5. Obsidian vault (`obsidian/`)
6. Source code (last resort)

Never skip directly to source code unless the previous sources are insufficient.

## Answer attribution

Every answer must state its provenance: **Knowledge Graph**, **Wiki**, **Source Code**,
or **Combination of sources**.

## Continuous improvement

If information is missing from the graph, enrich it so future requests become more
efficient. The objective is to continuously improve the knowledge graph while reducing
token usage and avoiding unnecessary repository scans.

## Knowledge graph maintenance

Whenever source code changes:

1. Detect the files that changed (e.g. `git diff --name-only`).
2. Run Graphify only on the changed files whenever incremental indexing is supported
   (the semantic cache skips unchanged files automatically).
3. Update `graph.json`, `wiki/`, `obsidian/`, and `GRAPH_REPORT.md`.
4. Commit the updated knowledge base.
5. Push changes to the `graphify-knowledge-base` repository.
6. Never rebuild the entire graph unless explicitly requested.

## Repository strategy

Treat the application repository and the knowledge repository as two synchronized repositories.

| Repository | Contents |
|---|---|
| **Application** ([elbruno/graphify-dotnet](https://github.com/elbruno/graphify-dotnet)) | Source code, tests, documentation |
| **Knowledge** (this repo) | Graph, wiki, Obsidian vault, reports, architecture, semantic documentation |

Every meaningful architectural change should update both repositories.

## Future AI provider

When an AI provider (Ollama, Azure OpenAI, OpenAI, or GitHub Models) becomes available:

- Generate semantic summaries.
- Discover cross-file relationships.
- Generate business-domain nodes.
- Improve architectural documentation.
- Rename anonymous communities (currently "Entity (Community N)").
- Update semantic links without rebuilding unchanged nodes.

Always preserve existing graph identifiers whenever possible.

## Token optimization

Before reading any file:

1. Check whether the answer already exists in the knowledge graph.
2. If it does, never reload the file.
3. Only retrieve the smallest amount of source code necessary to answer the question.

## Quick queries

```bash
# Find a node by name
jq '.nodes[] | select(.label | test("NAME"; "i"))' graph.json

# Neighbors of a node
jq --arg id "NODE_ID" '.edges[] | select(.source==$id or .target==$id)' graph.json

# Nodes in a community
jq '.nodes[] | select(.community==N) | .label' graph.json
```
