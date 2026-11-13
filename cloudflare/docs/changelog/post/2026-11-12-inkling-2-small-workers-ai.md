---
url: https://developers.cloudflare.com/changelog/post/2026-11-12-inkling-2-small-workers-ai/
title: Inkling 2 Small now available on Workers AI \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-13T09:17:05.158916+00:00
---

# Inkling 2 Small now available on Workers AI · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-12-inkling-2-small-workers-ai/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 12, 2026

## Inkling 2 Small now available on Workers AI

[Workers AI](https://developers.cloudflare.com/workers-ai/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[`@cf/thinkingmachines/inkling-2-small`](https://developers.cloudflare.com/workers-ai/models/inkling-2-small/) is now available on Workers AI. Inkling 2 Small is the second generation of Inkling models from Thinking Machines Lab, and the first frontier open model from a US lab on Workers AI.

Inkling 2 Small is more capable than the previous generation. It is a multimodal Mixture-of-Experts model with 594B total parameters and 18B active parameters. Thinking Machines trained it much faster than previous models because of improvements to their pre-training and infrastructure.

Inkling 2 Small works well for:

  * **Agentic coding** : Plan, write, and edit code across multi-step tasks.
  * **Vision understanding** : Interpret images sent alongside text in the same request.
  * **General agentic knowledge work** : Research, analyze, and act on information with tools.



**Key capabilities:**

  * **Vision** : Accepts text and image inputs.
  * **Reasoning** : Reasoning is on by default at `high` effort. Set `reasoning_effort` to `max`, `medium`, `low`, or `minimal` to change the effort, or to `none` to turn reasoning off.
  * **Function calling** : Build agents that invoke tools and APIs across multiple conversation turns.
  * **Long context** : A full 1,048,576 token context window.



Inkling 2 Small requires the [Workers Paid plan](https://developers.cloudflare.com/workers/platform/pricing/#workers) or prepaid [AI Gateway credits](https://developers.cloudflare.com/ai-gateway/features/unified-billing/). The default rate limit is 20 requests per minute with standard Workers AI billing and 50 requests per minute with prepaid AI Gateway credits. For details, refer to [limits](https://developers.cloudflare.com/workers-ai/platform/limits/#paid-models).

Use Inkling 2 Small through the [Workers AI binding](https://developers.cloudflare.com/workers-ai/configuration/bindings/) (`env.AI.run()`), the REST API, the [OpenAI-compatible endpoint](https://developers.cloudflare.com/workers-ai/configuration/open-ai-compatibility/), or [AI Gateway](https://developers.cloudflare.com/ai-gateway/).

For more information, refer to the [Inkling 2 Small model page](https://developers.cloudflare.com/workers-ai/models/inkling-2-small/) and [pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/).
