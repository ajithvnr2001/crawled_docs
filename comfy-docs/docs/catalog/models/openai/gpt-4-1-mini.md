---
url: https://docs.comfy.org/catalog/models/openai/gpt-4-1-mini/
title: GPT 4.1 Mini text generation model (openai/gpt-4.1-mini): where to run it and pricing - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-21T15:11:18.161326+00:00
---

# GPT 4.1 Mini text generation model (openai/gpt-4.1-mini): where to run it and pricing - ComfyUI

> Source: https://docs.comfy.org/catalog/models/openai/gpt-4-1-mini/

## On this page

Back to top

  * Where you can run it
  * Call it with Comfy Router
  * Pricing



Catalog

# GPT 4.1 Mini text generation model (openai/gpt-4.1-mini): where to run it and pricing

Copy pageCopy page

GPT 4.1 Mini is a text generation model from OpenAI (inc. Sora). Run it with Comfy Router; templates, files, nodes, and pricing.

Copy pageCopy page

Model ID: openai/gpt-4.1-mini Provider: openai Product: router Input: text, image Output: text License: closed GPT 4.1 Mini is a text generation model from OpenAI (inc. Sora). It takes text and image as input and produces text. It has no open weights. It runs on OpenAI (inc. Sora)‘s servers, so you use it through Comfy Router.

## Where you can run it

Where| Page| Use it when  
---|---|---  
Comfy Router (API)| [GPT 4.1 Mini with Comfy Router](https://docs.comfy.org/development/comfy-router/models/openai/gpt-4-1-mini/code)| You call `openai/gpt-4.1-mini` from your own code with `COMFY_API_KEY`  
  
## Call it with Comfy Router

  * `POST https://api.comfy.org/v2/models/openai/gpt-4.1-mini`. Live request schema: `GET /v2/models/openai/gpt-4.1-mini/openapi.json`.



## Pricing

Comfy Router charges the model maker’s list price, billed from your workspace credits (211 credits = $1 USD). Current per-model prices are on [router.comfy.org](https://router.comfy.org).

  * Price a call before you run it: `POST https://api.comfy.org/v2/models/openai/gpt-4.1-mini/estimate`.
  * Billing facts, such as whether a refused request is charged: the `billing` field from `GET https://api.comfy.org/v2/models/openai/gpt-4.1-mini`.

See [Comfy Router pricing](https://docs.comfy.org/development/comfy-router/pricing) and [Billing](https://docs.comfy.org/development/comfy-router/billing#model-billing-facts).

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/catalog/models/openai/gpt-4-1-mini.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/catalog/models/openai/gpt-4-1-mini)
