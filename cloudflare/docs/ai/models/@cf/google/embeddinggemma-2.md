---
url: https://developers.cloudflare.com/ai/models/%40cf/google/embeddinggemma-2/
title: embeddinggemma-2 (Google) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-11-13T09:17:04.650424+00:00
---

# embeddinggemma-2 (Google) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/%40cf/google/embeddinggemma-2/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Google logo](https://developers.cloudflare.com/_astro/google.DyXKPTPP.svg)

# embeddinggemma-2

Multimodal Embeddings • Google

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Model ID

`@cf/google/embeddinggemma-2`Copy

  * Cloudflare-hosted
  * Zero data retention



EmbeddingGemma 2 is an open multimodal embedding model built by Google DeepMind which maps text (incl. code), images, video, and audio inputs—and combinations thereof—into a single, unified 768-dimensional vector space.

Model Info|   
---|---  
Context Window[ ↗](https://developers.cloudflare.com/workers-ai/platform/glossary/)| 8,192 tokens  
Zero data retention| Yes  
Unit Pricing| $0.0017 per M input tokens  
  
## Usage

### Text
    
    
    export interface Env {
    	AI: Ai;
    }
    
    export default {
    	async fetch(request, env): Promise<Response> {
    		// Prefix queries and documents with task instructions for better retrieval quality.
    		const response = await env.AI.run("@cf/google/embeddinggemma-2", {
    			input: [
    				"task: search result | query: waterproof shoes for trail running",
    				"title: Trail Runner X | text: Waterproof running shoes with a breathable mesh upper.",
    				"title: City Sneaker | text: Lightweight canvas sneakers for everyday wear.",
    			],
    		});
    
    		// response.data[i].embedding is a 768-dimensional vector
    		return Response.json(response);
    	},
    } satisfies ExportedHandler<Env>;
    
    
    import os
    import requests
    
    ACCOUNT_ID = "your-account-id"
    AUTH_TOKEN = os.environ.get("CLOUDFLARE_AUTH_TOKEN")
    
    response = requests.post(
        f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@cf/google/embeddinggemma-2",
        headers={"Authorization": f"Bearer {AUTH_TOKEN}"},
        json={
            "input": [
                "task: search result | query: waterproof shoes for trail running",
                "title: Trail Runner X | text: Waterproof running shoes with a breathable mesh upper.",
                "title: City Sneaker | text: Lightweight canvas sneakers for everyday wear.",
            ]
        },
    )
    print(response.json())
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/google/embeddinggemma-2 \
      -X POST \
      -H "Authorization: Bearer $CLOUDFLARE_AUTH_TOKEN" \
      -d '{
        "input": [
          "task: search result | query: waterproof shoes for trail running",
          "title: Trail Runner X | text: Waterproof running shoes with a breathable mesh upper.",
          "title: City Sneaker | text: Lightweight canvas sneakers for everyday wear."
        ]
      }'

### Images and video
    
    
    export interface Env {
    	AI: Ai;
    }
    
    // Media must be sent as base64 data URIs.
    async function toDataUri(url: string, mimeType: string): Promise<string> {
    	const bytes = new Uint8Array(await (await fetch(url)).arrayBuffer());
    	let binary = "";
    	for (const byte of bytes) binary += String.fromCharCode(byte);
    	return `data:${mimeType};base64,${btoa(binary)}`;
    }
    
    export default {
    	async fetch(request, env): Promise<Response> {
    		const image = await toDataUri("https://example.com/shoe.png", "image/png");
    		const video = await toDataUri("https://example.com/grip-test.mp4", "video/mp4");
    
    		// Each conversation in the array produces one embedding.
    		const response = await env.AI.run("@cf/google/embeddinggemma-2", {
    			messages: [
    				// Text, an image, and a video combined into a single embedding
    				[
    					{
    						role: "user",
    						content: [
    							{ type: "text", text: "Waterproof running shoes." },
    							{ type: "image_url", image_url: { url: image } },
    							{ type: "video_url", video_url: { url: video } },
    						],
    					},
    				],
    				// A text query to compare against
    				[
    					{
    						role: "user",
    						content: "task: search result | query: waterproof shoes for trail running",
    					},
    				],
    			],
    		});
    
    		// Both embeddings share one vector space, so you can compare them directly.
    		return Response.json(response);
    	},
    } satisfies ExportedHandler<Env>;
    
    
    import base64
    import os
    import requests
    
    ACCOUNT_ID = "your-account-id"
    AUTH_TOKEN = os.environ.get("CLOUDFLARE_AUTH_TOKEN")
    
    def data_uri(path, mime_type):
        with open(path, "rb") as f:
            return f"data:{mime_type};base64," + base64.b64encode(f.read()).decode()
    
    response = requests.post(
        f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@cf/google/embeddinggemma-2",
        headers={"Authorization": f"Bearer {AUTH_TOKEN}"},
        json={
            "messages": [
                [
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": "Waterproof running shoes."},
                            {"type": "image_url", "image_url": {"url": data_uri("shoe.png", "image/png")}},
                            {"type": "video_url", "video_url": {"url": data_uri("grip-test.mp4", "video/mp4")}},
                        ],
                    }
                ],
                [
                    {
                        "role": "user",
                        "content": "task: search result | query: waterproof shoes for trail running",
                    }
                ],
            ]
        },
    )
    print(response.json())

