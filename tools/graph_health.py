#!/usr/bin/env python3
"""/graph health — knowledge-graph health report.

Usage:
    python3 tools/graph_health.py [--graph graph.json] [--wiki wiki]
                                  [--source /path/to/app/repo] [--json]

Reports: totals, growth (vs git history), orphans, missing documentation,
broken wiki links, duplicate concepts, weak communities, unindexed files,
documentation/semantic coverage, technical-debt hotspots.
"""
import argparse, json, os, re, subprocess, sys
from collections import Counter, defaultdict

SOURCE_EXTS = {'.cs', '.py', '.ts', '.js', '.go', '.rs', '.java', '.c', '.cpp',
               '.rb', '.kt', '.scala', '.php', '.swift', '.r', '.lua', '.sh',
               '.ps1', '.yaml', '.yml', '.json', '.toml', '.xml', '.md', '.sql'}
SKIP_DIRS = {'.git', 'bin', 'obj', 'node_modules', 'graphify-out', '.vs'}


def load_previous_graph(path):
    """Previous committed version of graph.json, for growth metrics."""
    try:
        out = subprocess.run(['git', 'show', f'HEAD~1:{os.path.basename(path)}'],
                             capture_output=True, text=True, cwd=os.path.dirname(os.path.abspath(path)) or '.')
        if out.returncode == 0 and out.stdout.strip():
            return json.loads(out.stdout)
    except Exception:
        pass
    return None


def wiki_articles(wiki_dir):
    if not os.path.isdir(wiki_dir):
        return {}
    return {f[:-3]: os.path.join(wiki_dir, f)
            for f in os.listdir(wiki_dir) if f.endswith('.md')}


