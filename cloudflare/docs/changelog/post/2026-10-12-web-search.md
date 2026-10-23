---
url: https://developers.cloudflare.com/changelog/post/2026-10-12-web-search/
title: New web_search tool in the Agents SDK, powered by the Cloudflare Web Search API \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:10:32.669955+00:00
---

# New web_search tool in the Agents SDK, powered by the Cloudflare Web Search API · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-10-12-web-search/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)October 12, 2026

## New web_search tool in the Agents SDK, powered by the Cloudflare Web Search API

[Agents](https://developers.cloudflare.com/agents/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The [Cloudflare Agents SDK](https://developers.cloudflare.com/agents/) now provides a `web_search` tool that searches the public web through the [Cloudflare Web Search API](https://developers.cloudflare.com/web-search/), powered by [ceramic.ai, Exa, and Linkup](https://developers.cloudflare.com/web-search/providers/).

When you give the `web_search` tool to your agent, the model provides a query and max results, and receives back a short numbered list of titles, URLs, and trimmed descriptions. When you also provide the [`web_fetch`](https://developers.cloudflare.com/agents/tools/web-fetch/) tool to your agent, the model is told to use it to read the pages that the `web_search` tool returns.

To use the `web_search` tool, make sure you have [Agents SDK v0.27.0 ↗︎](https://github.com/cloudflare/agents/releases/tag/agents%400.27.0) or greater installed, and add it to a [Pi Durable](https://developers.cloudflare.com/agents/harnesses/pi/) [extension registry](https://developers.cloudflare.com/agents/harnesses/pi/extensions/) before opening the harness:
    
    
    import { webSearchTool } from "agents/websearch/pi";
    
    export class MyAgent extends DurableObject {
    	// ...
    
    	harness = new PiHarness({
    		harness: async ({ storage, context }) => {
    			this.registry.install({
    				name: "web-tools",
    				tools: [webSearchTool({ binding: this.env.AI, provider: "exa" })],
    			});
    
    			// ...
    
    			return Harness.open(
    				storage,
    				{ models, registry: this.registry },
    				context,
    			);
    		},
    	});
    }
    
    
    import { webSearchTool } from "agents/websearch/pi";
    
    export class MyAgent extends DurableObject<Env> {
    	// ...
    
    	readonly harness = new PiHarness({
    		harness: async ({ storage, context }) => {
    			this.registry.install({
    				name: "web-tools",
    				tools: [webSearchTool({ binding: this.env.AI, provider: "exa" })],
    			});
    
    			// ...
    
    			return Harness.open(
    				storage,
    				{ models, registry: this.registry },
    				context,
    			);
    		},
    	});
    }

The SDK also includes AI SDK and TanStack AI adapters. To search without a model, such as from a scheduled job, use `createAIWebSearch()` or `createHTTPWebSearch()` from `agents/websearch`.

For setup, options, and error handling, refer to [Web search](https://developers.cloudflare.com/agents/tools/web-search/).
