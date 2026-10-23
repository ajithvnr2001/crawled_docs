---
url: https://docs.comfy.org/built-in-nodes/MaskComposite/
title: MaskComposite - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:29.844422+00:00
---

# MaskComposite - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MaskComposite/

Mask

# MaskComposite - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node specializes in combining two mask inputs through a variety of operations such as addition, subtraction, and logical operations, to produce a new

Copy pageCopy page

This node specializes in combining two mask inputs through a variety of operations such as addition, subtraction, and logical operations, to produce a new, modified mask. It abstractly handles the manipulation of mask data to achieve complex masking effects, serving as a crucial component in mask-based image editing and processing workflows.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`destination`| The primary mask that will be modified based on the operation with the source mask. It plays a central role in the composite operation, acting as the base for modifications.| MASK  
`source`| The secondary mask that will be used in conjunction with the destination mask to perform the specified operation, influencing the final output mask.| MASK  
`x`| The horizontal offset at which the source mask will be applied to the destination mask, affecting the positioning of the composite result.| INT  
`y`| The vertical offset at which the source mask will be applied to the destination mask, affecting the positioning of the composite result.| INT  
`operation`| Specifies the type of operation to apply between the destination and source masks, such as ‘add’, ‘subtract’, or logical operations, determining the nature of the composite effect.| COMBO[STRING]  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`mask`| The resulting mask after applying the specified operation between the destination and source masks, representing the composite outcome.| MASK  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MaskComposite/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MaskComposite.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MaskComposite)

[InvertMask - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/InvertMask)[MaskPreview - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/MaskPreview)

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
