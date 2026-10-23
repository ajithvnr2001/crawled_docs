---
url: https://docs.comfy.org/built-in-nodes/WanVaceToVideo/
title: WanVaceToVideo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:25.953937+00:00
---

# WanVaceToVideo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/WanVaceToVideo/

Vace

# WanVaceToVideo - ComfyUI Built-in Node Documentation

Copy pageCopy page

The WanVaceToVideo node prepares video conditioning data for VACE-controlled video generation models.

Copy pageCopy page

The WanVaceToVideo node prepares video conditioning data for VACE-controlled video generation models. It combines positive and negative conditioning with an optional control video, control masks, and a reference image, encodes them through a VAE, and outputs updated conditioning, an empty latent tensor, and a trim value.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`positive`| Positive conditioning input for guiding the generation| CONDITIONING| Yes| -  
`negative`| Negative conditioning input for guiding the generation| CONDITIONING| Yes| -  
`vae`| VAE model used for encoding images and video frames| VAE| Yes| -  
`width`| Output video width in pixels (default: 832, step: 16)| INT| Yes| 16 to MAX_RESOLUTION  
`height`| Output video height in pixels (default: 480, step: 16)| INT| Yes| 16 to MAX_RESOLUTION  
`length`| Number of frames in the video (default: 81, step: 4)| INT| Yes| 1 to MAX_RESOLUTION  
`batch_size`| Number of videos to generate simultaneously (default: 1)| INT| Yes| 1 to 4096  
`strength`| Condition strength for VACE control (default: 1.0, step: 0.01). This is not a LoRA strength. LoRA weights are applied through separate LoRA nodes.| FLOAT| Yes| 0.0 to 1000.0  
`control_video`| Optional input video used for control conditioning. If not provided, a neutral gray video is created automatically.| IMAGE| No| -  
`control_masks`| Optional masks that determine which parts of the control video are active. If not provided, a full white mask is used.| MASK| No| -  
`reference_image`| Optional reference image for additional conditioning. When provided, it is encoded and prepended to the latent sequence. Only the first image is used.| IMAGE| No| -  
  
**Note:** When `control_video` is provided, it is truncated to `length` frames and upscaled to the specified `width` and `height`; if it has fewer frames than `length`, the missing frames are padded with neutral gray (value 0.5). When it is not provided, a neutral gray video of `length` frames is created automatically. `control_masks` are upscaled to the specified `width` and `height`, truncated to `length` frames, and padded with value 1.0 if shorter. The mask separates the control video into inactive and reactive parts, each VAE-encoded and concatenated along the channel dimension; the mask is also downsampled to latent resolution. When `reference_image` is provided, its first image is VAE-encoded and prepended to the latent sequence, and `trim_latent` reports the number of latent frames added. The latent frame count is calculated as `((length - 1) // 4) + 1`, and the latent spatial dimensions are `height / 8` and `width / 8`.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| Positive conditioning with video control data (vace_frames, vace_mask, vace_strength) applied| CONDITIONING  
`negative`| Negative conditioning with video control data (vace_frames, vace_mask, vace_strength) applied| CONDITIONING  
`latent`| Empty latent tensor ready for video generation with shape [batch_size, 16, latent_length, height/8, width/8]| LATENT  
`trim_latent`| Number of latent frames to trim when a reference image is used; 0 if no reference image is provided| INT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanVaceToVideo/en.md)

* * *

**Source fingerprint (SHA-256):** `2039b7509ce5b731e9e41d9cd2dad022d4c5004751f571a4cf88c1ba0cae405b`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/WanVaceToVideo.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/WanVaceToVideo)

[WanSoundImageToVideoExtend - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/WanSoundImageToVideoExtend)[Wan22ImageToVideoLatent - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Wan22ImageToVideoLatent)

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
