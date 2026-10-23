# GUIDE — developer.cloudflare.com docs: full redo + incremental updates (end to end)

21,290+ markdown pages, sitemap coverage verified 100%, daily GitHub Action green. Redo from scratch via §2; daily updates via §3.

## 0. Architecture

```
crawl_cloudflare.py    → docs/<path>.md        (resume-safe crawl)
update_incremental.py  → incremental pass      (new + lastmod-stale, capped refresh)
.github/workflows/update-docs.yml              → daily 02:00 UTC on GitHub Actions
```

Stack: **Scrapling → Crawl4AI → ScrapeGraphAI → httpx** fallback chain (`fetch_one`). Saved as frontmatter `.md` + `_meta/*.json` + `_index.jsonl` + `_manifest.json` + daily stamp `_last_verified.json`. State: `crawl_state.json`.

## 1. Setup

```bash
pip install -r requirements.txt && python -m playwright install chromium
# patched tool clones under tools/ (scrapegraph-ai 1.36.0 needs langchain_core imports) — see ai-docs GUIDE §1
```

## 2. Full redo

```bash
python3 crawl_cloudflare.py --concurrency 15
python3 update_incremental.py --check-only       # expect new=0, stale≈0
find docs -name '*.md' | wc -l                   # ~21,290
```

- Sitemap exhaustive: every `<loc>` in `https://developers.cloudflare.com/sitemap.xml` is either a saved page or a recorded failure (0 onset the final verification).
- Locale variants (`/zh-cn/`, `/ja/`…) are intentionally NOT crawled (English canonical only) — sitemap coverage is computed against English URLs.
- Resumable at page level; kill/restart any time.

## 3. Incremental updates (GitHub Action, daily 02:00 UTC)

1. `update_incremental.py`: live sitemap diff → new pages crawled; `lastmod`-newer-than-fetched pages refreshed newest-first (cap 100); stamps `docs/_last_verified.json` + `_manifest.json` + "Last verified:" in READMEs.
2. Commit + push with retry: on conflict, `git rebase origin/main`, and for shared stamp files keep our fresh copy (`--ours`), then push.

Workflow_dispatch lets you run it manually anytime; locally the same line works: `python3 update_incremental.py --concurrency 10`.

## 4. Recovery

`boot.sh` + `cloud-init.yaml` pattern identical to ai-docs (service `Restart=on-failure`; only enabled post-crawl). `/data` survives reboots; `git push` is the durable secondary copy.

## 5. Gotchas

| Symptom | Fix |
|---|---|
| Daily Action mid-run says "no changes" for weeks | healthy — corpory is stable; stamps still refresh daily. |
| rebase conflict stamp loop | keep the `--ours` checkout; never force-push docs history. |
| thin-content 800-char floor pushes legit short pages to fallback | intended: gallery/redirect pages end up crawl4ai/httpx-sourced; check `method` in frontmatter. |
