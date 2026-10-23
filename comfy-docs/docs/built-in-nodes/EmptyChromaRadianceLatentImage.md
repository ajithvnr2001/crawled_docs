---
url: https://docs.comfy.org/built-in-nodes/EmptyChromaRadianceLatentImage/
title: EmptyChromaRadianceLatentImage - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:52.219084+00:00
---

# EmptyChromaRadianceLatentImage - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/EmptyChromaRadianceLatentImage/

Chroma Radiance

# EmptyChromaRadianceLatentImage - ComfyUI Built-in Node Documentation

Copy pageCopy page

The EmptyChromaRadianceLatentImage node creates a blank latent image with the dimensions you specify, for use in chroma radiance workflows.

Copy pageCopy page

The EmptyChromaRadianceLatentImage node creates a blank latent image with the dimensions you specify, for use in chroma radiance workflows. It produces a tensor filled with zeros that acts as the starting point for latent space operations, letting you define the width, height, and batch size of the empty latent image.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`width`| The width of the latent image in pixels (default: 1024)| INT| Yes| 16 to MAX_RESOLUTION  
`height`| The height of the latent image in pixels (default: 1024)| INT| Yes| 16 to MAX_RESOLUTION  
`batch_size`| The number of latent images to generate in a batch (default: 1)| INT| Yes| 1 to 4096  
  
Note: `width` and `height` are defined with a step of 16, so the values are adjusted in multiples of 16.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`samples`| The generated empty latent image tensor filled with zeros, with the shape batch_size x 3 x height x width| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyChromaRadianceLatentImage/en.md)

* * *

**Source fingerprint (SHA-256):** `870cc89fb021c258c214db153cda0a32a63da1b6bf92f09cbd3b8498c363096b`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/EmptyChromaRadianceLatentImage.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/EmptyChromaRadianceLatentImage)

[ReplaceVideoLatentFrames - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ReplaceVideoLatentFrames)[EmptyCosmosLatentVideo - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/EmptyCosmosLatentVideo)

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
