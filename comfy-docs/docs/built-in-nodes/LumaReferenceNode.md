---
url: https://docs.comfy.org/built-in-nodes/LumaReferenceNode/
title: LumaReferenceNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:28.191479+00:00
---

# LumaReferenceNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LumaReferenceNode/

Luma

# LumaReferenceNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node holds an image and weight value for use with the Luma Generate Image node.

Copy pageCopy page

This node holds an image and weight value for use with the Luma Generate Image node. It creates a reference chain that can be passed to other Luma nodes to influence image generation. The node can either start a new reference chain or add to an existing one.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| Image to use as reference.| IMAGE| Yes| -  
`weight`| Weight of image reference (default: 1.0).| FLOAT| Yes| 0.0 - 1.0  
`luma_ref`| Optional existing Luma reference chain to add to.| LUMA_REF| No| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`luma_ref`| The Luma reference chain containing the image and weight.| LUMA_REF  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaReferenceNode/en.md)

* * *

**Source fingerprint (SHA-256):** `f7e7789f2f19cac41cb9e55d21f10fef3012b10dcdbd59eb79f97fe5c2a944b7`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LumaReferenceNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LumaReferenceNode)

[LumaImageNode2 - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LumaImageNode2)[MagnificImageRelightNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/MagnificImageRelightNode)

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
