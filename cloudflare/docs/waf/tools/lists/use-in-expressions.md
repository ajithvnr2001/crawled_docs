---
url: https://developers.cloudflare.com/waf/tools/lists/use-in-expressions/
title: Use lists in expressions \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:48.505876+00:00
---

# Use lists in expressions · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/tools/lists/use-in-expressions/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

Additional tools

  4. /[Lists](https://developers.cloudflare.com/waf/tools/lists/)
  5. /Use lists in expressions



# Use lists in expressions

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/tools/lists/use-in-expressions/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewUse a list in the Expression BuilderUse a list in the Expression Editor

In the Cloudflare dashboard, there are two options for editing [expressions](https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/):

  * [Expression Builder](https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/edit-expressions/#expression-builder): Allows you to create expressions using drop-down lists, emphasizing a visual approach to defining an expression.
  * [Expression Editor](https://developers.cloudflare.com/ruleset-engine/rules-language/expressions/edit-expressions/#expression-editor): A text-only interface that supports advanced features, such as grouping symbols and functions for transforming and validating values.



## Use a list in the Expression Builder

To use a list in the Expression Builder:

  1. From the **Operator** drop-down list, select _is in list_ or _is not in list_. Note that not all fields support these operators.

![Selecting an IP list from the Value drop-down list when configuring the expression of a WAF custom rule](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=979,height=739,format=webp/_astro/cf-open-proxies-list.DYcEfIK7.png)
  2. Select a list from the **Value** drop-down list. Depending on your plan, you may be able to select a [Managed IP List](https://developers.cloudflare.com/waf/tools/lists/managed-lists/#managed-ip-lists).

  3. To commit your changes and enable the rule, select **Deploy**. If you are not ready to enable the rule, select **Save as Draft**.




## Use a list in the Expression Editor

To use a list in the Expression Editor, specify the `in` operator and use `$<list_name>` to specify the name of the list.

Examples:

  * Expression matching requests from IP addresses that are in an IP list named `office_network`:
        
        ip.src in $office_network

  * Expression matching requests with a source IP address different from IP addresses in the `office_network` IP list:
        
        not ip.src in $office_network

  * Expression matching requests from IP addresses in the Cloudflare Open Proxies [Managed IP List](https://developers.cloudflare.com/waf/tools/lists/managed-lists/#managed-ip-lists):
        
        ip.src in $cf.open_proxies




[PreviousCreate in the dashboard](https://developers.cloudflare.com/waf/tools/lists/create-dashboard/)[NextOverview](https://developers.cloudflare.com/waf/tools/lists/lists-api/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/tools/lists/use-in-expressions.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
