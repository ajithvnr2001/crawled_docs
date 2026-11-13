---
url: https://developers.cloudflare.com/changelog/post/2026-11-12-embeddinggemma-2-workers-ai/
title: EmbeddingGemma 2 now available on Workers AI \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-13T09:17:04.953871+00:00
---

# EmbeddingGemma 2 now available on Workers AI · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-12-embeddinggemma-2-workers-ai/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 12, 2026

## EmbeddingGemma 2 now available on Workers AI

[Workers AI](https://developers.cloudflare.com/workers-ai/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[`@cf/google/embeddinggemma-2`](https://developers.cloudflare.com/workers-ai/models/embeddinggemma-2/) is now available on Workers AI. EmbeddingGemma 2 is an open multimodal embedding model from Google DeepMind. It maps text (including code), images, video, and audio into a single 768-dimensional vector space, so you can search a mixed collection of products, documents, and media with one text query.

**Key capabilities:**

  * **Multimodal** : Embed text, images, video, audio, or any combination of them in one input. Every embedding shares the same vector space.
  * **Multilingual and code** : Understands more than 100 languages and improves code retrieval over the original EmbeddingGemma.
  * **Flexible dimensions** : Set `dimensions` to 128, 256, or 512 to return shorter vectors and reduce storage, with a small cost to quality.
  * **Long context** : An 8,192 token context window, shared across all content in an input.
  * **Task prefixes** : Add short instructions such as `task: search result | query: ...` to tune embeddings for search, classification, clustering, or similarity.



Send text with `input`. Send images, video, and audio as base64 data URIs in `messages`:
    
    
    const response = await env.AI.run("@cf/google/embeddinggemma-2", {
    	messages: [
    		[
    			{
    				role: "user",
    				content: [
    					{ type: "text", text: "Waterproof running shoes." },
    					{ type: "image_url", image_url: { url: imageDataUri } },
    				],
    			},
    		],
    		[
    			{
    				role: "user",
    				content:
    					"task: search result | query: waterproof shoes for trail running",
    			},
    		],
    	],
    });
    
    
    const response = await env.AI.run("@cf/google/embeddinggemma-2", {
    	messages: [
    		[
    			{
    				role: "user",
    				content: [
    					{ type: "text", text: "Waterproof running shoes." },
    					{ type: "image_url", image_url: { url: imageDataUri } },
    				],
    			},
    		],
    		[
    			{
    				role: "user",
    				content:
    					"task: search result | query: waterproof shoes for trail running",
    			},
    		],
    	],
    });

Pricing is $0.0017 per million input tokens.

For more information, refer to the [EmbeddingGemma 2 model page](https://developers.cloudflare.com/workers-ai/models/embeddinggemma-2/) and [pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/#embeddings-model-pricing).
