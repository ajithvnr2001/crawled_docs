---
url: https://developers.cloudflare.com/changelog/post/2026-10-12-waf-release/
title: WAF Release - 2026-10-12 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:10:32.714938+00:00
---

# WAF Release - 2026-10-12 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-12-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 12, 2026

## WAF Release - 2026-10-12

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This release introduces new detections to mitigate recent vulnerabilities affecting TanStack and Atlassian products.

**Key Findings**

  * CVE-2026-102989: A reflected Cross-Site Scripting (XSS) vulnerability affecting TanStack. Unauthenticated attackers can exploit this flaw to inject malicious scripts into web pages viewed by other users, potentially leading to session hijacking or unauthorized actions.

  * CVE-2026-21589: An arbitrary file access vulnerability affecting Atlassian products. Threat actors can exploit this flaw to read unauthorized files on the target system, risking the exposure of sensitive configuration data.


Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...02751ef3| N/A| Generic Rules - Template Injection - 2 - Beta| Disabled| Disabled| This rule is merged into the original rule "Generic Rules - Template Injection - 2" (ID: ...d3ed0123).  
Cloudflare Managed Ruleset| ...4ee560b2| N/A| TanStack - Reflected XSS - CVE:CVE-2026-102989| N/A| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...e919cd31| N/A| Atlassian - Arbitrary File Access - CVE:CVE-2026-21589| N/A| Block| This is a new detection.