def broken_wiki_links(articles):
    """[[links]] that point to no existing article (space/underscore-insensitive)."""
    norm = lambda s: re.sub(r'[\s_]+', '_', s.strip().lower())
    known = {norm(name) for name in articles}
    broken = []
    for name, path in articles.items():
        try:
            text = open(path, encoding='utf-8').read()
        except Exception:
            continue
        for link in re.findall(r'\[\[([^\]|#]+)', text):
            if norm(link) not in known:
                broken.append((name, link.strip()))
    return broken


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--graph', default='graph.json')
    ap.add_argument('--wiki', default='wiki')
    ap.add_argument('--source', default=None,
                    help='path to the application repo, to detect unindexed files')
    ap.add_argument('--json', action='store_true', help='machine-readable output')
    args = ap.parse_args()

    g = json.load(open(args.graph, encoding='utf-8'))
    nodes, edges = g['nodes'], g['edges']
    node_by_id = {n['id']: n for n in nodes}

    degree = Counter()
    for e in edges:
        degree[e['source']] += 1
        degree[e['target']] += 1

    # --- totals & growth -------------------------------------------------
    prev = load_previous_graph(args.graph)
    growth = None
    if prev:
        growth = {'nodes': len(nodes) - len(prev['nodes']),
                  'edges': len(edges) - len(prev['edges'])}

    # --- orphans ----------------------------------------------------------
    orphans = [n for n in nodes if degree[n['id']] == 0]

    # --- duplicates (same label, different ids) ---------------------------
    CONTROL_NOISE = {'if()', 'for()', 'foreach()', 'while()', 'switch()', 'catch()',
                     'return()', 'var()', 'new()', 'lock()', 'using()', 'private()',
                     'static()', 'abstract()', 'override()', 'async()'}
    by_label = defaultdict(list)
    for n in nodes:
        lbl = n['label'].lower()
        if lbl in CONTROL_NOISE:
            continue  # AST control-flow noise, not real concepts
        fp = n.get('file_path')
        if fp and lbl == os.path.basename(fp).lower():
            # file-identity node: same basename at different paths is NOT a duplicate
            by_label[fp.lower()].append(n['id'])
        else:
            by_label[lbl].append(n['id'])
    all_dupes = {l: ids for l, ids in by_label.items() if len(ids) > 1}
    # pairs joined by a canonical defined_in/implements edge are LINKED aliases,
    # not unresolved duplicates
    linked_pairs = set()
    for e in edges:
        if e['relationship'] in ('defined_in', 'implements', 'contains'):
            linked_pairs.add(frozenset((e['source'], e['target'])))
    def unresolved(ids):
        return any(frozenset((a, b)) not in linked_pairs
                   for i, a in enumerate(ids) for b in ids[i + 1:])
    duplicates = {l: ids for l, ids in all_dupes.items() if unresolved(ids)}
    linked_dupes = len(all_dupes) - len(duplicates)

    # --- communities ------------------------------------------------------
    comm_nodes = defaultdict(list)
    for n in nodes:
        if n.get('community') is not None:
            comm_nodes[n['community']].append(n['id'])
    comm_cohesion = {}
    for c, ids in comm_nodes.items():
        idset = set(ids)
        internal = sum(1 for e in edges if e['source'] in idset and e['target'] in idset)
        possible = len(ids) * (len(ids) - 1) / 2 or 1
        comm_cohesion[c] = internal / possible
    weak = sorted([(c, round(coh, 2), len(comm_nodes[c]))
                   for c, coh in comm_cohesion.items() if coh < 0.15 and len(comm_nodes[c]) >= 5],
                  key=lambda x: x[1])

    # --- documentation coverage -------------------------------------------
    articles = wiki_articles(args.wiki)
    file_nodes = [n for n in nodes if n.get('file_path')]
    files_in_graph = {n['file_path'] for n in file_nodes}
    documented = sum(1 for n in file_nodes
                     if os.path.basename(n['file_path']) in articles
                     or n['label'] in articles)
    doc_coverage = documented / len(file_nodes) if file_nodes else 0
    broken = broken_wiki_links(articles)

    # --- semantic coverage (INFERRED = AI-derived) --------------------------
    inferred = sum(1 for n in nodes if n.get('confidence') == 'INFERRED')
    semantic_coverage = inferred / len(nodes) if nodes else 0

    # --- unindexed files ----------------------------------------------------
    unindexed = []
    if args.source and os.path.isdir(args.source):
        for root, dirs, fnames in os.walk(args.source):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
            for f in fnames:
                if os.path.splitext(f)[1].lower() in SOURCE_EXTS:
                    rel = os.path.relpath(os.path.join(root, f), args.source)
                    if rel.replace(os.sep, '/') not in files_in_graph:
                        unindexed.append(rel)

    # --- technical-debt hotspots: huge, weakly cohesive, highly connected ---
    hotspots = sorted(((n['label'], degree[n['id']]) for n in nodes),
                      key=lambda x: -x[1])[:10]

    report = {
        'total_nodes': len(nodes),
        'total_relationships': len(edges),
        'communities': len(comm_nodes),
        'growth_since_last_commit': growth or 'no previous version in git history',
        'orphan_nodes': [n['label'] for n in orphans],
        'duplicate_concepts': {l: ids for l, ids in list(duplicates.items())[:15]},
        'duplicate_concept_count': len(duplicates),
        'linked_alias_pairs': linked_dupes,
        'weakly_connected_communities': weak[:10],
        'documentation_coverage': f'{doc_coverage:.0%} of file nodes have wiki articles ({documented}/{len(file_nodes)})',
        'broken_wiki_links': broken[:15],
        'broken_wiki_link_count': len(broken),
        'semantic_coverage': f'{semantic_coverage:.0%} of nodes are AI-inferred (0% = AST-only graph)',
        'unindexed_files': unindexed[:25] if args.source else 'pass --source to check',
        'unindexed_file_count': len(unindexed) if args.source else None,
        'top_connected_hotspots': hotspots,
    }

    if args.json:
        print(json.dumps(report, indent=2))
        return

    print('=' * 60)
    print('KNOWLEDGE GRAPH HEALTH REPORT')
    print('=' * 60)
    for k, v in report.items():
        print(f'\n## {k.replace("_", " ").title()}')
        if isinstance(v, list):
            for item in v:
                print(f'  - {item}')
            if not v:
                print('  (none)')
        elif isinstance(v, dict):
            for kk, vv in v.items():
                print(f'  - {kk}: {vv}')
            if not v:
                print('  (none)')
        else:
            print(f'  {v}')


if __name__ == '__main__':
    main()
