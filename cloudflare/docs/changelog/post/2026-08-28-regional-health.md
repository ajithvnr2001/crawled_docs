---
url: https://developers.cloudflare.com/changelog/post/2026-08-28-regional-health/
title: Load Balancing now supports regional health \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-28T08:03:52.759749+00:00
---

# Load Balancing now supports regional health · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-28-regional-health/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 28, 2026

## Load Balancing now supports regional health

[Load Balancing](https://developers.cloudflare.com/load-balancing/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Load Balancing now supports regional health. Each Cloudflare region can make an independent health decision for a pool. When pool reachability differs by region, traffic can avoid an unreachable pool without removing it from service elsewhere.

Configure regional health with the `health_sources` field on a pool. Set it to `["regional", "global"]` to prefer regional health and use global health when no regional decision is available. Pools without `health_sources` retain their existing health behavior.

Regional health is useful for multi-region deployments and failures that affect specific network paths.

For more information, refer to [Regional health](https://developers.cloudflare.com/load-balancing/understand-basics/regional-health/).
