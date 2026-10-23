---
url: https://docs.comfy.org/built-in-nodes/HunyuanImageToVideo/
title: HunyuanImageToVideo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:05.305426+00:00
---

# HunyuanImageToVideo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/HunyuanImageToVideo/

Hunyuan Video

# HunyuanImageToVideo - ComfyUI Built-in Node Documentation

Copy pageCopy page

The HunyuanImageToVideo node converts images into video latent representations using the Hunyuan video model.

Copy pageCopy page

The HunyuanImageToVideo node converts images into video latent representations using the Hunyuan video model. It takes conditioning inputs and optional starting images to generate video latents that can be further processed by video generation models. The node supports different guidance types for controlling how the starting image influences the video generation process.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`positive`| Positive conditioning input for guiding the video generation| CONDITIONING| Yes| -  
`vae`| VAE model used for encoding images into latent space| VAE| Yes| -  
`width`| Width of the output video in pixels (default: 848, step: 16)| INT| Yes| 16 to MAX_RESOLUTION  
`height`| Height of the output video in pixels (default: 480, step: 16)| INT| Yes| 16 to MAX_RESOLUTION  
`length`| Number of frames in the output video (default: 53, step: 4)| INT| Yes| 1 to MAX_RESOLUTION  
`batch_size`| Number of videos to generate simultaneously (default: 1)| INT| Yes| 1 to 4096  
`guidance_type`| Method for incorporating the starting image into video generation (default: “v1 (concat)”). Advanced option| COMBO| Yes| ”v1 (concat)"  
"v2 (replace)"  
"custom”  
`start_image`| Optional starting image (or image sequence) to initialize the video generation. Only the first `length` frames and the first 3 color channels are used| IMAGE| No| -  
  
**Note:** When `start_image` is provided, the node uses different guidance methods based on the selected `guidance_type`:

  * “v1 (concat)”: Concatenates the image latent with the video latent and applies a mask to blend the image into the video
  * “v2 (replace)”: Replaces initial video frames with the image latent and applies a noise mask
  * “custom”: Uses the image as a reference latent for guidance

If `start_image` is not provided, no guidance conditioning is added and the latent is returned as a plain block of zeros.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| Modified positive conditioning with image guidance applied when start_image is provided| CONDITIONING  
`latent`| Video latent representation ready for further processing by video generation models| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanImageToVideo/en.md)

* * *

**Source fingerprint (SHA-256):** `0ed00d59513492f31760a18ce3b0edf10b64cad848ba52c4e47d5f61fae9accc`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/HunyuanImageToVideo.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/HunyuanImageToVideo)

[CLIPTextEncodeHunyuanDiT - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ClipTextEncodeHunyuanDit)[HunyuanRefinerLatent - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/HunyuanRefinerLatent)

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
