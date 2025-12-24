#!/usr/bin/env python3
"""
Scan all `builds/` subfolders for partials snippet files and write
`builds/manifests/partials-manifest.json`.

Usage:
  python3 src/scripts/manifest_utils/manifest-generate-partials.py [--dry-run]

The script will back up the existing manifest to partials-manifest.json.bak before writing.
"""

import os
import json
import xml.etree.ElementTree as ET
import argparse


def local_name(tag):
  if tag is None:
    return None
  if '}' in tag:
    return tag.split('}', 1)[1]
  return tag


def infer_target_and_tags(root):
  tags = set()
  target = None
  for elem in root.iter():
    ln = local_name(elem.tag)
    if ln in ('numbering', 'abstractNum', 'num'):
      target = 'word:numbering'
      tags.add('numbering')
    if ln == 'style':
      if target is None:
        target = 'word:styles'
      tags.add('styles')
  return target, sorted(tags)


def parse_snippet_file(path, repo_root):
  try:
    tree = ET.parse(path)
    root = tree.getroot()
  except Exception:
    return None

  ln = local_name(root.tag)
  rel = os.path.relpath(path, repo_root).replace('\\', '/')

  if ln == 'snippet':
    sid = root.attrib.get('id') or os.path.splitext(os.path.basename(path))[0]
    target, tags = infer_target_and_tags(root)
    return {
      'id': sid,
      'path': rel,
      'target': target or '',
      'tags': tags or [],
      'status': 'active'
    }

  sid = os.path.splitext(os.path.basename(path))[0]
  target, tags = infer_target_and_tags(root)
  return {
    'id': sid,
    'path': rel,
    'target': target or '',
    'tags': tags or [],
    'status': 'active'
  }


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--dry-run', action='store_true', help='Print the manifest JSON but do not write')
  args = parser.parse_args()

  repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
  builds_root = os.path.join(repo_root, 'builds')
  # write the shared manifests under builds/manifests/
  manifest_dir = os.path.join(builds_root, 'manifests')
  manifest_path = os.path.join(manifest_dir, 'partials-manifest.json')

  if not os.path.isdir(builds_root):
    print('builds directory not found:', builds_root)
    return 2

  entries = []

  for dirpath, dirnames, filenames in os.walk(builds_root):
    # only consider files inside a `partials` folder
    parts = dirpath.replace('\\', '/').split('/')
    if 'partials' not in parts:
      continue
    for fn in sorted(filenames):
      if not fn.lower().endswith('.xml') and not fn.lower().endswith('.xmlx'):
        continue
      full = os.path.join(dirpath, fn)
      e = parse_snippet_file(full, repo_root)
      if e:
        entries.append(e)

  entries.sort(key=lambda x: (x.get('id') or '', x.get('path') or ''))

  manifest = {'snippets': entries}

  out = json.dumps(manifest, indent=2)

  if args.dry_run:
    print(out)
    return 0

  os.makedirs(manifest_dir, exist_ok=True)

  if os.path.exists(manifest_path):
    bak = manifest_path + '.bak'
    try:
      os.replace(manifest_path, bak)
      print('Backup saved to', bak)
    except Exception as ex:
      print('Warning: could not create backup:', ex)

  try:
    with open(manifest_path, 'w', encoding='utf-8') as f:
      f.write(out + '\n')
    print('Wrote', manifest_path)
  except Exception as ex:
    print('Error writing manifest:', ex)
    return 3

  print('Found', len(entries), 'snippet(s)')
  return 0


if __name__ == '__main__':
  raise SystemExit(main())
