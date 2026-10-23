---
url: https://docs.comfy.org/built-in-nodes/LTXVSpatioTemporalGuidance/
title: LTXVSpatioTemporalGuidance - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:19.692385+00:00
---

# LTXVSpatioTemporalGuidance - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LTXVSpatioTemporalGuidance/

Guidance

# LTXVSpatioTemporalGuidance - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node improves the spatial detail and motion coherence of LTXV video generation by running one extra pass at each sampling step.

Copy pageCopy page

This node improves the spatial detail and motion coherence of LTXV video generation by running one extra pass at each sampling step. During this pass, the self-attention of the selected transformer blocks is degraded to a value-passthrough, and the generation is guided away from that degraded result.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The base model to apply spatio-temporal guidance to. The model is cloned and a post-CFG guidance function is attached to the clone.| MODEL| Yes| —  
`scale`| The strength of the guidance applied to the denoised result. When set to 0, the guidance has no effect. (default: 1.0)| FLOAT| Yes| 0.0 to 100.0 (step 0.01)  
`blocks`| Comma-separated transformer block indices to perturb. Only numeric values are used; any other characters are ignored. (default: “29”)| STRING| Yes| —  
`start_percent`| The fraction of the sampling process at which guidance begins. This is an advanced parameter. (default: 0.0)| FLOAT| Yes| 0.0 to 1.0 (step 0.001)  
`end_percent`| The fraction of the sampling process at which guidance ends. This is an advanced parameter. (default: 1.0)| FLOAT| Yes| 0.0 to 1.0 (step 0.001)  
  
Note: Guidance is only applied during the sampling interval between `start_percent` and `end_percent`. Outside that interval, the original denoised result is returned unchanged. If `scale` is 0 or `blocks` contains no numeric values, the guided pass has no effect on the sampling process.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`MODEL`| The cloned model with the spatio-temporal guidance function attached.| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSpatioTemporalGuidance/en.md)

* * *

**Source fingerprint (SHA-256):** `0e14137b3bf416d36005b6b4b6db46495b1523f88b2bf574e2dc582175422a48`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LTXVSpatioTemporalGuidance.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LTXVSpatioTemporalGuidance)

[LTXVModalityGuidance - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LTXVModalityGuidance)[NAGuidance - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/NAGuidance)

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
