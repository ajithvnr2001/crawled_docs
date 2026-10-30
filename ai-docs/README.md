# Google AI Studio Docs — End-to-End Crawler

> Last verified: 2026-10-30 — see `docs/_last_verified.json` (rewritten daily by GitHub Actions).

Crawls **https://ai.google.dev/** completely (sitemap + linked reference domains: aistudio, saif, discuss, developer.android, developer.chrome) and saves clean Markdown docs. Pipeline: **Scrapling** (cookie-warmed) → **Crawl4AI** → **ScrapeGraphAI** (local, no LLM key).

**Current corpus:** 5,627 Markdown pages + 16 raw `.md.txt` API specs; **8,936 images across 1,263 pages**. Integrity audit: **0 CAPTCHA/OAuth pages, 0 404 pages, 0 missing/unindexed files, 0 relative image links**.

## Install

```bash
pip install -r requirements.txt
python -m playwright install chromium
```

## Run (resume-safe — re-run to resume)

```bash
python3 crawl_ai.py --max-pages 8000 --concurrency 4
python3 update_incremental.py --check-only        # counts only, no fetches
python3 update_incremental.py                    # new + stale + blocked-page repair
python3 update_incremental.py --repair-cap 1000  # one-off backlog repair
python3 audit_corpus.py                          # exits nonzero on hard errors
python3 prune_404.py                             # remove dead 404 pages
```

## Layout

```
crawl_ai.py  update_incremental.py  audit_corpus.py  prune_404.py  requirements.txt
guide_code/      # coder guide + coder_scrape.py / coder_update.py
ai-docs-crawl.service  boot.sh  cloud-init.yaml   # spot-VM boot resilience
docs/            # output: <area>/<path>.md + _meta/ + _index.jsonl + _manifest.json
```

## Notes

- **Anti-bot:** Google's edge returns an OAuth interstitial (302) or a CAPTCHA page to cold clients. The fetcher warms a cookie jar on `/gemini-api/docs`, retries with fresh cookies, and rejects CAPTCHA/OAuth pages at every layer — a block page can never overwrite a good doc.
- **Images:** DevSite pages are extracted from `div.devsite-article-body`, so `<img>`, tables and code samples are preserved as absolute Markdown links. Titles come from the page `<h1>`.
- **404s:** Crawl4AI can return HTTP 200 with a 404 body. Both hard and soft 404s are rejected; `prune_404.py` removes already-saved dead pages and records them in `docs/_excluded.json`.
- **Thin-page warnings** in `audit_corpus.py` are expected for client-rendered AI Studio app shells, forum user profiles, and MediaPipe module stubs; hard errors are blocked/404/missing/relative-image pages.
- Sitemap's 6,854 URLs collapse to ~653 canonical (`?hl=` locale variants deduped); `*.md.txt` entries are fetched as raw text.
- Login-walled hosts are recorded as failed, not silently dropped.
