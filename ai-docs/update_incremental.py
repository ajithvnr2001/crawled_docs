#!/usr/bin/env python3
"""Incremental update for ai.google.dev.

Three lanes:
  1. NEW      - sitemap URLs not indexed yet
  2. STALE    - pages whose sitemap lastmod is newer than our fetched_at
  3. REPAIR   - pages currently holding an anti-bot CAPTCHA/OAuth interstitial

Usage:
  python3 update_incremental.py --check-only
  python3 update_incremental.py
  python3 update_incremental.py --repair-cap 1000
  python3 update_incremental.py --force URL
"""
import argparse, json, os, re, pathlib, asyncio, sys
from urllib.parse import urlparse, urljoin, urldefrag
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import crawl_ai as C

DOCS = C.OUT_ROOT
STATE = C.STATE_FILE
REFRESH_CAP = 100   # max stale-page refetches per run (newest first)
REPAIR_CAP = 300    # max blocked-page repairs per run

# Strong markers of a saved CAPTCHA/OAuth page (never legitimate docs text).
BLOCK_RE = re.compile(
    r"please type the characters|please enable images|google\.com/sorry/image|"
    r"ai\.google\.dev/oauth2authorize|our systems have detected unusual traffic|"
    r"sign in - google accounts",
    re.I,
)

# Sitemap URLs whose origin is broken (verified by hand): excluded from auto-update
# so the daily Action doesn't re-add an error page every run.
KNOWN_BROKEN = {
    # serves Next.js "This page couldn't load" (was HTTP 500 at crawl time)
    "https://ai.google.dev/ms-agent-harness-dotnet/tutorials/ai-powered-textarea/step-2-setup-copilotkit/",
    # still advertised in sitemap but returns 404
    "https://ai.google.dev/edge/mediapipe/solutions/genai/rag/android/",
    "https://ai.google.dev/palm_docs/deprecation/",
    "https://ai.google.dev/robots.txt",
}

# Auto-excluded URLs pruned by shared/repair_corpus.py (block/404 pages).
try:
    KNOWN_BROKEN |= set(json.loads((pathlib.Path(C.OUT_ROOT) / "_excluded.json").read_text()))
except Exception:
    pass

async def live_sitemaps():
    """Read sitemap.xml, follow its child sitemap(s), return canonical URLs + lastmod.

    The index itself only contains one <loc> (the child sitemap); parsing it as
    docs made new/stale detection a no-op. Child sitemaps are ~19 MB.
    """
    out, lastmod = {}, {}
    c = await C.get_httpx_client()

    async def fetch(u):
        r = await c.get(u, timeout=90)
        if C.is_block_page(r.text):
            try:
                await c.get(C.WARM_URL)
            except Exception:
                pass
            r = await c.get(u, timeout=90)
        if C.is_block_page(r.text):
            raise RuntimeError(f"blocked sitemap {u}")
        r.raise_for_status()
        return r.text

    index_xml = await fetch("https://ai.google.dev/sitemap.xml")
    child_locs = [urljoin("https://ai.google.dev/", m)
                  for m in re.findall(r"<sitemap>\s*<loc>([^<]+)</loc>", index_xml)]
    if not child_locs and "<urlset" in index_xml:
        child_locs = ["https://ai.google.dev/sitemap.xml"]

    urls, lm = set(), {}
    for child in child_locs:
        xml = index_xml if child.endswith("sitemap.xml") and "<urlset" in index_xml else await fetch(child)
        for block in re.findall(r"<url>(.*?)</url>", xml, re.S):
            loc = re.search(r"<loc>([^<]+)</loc>", block)
            if not loc:
                continue
            n = C.normalize_url(loc.group(1))
            if not n:
                continue
            urls.add(n)
            d = re.search(r"<lastmod>([^<]+)</lastmod>", block)
            if d and (n not in lm or d.group(1) > lm[n]):
                lm[n] = d.group(1)
    if not urls:
        raise RuntimeError("sitemap had no <url> entries")
    out["docs"] = sorted(urls)
    return out, lm

