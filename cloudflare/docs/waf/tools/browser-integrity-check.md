---
url: https://developers.cloudflare.com/waf/tools/browser-integrity-check/
title: Browser Integrity Check \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:47.528956+00:00
---

# Browser Integrity Check · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/tools/browser-integrity-check/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /Additional tools
  4. /Browser Integrity Check



# Browser Integrity Check

Last updated Aug 3, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/tools/browser-integrity-check/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewDisable Browser Integrity Check Disable globally Disable selectively

Cloudflare's Browser Integrity Check (BIC) looks for common HTTP headers abused most commonly by spammers and denies access to your page.

It also challenges visitors without a user agent or with a non-standard user agent such as commonly used by abusive bots, crawlers, or visitors.

Browser Integrity Check is enabled by default.

## Disable Browser Integrity Check

### Disable globally

To disable BIC globally for your zone:

  1. In the Cloudflare dashboard, go to the Security **Settings** page.

[ Go to **Settings** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/settings)
  2. (Optional) Filter by **DDoS attacks**.

  3. Turn off **Browser integrity check**.




### Disable selectively

To disable BIC selectively, you can skip Browser Integrity Check using a [custom rule with a skip action](https://developers.cloudflare.com/waf/custom-rules/skip/).

Also, use a [configuration rule](https://developers.cloudflare.com/rules/configuration-rules/) to selectively enable or disable this feature for certain sections of your website using a filter expression (such as a matching hostname or request URL path).

[PreviousZone Lockdown](https://developers.cloudflare.com/waf/tools/zone-lockdown/)[NextEnable security.txt ↗︎](https://developers.cloudflare.com/security-center/infrastructure/security-file/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/tools/browser-integrity-check.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
