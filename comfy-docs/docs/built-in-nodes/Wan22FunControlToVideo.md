---
url: https://docs.comfy.org/built-in-nodes/Wan22FunControlToVideo/
title: Wan22FunControlToVideo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:21.787226+00:00
---

# Wan22FunControlToVideo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Wan22FunControlToVideo/

Fun Control

# Wan22FunControlToVideo - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Wan22FunControlToVideo node prepares conditioning data and an empty latent tensor for video generation with the Wan video model.

Copy pageCopy page

The Wan22FunControlToVideo node prepares conditioning data and an empty latent tensor for video generation with the Wan video model. It encodes optional reference images and control videos into latent space, attaches them to the positive and negative conditioning, and creates a zero-filled latent tensor with the correct spatial and temporal dimensions for the requested video.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`positive`| Positive conditioning input for guiding the video generation| CONDITIONING| Yes| -  
`negative`| Negative conditioning input for guiding the video generation| CONDITIONING| Yes| -  
`vae`| VAE model used to encode images into latent space| VAE| Yes| -  
`width`| Width of the output video in pixels (default: 832, step: 16)| INT| Yes| 16 to MAX_RESOLUTION  
`height`| Height of the output video in pixels (default: 480, step: 16)| INT| Yes| 16 to MAX_RESOLUTION  
`length`| Number of frames in the video sequence (default: 81, step: 4)| INT| Yes| 1 to MAX_RESOLUTION  
`batch_size`| Number of video sequences to generate (default: 1)| INT| Yes| 1 to 4096  
`ref_image`| Optional reference image that provides visual guidance for the generation| IMAGE| No| -  
`control_video`| Optional control video that guides the generation process| IMAGE| No| -  
  
**Note:** The `length` parameter is processed in steps of 4 frames, and the node automatically applies temporal scaling when building the latent space. When `ref_image` is provided, only its first frame is encoded (resized to `width` x `height`) and attached to the conditioning as reference latents. When `control_video` is provided, it is trimmed to `length` frames, resized, encoded, and placed into the concat latent used by the conditioning. The concatenated latent is duplicated along the channel dimension and its channel layout depends on the VAE’s latent channel count (48 channels uses the Wan 2.2 format, otherwise the Wan 2.1 format). The `start_image` parameter is referenced in the execution logic but is not exposed in the node’s input schema, so it cannot be set from the node interface.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| Positive conditioning with video-specific latent data added, including the concat latent, mask, and optional reference latents| CONDITIONING  
`negative`| Negative conditioning with video-specific latent data added, including the concat latent, mask, and optional reference latents| CONDITIONING  
`latent`| Empty latent tensor prepared for video generation, sized according to the batch size, latent channels, length, height, and width| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22FunControlToVideo/en.md)

* * *

**Source fingerprint (SHA-256):** `731b848f15c13ddc662f19230acb55d195f934bad7d9ae516a288e0ed8f8d899`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Wan22FunControlToVideo.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Wan22FunControlToVideo)

[WanDancerVideo - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/WanDancerVideo)[WanFunControlToVideo - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/WanFunControlToVideo)

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
