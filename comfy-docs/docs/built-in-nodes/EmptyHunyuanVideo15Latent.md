---
url: https://docs.comfy.org/built-in-nodes/EmptyHunyuanVideo15Latent/
title: EmptyHunyuanVideo15Latent - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:52.878420+00:00
---

# EmptyHunyuanVideo15Latent - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/EmptyHunyuanVideo15Latent/

Hunyuan Video

# EmptyHunyuanVideo15Latent - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node creates an empty latent tensor specifically formatted for use with the HunyuanVideo 1.5 model.

Copy pageCopy page

This node creates an empty latent tensor specifically formatted for use with the HunyuanVideo 1.5 model. It generates a blank starting point for video generation by allocating a tensor of zeros with the correct channel count and spatial dimensions for the model’s latent space.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`width`| The width of the video frame in pixels.| INT| Yes| -  
`height`| The height of the video frame in pixels.| INT| Yes| -  
`length`| The number of frames in the video sequence.| INT| Yes| -  
`batch_size`| The number of video samples to generate in a batch (default: 1).| INT| No| -  
  
**Note:** The spatial dimensions of the generated latent tensor are calculated by dividing the input `width` and `height` by 16 (this node uses a spatial scale factor of 16 rather than 8). The temporal dimension (frames) is calculated as `((length - 1) // 4) + 1`. These calculations use integer division, so `width` and `height` should be multiples of 16 to avoid truncation.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`samples`| An empty latent tensor with dimensions suitable for the HunyuanVideo 1.5 model. The tensor has a shape of `[batch_size, 32, ((length - 1) // 4) + 1, height // 16, width // 16]`. The output also includes a `downscale_ratio_spacial` value of 16.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanVideo15Latent/en.md)

* * *

**Source fingerprint (SHA-256):** `ce7ec75e8433c778d175a3e2ea260a4397aa5507428908b9a32f50fbe9e184c6`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/EmptyHunyuanVideo15Latent.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/EmptyHunyuanVideo15Latent)

[EmptyHunyuanLatentVideo - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/EmptyHunyuanLatentVideo)[HunyuanVideo15LatentUpscaleWithModel - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/HunyuanVideo15LatentUpscaleWithModel)

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
