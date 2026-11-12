---
url: https://developers.cloudflare.com/changelog/post/2026-11-11-hyperdrive-raised-limits/
title: Hyperdrive raises limits for connections and configurations \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-12T09:30:22.553297+00:00
---

# Hyperdrive raises limits for connections and configurations · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-11-hyperdrive-raised-limits/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 11, 2026

## Hyperdrive raises limits for connections and configurations

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Customers on a Workers Paid plan can now create up to 100 Hyperdrive configurations, up from 25, and configure up to 1,500 origin database connections per configuration, up from 100.

**Configuration limit**

The configuration limit is the maximum number of Hyperdrive configurations you can create per account. Workers Paid customers can now create up to 100 configurations, allowing more workloads to take advantage of connection pooling and query caching across different databases.

**Origin connection limit**

The origin connection limit is the maximum number of database connections that Hyperdrive can make to your origin database per configuration. Workers Paid customers can now configure up to 1,500 origin connections, increasing the connection pool size available for workloads that need more concurrent database access. You can configure this value via the dashboard, Wrangler, or the REST API.

We recommend setting the origin connection limit lower than your origin database's connection limit.

For more information, refer to [Hyperdrive limits](https://developers.cloudflare.com/hyperdrive/platform/limits/) and [Tune connection pooling](https://developers.cloudflare.com/hyperdrive/configuration/tune-connection-pool/).
