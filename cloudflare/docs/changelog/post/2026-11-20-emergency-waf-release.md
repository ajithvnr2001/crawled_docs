---
url: https://developers.cloudflare.com/changelog/post/2026-11-20-emergency-waf-release/
title: WAF Emergency Release - 2026-11-20 \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-25T10:59:48.289814+00:00
---

# WAF Emergency Release - 2026-11-20 · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-20-emergency-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 20, 2026

## WAF Emergency Release - 2026-11-20

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This release introduces new Ruby and WordPress security advisory mapped rules. Supplementary information around the security advisories covered are available through Zero Wire [ruby2shell: heap overflow in Ruby string case conversion ↗︎](https://radar.cloudflare.com/zero-wire/ruby2shell) and [WordPress 7.1.5: Template Part flaw can turn an administrator's click into code execution ↗︎](https://radar.cloudflare.com/zero-wire/wordpress-7-1-5-template-part-privilege-escalation).

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Free Ruleset| ...b01ffb6b| N/A| Ruby - Regexp Character Class Intersection - GHSA-7x2q-68qv-6p8x| N/A| Block| This is a new detection.  
Cloudflare Free Ruleset| ...d5ec80f7| N/A| Ruby - Regexp Compiled Program Size - GHSA-3p8q-wmhx-vm2w| N/A| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...aa981883| N/A| Ruby - Regexp Character Class Intersection - GHSA-7x2q-68qv-6p8x| N/A| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...1bd84008| N/A| Ruby - Regexp Compiled Program Size - GHSA-3p8q-wmhx-vm2w| N/A| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...e12fd7b1| N/A| WordPress - DoS - GHSA-56j2-5mp6-wr3x| N/A| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...a8ad193f| N/A| WordPress - Broken Access Control - GHSA-pmp8-6cv8-q323| N/A| Block| This is a new detection.  
Cloudflare Managed Ruleset| ...4755597d| N/A| WordPress - Stored XSS - GHSA-cr2m-2j4r-3v3x| N/A| Block| This is a new detection.
