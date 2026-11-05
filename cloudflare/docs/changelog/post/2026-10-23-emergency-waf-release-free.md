---
url: https://developers.cloudflare.com/changelog/post/2026-10-23-emergency-waf-release-free/
title: WAF Release - 2026-10-23 - Emergency - Cloudflare Free Ruleset \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-05T09:11:07.478408+00:00
---

# WAF Release - 2026-10-23 - Emergency - Cloudflare Free Ruleset · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-23-emergency-waf-release-free/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 23, 2026

## WAF Release - 2026-10-23 - Emergency - Cloudflare Free Ruleset

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The existing PHP remote code execution rule in the Cloudflare Free Ruleset covers CVE-2026-115560. This emergency release adds the CVE identifier to existing rule. Detection logic and rule actions remain unchanged.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Free Ruleset| ...7975ce1b| N/A| PHP Remote Code Execution Attack (CVE-2026-109618, CVE-2026-109619, CVE-2026-115560) #6| Block| N/A| Rule metadata description refined. Detection unchanged.  
  
For more information, refer to [WAF Managed Rules](https://developers.cloudflare.com/waf/managed-rules/).
