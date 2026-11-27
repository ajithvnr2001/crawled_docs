---
url: https://developers.cloudflare.com/basin-pipelines/sinks/manage-sinks/
title: Manage sinks \u00b7 Cloudflare Basin Pipelines Docs
method: scrapling+scrapegraph
fetched_at: 2026-11-27T10:39:59.924882+00:00
---

# Manage sinks · Cloudflare Basin Pipelines Docs

> Source: https://developers.cloudflare.com/basin-pipelines/sinks/manage-sinks/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/)
  3. /[Sinks](https://developers.cloudflare.com/basin-pipelines/sinks/)
  4. /Manage sinks



# Manage sinks

Last updated Nov 26, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCreate a sink Dashboard Wrangler CLIView sink configuration Dashboard Wrangler CLIUpdate sink credentials Dashboard APIDelete a sink Dashboard Wrangler CLILimitations

Learn how to:

  * Create and configure sinks for data storage
  * View sink configuration
  * Update sink credentials
  * Delete sinks when no longer needed



## Create a sink

Sinks are made available to pipelines as SQL tables using the sink name (for example, `INSERT INTO my_sink SELECT * FROM my_stream`).

### Dashboard

  1. In the Cloudflare dashboard, go to the **Basin Pipelines** page.

[ Go to **Pipelines** ↗ ](https://dash.cloudflare.com/?to=/:account/pipelines/overview)
  2. Select **Create Pipeline** to launch the pipeline creation wizard.

  3. Complete the wizard to create your sink along with the associated stream and pipeline.




### Wrangler CLI

To create a sink, run the `basin pipelines sinks create` command:

npmyarnpnpm
    
    
    npx wrangler basin pipelines sinks create <SINK_NAME> --type r2 --bucket my-bucket
    
    
    yarn wrangler basin pipelines sinks create <SINK_NAME> --type r2 --bucket my-bucket
    
    
    pnpm wrangler basin pipelines sinks create <SINK_NAME> --type r2 --bucket my-bucket

For sink-specific configuration options, refer to [Available sinks](https://developers.cloudflare.com/basin-pipelines/sinks/available-sinks/).

Alternatively, to use the interactive setup wizard that helps you configure a stream, sink, and pipeline, run the `basin pipelines setup` command:

npmyarnpnpm
    
    
    npx wrangler basin pipelines setup
    
    
    yarn wrangler basin pipelines setup
    
    
    pnpm wrangler basin pipelines setup

## View sink configuration

### Dashboard

  1. In the Cloudflare dashboard, go to **Basin Pipelines** > **Sinks**.

  2. Select a sink to view its configuration.




### Wrangler CLI

To view a specific sink, run the `basin pipelines sinks get` command with either the sink ID or sink name:

npmyarnpnpm
    
    
    npx wrangler basin pipelines sinks get <SINK_NAME_OR_ID>
    
    
    yarn wrangler basin pipelines sinks get <SINK_NAME_OR_ID>
    
    
    pnpm wrangler basin pipelines sinks get <SINK_NAME_OR_ID>

To list all sinks in your account, run the `basin pipelines sinks list` command:

npmyarnpnpm
    
    
    npx wrangler basin pipelines sinks list
    
    
    yarn wrangler basin pipelines sinks list
    
    
    pnpm wrangler basin pipelines sinks list

## Update sink credentials

Replace a sink's credentials when its token expires or is revoked. Pipelines that use the sink keep its earlier credentials until you [update them](https://developers.cloudflare.com/basin-pipelines/pipelines/manage-pipelines/#update-a-pipeline).

### Dashboard

  1. In the Cloudflare dashboard, go to **Basin Pipelines** > **Sinks**.

[ Go to **Sinks** ↗ ](https://dash.cloudflare.com/?to=/:account/pipelines/sinks)
  2. Select the sink.

  3. In **Destination** , select **Update credentials**.

  4. Select **Create a new API token** , or select **Enter credentials** and enter the credentials of a token you created.

  5. Select **Update credentials**.




### API

The [API token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) for this request must have **Basin Pipelines Edit** permission.

For a Basin Catalog sink, send `token` instead of `credentials`.
    
    
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

## Delete a sink

### Dashboard

  1. In the Cloudflare dashboard, go to **Basin Pipelines** > **Sinks**.

  2. Select the sink you want to delete.

  3. On the sink's page, select **Delete**.




### Wrangler CLI

To delete a sink, run the `basin pipelines sinks delete` command:

npmyarnpnpm
    
    
    npx wrangler basin pipelines sinks delete <SINK_ID>
    
    
    yarn wrangler basin pipelines sinks delete <SINK_ID>
    
    
    pnpm wrangler basin pipelines sinks delete <SINK_ID>

Caution

Deleting a sink stops all data writes to that destination.

## Limitations

  * Only a sink's credentials and, with the API, its rolling policy can be changed after creation. To change anything else, you must delete and recreate the sink.
  * The Basin Catalog Sink does not currently support writing to R2 buckets into a different jurisdiction.



[PreviousOverview](https://developers.cloudflare.com/basin-pipelines/sinks/)[NextR2](https://developers.cloudflare.com/basin-pipelines/sinks/available-sinks/r2/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/basin-pipelines/sinks/manage-sinks.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
