---
url: https://docs.comfy.org/built-in-nodes/TomePatchModel/
title: TomePatchModel - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:10.470752+00:00
---

# TomePatchModel - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/TomePatchModel/

Unet

# TomePatchModel - ComfyUI Built-in Node Documentation

Copy pageCopy page

TomePatchModel applies Token Merging (ToMe) to a diffusion model to reduce computational cost during inference.

Copy pageCopy page

TomePatchModel applies Token Merging (ToMe) to a diffusion model to reduce computational cost during inference. It works by merging similar tokens inside the model’s attention mechanism, so the model processes fewer tokens while keeping output quality largely intact.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The diffusion model to apply token merging to| MODEL| Yes| -  
`ratio`| The proportion of tokens to merge (default: 0.3). Higher values merge more tokens, which can give greater speedup but potentially lower quality.| FLOAT| Yes| 0.0 - 1.0  
  
Note: If the number of tokens in an attention block is small enough that no downsampling is needed, the merging functions are replaced with no-ops, and the model runs unchanged for that block.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| The modified model with token merging applied| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TomePatchModel/en.md)

* * *

**Source fingerprint (SHA-256):** `1202c0df17f357440cd156fa0920f70c18a318e32c41dc04cecff11613f0072f`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/TomePatchModel.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/TomePatchModel)

[TemporalScoreRescaling - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/TemporalScoreRescaling)[WanContextWindowsManual - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/WanContextWindowsManual)

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
