---
url: https://docs.comfy.org/built-in-nodes/FeatherMask/
title: FeatherMask - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:55.034253+00:00
---

# FeatherMask - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/FeatherMask/

Mask

# FeatherMask - ComfyUI Built-in Node Documentation

Copy pageCopy page

The FeatherMask node applies a feathering effect to the edges of a given mask

Copy pageCopy page

The `FeatherMask` node applies a feathering effect to the edges of a given mask, smoothly transitioning the mask’s edges by adjusting their opacity based on specified distances from each edge. This creates a softer, more blended edge effect.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`mask`| The mask to which the feathering effect will be applied. It determines the area of the image that will be affected by the feathering.| MASK  
`left`| Specifies the distance from the left edge within which the feathering effect will be applied.| INT  
`top`| Specifies the distance from the top edge within which the feathering effect will be applied.| INT  
`right`| Specifies the distance from the right edge within which the feathering effect will be applied.| INT  
`bottom`| Specifies the distance from the bottom edge within which the feathering effect will be applied.| INT  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`mask`| The output is a modified version of the input mask with a feathering effect applied to its edges.| MASK  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FeatherMask/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/FeatherMask.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/FeatherMask)

[CropMask - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/CropMask)[GrowMask - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/GrowMask)

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
