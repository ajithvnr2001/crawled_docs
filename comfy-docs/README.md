# ComfyUI Docs — End-to-End Crawler

> Last verified: 2026-10-20 — see `docs/_last_verified.json` (rewritten daily by GitHub Actions).

Crawls **https://docs.comfy.org/** completely — every English-canonical sitemap page (~1,806 after zh/ja/ko locale dedupe: get-started, 1,090 built-in-nodes reference, developers, tutorials, api-reference, registry, custom-nodes) — and saves clean markdown. Three stacks: **Scrapling** → **Crawl4AI** → **ScrapeGraphAI** (local, no LLM key). `llms.txt` + raw `_llms/en/*.txt` mirrors snapshotted under `docs/_llms/`.

## Install

```bash
pip install -r requirements.txt
python -m playwright install chromium
```

## Run (resume-safe — re-run to resume)

```bash
python3 crawl_comfy.py --max-pages 4000 --concurrency 12
python3 update_incremental.py --check-only   # new URLs + lastmod-stale only, never recrawls
python3 update_incremental.py
```

## Layout

```
crawl_comfy.py  update_incremental.py  requirements.txt
guide_code/      # coder guide + coder_scrape.py / coder_update.py
comfy-crawl.service  boot.sh  cloud-init.yaml   # spot-VM boot resilience
docs/            # output: <section>/<path>.md + _meta/ + _index.jsonl + _manifest.json
```

## Notes

- Sitemap's 7,019 URLs collapse to ~1,806 English canonicals (`/zh/`, `/ja/`, `/ko/` variants deduped by `normalize_url`); `lastmod` present on every URL → incremental refresh works.
- Login-walled/dead records land in the failed table, never silently dropped.
