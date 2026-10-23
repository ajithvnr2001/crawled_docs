---
url: https://docs.comfy.org/built-in-nodes/LatentComposite/
title: LatentComposite - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:20.264591+00:00
---

# LatentComposite - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LatentComposite/

Latent

# LatentComposite - ComfyUI Built-in Node Documentation

Copy pageCopy page

The LatentComposite node is designed to blend or merge two latent representations into a single output.

Copy pageCopy page

The LatentComposite node is designed to blend or merge two latent representations into a single output. This process is essential for creating composite images or features by combining the characteristics of the input latents in a controlled manner.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`samples_to`| The ‘samples_to’ latent representation where the ‘samples_from’ will be composited onto. It serves as the base for the composite operation.| `LATENT`  
`samples_from`| The ‘samples_from’ latent representation to be composited onto the ‘samples_to’. It contributes its features or characteristics to the final composite output.| `LATENT`  
`x`| The x-coordinate (horizontal position) where the ‘samples_from’ latent will be placed on the ‘samples_to’. It determines the horizontal alignment of the composite.| `INT`  
`y`| The y-coordinate (vertical position) where the ‘samples_from’ latent will be placed on the ‘samples_to’. It determines the vertical alignment of the composite.| `INT`  
`feather`| A boolean indicating whether the ‘samples_from’ latent should be resized to match the ‘samples_to’ before compositing. This can affect the scale and proportion of the composite result.| `INT`  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`latent`| The output is a composite latent representation, blending the features of both ‘samples_to’ and ‘samples_from’ latents based on the specified coordinates and resizing option.| `LATENT`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentComposite/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LatentComposite.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LatentComposite)

[GetAudioLatentSize - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/GetAudioLatentSize)[LatentCompositeMasked - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LatentCompositeMasked)

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
