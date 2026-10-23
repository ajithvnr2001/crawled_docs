---
url: https://docs.comfy.org/built-in-nodes/WanPhantomSubjectToVideo/
title: WanPhantomSubjectToVideo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:26.367287+00:00
---

# WanPhantomSubjectToVideo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/WanPhantomSubjectToVideo/

Phantom Subject

# WanPhantomSubjectToVideo - ComfyUI Built-in Node Documentation

Copy pageCopy page

The WanPhantomSubjectToVideo node prepares conditioning data and a latent for Wan video generation.

Copy pageCopy page

The WanPhantomSubjectToVideo node prepares conditioning data and a latent for Wan video generation. It creates an empty latent video from the requested width, height, length, and batch size, and, when reference images are supplied, encodes them with the VAE and adds them to the conditionings as time-dimensional visual guidance.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`positive`| Positive conditioning input for guiding video generation| CONDITIONING| Yes| -  
`negative`| Negative conditioning input to avoid certain characteristics| CONDITIONING| Yes| -  
`vae`| VAE model used to encode the reference images when they are provided| VAE| Yes| -  
`width`| Output video width in pixels (default: 832)| INT| Yes| 16 to MAX_RESOLUTION (step 16)  
`height`| Output video height in pixels (default: 480)| INT| Yes| 16 to MAX_RESOLUTION (step 16)  
`length`| Number of frames in the generated video (default: 81)| INT| Yes| 1 to MAX_RESOLUTION (step 4)  
`batch_size`| Number of videos to generate simultaneously (default: 1)| INT| Yes| 1 to 4096  
`images`| Optional reference images used as time-dimensional visual guidance| IMAGE| No| -  
  
**Note:** When `images` are provided, they are automatically upscaled to match the specified `width` and `height`, and only the first `length` images are used for processing. Each image is encoded with the `vae` and concatenated along the time dimension, and only the RGB channels of each image are used. When `images` are not provided, all three conditioning outputs are returned unchanged from the input conditionings.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| Positive conditioning with time-dimensional concatenation of the encoded reference images when images are provided; otherwise the input `positive` is returned unchanged| CONDITIONING  
`negative_text`| Negative conditioning with time-dimensional concatenation of the encoded reference images when images are provided; otherwise the input `negative` is returned unchanged| CONDITIONING  
`negative_img_text`| Negative conditioning with a zeroed time-dimensional concatenation when images are provided; otherwise the input `negative` is returned unchanged| CONDITIONING  
`latent`| Zero-filled latent video tensor with 16 channels; its frame count is derived from `length` and its spatial dimensions from `height` and `width`| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanPhantomSubjectToVideo/en.md)

* * *

**Source fingerprint (SHA-256):** `a1853382f6e564f66262b69dd7b06cc58e26b93386a460a98e6fcc2ff6acf12b`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/WanPhantomSubjectToVideo.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/WanPhantomSubjectToVideo)

[WanTrackToVideo - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/WanTrackToVideo)[SCAIL2ColoredMask - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SCAIL2ColoredMask)

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
