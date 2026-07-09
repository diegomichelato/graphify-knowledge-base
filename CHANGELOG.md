# Knowledge Base Changelog

## 2026-07-09

Graph: 1620→2163 nodes, 2852→5556 relationships.

### Added components (543)
  - `".NET 10 SDK not found"` (docs/troubleshooting.md)
  - `"How do I use this without AI?"` (docs/troubleshooting.md)
  - `"graphify: command not found"` (docs/troubleshooting.md)
  - `.gitignore` (.github/copilot-instructions.md)
  - `1. Karpathy's Vision: The Origin` (ROADMAP.md)
  - `16:9 Format (1792×1024) — Blog Hero & Hero Images` (.squad/image-prompts.md)
  - `1:1 Format (1024×1024) — LinkedIn & Twitter Posts` (.squad/image-prompts.md)
  - `2. Ecosystem Analysis` (ROADMAP.md)
  - `2026-04-07 - Report Generator + Exporters + URL Ingester Batch Implementation` (.squad/agents/trinity/history.md)
  - `3. Proposed Improvements` (ROADMAP.md)
  - `4. How graphify-dotnet Connects to Karpathy's Vision` (ROADMAP.md)
  - `5. Priority Matrix` (ROADMAP.md)
  - `6. References` (ROADMAP.md)
  - `AI Integration` (ARCHITECTURE.md)
  - `AI provider errors` (docs/troubleshooting.md)
  - `APPENDIX: RAW AGENT OUTPUTS` (.squad/templates/run-output.md)
  - `APPENDIX: RAW AGENT OUTPUTS` (.squad/templates/multi-agent-format.md)
  - `APPENDIX: RAW AGENT OUTPUTS` (.squad/templates/raw-agent-output.md)
  - `ARCHITECTURE.md` (ARCHITECTURE.md)
  - `About Me` (docs/blog-post.md)
  - … and 523 more
### Removed components (0)
  - (none)
### Renamed components (0)
  - (none)
### API changes
  - (none)
### Dependency changes (+2704 / -0)
  - `agentfactory_graphify_sdk` —exports→ `agentfactory`
  - `agentfactory_graphify_sdk` —exports→ `azureopenaiclientfactory`
  - `agentfactory_graphify_sdk` —exports→ `azureopenaioptions`
  - `agentfactory_graphify_sdk` —exports→ `chatclientfactory`
  - `agentfactory_graphify_sdk` —exports→ `copilotchatclient`
  - `agentfactory_graphify_sdk` —exports→ `copilotextractor`
  - `agentfactory_graphify_sdk` —exports→ `copilotextractoroptions`
  - `agentfactory_graphify_sdk` —exports→ `copilotsdkclientfactory`
  - `agentfactory_graphify_sdk` —exports→ `copilotsdkoptions`
  - `agentfactory_graphify_sdk` —exports→ `file:/home/claude/graphify-dotnet/src/Graphify.Sdk/OllamaClientFactory.cs`
  - `agentfactory_graphify_sdk` —exports→ `file:/home/claude/graphify-dotnet/src/Graphify.Sdk/OllamaOptions.cs`
  - `agentfactory_graphify_sdk` —exports→ `type:src/Graphify.Sdk/ChatClientFactory.cs#AiProvider`
  - `agentfactory_graphify_sdk` —exports→ `type:src/Graphify.Sdk/ChatClientFactory.cs#AiProviderOptions`
  - `analysisresult` —tested_by→ `analyzertests`
  - `analysisresult` —tested_by→ `exportintegrationtests`
  - … and 2689 more
  - (none)
### Architecture / business notes
  - Action 1+3: static doc/config indexing (106 files) and Roslyn-verified structural edges (implements/inherits/overrides/calls/references/tested_by/imports/exports); no AI, no full rebuild

## 2026-07-09

Graph: 0→1,620 nodes, 0→2,852 relationships (initial build).

### Added components (1,620)
  - Initial AST-only extraction of `elbruno/graphify-dotnet` @ `02b8276`:
    132 files processed, 167 communities detected.

### Removed / renamed components
  - (none — initial build)

### API changes
  - (baseline established)

### Dependency changes
  - (baseline: 2,852 relationships)

### Documentation updates
  - 173-article wiki, Obsidian vault (~1,300 notes), GRAPH_REPORT.md generated.
  - README.md (memory-layer usage), CLAUDE.md (operating + maintenance rules).

### Architecture changes
  - ADR-0001: knowledge repo as permanent memory layer (accepted).
  - ADR-0002: dual-repository strategy with incremental sync (accepted).

### Business rule changes
  - business/product-knowledge.md seeded (product purpose, features, standards, ops).

<!-- New entries are PREPENDED below the title by tools/update_knowledge.sh -->
