---
url: https://developers.cloudflare.com/waf/tools/ip-access-rules/actions/
title: IP Access rules actions \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:47.687978+00:00
---

# IP Access rules actions · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/tools/ip-access-rules/actions/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

Additional tools

  4. /[IP Access rules](https://developers.cloudflare.com/waf/tools/ip-access-rules/)
  5. /Actions



# IP Access rules actions

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/tools/ip-access-rules/actions/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

An IP Access rule can perform one of the following actions:

  * **Block** : Prevents a visitor from visiting your site.

  * **Allow** : Excludes visitors from all security checks, including [Browser Integrity Check](https://developers.cloudflare.com/waf/tools/browser-integrity-check/), [Under Attack mode](https://developers.cloudflare.com/fundamentals/reference/under-attack-mode/), and the WAF. Use this option when a trusted visitor is being blocked by Cloudflare's default security features. The _Allow_ action takes precedence over the _Block_ action.  
Allowing a given country code will not bypass WAF managed rules (previous and new versions). Refer to [Important remarks about allowing/blocking by country](https://developers.cloudflare.com/waf/tools/ip-access-rules/#important-remarks-about-allowingblocking-by-country) for more information.

  * **Managed Challenge** : Depending on the characteristics of a request, Cloudflare will dynamically choose the appropriate type of challenge from a list of possible actions. For more information, refer to [Interstitial Challenge Pages](https://developers.cloudflare.com/cloudflare-challenges/challenge-types/challenge-pages/#managed-challenge).

  * **Non-Interactive Challenge** : Presents a non-interactive challenge page to visitors. Prevents bots from accessing the site.

  * **Interactive Challenge** : Requires the visitor to complete an interactive challenge before visiting your site. Prevents bots from accessing the site.




[PreviousParameters](https://developers.cloudflare.com/waf/tools/ip-access-rules/parameters/)[NextOverview](https://developers.cloudflare.com/waf/tools/scrape-shield/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/tools/ip-access-rules/actions.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
