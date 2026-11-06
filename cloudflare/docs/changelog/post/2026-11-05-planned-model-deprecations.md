---
url: https://developers.cloudflare.com/changelog/post/2026-11-05-planned-model-deprecations/
title: Planned model deprecations on Workers AI \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-11-06T09:03:44.272768+00:00
---

# Planned model deprecations on Workers AI · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-11-05-planned-model-deprecations/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)November 5, 2026

## Planned model deprecations on Workers AI

[Workers AI](https://developers.cloudflare.com/workers-ai/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

We are refreshing the Workers AI model catalog to make room for new releases and updated models. Update your apps to remove references to the models listed below before November 15, 2026.

We recommend moving to newer models for the best token efficiency and throughput. For pricing, refer to the [Workers AI pricing page](https://developers.cloudflare.com/workers-ai/platform/pricing/).

#### Recommended LLM replacements

  * For frontier model needs: [`@cf/deepseek-ai/deepseek-v4.1-flash-1017`](https://developers.cloudflare.com/workers-ai/models/deepseek-v4.1-flash-1017/) and [`@cf/zai-org/glm-5.3`](https://developers.cloudflare.com/workers-ai/models/glm-5.3/).
  * For smaller model needs: [`@cf/google/gemma-4-26b-a4b-it`](https://developers.cloudflare.com/workers-ai/models/gemma-4-26b-a4b-it/) and [`@cf/qwen/qwen3.8-27b`](https://developers.cloudflare.com/workers-ai/models/qwen3.8-27b/).



#### Models deprecated on November 15, 2026

#### LLMs

  * `@cf/deepseek-ai/deepseek-r1-distill-qwen-32b`
  * `@cf/nvidia/nemotron-3-120b-a12b`
  * `@cf/deepseek-ai/deepseek-v4-pro-0813`
  * `@cf/deepseek-ai/deepseek-v4-flash-0731`
  * `@cf/qwen/qwq-32b`
  * `@cf/qwen/qwen3-30b-a3b-fp8`
  * `@cf/moonshotai/kimi-k2.6`
  * `@cf/moonshotai/kimi-k2.7-code`
  * `@cf/zai-org/glm-5.2`
  * `@cf/zai-org/glm-5.3-flash`
  * `@cf/meta-llama/llama-2-7b-chat-hf-lora`
  * `@cf/google/gemma-2b-it-lora`
  * `@cf/google/gemma-7b-it-lora`
  * `@cf/meta/llama-3.1-8b-instruct-fp8`
  * `@cf/meta/llama-3.2-1b-instruct`
  * `@cf/meta/llama-3.2-3b-instruct`



#### Other models

Each deprecated model is followed by its suggested replacement.

  * `@cf/myshell-ai/melotts` → [`@cf/deepgram/aura-2-en`](https://developers.cloudflare.com/workers-ai/models/aura-2-en/)
  * `@cf/stabilityai/stable-diffusion-xl-base-1.0` → [`@cf/black-forest-labs/flux-2-klein-9b`](https://developers.cloudflare.com/workers-ai/models/flux-2-klein-9b/)
  * `@cf/runwayml/stable-diffusion-v1-5-inpainting` → [`@cf/black-forest-labs/flux-2-klein-9b`](https://developers.cloudflare.com/workers-ai/models/flux-2-klein-9b/)
  * `@cf/bytedance/stable-diffusion-xl-lightning` → [`@cf/black-forest-labs/flux-2-klein-9b`](https://developers.cloudflare.com/workers-ai/models/flux-2-klein-9b/)
  * `@cf/lykon/dreamshaper-8-lcm` → [`@cf/black-forest-labs/flux-2-klein-9b`](https://developers.cloudflare.com/workers-ai/models/flux-2-klein-9b/)
  * `@cf/openai/whisper-tiny-en` → [`@cf/deepgram/nova-3`](https://developers.cloudflare.com/workers-ai/models/nova-3/)
  * `@cf/llava-hf/llava-1.5-7b-hf` → [`@cf/moondream/moondream3.1-9B-A2B`](https://developers.cloudflare.com/workers-ai/models/moondream3.1-9B-A2B/)
  * `@cf/google/embeddinggemma-300m` → `@cf/google/embeddinggemma-2` (available soon)



For the full list of available models, refer to the [Workers AI model catalog](https://developers.cloudflare.com/workers-ai/models/).
