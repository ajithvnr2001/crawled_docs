---
url: https://developers.cloudflare.com/changelog/post/2026-11-19-emergency-waf-release/
title: WAF Emergency Release - 2026-11-19 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-20T09:50:37.978847+00:00
---

# WAF Emergency Release - 2026-11-19 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-19-emergency-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 19, 2026

## WAF Emergency Release - 2026-11-19

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This release introduces updates to an existing PHP Remote Code Execution rule to improve detection accuracy, as well as a few new generic, PHP and Ruby CVE specific rules. The new PHP rules are being deployed in log mode by default (in lieu of False Positive risk) and can be overridden after evaluating requests matching the rules. Supplementary information around the CVEs are available through Zero Wire [phpAfterShell and six other PHP critical flaws ↗︎](https://radar.cloudflare.com/zero-wire/php-november-2026-security-release-phpaftershell) and [ruby2shell: heap overflow in Ruby string case conversion ↗︎](https://radar.cloudflare.com/zero-wire/ruby2shell).

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Free Ruleset| ...7975ce1b| N/A| PHP Remote Code Execution Attack (CVE-2026-109618, CVE-2026-109619, CVE-2026-115560, CVE-2026-126714) #6| N/A| Block| Rule detection and description updated.  
Cloudflare Free Ruleset| ...b19210f1| N/A| Ruby - Heap Overflow - CVE:CVE-2026-13282| N/A| Block| This is a new detection.  
Cloudflare Free Ruleset| ...e9855f05| N/A| Ruby - Integer Overflow - GHSA-87fm-7w84-j2px| N/A| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...9d9c073d| N/A| PHP Remote Code Execution Attack (CVE-2026-109618, CVE-2026-109619, CVE-2026-115560, CVE-2026-126714) #6| N/A| Block| Rule detection and description updated.  
Cloudflare Managed Ruleset| ...34402c88| N/A| Ruby - Heap Overflow - CVE:CVE-2026-13282| N/A| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...daf25922| N/A| Ruby - Integer Overflow - GHSA-87fm-7w84-j2px| N/A| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...6c6f42b2| N/A| PHP-FPM - CVE:CVE-2026-129289| N/A| Log| This is a new detection.  
Cloudflare Managed Ruleset| ...a54028d4| N/A| PHP SOAP - CVE:CVE-2026-15353| N/A| Log| This is a new detection.  
Cloudflare Managed Ruleset| ...4521b819| N/A| PHP SOAP - CVE:CVE-2026-129506| N/A| Log| This is a new detection.  
Cloudflare Managed Ruleset| ...3f53db3c| N/A| Generic Rules - Authentication Bypass| N/A| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...36ba9f71| N/A| Anomaly - Embedded Application Request| N/A| Block| This is a new detection.
