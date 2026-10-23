---
url: https://docs.comfy.org/built-in-nodes/SVD_img2vid_Conditioning/
title: SVD_img2vid_Conditioning - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:56.191693+00:00
---

# SVD_img2vid_Conditioning - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SVD_img2vid_Conditioning/

Video Models

# SVD_img2vid_Conditioning - ComfyUI Built-in Node Documentation

Copy pageCopy page

The SVDimg2vidConditioning node prepares conditioning data for video generation using Stable Video Diffusion.

Copy pageCopy page

The SVD_img2vid_Conditioning node prepares conditioning data for video generation using Stable Video Diffusion. It takes an initial image and processes it through CLIP vision and VAE encoders to create positive and negative conditioning pairs, along with an empty latent space for video generation. This node sets up the necessary parameters for controlling motion, frame rate, and augmentation levels in the generated video.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`clip_vision`| CLIP vision model for encoding the input image| CLIP_VISION| Yes| -  
`init_image`| Initial image to use as the starting point for video generation| IMAGE| Yes| -  
`vae`| VAE model for encoding the image into latent space| VAE| Yes| -  
`width`| Output video width (default: 1024, step: 8)| INT| Yes| 16 to MAX_RESOLUTION  
`height`| Output video height (default: 576, step: 8)| INT| Yes| 16 to MAX_RESOLUTION  
`video_frames`| Number of frames to generate in the video (default: 14)| INT| Yes| 1 to 4096  
`motion_bucket_id`| Controls the amount of motion in the generated video (default: 127)| INT| Yes| 1 to 1023  
`fps`| Frames per second for the generated video (default: 6)| INT| Yes| 1 to 1024  
`augmentation_level`| Level of noise augmentation to apply to the input image (default: 0.0, step: 0.01)| FLOAT| Yes| 0.0 to 10.0  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| Positive conditioning data containing image embeddings and video parameters| CONDITIONING  
`negative`| Negative conditioning data with zeroed embeddings and video parameters| CONDITIONING  
`latent`| Empty latent space tensor ready for video generation| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SVD_img2vid_Conditioning/en.md)

* * *

**Source fingerprint (SHA-256):** `33b295b6f2e459852aaa95d9dca26c724aa2e9ad0f884a1c7760766530a00a09`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SVD_img2vid_Conditioning.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SVD_img2vid_Conditioning)

[Stablezero123ConditioningBatched - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Stablezero123ConditioningBatched)[SvdImg2vidConditioning - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SvdImg2vidConditioning)

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
