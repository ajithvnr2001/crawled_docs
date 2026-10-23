#!/usr/bin/env python3
"""
End-to-end crawler for https://ai.google.dev/ including subdomains.
Uses all three requested stacks:
  1. Scrapling (D4Vinci/Scrapling)  - fast static fetch + CSS/XPath extraction (primary)
  2. Crawl4AI (unclecode/crawl4AI)   - JS rendering fallback + markdown generation
  3. ScrapeGraphAI (ScrapeGraphAI/Scrapegraph-ai) - cleanup_html + convert_to_md (HTML->MD)

Saves markdown docs to /data/opencode/aidocs/docs
"""
import asyncio
import os
import re
import json
import time
import threading
import hashlib
import importlib.util
from pathlib import Path

# shared monorepo guard (path-relative; works from a fresh clone and the VM symlink)
import sys as _sys
_sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "shared"))
import docguard as DG
from urllib.parse import urlparse, urljoin, urldefrag, unquote
from datetime import datetime, timezone

import httpx
from bs4 import BeautifulSoup

# ---------- paths (repo-relative so GitHub Actions runners work; override via env) ----------
REPO_ROOT = Path(__file__).resolve().parent
BASE_URL = "https://ai.google.dev"
SITEMAP_INDEX = "https://ai.google.dev/sitemap.xml"
MAIN_LLMS = "https://ai.google.dev/llms.txt"
FULL_LLMS = "https://ai.google.dev/llms-full.txt"
OUT_ROOT = Path(os.environ.get("DOCS_OUT", str(REPO_ROOT / "docs")))
TOOLS_ROOT = Path(os.environ.get("TOOLS_DIR", str(REPO_ROOT / "tools")))
STATE_FILE = Path(os.environ.get("CRAWL_STATE", str(REPO_ROOT / "crawl_state.json")))
INDEX_FILE = OUT_ROOT / "_index.jsonl"
MANIFEST_FILE = OUT_ROOT / "_manifest.json"

OUT_ROOT.mkdir(parents=True, exist_ok=True)
(OUT_ROOT / "_subdomains").mkdir(exist_ok=True, parents=True)
(OUT_ROOT / "_llms").mkdir(exist_ok=True, parents=True)
(OUT_ROOT / "_meta").mkdir(exist_ok=True, parents=True)

# ---------- anti-bot handling ----------
# Google's edge serves an OAuth interstitial (302) or a CAPTCHA page to cold
# clients. A warm cookie jar from a normal docs page makes requests succeed.
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
WARM_URL = BASE_URL + "/gemini-api/docs"
_BLOCK_RE = re.compile(
    r"please type the characters|please enable images|google\.com/sorry/image|"
    r"ai\.google\.dev/oauth2authorize|our systems have detected unusual traffic|"
    r"sign in - google accounts",
    re.I,
)
_COOKIE = {"data": {}, "ts": 0.0}
_COOKIE_LOCK = threading.Lock()
_COOKIE_TTL = 600


def get_cookies(force=False):
    """Return a warm ai.google.dev cookie jar, refreshing it periodically."""
    now = time.time()
    with _COOKIE_LOCK:
        if not force and _COOKIE["data"] and now - _COOKIE["ts"] < _COOKIE_TTL:
            return dict(_COOKIE["data"])
        try:
            with httpx.Client(follow_redirects=True, timeout=30,
                              headers={"User-Agent": UA}) as c:
                r = c.get(WARM_URL)
                if r.status_code == 200:
                    _COOKIE["data"] = dict(c.cookies)
                    _COOKIE["ts"] = now
        except Exception:
            pass
        return dict(_COOKIE["data"])


def is_block_page(html, title=""):
    """True when a response is an anti-bot CAPTCHA / OAuth interstitial."""
    if not html:
        return False
    if _BLOCK_RE.search(html[:300000]):
        return True
    t = (title or "").strip().lower()
    return t in {"redirecting...", "sign in - google accounts"} or "sign in - google accounts" in t


