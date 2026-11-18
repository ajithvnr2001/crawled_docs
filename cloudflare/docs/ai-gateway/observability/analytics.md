---
url: https://developers.cloudflare.com/ai-gateway/observability/analytics/
title: Analytics \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-11-18T09:55:29.189514+00:00
---

# Analytics · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/observability/analytics/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /Observability
  4. /Analytics



# Analytics

Last updated Nov 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewView analyticsGroup by a custom metadata key

Your AI Gateway dashboard shows metrics on requests, tokens, caching, errors, and cost. You can filter these metrics by time, provider, model, cost, token counts, and a custom metadata key or value. To break metrics down by the values of one metadata key, such as a team or user ID, use GraphQL. These analytics help you understand traffic patterns, token consumption, and potential issues across AI providers. You can view the following analytics:

  * **Requests** : Track the total number of requests processed by AI Gateway.
  * **Token Usage** : Analyze token consumption across requests, giving insight into usage patterns.
  * **Costs** : Gain visibility into the costs associated with using different AI providers, allowing you to track spending, manage budgets, and optimize resources.
  * **Errors** : Monitor the number of errors across the gateway, helping to identify and troubleshoot issues.
  * **Cached Responses** : View the percentage of responses served from cache, which can help reduce costs and improve speed.



## View analytics

To view analytics in the dashboard:

  1. Log into the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com) and select your account.
  2. Go to **AI** > **AI Gateway**.
  3. Make sure you have your gateway selected.



You can use GraphQL to query your usage data outside of the AI Gateway dashboard. To run this request, save a [Cloudflare API token](https://developers.cloudflare.com/analytics/graphql-api/getting-started/authentication/api-token-auth/) with the Account Analytics Read permission in the `CLOUDFLARE_API_TOKEN` environment variable, and replace `<ACCOUNT_ID>` with your account ID. Set `start` and `end` to a range of up to 32 days within the last 62 days.

Requestbash
    
    
    curl https://api.cloudflare.com/client/v4/graphql \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
        "query": "query ($accountTag: string!, $limit: uint64!, $start: Time!, $end: Time!) { viewer { accounts(filter: { accountTag: $accountTag }) { requests: aiGatewayRequestsAdaptiveGroups(limit: $limit, filter: { datetimeHour_geq: $start, datetimeHour_leq: $end }, orderBy: [datetimeMinute_ASC]) { count dimensions { model provider gateway ts: datetimeMinute } } } } }",
        "variables": {
          "accountTag": "<ACCOUNT_ID>",
          "limit": 1000,
          "start": "2026-10-01T00:00:00Z",
          "end": "2026-10-07T00:00:00Z"
        }
      }'

## Group by a custom metadata key

To see requests and cost for each value of one [custom metadata](https://developers.cloudflare.com/ai-gateway/observability/custom-metadata/) key, such as a team or user ID, query the GraphQL Analytics API and add `metadataValue(key: "<key>")` to `dimensions`. This example groups by a `team` key across every gateway and provider in the account, and returns up to 1,000 values ordered by cost. To use another key, change the `key` argument; keys can be up to 128 characters of letters, digits, and `_ . $ : / -`. To narrow the results, add `gateway: "<GATEWAY_NAME>"` or `provider: "workers-ai"` to the filter.

Save an [API token](https://developers.cloudflare.com/analytics/graphql-api/getting-started/authentication/api-token-auth/) with the Account Analytics Read permission in `CLOUDFLARE_API_TOKEN`, replace `<ACCOUNT_ID>`, and set `start` and `end` to a range of up to 32 days within the last 62 days.

Requestbash
    
    
    curl https://api.cloudflare.com/client/v4/graphql \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
        "query": "query ($accountTag: string!, $start: Time!, $end: Time!) { viewer { accounts(filter: { accountTag: $accountTag }) { aiGatewayRequestsAdaptiveGroups(limit: 1000, filter: { datetime_geq: $start, datetime_leq: $end }, orderBy: [sum_cost_DESC]) { count sum { cost } dimensions { team: metadataValue(key: \"team\") } } } } }",
        "variables": {
          "accountTag": "<ACCOUNT_ID>",
          "start": "2026-10-01T00:00:00Z",
          "end": "2026-10-07T00:00:00Z"
        }
      }'

Requests without the key are grouped under an empty value. Request counts and cost are calculated from sampled data, and cost is itself an [estimate](https://developers.cloudflare.com/ai-gateway/observability/costs/) based on tokens.

[PreviousLogpush](https://developers.cloudflare.com/ai-gateway/observability/logging/logpush/)[NextCosts](https://developers.cloudflare.com/ai-gateway/observability/costs/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/observability/analytics.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
