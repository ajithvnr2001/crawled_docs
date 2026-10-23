---
url: https://docs.comfy.org/built-in-nodes/WanReferenceVideoApi/
title: WanReferenceVideoApi - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:25.341556+00:00
---

# WanReferenceVideoApi - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/WanReferenceVideoApi/

Wan

# WanReferenceVideoApi - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Wan Reference to Video node uses the visual appearance and voice from one or more input reference videos, along with a text prompt, to generate a new video.

Copy pageCopy page

The Wan Reference to Video node uses the visual appearance and voice from one or more input reference videos, along with a text prompt, to generate a new video. It maintains consistency with the characters from the reference material while creating new content based on your description.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The specific AI model to use for video generation.| COMBO| Yes| `"wan2.6-r2v"`  
`prompt`| A description of the elements and visual features for the new video. Supports English and Chinese. Use identifiers like `character1` and `character2` to refer to the characters from the reference videos.| STRING| Yes| -  
`negative_prompt`| A description of elements or features to avoid in the generated video.| STRING| No| -  
`reference_videos`| A list of video inputs used as references for character appearance and voice. You must provide at least one video. Each video can be assigned a name like `character1`, `character2`, or `character3`.| AUTOGROW| Yes| -  
`size`| The resolution and aspect ratio for the output video.| COMBO| Yes| `"720p: 1:1 (960x960)"`  
`"720p: 16:9 (1280x720)"`  
`"720p: 9:16 (720x1280)"`  
`"720p: 4:3 (1088x832)"`  
`"720p: 3:4 (832x1088)"`  
`"1080p: 1:1 (1440x1440)"`  
`"1080p: 16:9 (1920x1080)"`  
`"1080p: 9:16 (1080x1920)"`  
`"1080p: 4:3 (1632x1248)"`  
`"1080p: 3:4 (1248x1632)"`  
`duration`| The length of the generated video in seconds (default: 5).| INT| Yes| 5 to 10  
`seed`| A random seed value for reproducible results. A value of 0 will generate a random seed.| INT| No| 0 to 2147483647  
`shot_type`| Specifies whether the generated video is a single continuous shot or contains multiple shots with cuts.| COMBO| Yes| `"single"`  
`"multi"`  
`watermark`| When enabled, an AI-generated watermark is added to the final video (default: False).| BOOLEAN| No| -  
  
**Constraints:**

  * Each video provided in `reference_videos` must be between 2 and 30 seconds in duration.
  * The `duration` parameter is limited to values of 5 or 10 seconds.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The newly generated video file.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanReferenceVideoApi/en.md)

* * *

**Source fingerprint (SHA-256):** `65ca81a7b5e83f8d8f4c00db41e24d5238ef438887362838351464e77a3af0c2`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/WanReferenceVideoApi.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/WanReferenceVideoApi)

[WanImageToVideoApi - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/WanImageToVideoApi)[WanTextToVideoApi - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/WanTextToVideoApi)

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
