---
url: https://docs.comfy.org/built-in-nodes/WanSoundImageToVideo/
title: WanSoundImageToVideo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:25.539540+00:00
---

# WanSoundImageToVideo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/WanSoundImageToVideo/

Sound

# WanSoundImageToVideo - ComfyUI Built-in Node Documentation

Copy pageCopy page

The WanSoundImageToVideo node prepares conditioning and an empty latent video tensor for Wan sound-to-video generation.

Copy pageCopy page

The WanSoundImageToVideo node prepares conditioning and an empty latent video tensor for Wan sound-to-video generation. It can optionally incorporate audio encoding, a reference image, a control video, and a motion reference to guide the generated video.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`positive`| Positive conditioning prompts that guide what content should appear in the generated video| CONDITIONING| Yes| -  
`negative`| Negative conditioning prompts that specify what content should be avoided in the generated video| CONDITIONING| Yes| -  
`vae`| VAE model used for encoding reference images, motion references, and control video frames into latent representations| VAE| Yes| -  
`width`| Width of the output video in pixels (default: 832, step: 16)| INT| Yes| 16 to MAX_RESOLUTION  
`height`| Height of the output video in pixels (default: 480, step: 16)| INT| Yes| 16 to MAX_RESOLUTION  
`length`| Number of frames in the generated video (default: 77, step: 4)| INT| Yes| 1 to MAX_RESOLUTION  
`batch_size`| Number of videos to generate simultaneously (default: 1)| INT| Yes| 1 to 4096  
`audio_encoder_output`| Optional audio encoding that can influence the video generation based on sound characteristics. When provided, the audio features are interpolated and used to condition the video generation.| AUDIO_ENCODER_OUTPUT| No| -  
`ref_image`| Optional reference image that provides visual guidance for the video content. The image is upscaled to match the specified width and height, then encoded into a latent representation. Only the first image of the input is used as the reference.| IMAGE| No| -  
`control_video`| Optional control video that guides the motion and structure of the generated video. The video is upscaled and encoded, then used to condition the output. Only the first `length` frames are used.| IMAGE| No| -  
`ref_motion`| Optional motion reference that provides guidance for movement patterns in the video. If the input has more than 73 frames, only the last 73 are used. If fewer than 73 frames are provided, the sequence is padded with neutral frames.| IMAGE| No| -  
  
Note: All optional inputs can be used independently or together. The node modifies the provided `positive` and `negative` conditioning based on which optional inputs are connected.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| Processed positive conditioning that has been modified for video generation, including audio embeddings, reference latents, motion references, and control video conditioning when the corresponding optional inputs are provided| CONDITIONING  
`negative`| Processed negative conditioning that has been modified for video generation, including audio embeddings (set to zero), reference latents, motion references, and control video conditioning when the corresponding optional inputs are provided| CONDITIONING  
`latent`| Empty latent video tensor used as the starting point for generation. The latent tensor has shape `[batch_size, 16, latent_t, height/8, width/8]`, where `latent_t` is calculated as `((length - 1) // 4) + 1`.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideo/en.md)

* * *

**Source fingerprint (SHA-256):** `b1148cd00d8999dd6842e3c2fb13655fda8f20d5befed975a6d1652688b2807c`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/WanSoundImageToVideo.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/WanSoundImageToVideo)

[WanSCAILToVideo - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/WanSCAILToVideo)[WanSoundImageToVideoExtend - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/WanSoundImageToVideoExtend)

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