def is_404_page(html, title=""):
    """True when the response is a 404 page served with HTTP 200."""
    t = (title or "").strip()
    if re.search(r"\b404\b", t) and re.search(r"not\s+found", t, re.I):
        return True
    if not html:
        return False
    head = html[:30000]
    if re.search(r"<h1[^>]*>\s*404\b", head, re.I):
        return True
    if "The requested URL" in head and "was not found" in head:
        return True
    return False

# ---------- load ScrapeGraphAI utils directly from cloned repo (bypass broken langchain imports) ----------
def load_module_from_file(name, filepath):
    spec = importlib.util.spec_from_file_location(name, filepath)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def _resolve_sg_utils():
    cands = [
        TOOLS_ROOT / "scrapegraph-ai" / "scrapegraphai" / "utils",
        REPO_ROOT / "tools" / "scrapegraph-ai" / "scrapegraphai" / "utils",
        Path("/data/opencode/cloudflare/tools/scrapegraph-ai/scrapegraphai/utils"),
    ]
    for c in cands:
        if (c / "convert_to_md.py").exists():
            return c
    try:  # pip-installed package fallback (utils files are langchain-free)
        import scrapegraphai
        c = Path(scrapegraphai.__file__).parent / "utils"
        if (c / "convert_to_md.py").exists():
            return c
    except Exception:
        pass
    return cands[0]

SCRAPEGRAPH_UTILS = _resolve_sg_utils()
convert_to_md_mod = load_module_from_file("sg_convert_to_md", str(SCRAPEGRAPH_UTILS / "convert_to_md.py"))
cleanup_html_mod = load_module_from_file("sg_cleanup_html", str(SCRAPEGRAPH_UTILS / "cleanup_html.py"))
sg_convert_to_md = convert_to_md_mod.convert_to_md
try:
    sg_cleanup_html = cleanup_html_mod.cleanup_html
    print("[scrapegraph-ai] loaded convert_to_md + cleanup_html from", SCRAPEGRAPH_UTILS)
except Exception as e:
    sg_cleanup_html = None
    print("[scrapegraph-ai] cleanup_html unavailable:", e)

# ---------- Scrapling ----------
from scrapling import Fetcher
print("[scrapling] Fetcher loaded:", Fetcher)

# ---------- Crawl4AI (lazy, only for fallback) ----------
_crawler = None
async def get_crawler():
    global _crawler
    if _crawler is None:
        from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode  # noqa
        from crawl4ai.async_webcrawler import BrowserConfig
        cookies = get_cookies()
        browser_cfg = BrowserConfig(
            headless=True, verbose=False, user_agent=UA,
            cookies=[{"name": k, "value": v, "domain": "ai.google.dev", "path": "/",
                      "secure": True, "sameSite": "None"}
                     for k, v in cookies.items()
                     if not k.startswith(("__Host-", "__Secure-"))] if cookies else None,
        )
        _crawler = AsyncWebCrawler(config=browser_cfg)
        await _crawler.start()
        print("[crawl4ai] AsyncWebCrawler started")
    return _crawler

# Shared httpx client (cookie-warmed) used by the final fallback.
_httpx_client = None
async def get_httpx_client():
    global _httpx_client
    if _httpx_client is None:
        _httpx_client = httpx.AsyncClient(
            follow_redirects=True, timeout=30, headers={"User-Agent": UA})
        try:
            await _httpx_client.get(WARM_URL)
        except Exception:
            pass
    return _httpx_client

# ---------- helpers ----------
ALLOWED_ROOT_SUFFIXES = (".google.dev", ".google.com")
MAIN_HOST = "ai.google.dev"

