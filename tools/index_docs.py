#!/usr/bin/env python3
"""Statically index documentation & configuration files into graph.json.

No AI, no fabrication: only facts that are verifiable from file contents —
file existence, markdown headings, resolvable relative links, config placement.

Usage:
    python3 tools/index_docs.py --source /path/to/app-repo [--graph graph.json]
                                [--wiki wiki] [--dry-run]

Adds:
  - File nodes (id: doc:<relpath>) for .md/.json/.yml/.yaml/.toml/.txt files
    not already in the graph.
  - Section nodes (id: doc:<relpath>#<slug>) for H1/H2 markdown headings,
    linked with `contains`.
  - `references` edges for relative markdown links that resolve to an indexed
    file (doc or source).
  - `configures` edges: appsettings/xunit.runner/workflow files -> the project
    or repository they demonstrably configure (same-directory csproj rule).
  - A repository node (id: repo:root) as the anchor for repo-level docs/CI.
  - One wiki article per newly indexed doc (headings + outgoing links).
"""
import argparse, json, os, re, sys

DOC_EXTS = {'.md', '.markdown', '.txt', '.rst', '.adoc'}
CFG_EXTS = {'.json', '.yml', '.yaml', '.toml'}
SKIP_DIRS = {'.git', 'bin', 'obj', 'node_modules', 'graphify-out', '.vs'}
SKIP_FILES = {'test-output.txt'}


