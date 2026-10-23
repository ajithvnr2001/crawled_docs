---
url: https://docs.comfy.org/built-in-nodes/EmptySD3LatentImage/
title: EmptySD3LatentImage - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:54.046825+00:00
---

# EmptySD3LatentImage - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/EmptySD3LatentImage/

Stable Diffusion

# EmptySD3LatentImage - ComfyUI Built-in Node Documentation

Copy pageCopy page

EmptySD3LatentImage creates a blank (all-zero) latent image in the layout that Stable Diffusion 3 models expect.

Copy pageCopy page

EmptySD3LatentImage creates a blank (all-zero) latent image in the layout that Stable Diffusion 3 models expect. Because the latent is empty, it is normally used as the starting point that a generation workflow fills in with an image. The width and height you choose determine the size of the final image.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`width`| The width of the latent image in pixels (default: 1024). Values are stepped in increments of 16.| INT| Yes| 16 to MAX_RESOLUTION (step: 16)  
`height`| The height of the latent image in pixels (default: 1024). Values are stepped in increments of 16.| INT| Yes| 16 to MAX_RESOLUTION (step: 16)  
`batch_size`| The number of latent images to generate in the batch (default: 1).| INT| Yes| 1 to 4096  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`LATENT`| A latent tensor containing blank (all-zero) samples in the SD3-compatible format. The tensor has 16 channels, is scaled down by a factor of 8 relative to `width` and `height`, and carries a spatial downscale ratio of 8.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptySD3LatentImage/en.md)

* * *

**Source fingerprint (SHA-256):** `694ede56f43e3f3889b4d23e636fa6b33b490bcbd214584557f0dc883fa0a32d`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/EmptySD3LatentImage.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/EmptySD3LatentImage)

[StableCascade_StageC_VAEEncode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/StableCascade_StageC_VAEEncode)[LatentCrop - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LatentCrop)

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