def normalize_url(u, base=BASE_URL):
    if not u:
        return None
    u = u.strip()
    if u.startswith("#") or u.startswith("mailto:") or u.startswith("tel:") or u.startswith("javascript:") or u.startswith("data:"):
        return None
    abs_u = urljoin(base, u)
    abs_u, _ = urldefrag(abs_u)
    try:
        p = urlparse(abs_u)
    except Exception:
        return None
    if p.scheme not in ("http", "https"):
        return None
    host = p.netloc.lower().split(":")[0]
    if host == "ai.google.dev" or host.endswith(".ai.google.dev") or host in ("aistudio.google.com", "saif.google", "discuss.ai.google.dev", "developer.android.com", "developer.chrome.com"):
        pass
    else:
        return None
    # skip binary assets
    low = p.path.lower()
    for ext in (".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".ico", ".css", ".js", ".woff", ".woff2", ".ttf", ".mp4", ".webm", ".zip", ".pdf", ".xml", ".aep", ".bin", ".gz", ".tar"):
        if low.endswith(ext):
            # allow .pdf? skip for now to keep docs focused, but record
            return None
    # canonicalize: map /index.md -> /, /index -> /, *.md (doc source) -> HTML url
    # e.g. /zaraz/history/versions/index.md -> /zaraz/history/versions/
    #      /zaraz/history/versions/index -> /zaraz/history/versions/
    #      /zaraz/history/versions.md -> /zaraz/history/versions/
    path = p.path
    # Google site-verification token files are not documentation
    if re.fullmatch(r"/google[0-9a-f]{16,}/?", path):
        return None
    if path.endswith("/index.md"):
        path = path[:-len("/index.md")] + "/"
    elif path.endswith("/index"):
        # be careful: /index as root file vs legit slug ending with -index? only strip exact /index segment
        path = path[:-len("/index")] + "/"
    elif path == "/index.md" or path == "/index":
        path = "/"
    elif path.endswith(".md"):
        # product llms.txt markdown source links: strip .md -> trailing slash
        path = path[:-3]
        if not path.endswith("/"):
            path = path + "/"
    # rebuild canonical url (drop query/fragment for docs; query hashed later only if needed)
    # keep query? docs don't need query; strip to dedupe (except search/page params handled via relpath hash, but we drop here)
    # Preserve query only if it looks like pagination? For now strip query to avoid dupes.
    canon = f"{p.scheme}://{p.netloc}{path}"
    # normalize trailing slash: keep "/" for root, ensure directory urls end with "/"
    # sitemap uses trailing slash, so enforce it for consistency (except files)
    if not canon.endswith("/") and "." not in canon.rsplit("/", 1)[-1]:
        canon = canon + "/"
    return canon

def url_to_relpath(url):
    p = urlparse(url)
    host = p.netloc.lower()
    path = unquote(p.path)
    # strip query for filename, but hash it if meaningful
    query = p.query
    path = path.strip("/")
    # canonical: trailing /index already stripped in normalize, but guard again
    if path.endswith("/index"):
        path = path[:-len("/index")].strip("/")
    if not path:
        fname = "_index"
    else:
        # remove trailing / already, keep hierarchy
        fname = path
    # sanitize each segment
    parts = []
    for seg in fname.split("/"):
        seg = re.sub(r'[<>:"\\|?*\x00-\x1F]', "_", seg).strip()
        if len(seg) > 120:
            seg = seg[:100] + "_" + hashlib.md5(seg.encode()).hexdigest()[:8]
        if seg in ("", ".", ".."):
            seg = "_"
        parts.append(seg)
    rel = "/".join(parts) if parts else "_index"
    if query:
        qh = hashlib.md5(query.encode()).hexdigest()[:8]
        rel = rel + f"__q_{qh}"
    if rel.endswith(".txt"):  # raw-text mirrors keep their filename
        return Path(rel) if host == MAIN_HOST else Path("_subdomains") / host / rel
    if host == MAIN_HOST:
        return Path(rel + ".md")
    else:
        return Path("_subdomains") / host / (rel + ".md")

def _page_title(soup):
    """Prefer the page h1 over the site-wide <title> suffix."""
    h1 = soup.find("h1")
    if h1:
        t = re.sub(r"\s+", " ", h1.get_text(" ", strip=True)).strip()
        if t:
            return t
    if soup.title and soup.title.string:
        t = soup.title.string.strip()
        t = re.sub(r"\s*\|\s*(Google AI for Developers|Gemini API|Google for Developers)\s*$", "", t)
        return re.sub(r"\s+", " ", t).strip(" |")
    return ""


def extract_main_content_html(html, base_url):
    """Keep the docs article body (DevSite-aware), fallback to main/body.

    DevSite's <main> includes the global nav/sidebar; div.devsite-article-body
    is the actual article and preserves images, tables and code samples.
    """
    soup = BeautifulSoup(html, "lxml")
    for tag in soup(["script", "style", "noscript", "svg"]):
        tag.decompose()
    title = _page_title(soup)
    main = (soup.select_one("div.devsite-article-body")
            or soup.find("article")
            or soup.find("main")
            or soup.find("div", {"id": "main-content"}))
    if main:
        for tag in main.select("nav, aside, .devsite-toc, .devsite-feedback"):
            tag.decompose()
        return str(main), title
    body = soup.find("body")
    if body:
        return str(body), title
    return html, title

def scrapegraph_markdown(html, url):
    try:
        return sg_convert_to_md(html, url)
    except Exception as e:
        # fallback html2text direct
        import html2text
        h = html2text.HTML2Text()
        h.ignore_links = False
        h.body_width = 0
        return h.handle(html)

# ---------- fetch with Scrapling (sync -> thread) ----------
def scrapling_fetch_sync(url):
    t0 = time.time()
    for attempt in range(2):
        cookies = get_cookies(force=attempt > 0)
        try:
            page = Fetcher.get(url, stealthy_headers=True, follow_redirects=True,
                               timeout=25, **({"cookies": cookies} if cookies else {}))
        except Exception:
            if attempt == 0:
                continue
            raise
        if page.status != 200:
            raise RuntimeError(f"scrapling status {page.status}")
        html = page.html_content
        if not html or len(html) < 500:
            raise RuntimeError("scrapling empty html")
        if is_block_page(html):
            _COOKIE["ts"] = 0.0
            if attempt == 0:
                continue
            raise RuntimeError("scrapling blocked page (captcha/oauth)")
        if is_404_page(html):
            raise RuntimeError("scrapling 404 page")
        soup = BeautifulSoup(html, "lxml")
        title = _page_title(soup)
        links = [a.get("href", "") for a in soup.find_all("a", href=True)]
        text_len = len(soup.get_text(" ", strip=True))
        return {"html": html, "links": links, "title": title,
                "text_len": text_len, "elapsed": time.time() - t0}
    raise RuntimeError("scrapling blocked page (captcha/oauth)")

async def crawl4ai_fetch(url):
    crawler = await get_crawler()
    from crawl4ai import CrawlerRunConfig, CacheMode
    cfg = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        only_text=False,
        excluded_tags=["nav", "footer", "header", "aside", "script", "style"],
        wait_until="domcontentloaded",
        page_timeout=45000,
    )
    res = await crawler.arun(url=url, config=cfg)
    if not res or not res.success:
        raise RuntimeError(f"crawl4ai failed: {getattr(res, 'error_message', 'unknown')}")
    html = res.html or ""
    md = res.markdown or ""
    if getattr(res, "status_code", 200) and int(res.status_code) >= 400:
        raise RuntimeError(f"crawl4ai status {res.status_code}")
    if is_block_page(html) or is_block_page(md):
        raise RuntimeError("crawl4ai blocked page (captcha/oauth)")
    if is_404_page(html):
        raise RuntimeError("crawl4ai 404 page")
    # res.links: dict with internal/external
    links = []
    try:
        internal = (res.links or {}).get("internal", []) if isinstance(res.links, dict) else []
        external = (res.links or {}).get("external", []) if isinstance(res.links, dict) else []
        for l in (internal + external):
            href = l.get("href") if isinstance(l, dict) else str(l)
            if href:
                links.append(href)
    except Exception:
        pass
    title = ""
    try:
        if res.metadata and isinstance(res.metadata, dict):
            title = res.metadata.get("title", "") or ""
    except Exception:
        pass
    return {"html": html, "markdown": md, "links": links, "title": title}

