---
url: https://docs.comfy.org/built-in-nodes/SUPIRApply/
title: SUPIRApply - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:55.574121+00:00
---

# SUPIRApply - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SUPIRApply/

Supir

# SUPIRApply - ComfyUI Built-in Node Documentation

Copy pageCopy page

The SUPIRApply node applies a SUPIR model patch to a diffusion model.

Copy pageCopy page

The SUPIRApply node applies a SUPIR model patch to a diffusion model. It uses the patch to modify the model’s behavior, allowing it to incorporate guidance from an input image during the sampling process. The node also provides controls for adjusting the strength of this guidance over time and includes an optional feature to help maintain fidelity to the original input.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The base diffusion model to which the SUPIR patch will be applied.| MODEL| Yes| -  
`model_patch`| The SUPIR model patch containing the weights and configuration for modifying the model.| MODEL_PATCH| Yes| -  
`vae`| The VAE (Variational Autoencoder) used for encoding the input image into a latent representation.| VAE| Yes| -  
`image`| The input image used to guide the generation process. Only the first three color channels (RGB) are used.| IMAGE| Yes| -  
`strength_start`| Control strength at the start of sampling (high sigma). The influence of the image guidance begins at this value. (default: 1.0)| FLOAT| Yes| 0.0 - 10.0  
`strength_end`| Control strength at the end of sampling (low sigma). Linearly interpolated from start. The influence of the image guidance ends at this value. (default: 1.0)| FLOAT| Yes| 0.0 - 10.0  
`restore_cfg`| Pulls denoised output toward the input latent. Higher = stronger fidelity to input. 0 to disable. (default: 4.0, advanced setting)| FLOAT| Yes| 0.0 - 20.0  
`restore_cfg_s_tmin`| Sigma threshold below which `restore_cfg` is disabled. (default: 0.05, advanced setting)| FLOAT| Yes| 0.0 - 1.0  
  
_Note:_ The `image` input is processed to extract only the RGB channels. If an image with an alpha channel is provided, the alpha channel is ignored. _Note:_ If the SUPIR model patch provides denoise encoder weights, the input image is encoded with those weights instead of the regular VAE encoder. _Note:_ `restore_cfg` only takes effect when set to a value greater than 0. Setting it to 0 disables the restore post-processing entirely. When active, the correction is applied only while the current sigma value is above `restore_cfg_s_tmin`. _Note:_ This node is marked as experimental in ComfyUI.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| A cloned copy of the input model with the SUPIR patch applied and any additional post-CFG functions configured.| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SUPIRApply/en.md)

* * *

**Source fingerprint (SHA-256):** `fa9f67f63777160863c44c620d8de11e92f79245c3f5b60e138975dfd0cc65c7`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SUPIRApply.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SUPIRApply)

[ModelSamplingSD3 - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ModelSamplingSD3)[Epsilon Scaling - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Epsilon%20Scaling)

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
