---
url: https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-admin-https/
title: Redirect admin area requests to HTTPS \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-11-28T09:57:36.627670+00:00
---

# Redirect admin area requests to HTTPS · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-admin-https/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Redirects](https://developers.cloudflare.com/rules/url-forwarding/)

  4. /[Examples](https://developers.cloudflare.com/rules/url-forwarding/examples/)
  5. /Redirect admin area requests to HTTPS



# Redirect admin area requests to HTTPS

Create a redirect rule to redirect requests for the administration area of `store.example.com` to HTTPS, keeping the original path and query string.

Last updated Nov 27, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

This example single redirect for zone `example.com` will redirect requests for the administration area of a specific subdomain (`store.example.com`) to HTTPS, keeping the original path and query string.

**When incoming requests match**

  * **Wildcard pattern**
    * **Request URL** : `http://store.example.com/admin*`



**Then**

  * **Target URL** : `https://store.example.com/admin${1}`
  * **Status code:** _301_
  * **Preserve query string:** Enabled



The request URL ends in `/admin*`, so it also matches other paths that start with `/admin`, such as `/administrator/`. To redirect only the admin area, use the request URL `http://store.example.com/admin/*` with the target URL `https://store.example.com/admin/${1}`. This pattern does not match `/admin` without a trailing slash, so create a second rule for that URL if needed.

For example, the redirect rule would perform the following redirects:

Request URL | Target URL | Status code  
---|---|---  
`http://store.example.com/admin/products/` | `https://store.example.com/admin/products/` | `301`  
`https://store.example.com/admin/products/` | (unchanged) | n/a  
`http://store.example.com/admin/?logged_out=true` | `https://store.example.com/admin/?logged_out=true` | `301`  
`http://store.example.com/?all_items=true` | (unchanged) | n/a  
`http://example.com/admin/` | (unchanged) | n/a  
  
[PreviousRedirect a website section to a subdomain](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-section-to-subdomain/)[NextRedirect from root to WWW](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-root-to-www/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/url-forwarding/examples/redirect-admin-https.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