async def fetch_one(url):
    """Try Scrapling -> Crawl4AI -> httpx. Returns dict with markdown, html, title, links, method."""
    # 0) raw-text mirrors (*.md.txt): fetch body as-is, no rendering needed
    if url.endswith(".txt"):
        c = await get_httpx_client()
        resp = await c.get(url)
        if is_block_page(resp.text):
            try:
                await c.get(WARM_URL)
            except Exception:
                pass
            resp = await c.get(url)
        if is_block_page(resp.text):
            raise RuntimeError(f"blocked raw text {url}")
        resp.raise_for_status()
        body = resp.text
        title = url.rsplit("/", 1)[-1].removesuffix(".md.txt").replace("-", " ").replace("_", " ")
        md = f"# {title}\n\n> Source: {url}\n\n" + body
        return {"url": url, "title": title, "html": "", "markdown": md, "links": [], "method": "httpx-raw-text"}
    # 1) Scrapling
    try:
        r = await asyncio.to_thread(scrapling_fetch_sync, url)
        html = r["html"]
        main_html, parsed_title = extract_main_content_html(html, url)
        title = r["title"] or parsed_title or url
        md_body = scrapegraph_markdown(main_html, url)
        header = f"# {title}\n\n> Source: {url}\n\n"
        md = header + md_body
        if len(md.strip()) < 800:
            raise RuntimeError(f"scrapling thin content ({len(md)} chars), fallback to crawl4ai")
        return {"url": url, "title": title, "html": html, "markdown": md, "links": r["links"], "method": "scrapling+scrapegraph"}
    except Exception as e1:
        last_err = f"scrapling: {e1}"
    # 2) Crawl4AI
    try:
        r = await crawl4ai_fetch(url)
        html = r["html"]
        md_raw = r["markdown"]
        title = r["title"]
        if not title:
            _, parsed_title = extract_main_content_html(html, url) if html else ("", "")
            title = parsed_title or url
        # run scrapegraph convert on main html too for consistency, prefer crawl4ai markdown if longer
        try:
            main_html, _ = extract_main_content_html(html, url) if html else ("", title)
            md_sg = scrapegraph_markdown(main_html, url) if main_html else ""
        except Exception:
            md_sg = ""
        md_best = md_raw if len(md_raw or "") >= len(md_sg or "") else md_sg
        header = f"# {title}\n\n> Source: {url}\n\n"
        md = header + (md_best or "")
        if len(md.strip()) < 200:
            raise RuntimeError(f"crawl4ai thin content: {last_err}")
        return {"url": url, "title": title, "html": html, "markdown": md, "links": r["links"], "method": f"crawl4ai+scrapegraph ({last_err})"}
    except Exception as e2:
        last_err2 = f"{last_err} | crawl4ai: {e2}"
    # 3) httpx fallback (shared, cookie-warmed client)
    try:
        c = await get_httpx_client()
        resp = await c.get(url)
        html = resp.text
        if is_block_page(html):
            try:
                await c.get(WARM_URL)  # refresh cookies
            except Exception:
                pass
            resp = await c.get(url)
            html = resp.text
        if is_block_page(html):
            raise RuntimeError("httpx blocked page (captcha/oauth)")
        if is_404_page(html):
            raise RuntimeError("httpx 404 page")
        resp.raise_for_status()
        main_html, parsed_title = extract_main_content_html(html, url)
        md_body = scrapegraph_markdown(main_html, url)
        title = parsed_title or url
        header = f"# {title}\n\n> Source: {url}\n\n"
        md = header + md_body
        soup = BeautifulSoup(html, "lxml")
        links = [a.get("href", "") for a in soup.find_all("a", href=True)]
        return {"url": url, "title": title, "html": html, "markdown": md, "links": links, "method": f"httpx+scrapegraph ({last_err2})"}
    except Exception as e3:
        raise RuntimeError(f"all fetchers failed for {url}: {last_err2} | httpx: {e3}")

