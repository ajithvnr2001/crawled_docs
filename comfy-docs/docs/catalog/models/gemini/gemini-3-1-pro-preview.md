---
url: https://docs.comfy.org/catalog/models/gemini/gemini-3-1-pro-preview/
title: Google Gemini audio generation and image generation model (vertexai/gemini-3.1-pro-preview): where to run it and pricing - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-21T15:11:14.173715+00:00
---

# Google Gemini audio generation and image generation model (vertexai/gemini-3.1-pro-preview): where to run it and pricing - ComfyUI

> Source: https://docs.comfy.org/catalog/models/gemini/gemini-3-1-pro-preview/

## On this page

Back to top

  * Where you can run it
  * Call it with Comfy Router
  * Workflow templates
  * Nodes
  * Pricing



Catalog

# Google Gemini audio generation and image generation model (vertexai/gemini-3.1-pro-preview): where to run it and pricing

Copy pageCopy page

Google Gemini is a audio generation and image generation model from Google Gemini. Run it with Comfy Router and Comfy Cloud; templates, files, nodes, and…

Copy pageCopy page

Model ID: vertexai/gemini-3.1-pro-preview Provider: gemini Product: router, cloud, workflows, nodes Input: text, image Output: audio, image License: closed Google Gemini is a audio generation and image generation model from Google Gemini. It takes text and image as input and produces audio and image. It has no open weights. It runs on Google Gemini’s servers, so you use it through Comfy Router and Partner Nodes in ComfyUI and Comfy Cloud.

## Where you can run it

Where| Page| Use it when  
---|---|---  
Comfy Router (API)| [Google Gemini with Comfy Router](https://docs.comfy.org/development/comfy-router/models/google/gemini/code)| You call `vertexai/gemini-3.1-pro-preview` from your own code with `COMFY_API_KEY`  
Partner Nodes (ComfyUI and Comfy Cloud)| [Gemini 4 Hydrogen: Image to Prompt in ComfyUI](https://docs.comfy.org/tutorials/partner-nodes/google/gemini-4-hydrogen)| You build a workflow with the hosted model  
Partner Nodes (ComfyUI and Comfy Cloud)| [Gemini Omni Flash 1.2: Conversational Video Generation](https://docs.comfy.org/tutorials/partner-nodes/google/gemini-omni-flash-1-2)| You build a workflow with the hosted model  
Partner Nodes (ComfyUI and Comfy Cloud)| [Gemini Omni Flash: Conversational Video Generation](https://docs.comfy.org/tutorials/partner-nodes/google/gemini-omni-flash)| You build a workflow with the hosted model  
Partner Nodes (ComfyUI and Comfy Cloud)| [Google Gemini in ComfyUI: Chat and Image Understanding](https://docs.comfy.org/tutorials/partner-nodes/google/gemini)| You build a workflow with the hosted model  
Comfy Cloud| [Open `api_google_gemini` on Comfy Cloud](https://cloud.comfy.org/?template=api_google_gemini)| You want to run a ready-made workflow without installing anything  
  
## Call it with Comfy Router

  * `POST https://api.comfy.org/v2/models/vertexai/gemini-3.1-pro-preview`. Live request schema: `GET /v2/models/vertexai/gemini-3.1-pro-preview/openapi.json`.



## Workflow templates

Template| Title| Added  
---|---|---  
`audio_ace_step_1_5_split_llm`| ACE-Step 1.5 AI Lyric Song Generation| 2026-02-09  
`templates-poster_product_integration`| Generate Poster/Ad Asset with your Product| 2025-12-15  
`api_google_gemini`| Google Gemini| 2025-03-01  
`template_seedance2_0_viral_videos_character_swap`| Seedance 2.0: Viral Videos Character Swap| 2026-05-19  
`template_seedance_2_0_plus_llm_prompt_helper`| Seedance 2.0 + LLM Prompt Helper| 2026-05-10  
`template_product_placement`| Product Placement| 2026-03-30  
`template_sirolim_image_script_video`| Image to Script to Kling Video Generation| 2026-03-09  
`templates_mjm_airt_machine_api`| AIrt MAchIne (API version)| 2026-03-03  
`templates_mjm_looped_restyler`| Looped Restyler| 2026-03-03  
`templates-3D_logo_texture_animation`| Dynamic 3D Logo Animations| 2025-12-15  
  
## Nodes

  * [GeminiNode](https://docs.comfy.org/built-in-nodes/GeminiNode)
  * [GeminiNodeV2](https://docs.comfy.org/built-in-nodes/GeminiNodeV2)
  * [GeminiNodeV3](https://docs.comfy.org/built-in-nodes/GeminiNodeV3)



## Pricing

Comfy Router charges the model maker’s list price, billed from your workspace credits (211 credits = $1 USD). Current per-model prices are on [router.comfy.org](https://router.comfy.org).

  * Price a call before you run it: `POST https://api.comfy.org/v2/models/vertexai/gemini-3.1-pro-preview/estimate`.
  * Billing facts, such as whether a refused request is charged: the `billing` field from `GET https://api.comfy.org/v2/models/vertexai/gemini-3.1-pro-preview`.

See [Comfy Router pricing](https://docs.comfy.org/development/comfy-router/pricing) and [Billing](https://docs.comfy.org/development/comfy-router/billing#model-billing-facts).

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/catalog/models/gemini/gemini-3-1-pro-preview.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/catalog/models/gemini/gemini-3-1-pro-preview)
