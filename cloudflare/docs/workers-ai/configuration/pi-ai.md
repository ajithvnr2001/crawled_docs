---
url: https://developers.cloudflare.com/workers-ai/configuration/pi-ai/
title: Pi AI \u00b7 Cloudflare Workers AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-23T16:39:49.789759+00:00
---

# Pi AI · Cloudflare Workers AI docs

> Source: https://developers.cloudflare.com/workers-ai/configuration/pi-ai/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers AI](https://developers.cloudflare.com/workers-ai/)
  3. /Configuration
  4. /Pi AI



# Pi AI

Last updated Oct 22, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers-ai/configuration/pi-ai/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSetupGenerate textStream textSet model detailsGenerate imagesUse AI GatewayRelated resources

To use Workers AI with [Pi AI ↗︎](https://github.com/earendil-works/pi/tree/main/packages/ai), use `createAI` from `agents/models/pi-ai`. It returns Pi AI `Model` objects, so Workers AI models work with Pi AI's `stream` and `complete`, with [Pi Durable ↗︎](https://github.com/earendil-works/pi/tree/main/packages/durable), and with the [Pi harness](https://developers.cloudflare.com/agents/harnesses/pi/). This page covers Workers AI models. For AI Gateway catalog models, fallback, gateway options, and the full reference, refer to [Pi AI](https://developers.cloudflare.com/agents/models/pi-ai/).

## Setup

Install the Agents SDK and Pi AI. `createAI` needs `@earendil-works/pi-ai@~1.4.0`:

npmyarnpnpmbun
    
    
    npm i agents @earendil-works/pi-ai
    
    
    yarn add agents @earendil-works/pi-ai
    
    
    pnpm add agents @earendil-works/pi-ai
    
    
    bun add agents @earendil-works/pi-ai

Add the `AI` binding to your Wrangler configuration:
    
    
    {
    	"ai": {
    		"binding": "AI",
    	},
    }
    
    
    [ai]
    binding = "AI"

## Generate text

Name a Workers AI model by its `@cf/` id. The provider carries Pi AI's entry points, so nothing is registered globally:
    
    
    import { createAI } from "agents/models/pi-ai";
    
    export default {
    	async fetch(request, env) {
    		const ai = createAI({ binding: env.AI });
    
    		const reply = await ai.complete(ai("@cf/zai-org/glm-4.7-flash"), {
    			messages: [
    				{ role: "user", content: "What is Cloudflare?", timestamp: Date.now() },
    			],
    		});
    
    		// `content` holds text, thinking, and tool call parts.
    		const text = reply.content
    			.filter((part) => part.type === "text")
    			.map((part) => part.text)
    			.join("");
    
    		return Response.json({ text });
    	},
    };
    
    
    import { createAI } from "agents/models/pi-ai";
    
    export default {
    	async fetch(request: Request, env: Env) {
    		const ai = createAI({ binding: env.AI });
    
    		const reply = await ai.complete(ai("@cf/zai-org/glm-4.7-flash"), {
    			messages: [
    				{ role: "user", content: "What is Cloudflare?", timestamp: Date.now() },
    			],
    		});
    
    		// `content` holds text, thinking, and tool call parts.
    		const text = reply.content
    			.filter((part) => part.type === "text")
    			.map((part) => part.text)
    			.join("");
    
    		return Response.json({ text });
    	},
    };

## Stream text

`ai.stream()` returns Pi AI's event stream. `ai.streamSimple()` and `ai.completeSimple()` take Pi AI's simple options, such as a `reasoning` level and `maxTokens`:
    
    
    const model = ai("@cf/zai-org/glm-4.7-flash");
    const context = {
    	messages: [{ role: "user", content: "Hi", timestamp: Date.now() }],
    };
    
    for await (const event of ai.stream(model, context)) {
    	// text_delta, thinking_delta, toolcall_*, done, error
    }

A compatibility layer turns each Workers AI model's response into the shape Pi AI's parsers read, so tool calls and reasoning work the same across model families.

## Set model details

A Workers AI id that Pi AI does not list resolves with a 128,000 token context window, 8,192 output tokens, and zero cost. Pass the real values when you know them:
    
    
    const model = ai("@cf/zai-org/glm-4.7-flash", {
    	contextWindow: 131_072,
    	maxTokens: 16_384,
    });

## Generate images
    
    
    const images = ai.images("@cf/black-forest-labs/flux-1-schnell", { steps: 8 });
    const result = await ai.generateImages(images, {
    	input: [{ type: "text", text: "A red bicycle" }],
    });

## Use AI Gateway

Every request goes through AI Gateway. Set the gateway with `id`, which defaults to `default`:
    
    
    const ai = createAI({ binding: env.AI, id: "my-gateway" });

To call from outside a Worker, pass `accountId` and `apiToken` instead of `binding`. For gateway options, catalog models, and fallback, refer to [Pi AI](https://developers.cloudflare.com/agents/models/pi-ai/).

## Related resources

  * [Pi AI provider reference](https://developers.cloudflare.com/agents/models/pi-ai/)
  * [Pi harness](https://developers.cloudflare.com/agents/harnesses/pi/)
  * [Workers AI models](https://developers.cloudflare.com/workers-ai/models/)
  * [Vercel AI SDK](https://developers.cloudflare.com/workers-ai/configuration/ai-sdk/)



[PreviousOpenAI compatible API endpoints](https://developers.cloudflare.com/workers-ai/configuration/open-ai-compatibility/)[NextVercel AI SDK](https://developers.cloudflare.com/workers-ai/configuration/ai-sdk/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers-ai/configuration/pi-ai.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
