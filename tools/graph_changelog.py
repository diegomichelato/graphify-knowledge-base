#!/usr/bin/env python3
"""Generate a changelog entry by diffing two versions of graph.json.

Usage:
    python3 tools/graph_changelog.py [--old HEAD~1] [--new graph.json]
                                     [--date YYYY-MM-DD] [--note "..."]

--old is a git revision (the file graph.json is read from it) or a file path.
Appends a Markdown section suitable for CHANGELOG.md to stdout.
"""
import argparse, json, os, subprocess, sys
from collections import defaultdict


def load(ref_or_path, repo_dir):
    if os.path.exists(ref_or_path):
        return json.load(open(ref_or_path, encoding='utf-8'))
    out = subprocess.run(['git', 'show', f'{ref_or_path}:graph.json'],
                         capture_output=True, text=True, cwd=repo_dir)
    if out.returncode != 0:
        sys.exit(f'cannot load graph from {ref_or_path}: {out.stderr.strip()}')
    return json.loads(out.stdout)


def edge_key(e):
    return (e['source'], e['target'], e['relationship'])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--old', default='HEAD~1')
    ap.add_argument('--new', default='graph.json')
    ap.add_argument('--date', default=None, help='entry date (YYYY-MM-DD); defaults to today')
    ap.add_argument('--note', default='', help='free-text note (architecture/business changes)')
    args = ap.parse_args()

    repo_dir = os.path.dirname(os.path.abspath(args.new)) or '.'
    old, new = load(args.old, repo_dir), load(args.new, repo_dir)

    old_nodes = {n['id']: n for n in old['nodes']}
    new_nodes = {n['id']: n for n in new['nodes']}
    added = [new_nodes[i] for i in new_nodes.keys() - old_nodes.keys()]
    removed = [old_nodes[i] for i in old_nodes.keys() - new_nodes.keys()]
    renamed = [(old_nodes[i]['label'], new_nodes[i]['label'])
               for i in new_nodes.keys() & old_nodes.keys()
               if old_nodes[i]['label'] != new_nodes[i]['label']]

    old_edges = {edge_key(e) for e in old['edges']}
    new_edges = {edge_key(e) for e in new['edges']}
    dep_added = new_edges - old_edges
    dep_removed = old_edges - new_edges

    def is_api(n):
        lbl = n['label']
        return lbl.startswith('I') and lbl[1:2].isupper() or lbl.endswith('()')

    api_added = [n['label'] for n in added if is_api(n)]
    api_removed = [n['label'] for n in removed if is_api(n)]

    date = args.date
    if not date:
        # date stamped by caller normally; fall back to git's view of "now"
        date = subprocess.run(['date', '+%Y-%m-%d'], capture_output=True,
                              text=True).stdout.strip()

    def fmt_nodes(ns, cap=20):
        lines = [f'  - `{n["label"]}`' + (f' ({n["file_path"]})' if n.get('file_path') else '')
                 for n in sorted(ns, key=lambda x: x['label'])[:cap]]
        if len(ns) > cap:
            lines.append(f'  - … and {len(ns) - cap} more')
        return lines or ['  - (none)']

    def fmt_edges(es, cap=15):
        lines = [f'  - `{s}` —{r}→ `{t}`' for s, t, r in sorted(es)[:cap]]
        if len(es) > cap:
            lines.append(f'  - … and {len(es) - cap} more')
        return lines or ['  - (none)']

    out = [f'## {date}',
           '',
           f'Graph: {len(old_nodes)}→{len(new_nodes)} nodes, {len(old_edges)}→{len(new_edges)} relationships.',
           '',
           f'### Added components ({len(added)})', *fmt_nodes(added),
           f'### Removed components ({len(removed)})', *fmt_nodes(removed),
           f'### Renamed components ({len(renamed)})',
           *([f'  - `{a}` → `{b}`' for a, b in renamed[:20]] or ['  - (none)']),
           f'### API changes',
           *([f'  - added `{a}`' for a in api_added[:15]] +
             [f'  - removed `{a}`' for a in api_removed[:15]] or ['  - (none)']),
           f'### Dependency changes (+{len(dep_added)} / -{len(dep_removed)})',
           *fmt_edges(dep_added), *fmt_edges(dep_removed)]
    if args.note:
        out += ['### Architecture / business notes', f'  - {args.note}']
    out.append('')
    print('\n'.join(out))


if __name__ == '__main__':
    main()
