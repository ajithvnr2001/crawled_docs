---
url: https://ai.google.dev/gemini-api/docs/optimization/
title: Gemini API optimization and inference
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:44:49.830530+00:00
---

# Gemini API optimization and inference

> Source: https://ai.google.dev/gemini-api/docs/optimization/

The Gemini API offers a variety of optimization mechanisms to help you balance speed, cost, and reliability based on your specific workload needs. Whether you're building real-time conversational bots or running heavy offline data-processing pipelines, choosing the right paradigm can significantly cut costs or boost performance.

Feature | Standard | Flex | Priority | Batch | Caching  
---|---|---|---|---|---  
**Pricing** | Full Price | 50% discount | 75% to 100% more than standard | 50% discount | 90% discount + Prorated token storage  
**Latency** | Seconds to minutes | Minutes (1–15 min target) | Seconds | Up to 24 hours | Faster time-to-first-token  
**Reliability** | High / Medium-high | Best-effort (Sheddable) | High (Non-sheddable) | High (for throughput) | N/A  
**Interface** | Synchronous | Synchronous | Synchronous | Asynchronous | Saved state  
**Best use case** | General application workflows | Non-urgent sequential chains | Production, user-facing apps | Massive datasets, offline evals | Recurring queries over same file  
  
## Inference service tiers (Synchronous)

You can shift between reliability-optimized and cost-optimized synchronous traffic by passing the `service_tier` parameter in your standard generation calls.

### Standard inference (Default)

The standard tier is the default option for sequential content generation. It provides normal response times without extra premiums or heavy queuing.

  * **Reliability:** Standard criticality
  * **Price:** Standard pricing.
  * **Best For:** Most interactive day-to-day applications.



### Priority inference (Latency-optimized)

[Priority](https://ai.google.dev/gemini-api/docs/priority-inference) processing routes your requests to high-criticality compute queues. This traffic is strictly non-sheddable (never preempted by other tiers) and offers the highest reliability. If you exceed dynamic Priority limits, the system will gracefully downgrade the request to Standard processing instead of failing with an error.

  * **Reliability:** Highest criticality
  * **Price:** 75% to 100% over Standard rates.
  * **Best for:** Customer chatbots, real-time fraud detection, and business-critical copilots.



### Flex inference (Cost-optimized)

[Flex inference](https://ai.google.dev/gemini-api/docs/flex-inference) offers a 50% discount compared to standard rates by utilizing opportunistic, off-peak compute capacity. Requests are processed synchronously, meaning you don't need to rewrite code to manage batch objects. Because it is "sheddable" traffic, requests may be preempted if the system experiences standard traffic spikes.

  * **Reliability:** Non-guaranteed, sheddable criticality
  * **Price:** 50% of Standard Pricing (billed per token).
  * **Best for:** Multi-step agentic workflows where call N+1 depends on the output of call N, background CRM updates, and offline evaluations.



## Batch API (Bulk, asynchronous)

[The Batch API](https://ai.google.dev/gemini-api/docs/batch-api) is designed to process large volumes of requests asynchronously at 50% of the standard cost. You can submit requests either as in-line dictionaries or using a JSONL input file (up to 2GB). It processes requests using background throughput queues with a target turnaround time of 24 hours.

  * **Reliability:** Sheddable but with 24h automated retries and queuing system
  * **Price:** 50% of Standard pricing.
  * **Best for:** Pre-processing massive datasets, running periodic regression test suites, and high-volume image or embedding generations.



## Context caching (Input savings)

[Context caching](https://ai.google.dev/gemini-api/docs/caching) is used when a substantial initial context is referenced repeatedly by shorter requests.

  * **Implicit caching:** Automatically enabled on Gemini 2.5 and newer models. The system passes on cost savings if your request hits existing caches based on common prompt prefixes.
  * **Explicit Caching:** You can manually create a cache object with a specific Time-To-Live (TTL). Once created, you refer to the cached tokens for subsequent requests to avoid passing the same corpus payload repeatedly. Explicit caching is not supported for Gemini 4 Argon and onward.
  * **Price:** Billed based on cache token count and storage duration (TTL).
  * **Best For:** Chatbots with extensive system instructions, repetitive analysis of lengthy video files, or queries against large document sets.



## Reduce video input costs with agentic processing

For long-form video content (over 5–10 minutes) or targeted queries, agentic processing can reduce input token costs by up to 88% while improving response quality. By default, all models (including Gemini 4) use [static processing](https://ai.google.dev/gemini-api/docs/video-understanding#agentic-video-understanding) to extract frames at 1 FPS. With agentic video understanding, the model inspects the video transcript first and dynamically loads visual segments at higher frame rates and resolutions only where needed. For short clips (under 5 minutes) or broad full-video summaries, keep the default static processing mode for a faster Time to First Token (TTFT) and lower token overhead. Agentic mode incurs internal reasoning (`total_thought_tokens`) and tool round-trips (`total_tool_use_tokens`) during timeline navigation.

To use agentic processing with Gemini 4 Argon, 3.8 Flash, 3.6 Flash, or 3.5 Flash Lite, set `processing: "agentic"` (Interactions API) or `media_processing: "AGENTIC"` (GenerateContent API) on your video input. If the model does not support agentic processing, it will return an error.

For more information, see [Agentic video understanding](https://ai.google.dev/gemini-api/docs/video-understanding#agentic-video-understanding).
