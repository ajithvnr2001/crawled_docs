---
url: https://developers.cloudflare.com/ai-search/api/namespaces/workers-binding/
title: Workers binding \u00b7 Cloudflare AI Search docs
method: scrapling+scrapegraph
fetched_at: 2026-11-14T08:45:51.841171+00:00
---

# Workers binding · Cloudflare AI Search docs

> Source: https://developers.cloudflare.com/ai-search/api/namespaces/workers-binding/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI Search](https://developers.cloudflare.com/ai-search/)
  3. /…

API

  4. /Namespaces
  5. /Workers binding



# Workers binding

Last updated Nov 13, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewConfigure the bindingWhat the binding can do Get an instance List instances Create an instance Delete an instanceBind multiple namespaces

The `ai_search_namespaces` binding gives a [Worker](https://developers.cloudflare.com/workers/) access to one [namespace](https://developers.cloudflare.com/ai-search/concepts/namespaces/). Use it to get, list, create, and delete instances in that namespace, and to search across several of its instances in one call.

The binding is scoped to the namespace you configure. It cannot create, list, update, or delete namespaces. To manage namespaces, use the [REST API](https://developers.cloudflare.com/ai-search/api/namespaces/rest-api/), [Terraform](https://developers.cloudflare.com/ai-search/api/namespaces/terraform/), or [Wrangler](https://developers.cloudflare.com/ai-search/wrangler-commands/).

## Configure the binding

Add an `ai_search_namespaces` entry to your [Wrangler configuration](https://developers.cloudflare.com/workers/wrangler/configuration/) and set the namespace the binding can access:
    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      // Set this to today's date
      "compatibility_date": "2026-11-14",
      "ai_search_namespaces": [
        {
          "binding": "AI_SEARCH",
          "namespace": "support"
        }
      ]
    }
    
    
    # Set this to today's date
    compatibility_date = "2026-11-14"
    
    [[ai_search_namespaces]]
    binding = "AI_SEARCH"
    namespace = "support"

Field | Type | Required | Description  
---|---|---|---  
`binding` | string | Yes | The variable name available on `env`. For example, `"AI_SEARCH"` makes it accessible as `env.AI_SEARCH`.  
`namespace` | string | Yes | The namespace to bind to. A `default` namespace exists for every account. If the namespace does not exist, Wrangler creates it when you deploy.  
`remote` | boolean | No | Set to `true` for local development with `wrangler dev`.  
  
## What the binding can do

At runtime, `env.AI_SEARCH` is the namespace handle. It exposes the following methods:

Method | Description  
---|---  
`get()` | Returns a handle to an instance. Does not make a network call.  
`list()` | Lists the instances in the namespace.  
`create()` | Creates an instance in the namespace and returns a handle.  
`delete()` | Permanently deletes an instance and its indexed content.  
`search()` | Searches across several instances in the namespace.  
`chatCompletions()` | Generates a response from several instances in the namespace.  
  
For parameters and responses of the instance methods, refer to the [Instances Workers binding](https://developers.cloudflare.com/ai-search/api/instances/workers-binding/) reference. For `search()` and `chatCompletions()`, refer to the [Search Workers binding](https://developers.cloudflare.com/ai-search/api/search/workers-binding/) reference.

### Get an instance
    
    
    const instance = env.AI_SEARCH.get("docs");
    const results = await instance.search({
    	messages: [{ role: "user", content: "How do I reset my password?" }],
    });

### List instances
    
    
    const { result } = await env.AI_SEARCH.list();
    
    for (const instance of result) {
    	console.log(instance.id);
    }

### Create an instance
    
    
    const instance = await env.AI_SEARCH.create({
    	id: "faq",
    });

### Delete an instance
    
    
    await env.AI_SEARCH.delete("faq");

Caution

Deleting an instance permanently removes all indexed data, including embeddings, chunks, and source files.

## Bind multiple namespaces

Declare one binding per namespace. Each binding only reaches the instances in its own namespace.
    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "ai_search_namespaces": [
        {
          "binding": "BLOG_SEARCH",
          "namespace": "blog"
        },
        {
          "binding": "SUPPORT_SEARCH",
          "namespace": "support"
        }
      ]
    }
    
    
    [[ai_search_namespaces]]
    binding = "BLOG_SEARCH"
    namespace = "blog"
    
    [[ai_search_namespaces]]
    binding = "SUPPORT_SEARCH"
    namespace = "support"
    
    
    const blogPosts = await env.BLOG_SEARCH.list();
    const supportDocs = env.SUPPORT_SEARCH.get("docs");

[PreviousSearch modes](https://developers.cloudflare.com/ai-search/concepts/search-modes/)[NextREST API](https://developers.cloudflare.com/ai-search/api/namespaces/rest-api/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ai-search/api/namespaces/workers-binding.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
