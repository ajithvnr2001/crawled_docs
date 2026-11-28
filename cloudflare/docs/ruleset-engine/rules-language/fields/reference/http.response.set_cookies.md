---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.response.set_cookies/
title: http.response.set_cookies \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-11-28T09:57:27.421828+00:00
---

# http.response.set_cookies · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/http.response.set_cookies/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Fields reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Http.Response.Set_cookies



# http.response.set_cookies

`http.response.set_cookies``Map<Array<String>>`

The parsed cookies from the current HTTP response `Set-Cookie` headers.

Map keys are URL-decoded cookie names. Cookie names that become identical after decoding share an array of values, in occurrence order.

Cookie values are not URL decoded. Attributes such as `Path`, `Secure`, and `HttpOnly` are not included in the values.

This field reflects response header changes from earlier phases. Fields remain immutable within a phase. Refer to [Field values during rule evaluation](https://developers.cloudflare.com/ruleset-engine/about/rules/#field-values-during-rule-evaluation).

To inspect the original response cookies, use [`raw.http.response.set_cookies`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/raw.http.response.set_cookies/).

The availability of HTTP response fields depends on the Cloudflare feature and your plan.

Example value:
    
    
    {"app": ["test", "preview"]}

Example usage:
    
    
    http.response.set_cookies["app"][0] eq "test"

Categories: 

  * Response
  * Headers



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
