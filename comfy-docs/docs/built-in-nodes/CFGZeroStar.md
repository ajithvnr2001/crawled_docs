---
url: https://docs.comfy.org/built-in-nodes/CFGZeroStar/
title: CFGZeroStar - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:31.777991+00:00
---

# CFGZeroStar - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/CFGZeroStar/

Guidance

# CFGZeroStar - ComfyUI Built-in Node Documentation

Copy pageCopy page

The CFGZeroStar node applies a specialized guidance scaling technique to diffusion models.

Copy pageCopy page

The CFGZeroStar node applies a specialized guidance scaling technique to diffusion models. It modifies the classifier-free guidance process by calculating an optimized scale factor based on the difference between conditional and unconditional predictions. This approach adjusts the final output to provide enhanced control over the generation process while maintaining model stability.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The diffusion model to be modified with the CFGZeroStar guidance scaling technique| MODEL| Yes| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`patched_model`| The modified model with CFGZeroStar guidance scaling applied| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGZeroStar/en.md)

* * *

**Source fingerprint (SHA-256):** `4ec70f67eed8aaca964ce3dfb5b650af2f44d34bcde3b74c3886c91e1e8e8cc0`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/CFGZeroStar.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/CFGZeroStar)

[CFGNorm - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/CFGNorm)[LTXVModalityGuidance - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LTXVModalityGuidance)

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
