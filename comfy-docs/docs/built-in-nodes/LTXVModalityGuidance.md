---
url: https://docs.comfy.org/built-in-nodes/LTXVModalityGuidance/
title: LTXVModalityGuidance - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:19.357335+00:00
---

# LTXVModalityGuidance - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LTXVModalityGuidance/

Guidance

# LTXVModalityGuidance - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node applies cross-modal (audio-video) guidance to an LTXV-AV model.

Copy pageCopy page

This node applies cross-modal (audio-video) guidance to an LTXV-AV model. During sampling, it runs one extra forward pass per step with the audio-to-video and video-to-audio cross-attention connections disabled, then pushes the result toward the coupled prediction to strengthen audio-visual synchronization, such as lip-sync. The reference default for `modality_scale` is 3.0; setting it to 1.0 disables the extra pass, and it stacks with the dual-CFG guider and STG.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The base model to which modality guidance will be applied. It is cloned internally, leaving the original model unchanged.| MODEL| Yes| -  
`modality_scale`| Strength of the audio-video coupling guidance. Default is 3.0. Set to 1.0 to disable the extra forward pass.| FLOAT| Yes| 1.0 to 100.0 (default: 3.0)  
`start_percent`| The point in the sampling process, as a percentage from 0.0 to 1.0, at which modality guidance begins. This is an advanced parameter. Default is 0.0.| FLOAT| Yes| 0.0 to 1.0 (default: 0.0)  
`end_percent`| The point in the sampling process, as a percentage from 0.0 to 1.0, at which modality guidance ends. This is an advanced parameter. Default is 1.0.| FLOAT| Yes| 0.0 to 1.0 (default: 1.0)  
  
Guidance is applied only for sampling steps whose sigma values fall within the range defined by `start_percent` and `end_percent`. Outside this range, the node returns the denoised result unchanged. A `modality_scale` of 1.0 also disables the extra forward pass entirely.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| The cloned model with a post-CFG guidance function attached. This modified model applies modality guidance during sampling.| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVModalityGuidance/en.md)

* * *

**Source fingerprint (SHA-256):** `038be607c42e626a8a8f5fe336ee466d0847d43835edb71e20ff38f668069cfb`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LTXVModalityGuidance.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LTXVModalityGuidance)

[CFGZeroStar - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/CFGZeroStar)[LTXVSpatioTemporalGuidance - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LTXVSpatioTemporalGuidance)

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
