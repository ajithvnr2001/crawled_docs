---
url: https://docs.comfy.org/built-in-nodes/AnimaLLLiteApply/
title: AnimaLLLiteApply - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:20.290964+00:00
---

# AnimaLLLiteApply - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/AnimaLLLiteApply/

Anima

# AnimaLLLiteApply - ComfyUI Built-in Node Documentation

Copy pageCopy page

AnimaLLLiteApply applies a lightweight animation patch to a diffusion model, enabling controlled image-to-image generation with adjustable strength and timing.

Copy pageCopy page

AnimaLLLiteApply applies a lightweight animation patch to a diffusion model, enabling controlled image-to-image generation with adjustable strength and timing. It integrates a pre-configured model patch with an input image and optional mask, modifying the model’s attention and MLP layers to influence the generation process.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The base diffusion model to apply the patch to| MODEL| Yes|   
`model_patch`| The pre-configured animation patch to apply| MODEL_PATCH| Yes|   
`image`| The reference image to guide the generation. Only the first 3 color channels (RGB) are used| IMAGE| Yes|   
`strength`| The strength of the patch effect (default: 1.0, step: 0.01)| FLOAT| Yes| -10.0 to 10.0  
`start_percent`| The percentage of the denoising process at which the patch starts taking effect (default: 0.0, step: 0.001)| FLOAT| Yes| 0.0 to 1.0  
`end_percent`| The percentage of the denoising process at which the patch stops taking effect (default: 1.0, step: 0.001)| FLOAT| Yes| 0.0 to 1.0  
`mask`| An optional mask to limit the patch effect to specific areas of the image| MASK| No|   
  
**Note on parameter constraints:** If the `model_patch` has 4 input channels and no `mask` is provided, a zero mask is automatically created to match the image dimensions. If the `model_patch` does not have 4 input channels, the `mask` parameter is ignored and set to `None`. Only the first 3 color channels of the input image are used. This node is marked as experimental in ComfyUI.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`MODEL`| The patched diffusion model with the animation patch applied| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AnimaLLLiteApply/en.md)

* * *

**Source fingerprint (SHA-256):** `48e455b767509a5a8c329365d5ffded86d6f4545d575c9fdc5ffbaf4da7c2287`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/AnimaLLLiteApply.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/AnimaLLLiteApply)

[VAESave - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/VAESave)[ChromaRadianceOptions - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ChromaRadianceOptions)

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
