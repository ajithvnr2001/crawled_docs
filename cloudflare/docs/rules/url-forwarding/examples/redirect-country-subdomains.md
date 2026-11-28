---
url: https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-country-subdomains/
title: Redirect local visitors to specific subdomains \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-11-28T09:57:36.665346+00:00
---

# Redirect local visitors to specific subdomains · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-country-subdomains/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Redirects](https://developers.cloudflare.com/rules/url-forwarding/)

  4. /[Examples](https://developers.cloudflare.com/rules/url-forwarding/examples/)
  5. /Redirect local visitors to specific subdomains



# Redirect local visitors to specific subdomains

Create a redirect rule to send visitors from specific countries to localized subdomains, such as `gb.example.com` and `fr.example.com`.

Last updated Nov 27, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This example single redirect for zone `example.com` will redirect United Kingdom and France visitors requesting the website's root path (`/`) to their localized subdomains `https://gb.example.com` and `https://fr.example.com`, respectively.

**When incoming requests match**

Using the Expression Editor:  
`http.host eq "example.com" and (ip.src.country eq "GB" or ip.src.country eq "FR") and http.request.uri.path eq "/"`

**Then**

  * **Type:** _Dynamic_
  * **Expression:** `lower(concat("https://", ip.src.country, ".example.com"))`
  * **Status code:** _302_



The `http.host eq "example.com"` condition prevents a redirect loop. Without it, a visitor from the United Kingdom who requests `https://gb.example.com/` would match the rule again and be redirected to the same URL.

This example uses a `302` (temporary) status code. Browsers can cache `301` (permanent) redirects, and Cloudflare does not add a `Cache-Control` header to redirect responses. A visitor who later browses from another country might keep receiving a cached `301` redirect.

For example, the redirect rule would perform the following redirects:

Visitor country | Request URL | Target URL | Status code  
---|---|---|---  
United Kingdom | `https://example.com/` | `https://gb.example.com` | `302`  
France | `https://example.com/` | `https://fr.example.com` | `302`  
United Kingdom | `https://gb.example.com/` | (unchanged) | n/a  
United States | `https://example.com/` | (unchanged) | n/a  
  
To redirect visitors from one country with the Expression Builder and a static target URL, refer to [Redirect visitors from one country to a subdomain](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-single-country-subdomain/).

[PreviousRedirect from WWW to root](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-www-to-root/)[NextRedirect requests for a domain to a new domain](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-different-domain-root/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/url-forwarding/examples/redirect-country-subdomains.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
