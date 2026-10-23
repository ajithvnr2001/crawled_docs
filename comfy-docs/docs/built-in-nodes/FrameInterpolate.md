---
url: https://docs.comfy.org/built-in-nodes/FrameInterpolate/
title: FrameInterpolate - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:58.517943+00:00
---

# FrameInterpolate - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/FrameInterpolate/

Video

# FrameInterpolate - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Frame Interpolate node creates new frames between existing ones in a sequence of images, effectively increasing the frame rate.

Copy pageCopy page

The Frame Interpolate node creates new frames between existing ones in a sequence of images, effectively increasing the frame rate. It uses an AI model to predict what the intermediate frames should look like, which can be used to create smooth slow-motion effects or to increase the smoothness of a video.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`interp_model`| The frame interpolation model to use for generating intermediate frames| INTERP_MODEL| Yes| -  
`images`| A batch of consecutive images (frames) to interpolate between. Requires at least 2 images. If fewer than 2 frames are provided, the node returns the input images unchanged.| IMAGE| Yes| -  
`multiplier`| The number of times to multiply the frame count. For example, a multiplier of 2 doubles the number of frames. (default: 2)| INT| Yes| 2 to 16  
  
**Note:** The node requires at least 2 input frames and a `multiplier` of at least 2. If either condition is not met, the input images are returned unchanged.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`IMAGE`| A new batch of images with the interpolated frames inserted between the original frames, resulting in a smoother sequence. The total number of output frames is `(number of input frames - 1) * multiplier + 1`.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolate/en.md)

* * *

**Source fingerprint (SHA-256):** `e0b9dd6ec3b09e665bcc0f95d2b7a0209d9045ba9b96828e46f126e6914f049c`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/FrameInterpolate.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/FrameInterpolate)

[CreateVideo - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/CreateVideo)[GetVideoComponents - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/GetVideoComponents)

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