# ---------- sitemap + llms discovery ----------
async def load_sitemap_urls():
    urls = set()
    async with httpx.AsyncClient(follow_redirects=True, timeout=30) as c:
        r = await c.get(SITEMAP_INDEX)
        r.raise_for_status()
        import xml.etree.ElementTree as ET
        try:
            root = ET.fromstring(r.text)
            ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
            # sitemap index?
            sitemaps = [e.find("s:loc", ns).text for e in root.findall("s:sitemap", ns) if e.find("s:loc", ns) is not None]
            if sitemaps:
                print(f"[sitemap] found {len(sitemaps)} sitemap files")
                for sm in sitemaps:
                    try:
                        rr = await c.get(sm, timeout=30)
                        rr.raise_for_status()
                        rt = ET.fromstring(rr.text)
                        locs = [e.find("s:loc", ns).text for e in rt.findall("s:url", ns) if e.find("s:loc", ns) is not None]
                        for u in locs:
                            n = normalize_url(u)
                            if n:
                                urls.add(n)
                        print(f"[sitemap] {sm}: {len(locs)} urls (total {len(urls)})")
                    except Exception as e:
                        print(f"[sitemap] failed {sm}: {e}")
            else:
                locs = [e.find("s:loc", ns).text for e in root.findall("s:url", ns) if e.find("s:loc", ns) is not None]
                if not locs:  # regex fallback
                    locs = re.findall(r"<loc>([^<]+)</loc>", r.text)
                for u in locs:
                    n = normalize_url(u)
                    if n:
                        urls.add(n)
                print(f"[sitemap] urlset: {len(locs)} urls (total {len(urls)})")
        except Exception as e:
            print(f"[sitemap] parse failed, regex fallback: {e}")
            for u in re.findall(r"<loc>([^<]+)</loc>", r.text):
                n = normalize_url(u)
                if n:
                    urls.add(n)
    return sorted(urls)

