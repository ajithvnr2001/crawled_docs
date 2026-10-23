---
url: https://docs.comfy.org/built-in-nodes/SkipLayerGuidanceDiT/
title: SkipLayerGuidanceDiT - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:02.477540+00:00
---

# SkipLayerGuidanceDiT - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SkipLayerGuidanceDiT/

Guidance

# SkipLayerGuidanceDiT - ComfyUI Built-in Node Documentation

Copy pageCopy page

Enhances guidance towards detailed structure by using another set of CFG negative with skipped layers.

Copy pageCopy page

Enhances guidance towards detailed structure by using another set of CFG negative with skipped layers. This generic version of SkipLayerGuidance can be used on every DiT model and is inspired by Perturbed Attention Guidance. The original experimental implementation was created for SD3.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The model to apply skip layer guidance to| MODEL| Yes| -  
`double_layers`| Comma-separated layer numbers for double blocks to skip (default: “7, 8, 9”)| STRING| Yes| -  
`single_layers`| Comma-separated layer numbers for single blocks to skip (default: “7, 8, 9”)| STRING| Yes| -  
`scale`| Guidance scale factor (default: 3.0)| FLOAT| Yes| 0.0 - 10.0  
`start_percent`| Starting percentage for guidance application (default: 0.01)| FLOAT| Yes| 0.0 - 1.0  
`end_percent`| Ending percentage for guidance application (default: 0.15)| FLOAT| Yes| 0.0 - 1.0  
`rescaling_scale`| Rescaling scale factor to adjust the output magnitude (default: 0.0, meaning no rescaling)| FLOAT| Yes| 0.0 - 10.0  
  
**Note:** If both `double_layers` and `single_layers` are empty (contain no layer numbers), the node returns the original model without applying any guidance.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| The modified model with skip layer guidance applied| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SkipLayerGuidanceDiT/en.md)

* * *

**Source fingerprint (SHA-256):** `35ca97f87913d0efcbb502ca040a8f357da112b202184d8786f63acd76809808`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SkipLayerGuidanceDiT.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SkipLayerGuidanceDiT)

[NAGuidance - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/NAGuidance)[SkipLayerGuidanceDiTSimple - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SkipLayerGuidanceDiTSimple)

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
