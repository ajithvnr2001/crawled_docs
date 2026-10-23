---
url: https://docs.comfy.org/built-in-nodes/LatentUpscaleModelLoader/
title: LatentUpscaleModelLoader - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:22.108247+00:00
---

# LatentUpscaleModelLoader - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LatentUpscaleModelLoader/

Loaders

# LatentUpscaleModelLoader - ComfyUI Built-in Node Documentation

Copy pageCopy page

The LatentUpscaleModelLoader node loads a model specialized in upscaling latent representations from a file stored in ComfyUI’s latentupscalemodels folder.

Copy pageCopy page

The LatentUpscaleModelLoader node loads a model specialized in upscaling latent representations from a file stored in ComfyUI’s `latent_upscale_models` folder. It automatically detects the model architecture from the file contents (Hunyuan Video 720p, Hunyuan Video 1080p, or a Latent Upsampler) and configures the matching internal model, so the result is ready to be used by other nodes.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model_name`| The name of the latent upscale model file to load. The available options are dynamically populated from the files present in ComfyUI’s `latent_upscale_models` directory.| COMBO| Yes| All files in the `latent_upscale_models` folder  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| The loaded latent upscale model, configured and ready for use. Depending on the detected file contents, this is a 720p Hunyuan Video upscaler, a 1080p Hunyuan Video upscaler, or a wrapped Latent Upsampler model.| LATENT_UPSCALE_MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscaleModelLoader/en.md)

* * *

**Source fingerprint (SHA-256):** `7e23214b1b1fc11be84910a5a209c7990a5199120cb0e6b6c61302a442dcf153`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LatentUpscaleModelLoader.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LatentUpscaleModelLoader)

[ImageOnlyCheckpointLoader - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ImageOnlyCheckpointLoader)[LoadBackgroundRemovalModel - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LoadBackgroundRemovalModel)

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
