---
url: https://docs.comfy.org/built-in-nodes/EmptyTrellis2LatentStructure/
title: EmptyTrellis2LatentStructure - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:54.710490+00:00
---

# EmptyTrellis2LatentStructure - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/EmptyTrellis2LatentStructure/

Trellis

# EmptyTrellis2LatentStructure - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node creates an empty latent structure for the Trellis2 model, where all values are set to zero.

Copy pageCopy page

This node creates an empty latent structure for the Trellis2 model, where all values are set to zero. It produces a blank 3D latent tensor with 32 channels at a resolution of 16×16×16, sized for the specified number of items in the batch.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`batch_size`| The number of latent images in the batch (default: 1).| INT| Yes| 1 to 4096  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`LATENT`| An empty Trellis2 latent structure. The samples are a zero-filled tensor with the shape (batch_size, 32, 16, 16, 16), and the latent type is set to “trellis2”.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyTrellis2LatentStructure/en.md)

* * *

**Source fingerprint (SHA-256):** `a551f0e05e58b025df03a3babee36f57fd900b5e02926fbdbd67a512ebead078`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/EmptyTrellis2LatentStructure.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/EmptyTrellis2LatentStructure)

[LatentRotate - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LatentRotate)[VaeDecodeShapeTrellis - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/VaeDecodeShapeTrellis)

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
