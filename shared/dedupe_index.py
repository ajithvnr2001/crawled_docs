#!/usr/bin/env python3
"""Collapse duplicate `_index.jsonl` rows that point at the same file.

Some crawlers record both `https://host` and `https://host/` for a subdomain
landing page; both map to the same `_index.md`. Keep the row whose url matches
the file's frontmatter, otherwise the last row.

Usage:
  python3 shared/dedupe_index.py --root ai-docs/docs
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)


def file_url(path: Path) -> str:
    try:
        m = FM_RE.match(path.read_text(errors="replace"))
    except Exception:
        return ""
    if not m:
        return ""
    for line in m.group(1).splitlines():
        if line.startswith("url: "):
            return line.split("url: ", 1)[1].strip().strip('"')
    return ""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True, type=Path)
    a = ap.parse_args()
    root = a.root.resolve()
    idx = root / "_index.jsonl"
    rows = [json.loads(l) for l in idx.open() if l.strip()]
    chosen: dict[str, dict] = {}
    order: list[str] = []
    dropped = 0
    for r in rows:
        f = r.get("file")
        if not f:
            continue
        if f not in chosen:
            chosen[f] = r
            order.append(f)
            continue
        fu = file_url(root / f)
        if r.get("url") == fu and chosen[f].get("url") != fu:
            chosen[f] = r
        dropped += 1
    tmp = idx.with_suffix(".tmp")
    with tmp.open("w") as out:
        for f in order:
            out.write(json.dumps(chosen[f], ensure_ascii=False) + "\n")
    tmp.replace(idx)
    print(f"{a.name if hasattr(a,'name') else root}: rows={len(rows)} kept={len(order)} dropped={dropped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
