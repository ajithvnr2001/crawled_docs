---
url: https://docs.comfy.org/built-in-nodes/ZImageFunControlnet/
title: ZImageFunControlnet - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:27.224176+00:00
---

# ZImageFunControlnet - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ZImageFunControlnet/

Patch

# ZImageFunControlnet - ComfyUI Built-in Node Documentation

Copy pageCopy page

ZImageFunControlnet applies a control network patch to a base model so it can guide the image generation or editing process.

Copy pageCopy page

ZImageFunControlnet applies a control network patch to a base model so it can guide the image generation or editing process. It combines a model, a model patch, and a VAE, and lets you control how strongly the control effect influences the result. Optional image, inpainting image, and mask inputs allow more targeted edits. The node works with Z-Image ControlNet patches and with Qwen Image 2.1 Fun ControlNet patches loaded through the Load Model Patch node.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The base model used for the generation process.| MODEL| Yes| -  
`model_patch`| A specialized patch model that applies the control network’s guidance.| MODEL_PATCH| Yes| -  
`vae`| The Variational Autoencoder used for encoding and decoding images.| VAE| Yes| -  
`strength`| The strength of the control network’s influence. Positive values apply the effect, while negative values can invert it (default: 1.0).| FLOAT| Yes| -10.0 to 10.0 (step 0.01)  
`image`| An optional base image to guide the generation process.| IMAGE| No| -  
`inpaint_image`| An optional image used specifically for inpainting areas defined by a mask.| IMAGE| No| -  
`mask`| An optional mask that defines which areas of an image should be edited or inpainted.| MASK| No| -  
`start_percent`| The point in the denoising process, as a fraction of the total sampling steps, where the control network starts taking effect (default: 0.0).| FLOAT| No| 0.0 to 1.0 (step 0.001)  
`end_percent`| The point in the denoising process where the control network stops taking effect (default: 1.0).| FLOAT| No| 0.0 to 1.0 (step 0.001)  
  
**Note:** The `inpaint_image` parameter is typically used in conjunction with a `mask` to specify the content for inpainting. The node’s behavior may change based on which optional inputs are provided (e.g., using `image` for guidance or using `image`, `mask`, and `inpaint_image` for inpainting). The `start_percent` and `end_percent` values restrict the control network to a window of the denoising process, and outside that window the model is sampled without the patch. If `strength` is 0, or if none of `image`, `inpaint_image`, and `mask` is connected, the node returns the base model unchanged. For Z-Image Control patches a provided mask is inverted (1.0 - mask) before use, while a Qwen Image 2.1 Fun ControlNet patch uses the mask as given. This node is flagged as experimental.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| The model with the control network patch applied, ready for use in a sampling pipeline.| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ZImageFunControlnet/en.md)

* * *

**Source fingerprint (SHA-256):** `9673b8b6e091713bcc93fe5fd1cfed12e6941571d1017e10ac94c19e1afd4ca1`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ZImageFunControlnet.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ZImageFunControlnet)

[ScaleROPE - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ScaleROPE)[APG - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/APG)

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
