---
url: https://docs.comfy.org/built-in-nodes/CFGGuider/
title: CFGGuider - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:31.472759+00:00
---

# CFGGuider - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/CFGGuider/

Guiders

# CFGGuider - ComfyUI Built-in Node Documentation

Copy pageCopy page

The CFG Guider node creates a guidance system for controlling the sampling process in image generation.

Copy pageCopy page

The CFG Guider node creates a guidance system for controlling the sampling process in image generation. It takes a model along with positive and negative conditioning inputs, then applies a classifier-free guidance scale to steer the generation toward desired content while avoiding unwanted elements. This node outputs a guider object that can be used by sampling nodes to control the image generation direction.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The model to be used for guidance| MODEL| Yes| -  
`positive`| The positive conditioning that guides the generation toward desired content| CONDITIONING| Yes| -  
`negative`| The negative conditioning that steers the generation away from unwanted content| CONDITIONING| Yes| -  
`cfg`| The classifier-free guidance scale that controls how strongly the conditioning influences the generation (default: 8.0)| FLOAT| Yes| 0.0 to 100.0 (step: 0.1)  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`GUIDER`| A guider object that can be passed to sampling nodes to control the generation process| GUIDER  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGGuider/en.md)

* * *

**Source fingerprint (SHA-256):** `73b57bfbb6d4fc083a8089bc0f786f82d03e0d7b2faeeb7a42b3d87e38047b9e`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/CFGGuider.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/CFGGuider)

[BasicGuider - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/BasicGuider)[CFGOverride - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/CFGOverride)

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
