#!/usr/bin/env python3
"""Absolutize relative/root-relative image URLs across a corpus.

Usage:
  python3 shared/postprocess_images.py --root cloudflare/docs
  python3 shared/postprocess_images.py --root gcpdocs/docs --skip-sidecars true
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import docguard as DG

FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)


def page_url(text: str) -> str:
    m = FM_RE.match(text)
    if not m:
        return ""
    for line in m.group(1).splitlines():
        if line.startswith("url: "):
            return line.split("url: ", 1)[1].strip().strip('"')
    return ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True, type=Path)
    ap.add_argument("--skip-sidecars", default="true")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    skip = a.skip_sidecars.lower() != "false"
    root = a.root.resolve()
    seen = changed = rewritten = 0
    for p in sorted(root.rglob("*.md")):
        s = "/" + str(p)
        if skip and any(x in s for x in ("/_meta/", "/_llms/", "/_d/", "/_excluded/")):
            continue
        if "/docs/reference/" in s:
            continue
        try:
            text = p.read_text(errors="replace")
        except Exception:
            continue
        url = page_url(text)
        if not url:
            continue
        seen += 1
        new = DG.absolutize_images(text, url)
        if new != text:
            changed += 1
            rewritten += sum(1 for a, b in zip(text.splitlines(), new.splitlines()) if a != b)
            if not a.dry_run:
                p.write_text(new)
    print(f"{root}: pages={seen} changed={changed} lines={rewritten}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
