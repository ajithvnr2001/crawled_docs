---
url: https://docs.comfy.org/built-in-nodes/WanImageToVideo/
title: WanImageToVideo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:24.311091+00:00
---

# WanImageToVideo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/WanImageToVideo/

Wan

# WanImageToVideo - ComfyUI Built-in Node Documentation

Copy pageCopy page

The WanImageToVideo node prepares conditioning and latent representations for video generation.

Copy pageCopy page

The WanImageToVideo node prepares conditioning and latent representations for video generation. It creates an empty latent space for the video and can optionally incorporate a starting image and CLIP vision output to guide the generation. Both the positive and negative conditioning inputs are updated with the provided image and vision data.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`positive`| Positive conditioning input used to guide the generation| CONDITIONING| Yes| -  
`negative`| Negative conditioning input used to guide the generation| CONDITIONING| Yes| -  
`vae`| VAE model used to encode images into latent space| VAE| Yes| -  
`width`| Width of the generated video (default: 832, step: 16)| INT| Yes| 16 to MAX_RESOLUTION  
`height`| Height of the generated video (default: 480, step: 16)| INT| Yes| 16 to MAX_RESOLUTION  
`length`| Number of frames in the video (default: 81, step: 4)| INT| Yes| 1 to MAX_RESOLUTION  
`batch_size`| Number of videos to generate in one batch (default: 1)| INT| Yes| 1 to 4096  
`clip_vision_output`| Optional CLIP vision output added as extra conditioning to both the positive and negative inputs| CLIP_VISION_OUTPUT| No| -  
`start_image`| Optional starting image used to initialize the video. When provided, it is resized to the specified `width` and `height` and placed at the beginning of the frame sequence; any frames beyond `length` are ignored. The remaining frames are filled with neutral gray (0.5) values unless `ref_pad_image` is supplied.| IMAGE| No| -  
`ref_pad_image`| Optional reference image whose first frame replaces the neutral gray padding of the frame sequence. It is resized to the specified `width` and `height`, and only the first image of the batch is used. Has an effect only when `start_image` is also provided.| IMAGE| No| -  
  
**Note:** When `start_image` is provided, the frame sequence is encoded with the VAE and a mask is applied to the conditioning. The mask is set to 0 for the frames covered by the starting image and 1 for the remaining frames, so generation continues from the provided image. Only the first three color channels (RGB) of the image are used during encoding. Both positive and negative conditioning receive the same concatenated latent image, mask, and (if supplied) CLIP vision output. When `ref_pad_image` is supplied together with `start_image`, its first frame is resized to `width` and `height` and written into the RGB channels of the padding frames before the starting image is placed on top, so the padding carries the reference image instead of flat gray. This is SVI-style anti-drift padding, used by models such as ID-V2V.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| Positive conditioning, updated with the image and vision data| CONDITIONING  
`negative`| Negative conditioning, updated with the image and vision data| CONDITIONING  
`latent`| Empty latent tensor ready for video generation, with shape [batch_size, 16, ((length-1)//4)+1, height//8, width//8]| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideo/en.md)

* * *

**Source fingerprint (SHA-256):** `3000c1c816d2c123fc5bc46ea1f193c52c0f81a2f8c4a9110d8a4fa909185aea`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/WanImageToVideo.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/WanImageToVideo)

[WanFirstLastFrameToVideo - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/WanFirstLastFrameToVideo)[SheetSage2AudioToABC - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SheetSage2AudioToABC)

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
