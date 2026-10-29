---
url: https://developers.cloudflare.com/changelog/post/2026-10-28-workers-builds-90-day-retention/
title: Workers Builds now retains builds and build logs for 90 days \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-29T08:13:59.424478+00:00
---

# Workers Builds now retains builds and build logs for 90 days · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-28-workers-builds-90-day-retention/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 28, 2026

## Workers Builds now retains builds and build logs for 90 days

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/) now retains each build and its build logs for 90 days after the build finishes. You can find them under **View build history** in your Worker's **Deployments** tab, or through the [Workers Builds API](https://developers.cloudflare.com/workers/ci-cd/builds/api-reference/).

After 90 days, a build and its logs are removed. The versions and deployments it created stay in your Worker's [version history](https://developers.cloudflare.com/workers/versions-and-deployments/), so you can still [roll back](https://developers.cloudflare.com/workers/versions-and-deployments/rollbacks/) to them.

If you need a build's logs for longer, you can download them with the [Get build logs](https://developers.cloudflare.com/api/resources/workers_builds/subresources/builds/methods/get_logs/) API endpoint.

For more information, refer to the [Workers Builds limits documentation](https://developers.cloudflare.com/workers/ci-cd/builds/limits-and-pricing/).
