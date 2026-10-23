---
url: https://docs.comfy.org/built-in-nodes/HappyHorseVideoEditApi/
title: HappyHorseVideoEditApi - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:02.926317+00:00
---

# HappyHorseVideoEditApi - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/HappyHorseVideoEditApi/

Wan

# HappyHorseVideoEditApi - ComfyUI Built-in Node Documentation

Copy pageCopy page

Edit a video using text instructions or reference images with the HappyHorse model.

Copy pageCopy page

Edit a video using text instructions or reference images with the HappyHorse model. Output duration is 3-15 seconds and matches the input video; inputs longer than 15 seconds are truncated.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The HappyHorse video editing model to use. This selection determines which prompt, resolution, ratio, and reference image options are available.| DYNAMIC_COMBO| Yes| ”happyhorse-1.0-video-edit”  
`video`| The video to edit.| VIDEO| Yes| 3 to 60 seconds  
`seed`| Seed to use for generation (default: 0).| INT| Yes| 0 to 2147483647  
`watermark`| Whether to add an AI-generated watermark to the result (default: False). Advanced parameter.| BOOLEAN| Yes| True  
False  
  
### 

​

happyhorse-1.0-video-edit Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Editing instructions or style transfer requirements. Must be at least 1 character long.| STRING| Yes| -  
`resolution`| The output resolution.| COMBO| Yes| ”720P"  
"1080P”  
`ratio`| Aspect ratio. If not changed, approximates the input video ratio.| COMBO| Yes| ”16:9"  
"9:16"  
"1:1"  
"4:3"  
"3:4”  
  
### 

​

Reference Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`reference_images`| Growable slot: connect 0 to 5 reference images (`image1`…`image5`) to guide the edit.| IMAGE| No| 0 to 5 images  
  
**Note:** The input video must be 3 to 60 seconds long. The output duration is 3-15 seconds and matches the input video; input videos longer than 15 seconds are truncated. The `prompt` must be at least 1 character long.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`video`| The edited video output.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseVideoEditApi/en.md)

* * *

**Source fingerprint (SHA-256):** `396cad4b5a06d457746a421050df98c892fa9db6019e3de983b4d0c417842b57`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/HappyHorseVideoEditApi.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/HappyHorseVideoEditApi)

[HappyHorseTextToVideoApi - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/HappyHorseTextToVideoApi)[Wan2ImageToVideoApi - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Wan2ImageToVideoApi)

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
