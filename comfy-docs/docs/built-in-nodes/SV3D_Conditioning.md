---
url: https://docs.comfy.org/built-in-nodes/SV3D_Conditioning/
title: SV3D_Conditioning - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:55.743699+00:00
---

# SV3D_Conditioning - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SV3D_Conditioning/

Stable Video 3d

# SV3D_Conditioning - ComfyUI Built-in Node Documentation

Copy pageCopy page

SV3DConditioning prepares conditioning data for 3D video generation using the SV3D model.

Copy pageCopy page

SV3D_Conditioning prepares conditioning data for 3D video generation using the SV3D model. It takes an initial image and processes it through CLIP vision and VAE encoders to create positive and negative conditioning, along with a latent representation. The node generates camera elevation and azimuth sequences for multi-frame video generation based on the specified number of video frames.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`clip_vision`| The CLIP vision model used for encoding the input image| CLIP_VISION| Yes| -  
`init_image`| The initial image that serves as the starting point for 3D video generation| IMAGE| Yes| -  
`vae`| The VAE model used for encoding the image into latent space| VAE| Yes| -  
`width`| The output width for the generated video frames (default: 576, step of 8)| INT| Yes| 16 to MAX_RESOLUTION  
`height`| The output height for the generated video frames (default: 576, step of 8)| INT| Yes| 16 to MAX_RESOLUTION  
`video_frames`| The number of frames to generate for the video sequence (default: 21)| INT| Yes| 1 to 4096  
`elevation`| The camera elevation angle in degrees for the 3D view (default: 0.0, step of 0.1)| FLOAT| Yes| -90.0 to 90.0  
  
Note: The camera azimuth starts at 0 degrees and increases by a constant amount each frame so that the camera completes a full 360-degree orbit around the object across the generated frames. The per-frame increment is calculated as 360 divided by (`video_frames` \- 1), using a minimum divisor of 2 when only one frame is requested. The `elevation` value stays constant for every frame. The `init_image` is scaled to the specified `width` and `height` before VAE encoding, and the returned latent uses dimensions of `video_frames` x 4 x (`height` // 8) x (`width` // 8).

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| The positive conditioning data containing image embeddings and camera parameters for generation| CONDITIONING  
`negative`| The negative conditioning data with zeroed embeddings and latents for contrastive generation| CONDITIONING  
`latent`| An empty latent tensor with dimensions matching the specified video frames and resolution| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SV3D_Conditioning/en.md)

* * *

**Source fingerprint (SHA-256):** `e28173cfa560290e66b032687088cf0b981256ca5c21f6aa608e0fdaec886665`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SV3D_Conditioning.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SV3D_Conditioning)

[SD_4XUpscale_Conditioning - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SD_4XUpscale_Conditioning)[StableZero123_Conditioning - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/StableZero123_Conditioning)

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
