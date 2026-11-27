---
url: https://developers.cloudflare.com/changelog/post/2026-11-25-update-sink-credentials-and-pipelines/
title: Pipelines Sink credentials can now be updated \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-27T10:39:57.836116+00:00
---

# Pipelines Sink credentials can now be updated · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-25-update-sink-credentials-and-pipelines/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 25, 2026

## Pipelines Sink credentials can now be updated

[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/)[Basin](https://developers.cloudflare.com/basin/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now replace the credentials of a [Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/) [sink](https://developers.cloudflare.com/basin-pipelines/sinks/). Previously, an expired or revoked token meant deleting and recreating the sink.

Pipelines keep the sink's earlier credentials until you update them. Updating a [failed pipeline](https://developers.cloudflare.com/basin-pipelines/pipelines/manage-pipelines/#fix-a-failed-pipeline) automatically restarts it.

![A failed pipeline's page with the reason it failed, the sink that changed, and the Update pipeline button](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1464,height=202,format=webp/_astro/pipeline-failed-update.BfN-FzVj.png)

#### Dashboard

  * **Update credentials** — On a sink's page, in **Destination**. Create a new API token, or enter the credentials of a token you created.
  * **Update pipeline** — On a pipeline's page, when a stream or sink it uses has changed.

[ Go to **Sinks** ↗ ](https://dash.cloudflare.com/?to=/:account/pipelines/sinks) ![The Update credentials dialog with two options: create a new API token, or enter credentials](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1152,height=652,format=webp/_astro/sink-update-credentials.BIUnRpCC.png)

#### API

Both requests need an [API token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) with **Basin Pipelines Edit** permission.

First, update the sink. The following is an example of updating credentials of an R2 sink.
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/pipelines/v1/sinks/$SINK_ID" \
      --request PATCH \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --json '{
        "config": {
          "credentials": {
            "access_key_id": "<ACCESS_KEY_ID>",
            "secret_access_key": "<SECRET_ACCESS_KEY>"
          }
        }
      }'

Then update each pipeline that uses it:
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/pipelines/v1/pipelines/$PIPELINE_ID/update_tables" \
      --request POST \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

For more information, refer to [Update sink credentials](https://developers.cloudflare.com/basin-pipelines/sinks/manage-sinks/#update-sink-credentials) and [Update a pipeline](https://developers.cloudflare.com/basin-pipelines/pipelines/manage-pipelines/#update-a-pipeline).
