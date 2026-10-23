#!/usr/bin/env python3
"""Integrity audit for one corpus inside the crawled_docs monorepo.

Hard errors (exit 1):
  * saved CAPTCHA / OAuth / anti-bot interstitial page
  * 404 page served with HTTP 200
  * root-relative / document-relative image URL still present
  * _index.jsonl row whose file does not exist
  * duplicate index entries

Warnings (do not fail): thin pages, files not listed in the index.

Usage:
  python3 shared/audit_corpus.py --name ai-docs --root ai-docs/docs
  python3 shared/audit_corpus.py --name gcpdocs --root gcpdocs/docs --skip-index
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import docguard as DG

FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)
SIDECAR = ("/_meta/", "/_llms/", "/_d/", "/_excluded/", "/docs/reference/")
_SIDECAR_ACTIVE = SIDECAR
THIN_CHARS = 200


def frontmatter(text: str):
    m = FM_RE.match(text)
    if not m:
        return {}, text
    d = {}
    for line in m.group(1).splitlines():
        if ": " in line:
            k, v = line.split(": ", 1)
            d[k] = v.strip().strip('"')
    return d, text[m.end():]


def is_sidecar(rel: str) -> bool:
    return any(x in "/" + rel for x in _SIDECAR_ACTIVE)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", required=True)
    ap.add_argument("--root", required=True, type=Path)
    ap.add_argument("--index", type=Path, default=None)
    ap.add_argument("--skip-index", action="store_true")
    ap.add_argument("--skip-sidecars", default="true")
    ap.add_argument("--skip-subdomains", action="store_true")
    a = ap.parse_args()
    skip_sidecars = a.skip_sidecars.lower() != "false"
    root = a.root.resolve()
    global _SIDECAR_ACTIVE
    _SIDECAR_ACTIVE = SIDECAR + (("/_subdomains/",) if a.skip_subdomains else ())
    index = a.index or (root / "_index.jsonl")

    blocked: list[str] = []
    notfound: list[str] = []
    relimg: list[str] = []
    thin: list[str] = []
    pages = 0
    present: set[str] = set()

    for p in sorted(root.rglob("*.md")):
        rel = str(p.relative_to(root))
        present.add(rel)
        if skip_sidecars and is_sidecar(rel):
            continue
        pages += 1
        try:
            text = p.read_text(errors="replace")
        except Exception:
            continue
        d, _body = frontmatter(text)
        title = d.get("title", "")
        url = d.get("url", "")
        if DG.is_block_page(text, title):
            blocked.append(rel)
        if DG.is_404_page(text, title):
            notfound.append(rel)
        if url and DG.absolutize_images(text, url) != text:
            relimg.append(rel)
        if len(text) < THIN_CHARS:
            thin.append(rel)

    missing_index: list[str] = []
    dup_url: list[str] = []
    dup_file: list[str] = []
    unindexed: list[str] = []
    rows = 0
    if not a.skip_index and index.exists():
        seen_url: set[str] = set()
        seen_file: set[str] = set()
        for line in index.open():
            if not line.strip():
                continue
            try:
                r = json.loads(line)
            except Exception:
                continue
            rows += 1
            f = r.get("file")
            u = r.get("url")
            if f and not (root / f).exists():
                missing_index.append(f)
            if f and f in seen_file:
                dup_file.append(f)
            seen_file.add(f)
            if u and u in seen_url:
                dup_url.append(u)
            seen_url.add(u)
        for rel in present:
            if rel not in seen_file and not is_sidecar(rel):
                unindexed.append(rel)

    hard = len(blocked) + len(notfound) + len(relimg) + len(missing_index) + len(dup_url)
    print(
        f"=== {a.name}: pages={pages} blocked={len(blocked)} notfound={len(notfound)} "
        f"relative_images={len(relimg)} index_missing={len(missing_index)} "
        f"index_dupes={len(dup_url)} index_file_collisions={len(dup_file)} "
        f"unindexed={len(unindexed)} thin={len(thin)} hard={hard}"
    )
    for label, items in (
        ("BLOCKED", blocked),
        ("404", notfound),
        ("RELIMG", relimg),
        ("IDX_MISSING", missing_index),
        ("IDX_DUP", dup_url),
        ("IDX_COLLISION", dup_file),
    ):
        for x in items[:20]:
            print(f"  {label}: {x}")
    for x in unindexed[:10]:
        print(f"  UNINDEXED: {x}")
    return 1 if hard else 0


if __name__ == "__main__":
    raise SystemExit(main())
