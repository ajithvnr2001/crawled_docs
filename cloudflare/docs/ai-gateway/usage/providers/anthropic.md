---
url: https://developers.cloudflare.com/ai-gateway/usage/providers/anthropic/
title: Anthropic \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-27T07:31:30.797939+00:00
---

# Anthropic · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/usage/providers/anthropic/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /…

Using AI Gateway

  4. /Provider Native
  5. /Anthropic



# Anthropic

Last updated Oct 27, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEndpointExamples cURL Anthropic SDKOpenAI-Compatible Endpoint

[Anthropic ↗︎](https://www.anthropic.com/) helps build reliable, interpretable, and steerable AI systems.

## Endpoint

**Base URL**
    
    
    https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/anthropic

When supplying a provider key to `/anthropic/v1/messages`, send it in `x-api-key`. AI Gateway does not recognize `Authorization: Bearer` as provider credentials on this endpoint. Authenticate to AI Gateway separately with `cf-aig-authorization`.

For stored keys and Unified Billing, refer to [credential precedence](https://developers.cloudflare.com/ai-gateway/features/unified-billing/#credential-precedence). If provider credentials are required but AI Gateway cannot find them, refer to [error `2044`](https://developers.cloudflare.com/ai-gateway/reference/troubleshooting/#400-provider-credentials-required-2044).

## Examples

### cURL

With API Key in Request
    
    
    curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/anthropic/v1/messages \
     --header 'x-api-key: {anthropic_api_key}' \
     --header 'cf-aig-authorization: Bearer {CF_AIG_TOKEN}' \
     --header 'anthropic-version: 2023-06-01' \
     --header 'Content-Type: application/json' \
     --data  '{
        "model": "claude-sonnet-4-5",
        "max_tokens": 1024,
        "messages": [
          {"role": "user", "content": "What is Cloudflare?"}
        ]
      }'
    
    
    curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/anthropic/v1/messages \
     --header 'x-api-key: {anthropic_api_key}' \
     --header 'anthropic-version: 2023-06-01' \
     --header 'Content-Type: application/json' \
     --data  '{
        "model": "claude-sonnet-4-5",
        "max_tokens": 1024,
        "messages": [
          {"role": "user", "content": "What is Cloudflare?"}
        ]
      }'

With Stored Keys (BYOK) / Unified Billing
    
    
    curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/anthropic/v1/messages \
     --header 'cf-aig-authorization: Bearer {CF_AIG_TOKEN}' \
     --header 'anthropic-version: 2023-06-01' \
     --header 'Content-Type: application/json' \
     --data  '{
        "model": "claude-sonnet-4-5",
        "max_tokens": 1024,
        "messages": [
          {"role": "user", "content": "What is Cloudflare?"}
        ]
      }'

### Anthropic SDK

Set `x-api-key` explicitly when supplying your Anthropic key. SDK authentication headers can differ between versions. Setting `Authorization` to `null` removes the SDK-generated bearer header. Use `cf-aig-authorization` separately to authenticate to AI Gateway.

With Key in Request
    
    
    import Anthropic from "@anthropic-ai/sdk";
    
    const baseURL = `https://gateway.ai.cloudflare.com/v1/{accountId}/{gatewayId}/anthropic`;
    const providerKey = "{ANTHROPIC_API_KEY}";
    
    const anthropic = new Anthropic({
    	apiKey: providerKey,
    	baseURL,
    	defaultHeaders: {
    		"x-api-key": providerKey,
    		"cf-aig-authorization": "Bearer {CF_AIG_TOKEN}",
    		Authorization: null,
    	},
    });
    
    const message = await anthropic.messages.create({
    	model: "claude-sonnet-4-5",
    	messages: [{ role: "user", content: "What is Cloudflare?" }],
    	max_tokens: 1024,
    });
    
    
    import Anthropic from "@anthropic-ai/sdk";
    
    const baseURL = `https://gateway.ai.cloudflare.com/v1/{accountId}/{gatewayId}/anthropic`;
    const providerKey = "{ANTHROPIC_API_KEY}";
    
    const anthropic = new Anthropic({
    	apiKey: providerKey,
    	baseURL,
    	defaultHeaders: {
    		"x-api-key": providerKey,
    		Authorization: null,
    	},
    });
    
    const message = await anthropic.messages.create({
    	model: "claude-sonnet-4-5",
    	messages: [{ role: "user", content: "What is Cloudflare?" }],
    	max_tokens: 1024,
    });

With Stored Keys (BYOK) / Unified Billing
    
    
    import Anthropic from "@anthropic-ai/sdk";
    
    const baseURL = `https://gateway.ai.cloudflare.com/v1/{accountId}/{gatewayId}/anthropic`;
    
    const anthropic = new Anthropic({
    	apiKey: "placeholder",
    	baseURL,
    	defaultHeaders: {
    		"cf-aig-authorization": "Bearer {CF_AIG_TOKEN}",
    		"x-api-key": null,
    		Authorization: null,
    	},
    });
    
    const message = await anthropic.messages.create({
    	model: "claude-sonnet-4-5",
    	messages: [{ role: "user", content: "What is Cloudflare?" }],
    	max_tokens: 1024,
    });

Note

The placeholder satisfies the SDK's credential configuration. The `null` headers remove SDK-generated provider credentials before sending the request. AI Gateway uses an applicable stored BYOK key, or falls back to Unified Billing when allowed. If **Require provider credentials** is on and no applicable stored key exists, the request returns [error `2044`](https://developers.cloudflare.com/ai-gateway/reference/troubleshooting/#400-provider-credentials-required-2044).

Supplying a real key in `x-api-key` instead selects request-key authentication. This bypasses stored keys and Unified Billing.

## OpenAI-Compatible Endpoint

You can also access Anthropic models using the OpenAI API schema through the [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/). Send your requests to:
    
    
    https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1/chat/completions

Specify:
    
    
    {
    	"model": "anthropic/{model}"
    }

[PreviousAmazon Bedrock](https://developers.cloudflare.com/ai-gateway/usage/providers/bedrock/)[NextAzure OpenAI](https://developers.cloudflare.com/ai-gateway/usage/providers/azureopenai/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/usage/providers/anthropic.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
