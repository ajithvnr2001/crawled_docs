---
url: https://docs.comfy.org/built-in-nodes/EasyCache/
title: EasyCache - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:51.203103+00:00
---

# EasyCache - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/EasyCache/

Debug

# EasyCache - ComfyUI Built-in Node Documentation

Copy pageCopy page

The EasyCache node adds a native caching system to a diffusion model that speeds up sampling by reusing results from previously computed steps instead

Copy pageCopy page

The EasyCache node adds a native caching system to a diffusion model that speeds up sampling by reusing results from previously computed steps instead of recomputing every step. It activates only between a configurable start and end point of the sampling process and skips steps when the estimated output change stays below a user-defined threshold. This is an experimental node intended for advanced debugging use.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The model to add EasyCache to.| MODEL| Yes| -  
`reuse_threshold`| The threshold for reusing cached steps (default: 0.2).| FLOAT| Yes| 0.0 - 3.0  
`start_percent`| The relative sampling step to begin use of EasyCache (default: 0.15).| FLOAT| Yes| 0.0 - 1.0  
`end_percent`| The relative sampling step to end use of EasyCache (default: 0.95).| FLOAT| Yes| 0.0 - 1.0  
`verbose`| Whether to log verbose information (default: False).| BOOLEAN| Yes| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| The model with EasyCache functionality added.| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EasyCache/en.md)

* * *

**Source fingerprint (SHA-256):** `3e10ac65f8df58ce8649fdf599e62bfb86f2d4166840bed5622c0aa2c419cd38`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/EasyCache.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/EasyCache)

[VoxelToMeshBasic - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/VoxelToMeshBasic)[LazyCache - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LazyCache)

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
