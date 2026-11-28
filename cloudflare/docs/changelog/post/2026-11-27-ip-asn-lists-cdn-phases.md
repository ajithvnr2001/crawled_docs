---
url: https://developers.cloudflare.com/changelog/post/2026-11-27-ip-asn-lists-cdn-phases/
title: Use IP and ASN lists in response-side and other CDN rule filters \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-28T09:57:26.938157+00:00
---

# Use IP and ASN lists in response-side and other CDN rule filters · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-27-ip-asn-lists-cdn-phases/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 27, 2026

## Use IP and ASN lists in response-side and other CDN rule filters

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Custom IP and autonomous system number (ASN) lists are supported in response-side filters, including Response Header Transform Rules and rate-limit response-counting expressions. You can reuse network groups on both the request and response sides.

Support extends across customer-owned CDN rule filters, including WAF custom rules, Cache Rules, Redirect Rules, and Request Header Transform Rules.

For example, reference an ASN list named `partner_networks`:
    
    
    ip.src.asnum in $partner_networks

For an IP list named `office_network`, use:
    
    
    ip.src in $office_network

This expands where you can reference existing lists. It does not change plan availability, quotas, or dynamic action-value expression support. ASN lists remain Enterprise-only, and hostname lists retain their product-specific restrictions.

For details, refer to [IP and ASN lists across Rules products](https://developers.cloudflare.com/waf/tools/lists/custom-lists/#ip-and-asn-lists-across-rules-products).
