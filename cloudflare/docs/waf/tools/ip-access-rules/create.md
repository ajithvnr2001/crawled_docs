---
url: https://developers.cloudflare.com/waf/tools/ip-access-rules/create/
title: Create an IP access rule \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:48.230019+00:00
---

# Create an IP access rule · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/tools/ip-access-rules/create/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

Additional tools

  4. /[IP Access rules](https://developers.cloudflare.com/waf/tools/ip-access-rules/)
  5. /Create a rule



# Create an IP access rule

Last updated Aug 3, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/tools/ip-access-rules/create/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Recommendation: Use custom rules instead

Cloudflare recommends that you create [custom rules](https://developers.cloudflare.com/waf/custom-rules/) instead of IP Access rules to perform IP-based or geography-based blocking (geoblocking).

Caution

For [Spectrum](https://developers.cloudflare.com/spectrum/) applications configured with the non-HTTP/HTTPS application type, IP Access rules are the only supported mechanism for filtering traffic by IP address, IP range, country, or ASN. To use them, enable IP Access rules in your [Spectrum app configuration](https://developers.cloudflare.com/spectrum/reference/configuration-options/#ip-access-rules).

Note

The **IP access rules** option appears only if you have configured at least one IP access rule.

  1. In the Cloudflare dashboard, go to the **Security rules** page.

[ Go to **Security rules** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/security-rules)
  2. Select **Create rule** > **IP access rules**.

  3. Enter the following rule details:

     1. For **IP, IP range, country name, or ASN** , enter an IP address, IP range, country code/name, or Autonomous System Number (ASN). For details, refer to [IP Access rules parameters](https://developers.cloudflare.com/waf/tools/ip-access-rules/parameters/).
     2. For **Action** , select an [action](https://developers.cloudflare.com/waf/tools/ip-access-rules/actions/).
     3. For **Zone** , select whether the rule applies to the current website only or to all websites in the account.
     4. (Optional) Enter a note for the rule (for example, `Payment Gateway`).
  4. Select **Create**.




Use the Cloudflare API to programmatically create IP access rules. For more information, refer to [Create an IP Access Rule](https://developers.cloudflare.com/api/resources/firewall/subresources/access_rules/methods/create/).

[PreviousOverview](https://developers.cloudflare.com/waf/tools/ip-access-rules/)[NextParameters](https://developers.cloudflare.com/waf/tools/ip-access-rules/parameters/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/tools/ip-access-rules/create.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
