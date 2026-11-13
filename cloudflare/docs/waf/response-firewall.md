---
url: https://developers.cloudflare.com/waf/response-firewall/
title: Response firewall \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-11-13T09:17:05.430696+00:00
---

# Response firewall · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/response-firewall/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /Response firewall



# Response firewall

Last updated Nov 12, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAvailabilitySupported actionsSupported fields

The response firewall applies security rules to HTTP responses. Cloudflare turns on default protections for everyone, on every plan.

You can create response custom rules to block responses or log matches. These rules run in the `http_response_firewall_custom` [phase](https://developers.cloudflare.com/ruleset-engine/about/phases/).

## Availability

Every plan includes three response custom rules per zone. All rules count toward this allowance, including disabled rules.

You can include at most one rule with the `execute` action. An `execute` rule leaves two slots for `block` or `log` rules.

## Supported actions

Response custom rules support the following actions:

Action | Behavior  
---|---  
`block` | Block a matching response.  
`log` | Log a match.  
`execute` | Run the default protections alongside your custom rules.  
  
## Supported fields

Response custom rules support the request fields available in [WAF custom rules](https://developers.cloudflare.com/waf/custom-rules/). The same field entitlements apply to response custom rules.

You can also match on the following response fields:

Field | Supported raw variant  
---|---  
`http.response.code` | —  
`http.response.content_type.media_type` | —  
`http.response.headers` | `raw.http.response.headers`  
`http.response.headers.names` | `raw.http.response.headers.names`  
`http.response.headers.values` | `raw.http.response.headers.values`  
`http.response.set_cookies` | `raw.http.response.set_cookies`  
  
For requests to `/api/` paths, this expression matches responses with status code `500`:
    
    
    starts_with(http.request.uri.path, "/api/") and http.response.code eq 500

Response custom rules do not support matching on `http.response.body.raw`.

[PreviousCloudflare Sensitive Data Detection](https://developers.cloudflare.com/waf/managed-rules/reference/sensitive-data-detection/)[NextOverview](https://developers.cloudflare.com/waf/tools/lists/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/response-firewall/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
