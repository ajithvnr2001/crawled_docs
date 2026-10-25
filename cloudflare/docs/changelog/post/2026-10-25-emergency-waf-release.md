---
url: https://developers.cloudflare.com/changelog/post/2026-10-25-emergency-waf-release/
title: WAF Release - 2026-10-25 - Emergency - Cloudflare Managed Ruleset \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-25T07:24:53.519791+00:00
---

# WAF Release - 2026-10-25 - Emergency - Cloudflare Managed Ruleset · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-25-emergency-waf-release/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 25, 2026

## WAF Release - 2026-10-25 - Emergency - Cloudflare Managed Ruleset

[WAF](https://developers.cloudflare.com/waf/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This emergency release will add two rules related to the Brotli vulnerability **CVE-2026-111497** to the Cloudflare Managed Ruleset. Both rules will be **enabled by default** with their action set to **Log** , providing visibility into matching requests so customers can evaluate the impact before choosing to block them.

**Rule behavior**

  * **Brotli rule:** Matches incoming requests that declare Brotli request-body encoding (`Content-Encoding: br`), including legitimate clients submitting Brotli-encoded request bodies. It does not match `Accept-Encoding: br` or affect Cloudflare's Brotli response-compression settings. The rule's default action is **Log**.
  * **Next.js rule:** Matches requests to the Next.js image optimization endpoint (`/_next/image`), including legitimate image optimization traffic. The default action is **Log** and does not block requests. Changing the action to **Block** may prevent optimized images from loading and disrupt image delivery for applications using this endpoint.



**Default behavior**

  * Both rules will log matching requests without blocking them when the ruleset defaults are used.
  * Customers will be able to review matches in analytics and configure a blocking action for either rule if desired.
  * Enabling these rules in **Log** mode provides visibility only; it does not block requests matching these rules.



**Important: Check existing action overrides**

If you have configured a ruleset-level action override that applies **Block** to these rules, matching requests may be blocked as soon as the rules are deployed, despite their default **Log** action. This may result in false positives and block legitimate traffic.

Review your existing ruleset overrides before deployment. If you want to evaluate these rules without blocking traffic, configure rule-specific overrides to use **Log** and review matching requests before switching to **Block**.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...ca706f3c| N/A| Brotli - Request Content-Encoding - CVE:CVE-2026-111497| N/A| Log| This is a new detection.  
Cloudflare Managed Ruleset| ...402fe5bb| N/A| Next.js - Image Optimizer Path - CVE:CVE-2026-111497| N/A| Log| This is a new detection.
