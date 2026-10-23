---
url: https://docs.comfy.org/built-in-nodes/VOIDInpaintConditioning/
title: VOIDInpaintConditioning - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:17.552387+00:00
---

# VOIDInpaintConditioning - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/VOIDInpaintConditioning/

Void

# VOIDInpaintConditioning - ComfyUI Built-in Node Documentation

Copy pageCopy page

The VOIDInpaintConditioning node prepares the conditioning data needed for inpainting with CogVideoX models.

Copy pageCopy page

The VOIDInpaintConditioning node prepares the conditioning data needed for inpainting with CogVideoX models. It takes a source video and a preprocessed quadmask, encodes them through the VAE, and combines them into a 32-channel conditioning signal (16 channels from the mask + 16 channels from the masked video) that the model uses to fill in the masked areas.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`positive`| The positive conditioning to be augmented with the inpainting latent information| CONDITIONING| Yes| -  
`negative`| The negative conditioning to be augmented with the inpainting latent information| CONDITIONING| Yes| -  
`vae`| The VAE model used to encode the mask and masked video into latent space| VAE| Yes| -  
`video`| Source video frames [T, H, W, 3]| IMAGE| Yes| -  
`quadmask`| Preprocessed quadmask from VOIDQuadmaskPreprocess [T, H, W]| MASK| Yes| -  
`width`| The width to resize the video and mask to (default: 672)| INT| Yes| 16 to MAX_RESOLUTION (step: 8)  
`height`| The height to resize the video and mask to (default: 384)| INT| Yes| 16 to MAX_RESOLUTION (step: 8)  
`length`| Number of pixel frames to process. For CogVideoX-Fun-V1.5 (patch_size_t=2), latent_t must be even — lengths that produce odd latent_t are rounded down (e.g. 49 → 45) (default: 45)| INT| Yes| 1 to MAX_RESOLUTION (step: 1)  
`batch_size`| The batch size for the output noise latent (default: 1)| INT| Yes| 1 to 64  
  
**Note:** Because CogVideoX-Fun-V1.5 uses `patch_size_t=2`, the encoded latent must have an even temporal dimension. If `length` would produce an odd `latent_t`, the node automatically rounds it down to the nearest valid value and logs a warning. Using an odd `latent_t` corrupts the last frame through circular padding, which can cause visible jitter or disappearing subjects near the end of the decoded video.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| The positive conditioning with the inpainting latent information added| CONDITIONING  
`negative`| The negative conditioning with the inpainting latent information added| CONDITIONING  
`latent`| A zero-filled noise latent tensor with shape [batch_size, 16, latent_t, latent_h, latent_w]| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDInpaintConditioning/en.md)

* * *

**Source fingerprint (SHA-256):** `885e462c0f17a3e9610146a05ba3b9c879db0112d3961c95a83f63ba2cd511f1`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/VOIDInpaintConditioning.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/VOIDInpaintConditioning)

[TripoSplatPreprocessImage - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/TripoSplatPreprocessImage)[WanAnimate2Cache - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/WanAnimate2Cache)

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
