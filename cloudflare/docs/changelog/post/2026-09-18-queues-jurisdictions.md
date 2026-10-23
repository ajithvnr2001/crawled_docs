---
url: https://developers.cloudflare.com/changelog/post/2026-09-18-queues-jurisdictions/
title: Queues now supports EU, US, and FedRAMP jurisdictions \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:10:34.196966+00:00
---

# Queues now supports EU, US, and FedRAMP jurisdictions · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-18-queues-jurisdictions/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 12, 2026

## Queues now supports EU, US, and FedRAMP jurisdictions

[Queues](https://developers.cloudflare.com/queues/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now create [Cloudflare Queues](https://developers.cloudflare.com/queues/) with jurisdictional restrictions, ensuring that messages published to a queue are stored and processed only within a specific jurisdiction. This helps you comply with data residency requirements such as the [GDPR ↗︎](https://gdpr-info.eu/) or [FedRAMP ↗︎](https://blog.cloudflare.com/cloudflare-achieves-fedramp-authorization/).

To create a jurisdiction-restricted queue with the [Cloudflare CLI](https://developers.cloudflare.com/cf/) (`cf`), use the `--jurisdiction` flag:
    
    
    cf queues create --queue-name my-eu-queue --jurisdiction eu

You can also pass a `jurisdiction` parameter when calling the [Create Queue](https://developers.cloudflare.com/api/resources/queues/methods/create/) endpoint:
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/queues \
      --request POST \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
        "queue_name": "my-eu-queue",
        "jurisdiction": "eu"
      }'

Supported jurisdictions are `eu` (European Union), `us` (United States), and `fedramp` (FedRAMP-Moderate data centers). Jurisdiction can only be set when a queue is created and cannot be changed afterwards.

For more information, refer to [Queues data location](https://developers.cloudflare.com/queues/configuration/data-location/).
