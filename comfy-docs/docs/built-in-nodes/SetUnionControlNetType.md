---
url: https://docs.comfy.org/built-in-nodes/SetUnionControlNetType/
title: SetUnionControlNetType - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:02.070002+00:00
---

# SetUnionControlNetType - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SetUnionControlNetType/

Controlnet

# SetUnionControlNetType - ComfyUI Built-in Node Documentation

Copy pageCopy page

The SetUnionControlNetType node lets you choose which control type a control network uses.

Copy pageCopy page

The SetUnionControlNetType node lets you choose which control type a control network uses. It takes an existing control network and creates a modified copy with the selected control type, leaving the original control network unchanged. When “auto” is selected, the stored control type is cleared so the type can be detected automatically.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`control_net`| The control network to modify with a new type setting| CONTROL_NET| Yes| -  
`type`| The control network type to apply. Use “auto” for automatic type detection or select a specific control network type from the available options (default: “auto”)| COMBO| Yes| `"auto"`  
`"openpose"`  
`"depth"`  
`"hed/pidi/softedge"`  
`"canny"`  
`"scribble"`  
`"seg"`  
`"tile"`  
`"inpaint"`  
`"lineart"`  
`"blur"`  
`"mlsd"`  
`"normalbae"`  
`"mask"`  
  
When `type` is set to `"auto"`, the node clears the stored control type so the type can be detected automatically. When a specific type is selected, the node stores the matching control type in the copied control network. The input control network is never changed in place; a modified copy is returned instead.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`control_net`| The modified control network with the specified type setting applied| CONTROL_NET  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetUnionControlNetType/en.md)

* * *

**Source fingerprint (SHA-256):** `db4b1a3cebafcff2be3172faa09cecbd5e19331376491c491cbe359013ed3da3`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SetUnionControlNetType.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SetUnionControlNetType)

[ControlNetInpaintingAliMamaApply - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ControlNetInpaintingAliMamaApply)[CosmosImageToVideoLatent - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/CosmosImageToVideoLatent)

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
