---
url: https://developers.cloudflare.com/changelog/post/2026-10-30-keyless-ssl-tls13-ecdsa/
title: Keyless SSL supports TLS 1.3 with ECDSA certificates \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-31T08:10:17.470248+00:00
---

# Keyless SSL supports TLS 1.3 with ECDSA certificates · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-30-keyless-ssl-tls13-ecdsa/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 30, 2026

## Keyless SSL supports TLS 1.3 with ECDSA certificates

[SSL/TLS](https://developers.cloudflare.com/ssl/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Keyless SSL](https://developers.cloudflare.com/ssl/keyless-ssl/) supports TLS 1.3 for ECDSA certificates. When [TLS 1.3](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/tls-13/) is enabled on your zone, visitors connecting to a hostname that serves a Keyless ECDSA certificate negotiate TLS 1.3, and your private keys stay on your own key server.

Keyless SSL connections that use RSA certificates continue to negotiate up to TLS 1.2.

For details, refer to the [Keyless SSL limitations](https://developers.cloudflare.com/ssl/keyless-ssl/#limitations).
