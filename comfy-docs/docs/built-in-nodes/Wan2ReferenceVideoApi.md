---
url: https://docs.comfy.org/built-in-nodes/Wan2ReferenceVideoApi/
title: Wan2ReferenceVideoApi - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:21.937946+00:00
---

# Wan2ReferenceVideoApi - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Wan2ReferenceVideoApi/

Wan

# Wan2ReferenceVideoApi - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node generates a video featuring a person or object based on provided reference materials.

Copy pageCopy page

This node generates a video featuring a person or object based on provided reference materials. It uses the Wan 2.7 model to create videos from a text prompt, supporting single-character performances and multi-character interactions. You must provide at least one reference video or reference image for the generation to work.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The specific model to use for video generation.| DYNAMIC_COMBO| Yes| ”wan2.7-r2v”  
`seed`| Seed to use for generation, which helps control the randomness of the output (default: 0).| INT| Yes| 0 to 2147483647  
`watermark`| Whether to add an AI-generated watermark to the result (default: False). This is an advanced setting.| BOOLEAN| Yes| True  
False  
  
### 

​

wan2.7-r2v Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Prompt describing the video. Use identifiers such as ‘character1’ and ‘character2’ to refer to the reference characters. Must contain at least one character.| STRING| Yes| -  
`negative_prompt`| Negative prompt describing what to avoid (default: empty).| STRING| No| -  
`resolution`| The resolution of the output video.| COMBO| Yes| ”720P"  
"1080P”  
`ratio`| The aspect ratio of the output video.| COMBO| Yes| ”16:9"  
"9:16"  
"1:1"  
"4:3"  
"3:4”  
`duration`| The length of the generated video in seconds (default: 5).| INT| Yes| 2 to 10  
  
### 

​

Reference Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`reference_videos`| Growable slot: connect up to 3 reference videos (slots `video1` to `video3`). At least one reference video or image is required overall.| VIDEO| No| 0 to 3 items  
`reference_images`| Growable slot: connect up to 5 reference images (slots `image1` to `image5`). At least one reference video or image is required overall.| IMAGE| No| 0 to 5 items  
  
**Important Constraints:**

  * You must provide at least one reference video or reference image in the `reference_videos` or `reference_images` inputs. Otherwise the node raises an error.
  * The total combined number of reference videos and reference images cannot exceed 5.
  * The `prompt` input must contain at least one character.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated video file.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2ReferenceVideoApi/en.md)

* * *

**Source fingerprint (SHA-256):** `52ac550522bf3fe8f57444ce8586fe83be470b893ff8c01292743553cfbd623d`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Wan2ReferenceVideoApi.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Wan2ReferenceVideoApi)

[Wan2ImageToVideoApi - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Wan2ImageToVideoApi)[Wan2TextToVideoApi - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Wan2TextToVideoApi)

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