async def load_llms_urls():
    urls = set()
    llms_files = []
    async with httpx.AsyncClient(follow_redirects=True, timeout=30) as c:
        for llms_url in [MAIN_LLMS, FULL_LLMS]:
            try:
                r = await c.get(llms_url, timeout=30)
                if r.status_code != 200:
                    print(f"[llms] {llms_url} -> {r.status_code}")
                    continue
                safe = llms_url.replace("https://", "").replace("/", "_")
                (OUT_ROOT / "_llms" / safe).write_text(r.text[:5000000], encoding="utf-8")
                llms_files.append(llms_url)
                print(f"[llms] saved {llms_url} ({len(r.text)} chars)")
                for m in re.findall(r"\(https://ai\.google\.dev[^\)]+\)", r.text):
                    m = m.strip("()")
                    n = normalize_url(m)
                    if n:
                        urls.add(n)
                for m in re.findall(r"https://ai\.google\.dev/[^\s\)\]]+", r.text):
                    m = m.rstrip(").,")
                    if m.endswith(".txt"):
                        continue
                    n = normalize_url(m)
                    if n:
                        urls.add(n)
            except Exception as e:
                print(f"[llms] failed {llms_url}: {e}")
    print(f"[llms] discovered {len(urls)} urls from llms.txt")
    return sorted(urls), llms_files

