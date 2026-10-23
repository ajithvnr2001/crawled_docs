---
url: https://docs.comfy.org/built-in-nodes/FreeU_V2/
title: FreeU_V2 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:58.445801+00:00
---

# FreeU_V2 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/FreeU_V2/

Unet

# FreeU_V2 - ComfyUI Built-in Node Documentation

Copy pageCopy page

FreeUV2 enhances image generation quality by applying frequency-based modifications to a diffusion model’s U-Net architecture.

Copy pageCopy page

FreeU_V2 enhances image generation quality by applying frequency-based modifications to a diffusion model’s U-Net architecture. It uses configurable scaling factors to adjust feature channels in different blocks, improving output without requiring additional training. The node works by patching the model’s output blocks and filtering high-frequency components of the hidden states.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The diffusion model to apply FreeU enhancement to| MODEL| Yes| -  
`b1`| Backbone feature scaling factor for the first block (default: 1.3)| FLOAT| Yes| 0.0 - 10.0  
`b2`| Backbone feature scaling factor for the second block (default: 1.4)| FLOAT| Yes| 0.0 - 10.0  
`s1`| Skip feature scaling factor for the first block (default: 0.9)| FLOAT| Yes| 0.0 - 10.0  
`s2`| Skip feature scaling factor for the second block (default: 0.2)| FLOAT| Yes| 0.0 - 10.0  
  
Note: `b1`, `b2`, `s1`, and `s2` are advanced parameters hidden by default in the node’s UI. They can be set in steps of 0.01 within the 0.0 - 10.0 range. `b1` and `s1` control the U-Net block with the most channels (four times the model’s base channel count), while `b2` and `s2` control the block with half as many channels (twice the base channel count).

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| The enhanced diffusion model with FreeU modifications applied| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreeU_V2/en.md)

* * *

**Source fingerprint (SHA-256):** `4cef2af9b04164a8ead25bea9c9bb3311be9224f2539a5cc6edbe97ad8465d65`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/FreeU_V2.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/FreeU_V2)

[FreeU - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/FreeU)[HyperTile - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/HyperTile)

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
