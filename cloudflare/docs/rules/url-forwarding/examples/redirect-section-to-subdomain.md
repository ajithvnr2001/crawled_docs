---
url: https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-section-to-subdomain/
title: Redirect a website section to a subdomain \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-11-28T09:57:27.025091+00:00
---

# Redirect a website section to a subdomain · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-section-to-subdomain/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Redirects](https://developers.cloudflare.com/rules/url-forwarding/)

  4. /[Examples](https://developers.cloudflare.com/rules/url-forwarding/examples/)
  5. /Redirect a website section to a subdomain



# Redirect a website section to a subdomain

Redirect requests for a section of your website, such as `/blog/`, to a subdomain while keeping the rest of the path and the query string.

Last updated Nov 27, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRedirect the section root without a trailing slashMigrate from Page Rules

This example single redirect sends visitors from `www.example.com/blog/` to the subdomain `blog.example.com`. The redirect keeps the rest of the path and the query string.

Use this redirect when you move part of your website to a new hostname. For example, you might move a blog to [Cloudflare Pages](https://developers.cloudflare.com/pages/) on its own subdomain.

**When incoming requests match**

  * **Wildcard pattern**
    * **Request URL** : `http*://www.example.com/blog/*`



**Then**

  * **Target URL** : `https://blog.example.com/${2}`
  * **Status code** : _301_
  * **Preserve query string** : Enabled



In the request URL, the `*` in `http*` is `${1}`, and the second `*` captures everything after `/blog/`. Refer to [How wildcard references are numbered](https://developers.cloudflare.com/rules/url-forwarding/single-redirects/settings/#how-wildcard-references-are-numbered).

For example, the redirect rule would perform the following redirects:

Request URL | Target URL | Status code  
---|---|---  
`https://www.example.com/blog/2009/05/my-post.html` | `https://blog.example.com/2009/05/my-post.html` | `301`  
`http://www.example.com/blog/` | `https://blog.example.com/` | `301`  
`https://www.example.com/blog/archive?page=2` | `https://blog.example.com/archive?page=2` | `301`  
`https://www.example.com/Blog/archive` | `https://blog.example.com/archive` | `301`  
`https://www.example.com/blog` | (unchanged) | n/a  
`https://www.example.com/about/` | (unchanged) | n/a  
  
Wildcard matching ignores upper and lower case, so the rule also redirects `/Blog/`. The rule does not redirect `https://www.example.com/blog`, because the request URL requires a slash after `/blog`. To redirect this URL, refer to Redirect the section root without a trailing slash.

## Redirect the section root without a trailing slash

The request URL `http*://www.example.com/blog/*` does not match `/blog` without a trailing slash. A Page Rule with the URL `www.example.com/blog/*` does not match `/blog` either, so this second rule is optional.

To redirect `/blog`, create a second redirect rule. Use a custom filter expression so that the rule also matches requests with a query string, such as `/blog?page=2`:

**When incoming requests match**

  * **Custom filter expression**



Using the Expression Builder:

  * _Hostname_ _equals_ `www.example.com` **AND**
  * _URI Path_ _equals_ `/blog`



If you are using the Expression Editor, enter the following expression:  
`(http.host eq "www.example.com" and lower(http.request.uri.path) eq "/blog")`

**Then**

  * **Type:** _Static_
  * **URL:** `https://blog.example.com/`
  * **Status code:** _301_
  * **Preserve query string:** Enabled



The _equals_ operator is case-sensitive, so the Expression Builder version does not match `/Blog`. The Expression Editor version uses the `lower()` function to also match `/Blog` and `/BLOG`.

For example, the second redirect rule would perform the following redirects:

Request URL | Target URL | Status code  
---|---|---  
`https://www.example.com/blog` | `https://blog.example.com/` | `301`  
`https://www.example.com/blog?page=2` | `https://blog.example.com/?page=2` | `301`  
`https://www.example.com/blogroll` | (unchanged) | n/a  
  
Do not use the wildcard pattern `http*://www.example.com/blog*` for this rule. It would also match unrelated paths, redirecting `/blogroll` to `https://blog.example.com/roll`, and it would redirect `/blog/post` to `https://blog.example.com//post`, with a double slash.

## Migrate from Page Rules

This redirect replaces a Page Rule with the following configuration:

  * **URL** : `www.example.com/blog/*`
  * **Setting** : _Forwarding URL_
  * **Select Status code** : _301 - Permanent Redirect_
  * **Destination URL** : `https://blog.example.com/$1`



This Page Rule URL does not include a URI scheme, so its first wildcard (`$1`) is the rest of the path after `/blog/`. In the redirect rule, the `*` in `http*` is the first wildcard (`${1}`), so the path is `${2}`.

For more information, refer to [Migrate Forwarding URL](https://developers.cloudflare.com/rules/reference/page-rules-migration/#migrate-forwarding-url).

[PreviousPerform mobile redirects](https://developers.cloudflare.com/rules/url-forwarding/examples/perform-mobile-redirects/)[NextRedirect admin area requests to HTTPS](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-admin-https/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/url-forwarding/examples/redirect-section-to-subdomain.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
