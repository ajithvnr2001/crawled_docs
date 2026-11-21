---
url: https://docs.comfy.org/catalog/models/gemini/gemini-3-8-flash/
title: Gemini 3.8 Flash text generation model (vertexai/gemini-3.8-flash): where to run it and pricing - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-21T15:11:14.027636+00:00
---

# Gemini 3.8 Flash text generation model (vertexai/gemini-3.8-flash): where to run it and pricing - ComfyUI

> Source: https://docs.comfy.org/catalog/models/gemini/gemini-3-8-flash/

## On this page

Back to top

  * Where you can run it
  * Call it with Comfy Router
  * Pricing



Catalog

# Gemini 3.8 Flash text generation model (vertexai/gemini-3.8-flash): where to run it and pricing

Copy pageCopy page

Gemini 3.8 Flash is a text generation model from Google Gemini. Run it with Comfy Router; templates, files, nodes, and pricing.

Copy pageCopy page

Model ID: vertexai/gemini-3.8-flash Provider: gemini Product: router Input: text, image, audio, video Output: text License: closed Gemini 3.8 Flash is a text generation model from Google Gemini. It takes text, image, audio and video as input and produces text. It has no open weights. It runs on Google Gemini’s servers, so you use it through Comfy Router.

## Where you can run it

Where| Page| Use it when  
---|---|---  
Comfy Router (API)| [Gemini 3.8 Flash with Comfy Router](https://docs.comfy.org/development/comfy-router/models/google/gemini-3-8-flash/code)| You call `vertexai/gemini-3.8-flash` from your own code with `COMFY_API_KEY`  
  
## Call it with Comfy Router

  * `POST https://api.comfy.org/v2/models/vertexai/gemini-3.8-flash`. Live request schema: `GET /v2/models/vertexai/gemini-3.8-flash/openapi.json`.



## Pricing

Comfy Router charges the model maker’s list price, billed from your workspace credits (211 credits = $1 USD). Current per-model prices are on [router.comfy.org](https://router.comfy.org).

  * Price a call before you run it: `POST https://api.comfy.org/v2/models/vertexai/gemini-3.8-flash/estimate`.
  * Billing facts, such as whether a refused request is charged: the `billing` field from `GET https://api.comfy.org/v2/models/vertexai/gemini-3.8-flash`.

See [Comfy Router pricing](https://docs.comfy.org/development/comfy-router/pricing) and [Billing](https://docs.comfy.org/development/comfy-router/billing#model-billing-facts).

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/catalog/models/gemini/gemini-3-8-flash.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/catalog/models/gemini/gemini-3-8-flash)
