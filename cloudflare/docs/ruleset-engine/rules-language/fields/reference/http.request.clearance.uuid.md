---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.clearance.uuid/
title: http.request.clearance.uuid \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-23T16:39:49.388030+00:00
---

# http.request.clearance.uuid · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.request.clearance.uuid/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Http.Request.Clearance.Uuid



# http.request.clearance.uuid

`http.request.clearance.uuid``String`

Provides the stable UUID from a valid Cloudflare clearance cookie.

Use this field as an Advanced Rate Limiting characteristic to keep the same request counter when Cloudflare refreshes the encrypted `cf_clearance` cookie value.

The value is an empty string when the request does not contain a valid clearance cookie. Use `http.request.clearance.uuid ne ""` in the counting expression to exclude those requests from the clearance counter.

Categories: 

  * Request
  * Cloudflare



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
