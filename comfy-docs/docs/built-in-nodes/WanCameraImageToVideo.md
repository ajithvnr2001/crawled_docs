---
url: https://docs.comfy.org/built-in-nodes/WanCameraImageToVideo/
title: WanCameraImageToVideo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:23.071625+00:00
---

# WanCameraImageToVideo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/WanCameraImageToVideo/

Camera

# WanCameraImageToVideo - ComfyUI Built-in Node Documentation

Copy pageCopy page

The WanCameraImageToVideo node prepares conditioning and latent data for camera-controlled video generation from images.

Copy pageCopy page

The WanCameraImageToVideo node prepares conditioning and latent data for camera-controlled video generation from images. It takes positive and negative conditioning prompts, along with optional inputs such as a starting image, CLIP vision output, and camera conditions, and outputs updated conditioning plus an empty latent tensor ready for a video model to fill in.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`positive`| Positive conditioning prompts for video generation| CONDITIONING| Yes| -  
`negative`| Negative conditioning prompts to avoid in video generation| CONDITIONING| Yes| -  
`vae`| VAE model for encoding images to latent space| VAE| Yes| -  
`width`| Output video width in pixels (default: 832, step: 16)| INT| Yes| 16 to MAX_RESOLUTION  
`height`| Output video height in pixels (default: 480, step: 16)| INT| Yes| 16 to MAX_RESOLUTION  
`length`| Number of frames in the video sequence (default: 81, step: 4)| INT| Yes| 1 to MAX_RESOLUTION  
`batch_size`| Number of videos to generate simultaneously (default: 1)| INT| Yes| 1 to 4096  
`clip_vision_output`| Optional CLIP vision output for additional conditioning| CLIP_VISION_OUTPUT| No| -  
`start_image`| Optional starting image to initialize the video sequence. When provided, only the first `length` frames are used, and the image is resized to match the specified `width` and `height`. The first frames of the sequence are encoded into the latent and a mask is applied to blend the starting frames with generated content.| IMAGE| No| -  
`camera_conditions`| Optional camera embedding conditions for video generation. When provided, these conditions are applied to both the positive and negative conditioning.| WAN_CAMERA_EMBEDDING| No| -  
  
**Note:** When `start_image` is provided, the node sets `concat_latent_image` and `concat_mask` values on both `positive` and `negative` conditioning. The `camera_conditions` and `clip_vision_output` parameters are optional, but when provided, they modify the conditioning for both the positive and negative prompts.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| Modified positive conditioning with applied camera conditions, clip vision output, and/or starting image data| CONDITIONING  
`negative`| Modified negative conditioning with applied camera conditions, clip vision output, and/or starting image data| CONDITIONING  
`latent`| Empty video latent representation for use with video models. The latent tensor has dimensions [batch_size, 16, frames, height/8, width/8], where frames is calculated as ((length - 1) // 4) + 1.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraImageToVideo/en.md)

* * *

**Source fingerprint (SHA-256):** `467a82be0dfd6ac1c3b2dd2a6cb02e0d0749de4536a7fbdb000456b817b20ebb`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/WanCameraImageToVideo.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/WanCameraImageToVideo)

[WanCameraEmbedding - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/WanCameraEmbedding)[WanDancerEncodeAudio - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/WanDancerEncodeAudio)

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
