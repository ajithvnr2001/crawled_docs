---
url: https://docs.comfy.org/development/comfy-router/providers/
title: Comfy Router serving providers - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-18T16:18:18.432266+00:00
---

# Comfy Router serving providers - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/providers/

## On this page

Back to top

  * Provider coverage



Models

# Comfy Router serving providers

Copy pageCopy page

See which providers can serve each Comfy Router model and how to select an alternate provider.

Copy pageCopy page

Every model uses `POST /v2/models/{provider}/{model}`. Comfy is the default provider. For models with alternate coverage, `model_provider` selects another provider without changing the model ID or request body. See [`model_provider`, `strict_mode` and `fallback_provider`](https://docs.comfy.org/development/comfy-router/reference#post-v2modelsprovidermodel) in the API reference.

## Provider coverage

Model / provider| **Comfy (default)**| **fal**| **Higgsfield**| **Kelly**| **MiniMax**| **Pika**| **Runware**| **Tencent**| **WaveSpeed**  
---|---|---|---|---|---|---|---|---|---  
[Dreamina Seedance 2.0 260128](https://docs.comfy.org/development/comfy-router/models/byteplus/dreamina-seedance-2-0-260128/code)| ✓| ✓| ✓| ✓| -| ✓| ✓| -| ✓  
[Dreamina Seedance 2.0 Fast 260128](https://docs.comfy.org/development/comfy-router/models/byteplus/dreamina-seedance-2-0-fast-260128/code)| ✓| -| -| ✓| -| -| -| -| -  
[Dreamina Seedance 2.5 260628](https://docs.comfy.org/development/comfy-router/models/byteplus/dreamina-seedance-2-5-260628/code)| ✓| ✓| ✓| ✓| -| -| ✓| -| ✓  
[Gemini 2.5 Flash Image](https://docs.comfy.org/development/comfy-router/models/google/gemini-2-5-flash-image/code)| ✓| -| -| -| ✓| -| -| -| -  
[Gemini Nano Banana 2.1](https://docs.comfy.org/development/comfy-router/models/google/gemini-nano-banana-2-1/code)| ✓| -| -| -| ✓| -| -| -| -  
[GPT Image 2](https://docs.comfy.org/development/comfy-router/models/openai/gpt-image-2/code)| ✓| ✓| -| -| ✓| -| ✓| -| ✓  
[GPT Image 2.5 Flare](https://docs.comfy.org/development/comfy-router/models/openai/gpt-image-2-5-flare/code)| ✓| ✓| -| -| ✓| -| ✓| -| ✓  
[GPT Image 2.5 Sunburst](https://docs.comfy.org/development/comfy-router/models/openai/gpt-image-2-5-sunburst/code)| ✓| ✓| -| -| ✓| -| ✓| -| ✓  
[GPT Image 2.6 Flare](https://docs.comfy.org/development/comfy-router/models/openai/gpt-image-2-6-flare/code)| ✓| -| -| -| ✓| -| -| -| -  
[GPT Image 2.6 Sunburst](https://docs.comfy.org/development/comfy-router/models/openai/gpt-image-2-6-sunburst/code)| ✓| -| -| -| ✓| -| -| -| -  
[Kling 3.0 Turbo](https://docs.comfy.org/development/comfy-router/models/kling/kling-3-0-turbo/code)| ✓| -| ✓| -| -| -| -| -| -  
[Kling V3](https://docs.comfy.org/development/comfy-router/models/kling/kling-v3/code)| ✓| -| ✓| -| -| -| -| ✓*| -  
[Nano Banana 2](https://docs.comfy.org/development/comfy-router/models/google/nano-banana-2/code)| ✓| ✓| -| -| ✓| ✓| ✓| -| ✓  
[Nano Banana Pro](https://docs.comfy.org/development/comfy-router/models/google/nano-banana-pro/code)| ✓| ✓| -| -| ✓| ✓| ✓| -| ✓  
[Wan 3.0 Video](https://docs.comfy.org/development/comfy-router/models/wan/wan3-0-video/code)| ✓| -| ✓| -| -| -| -| -| -  
  
* This provider serves the model with narrower limits than the default; see the model page. `strict_mode=false` (the default) translates the native request and response for the selected provider. Fields that cannot be translated are listed in the `X-Comfy-Router-Dropped-Params` response header.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/providers.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/providers)

[Pricing](https://docs.comfy.org/development/comfy-router/pricing)[Claude Fable 5.1](https://docs.comfy.org/development/comfy-router/models/anthropic/claude-fable-5-1/code)
