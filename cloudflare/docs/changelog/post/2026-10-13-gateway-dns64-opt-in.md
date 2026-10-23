---
url: https://developers.cloudflare.com/changelog/post/2026-10-13-gateway-dns64-opt-in/
title: Request Gateway DNS64 through DNS locations and EDNS \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:10:32.639889+00:00
---

# Request Gateway DNS64 through DNS locations and EDNS · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-13-gateway-dns64-opt-in/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 13, 2026

## Request Gateway DNS64 through DNS locations and EDNS

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-controls/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now request DNS64 through Cloudflare Gateway DNS location settings or Extension Mechanisms for DNS (EDNS) options.

DNS64 synthesizes `AAAA` records from `A` records for IPv6-only networks. These networks require network address translation from IPv6 to IPv4 (NAT64).

Turn on **Enable DNS64** for a location, or include an empty EDNS option `65051` in individual queries. Both mechanisms support UDP, TCP, DNS over TLS (DoT), and DNS over HTTPS (DoH).

For example, request DNS64 through EDNS with `dig`:
    
    
    dig @"<DNS_RESOLVER_IP>" ipv4only.arpa AAAA +ednsopt=65051 +short

The existing `cf-dns-options: dns64` DoH header remains supported independently. DNS64 is off by default. Each mechanism independently requests synthesis.

For configuration, API update behavior, and request examples, refer to [DNS64](https://developers.cloudflare.com/cloudflare-one/traffic-controls/resolver-endpoints/dns64/).
