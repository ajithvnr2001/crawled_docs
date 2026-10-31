---
url: https://developers.cloudflare.com/changelog/post/2026-10-30-cloudflare-wan-regional-processing/
title: Cloudflare WAN supports regional Gateway HTTP inspection \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-31T08:10:17.511584+00:00
---

# Cloudflare WAN supports regional Gateway HTTP inspection · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-30-cloudflare-wan-regional-processing/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 30, 2026

## Cloudflare WAN supports regional Gateway HTTP inspection

[Data Localization Suite](https://developers.cloudflare.com/data-localization/)[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare WAN traffic can now use a Gateway processing region with Regional Services. HTTPS traffic enters a Cloudflare data center (that may be outside the selected region) via an IPsec or GRE tunnel, or through Direct CNI, and remains encrypted until Gateway forwards it to the selected region for TLS decryption and HTTP inspection. This feature gives organizations control over where their sensitive traffic is processed, supporting their data sovereignty goals.

This feature requires [unified routing](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/reference/traffic-steering/#unified-routing-mode). The processing region applies to Gateway HTTP traffic and does not apply to Gateway DNS or network policy processing.

Contact your account team to configure a processing region. For supported regions, configuration details, and limitations, refer to [Data residency for Cloudflare One](https://developers.cloudflare.com/data-localization/how-to/zero-trust/#processing-region-for-gateway).