async def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check-only", action="store_true")
    ap.add_argument("--force", default=None)
    ap.add_argument("--concurrency", type=int, default=4)
    ap.add_argument("--repair-cap", type=int, default=REPAIR_CAP)
    a = ap.parse_args()
    idx = [json.loads(l) for l in open(DOCS / "_index.jsonl")] if (DOCS / "_index.jsonl").exists() else []
    indexed = set(r["url"] for r in idx)
    from urllib.parse import unquote
    idec = {unquote(u) for u in indexed}
    try:
        live, lastmod = await live_sitemaps()
    except Exception as e:
        # Do not lose the repair lane when Google throttles the sitemap fetch.
        print(f"sitemap fetch failed: {e}")
        live, lastmod = {}, {}
    new = {}
    for k, urls in live.items():
        miss = [u for u in urls if u not in indexed and unquote(u) not in idec and ".json" not in u and "`" not in u and u not in KNOWN_BROKEN]
        new[k] = miss
        print(f"{k}: live={len(urls)} indexed~{len(indexed)} new={len(miss)}")
        for u in miss[:20]: print(f"  NEW: {u}")
    total_new = sum(len(v) for v in new.values())
    # stale: sitemap lastmod newer than our _meta fetched_at (newest first, capped)
    stale = []
    if lastmod:
        for mfile in (DOCS / "_meta").rglob("*.json"):
            try:
                m = json.loads(mfile.read_text())
            except Exception:
                continue
            u, fa = m.get("url"), m.get("fetched_at")
            d = lastmod.get(u) if u else None
            if not u or not fa or not d:
                continue
            if u in set(sum(new.values(), [])) or u in KNOWN_BROKEN:
                continue
            try:
                from datetime import datetime as _dt
                if _dt.fromisoformat(d.replace("Z", "+00:00")) > _dt.fromisoformat(fa):
                    stale.append((d, u))
            except Exception:
                pass
    stale.sort(reverse=True)
    refresh = [u for _, u in stale[:REFRESH_CAP]]
    print(f"stale: {len(stale)}, refreshing newest {len(refresh)}")

    # blocked repair lane: indexed pages that currently contain a CAPTCHA/OAuth page
    blocked = []
    for row in idx:
        u, rel = row.get("url"), row.get("file")
        if not u or not rel or u in KNOWN_BROKEN:
            continue
        fp = DOCS / rel
        try:
            if fp.exists() and BLOCK_RE.search(fp.read_text(errors="replace")[:30000]):
                blocked.append(u)
        except Exception:
            continue
    print(f"blocked: {len(blocked)}, repairing up to {a.repair_cap}")
    in_other = set(refresh) | {u for v in new.values() for u in v}
    repair = [u for u in blocked if u not in in_other][:a.repair_cap]
    targets = ([a.force] if a.force
               else [u for v in new.values() for u in v] + refresh + repair)
    refresh_urls = set(refresh)
    if not a.check_only:
        # daily verification stamp (committed even when nothing new)
        from datetime import datetime, timezone
        now = datetime.now(timezone.utc)
        stamp = {"date": now.strftime("%F"), "at": now.isoformat(),
                 "new": {k: len(v) for k, v in new.items()},
                 "refreshed": len(refresh), "stale_total": len(stale),
                 "blocked_total": len(blocked), "repaired": len(repair),
                 "total_index": len(indexed) + (1 if a.force else 0)}
        (DOCS / "_last_verified.json").write_text(json.dumps(stamp, indent=2))
        try:
            mp = DOCS / "_manifest.json"
            m = json.loads(mp.read_text()) if mp.exists() else {}
            m["last_verified"] = stamp["date"]
            m["generated_at"] = stamp["at"]
            mp.write_text(json.dumps(m, indent=2))
        except Exception as e:
            print("stamp manifest skip:", e)
        try:  # keep README verification date fresh (committed by Actions)
            for _rp in [C.REPO_ROOT / "README.md", C.REPO_ROOT / "guide_code" / "README.md"]:
                if _rp.exists():
                    _t = _rp.read_text()
                    _t2 = re.sub(r"Last verified: \d{4}-\d{2}-\d{2}", f"Last verified: {stamp['date']}", _t)
                    _t2 = re.sub(r"## Results \(verified \d{4}-\d{2}-\d{2}\)", f"## Results (verified {stamp['date']})", _t2)
                    if _t2 != _t:
                        _rp.write_text(_t2)
                        print(f"readme date -> {stamp['date']} ({_rp})")
        except Exception as e:
            print("readme stamp skip:", e)
        print(f"stamped {stamp['date']} (new={total_new} refresh={len(refresh)} repair={len(repair)})")
    if a.check_only or not targets:
        print("check-only" if a.check_only else "no new docs — up to date")
        return
    print(f"fetching {len(targets)} docs ({total_new} new + {len(refresh)} refresh + {len(repair)} repair)...")
    st = json.load(open(STATE)) if STATE.exists() else {"visited": {}, "failed": {}}
    vs, failed = st.get("visited", {}), st.get("failed", {})
    from datetime import datetime, timezone
    lines = [json.loads(l) for l in open(DOCS / "_index.jsonl")] if (DOCS / "_index.jsonl").exists() else []
    if len({r["url"] for r in lines}) != len(lines):  # drop dupes from legacy appends
        seen, ded = set(), []
        for r in reversed(lines):
            if r["url"] not in seen:
                seen.add(r["url"]); ded.append(r)
        lines = list(reversed(ded))
    pos = {r["url"]: i for i, r in enumerate(lines)}
    sem = asyncio.Semaphore(a.concurrency)
    ok = fail = 0
    async def one(url):
        nonlocal ok, fail
        async with sem:
            try:
                data = await C.fetch_one(url)
                rel = C.url_to_relpath(url); fp = DOCS / rel
                fp.parent.mkdir(parents=True, exist_ok=True)
                fm = f"---\nurl: {url}\ntitle: {json.dumps(data['title'])[1:-1]}\nmethod: {data['method']}\nfetched_at: {datetime.now(timezone.utc).isoformat()}\n---\n\n"
                fp.write_text(fm + data["markdown"], encoding="utf-8")
                mr = pathlib.Path("_meta") / rel.with_suffix(".json")
                (DOCS / mr).parent.mkdir(parents=True, exist_ok=True)
                (DOCS / mr).write_text(json.dumps({"url": url, "file": str(rel), "title": data["title"], "method": data["method"], "fetched_at": datetime.now(timezone.utc).isoformat()}, indent=2))
                vs[url] = {"file": str(rel), "title": data["title"], "method": data["method"]}
                row = {"url": url, "file": str(rel), "title": data["title"], "method": data["method"]}
                if url in pos:
                    lines[pos[url]] = row
                    print(f"[refresh] {url}")
                else:
                    pos[url] = len(lines); lines.append(row)
                    print(f"[new] {url}")
                failed.pop(url, None)
                ok += 1
            except Exception as e:
                failed[url] = str(e)[:300]; fail += 1; print(f"[fail] {url}: {e}")
    await asyncio.gather(*(one(u) for u in targets))
    (DOCS / "_index.jsonl").write_text("".join(json.dumps(r) + "\n" for r in lines))
    try:
        if C._crawler is not None: await C._crawler.close()
    except Exception: pass
    open(STATE, "w").write(json.dumps({"visited": vs, "failed": failed}))
    print(f"done: ok={ok} fail={fail}")

if __name__ == "__main__":
    asyncio.run(main())
