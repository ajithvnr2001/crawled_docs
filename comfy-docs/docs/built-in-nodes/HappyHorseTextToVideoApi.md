---
url: https://docs.comfy.org/built-in-nodes/HappyHorseTextToVideoApi/
title: HappyHorseTextToVideoApi - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:02.674249+00:00
---

# HappyHorseTextToVideoApi - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/HappyHorseTextToVideoApi/

Wan

# HappyHorseTextToVideoApi - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generates a video based on a text prompt using the HappyHorse model.

Copy pageCopy page

Generates a video based on a text prompt using the HappyHorse model. This node sends your prompt and settings to the HappyHorse API, waits for the video to be generated, and then downloads the result.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The HappyHorse model used for generation, along with its sub-parameters. Selecting a model determines which sub-parameters are available (see the model sections below).| DYNAMIC_COMBO| Yes| ”happyhorse-1.1-t2v"  
"happyhorse-1.0-t2v”  
`seed`| Seed to use for generation. Using the same seed with the same inputs will produce the same result. (default: 0).| INT| Yes| 0 to 2147483647  
`watermark`| Whether to add an AI-generated watermark to the result. (default: False).| BOOLEAN| Yes| True / False  
  
### 

​

happyhorse-1.1-t2v Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Prompt describing the elements and visual features. Supports English and Chinese. (default: "").| STRING| Yes| -  
`resolution`| The resolution of the output video.| COMBO| Yes| ”720P"  
"1080P”  
`ratio`| The aspect ratio of the output video.| COMBO| Yes| ”16:9"  
"9:16"  
"1:1"  
"4:3"  
"3:4"  
"21:9"  
"9:21"  
"5:4"  
"4:5”  
`duration`| The length of the video in seconds. (default: 5, min: 3, max: 15, step: 1).| INT| Yes| 3 to 15  
  
### 

​

happyhorse-1.0-t2v Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Prompt describing the elements and visual features. Supports English and Chinese. (default: "").| STRING| Yes| -  
`resolution`| The resolution of the output video.| COMBO| Yes| ”720P"  
"1080P”  
`ratio`| The aspect ratio of the output video.| COMBO| Yes| ”16:9"  
"9:16"  
"1:1"  
"4:3"  
"3:4”  
`duration`| The length of the video in seconds. (default: 5, min: 3, max: 15, step: 1).| INT| Yes| 3 to 15  
  
Note: The prompt must not be empty; an error is raised if no prompt is provided. Both models support video durations from 3 to 15 seconds. The `happyhorse-1.1-t2v` model offers additional aspect ratios (`21:9`, `9:21`, `5:4`, `4:5`) that are not available with `happyhorse-1.0-t2v`.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`VIDEO`| The generated video file.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseTextToVideoApi/en.md)

* * *

**Source fingerprint (SHA-256):** `b60cfc3ce4935d7eb36bb28f9bd268446c4df5b437e06278b7e6d91d349d0238`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/HappyHorseTextToVideoApi.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/HappyHorseTextToVideoApi)

[HappyHorseReferenceVideoApi - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/HappyHorseReferenceVideoApi)[HappyHorseVideoEditApi - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/HappyHorseVideoEditApi)

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
