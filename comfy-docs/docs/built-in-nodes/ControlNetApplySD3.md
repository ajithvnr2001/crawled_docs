---
url: https://docs.comfy.org/built-in-nodes/ControlNetApplySD3/
title: ControlNetApplySD3 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:43.722617+00:00
---

# ControlNetApplySD3 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ControlNetApplySD3/

Controlnet

# ControlNetApplySD3 - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node applies ControlNet guidance to Stable Diffusion 3 conditioning.

Copy pageCopy page

This node applies ControlNet guidance to Stable Diffusion 3 conditioning. It takes positive and negative conditioning inputs along with a ControlNet model and an image, then applies the control guidance with adjustable strength and timing parameters to influence the generation process. **Note:** This node has been marked as deprecated and may be removed in future versions.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`positive`| The positive conditioning to apply ControlNet guidance to| CONDITIONING| Yes| -  
`negative`| The negative conditioning to apply ControlNet guidance to| CONDITIONING| Yes| -  
`control_net`| The ControlNet model to use for guidance| CONTROL_NET| Yes| -  
`vae`| The VAE model used in the process| VAE| Yes| -  
`image`| The input image that ControlNet will use as guidance| IMAGE| Yes| -  
`strength`| The strength of the ControlNet effect (default: 1.0). When set to 0.0, the node skips ControlNet application and returns the conditioning unchanged.| FLOAT| Yes| 0.0 - 10.0  
`start_percent`| The starting point in the generation process where ControlNet begins to apply (default: 0.0)| FLOAT| Yes| 0.0 - 1.0  
`end_percent`| The ending point in the generation process where ControlNet stops applying (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
  
**Note:** When `strength` is set to 0.0, no ControlNet guidance is applied and the input conditioning is passed through unchanged to both outputs. **Note:** If the same conditioning is reused elsewhere and already contains control information, the new ControlNet is linked after the previous one, so multiple ControlNets can be applied in sequence.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| The modified positive conditioning with ControlNet guidance applied| CONDITIONING  
`negative`| The modified negative conditioning with ControlNet guidance applied| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApplySD3/en.md)

* * *

**Source fingerprint (SHA-256):** `b76b0683c05e38102280ca8b0bd23f39a9b9b1b4f52125c77c95686c0a06f398`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ControlNetApplySD3.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ControlNetApplySD3)

[ControlNetApplyAdvanced - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ControlNetApplyAdvanced)[ControlNetInpaintingAliMamaApply - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ControlNetInpaintingAliMamaApply)

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
