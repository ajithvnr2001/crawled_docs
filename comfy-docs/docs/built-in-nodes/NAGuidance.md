---
url: https://docs.comfy.org/built-in-nodes/NAGuidance/
title: NAGuidance - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:38.229413+00:00
---

# NAGuidance - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/NAGuidance/

Guidance

# NAGuidance - ComfyUI Built-in Node Documentation

Copy pageCopy page

The NAGuidance node applies Normalized Attention Guidance to a model.

Copy pageCopy page

The NAGuidance node applies Normalized Attention Guidance to a model. This technique enables the use of negative prompts with distilled or schnell models by modifying the model’s attention mechanism during the sampling process to steer the generation away from undesired concepts.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The model to apply Normalized Attention Guidance to.| MODEL| Yes| -  
`nag_scale`| The guidance scale factor. Higher values push the generation further from the negative prompt. (default: 5.0)| FLOAT| Yes| 0.0 - 50.0  
`nag_alpha`| The blending factor for the normalized attention. A value of 1.0 fully replaces the original attention, while 0.0 has no effect. (default: 0.5)| FLOAT| Yes| 0.0 - 1.0  
`nag_tau`| A scaling factor used to limit the normalization ratio. (default: 1.5)| FLOAT| Yes| 1.0 - 10.0  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| The patched model with Normalized Attention Guidance enabled.| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NAGuidance/en.md)

* * *

**Source fingerprint (SHA-256):** `42b4d601312dcbb1c934c6a79bbb5e9fd6598fa5f32b18f5c0affcb596672cba`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/NAGuidance.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/NAGuidance)

[LTXVSpatioTemporalGuidance - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LTXVSpatioTemporalGuidance)[SkipLayerGuidanceDiT - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SkipLayerGuidanceDiT)

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
