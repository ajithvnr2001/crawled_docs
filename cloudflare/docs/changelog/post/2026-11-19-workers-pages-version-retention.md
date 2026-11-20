---
url: https://developers.cloudflare.com/changelog/post/2026-11-19-workers-pages-version-retention/
title: Workers and Pages now keep versions for 30 days \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-20T09:50:37.779294+00:00
---

# Workers and Pages now keep versions for 30 days · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-19-workers-pages-version-retention/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 19, 2026

## Workers and Pages now keep versions for 30 days

[Workers](https://developers.cloudflare.com/workers/)[Pages](https://developers.cloudflare.com/pages/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare now keeps [versions](https://developers.cloudflare.com/workers/versions-and-deployments/) of your Workers and [deployments](https://developers.cloudflare.com/pages/configuration/preview-deployments/) of your Pages projects for 30 days. After 30 days, they are deleted, except your 100 most recent and what is currently deployed.

**What is not affected:**

  * **Running applications:** Deployed Worker versions and your current Pages production deployment are always kept
  * **Rollbacks:** You can still [roll back](https://developers.cloudflare.com/workers/versions-and-deployments/rollbacks/) to any of your 100 most recent Worker versions, and to any Pages [production deployment](https://developers.cloudflare.com/pages/configuration/rollbacks/) that has not been deleted
  * **Worker Previews:** [Worker Preview](https://developers.cloudflare.com/workers/previews/) URLs always serve the latest deployment of that Preview. Use Worker Previews for branches and pull requests instead of Version URLs, which run with your production bindings



**What you will notice:**

  * Deleted versions and deployments no longer appear in the dashboard or API
  * The URL associated with each deleted Worker version, known as its [Version URL](https://developers.cloudflare.com/workers/versions-and-deployments/version-urls/) (including any `--preview-alias`), stops working, as does the [preview URL](https://developers.cloudflare.com/pages/configuration/preview-deployments/) of each deleted Pages deployment



For more information, refer to [Workers version retention](https://developers.cloudflare.com/workers/versions-and-deployments/#version-retention), [Pages deployment limits](https://developers.cloudflare.com/pages/platform/limits/#deployments), and [Compare workflows](https://developers.cloudflare.com/workers/previews/compare-workflows/).
