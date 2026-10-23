---
url: https://docs.comfy.org/built-in-nodes/TextEncodeMageFlowEdit/
title: TextEncodeMageFlowEdit - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-18T12:01:26.949826+00:00
---

# TextEncodeMageFlowEdit - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/TextEncodeMageFlowEdit/

Mage

# TextEncodeMageFlowEdit - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node encodes an edit instruction (prompt) along with one or more reference images for the Mage-Flow-Edit model.

Copy pageCopy page

## 

​

Overview

This node encodes an edit instruction (prompt) along with one or more reference images for the Mage-Flow-Edit model. It resizes all reference images to the target output resolution, encodes them into latent space if a VAE is provided, and attaches the reference latents to the conditioning output. A blank latent tensor with the correct dimensions for sampling is also generated, ensuring the size always matches the output width and height.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`clip`| The CLIP model used to tokenize and encode the text prompts.| CLIP| Yes|   
`prompt`| The editing instruction (positive prompt) to apply.| STRING| Yes| multiline, dynamic prompts enabled  
`negative_prompt`| The negative prompt to steer away from. Default: empty string (uses a space internally when blank). Shown in the advanced section of the UI.| STRING| No| multiline, dynamic prompts enabled  
`vae`| VAE model to encode reference images into latent space. If not provided, no reference latents are added to the conditioning.| VAE| No|   
`images`| Reference image(s) to edit. All references are resized to the output resolution before encoding.| IMAGE (autogrow)| No| Up to 16 images (named `image_1`…`image_16`), at least 0  
`width`| Output width in pixels. If set to 0, the width of the first reference image is used. Always rounded down to a multiple of 16. Default: 0.| INT| Yes| 0 to 8192 (step 16)  
`height`| Output height in pixels. Same fallback behavior as width. Default: 0.| INT| Yes| 0 to 8192 (step 16)  
`batch_size`| Number of latent samples to generate. Default: 1.| INT| Yes| 1 to 4096  
  
**Notes on parameter dependencies:**

  * If `width` and/or `height` are 0 and no reference images are provided, they fall back to 1024 each.
  * If only one of `width` or `height` is 0, the missing dimension is taken from the first reference image while the explicitly set dimension is kept.
  * The `vae` parameter is optional; reference latents are only generated and attached to conditioning when a VAE is connected.
  * The `negative_prompt` field is optional – if left empty, a single space is used internally as the negative text.
  * For the text conditioning, each reference image is resized so its longest edge is at most 384 pixels, matching training preprocessing. The VAE encoding branch instead resizes all references to the full output resolution.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| Conditioning output containing the positive prompt tokens, plus (if a VAE was provided) the encoded reference latents.| CONDITIONING  
`negative`| Conditioning output containing the negative prompt tokens, plus the same reference latents (if VAE provided).| CONDITIONING  
`latent`| A blank latent tensor with shape `[batch_size, 128, height÷16, width÷16]` for use as the initial noise during sampling.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeMageFlowEdit/en.md)

* * *

**Source fingerprint (SHA-256):** `880d8856b7f6e656bc68ca953fbf892898d05bc5d65290ae3bf7a4405ee09be3`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/TextEncodeMageFlowEdit.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/TextEncodeMageFlowEdit)

[CLIPTextEncodeLumina2 - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/CLIPTextEncodeLumina2)[TextEncodeMingImageEdit - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/TextEncodeMingImageEdit)

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
