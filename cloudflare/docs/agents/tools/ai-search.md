---
url: https://developers.cloudflare.com/agents/tools/ai-search/
title: AI Search \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-10-30T08:19:27.307827+00:00
---

# AI Search · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/tools/ai-search/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /Tools
  4. /AI Search



# AI Search

Last updated Oct 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBasic patternConfigurationRelated resources

Agents can use [AI Search](https://developers.cloudflare.com/ai-search/) to retrieve relevant information from indexed content and use it to augment [calls to AI models](https://developers.cloudflare.com/agents/models/). AI Search manages the retrieval pipeline for you, including indexing, search, and optional chat completions over your content.

Use AI Search when you want an agent to:

  * Search product docs, support content, user files, or internal knowledge bases.
  * Retrieve relevant chunks before calling a model.
  * Use managed indexing instead of building retrieval infrastructure yourself.
  * Query content from an R2 bucket, website, or uploaded files.



## Basic pattern

Bind AI Search to your Worker, then query an instance from an agent method.
    
    
    import { Agent, callable } from "agents";
    
    export class SearchAgent extends Agent {
    	@callable()
    	async searchKnowledge(query) {
    		const instance = this.env.AI_SEARCH.get("my-instance");
    
    		const results = await instance.search({
    			messages: [{ role: "user", content: query }],
    		});
    
    		return results;
    	}
    }
    
    
    import { Agent, callable } from "agents";
    
    type Env = {
    	AI_SEARCH: AiSearchNamespace;
    };
    
    export class SearchAgent extends Agent<Env> {
    	@callable()
    	async searchKnowledge(query: string) {
    		const instance = this.env.AI_SEARCH.get("my-instance");
    
    		const results = await instance.search({
    			messages: [{ role: "user", content: query }],
    		});
    
    		return results;
    	}
    }

For answer generation, use `chatCompletions()` to retrieve relevant content and generate a response in one call.
    
    
    const instance = this.env.AI_SEARCH.get("my-instance");
    
    const response = await instance.chatCompletions({
    	messages: [{ role: "user", content: "How do I deploy an Agent?" }],
    	model: "@cf/meta/llama-3.3-70b-instruct-fp8-fast",
    	ai_search_options: {
    		retrieval: {
    			max_num_results: 5,
    		},
    	},
    });
    
    
    const instance = this.env.AI_SEARCH.get("my-instance");
    
    const response = await instance.chatCompletions({
    	messages: [{ role: "user", content: "How do I deploy an Agent?" }],
    	model: "@cf/meta/llama-3.3-70b-instruct-fp8-fast",
    	ai_search_options: {
    		retrieval: {
    			max_num_results: 5,
    		},
    	},
    });

## Configuration

Use an `ai_search_namespaces` binding when the agent needs to access AI Search instances by name.
    
    
    {
    	"ai_search_namespaces": [
    		{
    			"binding": "AI_SEARCH",
    			"namespace": "default",
    			"remote": true
    		}
    	]
    }
    
    
    [[ai_search_namespaces]]
    binding = "AI_SEARCH"
    namespace = "default"
    remote = true

Use `remote: true` to query deployed AI Search instances during local development with `wrangler dev`.

## Related resources

### [AI Search](https://developers.cloudflare.com/ai-search/)

Create managed retrieval pipelines over websites, R2 buckets, and uploaded files.

### [Workers binding](https://developers.cloudflare.com/ai-search/api/search/workers-binding/)

Query AI Search directly from Workers code.

### [Create an AI Search instance](https://developers.cloudflare.com/ai-search/get-started/)

Create your first AI Search instance and run your first query.

[PreviousWeb search](https://developers.cloudflare.com/agents/tools/web-search/)[NextOverview](https://developers.cloudflare.com/agents/tools/payments/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/tools/ai-search.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
