---
url: https://developers.cloudflare.com/ai-search/configuration/retrieval/public-endpoint/namespace/
title: Namespace public endpoints \u00b7 Cloudflare AI Search docs
method: scrapling+scrapegraph
fetched_at: 2026-11-14T08:45:57.525465+00:00
---

# Namespace public endpoints · Cloudflare AI Search docs

> Source: https://developers.cloudflare.com/ai-search/configuration/retrieval/public-endpoint/namespace/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Search](https://developers.cloudflare.com/ai-search/)
  3. /…

[Configuration](https://developers.cloudflare.com/ai-search/configuration/)Retrieval

  4. /[Public endpoint settings](https://developers.cloudflare.com/ai-search/configuration/retrieval/public-endpoint/)
  5. /Namespace public endpoints



# Namespace public endpoints

Last updated Nov 13, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEnable a namespace public endpointThe instances allowlistSearch the allowlistDisable a namespace public endpointErrorsNext steps

A [namespace](https://developers.cloudflare.com/ai-search/concepts/namespaces/) can expose its own public endpoint. A single URL then searches across several instances in that namespace and merges the results. Use one when a single search experience covers content that lives in several instances, such as documentation, a blog, and a support portal.

A namespace endpoint serves the same paths and takes the same settings as an instance endpoint, including [custom domains](https://developers.cloudflare.com/ai-search/configuration/retrieval/public-endpoint/custom-domains/) and [Cloudflare Access](https://developers.cloudflare.com/ai-search/configuration/retrieval/public-endpoint/cloudflare-access/). Refer to [Public endpoint settings](https://developers.cloudflare.com/ai-search/configuration/retrieval/public-endpoint/). This page covers what is specific to namespaces.

## Enable a namespace public endpoint

Set `public_endpoint_params` on the namespace and list the instances to expose in `instances_allowed`.
    
    
    curl -X PUT "https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/ai-search/namespaces/<NAMESPACE>" \
      -H "Authorization: Bearer <API_TOKEN>" \
      -H "Content-Type: application/json" \
      -d '{
        "public_endpoint_params": {
          "enabled": true,
          "instances_allowed": ["docs", "blog", "support"]
        }
      }'

The response returns the generated `public_endpoint_id`. A namespace hostname is prefixed with `ns-`:
    
    
    https://ns-<NAMESPACE_ENDPOINT_ID>.search.ai.cloudflare.com/search

Enabling a namespace endpoint does not change the instance endpoints inside it. Each is enabled and disabled separately.

## The instances allowlist

`instances_allowed` controls which instances the endpoint can reach.

  * Every entry must be an existing instance in that namespace. An unknown entry returns error `7097`.
  * The list holds up to 10 instances.
  * An empty list means nothing is searchable. This is the state a namespace starts in when you first enable the endpoint.
  * Deleting an instance, or moving it to another namespace, removes it from the allowlist.



While the allowlist is empty, every request returns a `404` with error `60013`.

Caution

`public_endpoint_params` is replaced in full on every update. Send the complete object, including `instances_allowed`, or omitted fields revert to their defaults. Omitting `instances_allowed` resets it to an empty list and makes the endpoint return `404` for every request.

## Search the allowlist

Every request searches all instances in the allowlist and merges the results. You cannot narrow a request to a subset of instances. If the request body includes `ai_search_options.instance_ids`, the endpoint replaces it with the full allowlist.
    
    
    curl https://ns-<NAMESPACE_ENDPOINT_ID>.search.ai.cloudflare.com/search \
      --header "Content-Type: application/json" \
      --data '{
        "messages": [
          {
            "content": "How do I configure AI Search?",
            "role": "user"
          }
        ]
      }'

To search a different set of instances, update `instances_allowed`, or query the instances from a [Workers binding or the REST API](https://developers.cloudflare.com/ai-search/how-to/search-multiple-sources/).

Note

The request body must be a JSON object. An array or a string returns a `400` with error `60015`. An empty body is treated as an empty JSON object.

## Disable a namespace public endpoint

Set `public_endpoint_params` to `null`. This clears the configuration and stops serving traffic, but keeps the identifier so the URL is reused if you enable the endpoint again.
    
    
    curl -X PUT "https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/ai-search/namespaces/<NAMESPACE>" \
      -H "Authorization: Bearer <API_TOKEN>" \
      -H "Content-Type: application/json" \
      -d '{
        "public_endpoint_params": null
      }'

## Errors

Code | Message | HTTP status | Cause  
---|---|---|---  
`7097` | `instances_allowed_contains_unknown_instances` | 400 | An entry in `instances_allowed` is not an instance in this namespace.  
`7099` | `namespace_modified_concurrently_please_retry` | 409 | Another update changed the namespace at the same time. Retry.  
`60013` | `ai_search_not_found` | 404 | The allowlist is empty, so no instance is searchable.  
`60014` | `path not supported for namespace-kind hash` | 404 | The path is not `/search`, `/chat/completions`, or `/mcp`.  
`60015` | `request body must be a JSON object` | 400 | The request body is not a JSON object.  
  
## Next steps

### [Namespaces](https://developers.cloudflare.com/ai-search/concepts/namespaces/)

Group instances into namespaces and manage them from a Workers binding.

### [Search across multiple instances](https://developers.cloudflare.com/ai-search/how-to/search-multiple-sources/)

Query several instances from a Worker or the REST API.

### [Custom domains](https://developers.cloudflare.com/ai-search/configuration/retrieval/public-endpoint/custom-domains/)

Serve a namespace public endpoint from a hostname that you own.

[PreviousOverview](https://developers.cloudflare.com/ai-search/configuration/retrieval/public-endpoint/)[NextCustom domains](https://developers.cloudflare.com/ai-search/configuration/retrieval/public-endpoint/custom-domains/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-search/configuration/retrieval/public-endpoint/namespace.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
