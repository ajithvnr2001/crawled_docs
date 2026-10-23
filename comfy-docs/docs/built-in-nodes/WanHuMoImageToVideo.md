---
url: https://docs.comfy.org/built-in-nodes/WanHuMoImageToVideo/
title: WanHuMoImageToVideo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:24.105942+00:00
---

# WanHuMoImageToVideo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/WanHuMoImageToVideo/

Humo

# WanHuMoImageToVideo - ComfyUI Built-in Node Documentation

Copy pageCopy page

The WanHuMoImageToVideo node prepares conditioning data and an empty latent video for the Wan HuMo video generation pipeline.

Copy pageCopy page

The WanHuMoImageToVideo node prepares conditioning data and an empty latent video for the Wan HuMo video generation pipeline. It can attach a reference image and audio embeddings to the positive and negative conditioning inputs, and it creates a zero-filled latent sized from the requested width, height, length, and batch size.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`positive`| Positive conditioning input that guides the video generation toward desired content.| CONDITIONING| Yes| -  
`negative`| Negative conditioning input that steers the video generation away from unwanted content.| CONDITIONING| Yes| -  
`vae`| VAE model used for encoding reference images into latent space.| VAE| Yes| -  
`width`| Width of the output video frames in pixels. Default: 832.| INT| Yes| 16 to MAX_RESOLUTION, step 16  
`height`| Height of the output video frames in pixels. Default: 480.| INT| Yes| 16 to MAX_RESOLUTION, step 16  
`length`| Number of frames in the generated video sequence. Default: 97.| INT| Yes| 1 to MAX_RESOLUTION, step 4  
`batch_size`| Number of video sequences to generate simultaneously. Default: 1.| INT| Yes| 1 to 4096  
`audio_encoder_output`| Optional audio encoding data that can influence video generation based on audio content.| AUDIOENCODEROUTPUT| No| -  
`ref_image`| Optional reference image used to guide the video generation style and content. Only the first image in the batch is used.| IMAGE| No| -  
  
**Note:** When a reference image is provided, the first image in the batch is upscaled to the requested `width` and `height` using bilinear interpolation and encoded with the VAE. That reference latent is attached to the positive conditioning, while a zero-filled latent of the same shape is attached to the negative conditioning. When `audio_encoder_output` is provided, the audio embeddings are interpolated and attached to the positive conditioning, while a zero-filled audio embedding is attached to the negative conditioning. If either optional input is omitted, zero-filled placeholder tensors are used: a zero reference latent of shape `[batch_size, 16, 1, height // 8, width // 8]` and/or zero audio embeddings of shape `[batch_size, latent_t + 1, 8, 5, 1280]`, where `latent_t = ((length - 1) // 4) + 1`.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| Modified positive conditioning with reference image and/or audio embeddings incorporated.| CONDITIONING  
`negative`| Modified negative conditioning with reference image and/or audio embeddings incorporated.| CONDITIONING  
`latent`| Zero-initialized latent representation for the video sequence, sized according to `width`, `height`, `length`, and `batch_size`. Shape: `[batch_size, 16, latent_t, height // 8, width // 8]`, where `latent_t = ((length - 1) // 4) + 1`.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanHuMoImageToVideo/en.md)

* * *

**Source fingerprint (SHA-256):** `db674a4a00729a8715988030083e2858f958cd21de73bbbe4ed6d76f5f539419`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/WanHuMoImageToVideo.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/WanHuMoImageToVideo)

[WanFunInpaintToVideo - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/WanFunInpaintToVideo)[WanInfiniteTalkToVideo - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/WanInfiniteTalkToVideo)

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
