---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.multipart.empty_parts_count/
title: http.request.body.multipart.empty_parts_count \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-11-28T09:57:26.978122+00:00
---

# http.request.body.multipart.empty_parts_count · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.multipart.empty_parts_count/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Fields reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Http.Request.Body.Multipart.Empty_parts_count



# http.request.body.multipart.empty_parts_count

`http.request.body.multipart.empty_parts_count``Integer`

The number of headerless multipart parts with empty bodies skipped during parsing.

Requires a Cloudflare Enterprise plan.

These parts do not appear in the multipart part arrays and do not consume the exposed-part limit.

A part with headers and an empty body is not counted. A part with a whitespace-only body is not counted.

The count includes only parts encountered before parsing stops. Request body inspection and multipart parsing limits apply.

Example value:
    
    
    2

Example usage:
    
    
    http.request.body.multipart.empty_parts_count gt 0

Caution

All `http.request.body.*` fields (except [ `http.request.body.size`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.size/)) handle a given maximum body size, which varies per plan. For Enterprise customers, the maximum body size is 128 KB. For other paid plans, the limit is lower by default — reach out to your account team or to Cloudflare Support to increase the limit. For users in the Free plan, the limit is 1 MB.

You cannot define expressions that rely on request body data beyond the maximum size set for your plan. If the request body is larger, the body fields will contain a truncated value and the [`http.request.body.truncated`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.truncated/) field will be set to `true`. The [`http.request.body.size`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.size/) field will contain the full size of the request without any truncation.

The maximum body size applies only to the values of HTTP body fields — the origin server will still receive the complete request body.

Categories: 

  * Request
  * Body



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
