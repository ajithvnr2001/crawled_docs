---
url: https://docs.comfy.org/built-in-nodes/SkipLayerGuidanceSD3/
title: SkipLayerGuidanceSD3 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:02.898497+00:00
---

# SkipLayerGuidanceSD3 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SkipLayerGuidanceSD3/

Guidance

# SkipLayerGuidanceSD3 - ComfyUI Built-in Node Documentation

Copy pageCopy page

The SkipLayerGuidanceSD3 node enhances guidance towards detailed structure by applying an additional set of classifier-free guidance with skipped layers.

Copy pageCopy page

The SkipLayerGuidanceSD3 node enhances guidance towards detailed structure by applying an additional set of classifier-free guidance with skipped layers. This experimental implementation is inspired by Perturbed Attention Guidance and works by selectively bypassing certain layers during the negative conditioning process to improve structural details in the generated output.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The model to apply skip layer guidance to| MODEL| Yes| -  
`layers`| Comma-separated list of layer indices to skip (default: “7, 8, 9”)| STRING| Yes| -  
`scale`| The strength of the skip layer guidance effect (default: 3.0)| FLOAT| Yes| 0.0 - 10.0  
`start_percent`| The starting point of guidance application as a percentage of total steps (default: 0.01)| FLOAT| Yes| 0.0 - 1.0  
`end_percent`| The ending point of guidance application as a percentage of total steps (default: 0.15)| FLOAT| Yes| 0.0 - 1.0  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| The modified model with skip layer guidance applied| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SkipLayerGuidanceSD3/en.md)

* * *

**Source fingerprint (SHA-256):** `8fba6e3037387e6beab64175099de1c96babdd492609099ba8ad3a49a6c34efe`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SkipLayerGuidanceSD3.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SkipLayerGuidanceSD3)

[SkipLayerGuidanceDiTSimple - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SkipLayerGuidanceDiTSimple)[TCFG - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/TCFG)

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
