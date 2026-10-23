---
url: https://developers.cloudflare.com/waf/tools/validation-checks/
title: Validation checks \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:49.070484+00:00
---

# Validation checks · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/tools/validation-checks/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /Additional tools
  4. /Validation checks



# Validation checks

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/tools/validation-checks/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEvent logs for validation checks

Cloudflare performs a validation check for every request. The Validation component executes prior to all other security features like custom rules or Managed Rules. The validation check blocks malformed requests like Shellshock attacks and requests with certain attack patterns in their HTTP headers before any allowlist logic occurs.

Note

Currently, you cannot disable validation checks. They run early in Cloudflare's infrastructure before the configuration for domains has been loaded.

## Event logs for validation checks

Actions performed by the Validation component appear in [Sampled logs](https://developers.cloudflare.com/waf/analytics/security-events/#sampled-logs) in Security Events, associated with the `Validation` service and without a rule ID. Event logs downloaded from the API show source as `Validation` and action as `drop` when this behavior occurs.

The following example shows a request blocked by the Validation component due to a malformed `User-Agent` HTTP request header:

![Sampled logs displaying an example of a validation check event](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=972,height=439,format=webp/_astro/validation-service.CC6rqWo_.png)

In the downloaded JSON file for the event, the `ruleId` value indicates the detected issue — in this case, it was a Shellshock attack.
    
    
    {
    	"action": "drop",
    	"ruleId": "sanity-shellshock",
    	"source": "sanitycheck",
    	"userAgent": "() { :;}; printf \\\\\"detection[%s]string\\\\\" \\\\\"TjcLLwVzBtLzvbN\\\\"
    	//...
    }

[PreviousSecurity Level](https://developers.cloudflare.com/waf/tools/security-level/)[NextOverview](https://developers.cloudflare.com/waf/account/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/tools/validation-checks.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
