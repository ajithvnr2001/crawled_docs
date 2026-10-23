---
url: https://docs.comfy.org/built-in-nodes/GrowMask/
title: GrowMask - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:02.169082+00:00
---

# GrowMask - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/GrowMask/

Mask

# GrowMask - ComfyUI Built-in Node Documentation

Copy pageCopy page

The GrowMask node is designed to modify the size of a given mask, either expanding or contracting it

Copy pageCopy page

The `GrowMask` node is designed to modify the size of a given mask, either expanding or contracting it, while optionally applying a tapered effect to the corners. This functionality is crucial for dynamically adjusting mask boundaries in image processing tasks, allowing for more flexible and precise control over the area of interest.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`mask`| The input mask to be modified. This parameter is central to the node’s operation, serving as the base upon which the mask is either expanded or contracted.| MASK  
`expand`| Determines the magnitude and direction of the mask modification. Positive values cause the mask to expand, while negative values lead to contraction. This parameter directly influences the final size of the mask.| INT  
`tapered_corners`| A boolean flag that, when set to True, applies a tapered effect to the corners of the mask during modification. This option allows for smoother transitions and visually appealing results.| BOOLEAN  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`mask`| The modified mask after applying the specified expansion/contraction and optional tapered corners effect.| MASK  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrowMask/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/GrowMask.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/GrowMask)

[FeatherMask - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/FeatherMask)[ImageColorToMask - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ImageColorToMask)

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
