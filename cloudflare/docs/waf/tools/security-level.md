---
url: https://developers.cloudflare.com/waf/tools/security-level/
title: Security Level \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:49.115160+00:00
---

# Security Level · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/tools/security-level/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /Additional tools
  4. /Security Level



# Security Level

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/tools/security-level/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewThreat score

In the old Cloudflare dashboard, security level has the value _Always protected_ and you cannot change this setting. To turn [Under Attack mode](https://developers.cloudflare.com/fundamentals/reference/under-attack-mode/) on or off, use the separate toggle.

In the new security dashboard, the Cloudflare API, and in Terraform, use security level to turn Under Attack mode on or off.

Cloudflare's [Under Attack mode](https://developers.cloudflare.com/fundamentals/reference/under-attack-mode/) performs additional security checks to help mitigate layer 7 DDoS attacks. When you enable Under Attack mode, Cloudflare will present a Managed Challenge page.

Caution

Only use [Under Attack mode](https://developers.cloudflare.com/fundamentals/reference/under-attack-mode/) when a website is under a DDoS attack. Under Attack mode may affect some actions on your domain, such as your API traffic.

To enable or disable Under Attack mode for your API or any other part of your domain, create a [configuration rule](https://developers.cloudflare.com/rules/configuration-rules/).

## Threat score

Previously, a threat score represented a Cloudflare threat score from 0–100, where 0 indicates low risk. Now, the threat score is always `0` (zero).

Recommendation

Currently we do not recommend creating rules based on the threat score, since this score is no longer being populated.

[PreviousReplace insecure JS libraries](https://developers.cloudflare.com/waf/tools/replace-insecure-js-libraries/)[NextValidation checks](https://developers.cloudflare.com/waf/tools/validation-checks/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/tools/security-level.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
