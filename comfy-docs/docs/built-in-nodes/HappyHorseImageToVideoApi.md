---
url: https://docs.comfy.org/built-in-nodes/HappyHorseImageToVideoApi/
title: HappyHorseImageToVideoApi - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:03.380239+00:00
---

# HappyHorseImageToVideoApi - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/HappyHorseImageToVideoApi/

Wan

# HappyHorseImageToVideoApi - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node generates a short video from a single starting image using the HappyHorse model.

Copy pageCopy page

This node generates a short video from a single starting image using the HappyHorse model. You provide a first frame image and a text prompt describing the desired motion and scene, and the node creates a video that continues from that image.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The HappyHorse model to use for video generation.| DYNAMIC_COMBO| Yes| `"happyhorse-1.1-i2v"`  
`"happyhorse-1.0-i2v"`  
`first_frame`| First frame image. The output aspect ratio is derived from this image.| IMAGE| Yes| 300×300 px min; 1:2.5 to 2.5:1  
`seed`| Seed to use for generation. (default: 0)| INT| Yes| 0 to 2147483647  
`watermark`| Whether to add an AI-generated watermark to the result. (advanced option; default: False)| BOOLEAN| Yes| True / False  
  
### 

​

happyhorse-1.1-i2v and happyhorse-1.0-i2v Inputs

Both model versions share the same set of parameters.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Prompt describing the elements and visual features. Supports English and Chinese. (default: "")| STRING| No| N/A  
`resolution`| The output video resolution. (default: `"720P"`)| COMBO| Yes| `"720P"`  
`"1080P"`  
`duration`| The duration of the generated video in seconds. (default: 5)| INT| Yes| 3 to 15  
  
Note: The `first_frame` image must be at least 300x300 pixels, and its aspect ratio must be between 1:2.5 and 2.5:1.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`video`| The generated video file.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseImageToVideoApi/en.md)

* * *

**Source fingerprint (SHA-256):** `4bf6eece0d1b4104ce2d84e29b2c918a0a6ba782da1dd801b66cbfa1666d150b`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/HappyHorseImageToVideoApi.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/HappyHorseImageToVideoApi)

[ViduTextToVideoNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ViduTextToVideoNode)[HappyHorseReferenceVideoApi - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/HappyHorseReferenceVideoApi)

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
