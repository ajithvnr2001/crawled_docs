---
url: https://docs.comfy.org/built-in-nodes/LTXVImgToVideo/
title: LTXVImgToVideo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:18.658925+00:00
---

# LTXVImgToVideo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LTXVImgToVideo/

Ltxv

# LTXVImgToVideo - ComfyUI Built-in Node Documentation

Copy pageCopy page

LTXVImgToVideo converts an input image into a video latent representation for video generation models.

Copy pageCopy page

LTXVImgToVideo converts an input image into a video latent representation for video generation models. It resizes the image to the requested width and height, encodes it with the VAE, and places the encoded frames at the start of a video-sized latent of zeros. The strength control determines how much of the original image content is preserved versus modified during video generation.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`positive`| Positive conditioning prompts for guiding the video generation| CONDITIONING| Yes| -  
`negative`| Negative conditioning prompts for avoiding certain elements in the video| CONDITIONING| Yes| -  
`vae`| VAE model used for encoding the input image into latent space| VAE| Yes| -  
`image`| Input image to be converted into video frames| IMAGE| Yes| -  
`width`| Output video width in pixels (default: 768, step: 32)| INT| Yes| 64 to MAX_RESOLUTION  
`height`| Output video height in pixels (default: 512, step: 32)| INT| Yes| 64 to MAX_RESOLUTION  
`length`| Number of frames in the generated video (default: 97, step: 8)| INT| Yes| 9 to MAX_RESOLUTION  
`batch_size`| Number of videos to generate simultaneously (default: 1)| INT| Yes| 1 to 4096  
`strength`| Control over how much of the original image content is preserved in the first frames of the generated video. A value of 1.0 preserves the original image completely, while 0.0 allows maximum modification (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
  
Note: `width` and `height` change in steps of 32 pixels, and `length` changes in steps of 8 frames, matching the video latent compression (32x in the spatial dimensions and 8x in the temporal dimension). The video latent contains ((length - 1) // 8) + 1 frames. The input image is resized to `width` x `height` using bilinear scaling with center cropping, and only the first three channels are used for encoding.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| The positive conditioning passed through unchanged for use with the generated latent| CONDITIONING  
`negative`| The negative conditioning passed through unchanged for use with the generated latent| CONDITIONING  
`latent`| Video latent representation containing the encoded image frames and a noise mask that controls how strongly the conditioning is applied during video generation| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideo/en.md)

* * *

**Source fingerprint (SHA-256):** `4ebc7f80b4d9ac3329e3349c7048885de22b827b5bdd102976687afd7e07a16b`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LTXVImgToVideo.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LTXVImgToVideo)

[LTXVGeneratedKeyframesToGuides - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LTXVGeneratedKeyframesToGuides)[LTXVImgToVideoInplace - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LTXVImgToVideoInplace)

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
