---
url: https://docs.comfy.org/built-in-nodes/Wan22ImageToVideoLatent/
title: Wan22ImageToVideoLatent - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:22.231338+00:00
---

# Wan22ImageToVideoLatent - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Wan22ImageToVideoLatent/

Wan

# Wan22ImageToVideoLatent - ComfyUI Built-in Node Documentation

Copy pageCopy page

Wan22ImageToVideoLatent creates video latent representations from images.

Copy pageCopy page

Wan22ImageToVideoLatent creates video latent representations from images. It generates a blank video latent space with the specified width, height, frame length, and batch size, and can optionally encode a starting image sequence into the beginning frames. When a start image is provided, the node encodes it into the latent space and creates a corresponding noise mask that marks which regions should be denoised during generation.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`vae`| The VAE model used to encode the start image into latent space| VAE| Yes| -  
`width`| The width of the output video in pixels (default: 1280, step: 32)| INT| Yes| 32 to MAX_RESOLUTION  
`height`| The height of the output video in pixels (default: 704, step: 32)| INT| Yes| 32 to MAX_RESOLUTION  
`length`| The number of frames in the video sequence (default: 49, step: 4)| INT| Yes| 1 to MAX_RESOLUTION  
`batch_size`| The number of video latents to generate (default: 1)| INT| Yes| 1 to 4096  
`start_image`| Optional starting image sequence to encode into the beginning frames of the video latent (uses the first `length` frames)| IMAGE| No| -  
  
**Note:** When `start_image` is provided, the image sequence is upscaled to the target `width` and `height`, encoded with the VAE, and placed into the first frames of the latent. The noise mask for those frames is set to 0 (preserved), while the remaining frames have a mask value of 1 (to be denoised). The latent always has 48 channels, spatial dimensions of `height / 16` by `width / 16`, and a temporal dimension of `((length - 1) // 4) + 1`. `width` and `height` must be divisible by 16 (enforced by the step of 32), and `length` increases the temporal dimension in steps of 4. When `start_image` is not provided, a fully blank latent is returned with no noise mask, and the `batch_size` input is not applied to that blank latent.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`samples`| The generated video latent representation, repeated for each item in the batch| LATENT  
`noise_mask`| The noise mask indicating which regions should be denoised (value 1) and which retain the encoded start image (value 0)| LATENT  
  
Both fields are returned together inside a single LATENT output.

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22ImageToVideoLatent/en.md)

* * *

**Source fingerprint (SHA-256):** `3d05980641eeef2e86df7a845aa8b2bd703882db98fe71adef2746ab34a9d717`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Wan22ImageToVideoLatent.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Wan22ImageToVideoLatent)

[WanVaceToVideo - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/WanVaceToVideo)[WanFirstLastFrameToVideo - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/WanFirstLastFrameToVideo)

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
