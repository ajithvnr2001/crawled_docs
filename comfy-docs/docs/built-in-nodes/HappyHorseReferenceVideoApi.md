---
url: https://docs.comfy.org/built-in-nodes/HappyHorseReferenceVideoApi/
title: HappyHorseReferenceVideoApi - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:02.575888+00:00
---

# HappyHorseReferenceVideoApi - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/HappyHorseReferenceVideoApi/

Wan

# HappyHorseReferenceVideoApi - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node generates a video featuring a person or object from reference images using the HappyHorse model.

Copy pageCopy page

This node generates a video featuring a person or object from reference images using the HappyHorse model. It supports single-character performances and multi-character interactions. The reference images are uploaded and used to represent the characters in the generated video.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The HappyHorse reference-to-video model to use for generation.| DYNAMIC_COMBO| Yes| `"happyhorse-1.1-r2v"`  
`"happyhorse-1.0-r2v"`  
`seed`| Seed to use for generation (default: 0). Can be set to automatically change after each generation.| INT| Yes| 0 to 2147483647  
`watermark`| Whether to add an AI-generated watermark to the result (default: False).| BOOLEAN| Yes| True or False  
  
### 

​

HappyHorse 1.1 Inputs (happyhorse-1.1-r2v)

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Prompt describing the video. Use identifiers such as ‘character1’ and ‘character2’ to refer to the reference characters.| STRING| Yes| N/A  
`resolution`| The resolution of the generated video.| COMBO| Yes| `"720P"`  
`"1080P"`  
`ratio`| The aspect ratio of the generated video.| COMBO| Yes| `"16:9"`  
`"9:16"`  
`"1:1"`  
`"4:3"`  
`"3:4"`  
`"21:9"`  
`"9:21"`  
`"5:4"`  
`"4:5"`  
`duration`| The duration of the generated video in seconds (default: 5).| INT| Yes| 3 to 15  
  
### 

​

HappyHorse 1.0 Inputs (happyhorse-1.0-r2v)

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Prompt describing the video. Use identifiers such as ‘character1’ and ‘character2’ to refer to the reference characters.| STRING| Yes| N/A  
`resolution`| The resolution of the generated video.| COMBO| Yes| `"720P"`  
`"1080P"`  
`ratio`| The aspect ratio of the generated video.| COMBO| Yes| `"16:9"`  
`"9:16"`  
`"1:1"`  
`"4:3"`  
`"3:4"`  
`duration`| The duration of the generated video in seconds (default: 5).| INT| Yes| 3 to 15  
  
### 

​

Reference Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`reference_images`| Growable slot: connect 1 to 9 reference images of the person or object to feature in the video. At least one reference image must be provided.| IMAGE| Yes| 1 to 9 (per model)  
  
Note: At least one reference image must be provided, otherwise the node raises an error. Each reference image must be at least 400 x 400 pixels and have an aspect ratio between 1:2.5 and 2.5:1. The prompt must not be empty.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`VIDEO`| The generated video file.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseReferenceVideoApi/en.md)

* * *

**Source fingerprint (SHA-256):** `252c918afc4cf38be9c7d09b7112075b9adb23490ec9fed1717a8548519d2554`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/HappyHorseReferenceVideoApi.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/HappyHorseReferenceVideoApi)

[HappyHorseImageToVideoApi - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/HappyHorseImageToVideoApi)[HappyHorseTextToVideoApi - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/HappyHorseTextToVideoApi)

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
