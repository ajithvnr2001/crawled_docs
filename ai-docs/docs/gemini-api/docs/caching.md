---
url: https://ai.google.dev/gemini-api/docs/caching/
title: Context caching
method: scrapling+scrapegraph
fetched_at: 2026-10-23T16:39:43.340295+00:00
---

# Context caching

> Source: https://ai.google.dev/gemini-api/docs/caching/

In a typical AI workflow, you might pass the same input tokens over and over to a model. The Gemini API offers implicit caching to optimize performance and costs.

## Implicit caching

Implicit caching is enabled by default for all Gemini 2.5 and newer models. It is supported for both [stateful](https://ai.google.dev/gemini-api/docs/text-generation#multi-turn-conversations) (using `previous_interaction_id`) and [stateless](https://ai.google.dev/gemini-api/docs/text-generation#stateless-conversations) conversation modes. We automatically pass on cost savings if your request hits caches. You don't need to configure anything to turn it on. The following table lists the minimum input token count for each model:

Model | Min token limit  
---|---  
Gemini 4 Argon | 4,096  
Gemini 3.8 Flash | 4,096  
Gemini 3.6 Flash | 4,096  
Gemini 3.1 Pro Preview | 4,096  
Gemini 2.5 Flash | 2,048  
Gemini 2.5 Pro | 2,048  
  
To increase the chance of an implicit cache hit:

  * Try putting large and common contents at the beginning of your prompt
  * Try to send requests with similar prefix in a short amount of time



You can see the number of tokens which were cache hits in the response object's `usage.total_cached_tokens` (Python and JavaScript) field.
