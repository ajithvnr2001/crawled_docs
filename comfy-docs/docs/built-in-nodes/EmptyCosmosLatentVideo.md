---
url: https://docs.comfy.org/built-in-nodes/EmptyCosmosLatentVideo/
title: EmptyCosmosLatentVideo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:52.651143+00:00
---

# EmptyCosmosLatentVideo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/EmptyCosmosLatentVideo/

Cosmos

# EmptyCosmosLatentVideo - ComfyUI Built-in Node Documentation

Copy pageCopy page

EmptyCosmosLatentVideo creates an empty latent video tensor with the specified dimensions.

Copy pageCopy page

EmptyCosmosLatentVideo creates an empty latent video tensor with the specified dimensions. It generates a zero-filled latent representation that can be used as a starting point for video generation workflows, with configurable width, height, length, and batch size parameters.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`width`| The width of the latent video in pixels (default: 1280, increments of 16)| INT| Yes| 16 to MAX_RESOLUTION  
`height`| The height of the latent video in pixels (default: 704, increments of 16)| INT| Yes| 16 to MAX_RESOLUTION  
`length`| The number of frames in the latent video (default: 121, increments of 8)| INT| Yes| 1 to MAX_RESOLUTION  
`batch_size`| The number of latent videos to generate in a batch (default: 1)| INT| No| 1 to 4096  
  
Note: The latent tensor is spatially downsampled by a factor of 8 in both height and width, and contains 16 channels. The number of latent temporal frames is calculated as `((length - 1) // 8) + 1`.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`samples`| The generated empty latent video tensor with zero values| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyCosmosLatentVideo/en.md)

* * *

**Source fingerprint (SHA-256):** `7ee194324b02367ed853f6d36bc51742081bac6a9469c4a619586e0560a1b33b`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/EmptyCosmosLatentVideo.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/EmptyCosmosLatentVideo)

[EmptyChromaRadianceLatentImage - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/EmptyChromaRadianceLatentImage)[EmptyFlux2LatentImage - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/EmptyFlux2LatentImage)

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
