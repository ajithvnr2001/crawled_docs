#!/usr/bin/env python3
"""Remove saved block/404 pages from a corpus.

Safety: the original file is moved (not deleted) under
/data/opencode/_archive/removed/<name>/, the matching _meta file is removed,
the corpus _index.jsonl is filtered, and every offending URL is appended to
docs/_excluded.json so incremental updaters never re-add it.

Usage:
  python3 shared/repair_corpus.py --name sarvam --root sarvam-docs/docs \
      --index sarvam-docs/docs/_index.jsonl --meta sarvam-docs/docs/_meta \
      --skip-sidecars false
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import docguard as DG

FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)
ARCHIVE = Path("/data/opencode/_archive/removed")


def fm(text: str):
    m = FM_RE.match(text)
    if not m:
        return {}, text
    d = {}
    for line in m.group(1).splitlines():
        if ": " in line:
            k, v = line.split(": ", 1)
            d[k] = v.strip().strip('"')
    return d, text[m.end():]


def iter_pages(root: Path, skip_sidecars: bool):
    for p in root.rglob("*.md"):
        s = "/" + str(p)
        if skip_sidecars and any(x in s for x in ("/_meta/", "/_llms/", "/_d/", "/_subdomains/", "/_excluded/")):
            continue
        if "/docs/reference/" in s:
            continue
        yield p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", required=True)
    ap.add_argument("--root", required=True, type=Path)
    ap.add_argument("--index", type=Path, default=None)
    ap.add_argument("--meta", type=Path, default=None)
    ap.add_argument("--exclude-file", type=Path, default=None)
    ap.add_argument("--skip-sidecars", default="true")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    skip = a.skip_sidecars.lower() != "false"
    root = a.root.resolve()
    archive = ARCHIVE / a.name
    removed_urls, removed_files = set(), []
    pages = blocked = notfound = 0

    for p in iter_pages(root, skip):
        pages += 1
        try:
            text = p.read_text(errors="replace")
        except Exception:
            continue
        d, _body = fm(text)
        title = d.get("title", "")
        url = d.get("url", "")
        kind = None
        if DG.is_block_page(text, title):
            kind = "block"
        elif DG.is_404_page(text, title):
            kind = "404"
        if not kind:
            continue
        rel = p.relative_to(root)
        removed_files.append(str(rel))
        if url:
            removed_urls.add(url)
        if kind == "block":
            blocked += 1
        else:
            notfound += 1
        if not a.dry_run:
            dst = archive / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(p), str(dst))
            if a.meta:
                mrel = rel.with_suffix(".json")
                mp = a.meta / mrel
                if mp.exists():
                    mp.unlink()
        print(f"  [{kind}] {rel}  <- {url}")

    if a.index and a.index.exists() and not a.dry_run:
        tmp = a.index.with_suffix(".tmp")
        kept = dropped = 0
        with a.index.open() as fin, tmp.open("w") as fout:
            for line in fin:
                if not line.strip():
                    continue
                try:
                    row = json.loads(line)
                except Exception:
                    fout.write(line)
                    continue
                if row.get("url") in removed_urls or row.get("file") in removed_files:
                    dropped += 1
                else:
                    fout.write(line)
                    kept += 1
        tmp.replace(a.index)
        print(f"index: kept={kept} dropped={dropped}")

    if a.exclude_file and not a.dry_run:
        cur = []
        if a.exclude_file.exists():
            try:
                cur = json.loads(a.exclude_file.read_text())
            except Exception:
                cur = []
        merged = sorted(set(cur) | removed_urls)
        a.exclude_file.write_text(json.dumps(merged, indent=2) + "\n")
        print(f"excluded: {len(merged)} urls -> {a.exclude_file}")

    print(f"{a.name}: pages={pages} removed={len(removed_files)} block={blocked} 404={notfound}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
