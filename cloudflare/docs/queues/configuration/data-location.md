---
url: https://developers.cloudflare.com/queues/configuration/data-location/
title: Data location \u00b7 Cloudflare Queues docs
method: scrapling+scrapegraph
fetched_at: 2026-10-13T08:46:37.277766+00:00
---

# Data location · Cloudflare Queues docs

> Source: https://developers.cloudflare.com/queues/configuration/data-location/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Queues](https://developers.cloudflare.com/queues/)
  3. /[Configuration](https://developers.cloudflare.com/queues/configuration/)
  4. /Data location



# Data location

Last updated Oct 12, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSupported jurisdictionsCreate a queue with a jurisdiction Use the dashboard Use the cf CLI Use the REST APIDead Letter Queues

By default, Queues stores and processes messages across Cloudflare's global network. You can restrict a queue to a jurisdiction to meet data residency requirements, such as the [General Data Protection Regulation (GDPR) ↗︎](https://gdpr-info.eu/) or [FedRAMP ↗︎](https://blog.cloudflare.com/cloudflare-achieves-fedramp-authorization/).

Workers can produce to and consume from a restricted queue from any location. The jurisdiction only restricts where Queues stores and processes messages.

## Supported jurisdictions

Parameter | Location  
---|---  
`eu` | European Union  
`us` | United States  
`fedramp` | FedRAMP-Moderate data centers  
  
## Create a queue with a jurisdiction

### Use the dashboard

  1. In the Cloudflare dashboard, go to **Queues**.

[ Go to **Queues** ↗ ](https://dash.cloudflare.com/?to=/:account/workers/queues)
  2. Select **Create queue**.

  3. Enter a queue name and select a jurisdiction.

  4. Select **Create queue**.




### Use the cf CLI

With the [Cloudflare CLI](https://developers.cloudflare.com/cf/) (`cf`) installed and authenticated, use the `--jurisdiction` flag to create a restricted queue:
    
    
    cf queues create --queue-name my-eu-queue --jurisdiction eu

### Use the REST API

Set the `jurisdiction` parameter when you create a queue with the [Create Queue](https://developers.cloudflare.com/api/resources/queues/methods/create/) endpoint:
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/queues \
      --request POST \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
        "queue_name": "my-eu-queue",
        "jurisdiction": "eu"
      }'

You can only set a jurisdiction when you create a queue. You cannot add, change, or remove the jurisdiction later.

The dashboard displays a queue's jurisdiction on the Queues overview and settings pages.

## Dead Letter Queues

A [Dead Letter Queue (DLQ)](https://developers.cloudflare.com/queues/configuration/dead-letter-queues/) must use the same jurisdiction as its source queue. If you specify a queue name that does not exist as the DLQ, Cloudflare automatically creates that queue in the same jurisdiction as the source queue.

[PreviousConfigure Queues](https://developers.cloudflare.com/queues/configuration/configure-queues/)[NextBatching, Retries and Delays](https://developers.cloudflare.com/queues/configuration/batching-retries/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/queues/configuration/data-location.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
