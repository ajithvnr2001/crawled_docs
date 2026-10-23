---
url: https://docs.comfy.org/built-in-nodes/EmptyFlux2LatentImage/
title: EmptyFlux2LatentImage - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:53.024108+00:00
---

# EmptyFlux2LatentImage - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/EmptyFlux2LatentImage/

FLUX

# EmptyFlux2LatentImage - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Empty Flux 2 Latent node creates a blank latent representation filled with zeros.

Copy pageCopy page

The Empty Flux 2 Latent node creates a blank latent representation filled with zeros. It is used as a starting point for the Flux model’s denoising process. The latent dimensions are taken from the input width and height, each divided by 16.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`width`| The width of the final image to generate. The latent width will be this value divided by 16. The default value is 1024.| INT| Yes| 16 to 16384  
`height`| The height of the final image to generate. The latent height will be this value divided by 16. The default value is 1024.| INT| Yes| 16 to 16384  
`batch_size`| The number of latent samples to generate in a single batch. The default value is 1.| INT| No| 1 to 4096  
  
**Note:** The `width` and `height` inputs use a step of 16, so they must be divisible by 16. This is because the node divides them by this factor to create the latent dimensions.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`samples`| A latent tensor filled with zeros. The shape is `[batch_size, 128, height // 16, width // 16]`.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyFlux2LatentImage/en.md)

* * *

**Source fingerprint (SHA-256):** `f8356568f0ab521a3f246d1f672492e74f9a2f449694961b913bd14a5f0f3878`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/EmptyFlux2LatentImage.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/EmptyFlux2LatentImage)

[EmptyCosmosLatentVideo - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/EmptyCosmosLatentVideo)[EmptyHiDreamO1LatentImage - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/EmptyHiDreamO1LatentImage)

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
