# GUIDE — ai.google.dev docs: full redo + incremental updates (end to end)

Written from the run that produced 5,627 Markdown pages (+ 8 raw `.md.txt` API specs) in 6 hosts. Follow top-to-bottom to **redo the crawl from zero**, or skip to §3 for daily updates.

## 0. Scope + architecture

Crawls **https://ai.google.dev/** (653 canonical sitemap URLs after locale dedupe, plus raw `.md.txt` API mirrors) and linked reference domains at depth ≤1: `aistudio.google.com`, `saif.google`, `discuss.ai.google.dev`, `developer.android.com`, `developer.chrome.com` → lands under `docs/_subdomains/<host>/`.

Pipeline (`crawl_ai.py::fetch_one`):
cookie-warm `Scrapling Fetcher.get(stealthy_headers)` → DevSite article-body extract → **ScrapeGraphAI** `convert_to_md` (local, no key) → thin-content fallback **Crawl4AI** headless → cookie-warmed **httpx** last resort. URLs ending `.txt` are fetched raw (no rendering).

Every layer rejects CAPTCHA/OAuth pages and hard/soft 404s; the fetcher warms a cookie jar on `/gemini-api/docs` first, because Google gates cold requests with a 302 to OAuth or a "Please type the characters" page. Article extraction prefers `div.devsite-article-body` (not `<main>`) so images, tables and code survive; titles come from `<h1>`.

State: `crawl_state.json` (visited/failed), `docs/_index.jsonl`, `docs/_meta/*/*.json`, `docs/_manifest.json`, `crawl.log`.

## 1. Setup (fresh machine)

```bash
git clone https://github.com/ajithvnr2001/ai-docs   # or start bare with the scripts
pip install -r requirements.txt
python -m playwright install chromium
mkdir -p tools && for t in scrapegraph-ai crawl4AI scrapling; do ln -s /data/opencode/cloudflare/tools/$t tools/$t; done
```

scrapegraph-ai 1.36.0 ships stale `langchain.prompts` imports — use the patched clone (tools/) or `sed 's/langchain\.prompts/langchain_core.prompts/'` its `utils/convert_to_md.py`.

## 2. Full crawl redo

```bash
python3 crawl_ai.py --max-pages 8000 --concurrency 4
```

- Seeds = `https://ai.google.dev/sitemap.xml` → `sitemap_0_of_1.xml`, locale variants deduped by `normalize_url()`; `?hl=` dropped; binaries/`.json`/login-walled hosts skipped and recorded.
- Fully resumable — rerun the same command; visited set is skipped.
- Watch: `tail -f crawl.log`; final state: `[done] visited=N failed=M` + `_manifest.json`.

Expected: ~5,627 pages total (`ai.google.dev` + 5 subdomain hosts), ~90MB. Concurrency is deliberately 4: higher rates trigger Google's anti-bot throttle.

## 3. Daily incremental updates (GitHub Actions)

`.github/workflows/update-docs.yml` runs daily 04:00 UTC (a pin-stagger with cloudflare 02:00 and copilotkit 03:00):

1. checkout → install pinned deps → `python3 update_incremental.py --concurrency 4`
   - fetches live sitemap + `lastmod`
   - **new** = URLs not in `_index.jsonl` → crawled
   - **stale** = `lastmod` > our `fetched_at` → refreshed newest-first, capped at 100/run
   - **repair** = indexed pages whose saved file contains CAPTCHA/OAuth markers → refetched regardless of `lastmod`, capped at 300/run (`--repair-cap`)
   - writes daily stamp `docs/_last_verified.json`, updates `_manifest.json`, stamps "Last verified:" in both READMEs
2. If anything changed: commit `chore: daily docs update <date>` + push with **retry-with-rebase** (on stamp-file conflicts it keeps our fresh copy: `git checkout --ours -- docs/_last_verified.json docs/_manifest.json`).
3. `python3 audit_corpus.py` — fails the job on blocked/404/missing/unindexed/duplicate/relative-image pages, so a regression cannot pass silently.

Run manually anytime: **Actions → daily-docs-update → Run workflow** (workflow_dispatch). Locally:

```bash
python3 update_incremental.py --check-only
python3 update_incremental.py --concurrency 4
python3 update_incremental.py --repair-cap 1000   # one-off blocked backlog
```

## 4. Verifying a healthy corpus

```bash
python3 update_incremental.py --check-only   # expect new=0, stale<=100, blocked=0
python3 audit_corpus.py                      # RESULT: OK; all hard errors zero
find docs -name '*.md' | wc -l               # ~5,627
python3 -c "import json;print(json.load(open('docs/_last_verified.json')))"
python3 prune_404.py                         # optional: remove dead pages recorded as 404
```

`audit_corpus.py` warns about thin pages (client-rendered app shells, forum profiles, MediaPipe module stubs) but only exits nonzero for blocked pages, 404s, missing or unindexed files, duplicate URLs, or relative image links.

A green daily Action that says "no changes" most days = healthy. If `new` grows monotonically without commits, check the Actions log for the push-retry dance.

## 5. VM eviction recovery

- `ai-docs-crawl.service` (`Restart=on-failure`) + `boot.sh` + `cloud-init.yaml` — after a reboot the service starts and the crawl resumes; when the crawl is already done the service stays idle (on-failure, no loop).
- One-time per new VM: attach `cloud-init.yaml` as custom-data.

## 6. Gotchas (real ones we hit)

| Symptom | Fix |
|---|---|
| Page saved as Google CAPTCHA / OAuth "Please type the characters" | cookie warm-up + `is_block_page()` at every fetch layer; daily `repair` lane refetches blocked files, never overwrites a good page. |
| Crawl4AI saved HTTP 200 pages that are actually "404 Page Not Found" | `is_404_page()` + status-code check; `prune_404.py` removes dead pages and records them in `docs/_excluded.json`. |
| Images/table/code missing or Markdown full of nav links | extract `div.devsite-article-body` instead of `<main>`; titles from `<h1>`; image URLs are absolutized by `convert_to_md`. |
| Playwright `add_cookies: Invalid cookie fields` | skip `__Host-`/`__Secure-` cookies when seeding Crawl4AI (they may not carry a domain). |
| 9 sitemap `.txt` files saved as garbage md | raw-text branch in `fetch_one` (urls ending `.txt` → cookie-warmed httpx plain fetch) — keep it. |
| `Restart=always` re-crawled a *finished* corpus on boot | now `Restart=on-failure`; only start the service when you want a (re)crawl. |
| llms.txt returns 404 despite sitemap advertising it | not all sites ship it; seeds fall back to sitemap only — fine. |
| Stamp-file rebase conflicts in Actions | handled by the `--ours` checkout of `_last_verified.json` + `_manifest.json`. |
| `developer.android.com` reference explosion (100k+ gradle pages) | kept `--max-pages 8000` cap + depth ≤1 on reference domains; raise if you want the full Android reference (be ready for a multi-day crawl). |
