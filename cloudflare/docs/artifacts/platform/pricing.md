---
url: https://developers.cloudflare.com/artifacts/platform/pricing/
title: Pricing \u00b7 Cloudflare Artifacts docs
method: scrapling+scrapegraph
fetched_at: 2026-11-20T09:50:41.224219+00:00
---

# Pricing · Cloudflare Artifacts docs

> Source: https://developers.cloudflare.com/artifacts/platform/pricing/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Artifacts](https://developers.cloudflare.com/artifacts/)
  3. /Platform
  4. /Pricing



# Pricing

Last updated Nov 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewArtifacts pricingStorage usageRepository pricing (coming soon)

Artifacts is currently only available on the Workers Paid plan.

Note

Cloudflare will begin billing for Artifacts operations and storage on November 19, 2026.

Artifacts pricing is billed on two dimensions:

  * **Operations** : the number of repo operations, such as `create`, `push`, and `pull`.
  * **Storage** : the total amount of stored data, measured in gigabyte-months (`GB-mo`).



## Artifacts pricing

Unit | Workers Free | Workers Paid  
---|---|---  
Operations (1,000 operations)1 | Unavailable | First 10,000 per month + $0.15 per additional 1,000 operations  
Storage (GB-mo) | Unavailable | First 1 GB per month + $0.50 per additional GB-mo  
  
1 Pulls (including Git clones and fetches), pushes, creates, forks, and deletes each count as 1 operation. Reads of repo content, such as files, trees, commits, and logs, are billed at a 100:1 ratio, and token operations, such as creating or revoking a repo token, at a 5:1 ratio. For example, 100 reads or 5 token operations count as 1 operation for billing purposes. These ratios do not affect Artifacts metrics and analytics, which reflect actual usage.

## Storage usage

Storage is billed using gigabyte-month (`GB-mo`) as the billing metric, identical to [Durable Objects SQL storage](https://developers.cloudflare.com/durable-objects/platform/pricing/#sqlite-storage-backend). A `GB-mo` is calculated by averaging peak storage per day over a 30-day billing period.

  * Storage is calculated across all repositories.
  * Replicas do not add storage charges. Storage is replicated by default, and you do not need to manage repository availability or uptime.
  * Repos remain stored until you explicitly delete them.



## Repository pricing (coming soon)

In addition to operations and storage, Artifacts will bill for the number of repositories an account stores. Repository charges are not part of the November 19, 2026 billing start. Cloudflare will notify you before repository charges begin.

Unit | Workers Free | Workers Paid  
---|---|---  
Repositories | Unavailable | First 100,000 per month + $0.01 per additional repository  
  
[PreviousSandbox SDK + Artifacts](https://developers.cloudflare.com/artifacts/examples/sandbox-sdk-artifacts/)[NextLimits](https://developers.cloudflare.com/artifacts/platform/limits/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/artifacts/platform/pricing.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
