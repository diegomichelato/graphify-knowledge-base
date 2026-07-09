#!/usr/bin/env python3
"""/graph impact <node> — blast-radius analysis for a node.

Usage:
    python3 tools/graph_impact.py <name-or-id> [--graph graph.json] [--hops 3] [--json]

Returns: dependencies, dependents, affected APIs, affected tests,
documentation, related ADRs, business features, estimated blast radius.
"""
import argparse, json, os, re, sys
from collections import defaultdict, deque


def find_node(nodes, query):
    q = query.lower()
    exact = [n for n in nodes if n['id'].lower() == q or n['label'].lower() == q]
    if exact:
        return exact[0]
    partial = [n for n in nodes if q in n['id'].lower() or q in n['label'].lower()]
    if not partial:
        return None
    # prefer file nodes, then shortest label
    partial.sort(key=lambda n: (0 if n.get('file_path') else 1, len(n['label'])))
    return partial[0]


def grep_dir(directory, term):
    """Files under directory mentioning term (case-insensitive)."""
    hits = []
    if not os.path.isdir(directory):
        return hits
    for f in sorted(os.listdir(directory)):
        if not f.endswith('.md'):
            continue
        try:
            if re.search(re.escape(term), open(os.path.join(directory, f), encoding='utf-8').read(), re.I):
                hits.append(f)
        except Exception:
            pass
    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('query')
    ap.add_argument('--graph', default='graph.json')
    ap.add_argument('--hops', type=int, default=3)
    ap.add_argument('--json', action='store_true')
    args = ap.parse_args()

    g = json.load(open(args.graph, encoding='utf-8'))
    nodes, edges = g['nodes'], g['edges']
    node_by_id = {n['id']: n for n in nodes}

    target = find_node(nodes, args.query)
    if not target:
        print(f'No node matching "{args.query}" found in the graph.', file=sys.stderr)
        sys.exit(1)

    out_edges = defaultdict(list)   # source -> [(target, rel)]
    in_edges = defaultdict(list)    # target -> [(source, rel)]
    for e in edges:
        out_edges[e['source']].append((e['target'], e['relationship']))
        in_edges[e['target']].append((e['source'], e['relationship']))

    def label(nid):
        n = node_by_id.get(nid)
        return n['label'] if n else nid

    tid = target['id']
    dependencies = [(label(t), rel) for t, rel in out_edges[tid]]
    dependents = [(label(s), rel) for s, rel in in_edges[tid]]

    # BFS blast radius over undirected edges
    adj = defaultdict(set)
    for e in edges:
        adj[e['source']].add(e['target'])
        adj[e['target']].add(e['source'])
    seen, frontier = {tid}, deque([(tid, 0)])
    per_hop = defaultdict(int)
    while frontier:
        nid, d = frontier.popleft()
        if d >= args.hops:
            continue
        for nb in adj[nid]:
            if nb not in seen:
                seen.add(nb)
                per_hop[d + 1] += 1
                frontier.append((nb, d + 1))
    reached = seen - {tid}

    reached_nodes = [node_by_id[n] for n in reached if n in node_by_id]
    affected_tests = {n['label'] for n in reached_nodes
                      if 'test' in (n.get('file_path') or '').lower()
                      or 'test' in n['label'].lower()}
    # AST-only graphs lack cross-file edges: fall back to name matching
    stem = re.sub(r'\.(cs|py|ts|js)$', '', target['label'], flags=re.I).lower()
    affected_tests |= {n['label'] for n in nodes
                       if stem in n['label'].lower() and 'test' in n['label'].lower()}
    affected_tests = sorted(affected_tests)
    # APIs ~ interface/public-surface nodes reached
    affected_apis = sorted({n['label'] for n in reached_nodes
                            if n['label'].startswith('I') and n['label'][1:2].isupper()
                            or (n.get('file_path', '') or '').endswith(('.cs',))
                            and n['label'].endswith('.cs') and n['label'].startswith('I')})

    base = os.path.dirname(os.path.abspath(args.graph))
    term = target['label'].replace('.cs', '').replace('()', '')
    docs = grep_dir(os.path.join(base, 'wiki'), term)
    adrs = grep_dir(os.path.join(base, 'adr'), term)
    business = grep_dir(os.path.join(base, 'business'), term)

    pct = len(reached) / max(len(nodes) - 1, 1)
    if pct > .25 or len(dependents) > 20:
        risk = 'HIGH'
    elif pct > .05 or len(dependents) > 5:
        risk = 'MEDIUM'
    else:
        risk = 'LOW'

    report = {
        'node': {'id': tid, 'label': target['label'],
                 'file': target.get('file_path'), 'community': target.get('community')},
        'dependencies': dependencies,
        'dependents': dependents,
        'affected_apis': affected_apis[:20],
        'affected_tests': affected_tests[:25],
        'documentation': docs[:15],
        'related_adrs': adrs,
        'business_features': business,
        'blast_radius': {
            'hops_analyzed': args.hops,
            'nodes_reached': len(reached),
            'per_hop': dict(per_hop),
            'percent_of_graph': f'{pct:.1%}',
            'risk': risk,
        },
    }

    if args.json:
        print(json.dumps(report, indent=2))
        return
    print('=' * 60)
    print(f"IMPACT ANALYSIS: {target['label']}  (id: {tid})")
    print('=' * 60)
    for k, v in report.items():
        if k == 'node':
            continue
        print(f'\n## {k.replace("_", " ").title()}')
        if isinstance(v, list):
            for item in v:
                print(f'  - {item}')
            if not v:
                print('  (none)')
        else:
            for kk, vv in v.items():
                print(f'  - {kk}: {vv}')


if __name__ == '__main__':
    main()
