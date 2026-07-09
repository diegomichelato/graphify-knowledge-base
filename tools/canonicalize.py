#!/usr/bin/env python3
"""Canonicalize entity/file dual nodes — without merging or deleting anything.

graphify creates two nodes per source file: an Entity node (e.g. `inputvalidator`,
label "InputValidator.cs") and a File node (`file:/abs/path/InputValidator.cs`).
This tool links each pair explicitly and marks the Entity as the preferred
retrieval target:

    Entity --defined_in--> File
    File   --contains-->   Entity

Also applies to Roslyn-created class nodes (`type:<path>#<Name>`) and
doc nodes (`doc:<relpath>` sections already have containment).

All existing node identifiers are preserved. Nothing is merged or deleted.

Usage: python3 tools/canonicalize.py [--graph graph.json] [--dry-run]
"""
import argparse, json, os
from collections import defaultdict


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--graph', default='graph.json')
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    g = json.load(open(args.graph, encoding='utf-8'))
    nodes, edges = g['nodes'], g['edges']
    existing = {(e['source'], e['target'], e['relationship']) for e in edges}

    # file: nodes indexed by the tail of their absolute path
    file_nodes = {}  # relative-ish suffix -> id
    for n in nodes:
        if n['id'].startswith('file:'):
            file_nodes[n['id'][len('file:'):].replace('\\', '/')] = n['id']

    def file_node_for(relpath):
        for abspath, nid in file_nodes.items():
            if abspath.endswith('/' + relpath) or abspath == relpath:
                return nid
        return None

    new_edges, preferred = [], 0

    def add(s, t, rel):
        if (s, t, rel) in existing or s == t:
            return
        existing.add((s, t, rel))
        new_edges.append({'source': s, 'target': t, 'relationship': rel,
                          'weight': 1, 'confidence': 'EXTRACTED',
                          'metadata': {'indexed_by': 'canonicalize.py (static)'}})

    for n in nodes:
        nid, fp = n['id'], n.get('file_path')
        if not fp or nid.startswith(('file:', 'doc:')):
            continue
        is_entity_for_file = (n['label'].lower() == os.path.basename(fp).lower())
        is_class_node = nid.startswith('type:')
        if not (is_entity_for_file or is_class_node):
            continue
        fid = file_node_for(fp)
        if not fid:
            continue
        add(nid, fid, 'defined_in')
        add(fid, nid, 'contains')
        if is_entity_for_file:
            n.setdefault('metadata', {})['retrieval_preferred'] = 'true'
            preferred += 1

    print(f'new canonical edges: {len(new_edges)} | entities marked retrieval_preferred: {preferred}')
    if args.dry_run:
        for e in new_edges[:10]:
            print('  +', e['source'], f"—{e['relationship']}→", e['target'])
        return
    edges.extend(new_edges)
    g.setdefault('metadata', {})['canonicalized'] = 'entity defined_in file; file contains entity; entity preferred'
    json.dump(g, open(args.graph, 'w', encoding='utf-8'), indent=2)
    print(f'graph now: {len(nodes)} nodes, {len(edges)} edges')


if __name__ == '__main__':
    main()
