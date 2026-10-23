---
url: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.content_scan.has_encrypted_obj/
title: cf.waf.content_scan.has_encrypted_obj \u00b7 Cloudflare Ruleset Engine docs
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:09:57.793924+00:00
---

# cf.waf.content_scan.has_encrypted_obj · Cloudflare Ruleset Engine docs

> Source: https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.waf.content_scan.has_encrypted_obj/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Ruleset Engine](https://developers.cloudflare.com/ruleset-engine/)
  3. /…

[Rules Language](https://developers.cloudflare.com/ruleset-engine/rules-language/)[Fields](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/)

  4. /[Reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/)
  5. /Cf.Waf.Content_scan.Has_encrypted_obj



# cf.waf.content_scan.has_encrypted_obj

`cf.waf.content_scan.has_encrypted_obj``Boolean`

Indicates whether the request contains at least one password-protected (encrypted) content object.

Requires a Cloudflare Enterprise plan with [malicious uploads detection](https://developers.cloudflare.com/waf/detections/malicious-uploads/).

Refer to [Encrypted content](https://developers.cloudflare.com/waf/detections/malicious-uploads/#encrypted-content) for the file types this field covers.

Example usage:
    
    
    # Block requests containing password-protected uploads
    cf.waf.content_scan.has_encrypted_obj and http.request.uri.path eq "/upload"

Categories: 

  * Request



Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/fields/index.yaml)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
