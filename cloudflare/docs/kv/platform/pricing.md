---
url: https://developers.cloudflare.com/kv/platform/pricing/
title: Pricing \u00b7 Cloudflare Workers KV docs
method: scrapling+scrapegraph
fetched_at: 2026-10-31T08:10:20.309488+00:00
---

# Pricing · Cloudflare Workers KV docs

> Source: https://developers.cloudflare.com/kv/platform/pricing/

  1. [Home](https://developers.cloudflare.com/)
  2. /[KV](https://developers.cloudflare.com/kv/)
  3. /Platform
  4. /Pricing



# Pricing

Last updated Oct 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPricing FAQ How much do additional namespaces cost? When writing via KV's REST API, how are writes charged? Do queries I issue from the dashboard or wrangler (the CLI) count as billable usage? Does Workers KV charge for data transfer / egress? What operations incur operations charges?

Workers KV is included in both the Free and Paid [Workers plans](https://developers.cloudflare.com/workers/platform/pricing/).

| Free plan1 | Paid plan  
---|---|---  
Keys read | 100,000 / day | 10 million/month, + $0.50/million  
Keys written | 1,000 / day | 1 million/month, + $5.00/million  
Keys deleted | 1,000 / day | 1 million/month, + $5.00/million  
List requests | 1,000 / day | 1 million/month, + $5.00/million  
Stored data | 1 GB | 1 GB, + $0.50/ GB-month  
Namespaces | 1,000 | Unlimited, with a default limit of 1,000. First 1,000 included + $0.10 per additional namespace per month.  
  
Refer to [KV limits](https://developers.cloudflare.com/kv/platform/limits/#workers-kv) for namespace creation limits and limit increases.

1 The Workers Free plan includes limited Workers KV usage. Daily usage limits reset daily at 00:00 UTC. If you exceed any one of these limits, further operations of that type will fail with an error.

Note

Workers KV pricing for read, write and delete operations is on a per-key basis. Bulk read operations are billed by the amount of keys read in a bulk read operation.

## Pricing FAQ

### How much do additional namespaces cost?

The Workers Paid plan includes 1,000 namespaces per account. Each additional namespace costs $0.10 per month.

For example, 1,050 namespaces existing for a full billing month cost `(1,050 - 1,000) × $0.10 = $5.00` for the 50 additional namespaces. Read, write, delete, list, and storage charges apply separately.

### When writing via KV's [REST API](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/subresources/keys/methods/bulk_update/), how are writes charged?

Each key-value pair in the `PUT` request is counted as a single write, identical to how each call to `PUT` in the Workers API counts as a write. Writing 5,000 keys via the REST API incurs the same write costs as making 5,000 `PUT` calls in a Worker.

### Do queries I issue from the dashboard or wrangler (the CLI) count as billable usage?

Yes, any operations via the Cloudflare dashboard or wrangler, including updating (writing) keys, deleting keys, and listing the keys in a namespace count as billable KV usage.

### Does Workers KV charge for data transfer / egress?

No.

### What operations incur operations charges?

All operations incur charges, including fetches for non-existent keys that return a `null` (Workers API) or `HTTP 404` (REST API). These operations still traverse KV's infrastructure.

[PreviousMetrics and analytics](https://developers.cloudflare.com/kv/observability/metrics-analytics/)[NextLimits](https://developers.cloudflare.com/kv/platform/limits/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/kv/platform/pricing.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
