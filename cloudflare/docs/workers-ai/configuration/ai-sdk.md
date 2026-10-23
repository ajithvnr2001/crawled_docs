---
url: https://developers.cloudflare.com/workers-ai/configuration/ai-sdk/
title: Vercel AI SDK \u00b7 Cloudflare Workers AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-23T16:40:08.549407+00:00
---

# Vercel AI SDK · Cloudflare Workers AI docs

> Source: https://developers.cloudflare.com/workers-ai/configuration/ai-sdk/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers AI](https://developers.cloudflare.com/workers-ai/)
  3. /Configuration
  4. /Vercel AI SDK



# Vercel AI SDK

Last updated Oct 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers-ai/configuration/ai-sdk/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSetupChoose a modelGenerate textStream textGenerate structured outputUse other model typesUse AI GatewayRelated resources

To use Workers AI with the [AI SDK ↗︎](https://ai-sdk.dev/), use `createAI` from `agents/models/ai-sdk`. This page covers Workers AI models. For AI Gateway catalog models, fallback, gateway options, and the full option reference, refer to [AI SDK](https://developers.cloudflare.com/agents/models/ai-sdk/).

The `workers-ai-provider` package is deprecated. Use `createAI` instead.

## Setup

Install the Agents SDK and the AI SDK. `createAI` needs `ai@^7` and `@ai-sdk/provider@^4`:

npmyarnpnpmbun
    
    
    npm i agents ai @ai-sdk/provider
    
    
    yarn add agents ai @ai-sdk/provider
    
    
    pnpm add agents ai @ai-sdk/provider
    
    
    bun add agents ai @ai-sdk/provider

Add the `AI` binding to your Wrangler configuration:
    
    
    {
    	"ai": {
    		"binding": "AI",
    	},
    }
    
    
    [ai]
    binding = "AI"

## Choose a model

Pass the id of any [Workers AI model](https://developers.cloudflare.com/workers-ai/models/). Model ids start with `@cf/` and autocomplete from `@cloudflare/workers-types`:
    
    
    import { createAI } from "agents/models/ai-sdk";
    
    const ai = createAI({ binding: env.AI });
    
    const model = ai("@cf/zai-org/glm-4.7-flash");

## Generate text
    
    
    import { createAI } from "agents/models/ai-sdk";
    import { generateText } from "ai";
    
    export default {
    	async fetch(request, env) {
    		const ai = createAI({ binding: env.AI });
    
    		const { text } = await generateText({
    			model: ai("@cf/zai-org/glm-4.7-flash"),
    			prompt: "Write a 50-word essay about hello world.",
    		});
    
    		return new Response(text);
    	},
    };
    
    
    import { createAI } from "agents/models/ai-sdk";
    import { generateText } from "ai";
    
    export default {
    	async fetch(request: Request, env: Env) {
    		const ai = createAI({ binding: env.AI });
    
    		const { text } = await generateText({
    			model: ai("@cf/zai-org/glm-4.7-flash"),
    			prompt: "Write a 50-word essay about hello world.",
    		});
    
    		return new Response(text);
    	},
    };

## Stream text

For longer responses, stream the output as the model generates it:
    
    
    import { createAI } from "agents/models/ai-sdk";
    import { streamText } from "ai";
    
    export default {
    	async fetch(request, env) {
    		const ai = createAI({ binding: env.AI });
    
    		const result = streamText({
    			model: ai("@cf/zai-org/glm-4.7-flash"),
    			prompt: "Write a 50-word essay about hello world.",
    		});
    
    		return result.toTextStreamResponse();
    	},
    };
    
    
    import { createAI } from "agents/models/ai-sdk";
    import { streamText } from "ai";
    
    export default {
    	async fetch(request: Request, env: Env) {
    		const ai = createAI({ binding: env.AI });
    
    		const result = streamText({
    			model: ai("@cf/zai-org/glm-4.7-flash"),
    			prompt: "Write a 50-word essay about hello world.",
    		});
    
    		return result.toTextStreamResponse();
    	},
    };

## Generate structured output

Pass a Zod schema to get a typed JSON response:
    
    
    import { createAI } from "agents/models/ai-sdk";
    import { generateText, Output } from "ai";
    import { z } from "zod";
    
    export default {
    	async fetch(request, env) {
    		const ai = createAI({ binding: env.AI });
    
    		const { output } = await generateText({
    			model: ai("@cf/zai-org/glm-4.7-flash"),
    			prompt: "Generate a lasagna recipe.",
    			output: Output.object({
    				schema: z.object({
    					recipe: z.object({
    						ingredients: z.array(z.string()),
    						description: z.string(),
    					}),
    				}),
    			}),
    		});
    
    		return Response.json(output);
    	},
    };
    
    
    import { createAI } from "agents/models/ai-sdk";
    import { generateText, Output } from "ai";
    import { z } from "zod";
    
    export default {
    	async fetch(request: Request, env: Env) {
    		const ai = createAI({ binding: env.AI });
    
    		const { output } = await generateText({
    			model: ai("@cf/zai-org/glm-4.7-flash"),
    			prompt: "Generate a lasagna recipe.",
    			output: Output.object({
    				schema: z.object({
    					recipe: z.object({
    						ingredients: z.array(z.string()),
    						description: z.string(),
    					}),
    				}),
    			}),
    		});
    
    		return Response.json(output);
    	},
    };

## Use other model types

Embeddings, images, speech, transcription, and reranking come from the same provider:
    
    
    import {
    	embedMany,
    	generateImage,
    	generateSpeech,
    	rerank,
    	transcribe,
    } from "ai";
    
    const { embeddings } = await embedMany({
    	model: ai.embedding("@cf/baai/bge-base-en-v1.5"),
    	values: ["hello", "world"],
    });
    
    const { image } = await generateImage({
    	model: ai.image("@cf/black-forest-labs/flux-1-schnell"),
    	prompt: "A cyberpunk lizard",
    });
    
    const { audio } = await generateSpeech({
    	model: ai.speech("@cf/deepgram/aura-1"),
    	text: "Hello from Cloudflare.",
    });
    
    const { text } = await transcribe({
    	model: ai.transcription("@cf/openai/whisper-large-v3-turbo"),
    	audio: audio.uint8Array,
    });
    
    const { rerankedDocuments } = await rerank({
    	model: ai.reranking("@cf/baai/bge-reranker-base"),
    	documents: ["a cyberpunk lizard", "a rainy Tuesday"],
    	query: "Which one is cooler?",
    });

For model-specific settings, refer to [Use other modalities](https://developers.cloudflare.com/agents/models/ai-sdk/#use-other-modalities).

## Use AI Gateway

Requests go through [AI Gateway](https://developers.cloudflare.com/ai-gateway/). The gateway defaults to `default`. To use another gateway, set its `id`:
    
    
    const ai = createAI({ binding: env.AI, id: "my-gateway" });

The same provider also calls models from the [AI Gateway catalog](https://developers.cloudflare.com/ai/models/), such as `anthropic/claude-opus-5.5`. Refer to [AI SDK](https://developers.cloudflare.com/agents/models/ai-sdk/) for catalog models, caching, fallback, and the other gateway options.

## Related resources

  * [AI SDK provider reference](https://developers.cloudflare.com/agents/models/ai-sdk/)
  * [Workers AI models](https://developers.cloudflare.com/workers-ai/models/)
  * [AI SDK documentation ↗︎](https://ai-sdk.dev/docs/introduction)



[PreviousPi AI](https://developers.cloudflare.com/workers-ai/configuration/pi-ai/)[NextHugging Face Chat UI](https://developers.cloudflare.com/workers-ai/configuration/hugging-face-chat-ui/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers-ai/configuration/ai-sdk.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