def slug(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')[:60]


def md_headings(text):
    return [(len(m.group(1)), m.group(2).strip())
            for m in re.finditer(r'^(#{1,2})\s+(.+)$', text, re.M)]


def md_links(text):
    """Relative markdown link targets (path part only)."""
    out = []
    for m in re.finditer(r'\[[^\]]*\]\(([^)#\s]+)', text):
        t = m.group(1)
        if not t.startswith(('http://', 'https://', 'mailto:', '#')):
            out.append(t)
    return out


def nearest_project(relpath, source):
    """Name of the csproj in the same directory (or nearest ancestor)."""
    d = os.path.dirname(os.path.join(source, relpath))
    while len(d) >= len(source.rstrip('/')):
        for f in os.listdir(d):
            if f.endswith('.csproj'):
                return os.path.splitext(f)[0]
        nd = os.path.dirname(d)
        if nd == d:
            break
        d = nd
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--source', required=True)
    ap.add_argument('--graph', default='graph.json')
    ap.add_argument('--wiki', default='wiki')
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    g = json.load(open(args.graph, encoding='utf-8'))
    nodes, edges = g['nodes'], g['edges']
    existing_paths = {n.get('file_path') for n in nodes if n.get('file_path')}
    existing_ids = {n['id'] for n in nodes}
    existing_edge_keys = {(e['source'], e['target'], e['relationship']) for e in edges}
    # representative existing node per label (for configures targets)
    by_label = {}
    for n in sorted(nodes, key=lambda x: x['id']):
        by_label.setdefault(n['label'].lower(), n['id'])
    # basename -> file_path for link resolution against source files
    by_basename = {}
    for p in existing_paths:
        by_basename.setdefault(os.path.basename(p).lower(), p)

    next_comm = max((n.get('community') or 0) for n in nodes) + 1
    COMM = {'docs': next_comm, 'config': next_comm + 1, 'ci': next_comm + 2}
    COMM_LABEL = {next_comm: 'Documentation', next_comm + 1: 'Configuration',
                  next_comm + 2: 'CI/CD'}

    new_nodes, new_edges = [], []

    def add_node(nid, label, ntype, relpath, community, meta=None):
        if nid in existing_ids:
            return False
        existing_ids.add(nid)
        new_nodes.append({'id': nid, 'label': label, 'type': ntype,
                          'community': community, 'file_path': relpath,
                          'confidence': 'EXTRACTED',
                          'metadata': meta or {'indexed_by': 'index_docs.py (static)'}})
        return True

    def add_edge(s, t, rel):
        k = (s, t, rel)
        if k in existing_edge_keys or s == t:
            return
        existing_edge_keys.add(k)
        new_edges.append({'source': s, 'target': t, 'relationship': rel,
                          'weight': 1, 'confidence': 'EXTRACTED',
                          'metadata': {'indexed_by': 'index_docs.py (static)'}})

    # repository anchor node
    add_node('repo:root', 'graphify-dotnet (repository)', 'Entity', None, COMM['docs'],
             {'indexed_by': 'index_docs.py (static)', 'role': 'repository root'})

    # ---- discover candidate files ------------------------------------------
    candidates = []
    for root, dirs, fnames in os.walk(args.source):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in fnames:
            ext = os.path.splitext(f)[1].lower()
            if f in SKIP_FILES or ext not in DOC_EXTS | CFG_EXTS:
                continue
            rel = os.path.relpath(os.path.join(root, f), args.source).replace(os.sep, '/')
            if rel not in existing_paths:
                candidates.append(rel)
    candidates.sort()

    doc_meta = {}   # relpath -> (headings, links) for wiki generation
    for rel in candidates:
        full = os.path.join(args.source, rel)
        ext = os.path.splitext(rel)[1].lower()
        base = os.path.basename(rel)
        is_ci = rel.startswith('.github/workflows/')
        comm = COMM['ci'] if is_ci else (COMM['docs'] if ext in DOC_EXTS else COMM['config'])
        nid = f'doc:{rel}'
        add_node(nid, base, 'File', rel, comm)
        add_edge('repo:root', nid, 'contains')

        try:
            text = open(full, encoding='utf-8', errors='replace').read()
        except Exception:
            continue

        if ext in DOC_EXTS:
            heads = md_headings(text)
            links = md_links(text)
            doc_meta[rel] = (heads, links)
            for lvl, h in heads[:20]:
                if lvl == 1:
                    continue  # H1 duplicates the file itself
                sid = f'{nid}#{slug(h)}'
                add_node(sid, h, 'Section', rel, comm)
                add_edge(nid, sid, 'contains')
            for link in links:
                targ = os.path.normpath(os.path.join(os.path.dirname(rel), link)).replace(os.sep, '/')
                tb = os.path.basename(targ).lower()
                if targ in existing_paths:                       # source file
                    tid = f'doc:{targ}' if f'doc:{targ}' in existing_ids else by_label.get(tb)
                    if tid:
                        add_edge(nid, tid, 'references')
                elif f'doc:{targ}' in existing_ids:              # another doc
                    add_edge(nid, f'doc:{targ}', 'references')
                elif tb in by_basename:                          # basename fallback
                    tid = by_label.get(tb)
                    if tid:
                        add_edge(nid, tid, 'references')

        # ---- configures edges (statically verifiable placement) ------------
        if base == 'appsettings.json' or base.startswith('appsettings.'):
            proj = nearest_project(rel, args.source)
            if proj and proj.lower() in by_label:
                add_edge(nid, by_label[proj.lower()], 'configures')
        elif base == 'xunit.runner.json':
            proj = nearest_project(rel, args.source)
            if proj and proj.lower() in by_label:
                add_edge(nid, by_label[proj.lower()], 'configures')
        elif is_ci or base in ('global.json', 'Directory.Build.props', 'squad.config.ts',
                               'mcp-config.json', 'copilot-instructions.md'):
            add_edge(nid, 'repo:root', 'configures')

    # second pass: doc->doc links now that all doc nodes exist
    for rel, (_, links) in doc_meta.items():
        for link in links:
            targ = os.path.normpath(os.path.join(os.path.dirname(rel), link)).replace(os.sep, '/')
            if f'doc:{targ}' in existing_ids:
                add_edge(f'doc:{rel}', f'doc:{targ}', 'references')

    print(f'candidates: {len(candidates)} | new nodes: {len(new_nodes)} | new edges: {len(new_edges)}')
    if args.dry_run:
        for n in new_nodes[:15]:
            print('  +node', n['id'])
        for e in new_edges[:15]:
            print('  +edge', e['source'], f"—{e['relationship']}→", e['target'])
        return

    nodes.extend(new_nodes)
    edges.extend(new_edges)
    g.setdefault('metadata', {})['augmented_by'] = 'index_docs.py (static, no AI)'
    g['metadata']['community_labels'] = {**g['metadata'].get('community_labels', {}),
                                         **{str(k): v for k, v in COMM_LABEL.items()}}
    json.dump(g, open(args.graph, 'w', encoding='utf-8'), indent=2)

    # ---- wiki articles for newly indexed docs ------------------------------
    os.makedirs(args.wiki, exist_ok=True)
    for rel, (heads, links) in doc_meta.items():
        name = os.path.basename(rel)
        art = os.path.join(args.wiki, f'{name}.md')
        if os.path.exists(art):
            continue
        with open(art, 'w', encoding='utf-8') as f:
            f.write(f'# {name}\n\n> Statically indexed from `{rel}` (no AI). '
                    f'Node id: `doc:{rel}`\n\n## Sections\n\n')
            for lvl, h in heads[:25]:
                f.write(f'{"  " * (lvl - 1)}- {h}\n')
            if links:
                f.write('\n## Outgoing references\n\n')
                for l in sorted(set(links))[:25]:
                    f.write(f'- `{l}`\n')
    print(f'wiki articles written for {len(doc_meta)} docs')


if __name__ == '__main__':
    main()
