#!/usr/bin/env python3
"""One-time migration: re-point structural edges from file: alias nodes to their
canonical Entity nodes (per the canonicalization policy: Entity is the preferred
retrieval target). No nodes are merged or deleted; only edge endpoints created by
RoslynEdges/index_docs are normalized. `contains`/`defined_in` alias links stay.

Usage: python3 tools/migrate_edges_to_entities.py [--graph graph.json] [--dry-run]
"""
import argparse, json, os

STRUCTURAL = {'implements', 'inherits', 'overrides', 'calls', 'references',
              'tested_by', 'imports', 'exports', 'configures'}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--graph', default='graph.json')
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    g = json.load(open(args.graph, encoding='utf-8'))
    nodes, edges = g['nodes'], g['edges']

    # file: node id -> canonical entity id (same file_path, label == basename)
    entity_for_path = {}
    for n in nodes:
        fp = n.get('file_path')
        if fp and not n['id'].startswith(('file:', 'doc:')) \
           and n['label'].lower() == os.path.basename(fp).lower():
            entity_for_path[fp] = n['id']
    alias = {}
    for n in nodes:
        if n['id'].startswith('file:'):
            tail = n['id'][len('file:'):].replace('\\', '/')
            for fp, eid in entity_for_path.items():
                if tail.endswith('/' + fp) or tail == fp:
                    alias[n['id']] = eid
                    break

    seen = {(e['source'], e['target'], e['relationship']) for e in edges}
    migrated, dropped_dupes = 0, 0
    kept = []
    for e in edges:
        if e['relationship'] in STRUCTURAL:
            ns, nt = alias.get(e['source'], e['source']), alias.get(e['target'], e['target'])
            if (ns, nt) != (e['source'], e['target']):
                key = (ns, nt, e['relationship'])
                old = (e['source'], e['target'], e['relationship'])
                if key in seen or ns == nt:
                    dropped_dupes += 1   # entity-level edge already exists
                    seen.discard(old)
                    continue
                seen.discard(old)
                seen.add(key)
                e['source'], e['target'] = ns, nt
                e.setdefault('metadata', {})['migrated'] = 'file-alias -> entity'
                migrated += 1
        kept.append(e)

    print(f'migrated to entity endpoints: {migrated} | redundant after migration: {dropped_dupes}')
    if args.dry_run:
        return
    g['edges'] = kept
    json.dump(g, open(args.graph, 'w', encoding='utf-8'), indent=2)
    print(f'graph now: {len(nodes)} nodes, {len(kept)} edges')


if __name__ == '__main__':
    main()
