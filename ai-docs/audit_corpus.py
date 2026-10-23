#!/usr/bin/env python3
"""Integrity audit for the ai.google.dev mirror.

Scans every mirrored page and exits nonzero on hard errors:

  - anti-bot CAPTCHA / OAuth pages saved as docs
  - 404 / error pages saved as docs
  - index rows whose Markdown file is missing
  - Markdown files that are not present in _index.jsonl
  - duplicate index URLs
  - relative image URLs (GitHub cannot render them)

Warns (without failing) on thin pages (app shells) and recorded fetch failures.

Usage:
  python3 audit_corpus.py
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import crawl_ai as C

DOCS = C.OUT_ROOT
BLOCK_RE = C._BLOCK_RE
MIN_BODY = 400
KNOWN_THIN = {
    # static shell for a client-rendered status dashboard; no readable content
    "https://aistudio.google.com/status/",
}


def split_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}, text
    fm = {}
    for line in m.group(1).splitlines():
        if ": " in line:
            k, v = line.split(": ", 1)
            fm[k] = v.strip().strip('"')
    return fm, text[m.end():]


def main():
    blocked, notfound, thin, relimg, missing = [], [], [], [], []
    titles_eq_url, md_files = [], []
    pages = img_total = pages_with_img = 0

    for p in sorted(DOCS.rglob("*.md")):
        if p.name.startswith("_") and p.name != "_index.md":
            continue
        pages += 1
        md_files.append(str(p.relative_to(DOCS)))
        try:
            text = p.read_text(errors="replace")
        except Exception as e:
            missing.append((str(p), f"unreadable: {e}"))
            continue
        fm, body = split_frontmatter(text)
        url = fm.get("url", "")

        if BLOCK_RE.search(text[:30000]):
            blocked.append(str(p))

        head = body.lstrip()[:300]
        title = fm.get("title", "").lower()
        if (title in ("404 not found", "page not found")
                or head.startswith("# Error: Not Found")
                or "was not found on this server" in head):
            notfound.append(str(p))

        plain = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", body)
        plain = re.sub(r"\[[^\]]*\]\([^)]*\)", "", plain)
        if len(plain.strip()) < MIN_BODY and url not in KNOWN_THIN:
            thin.append((str(p), len(plain.strip()), url))

        imgs = re.findall(r"!\[[^\]]*\]\(([^)\s]+)", body)
        if imgs:
            pages_with_img += 1
            img_total += len(imgs)
        for u in imgs:
            if not re.match(r"https?://", u):
                relimg.append((str(p), u))

        if url and fm.get("title", "") == url:
            titles_eq_url.append(str(p))

    idx = []
    if (DOCS / "_index.jsonl").exists():
        idx = [json.loads(l) for l in open(DOCS / "_index.jsonl") if l.strip()]
    urls = [r.get("url") for r in idx]
    dupes = len(urls) - len(set(urls))
    indexed_files = {r.get("file") for r in idx}
    unindexed = [f for f in md_files if f not in indexed_files]
    for r in idx:
        rel = r.get("file", "")
        if not rel or not (DOCS / rel).exists():
            missing.append((r.get("url"), rel))

    failed = {}
    if C.STATE_FILE.exists():
        try:
            failed = json.loads(C.STATE_FILE.read_text()).get("failed", {})
        except Exception:
            pass

    hard = len(blocked) + len(notfound) + len(missing) + dupes + len(relimg) + len(unindexed)
    print(f"pages={pages} index={len(idx)} unique={len(set(urls))}")
    print(f"images={img_total} across {pages_with_img} pages")
    print(f"hard errors: blocked={len(blocked)} notfound={len(notfound)} "
          f"missing={len(missing)} unindexed={len(unindexed)} dupes={dupes} relative_images={len(relimg)}")
    if blocked:
        for p in blocked[:10]:
            print(f"  BLOCKED: {p}")
    if notfound:
        for p in notfound[:10]:
            print(f"  404: {p}")
    if missing:
        for u, rel in missing[:10]:
            print(f"  MISSING: {u} -> {rel}")
    if unindexed:
        for f in unindexed[:10]:
            print(f"  UNINDEXED: {f}")
    if relimg:
        for p, u in relimg[:10]:
            print(f"  REL-IMG: {p} -> {u}")
    print(f"warnings: thin={len(thin)} title_eq_url={len(titles_eq_url)} failed_state={len(failed)}")
    for p, n, u in thin[:5]:
        print(f"  THIN ({n} chars): {u or p}")
    for p in titles_eq_url[:5]:
        print(f"  TITLE=URL: {p}")
    for u, e in list(failed.items())[:5]:
        print(f"  FAILED: {u} -> {str(e)[:100]}")

    if hard:
        print("RESULT: FAIL")
        sys.exit(1)
    print("RESULT: OK")


if __name__ == "__main__":
    main()
