---
url: https://developers.cloudflare.com/rules/snippets/how-it-works/
title: How Snippets work \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-17T06:28:15.228523+00:00
---

# How Snippets work · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/snippets/how-it-works/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /[Snippets](https://developers.cloudflare.com/rules/snippets/)
  4. /How it works



# How Snippets work

Last updated Oct 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview1\. Evaluate snippet rules2\. Build Snippets table3\. Execute snippets code4\. Continue with the request execution workflowSubrequests made by a snippet

Cloudflare Snippets are executed based on rules defined within your zone. Here is how the process works:

![Diagram of the snippets execution workflow](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1546,height=491,format=webp/_astro/snippets-execution.Cb6ZLHBP.png)

## 1\. Evaluate snippet rules

For each incoming request, Cloudflare evaluates the expression of every snippet rule defined in the zone. The evaluation checks for a match based on various request properties (such as bot score, WAF attack score, country of origin, and cookies).

## 2\. Build Snippets table

For every snippet rule in a zone that matches an incoming request, Cloudflare adds the corresponding unique snippet ID to a Snippets table.

## 3\. Execute snippets code

Once all the rules have been evaluated and the full table has been compiled, Cloudflare starts processing all the snippet IDs in the table.

The snippets are executed sequentially. Each snippet receives the modified request from the previous snippet and applies new modifications to it.

## 4\. Continue with the request execution workflow

After executing the final snippet IDs, the resulting modified request is passed back to the request execution workflow. Refer to [Execution order](https://developers.cloudflare.com/rules/snippets/#execution-order) for more information on the Rules features evaluated before and after Cloudflare Snippets.

## Subrequests made by a snippet

When a snippet calls `fetch()` to a proxied hostname in the same zone, the request that the snippet makes is a subrequest. The incoming request that triggered the snippet is evaluated as normal, including by the security features configured for the hostname the visitor requested.

[WAF custom rules](https://developers.cloudflare.com/waf/custom-rules/) and [WAF managed rules](https://developers.cloudflare.com/waf/managed-rules/) on the target hostname are not evaluated for a same-zone subrequest made by a snippet. This applies to both `fetch(url)` and `fetch(request)`.

Caution

Do not rely on custom rules on the target hostname to restrict access to subrequests made by a snippet. To protect the target, apply protections to the incoming request that triggers the snippet, or validate the request at the target itself (for example, in your origin server or in a Worker).

[PreviousOverview](https://developers.cloudflare.com/rules/snippets/)[NextCreate in the dashboard](https://developers.cloudflare.com/rules/snippets/create-dashboard/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/snippets/how-it-works.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
