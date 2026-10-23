---
url: https://developers.cloudflare.com/ai-gateway/integrations/vercel-ai-sdk/
title: Vercel AI SDK \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-23T16:40:09.035095+00:00
---

# Vercel AI SDK · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/integrations/vercel-ai-sdk/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /Integrations
  4. /Vercel AI SDK



# Vercel AI SDK

Last updated Oct 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-gateway/integrations/vercel-ai-sdk/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInstallationCall a catalog modelCall a vendor's model objectFall back to another modelSet gateway optionsUse an account id and API tokenRelated resources

To call AI Gateway from the [AI SDK ↗︎](https://ai-sdk.dev/), use `createAI` from `agents/models/ai-sdk`. It calls models from the [model catalog](https://developers.cloudflare.com/ai/models/), [dynamic routes](https://developers.cloudflare.com/ai-gateway/features/dynamic-routing/), and a vendor's own AI SDK models through your gateway. This page covers the AI Gateway features. For the full reference, refer to [AI SDK](https://developers.cloudflare.com/agents/models/ai-sdk/).

The `ai-gateway-provider` package is deprecated. Use `createAI` instead.

## Installation

Install the Agents SDK and the AI SDK. `createAI` needs `ai@^7` and `@ai-sdk/provider@^4`:

npmyarnpnpmbun
    
    
    npm i agents ai @ai-sdk/provider
    
    
    yarn add agents ai @ai-sdk/provider
    
    
    pnpm add agents ai @ai-sdk/provider
    
    
    bun add agents ai @ai-sdk/provider

In a Worker, add the `AI` binding to your Wrangler configuration:
    
    
    {
    	"ai": {
    		"binding": "AI",
    	},
    }
    
    
    [ai]
    binding = "AI"

## Call a catalog model

Pass an `<author>/<model>` id from the [model catalog](https://developers.cloudflare.com/ai/models/). You do not need a vendor package or a vendor key. AI Gateway bills the request through [Unified Billing](https://developers.cloudflare.com/ai-gateway/features/unified-billing/), or uses a [key stored on the gateway](https://developers.cloudflare.com/ai-gateway/configuration/bring-your-own-keys/):
    
    
    import { createAI } from "agents/models/ai-sdk";
    import { streamText } from "ai";
    
    export default {
    	async fetch(request, env) {
    		const ai = createAI({ binding: env.AI, id: "my-gateway" });
    
    		const result = streamText({
    			model: ai("anthropic/claude-opus-5.5"),
    			messages: [{ role: "user", content: "Write a short story" }],
    		});
    
    		return result.toTextStreamResponse();
    	},
    };
    
    
    import { createAI } from "agents/models/ai-sdk";
    import { streamText } from "ai";
    
    export default {
    	async fetch(request: Request, env: Env) {
    		const ai = createAI({ binding: env.AI, id: "my-gateway" });
    
    		const result = streamText({
    			model: ai("anthropic/claude-opus-5.5"),
    			messages: [{ role: "user", content: "Write a short story" }],
    		});
    
    		return result.toTextStreamResponse();
    	},
    };

Use the catalog's spelling of the id, such as `anthropic/claude-opus-5.5` or `openai/gpt-5.5`. `id` sets the gateway and defaults to `default`. A [dynamic route](https://developers.cloudflare.com/ai-gateway/features/dynamic-routing/) on that gateway is `dynamic/<route>`, for example `ai("dynamic/support")`.

## Call a vendor's model object

Pass a model from the vendor's own AI SDK package. The request goes unchanged to the vendor's [provider-native endpoint](https://developers.cloudflare.com/ai-gateway/usage/providers/) on your gateway. AI Gateway holds the credential, so the vendor's `apiKey` is a placeholder:
    
    
    import { createAnthropic } from "@ai-sdk/anthropic";
    import { createAI } from "agents/models/ai-sdk";
    
    const ai = createAI({ binding: env.AI, id: "my-gateway" });
    const anthropic = createAnthropic({ apiKey: "cloudflare" });
    
    const model = ai(anthropic("claude-opus-5-5"));

Use the vendor's own model id here, such as `claude-opus-5-5`. To send a key you hold instead, refer to [Unified billing and BYOK](https://developers.cloudflare.com/agents/models/ai-sdk/#unified-billing-and-byok).

## Fall back to another model

`fallback` lists models to try in order if the primary model fails before it produces any output. Mix catalog ids, dynamic routes, Workers AI ids, and model objects:
    
    
    const model = ai(anthropic("claude-opus-5-5"), {
    	fallback: ["openai/gpt-5.5", "@cf/zai-org/glm-4.7-flash"],
    });

## Set gateway options

Set [caching](https://developers.cloudflare.com/ai-gateway/features/caching/), logging, metadata, timeouts, and retries on the provider, on a model, or per call under `providerOptions.cloudflare`:
    
    
    const ai = createAI({
    	binding: env.AI,
    	id: "my-gateway",
    	cacheTtl: 60,
    	metadata: { app: "support-bot" },
    });
    
    await generateText({
    	model: ai("openai/gpt-5.5"),
    	prompt: "Summarize this ticket",
    	providerOptions: {
    		cloudflare: { skipCache: true, metadata: { userId: "u_123" } },
    	},
    });

For every option, refer to [Set options](https://developers.cloudflare.com/agents/models/ai-sdk/#set-options).

## Use an account id and API token

To use a gateway in another account, or to call from outside a Worker, pass `accountId` and `apiToken` instead of `binding`:
    
    
    const ai = createAI({
    	accountId: "<ACCOUNT_ID>",
    	apiToken: env.CLOUDFLARE_API_TOKEN,
    	gateway: "my-gateway",
    });

The call forms and options are the same. [Create an API token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) with the **Workers AI Read** permission for model ids and **AI Gateway Run** for model objects.

## Related resources

  * [AI SDK provider reference](https://developers.cloudflare.com/agents/models/ai-sdk/)
  * [Model catalog](https://developers.cloudflare.com/ai/models/)
  * [Dynamic routing](https://developers.cloudflare.com/ai-gateway/features/dynamic-routing/)
  * [Unified Billing](https://developers.cloudflare.com/ai-gateway/features/unified-billing/)



[PreviousPi AI](https://developers.cloudflare.com/ai-gateway/integrations/pi-ai/)[NextAgents ↗︎](https://developers.cloudflare.com/agents/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/integrations/vercel-ai-sdk.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
