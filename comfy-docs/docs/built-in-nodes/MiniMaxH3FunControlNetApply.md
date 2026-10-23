---
url: https://docs.comfy.org/built-in-nodes/MiniMaxH3FunControlNetApply/
title: MiniMaxH3FunControlNetApply - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:32.930465+00:00
---

# MiniMaxH3FunControlNetApply - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MiniMaxH3FunControlNetApply/

Minimax

# MiniMaxH3FunControlNetApply - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node applies a MiniMax H3 Fun ControlNet to a text-to-video model as a model patch.

Copy pageCopy page

This node applies a MiniMax H3 Fun ControlNet to a text-to-video model as a model patch. It can use an optional control video and an optional mask to steer generation, and it returns a patched copy of the model for further sampling. When the strength is set to 0, or when neither a control video nor a mask is provided, the input model is returned unchanged.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The diffusion model to which the MiniMax H3 Fun ControlNet patch is applied.| MODEL| Yes| N/A  
`model_patch`| The MiniMax H3 Fun ControlNet patch whose control signals are injected into the model; it must be compatible with the given `model`.| MODEL_PATCH| Yes| N/A  
`vae`| VAE used to encode the control and source video frames into the latent space expected by the model.| VAE| Yes| N/A  
`strength`| Overall strength of the ControlNet effect. When set to 0, the node does nothing and returns the input model unchanged. (default: 1.0)| FLOAT| Yes| min 0.0, max 10.0, step 0.01  
`start_percent`| Start of the sampling range, expressed as a percentage of the sampling schedule, during which the ControlNet is active. It is converted internally to the equivalent sigma value. This is an advanced setting. (default: 0.0)| FLOAT| Yes| min 0.0, max 1.0, step 0.001  
`end_percent`| End of the sampling range, expressed as a percentage of the sampling schedule, during which the ControlNet is active. It is converted internally to the equivalent sigma value. This is an advanced setting. (default: 1.0)| FLOAT| Yes| min 0.0, max 1.0, step 0.001  
`control_video`| Optional video frames used as the ControlNet visual hint. The frames are resized to match the generated video and encoded with the `vae`.| IMAGE| No| N/A  
`mask`| 1 marks the regions to regenerate. Mask values above 0.5 are treated as marked regions.| MASK| No| N/A  
`source_video`| Video behind the mask; only read when a mask is given.| IMAGE| No| N/A  
  
Note: For the patch to have an effect, `strength` must be greater than 0 and at least one of `control_video` or `mask` must be supplied. `source_video` is ignored unless `mask` is provided; if `mask` is given without `source_video`, the content behind the masked regions is treated as black. When both `control_video` and `mask` are provided, the control hint combines the control video features with the masked source content.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| A patched clone of the input model with the MiniMax H3 Fun ControlNet applied. If `strength` is 0, or no control video or mask is supplied, the original model is returned unchanged.| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3FunControlNetApply/en.md)

* * *

**Source fingerprint (SHA-256):** `e907fb8e5ae60663d1d10b315985695ee5d49397fef6bd76b0e723637457a74a`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MiniMaxH3FunControlNetApply.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MiniMaxH3FunControlNetApply)

[ModelSamplingLTXV - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ModelSamplingLTXV)[MiniMaxH3SigmaShift - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/MiniMaxH3SigmaShift)

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
