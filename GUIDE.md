# crawled_docs — operations runbook

## 1. Runners

### GitHub Actions (six corpora)
`.github/workflows/update-<corpus>.yml` preserves the original cron schedule.
The job `cd`s into the corpus via `defaults.run.working-directory`, runs
`update_incremental.py`, runs `shared/audit_corpus.py`, then commits and pushes
only that corpus's paths.

`.github/workflows/audit-all.yml` (10:30 UTC) audits all eight corpora,
including the two VM-managed ones, and fails if any hard error appears.

### VM systemd (gcpdocs, sarvam-docs)
Installed units keep their original names and schedules:

| Unit | Schedule | What it runs |
|------|----------|--------------|
| `gcp-update.timer` → `gcp-update.service` | 05:30 | `update_gcp.py --concurrency 20 --refresh-cap 4000` |
| `gcp-drain-kick.timer` → `gcp-drain-kick.service` | every 4 h at :15 | restart the drain if backlog remains |
| `gcp-drain.service` | on demand | `drain_until_done.sh` (4k-page batches) |
| `gcp-git-ship.timer` → `gcp-git-ship.service` | 08:20 | `gcp_git_ship.sh` (commit + push product docs) |
| `sarvam-update.timer` → `sarvam-update.service` | 06:30 | `update_incremental.py` + `vm-ship.sh` |

All of them push to **`ajithvnr2001/crawled_docs`** now (the release assets for
the GCP API reference still use the same repository).

## 2. Paths and the compatibility symlinks

The repositories were physically moved into this tree and the historical names
were replaced by symlinks, so every absolute path in the existing units and
shell scripts keeps resolving:

```
/data/opencode/aidocs       -> crawled_docs/ai-docs
/data/opencode/canva        -> crawled_docs/canva-docs
/data/opencode/cloudflare   -> crawled_docs/cloudflare
/data/opencode/comfy        -> crawled_docs/comfy-docs
/data/opencode/copilotkit   -> crawled_docs/copilotkit-docs
/data/opencode/fishaudio    -> crawled_docs/fish-audio-docs
/data/opencode/gcpdocs      -> crawled_docs/gcpdocs
/data/opencode/sarvam       -> crawled_docs/sarvam-docs
```

`/data/opencode/boot-all.sh` recreates them after a reprovision (the `/data`
disk is persistent, so normally they are already there). New units should
prefer the real `crawled_docs/<corpus>` paths.

Full git history for every original repository is archived at
`/data/opencode/_archive/git/<name>.git` (plain git dirs, not bare). To inspect:
`git --git-dir=/data/opencode/_archive/git/aidocs.git log -1`.

## 3. Secrets

`/data/opencode/secrets/git.env` is root-only and contains `GH_TOKEN`. It is
never copied into this repo and is referenced by units via `EnvironmentFile=`.
Never commit a token; the audit and a `git grep` for `ghp_`/`github_pat_` are
expected to stay clean.

## 4. Repairing a corpus

```bash
# 1. see what the shared guard flags
python3 shared/audit_corpus.py --name comfy-docs --root comfy-docs/docs

# 2. prune saved block/404 pages (moves them under /data/opencode/_archive/removed/)
python3 shared/repair_corpus.py --name comfy \
  --root comfy-docs/docs \
  --index comfy-docs/docs/_index.jsonl \
  --meta comfy-docs/docs/_meta \
  --exclude-file comfy-docs/docs/_excluded.json \
  --skip-sidecars true

# 3. rewrite any surviving relative image URLs
python3 shared/postprocess_images.py --root comfy-docs/docs
```

`repair_corpus.py` also streams `_index.jsonl` and drops the rows that pointed
at the removed pages, then appends the URLs to `docs/_excluded.json`. Every
`update_incremental.py` merges that file into its `KNOWN_BROKEN`/`EXCLUDED`
set, so the nightly run will not fetch them again.

## 5. Adding a new corpus

1. Drop the crawler + `update_incremental.py` + `requirements.txt` under
   `<name>/`.
2. Make the crawler import the shared guard:
   ```python
   sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "shared"))
   import docguard as DG
   ```
   and call `DG.check_document(html, title, markdown, url)` before saving plus
   `DG.absolutize_images(markdown, url)` on the body.
3. Add `<name>/docs/_excluded.json` handling to its updater (copy the block
   from an existing updater).
4. Add `.github/workflows/update-<name>.yml` with the corpus cron and
   `working-directory: <name>`.
5. Add the corpus to `audit-all.yml` and to the table in `README.md`.

## 6. GCP specifics

Product/guide docs are tracked in git (≈82 k files). The versioned API
reference and the crawler sidecars (`docs/_meta`, `docs/_llms`,
`docs/_subdomains`, `docs/_d`, `docs/_index*`, `docs/**/docs/reference/`) are
ignored by `gcpdocs/.gitignore`; the huge API reference ships as Release delta
assets via `drain_until_done.sh` / `build_final_release.sh`. Keep it that way:
`git status` inside `crawled_docs` must stay fast.

## 7. Sarvam specifics

`Sarvam .gitignore` no longer hides `docs/` (docs are tracked now) and instead
ignores non-documentation media and training assets (`*.mp3`, `*_chunks/`,
`sfx/`, `rag-embeddinggemma2-course/`, TTS generators). `dashboard.sarvam.ai`
and `indus.sarvam.ai` are login-walled and blocked; the crawler refuses those
hosts and the guard rejects them if they ever appear again.
