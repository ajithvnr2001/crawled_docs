---
url: https://docs.comfy.org/built-in-nodes/GrokVideoExtendNode/
title: GrokVideoExtendNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:02.032494+00:00
---

# GrokVideoExtendNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/GrokVideoExtendNode/

Grok

# GrokVideoExtendNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Grok Video Extend node extends an existing video with a seamless continuation based on a text prompt.

Copy pageCopy page

The Grok Video Extend node extends an existing video with a seamless continuation based on a text prompt. Provide a short source video and describe what should happen next; the node returns a new video clip that continues from the original.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The model to use for video extension. Selecting the `"grok-imagine-video"` option reveals its model-specific settings.| DYNAMIC_COMBO| Yes| `"grok-imagine-video"`  
`prompt`| Text description of what should happen next in the video.| STRING| Yes| N/A  
`video`| Source video to extend. MP4 format, 2-15 seconds.| VIDEO| Yes| MP4, 2-15 seconds, maximum 50MB  
`seed`| Seed to determine if node should re-run; actual results are nondeterministic regardless of seed (default: 0).| INT| Yes| 0 to 2147483647  
  
### 

​

grok-imagine-video Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`duration`| Length of the extension in seconds (default: 8).| INT| Yes| 2 to 10  
  
**Parameter Constraints:**

  * The `video` input must be an MP4 file between 2 and 15 seconds in length and cannot exceed 50MB in file size.
  * The `prompt` must contain at least one character after whitespace is trimmed.
  * The `model` parameter is a dynamic combo. Selecting the `"grok-imagine-video"` option reveals the nested `duration` parameter.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The newly generated video extension.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoExtendNode/en.md)

* * *

**Source fingerprint (SHA-256):** `5009c007b6f93cd44f2742b024b65f1ac92ab9bca3b85a55554b1d99649e323b`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/GrokVideoExtendNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/GrokVideoExtendNode)

[GrokVideoEditNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/GrokVideoEditNode)[GrokVideoNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/GrokVideoNode)

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
