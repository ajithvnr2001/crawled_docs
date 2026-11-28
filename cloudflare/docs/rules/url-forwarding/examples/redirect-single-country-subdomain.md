---
url: https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-single-country-subdomain/
title: Redirect visitors from one country to a subdomain \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-11-28T09:57:27.344829+00:00
---

# Redirect visitors from one country to a subdomain · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-single-country-subdomain/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Redirects](https://developers.cloudflare.com/rules/url-forwarding/)

  4. /[Examples](https://developers.cloudflare.com/rules/url-forwarding/examples/)
  5. /Redirect visitors from one country to a subdomain



# Redirect visitors from one country to a subdomain

Create a redirect rule with the Expression Builder to temporarily redirect visitors from one country to a localized subdomain.

Last updated Nov 27, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This example single redirect for zone `example.com` will redirect visitors from Germany who request the website's root path (`/`) to `https://de.example.com/`. You can create this rule with the Expression Builder and a static target URL, without writing an expression.

**When incoming requests match**

  * **Custom filter expression**



Using the Expression Builder:

  * _Hostname_ _equals_ `example.com` **AND**
  * _Country_ _equals_ _Germany_ **AND**
  * _URI Path_ _equals_ `/`



If you are using the Expression Editor, enter the following expression:  
`(http.host eq "example.com" and ip.src.country eq "DE" and http.request.uri.path eq "/")`

**Then**

  * **Type:** _Static_
  * **URL:** `https://de.example.com/`
  * **Status code:** _302_
  * **Preserve query string:** Enabled



The _Hostname_ condition prevents a redirect loop. Without it, a visitor from Germany who requests `https://de.example.com/` would match the rule again and be redirected to the same URL.

This example uses a `302` (temporary) status code. Browsers can cache `301` (permanent) redirects, and Cloudflare does not add a `Cache-Control` header to redirect responses. A visitor who later browses from another country might keep receiving a cached `301` redirect.

For example, the redirect rule would perform the following redirects:

Visitor country | Request URL | Target URL | Status code  
---|---|---|---  
Germany | `https://example.com/` | `https://de.example.com/` | `302`  
Germany | `https://example.com/?ref=1` | `https://de.example.com/?ref=1` | `302`  
Germany | `https://de.example.com/` | (unchanged) | n/a  
United States | `https://example.com/` | (unchanged) | n/a  
  
To redirect every path for visitors from one country to another domain, refer to [Redirect requests from one country to a domain](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-country/). That example uses Bulk Redirects and the Expression Editor.

[PreviousRedirect requests to a different hostname](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-different-hostname/)[NextRedirect visitors to a new page URL](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-new-url/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/url-forwarding/examples/redirect-single-country-subdomain.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
