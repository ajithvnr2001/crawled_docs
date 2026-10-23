---
url: https://docs.comfy.org/built-in-nodes/WanUni3CControlnetApply/
title: WanUni3CControlnetApply - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-18T12:01:27.089954+00:00
---

# WanUni3CControlnetApply - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/WanUni3CControlnetApply/

Wan

# WanUni3CControlnetApply - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node applies a Uni3C ControlNet to a Wan video diffusion model, using a rendered guidance video (e.g.

Copy pageCopy page

## 

​

Overview

This node applies a Uni3C ControlNet to a Wan video diffusion model, using a rendered guidance video (e.g., warped point cloud renders) to influence the model’s output. It injects control signals at specific block layers, enabling camera-trajectory-based guidance during video generation.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The Wan diffusion model to patch.| MODEL| Yes| –  
`model_patch`| A Uni3C ControlNet patch (must be an instance of `comfy.ldm.wan.uni3c.WanUni3CControlnet`).| MODEL_PATCH| Yes| –  
`vae`| The VAE used to encode the guidance video into latents.| VAE| Yes| –  
`render_video`| The guidance video rendered from the camera trajectory, most commonly warped point cloud renders of the input image.| IMAGE| Yes| –  
`strength`| The strength of the control signal applied.| FLOAT| Yes| -10.0 to 10.0 (default: 1.0)  
`start_percent`| The percentage of the denoising process at which the control starts.| FLOAT| Yes| 0.0 to 1.0 (default: 0.0)  
`end_percent`| The percentage of the denoising process at which the control ends.| FLOAT| Yes| 0.0 to 1.0 (default: 1.0)  
  
**Notes:**

  * The `model_patch` must be a Uni3C ControlNet; otherwise the node raises an error.
  * The Uni3C ControlNet only works with Wan models; an error is raised if the model is not Wan-based.
  * The controlnet’s internal dimension must match the Wan model’s dimension – an error is raised if they differ.
  * The `render_video` input image is expected to be in RGB format (only the first 3 channels are used).
  * This node is experimental.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`MODEL`| The patched Wan model with the Uni3C ControlNet applied.| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanUni3CControlnetApply/en.md)

* * *

**Source fingerprint (SHA-256):** `f69253f06aba9208778f713ad36e9995f53a15d2e61243b853b9ac9131637371`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/WanUni3CControlnetApply.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/WanUni3CControlnetApply)

[WanContextWindowsManual - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/WanContextWindowsManual)[BlockSparseAttention - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/BlockSparseAttention)

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
