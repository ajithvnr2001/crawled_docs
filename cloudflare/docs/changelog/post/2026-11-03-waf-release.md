---
url: https://developers.cloudflare.com/changelog/post/2026-11-03-waf-release/
title: WAF Release - 2026-11-03 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-04T08:48:16.720894+00:00
---

# WAF Release - 2026-11-03 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-03-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 3, 2026

## WAF Release - 2026-11-03

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This release introduces updates to the underlying rule expressions for PHP out-of-memory (OOM) vulnerabilities CVE-2026-109618, CVE-2026-109619 and CVE-2026-115560. The improvements are iterative changes based on reports from Security Researchers as part of [PHP Capture the Flag (CTF) challenge ↗︎](https://blog.cloudflare.com/php-ctf).

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Free Ruleset| ...bcd95984| N/A| PHP Remote Code Execution Attack (CVE-2026-109618, CVE-2026-109619) #2| Block| Block| Rule detection updated.  
Cloudflare Free Ruleset| ...82dab691| N/A| PHP Remote Code Execution Attack (CVE-2026-109618, CVE-2026-109619) #3| Block| Block| Rule detection updated.  
Cloudflare Managed Ruleset| ...0a0c2f64| N/A| PHP Remote Code Execution Attack (CVE-2026-109618, CVE-2026-109619) #2| Block| Block| Rule detection updated.  
Cloudflare Managed Ruleset| ...545d163c| N/A| PHP Remote Code Execution Attack (CVE-2026-109618, CVE-2026-109619) #3| Block| Block| Rule detection updated.  
Cloudflare Managed Ruleset| ...13f91633| N/A| phpMyAdmin - Authentication Bypass| N/A| Disabled| This is a new detection.
