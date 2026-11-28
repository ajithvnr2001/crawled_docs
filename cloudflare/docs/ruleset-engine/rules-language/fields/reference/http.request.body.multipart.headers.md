---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.multipart.headers/
title: http.request.body.multipart.headers \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-11-28T09:57:27.298514+00:00
---

# http.request.body.multipart.headers · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.multipart.headers/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Fields reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Http.Request.Body.Multipart.Headers



# http.request.body.multipart.headers

`http.request.body.multipart.headers``Array<Map<Array<String>>>`

The headers of each parsed multipart part, grouped by lowercase header name.

Requires a Cloudflare Enterprise plan.

The outer array follows the same part order as [`http.request.body.multipart.values`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.multipart.values/). Each map includes standard and custom headers. Repeated header names share an array of values in occurrence order.

A part with a body but no headers has an empty map. Parts with no headers and an empty body are excluded from the part arrays and counted by [`http.request.body.multipart.empty_parts_count`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.multipart.empty_parts_count/).

Folded header values are unfolded. Request body inspection and multipart parsing limits apply.

Example value:
    
    
    [{"content-type": ["text/plain"], "x-upload-tag": ["first", "second"]}, {}]

Example usage:
    
    
    http.request.body.multipart.headers[0]["x-upload-tag"][0] eq "first"

Caution

All `http.request.body.*` fields (except [ `http.request.body.size`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.size/)) handle a given maximum body size, which varies per plan. For Enterprise customers, the maximum body size is 128 KB. For other paid plans, the limit is lower by default — reach out to your account team or to Cloudflare Support to increase the limit. For users in the Free plan, the limit is 1 MB.

You cannot define expressions that rely on request body data beyond the maximum size set for your plan. If the request body is larger, the body fields will contain a truncated value and the [`http.request.body.truncated`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.truncated/) field will be set to `true`. The [`http.request.body.size`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.body.size/) field will contain the full size of the request without any truncation.

The maximum body size applies only to the values of HTTP body fields — the origin server will still receive the complete request body.

Categories: 

  * Request
  * Body
  * Headers



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
