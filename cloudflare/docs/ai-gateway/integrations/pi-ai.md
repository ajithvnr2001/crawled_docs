---
url: https://developers.cloudflare.com/ai-gateway/integrations/pi-ai/
title: Pi AI \u00b7 Cloudflare AI Gateway docs
method: scrapling+scrapegraph
fetched_at: 2026-10-23T16:39:48.052722+00:00
---

# Pi AI · Cloudflare AI Gateway docs

> Source: https://developers.cloudflare.com/ai-gateway/integrations/pi-ai/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Gateway](https://developers.cloudflare.com/ai-gateway/)
  3. /Integrations
  4. /Pi AI



# Pi AI

Last updated Oct 22, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai-gateway/integrations/pi-ai/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInstallationCall a catalog modelCall a Pi AI model objectFall back to another modelSet gateway optionsUse an account id and API tokenRelated resources

To call AI Gateway from [Pi AI ↗︎](https://github.com/earendil-works/pi/tree/main/packages/ai), use `createAI` from `agents/models/pi-ai`. It calls models from the [model catalog](https://developers.cloudflare.com/ai/models/), [dynamic routes](https://developers.cloudflare.com/ai-gateway/features/dynamic-routing/), and Pi AI's own model objects through your gateway. This page covers the AI Gateway features. For the full reference, refer to [Pi AI](https://developers.cloudflare.com/agents/models/pi-ai/).

## Installation

Install the Agents SDK and Pi AI. `createAI` needs `@earendil-works/pi-ai@~1.4.0`:

npmyarnpnpmbun
    
    
    npm i agents @earendil-works/pi-ai
    
    
    yarn add agents @earendil-works/pi-ai
    
    
    pnpm add agents @earendil-works/pi-ai
    
    
    bun add agents @earendil-works/pi-ai

In a Worker, add the `AI` binding to your Wrangler configuration:
    
    
    {
    	"ai": {
    		"binding": "AI",
    	},
    }
    
    
    [ai]
    binding = "AI"

## Call a catalog model

Pass a `<provider>/<id>` from Pi AI's AI Gateway catalog. You do not need a vendor key. AI Gateway bills the request through [Unified Billing](https://developers.cloudflare.com/ai-gateway/features/unified-billing/), or uses a [key stored on the gateway](https://developers.cloudflare.com/ai-gateway/configuration/bring-your-own-keys/):
    
    
    import { createAI } from "agents/models/pi-ai";
    
    export default {
    	async fetch(request, env) {
    		const ai = createAI({ binding: env.AI, id: "my-gateway" });
    
    		const reply = await ai.complete(ai("anthropic/claude-opus-5.5"), {
    			messages: [
    				{ role: "user", content: "Write a short story", timestamp: Date.now() },
    			],
    		});
    
    		return Response.json(reply.content);
    	},
    };
    
    
    import { createAI } from "agents/models/pi-ai";
    
    export default {
    	async fetch(request: Request, env: Env) {
    		const ai = createAI({ binding: env.AI, id: "my-gateway" });
    
    		const reply = await ai.complete(ai("anthropic/claude-opus-5.5"), {
    			messages: [
    				{ role: "user", content: "Write a short story", timestamp: Date.now() },
    			],
    		});
    
    		return Response.json(reply.content);
    	},
    };

Use the catalog's spelling of the id, such as `anthropic/claude-opus-5.5` or `openai/gpt-5.5`. The request goes in the model's own format, Anthropic Messages or OpenAI Responses, so Pi AI's own parsers read the answer and thinking works as it does with the vendor. `id` sets the gateway and defaults to `default`. A dynamic route on that gateway is `dynamic/<route>`, for example `ai("dynamic/support")`.

## Call a Pi AI model object

Pass any model from a Pi AI registry. The request goes to the vendor's [provider-native endpoint](https://developers.cloudflare.com/ai-gateway/usage/providers/) on your gateway, and AI Gateway supplies the credential:
    
    
    import { getBuiltinModel } from "@earendil-works/pi-ai/providers/all";
    import { createAI } from "agents/models/pi-ai";
    
    const ai = createAI({ binding: env.AI, id: "my-gateway" });
    
    const model = ai(getBuiltinModel("anthropic", "claude-opus-5-5"));

A model object keeps the vendor's own id, such as `claude-opus-5-5`, and all of Pi AI's metadata for it.

## Fall back to another model

`fallback` lists models to try in order if the primary model fails before it produces any output. Mix catalog ids, dynamic routes, Workers AI ids, and model objects:
    
    
    const model = ai("anthropic/claude-opus-5.5", {
    	fallback: ["openai/gpt-5.5", "@cf/zai-org/glm-4.7-flash"],
    });

## Set gateway options

Set [caching](https://developers.cloudflare.com/ai-gateway/features/caching/), logging, metadata, timeouts, and retries on `createAI`, on a model, or per call:
    
    
    const ai = createAI({
    	binding: env.AI,
    	id: "my-gateway",
    	cacheTtl: 60,
    	metadata: { app: "support-bot" },
    });
    
    const model = ai("openai/gpt-5.5", { byokAlias: "production" });

For every option, refer to [Cache, tag, and time out requests](https://developers.cloudflare.com/agents/models/pi-ai/#cache-tag-and-time-out-requests).

## Use an account id and API token

To use a gateway in another account, or to call from outside a Worker, pass `accountId` and `apiToken` instead of `binding`:
    
    
    const ai = createAI({
    	accountId: "<ACCOUNT_ID>",
    	apiToken: env.CLOUDFLARE_API_TOKEN,
    	gateway: "my-gateway",
    });

[Create an API token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) with the **Workers AI Read** permission for model ids and **AI Gateway Run** for model objects.

## Related resources

  * [Pi AI provider reference](https://developers.cloudflare.com/agents/models/pi-ai/)
  * [Pi harness](https://developers.cloudflare.com/agents/harnesses/pi/)
  * [Model catalog](https://developers.cloudflare.com/ai/models/)
  * [Vercel AI SDK](https://developers.cloudflare.com/ai-gateway/integrations/vercel-ai-sdk/)



[PreviousOpenTelemetry](https://developers.cloudflare.com/ai-gateway/observability/otel-integration/)[NextVercel AI SDK](https://developers.cloudflare.com/ai-gateway/integrations/vercel-ai-sdk/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-gateway/integrations/pi-ai.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
