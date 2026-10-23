---
url: https://docs.comfy.org/built-in-nodes/ByteDanceTextToVideoNode/
title: ByteDanceTextToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:31.007968+00:00
---

# ByteDanceTextToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ByteDanceTextToVideoNode/

Bytedance

# ByteDanceTextToVideoNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ByteDance Text to Video node generates a video using ByteDance models through an API based on a text prompt.

Copy pageCopy page

The ByteDance Text to Video node generates a video using ByteDance models through an API based on a text prompt. You provide a prompt and choose settings such as the model, resolution, aspect ratio, and duration; the node submits the generation request and returns the generated video.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The ByteDance model used to generate the video (default: `"seedance-1-0-pro-fast-251015"`).| COMBO| Yes| `"seedance-1-5-pro-251215"`  
`"seedance-1-0-pro-250528"`  
`"seedance-1-0-pro-fast-251015"`  
`prompt`| The text prompt used to generate the video.| STRING| Yes| -  
`resolution`| The resolution of the output video.| COMBO| Yes| `"480p"`  
`"720p"`  
`"1080p"`  
`aspect_ratio`| The aspect ratio of the output video.| COMBO| Yes| `"16:9"`  
`"4:3"`  
`"1:1"`  
`"3:4"`  
`"9:16"`  
`"21:9"`  
`duration`| The duration of the output video in seconds (default: 5).| INT| Yes| 3 to 12  
`seed`| Seed to use for generation (default: 0).| INT| No| 0 to 2147483647  
`camera_fixed`| Specifies whether to fix the camera. The platform appends an instruction to fix the camera to your prompt, but does not guarantee the actual effect (default: False).| BOOLEAN| No| -  
`watermark`| Whether to add an “AI generated” watermark to the video (default: False).| BOOLEAN| No| -  
`generate_audio`| This parameter is ignored for any model except `seedance-1-5-pro-251215` (default: False).| BOOLEAN| No| -  
  
**Parameter Constraints:**

  * The `prompt` parameter must contain at least 1 character after whitespace removal.
  * The `prompt` parameter cannot contain the following text parameters: “resolution”, “ratio”, “duration”, “seed”, “camerafixed”, “watermark”.
  * The node builds the final prompt by appending the selected `resolution`, `aspect_ratio`, `duration`, `seed`, `camera_fixed`, and `watermark` settings to the prompt text.
  * The `duration` parameter is limited to values between 3 and 12 seconds. For the `seedance-1-5-pro-251215` model, the minimum supported duration is 4 seconds.
  * The `seed` parameter accepts values from 0 to 2,147,483,647.
  * The `generate_audio` parameter only has an effect when the `model` is set to `seedance-1-5-pro-251215`; it is ignored for all other models.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated video file| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceTextToVideoNode/en.md)

* * *

**Source fingerprint (SHA-256):** `83b805b63e59a76cae378b0407b409e1bfe900677ef1e01fc836fede47283eee`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ByteDanceTextToVideoNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ByteDanceTextToVideoNode)

[ByteDanceImageToVideoNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ByteDanceImageToVideoNode)[ByteDanceVideoEnhanceNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ByteDanceVideoEnhanceNode)

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
