---
url: https://docs.comfy.org/built-in-nodes/LatentCompositeMasked/
title: LatentCompositeMasked - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:20.550873+00:00
---

# LatentCompositeMasked - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LatentCompositeMasked/

Latent

# LatentCompositeMasked - ComfyUI Built-in Node Documentation

Copy pageCopy page

The LatentCompositeMasked node is designed for blending two latent representations together at specified coordinates

Copy pageCopy page

The LatentCompositeMasked node is designed for blending two latent representations together at specified coordinates, optionally using a mask for more controlled compositing. This node enables the creation of complex latent images by overlaying parts of one image onto another, with the ability to resize the source image for a perfect fit.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`destination`| The latent representation onto which another latent representation will be composited. Acts as the base layer for the composite operation.| `LATENT`  
`source`| The latent representation to be composited onto the destination. This source layer can be resized and positioned according to the specified parameters.| `LATENT`  
`x`| The x-coordinate in the destination latent representation where the source will be placed. Allows for precise positioning of the source layer.| `INT`  
`y`| The y-coordinate in the destination latent representation where the source will be placed, enabling accurate overlay positioning.| `INT`  
`resize_source`| A boolean flag indicating whether the source latent representation should be resized to match the destination’s dimensions before compositing.| `BOOLEAN`  
`mask`| An optional mask that can be used to control the blending of the source onto the destination. The mask defines which parts of the source will be visible in the final composite.| `MASK`  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`latent`| The resulting latent representation after compositing the source onto the destination, potentially using a mask for selective blending.| `LATENT`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCompositeMasked/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LatentCompositeMasked.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LatentCompositeMasked)

[LatentComposite - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LatentComposite)[LatentUpscale - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LatentUpscale)

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