# ---------- main crawl ----------
async def main(max_pages=15000, concurrency=4):
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    # load state
    visited = {}
    failed = {}
    if STATE_FILE.exists():
        try:
            st = json.loads(STATE_FILE.read_text())
            visited = st.get("visited", {})
            failed = st.get("failed", {})
            print(f"[state] resumed: {len(visited)} visited, {len(failed)} failed")
        except Exception as e:
            print(f"[state] corrupt, starting fresh: {e}")
    # seed urls
    sitemap_urls = await load_sitemap_urls()
    llms_urls, llms_files = await load_llms_urls()
    seeds = []
    seen_seed = set()
    for u in sitemap_urls + llms_urls + [BASE_URL + "/"]:
        if u not in seen_seed:
            seen_seed.add(u)
            seeds.append(u)
    print(f"[seed] sitemap={len(sitemap_urls)} llms-derived={len(llms_urls)} total seeds={len(seeds)}")
    # BFS queue: prioritize seeds not yet visited
    queue = asyncio.Queue()
    queued = set()
    for u in seeds:
        if u not in visited and u not in queued:
            await queue.put((u, 0))
            queued.add(u)
    # also track subdomain stats
    stats = {"ok": 0, "fail": 0, "skipped_existing": 0, "by_method": {}, "by_host": {}}
    # resume counts
    stats["ok"] = len(visited)
    # open index file append
    existing_index_urls = set(visited.keys())
    idx_f = open(INDEX_FILE, "a", encoding="utf-8")

    sem = asyncio.Semaphore(concurrency)

    async def worker(wid):
        nonlocal stats
        while True:
            try:
                url, depth = queue.get_nowait()
            except asyncio.QueueEmpty:
                return
            if len(visited) >= max_pages and url not in visited:
                # cap total pages (fixed: previously used queue.qsize which broke smoke tests)
                queue.task_done()
                continue
            rel = url_to_relpath(url)
            fpath = OUT_ROOT / rel
            # skip if file exists and visited (resume)
            if url in visited and fpath.exists():
                stats["skipped_existing"] += 1
                queue.task_done()
                continue
            # skip if file exists on disk but not in state (previous run)
            if fpath.exists() and fpath.stat().st_size > 500 and url not in visited:
                visited[url] = {"file": str(rel), "skipped": True}
                queue.task_done()
                continue
            async with sem:
                try:
                    data = await fetch_one(url)
                    # save markdown
                    fpath.parent.mkdir(parents=True, exist_ok=True)
                    # frontmatter
                    fm = f"---\nurl: {url}\ntitle: {json.dumps(data['title'])[1:-1]}\nmethod: {data['method']}\nfetched_at: {datetime.now(timezone.utc).isoformat()}\n---\n\n"
                    (fpath).write_text(fm + data["markdown"], encoding="utf-8")
                    # save meta
                    meta_rel = Path("_meta") / (rel.with_suffix(".json") if rel.suffix == ".md" else Path(str(rel) + ".json"))
                    meta_path = OUT_ROOT / meta_rel
                    meta_path.parent.mkdir(parents=True, exist_ok=True)
                    meta = {"url": url, "file": str(rel), "title": data["title"], "method": data["method"], "fetched_at": datetime.now(timezone.utc).isoformat(), "html_len": len(data.get("html", "")), "md_len": len(data.get("markdown", "")), "depth": depth}
                    meta_path.write_text(json.dumps(meta, indent=2), encoding="utf-8")
                    visited[url] = {"file": str(rel), "title": data["title"], "method": data["method"]}
                    idx_f.write(json.dumps({"url": url, "file": str(rel), "title": data["title"], "method": data["method"]}) + "\n")
                    if len(visited) % 20 == 0:
                        idx_f.flush()
                    stats["ok"] += 1
                    m = data["method"].split()[0]
                    stats["by_method"][m] = stats["by_method"].get(m, 0) + 1
                    host = urlparse(url).netloc
                    stats["by_host"][host] = stats["by_host"].get(host, 0) + 1
                    # enqueue discovered links (depth+1), only if depth < 6 for subdomains expansion + unlimited for main sitemap?
                    # Since seeds already cover sitemap, we expand all internal links to catch missing pages
                    for href in data.get("links", []):
                        n = normalize_url(href, base=url)
                        if not n:
                            continue
                        if n in visited or n in queued:
                            continue
                        # depth guard: main host unlimited depth (sitemap covers), subdomains max depth 4
                        nhost = urlparse(n).netloc
                        nd = depth + 1
                        if nhost != MAIN_HOST and nd > 4:
                            continue
                        if len(queued) + len(visited) >= max_pages:
                            break
                        queued.add(n)
                        await queue.put((n, nd))
                    if stats["ok"] % 100 == 0:
                        print(f"[progress] ok={stats['ok']} fail={stats['fail']} queue={queue.qsize()} methods={stats['by_method']} hosts={dict(list(stats['by_host'].items())[:5])}")
                        # checkpoint state
                        STATE_FILE.write_text(json.dumps({"visited": visited, "failed": failed, "updated": datetime.now(timezone.utc).isoformat()}, indent=2)[:20000000])
                except Exception as e:
                    failed[url] = str(e)[:500]
                    stats["fail"] += 1
                    if stats["fail"] % 50 == 0 or len(str(e)) < 200:
                        print(f"[fail] {url}: {e}")
                finally:
                    queue.task_done()
            # periodic state save
            if (stats["ok"] + stats["fail"]) % 200 == 0:
                try:
                    STATE_FILE.write_text(json.dumps({"visited": visited, "failed": failed, "updated": datetime.now(timezone.utc).isoformat()}))
                except Exception:
                    pass

    # launch workers as tasks draining queue dynamically (workers loop until empty, new items added during run)
    # Use N concurrent workers
    async def supervisor():
        tasks = [asyncio.create_task(worker(i)) for i in range(concurrency)]
        # wait until queue empty and workers done; queue may grow, so poll
        while True:
            await asyncio.sleep(2)
            if queue.empty():
                await asyncio.sleep(3)
                if queue.empty():
                    break
        for t in tasks:
            t.cancel()
        await asyncio.gather(*tasks, return_exceptions=True)

    t0 = time.time()
    await supervisor()
    idx_f.close()
    # close crawler
    global _crawler
    if _crawler is not None:
        try:
            await _crawler.close()
        except Exception:
            pass
    STATE_FILE.write_text(json.dumps({"visited": visited, "failed": failed, "updated": datetime.now(timezone.utc).isoformat()}))
    manifest = {
        "base": BASE_URL,
        "total_seeds": len(seeds),
        "sitemap_count": len(sitemap_urls),
        "llms_files": llms_files,
        "visited": len(visited),
        "failed": len(failed),
        "stats": stats,
        "elapsed_sec": round(time.time() - t0, 1),
        "out_root": str(OUT_ROOT),
        "tools": ["scrapling (Fetcher)", "crawl4ai (AsyncWebCrawler fallback)", "scrapegraph-ai (cleanup_html/convert_to_md)"],
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }
    try:  # merge over existing manifest: preserves updater stamps (last_verified) across resume runs
        prev = json.loads(MANIFEST_FILE.read_text()) if MANIFEST_FILE.exists() else {}
        prev.update(manifest)
        manifest = prev
    except Exception as e:
        print(f"[manifest] merge skipped: {e}")
    MANIFEST_FILE.write_text(json.dumps(manifest, indent=2))
    print(f"[done] visited={len(visited)} failed={len(failed)} elapsed={manifest['elapsed_sec']}s")
    print(f"[done] manifest -> {MANIFEST_FILE}")
    # list sample
    print(f"[sample] {list(visited.items())[:3]}")


# ── shared guard: never persist block/404 pages; absolutize images ──
_orig_fetch_one = fetch_one

async def fetch_one(url):
    data = await _orig_fetch_one(url)
    DG.check_document(data.get("html", ""), data.get("title", ""), data.get("markdown", ""), url)
    data["markdown"] = DG.absolutize_images(data.get("markdown", ""), url)
    return data

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-pages", type=int, default=15000)
    ap.add_argument("--concurrency", type=int, default=4)
    args = ap.parse_args()
    asyncio.run(main(max_pages=args.max_pages, concurrency=args.concurrency))
