---
url: https://docs.comfy.org/built-in-nodes/KlingTextToVideoNode/
title: KlingTextToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:16.171673+00:00
---

# KlingTextToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/KlingTextToVideoNode/

Kling

# KlingTextToVideoNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Kling Text to Video node generates videos from text descriptions using the Kling video generation API.

Copy pageCopy page

The Kling Text to Video node generates videos from text descriptions using the Kling video generation API. It sends the prompt and settings (aspect ratio, generation mode, and CFG scale) to the API, waits for the generation task to complete, and then returns the resulting video along with its ID and duration.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Positive text prompt| STRING| Yes| Maximum 2500 characters  
`negative_prompt`| Negative text prompt| STRING| No| Maximum 2500 characters  
`cfg_scale`| Configuration scale value that controls how closely the video follows the prompt (default: 1.0)| FLOAT| No| 0.0 to 1.0  
`aspect_ratio`| Video aspect ratio setting (default: “16:9”)| COMBO| No| ”16:9"  
"9:16"  
"1:1”  
`mode`| The configuration to use for the video generation following the format: mode / duration / model_name (default: “pro mode / 5s duration / kling-v2-5-turbo”)| COMBO| No| ”pro mode / 5s duration / kling-v2-5-turbo"  
"pro mode / 10s duration / kling-v2-5-turbo”  
  
Note: The `prompt` parameter is required and must not be empty. Both `prompt` and `negative_prompt` are limited to a maximum of 2500 characters. The 10-second `mode` option costs more than the 5-second option.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated video output| VIDEO  
`video_id`| Unique identifier for the generated video| STRING  
`duration`| Duration information for the generated video| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoNode/en.md)

* * *

**Source fingerprint (SHA-256):** `6a63b0b8bc45dc5a6300cdfe7a373399eeead36de6727f7aae2c026ba0deaea8`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/KlingTextToVideoNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/KlingTextToVideoNode)

[KlingStartEndFrameNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/KlingStartEndFrameNode)[KlingTextToVideoWithAudio - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/KlingTextToVideoWithAudio)

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
