#!/usr/bin/env bash
# Incremental knowledge-base update pipeline.
#
# Usage: tools/update_knowledge.sh <app-repo-path> [note]
#
# 1. Detects changed files in the application repo (git status/diff).
# 2. Re-runs graphify (its semantic cache skips unchanged files).
# 3. Copies updated artifacts (graph.json, wiki, obsidian, report) here.
# 4. Generates a changelog entry from the graph diff.
# 5. Commits. Push is left to the caller (needs credentials).
set -euo pipefail

APP_REPO="${1:?usage: update_knowledge.sh <app-repo-path> [note]}"
NOTE="${2:-}"
KB_DIR="$(cd "$(dirname "$0")/.." && pwd)"

echo "==> Detecting changed files in $APP_REPO"
cd "$APP_REPO"
CHANGED=$(git status --porcelain=v1 -- '*.cs' '*.md' '*.json' '*.yml' '*.yaml' '*.ts' | wc -l)
git diff --name-only HEAD~1 2>/dev/null | head -20 || true
echo "    $CHANGED uncommitted changed files"

echo "==> Running graphify (incremental via semantic cache)"
graphify run "$APP_REPO" -o "$APP_REPO/graphify-out" -f json,html,wiki,report,obsidian

echo "==> Syncing artifacts into knowledge base"
cp "$APP_REPO/graphify-out/graph.json" "$KB_DIR/graph.json"
cp "$APP_REPO/graphify-out/graph.html" "$KB_DIR/graph.html"
cp "$APP_REPO/graphify-out/GRAPH_REPORT.md" "$KB_DIR/GRAPH_REPORT.md"
rsync -a --delete "$APP_REPO/graphify-out/wiki/" "$KB_DIR/wiki/"
rsync -a --delete "$APP_REPO/graphify-out/obsidian/" "$KB_DIR/obsidian/"

echo "==> Generating changelog entry"
cd "$KB_DIR"
if ! git diff --quiet graph.json; then
    TMP=$(mktemp)
    python3 tools/graph_changelog.py --old HEAD --new graph.json ${NOTE:+--note "$NOTE"} > "$TMP"
    # prepend under the header line of CHANGELOG.md
    head -2 CHANGELOG.md > CHANGELOG.new
    cat "$TMP" >> CHANGELOG.new
    tail -n +3 CHANGELOG.md >> CHANGELOG.new
    mv CHANGELOG.new CHANGELOG.md
    rm -f "$TMP"
else
    echo "    graph.json unchanged — no changelog entry"
fi

echo "==> Committing"
git add -A
git commit -m "Incremental knowledge-base update${NOTE:+: $NOTE}" || echo "    nothing to commit"
echo "==> Done. Push with: git push origin knowledge-graph-output"
