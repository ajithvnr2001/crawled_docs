---
url: https://docs.comfy.org/development/comfy-router/providers/
title: Comfy Router serving providers - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:53.074969+00:00
---

# Comfy Router serving providers - ComfyUI

> Source: https://docs.comfy.org/development/comfy-router/providers/

## On this page

  * Provider coverage



Models

# Comfy Router serving providers

Copy pageCopy page

See which providers can serve each Comfy Router model and how to select an alternate provider.

Copy pageCopy page

Every model uses `POST /v2/models/{provider}/{model}`. Comfy is the default provider. For models with alternate coverage, `model_provider` selects another provider without changing the model ID or request body. See [`model_provider`, `strict_mode` and `fallback_provider`](https://docs.comfy.org/development/comfy-router/reference#post-v2modelsprovidermodel) in the API reference.

## 

​

Provider coverage

Model / provider| **Comfy (default)**| **fal**| **Higgsfield**| **Pika**| **Runware**| **WaveSpeed**  
---|---|---|---|---|---|---  
[Dreamina Seedance 2.0 260128](https://docs.comfy.org/development/comfy-router/models/byteplus/dreamina-seedance-2-0-260128/code)| ✓| ✓| ✓| ✓| ✓| ✓  
[Dreamina Seedance 2.5 260628](https://docs.comfy.org/development/comfy-router/models/byteplus/dreamina-seedance-2-5-260628/code)| ✓| ✓| ✓| -| ✓| ✓  
[GPT Image 2](https://docs.comfy.org/development/comfy-router/models/openai/gpt-image-2/code)| ✓| ✓| -| ✓| ✓| ✓  
[GPT Image 2.5 Flare](https://docs.comfy.org/development/comfy-router/models/openai/gpt-image-2-5-flare/code)| ✓| ✓| -| -| ✓| ✓  
[GPT Image 2.5 Sunburst](https://docs.comfy.org/development/comfy-router/models/openai/gpt-image-2-5-sunburst/code)| ✓| ✓| -| -| ✓| ✓  
[Kling 3.0 Turbo](https://docs.comfy.org/development/comfy-router/models/kling/kling-3-0-turbo/code)| ✓| -| ✓| -| -| -  
[Kling V3](https://docs.comfy.org/development/comfy-router/models/kling/kling-v3/code)| ✓| -| ✓| -| -| -  
[Nano Banana 2](https://docs.comfy.org/development/comfy-router/models/google/nano-banana-2/code)| ✓| ✓| -| ✓| ✓| ✓  
[Nano Banana Pro](https://docs.comfy.org/development/comfy-router/models/google/nano-banana-pro/code)| ✓| ✓| -| ✓| ✓| ✓  
[Wan 3.0 Video](https://docs.comfy.org/development/comfy-router/models/wan/wan3-0-video/code)| ✓| -| ✓| -| -| -  
  
`strict_mode=false` (the default) translates the native request and response for the selected provider. Fields that cannot be translated are listed in the `X-Comfy-Router-Dropped-Params` response header.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfy-router/providers.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfy-router/providers)

[Comfy Router pricingPrevious](https://docs.comfy.org/development/comfy-router/pricing)[Use Claude Fable 5.1 with Comfy RouterNext](https://docs.comfy.org/development/comfy-router/models/anthropic/claude-fable-5-1/code)

⌘I

[ComfyUI home page![light logo](https://mintcdn.com/dripart/WCFdTagRdhtvk9-o/logo/light.svg?fit=max&auto=format&n=WCFdTagRdhtvk9-o&q=85&s=ec112de87239058f5a931a7e4b594965)![dark logo](https://mintcdn.com/dripart/QzWbjSCBG7w61rR3/logo/dark.svg?fit=max&auto=format&n=QzWbjSCBG7w61rR3&q=85&s=62b4d879fb3aadbd7a468d1539032d6f)](https://docs.comfy.org/)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

Resources

[installation](https://docs.comfy.org/installation/system_requirements)[Tutorials](https://docs.comfy.org/tutorials/basic/text-to-image)[Development](https://docs.comfy.org/development/overview)

Products

[Features](https://www.comfy.org/?utm_source=docs)[Gallery](https://www.comfy.org/gallery?utm_source=docs)[Download](https://www.comfy.org/download?utm_source=docs)

Company

[About](https://www.comfy.org/about?utm_source=docs)[Careers](https://www.comfy.org/careers?utm_source=docs)[Terms of Service](https://www.comfy.org/terms-of-service?utm_source=docs)[Privacy Policy](https://www.comfy.org/privacy-policy?utm_source=docs)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=dripart)
