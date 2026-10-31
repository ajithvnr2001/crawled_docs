---
url: https://developers.cloudflare.com/changelog/post/2026-10-30-emergency-waf-release/
title: WAF Release - 2026-10-30 - Emergency \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-31T08:10:17.447902+00:00
---

# WAF Release - 2026-10-30 - Emergency · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-30-emergency-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 30, 2026

## WAF Release - 2026-10-30 - Emergency

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This emergency release adds a new rule to the Cloudflare Managed Ruleset, disabled by default, for a vulnerability in Nuxt Image and IPX. The rule offers partial coverage. Please follow the advisory and patch to the latest version.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...5b82bffe| N/A| Nuxt Image / IPX - Explicit GIF or Animation Modifier Exposure| N/A| Disabled| This is a new detection.
