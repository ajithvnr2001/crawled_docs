---
url: https://developers.cloudflare.com/waf/tools/lists/lists-api/
title: Lists API \u00b7 Cloudflare Web Application Firewall (WAF) docs
method: scrapling+scrapegraph
fetched_at: 2026-10-23T16:40:12.102229+00:00
---

# Lists API · Cloudflare Web Application Firewall (WAF) docs

> Source: https://developers.cloudflare.com/waf/tools/lists/lists-api/

  1. [Home](https://developers.cloudflare.com/)
  2. /[WAF](https://developers.cloudflare.com/waf/)
  3. /…

Additional tools

  4. /[Lists](https://developers.cloudflare.com/waf/tools/lists/)
  5. /Lists API



# Lists API

Last updated Oct 15, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/waf/tools/lists/lists-api/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewGet startedRate limiting for Lists API requests CrowdSec-managed lists

The [Lists API](https://developers.cloudflare.com/api/resources/rules/subresources/lists/) provides an interface for programmatically managing the following types of lists:

  * [Custom lists](https://developers.cloudflare.com/waf/tools/lists/custom-lists/): Contain one or more strings of the same type (such as IP addresses or hostnames) that you can reference collectively, by name, in rule expressions.

  * [Bulk Redirect Lists](https://developers.cloudflare.com/rules/url-forwarding/bulk-redirects/concepts/#bulk-redirect-lists): Contain URL redirects that you enable by creating a Bulk Redirect Rule.




To use a list in a rule expression, refer to [Lists](https://developers.cloudflare.com/ruleset-engine/rules-language/values/#lists) in the Rules language documentation.

## Get started

To get started, review the Lists [JSON object](https://developers.cloudflare.com/waf/tools/lists/lists-api/json-object/) and [Endpoints](https://developers.cloudflare.com/waf/tools/lists/lists-api/endpoints/).

* * *

## Rate limiting for Lists API requests

Cloudflare may apply rate limiting to your API requests creating, modifying, or deleting list items in custom lists and Bulk Redirect Lists.

Each operation (create, edit, or delete) on a list item counts as a modification. The following limits apply:

  * You can make a maximum of 1,000,000 list item modifications in API requests over 12 hours.
  * You can make a maximum of 30,000 API requests over 12 hours doing list item modifications.



If a write operation is still being processed — which happens asynchronously — and you submit a new request, you will receive a `429` HTTP status code. When this happens, submit your request again later.

### CrowdSec-managed lists

Lists that are kept up to date by a CrowdSec integration have a stricter limit: you can perform one bulk operation on each of these lists every 24 hours.

If you exceed this limit, the API rejects the request with a `429` HTTP status code and error code `10040`. The response does not include an `operation_id`, because the request is rejected before the bulk operation is created.

To avoid hitting this limit, schedule automated updates to run at most once every 24 hours, or use a separate custom list for more frequent updates.

[PreviousUse lists in expressions](https://developers.cloudflare.com/waf/tools/lists/use-in-expressions/)[NextJSON object](https://developers.cloudflare.com/waf/tools/lists/lists-api/json-object/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/waf/tools/lists/lists-api/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
