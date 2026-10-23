#!/usr/bin/env python3
"""Remove saved 404/error pages from the mirror.

Two passes:
  1. Markdown whose content is a 404/error page
  2. URLs recorded as 404 failures in crawl_state.json (their saved file may be
     a CAPTCHA page, e.g. blocked MediaPipe reference URLs)

Deletes the Markdown + _meta entry, drops the URL from _index.jsonl and
crawl_state.json, updates _manifest.json, and records pruned URLs in
docs/_excluded.json.

Usage:
  python3 prune_404.py
"""
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import crawl_ai as C

DOCS = C.OUT_ROOT


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


def is_404_markdown(text):
    fm, body = split_frontmatter(text)
    title = fm.get("title", "")
    if re.search(r"\b404\b", title) and re.search(r"not\s*found", title, re.I):
        return True
    head = body.lstrip()[:2000]
    if head.startswith("# 404") or head.startswith("# Error: Not Found"):
        return True
    if "The requested URL" in head and "was not found" in head:
        return True
    return False


def main():
    st = {"visited": {}, "failed": {}}
    if C.STATE_FILE.exists():
        try:
            st = json.loads(C.STATE_FILE.read_text())
        except Exception:
            pass

    failed_404 = []
    for u, err in list(st.get("failed", {}).items()):
        if re.search(r"\b404\b|not\s+found", str(err), re.I):
            failed_404.append(u)
    failed_404_set = set(failed_404)

    idx_path = DOCS / "_index.jsonl"
    rows = [json.loads(l) for l in open(idx_path) if l.strip()]
    keep, removed, deleted_dirs = [], [], set()

    for row in rows:
        rel = row.get("file", "")
        fp = DOCS / rel
        try:
            text = fp.read_text(errors="replace") if fp.exists() else ""
        except Exception:
            text = ""
        is_404 = (text and is_404_markdown(text)) or row.get("url") in failed_404_set
        if is_404:
            removed.append(row)
            try:
                fp.unlink()
            except FileNotFoundError:
                pass
            meta = DOCS / "_meta" / Path(rel).with_suffix(".json")
            try:
                meta.unlink()
            except FileNotFoundError:
                pass
            deleted_dirs.add(fp.parent)
        else:
            keep.append(row)

    idx_path.write_text("".join(json.dumps(r) + "\n" for r in keep))

    for r in removed:
        st.get("visited", {}).pop(r["url"], None)
        st.get("failed", {}).pop(r["url"], None)
    for u in failed_404:
        st.get("failed", {}).pop(u, None)
        st.get("visited", {}).pop(u, None)
    C.STATE_FILE.write_text(json.dumps(st))

    # manifest counters
    mp = DOCS / "_manifest.json"
    if mp.exists():
        try:
            m = json.loads(mp.read_text())
            m["visited"] = len(keep)
            m["pages"] = len(keep)
            m["pruned_404"] = m.get("pruned_404", 0) + len(removed)
            m["generated_at"] = datetime.now(timezone.utc).isoformat()
            mp.write_text(json.dumps(m, indent=2))
        except Exception as e:
            print("manifest update skipped:", e)

    excluded = {"generated_at": datetime.now(timezone.utc).isoformat(), "not_found": []}
    ep = DOCS / "_excluded.json"
    if ep.exists():
        try:
            excluded = json.loads(ep.read_text())
        except Exception:
            pass
    excluded.setdefault("not_found", [])
    excluded["generated_at"] = datetime.now(timezone.utc).isoformat()
    known = {x.get("url") for x in excluded["not_found"]}
    for r in removed:
        if r["url"] not in known:
            excluded["not_found"].append({"url": r["url"], "file": r.get("file", "")})
    for u in failed_404:
        if u not in known:
            excluded["not_found"].append({"url": u, "file": "", "reason": "404"})
    seen = set()
    unique = []
    for x in excluded["not_found"]:
        if x.get("url") not in seen:
            seen.add(x.get("url"))
            unique.append(x)
    excluded["not_found"] = unique
    ep.write_text(json.dumps(excluded, indent=2))

    for d in sorted(deleted_dirs, key=lambda x: len(x.parts), reverse=True):
        try:
            d.rmdir()
        except OSError:
            pass

    print(f"pruned 404 pages: {len(removed)} | remaining index rows: {len(keep)}")
    for r in removed[:10]:
        print("  -", r["url"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