### Audio
    
    
    export interface Env {
    	AI: Ai;
    }
    
    export default {
    	async fetch(request, env): Promise<Response> {
    		// Use mono 16 kHz audio for best results.
    		const bytes = new Uint8Array(await (await fetch("https://example.com/clip.wav")).arrayBuffer());
    		let binary = "";
    		for (const byte of bytes) binary += String.fromCharCode(byte);
    
    		const response = await env.AI.run("@cf/google/embeddinggemma-2", {
    			messages: [
    				{
    					role: "user",
    					content: [
    						{ type: "input_audio", input_audio: { data: btoa(binary), format: "wav" } },
    					],
    				},
    			],
    			dimensions: 256,
    		});
    
    		// dimensions: 256 returns a shorter vector to reduce storage.
    		return Response.json(response);
    	},
    } satisfies ExportedHandler<Env>;
    
    
    import base64
    import os
    import requests
    
    ACCOUNT_ID = "your-account-id"
    AUTH_TOKEN = os.environ.get("CLOUDFLARE_AUTH_TOKEN")
    
    with open("clip.wav", "rb") as f:
        audio = base64.b64encode(f.read()).decode()
    
    response = requests.post(
        f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@cf/google/embeddinggemma-2",
        headers={"Authorization": f"Bearer {AUTH_TOKEN}"},
        json={
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"type": "input_audio", "input_audio": {"data": audio, "format": "wav"}}
                    ],
                }
            ],
            "dimensions": 256,
        },
    )
    print(response.json())
    
    
    {
      "id": "embd-...",
      "object": "list",
      "created": 1793902589,
      "model": "@cf/google/embeddinggemma-2",
      "data": [
        { "object": "embedding", "index": 0, "embedding": [-0.0137, 0.0037, 0.0386, ...] },
        { "object": "embedding", "index": 1, "embedding": [0.0312, -0.0147, 0.0081, ...] }
      ],
      "usage": { "prompt_tokens": 266, "total_tokens": 266 }
    }

Task prefixes

Prefix text with a task instruction for best results. For search, use `task: search result | query: ...` for queries and `title: ... | text: ...` for documents (use `title: none` when there is no title). For classification, clustering, or similarity, use the same prefix on every input, for example `task: clustering | query: ...`. Do not add prefixes to images, video, or audio. 

Inputs and limits

Send media as base64 data URIs. Remote URLs are not supported. All content in one embedding shares an 8,192 token context window. An image uses about 260 tokens, video uses about 140 tokens per sampled frame (one frame per second), and audio uses about 25 tokens per second. Set `dimensions` to 128, 256, or 512 to return shorter vectors, and use the same size for queries and documents. 

## Parameters

Schema variant

TextMultimodal

▶input

`one of`required

dimensions

`integer`default: 768enum: 128, 256, 512, 768Number of dimensions in the output embedding. Smaller sizes use Matryoshka truncation to reduce storage with a small quality cost. Queries and documents must use the same size.

encoding_format

`string`default: floatenum: float, base64Return each embedding as an array of floats, or as a base64-encoded string of little-endian float32 values.

▶messages[]

`array`requiredminItems: 1A conversation that produces one embedding, or an array of conversations that produces one embedding each. Content can mix text, images, video, and audio. Every input shares an 8,192 token context window.

dimensions

`integer`default: 768enum: 128, 256, 512, 768Number of dimensions in the output embedding. Smaller sizes use Matryoshka truncation to reduce storage with a small quality cost. Queries and documents must use the same size.

encoding_format

`string`default: floatenum: float, base64Return each embedding as an array of floats, or as a base64-encoded string of little-endian float32 values.

id

`string`

object

`string`enum: list

created

`integer`Unix timestamp of when the embeddings were created.

model

`string`

▶data[]

`array`One embedding per input, in request order.

▶usage{}

`object`

id

`string`

object

`string`enum: list

created

`integer`Unix timestamp of when the embeddings were created.

model

`string`

▶data[]

`array`One embedding per input, in request order.

▶usage{}

`object`

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/@cf/google/embeddinggemma-2/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/@cf/google/embeddinggemma-2/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/@cf/google/embeddinggemma-2/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/@cf/google/embeddinggemma-2/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
