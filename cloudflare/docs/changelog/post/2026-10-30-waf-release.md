---
url: https://developers.cloudflare.com/changelog/post/2026-10-30-waf-release/
title: WAF Release - 2026-10-30 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-31T08:10:17.775472+00:00
---

# WAF Release - 2026-10-30 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-30-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 30, 2026

## WAF Release - 2026-10-30

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This release introduces updates to the underlying rule expressions for PHP out-of-memory (OOM) vulnerabilities CVE-2026-109618, CVE-2026-109619 and CVE-2026-115560. The improvements are iterative changes based on reports from Security Researchers as part of [PHP Capture the Flag (CTF) challenge ↗︎](https://blog.cloudflare.com/php-ctf).

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...545d163c| N/A| PHP Remote Code Execution Attack (CVE-2026-109618, CVE-2026-109619) #3| Block| Block| Rule detection updated.  
Cloudflare Free Ruleset| ...82dab691| N/A| PHP Remote Code Execution Attack (CVE-2026-109618, CVE-2026-109619) #3| Block| Block| Rule detection updated.  
Cloudflare Managed Ruleset| ...212afcc9| N/A| PHP Remote Code Execution Attack (CVE-2026-109618, CVE-2026-109619) #4| Block| Block| Rule detection updated.  
Cloudflare Free Ruleset| ...24b1a4c6| N/A| PHP Remote Code Execution Attack (CVE-2026-109618, CVE-2026-109619) #4| Block| Block| Rule detection updated.  
Cloudflare Response Ruleset| ...48d2242a| N/A| Default block for High confidence Signatures| Block| Block| Rule detection updated.
