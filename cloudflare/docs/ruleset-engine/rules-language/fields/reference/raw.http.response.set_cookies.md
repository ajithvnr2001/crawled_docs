---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/raw.http.response.set_cookies/
title: raw.http.response.set_cookies \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-11-28T09:57:27.396865+00:00
---

# raw.http.response.set_cookies · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/raw.http.response.set_cookies/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Fields reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Raw.Http.Response.Set_cookies



# raw.http.response.set_cookies

`raw.http.response.set_cookies``Map<Array<String>>`

The parsed cookies from the original HTTP response `Set-Cookie` headers.

This is the raw field version of [`http.response.set_cookies`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.response.set_cookies/). It preserves the original response cookies and is unaffected by subsequent response header changes.

The same cookie parsing applies to both fields: names are URL decoded, duplicate names share an array of values, and values exclude cookie attributes. The `raw.` prefix does not disable parsing or name decoding.

The availability of HTTP response fields depends on the Cloudflare feature and your plan.

Example value:
    
    
    {"app": ["test", "preview"]}

Example usage:
    
    
    raw.http.response.set_cookies["app"][0] eq "test"

Categories: 

  * Response
  * Headers



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
