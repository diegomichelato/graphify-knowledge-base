#!/usr/bin/env python3
"""Merge RoslynEdges output into graph.json, preserving all existing node IDs.

Only creates edges whose BOTH endpoints map to existing graph nodes
(matched by file_path + label). Unmappable edges are dropped and counted —
never fabricated. Namespace endpoints map to the canonical (lexicographically
first) node carrying that label, matching graphify's per-file namespace quirk.

Usage:
    python3 tools/merge_edges.py --edges /tmp/roslyn_edges.json [--graph graph.json] [--dry-run]
"""
import argparse, json, os
from collections import Counter, defaultdict


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--edges', required=True)
    ap.add_argument('--graph', default='graph.json')
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    g = json.load(open(args.graph, encoding='utf-8'))
    nodes, edges = g['nodes'], g['edges']
    raw = json.load(open(args.edges, encoding='utf-8'))

    by_file_label = {}                      # (file_path, label.lower()) -> id
    ns_canonical = {}                       # namespace label -> canonical id
    file_entity = {}                        # file_path -> entity node id (label == basename)
    for n in sorted(nodes, key=lambda x: x['id']):
        fp, lbl = n.get('file_path'), n['label']
        if fp:
            by_file_label.setdefault((fp, lbl.lower()), n['id'])
            if lbl.lower() == os.path.basename(fp).lower() and not n['id'].startswith('file:'):
                file_entity.setdefault(fp, n['id'])
        if '.' in lbl and lbl[0].isupper() and not fp and n['type'] == 'Entity':
            ns_canonical.setdefault(lbl, n['id'])
        # graphify namespace nodes DO carry file_path; also index those by label
        if n['type'] == 'Entity' and lbl[:1].isupper() and '.' in lbl and not lbl.endswith(('.cs', '.ts')):
            ns_canonical.setdefault(lbl, n['id'])

    new_type_nodes = []

    def resolve(kind, name, file, create_types=False):
        if kind == 'Namespace':
            return ns_canonical.get(name)
        if not file:
            return None
        if kind == 'Method':
            return by_file_label.get((file, name.lower()))
        if kind in ('Type', 'File'):
            hit = (by_file_label.get((file, f'{name}.cs'.lower()))
                   or by_file_label.get((file, name.lower())))
            if hit:
                return hit
            stem = os.path.splitext(os.path.basename(file))[0].lower()
            if kind == 'Type' and name.lower() != stem and create_types:
                # Class verified by Roslyn but absent from graphify's file-stem
                # model (multiple types per file). Create a stable node for it.
                nid = f'type:{file}#{name}'
                if nid not in {n['id'] for n in new_type_nodes}:
                    parent = file_entity.get(file)
                    comm = next((n.get('community') for n in nodes
                                 if n['id'] == parent), None) if parent else None
                    new_type_nodes.append({'id': nid, 'label': name, 'type': 'Entity',
                                           'community': comm, 'file_path': file,
                                           'confidence': 'EXTRACTED',
                                           'metadata': {'indexed_by': 'RoslynEdges (static analysis)'}})
                    by_file_label[(file, name.lower())] = nid
                    if parent:
                        pending_contains.append((parent, nid))
                return nid
            return file_entity.get(file)
        return None

    pending_contains = []

    existing = {(e['source'], e['target'], e['relationship']) for e in edges}
    added, dropped = [], Counter()
    # only structural rels justify creating class-level nodes
    STRUCTURAL = {'inherits', 'implements', 'references', 'tested_by', 'exports'}
    for r in raw:
        rel = r['relationship']
        create = rel in STRUCTURAL
        s = resolve(r['source_kind'], r['source_name'], r.get('source_file'), create)
        t = resolve(r['target_kind'], r['target_name'], r.get('target_file'), create)
        if not s or not t:
            dropped[rel] += 1
            continue
        if s == t or (s, t, rel) in existing:
            continue
        existing.add((s, t, rel))
        added.append({'source': s, 'target': t, 'relationship': rel,
                      'weight': 1, 'confidence': 'EXTRACTED',
                      'metadata': {'indexed_by': 'RoslynEdges (static analysis)'}})

    for parent, child in pending_contains:
        if (parent, child, 'contains') not in existing:
            existing.add((parent, child, 'contains'))
            added.append({'source': parent, 'target': child, 'relationship': 'contains',
                          'weight': 1, 'confidence': 'EXTRACTED',
                          'metadata': {'indexed_by': 'RoslynEdges (static analysis)'}})

    stats = Counter(e['relationship'] for e in added)
    print(f'mapped: {len(added)} new edges, {len(new_type_nodes)} new type nodes | '
          f'dropped (unmappable endpoints): {sum(dropped.values())}')
    for rel, c in stats.most_common():
        print(f'  +{rel}: {c}')
    for rel, c in dropped.most_common():
        print(f'  dropped {rel}: {c}')

    if args.dry_run:
        return
    nodes.extend(new_type_nodes)
    edges.extend(added)
    g.setdefault('metadata', {})['structural_edges'] = 'RoslynEdges (static, no AI)'
    json.dump(g, open(args.graph, 'w', encoding='utf-8'), indent=2)
    print(f'graph now: {len(nodes)} nodes, {len(edges)} edges')


if __name__ == '__main__':
    main()
