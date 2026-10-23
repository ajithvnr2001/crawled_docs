---
url: https://docs.comfy.org/built-in-nodes/PerpNegGuider/
title: PerpNegGuider - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:41.355251+00:00
---

# PerpNegGuider - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/PerpNegGuider/

Experimental

# PerpNegGuider - ComfyUI Built-in Node Documentation

Copy pageCopy page

The PerpNegGuider node creates a guidance system for controlling image generation using perpendicular negative conditioning.

Copy pageCopy page

The PerpNegGuider node creates a guidance system for controlling image generation using perpendicular negative conditioning. It takes positive, negative, and empty conditioning inputs and applies a specialized guidance algorithm that computes all three noise predictions in a single batch for efficiency. This node is designed for experimental testing and provides fine control over the guidance strength and negative scaling.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The model to use for guidance generation| MODEL| Yes| -  
`positive`| The positive conditioning that guides the generation toward desired content| CONDITIONING| Yes| -  
`negative`| The negative conditioning that guides the generation away from unwanted content| CONDITIONING| Yes| -  
`empty_conditioning`| The empty or neutral conditioning used as a baseline reference for perpendicular negative guidance| CONDITIONING| Yes| -  
`cfg`| The classifier-free guidance scale that controls how strongly the conditioning influences the generation (default: 8.0)| FLOAT| Yes| 0.0 - 100.0  
`neg_scale`| The negative scaling factor that adjusts the strength of the perpendicular negative effect (default: 1.0)| FLOAT| Yes| 0.0 - 100.0  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`guider`| A configured guidance system ready for use in the generation pipeline| GUIDER  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerpNegGuider/en.md)

* * *

**Source fingerprint (SHA-256):** `02e4b4e0ea413da31c280cb1e510bdf5caa7b5187eb6de94632e45a91e881820`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/PerpNegGuider.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/PerpNegGuider)

[PerpNeg - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/PerpNeg)[SamplerEulerCFGpp - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SamplerEulerCFGpp)

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
