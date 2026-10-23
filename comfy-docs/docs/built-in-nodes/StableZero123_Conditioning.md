---
url: https://docs.comfy.org/built-in-nodes/StableZero123_Conditioning/
title: StableZero123_Conditioning - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:05.551155+00:00
---

# StableZero123_Conditioning - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/StableZero123_Conditioning/

Stable Zero123

# StableZero123_Conditioning - ComfyUI Built-in Node Documentation

Copy pageCopy page

The StableZero123Conditioning node processes an input image and camera angles to generate conditioning data and latent representations for 3D model generation.

Copy pageCopy page

The StableZero123_Conditioning node processes an input image and camera angles to generate conditioning data and latent representations for 3D model generation. It uses a CLIP vision model to encode the image features, combines them with camera embedding information based on elevation and azimuth angles, and produces positive and negative conditioning along with a latent representation for downstream 3D generation tasks.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`clip_vision`| The CLIP vision model used to encode image features| CLIP_VISION| Yes| -  
`init_image`| The input image to be processed and encoded| IMAGE| Yes| -  
`vae`| The VAE model used for encoding pixels to latent space| VAE| Yes| -  
`width`| Output width for the latent representation (default: 256, step: 8)| INT| Yes| 16 to MAX_RESOLUTION  
`height`| Output height for the latent representation (default: 256, step: 8)| INT| Yes| 16 to MAX_RESOLUTION  
`batch_size`| Number of samples to generate in the batch (default: 1)| INT| Yes| 1 to 4096  
`elevation`| Camera elevation angle in degrees (default: 0.0, step: 0.1)| FLOAT| Yes| -180.0 to 180.0  
`azimuth`| Camera azimuth angle in degrees (default: 0.0, step: 0.1)| FLOAT| Yes| -180.0 to 180.0  
  
**Note:** The `width` and `height` parameters use a step of 8, so values are set in increments of 8. The node divides them by 8 to determine the latent representation dimensions. The image is rescaled to the given `width` and `height` using bilinear upscaling with center cropping before VAE encoding.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| Positive conditioning data combining image features and camera embeddings, including the VAE-encoded input image as a latent to concatenate| CONDITIONING  
`negative`| Negative conditioning data with zero-initialized features and a zero-initialized latent| CONDITIONING  
`latent`| Zero-initialized latent representation with dimensions [batch_size, 4, height//8, width//8]| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning/en.md)

* * *

**Source fingerprint (SHA-256):** `a694610c9f22fe0dab3ae02f4aabb33e3de8e5031c82dff5e8ba232c098f4a1d`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/StableZero123_Conditioning.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/StableZero123_Conditioning)

[SV3D_Conditioning - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SV3D_Conditioning)[StableZero123_Conditioning_Batched - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/StableZero123_Conditioning_Batched)

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
