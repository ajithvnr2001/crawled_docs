---
url: https://docs.comfy.org/built-in-nodes/Wan2VideoContinuationApi/
title: Wan2VideoContinuationApi - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:22.133026+00:00
---

# Wan2VideoContinuationApi - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Wan2VideoContinuationApi/

Wan

# Wan2VideoContinuationApi - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Wan 2.7 Video Continuation node generates a new video segment that continues from the end of an input video clip.

Copy pageCopy page

The Wan 2.7 Video Continuation node generates a new video segment that continues from the end of an input video clip. It uses the Wan 2.7 model to synthesize the continuation based on a text prompt and can optionally guide the ending towards a specific target frame.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The video generation model to use. The selected option determines which additional settings appear below.| DYNAMIC_COMBO| Yes| `"wan2.7-i2v"`  
`first_clip`| Input video to continue from. Duration: 2s-10s. The output aspect ratio is derived from this video.| VIDEO| Yes| 2s to 10s  
`last_frame`| Last frame image. The continuation will transition towards this frame.| IMAGE| No| -  
`seed`| Seed to use for generation. (default: 0)| INT| Yes| 0 to 2147483647  
`prompt_extend`| Whether to enhance the prompt with AI assistance. (default: True)| BOOLEAN| Yes| -  
`watermark`| Whether to add an AI-generated watermark to the result. (default: False)| BOOLEAN| Yes| -  
  
### 

​

wan2.7-i2v Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Prompt describing the elements and visual features. Supports English and Chinese. (default: empty string)| STRING| Yes| -  
`negative_prompt`| Negative prompt describing what to avoid. (default: empty string)| STRING| Yes| -  
`resolution`| The output resolution for the generated video.| COMBO| Yes| `"720P"`  
`"1080P"`  
`duration`| Total output duration in seconds. The model generates continuation to fill the remaining time after the input clip. (default: 5)| INT| Yes| 2 to 15  
  
**Note:** The `first_clip` input video must be between 2 and 10 seconds in duration.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated video continuation.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2VideoContinuationApi/en.md)

* * *

**Source fingerprint (SHA-256):** `591e551676969bc1fedb5f820f6866512c132bb98ee8ef1766d1e0b389e2dc11`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Wan2VideoContinuationApi.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Wan2VideoContinuationApi)

[Wan2TextToVideoApi - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Wan2TextToVideoApi)[Wan2VideoEditApi - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Wan2VideoEditApi)

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
