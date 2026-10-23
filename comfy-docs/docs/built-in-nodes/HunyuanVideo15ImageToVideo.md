---
url: https://docs.comfy.org/built-in-nodes/HunyuanVideo15ImageToVideo/
title: HunyuanVideo15ImageToVideo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:05.120155+00:00
---

# HunyuanVideo15ImageToVideo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/HunyuanVideo15ImageToVideo/

Hunyuan Video

# HunyuanVideo15ImageToVideo - ComfyUI Built-in Node Documentation

Copy pageCopy page

The HunyuanVideo15ImageToVideo node prepares conditioning and latent space data for video generation based on the HunyuanVideo 1.5 model.

Copy pageCopy page

The HunyuanVideo15ImageToVideo node prepares conditioning and latent space data for video generation based on the HunyuanVideo 1.5 model. It creates an initial latent representation for a video sequence and can optionally integrate a starting image or a CLIP vision output to guide the generation process.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`positive`| The positive conditioning prompts that describe what the video should contain.| CONDITIONING| Yes| -  
`negative`| The negative conditioning prompts that describe what the video should avoid.| CONDITIONING| Yes| -  
`vae`| The VAE (Variational Autoencoder) model used to encode the starting image into the latent space.| VAE| Yes| -  
`width`| The width of the output video frames in pixels. Must be divisible by 16. (default: 848)| INT| Yes| 16 to MAX_RESOLUTION, step: 16  
`height`| The height of the output video frames in pixels. Must be divisible by 16. (default: 480)| INT| Yes| 16 to MAX_RESOLUTION, step: 16  
`length`| The total number of frames in the video sequence. Values increase in steps of 4 starting from 1 (1, 5, 9, 13, …). (default: 33)| INT| Yes| 1 to MAX_RESOLUTION, step: 4  
`batch_size`| The number of video sequences to generate in a single batch. (default: 1)| INT| Yes| 1 to 4096  
`start_image`| An optional starting image to initialize the video generation. If provided, it is encoded and used to condition the first frames. Only the first `length` frames of the image are used.| IMAGE| No| -  
`clip_vision_output`| Optional CLIP vision embeddings to provide additional visual conditioning for the generation.| CLIP_VISION_OUTPUT| No| -  
  
**Note:** When a `start_image` is provided, it is automatically resized to match the specified `width` and `height` using bilinear interpolation. The first `length` frames of the image batch are used, and only the first 3 color channels of each frame are encoded. The encoded image is then added to both the `positive` and `negative` conditioning as a `concat_latent_image` with a corresponding `concat_mask`. The mask is set to 0.0 for the frames covered by the starting image and 1.0 for the remaining frames. When a `clip_vision_output` is provided, it is also added to both the `positive` and `negative` conditioning.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| The modified positive conditioning, which may now include the encoded starting image or CLIP vision output.| CONDITIONING  
`negative`| The modified negative conditioning, which may now include the encoded starting image or CLIP vision output.| CONDITIONING  
`latent`| An empty latent tensor with dimensions configured for the specified batch size, video length, width, and height.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15ImageToVideo/en.md)

* * *

**Source fingerprint (SHA-256):** `dbedf7f378ae9613c8f47fe9876a4576c815055b4cdb6bf687b7575fcd7ea80a`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/HunyuanVideo15ImageToVideo.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/HunyuanVideo15ImageToVideo)

[HunyuanRefinerLatent - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/HunyuanRefinerLatent)[HunyuanVideo15SuperResolution - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/HunyuanVideo15SuperResolution)

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
