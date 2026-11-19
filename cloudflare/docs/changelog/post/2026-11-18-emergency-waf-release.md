---
url: https://developers.cloudflare.com/changelog/post/2026-11-18-emergency-waf-release/
title: WAF Emergency Release - 2026-11-18 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-19T10:02:04.647686+00:00
---

# WAF Emergency Release - 2026-11-18 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-18-emergency-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 18, 2026

## WAF Emergency Release - 2026-11-18

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This release introduces 6 new malformed base64 Cloudflare Managed Ruleset detections for Java4Shell CVE-2026-114938. The rules are being deployed in log mode by default (in lieu of False Positive risk) and can be overridden if needed with supplementary information around the same available through blog post [How Cloudflare WAF helps protect against Java4Shell (CVE-2026-114938) ↗︎](https://blog.cloudflare.com/java4shell-waf-protection/).

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...4d718bf4| N/A| Java4Shell - Malformed Base64 Header - CVE-2026-114938| N/A| Log| This is a new detection.  
Cloudflare Managed Ruleset| ...2337b51d| N/A| Java4Shell - Malformed Base64 Query Value - CVE-2026-114938| N/A| Log| This is a new detection.  
Cloudflare Managed Ruleset| ...e5e5836c| N/A| Java4Shell - Malformed Base64 Body Value - CVE-2026-114938| N/A| Log| This is a new detection.  
Cloudflare Managed Ruleset| ...6fd6f152| N/A| Java4Shell - Malformed Base64 Path Segment - CVE-2026-114938| N/A| Log| This is a new detection.  
Cloudflare Managed Ruleset| ...5a25d991| N/A| Java4Shell - Malformed Base64url JWT Component - CVE-2026-114938| N/A| Log| This is a new detection.  
Cloudflare Managed Ruleset| ...67d74ebb| N/A| Java4Shell - Malformed Base64 WebAuthn Value - CVE-2026-114938| N/A| Log| This is a new detection.
