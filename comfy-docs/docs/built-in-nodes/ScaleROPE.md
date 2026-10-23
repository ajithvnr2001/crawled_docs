---
url: https://docs.comfy.org/built-in-nodes/ScaleROPE/
title: ScaleROPE - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:00.588690+00:00
---

# ScaleROPE - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ScaleROPE/

Patch

# ScaleROPE - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ScaleROPE node allows you to modify the Rotary Position Embedding (ROPE) of a model by applying separate scaling and shifting factors to its X, Y

Copy pageCopy page

The ScaleROPE node allows you to modify the Rotary Position Embedding (ROPE) of a model by applying separate scaling and shifting factors to its X, Y, and T (time) components. It is an advanced, experimental node used to adjust the model’s positional encoding behavior.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The model whose ROPE parameters will be modified.| MODEL| Yes| -  
`scale_x`| The scaling factor to apply to the X component of the ROPE (default: 1.0).| FLOAT| Yes| 0.0 - 100.0 (step 0.1)  
`shift_x`| The shift value to apply to the X component of the ROPE (default: 0.0).| FLOAT| Yes| -256.0 - 256.0 (step 0.1)  
`scale_y`| The scaling factor to apply to the Y component of the ROPE (default: 1.0).| FLOAT| Yes| 0.0 - 100.0 (step 0.1)  
`shift_y`| The shift value to apply to the Y component of the ROPE (default: 0.0).| FLOAT| Yes| -256.0 - 256.0 (step 0.1)  
`scale_t`| The scaling factor to apply to the T (time) component of the ROPE (default: 1.0).| FLOAT| Yes| 0.0 - 100.0 (step 0.1)  
`shift_t`| The shift value to apply to the T (time) component of the ROPE (default: 0.0).| FLOAT| Yes| -256.0 - 256.0 (step 0.1)  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| The model with the new ROPE scaling and shifting parameters applied.| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ScaleROPE/en.md)

* * *

**Source fingerprint (SHA-256):** `5d5ab0182b78c8c12ceaf44685a91e666ce15fa099fd194e3605bbdb9cc3c961`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ScaleROPE.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ScaleROPE)

[RescaleCFG - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/RescaleCFG)[ZImageFunControlnet - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ZImageFunControlnet)

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
