#!/usr/bin/env python3
"""Repair broken wiki [[links]] against the knowledge graph.

Policy (per operating instructions):
  1. If the link target matches an existing graph node -> the page SHOULD exist:
     generate it from the graph (id, file, community, relationships).
  2. If the target matches an existing article under a different normalization
     -> repair the link text in place.
  3. Only if the referenced entity truly does not exist in the graph ->
     unlink it (convert [[X]] to `X`), preserving the text.

Never deletes articles or nodes.

Usage: python3 tools/refine_wiki.py [--graph graph.json] [--wiki wiki] [--dry-run]
"""
import argparse, json, os, re
from collections import defaultdict


def norm(s):
    return re.sub(r'[\s_]+', '_', s.strip().lower())


def safe_filename(label):
    """Match graphify's wiki naming: spaces -> underscore, strip path chars."""
    return re.sub(r'[\\/:*?"<>|]', '_', label.replace(' ', '_'))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--graph', default='graph.json')
    ap.add_argument('--wiki', default='wiki')
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    g = json.load(open(args.graph, encoding='utf-8'))
    nodes, edges = g['nodes'], g['edges']
    by_label = defaultdict(list)
    for n in nodes:
        by_label[n['label'].lower()].append(n)
    nbrs = defaultdict(list)
    node_by_id = {n['id']: n for n in nodes}
    for e in edges:
        nbrs[e['source']].append((e['relationship'], e['target'], '→'))
        nbrs[e['target']].append((e['relationship'], e['source'], '←'))

    articles = {norm(f[:-3]): f for f in os.listdir(args.wiki) if f.endswith('.md')}

    created, repaired, unlinked = [], [], []
    for fname in sorted(os.listdir(args.wiki)):
        if not fname.endswith('.md'):
            continue
        path = os.path.join(args.wiki, fname)
        text = open(path, encoding='utf-8').read()
        changed = False

        for m in sorted(set(re.findall(r'\[\[([^\]|#]+)\]\]', text))):
            target = m.strip()
            if norm(target) in articles:
                continue  # resolves fine

            cand = by_label.get(target.lower())
            if cand:
                # entity exists in graph -> page should exist; create it
                node = sorted(cand, key=lambda n: (n['id'].startswith('file:'), n['id']))[0]
                new_name = f'{safe_filename(target)}.md'
                new_path = os.path.join(args.wiki, new_name)
                if norm(new_name[:-3]) not in articles:
                    if not args.dry_run:
                        with open(new_path, 'w', encoding='utf-8') as f:
                            f.write(f'# {node["label"]}\n\n')
                            f.write(f'> Auto-generated from the knowledge graph '
                                    f'(refine_wiki.py, static). Node id: `{node["id"]}`\n\n')
                            if node.get('file_path'):
                                f.write(f'- **File:** `{node["file_path"]}`\n')
                            f.write(f'- **Type:** {node["type"]}\n')
                            f.write(f'- **Community:** [[Community {node.get("community")}]]\n')
                            if len(cand) > 1:
                                f.write(f'- **Also known as:** '
                                        + ', '.join(f'`{c["id"]}`' for c in cand if c is not node) + '\n')
                            rels = nbrs[node['id']][:30]
                            if rels:
                                f.write('\n## Relationships\n\n')
                                for rel, other, arrow in rels:
                                    lbl = node_by_id.get(other, {}).get('label', other)
                                    # link only to articles that exist; never mint new broken links
                                    if norm(safe_filename(lbl)) in articles:
                                        f.write(f'- {arrow} *{rel}* [[{safe_filename(lbl)}]]\n')
                                    else:
                                        f.write(f'- {arrow} *{rel}* `{lbl}`\n')
                    articles[norm(new_name[:-3])] = new_name
                    created.append(new_name)
                # repair link if filename normalization differs from link text
                if norm(target) != norm(safe_filename(target)):
                    text = text.replace(f'[[{m}]]', f'[[{safe_filename(target)}]]')
                    changed = True
                    repaired.append((fname, target))
            else:
                # entity truly absent from the graph -> unlink, keep the text
                text = text.replace(f'[[{m}]]', f'`{target}`')
                changed = True
                unlinked.append((fname, target))

        if changed and not args.dry_run:
            open(path, 'w', encoding='utf-8').write(text)

    print(f'created pages: {len(created)} | repaired links: {len(repaired)} | '
          f'unlinked (entity does not exist): {len(unlinked)}')
    for f in created[:20]:
        print('  +page', f)
    for f, t in unlinked[:20]:
        print('  -link', f, '→', t)


if __name__ == '__main__':
    main()
