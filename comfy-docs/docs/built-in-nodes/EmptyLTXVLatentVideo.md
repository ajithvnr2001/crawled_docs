---
url: https://docs.comfy.org/built-in-nodes/EmptyLTXVLatentVideo/
title: EmptyLTXVLatentVideo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:53.438603+00:00
---

# EmptyLTXVLatentVideo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/EmptyLTXVLatentVideo/

Ltxv

# EmptyLTXVLatentVideo - ComfyUI Built-in Node Documentation

Copy pageCopy page

The EmptyLTXVLatentVideo node creates an empty (zero-filled) latent video tensor using the width, height, length, and batch size you specify.

Copy pageCopy page

The EmptyLTXVLatentVideo node creates an empty (zero-filled) latent video tensor using the width, height, length, and batch size you specify. It provides a blank starting point for LTXV video generation workflows, with the latent dimensions automatically compressed relative to the requested video size.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`width`| The width of the latent video tensor (default: 768, step: 32)| INT| Yes| 64 to MAX_RESOLUTION  
`height`| The height of the latent video tensor (default: 512, step: 32)| INT| Yes| 64 to MAX_RESOLUTION  
`length`| The number of frames in the latent video (default: 97, step: 8)| INT| Yes| 1 to MAX_RESOLUTION  
`batch_size`| The number of latent videos to generate in a batch (default: 1)| INT| Yes| 1 to 4096  
  
Note: The latent video is compressed compared to the requested dimensions: the spatial dimensions (width and height) are divided by 32, and the frame count (length) is divided by 8 and rounded up to the nearest whole number. The step values for width, height, and length help keep these divisions even.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`samples`| The generated empty latent tensor with zero values in the specified dimensions, along with a spatial downscale ratio of 32| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLTXVLatentVideo/en.md)

* * *

**Source fingerprint (SHA-256):** `0b1e57baf9730d852b03b6bccbb8a033e2be9b9cd2420a0aa3638c31f6d3cd26`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/EmptyLTXVLatentVideo.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/EmptyLTXVLatentVideo)

[HunyuanVideo15LatentUpscaleWithModel - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/HunyuanVideo15LatentUpscaleWithModel)[LTXVAudioVAEDecode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LTXVAudioVAEDecode)

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
