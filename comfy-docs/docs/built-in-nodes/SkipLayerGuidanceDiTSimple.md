---
url: https://docs.comfy.org/built-in-nodes/SkipLayerGuidanceDiTSimple/
title: SkipLayerGuidanceDiTSimple - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:02.581942+00:00
---

# SkipLayerGuidanceDiTSimple - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SkipLayerGuidanceDiTSimple/

Guidance

# SkipLayerGuidanceDiTSimple - ComfyUI Built-in Node Documentation

Copy pageCopy page

Simple version of the SkipLayerGuidanceDiT node that only modifies the unconditional pass during the denoising process.

Copy pageCopy page

Simple version of the SkipLayerGuidanceDiT node that only modifies the unconditional pass during the denoising process. This node applies skip layer guidance to specific transformer layers in DiT (Diffusion Transformer) models by selectively skipping certain layers during the unconditional pass based on specified timing and layer parameters.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The model to apply skip layer guidance to| MODEL| Yes| -  
`double_layers`| Comma-separated list of double block layer indices to skip (default: “7, 8, 9”)| STRING| No| -  
`single_layers`| Comma-separated list of single block layer indices to skip (default: “7, 8, 9”)| STRING| No| -  
`start_percent`| The starting percentage of the denoising process when skip layer guidance begins (default: 0.0)| FLOAT| No| 0.0 - 1.0  
`end_percent`| The ending percentage of the denoising process when skip layer guidance stops (default: 1.0)| FLOAT| No| 0.0 - 1.0  
  
**Note:** Skip layer guidance is only applied when both `double_layers` and `single_layers` contain valid layer indices. If both are empty, the node returns the original model unchanged. The skip layer guidance is active only when the current denoising step’s sigma value falls between `start_percent` and `end_percent` (converted to sigma values internally).

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| The modified model with skip layer guidance applied to the specified layers| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SkipLayerGuidanceDiTSimple/en.md)

* * *

**Source fingerprint (SHA-256):** `f153348d75cf3b52d7d7d541f7467e51c797e1fe5844516591db7a191415cdb2`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SkipLayerGuidanceDiTSimple.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SkipLayerGuidanceDiTSimple)

[SkipLayerGuidanceDiT - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SkipLayerGuidanceDiT)[SkipLayerGuidanceSD3 - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SkipLayerGuidanceSD3)

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
