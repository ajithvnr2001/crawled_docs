---
url: https://docs.comfy.org/built-in-nodes/ControlNetInpaintingAliMamaApply/
title: ControlNetInpaintingAliMamaApply - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:43.937069+00:00
---

# ControlNetInpaintingAliMamaApply - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ControlNetInpaintingAliMamaApply/

Controlnet

# ControlNetInpaintingAliMamaApply - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ControlNetInpaintingAliMamaApply node applies ControlNet conditioning for inpainting tasks by combining positive and negative conditioning with a control

Copy pageCopy page

The ControlNetInpaintingAliMamaApply node applies ControlNet conditioning for inpainting tasks by combining positive and negative conditioning with a control image and mask. It processes the input image and mask to create modified conditioning that guides the generation process, allowing control over which areas of the image are inpainted. The node supports strength adjustment and timing controls to fine-tune the ControlNet’s influence during different stages of the generation process.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`positive`| The positive conditioning that guides the generation toward desired content| CONDITIONING| Yes| -  
`negative`| The negative conditioning that guides the generation away from unwanted content| CONDITIONING| Yes| -  
`control_net`| The ControlNet model that provides additional control over the generation| CONTROL_NET| Yes| -  
`vae`| The VAE (Variational Autoencoder) used for encoding and decoding images| VAE| Yes| -  
`image`| The input image that serves as control guidance for the ControlNet| IMAGE| Yes| -  
`mask`| The mask that defines which areas of the image should be inpainted| MASK| Yes| -  
`strength`| The strength of the ControlNet effect (default: 1.0, step: 0.01)| FLOAT| Yes| 0.0 to 10.0  
`start_percent`| Advanced parameter. The starting point (as percentage) of when ControlNet influence begins during generation (default: 0.0, step: 0.001)| FLOAT| Yes| 0.0 to 1.0  
`end_percent`| Advanced parameter. The ending point (as percentage) of when ControlNet influence stops during generation (default: 1.0, step: 0.001)| FLOAT| Yes| 0.0 to 1.0  
  
**Note:** When the ControlNet has `concat_mask` enabled, the mask is inverted and applied to the image before processing, and the inverted mask is included in the extra concatenation data sent to the ControlNet.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| The modified positive conditioning with ControlNet applied for inpainting| CONDITIONING  
`negative`| The modified negative conditioning with ControlNet applied for inpainting| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetInpaintingAliMamaApply/en.md)

* * *

**Source fingerprint (SHA-256):** `307b55c7b4936826b9e4424c172248fa4b41921c2362de724e5cfa2f1c25de68`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ControlNetInpaintingAliMamaApply.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ControlNetInpaintingAliMamaApply)

[ControlNetApplySD3 - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ControlNetApplySD3)[SetUnionControlNetType - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SetUnionControlNetType)

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
