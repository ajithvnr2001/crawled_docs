---
url: https://docs.comfy.org/built-in-nodes/WanFirstLastFrameToVideo/
title: WanFirstLastFrameToVideo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:24.018645+00:00
---

# WanFirstLastFrameToVideo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/WanFirstLastFrameToVideo/

Wan

# WanFirstLastFrameToVideo - ComfyUI Built-in Node Documentation

Copy pageCopy page

The WanFirstLastFrameToVideo node prepares conditioning for video generation by combining a start frame and an end frame with text prompts.

Copy pageCopy page

The WanFirstLastFrameToVideo node prepares conditioning for video generation by combining a start frame and an end frame with text prompts. It encodes the frame images into latent space, creates a mask that tells the video model which frames are already known, and attaches CLIP vision features when they are provided. The node outputs updated positive and negative conditioning plus an empty latent that defines the size and length of the video to generate.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`positive`| Positive text conditioning used to guide the video generation.| CONDITIONING| Yes| -  
`negative`| Negative text conditioning used to guide the video generation.| CONDITIONING| Yes| -  
`vae`| VAE model used to encode the combined frame images into latent space.| VAE| Yes| -  
`width`| Width of the generated video in pixels (default: 832, step: 16).| INT| Yes| 16 to MAX_RESOLUTION  
`height`| Height of the generated video in pixels (default: 480, step: 16).| INT| Yes| 16 to MAX_RESOLUTION  
`length`| Number of frames in the video sequence (default: 81, step: 4).| INT| Yes| 1 to MAX_RESOLUTION  
`batch_size`| Number of videos to generate at once (default: 1).| INT| Yes| 1 to 4096  
`clip_vision_start_image`| CLIP vision features extracted from the start image. If both start and end CLIP vision inputs are provided, their features are combined.| CLIP_VISION_OUTPUT| No| -  
`clip_vision_end_image`| CLIP vision features extracted from the end image. If both start and end CLIP vision inputs are provided, their features are combined.| CLIP_VISION_OUTPUT| No| -  
`start_image`| Starting frame image for the video sequence. Its first `length` frames are used and resized to `width` × `height`.| IMAGE| No| -  
`end_image`| Ending frame image for the video sequence. Its last `length` frames are used and resized to `width` × `height`.| IMAGE| No| -  
  
**Note:** When at least one of `start_image` or `end_image` is provided, the node builds a combined frame sequence where the start and end frames are filled in and the remaining frames use a neutral gray placeholder (0.5). A mask marks the filled regions as known and the placeholder regions as unknown, allowing the video model to generate the in-between frames. When a start image is provided, the known region also extends 3 extra frames beyond the image. The same encoded frame image and mask are attached to both `positive` and `negative` conditioning. If both CLIP vision inputs are provided, their hidden states are concatenated; if only one is provided, it is used on its own. The latent video length is derived from `length` after temporal compression: `((length - 1) // 4) + 1`.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| Positive conditioning with the encoded frame image, mask, and (if provided) CLIP vision features attached.| CONDITIONING  
`negative`| Negative conditioning with the encoded frame image, mask, and (if provided) CLIP vision features attached.| CONDITIONING  
`latent`| Empty latent tensor (all zeros) shaped for the given batch size, video length, and resolution.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFirstLastFrameToVideo/en.md)

* * *

**Source fingerprint (SHA-256):** `0072e441cb80334c3c961d1bbf2d081c78bc38ed1eacca840c577a2d01b36f05`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/WanFirstLastFrameToVideo.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/WanFirstLastFrameToVideo)

[Wan22ImageToVideoLatent - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Wan22ImageToVideoLatent)[WanImageToVideo - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/WanImageToVideo)

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
