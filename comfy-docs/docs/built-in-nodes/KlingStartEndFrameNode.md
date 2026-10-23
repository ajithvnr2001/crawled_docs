---
url: https://docs.comfy.org/built-in-nodes/KlingStartEndFrameNode/
title: KlingStartEndFrameNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:15.905120+00:00
---

# KlingStartEndFrameNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/KlingStartEndFrameNode/

Kling

# KlingStartEndFrameNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node creates a video sequence that transitions between your provided start and end images.

Copy pageCopy page

This node creates a video sequence that transitions between your provided start and end images. It generates all the frames in between to produce a smooth transformation from the first frame to the last frame. This node calls the image-to-video API but only supports the input options that work with the `image_tail` request field.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`start_frame`| Reference Image - URL or Base64 encoded string, cannot exceed 10MB, resolution not less than 300*300px, aspect ratio between 1:2.5 ~ 2.5:1. Base64 should not include data:image prefix.| IMAGE| Yes| -  
`end_frame`| Reference Image - End frame control. URL or Base64 encoded string, cannot exceed 10MB, resolution not less than 300*300px. Base64 should not include data:image prefix.| IMAGE| Yes| -  
`prompt`| Positive text prompt. Must not be empty and cannot exceed 500 characters.| STRING| Yes| -  
`negative_prompt`| Negative text prompt. Cannot exceed 500 characters. If left empty, it is omitted from the request.| STRING| Yes| -  
`cfg_scale`| Controls the strength of the prompt guidance (default: 0.5).| FLOAT| Yes| 0.0-1.0  
`aspect_ratio`| The aspect ratio for the generated video (default: “16:9”).| COMBO| Yes| ”16:9"  
"9:16"  
"1:1”  
`mode`| The configuration to use for the video generation following the format: mode / duration / model_name. (default: “pro mode / 5s duration / kling-v2-5-turbo”)| COMBO| Yes| ”pro mode / 5s duration / kling-v2-5-turbo"  
"pro mode / 10s duration / kling-v2-5-turbo”  
  
**Image Constraints:**

  * Both `start_frame` and `end_frame` are required and cannot exceed 10MB in file size.
  * Minimum resolution: 300×300 pixels for both images.
  * `start_frame` aspect ratio must be between 1:2.5 and 2.5:1.
  * Base64 encoded images should not include the “data:image” prefix.

**Prompt Constraints:**

  * `prompt` must not be empty and cannot exceed 500 characters.
  * `negative_prompt` cannot exceed 500 characters; when empty, it is not sent with the request.

**Mode Notes:**

  * Both mode options use pro mode with the kling-v2-5-turbo model and differ only in duration (5 seconds or 10 seconds).
  * Pricing per generation, as shown in the node’s price badge: 5s mode costs 0.35USDand10smodecosts0.35 USD and 10s mode costs 0.35USDand10smodecosts0.70 USD.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated video sequence.| VIDEO  
`video_id`| Unique identifier for the generated video.| STRING  
`duration`| Duration of the generated video.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingStartEndFrameNode/en.md)

* * *

**Source fingerprint (SHA-256):** `a27977226360a425614255f8330ce7fd8ba94b8c3020eb8fdddc01eb74f035c1`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/KlingStartEndFrameNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/KlingStartEndFrameNode)

[KlingOmniProVideoToVideoNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/KlingOmniProVideoToVideoNode)[KlingTextToVideoNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/KlingTextToVideoNode)

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
