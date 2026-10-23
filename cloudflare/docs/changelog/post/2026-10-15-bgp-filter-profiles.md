---
url: https://developers.cloudflare.com/changelog/post/2026-10-15-bgp-filter-profiles/
title: BGP route filtering for IPsec and GRE tunnels \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:10:32.507717+00:00
---

# BGP route filtering for IPsec and GRE tunnels · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-15-bgp-filter-profiles/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 15, 2026

## BGP route filtering for IPsec and GRE tunnels

[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)[Magic Transit](https://developers.cloudflare.com/magic-transit/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare WAN and Magic Transit IPsec and GRE tunnels now support BGP import and export filtering.

Create reusable filter profiles that specify an `allow` or `deny` action and a list of Classless Inter-Domain Routing (CIDR) targets with exact, more-specific, or prefix-length matching. Each tunnel supports one import filter and one export filter.

You can create and assign profiles through the dashboard, API, or Terraform. Profile changes apply without resetting the BGP session.

For configuration details, refer to:

  * [Filter BGP routes for Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-routes/#filter-bgp-routes)
  * [Filter BGP routes for Magic Transit](https://developers.cloudflare.com/magic-transit/how-to/configure-routes/#filter-bgp-routes)


