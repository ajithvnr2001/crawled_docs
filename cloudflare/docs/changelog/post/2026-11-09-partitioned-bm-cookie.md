---
url: https://developers.cloudflare.com/changelog/post/2026-11-09-partitioned-bm-cookie/
title: Partitioned cookie support for Bot Management \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-11T09:00:58.609246+00:00
---

# Partitioned cookie support for Bot Management · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-09-partitioned-bm-cookie/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 9, 2026

## Partitioned cookie support for Bot Management

[Bots](https://developers.cloudflare.com/bots/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare now adds the `Partitioned` attribute to the `__cf_bm` cookie on compatible HTTPS requests. The attribute is added only when the cookie can also be issued with `SameSite=None` and `Secure`.

When users access your content through an `<iframe>` on another site, the browser handles `__cf_bm` as a third-party cookie. Browser privacy controls may block third-party cookies. Adding `Partitioned` allows the `__cf_bm` cookie to persist within that top-level site. This means that Bot Management can preserve continuity across requests, even when your content is embedded on another site.

For more information, refer to [Cloudflare cookies](https://developers.cloudflare.com/fundamentals/reference/policies-compliances/cloudflare-cookies/#__cf_bm-cookie-for-cloudflare-bot-products).
