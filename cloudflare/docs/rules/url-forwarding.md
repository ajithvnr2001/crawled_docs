---
url: https://developers.cloudflare.com/rules/url-forwarding/
title: Redirects \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-11-28T09:57:37.111575+00:00
---

# Redirects · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/url-forwarding/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /Redirects



# Redirects

Last updated Nov 27, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewChoose a redirect productRedirect productsRedirect Rules templatesAvailability Bulk Redirects Single RedirectsExecution orderTroubleshooting

A redirect sends visitors from one URL to another URL with an HTTP status code, such as `301`. Redirects are also known as URL forwarding. Single Redirects and Bulk Redirects replace the _Forwarding URL_ setting in Page Rules.

In the Cloudflare dashboard, Single Redirects appear as **Redirect Rules**.

## Choose a redirect product

Use the following table to choose a redirect product for your use case:

Goal | Product | Refer to  
---|---|---  
Move a whole domain or subdomain to a new hostname, keeping the path | Single Redirects | [Redirect requests to a different hostname](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-different-hostname/)  
Send every page of an old domain to the homepage of a new domain | Single Redirects | [Redirect requests for a domain to a new domain](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-all-different-domain-root/)  
Redirect one page to another page | Single Redirects | [Redirect visitors to a new page URL](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-new-url/)  
Redirect a section of a website, such as `/blog/*` to `blog.example.com/*` | Single Redirects | [Redirect a website section to a subdomain](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-section-to-subdomain/)  
Redirect all HTTP requests to HTTPS | Always Use HTTPS (recommended) | [Always Use HTTPS](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/always-use-https/)  
Redirect HTTP to HTTPS for some hostnames or paths only | Single Redirects | [Redirect admin area requests to HTTPS](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-admin-https/)  
Redirect `www` to the root domain, or the root domain to `www` | Single Redirects | [Redirect from WWW to root](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-www-to-root/), [Redirect from root to WWW](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-root-to-www/)  
Redirect visitors based on country | Single Redirects | [Redirect local visitors to specific subdomains](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-country-subdomains/), [Redirect visitors from one country to a subdomain](https://developers.cloudflare.com/rules/url-forwarding/examples/redirect-single-country-subdomain/)  
Redirect visitors based on device, such as mobile phones | Single Redirects | [Perform mobile redirects](https://developers.cloudflare.com/rules/url-forwarding/examples/perform-mobile-redirects/)  
Redirect using regular expressions (Business and Enterprise plans) | Single Redirects | [Remove locale from URL path](https://developers.cloudflare.com/rules/url-forwarding/examples/remove-locale-url/), Single Redirects availability  
Replace a Page Rule that uses the _Forwarding URL_ setting | Single Redirects | [Migrate Forwarding URL](https://developers.cloudflare.com/rules/reference/page-rules-migration/#migrate-forwarding-url)  
Redirect a list of specific URLs, such as old and new URLs from a migration | Bulk Redirects | [Create Bulk Redirects in the dashboard](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/create-dashboard/)  
Redirect the same path prefix on several domains (one URL redirect per hostname) | Bulk Redirects | [Subpath matching](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/parameters/#subpath-matching), [CSV file format](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/csv-file-format/)  
Redirect with custom logic that rules cannot express (Pro plan and above) | Snippets | [Bulk redirect based on a map object](https://developers.cloudflare.com/rules/snippets/examples/bulk-redirect-map/), [Country code redirect](https://developers.cloudflare.com/rules/snippets/examples/country-code-redirect/)  
  
To create a redirect, refer to [Create a redirect rule in the dashboard](https://developers.cloudflare.com/rules/url-forwarding/single-redirects/create-dashboard/) or [Create Bulk Redirects in the dashboard](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/create-dashboard/).

## Redirect products

  * [**Single Redirects**](https://developers.cloudflare.com/rules/url-forwarding/single-redirects/): Static or dynamic redirects for one zone (a domain you added to Cloudflare, including its subdomains). With a [wildcard pattern](https://developers.cloudflare.com/rules/url-forwarding/single-redirects/settings/#wildcard-url-redirect), one rule can cover thousands of URLs without functions or regular expressions. You can also match requests by country, device, header, or cookie with a [custom filter expression](https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/edit-expressions/).

  * [**Bulk Redirects**](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/): Lists of source and target URLs at the account level, which can apply across domains in your account. Each URL redirect maps one source URL to one target URL. Bulk Redirects do not support wildcards or regular expressions, but [URL redirect parameters](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/reference/parameters/), such as **Subpath matching** and **Include subdomains** , control how source URLs match.

  * [**Snippets**](https://developers.cloudflare.com/rules/snippets/): Short pieces of JavaScript code for complex redirect logic. Refer to the [Snippets examples](https://developers.cloudflare.com/rules/snippets/examples/) to get started.




Note

Single Redirects and Bulk Redirects require that you [proxy the DNS records](https://developers.cloudflare.com/dns/proxy-status/) of your domain (or subdomain) through Cloudflare.

## Redirect Rules templates

Cloudflare provides you with rules templates for common use cases.

  1. In the Cloudflare dashboard, go to the Rules **Overview** page.

[ Go to **Overview** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/rules/overview)
  2. Select **Templates** , and then select one of the available templates.




You can also refer to the [Examples gallery](https://developers.cloudflare.com/rules/examples/) in the developer docs.

Redirect templates include **Redirect from HTTP to HTTPS** , **Redirect from WWW to root** , and **Redirect from root to WWW**. The **Redirect from HTTP to HTTPS** template uses the request URL `http://*` and the target URL `https://${1}`.

The **Redirect from WWW to root** and **Redirect from root to WWW** templates match HTTPS requests only. To also redirect HTTP requests, turn on [Always Use HTTPS](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/always-use-https/), or change the request URL to start with `http*://` and update the wildcard references in the target URL. Refer to [How wildcard references are numbered](https://developers.cloudflare.com/rules/url-forwarding/single-redirects/settings/#how-wildcard-references-are-numbered).

## Availability

Single Redirects and Bulk Redirects are available on all Cloudflare plans. The exact quotas and features depend on your plan.

### Bulk Redirects

| Free | Pro | Business | Enterprise  
---|---|---|---|---  
Availability | Yes | Yes | Yes | Yes  
Bulk Redirect Rules | 15 | 15 | 15 | 50  
Bulk Redirect Lists | 5 | 5 | 5 | 25  
URL redirects across lists | 10,000 | 25,000 | 50,000 | 1,000,000  
  
For _URL redirects across lists_ , this table provides the default quota for the Enterprise plan. Bulk Redirects supports several million URL redirects — to get more redirects, contact your account team.

Bulk Redirects features and quotas are per account and they depend on the highest Cloudflare plan on your account.

### Single Redirects

| Free | Pro | Business | Enterprise  
---|---|---|---|---  
Availability | Yes | Yes | Yes | Yes  
Number of rules | 10 | 25 | 50 | 300  
Wildcard support | Yes | Yes | Yes | Yes  
Regex support | No | No | Yes | Yes  
  
Single Redirects features and quotas are per zone and depend on the zone plan.

## Execution order

The execution order of Rules features is the following:

  * [Single Redirects](https://developers.cloudflare.com/rules/url-forwarding/single-redirects/)
  * [URL Rewrite Rules](https://developers.cloudflare.com/rules/transform/url-rewrite/)
  * [Configuration Rules](https://developers.cloudflare.com/rules/configuration-rules/)
  * [Origin Rules](https://developers.cloudflare.com/rules/origin-rules/)
  * [Bulk Redirects](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/)
  * [Managed Transforms](https://developers.cloudflare.com/rules/transform/managed-transforms/)
  * [Request Header Transform Rules](https://developers.cloudflare.com/rules/transform/request-header-modification/)
  * [Cache Rules](https://developers.cloudflare.com/cache/how-to/cache-rules/)
  * [Snippets](https://developers.cloudflare.com/rules/snippets/)
  * [Cloud Connector](https://developers.cloudflare.com/rules/cloud-connector/)



The different types of rules listed above will take precedence over [Page Rules](https://developers.cloudflare.com/rules/page-rules/). This means that Page Rules will be overridden if there is a match for both Page Rules and the Rules products listed above.

Generally speaking, for [non-terminating actions](https://developers.cloudflare.com/ruleset-engine/rules-language/actions/) the last change made by rules in the same [phase](https://developers.cloudflare.com/ruleset-engine/about/phases/) will win (later rules can overwrite changes done by previous rules). However, for terminating actions (_Block_ , _Redirect_ , or one of the challenge actions), rule evaluation will stop and the action will be executed immediately.

For example, if multiple rules with the _Redirect_ action match, Cloudflare will always use the URL redirect of the first rule that matches. Also, if you configure URL redirects using different Cloudflare products (Single Redirects and Bulk Redirects), the product executed first will apply, if there is a rule match (in this case, Single Redirects).

Refer to the [Phases list](https://developers.cloudflare.com/ruleset-engine/reference/phases-list/) for the product execution order.

Caution

Using Cloudflare challenges along with Rules features may cause challenge loops. Refer to [Rules troubleshooting](https://developers.cloudflare.com/rules/reference/troubleshooting/) for more information.

## Troubleshooting

When troubleshooting URL redirects, use [Rules simulator](https://developers.cloudflare.com/rules/simulator/) to determine if a rule is triggering for a specific URL.

[PreviousSet response header with a static value](https://developers.cloudflare.com/rules/transform/examples/set-response-header-static-value/)[NextOverview](https://developers.cloudflare.com/rules/url-forwarding/single-redirects/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/url-forwarding/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
