---
url: https://developers.cloudflare.com/changelog/post/2026-11-09-durable-objects-reactivation-placement/
title: Improved Durable Object Startup Placement \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-10T09:28:45.552589+00:00
---

# Improved Durable Object Startup Placement · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-09-durable-objects-reactivation-placement/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 9, 2026

## Improved Durable Object Startup Placement

[Durable Objects](https://developers.cloudflare.com/durable-objects/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare has improved how it chooses where to start a Durable Object after the object has been inactive.

Reactivated Durable Objects now start on the machine that last ran them whenever possible, so their data doesn't need to be loaded again.

This can make cold starts less frequent for SQLite-backed Durable Objects that are reactivated soon after going idle. Actual results depend on your workload and traffic patterns.

The change is live in all regions. No action is needed by customers to see benefits from this change.

To learn more about how Durable Objects are placed, refer to [Data location](https://developers.cloudflare.com/durable-objects/reference/data-location/).
