---
url: https://docs.comfy.org/built-in-nodes/StableZero123_Conditioning_Batched/
title: StableZero123_Conditioning_Batched - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:05.654684+00:00
---

# StableZero123_Conditioning_Batched - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/StableZero123_Conditioning_Batched/

Stable Zero123

# StableZero123_Conditioning_Batched - ComfyUI Built-in Node Documentation

Copy pageCopy page

The StableZero123ConditioningBatched node prepares conditioning data for generating a 3D model from a single input image.

Copy pageCopy page

The StableZero123_Conditioning_Batched node prepares conditioning data for generating a 3D model from a single input image. It encodes the image with a CLIP vision model and a VAE, combines the visual features with camera embeddings built from elevation and azimuth angles, and produces positive and negative conditioning plus a latent tensor for a batch of samples. When `batch_size` is greater than 1, the elevation and azimuth angles are increased by their batch increment values for each item in the batch.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`clip_vision`| The CLIP vision model used for encoding the input image| CLIP_VISION| Yes| -  
`init_image`| The initial input image to be processed and encoded| IMAGE| Yes| -  
`vae`| The VAE model used for encoding image pixels into latent space| VAE| Yes| -  
`width`| The output width for the processed image (default: 256)| INT| Yes| 16 to MAX_RESOLUTION (step of 8)  
`height`| The output height for the processed image (default: 256)| INT| Yes| 16 to MAX_RESOLUTION (step of 8)  
`batch_size`| The number of conditioning samples to generate in the batch (default: 1)| INT| Yes| 1 to 4096  
`elevation`| The initial camera elevation angle in degrees (default: 0.0)| FLOAT| Yes| -180.0 to 180.0 (step of 0.1)  
`azimuth`| The initial camera azimuth angle in degrees (default: 0.0)| FLOAT| Yes| -180.0 to 180.0 (step of 0.1)  
`elevation_batch_increment`| The amount to increment elevation for each batch item (default: 0.0). Marked as an advanced input.| FLOAT| Yes| -180.0 to 180.0 (step of 0.1)  
`azimuth_batch_increment`| The amount to increment azimuth for each batch item (default: 0.0). Marked as an advanced input.| FLOAT| Yes| -180.0 to 180.0 (step of 0.1)  
  
**Note:** The `width` and `height` values must be multiples of 8, since the node divides these dimensions by 8 internally when building the latent tensor.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| The positive conditioning data containing the image embeddings and camera embeddings for each batch item| CONDITIONING  
`negative`| The negative conditioning data with zero-initialized embeddings| CONDITIONING  
`latent`| A zero-initialized latent tensor with dimensions batch_size x 4 x height/8 x width/8, along with batch indexing information| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning_Batched/en.md)

* * *

**Source fingerprint (SHA-256):** `94fc53dace8f294a746c47f8aa0da145f3e7beeb77a95912a38f0037ac094292`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/StableZero123_Conditioning_Batched.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/StableZero123_Conditioning_Batched)

[StableZero123_Conditioning - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/StableZero123_Conditioning)[ConditioningConcat - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ConditioningConcat)

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
