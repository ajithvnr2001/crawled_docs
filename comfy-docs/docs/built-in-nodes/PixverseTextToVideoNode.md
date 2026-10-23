---
url: https://docs.comfy.org/built-in-nodes/PixverseTextToVideoNode/
title: PixverseTextToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:42.888748+00:00
---

# PixverseTextToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/PixverseTextToVideoNode/

Pixverse

# PixverseTextToVideoNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generates videos from a text prompt using the PixVerse API.

Copy pageCopy page

Generates videos from a text prompt using the PixVerse API. The node lets you control the video’s shape, quality, length, and motion style, and can optionally apply a saved style template. It submits the request, waits for the generation to finish, and returns the finished video.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Prompt for the video generation (default: "")| STRING| Yes| Must contain at least 1 character  
`aspect_ratio`| Aspect ratio for the generated video| COMBO| Yes| `"16:9"`  
`"9:16"`  
`"1:1"`  
`quality`| Video quality setting (default: “540p”)| COMBO| Yes| `"540p"`  
`"1080p"`  
`duration_seconds`| Duration of the generated video in seconds| COMBO| Yes| `"5"`  
`"10"`  
`motion_mode`| Motion style for the video generation| COMBO| Yes| `"normal"`  
`"fast"`  
`seed`| Seed for video generation (default: 0)| INT| Yes| 0 to 2147483647  
`negative_prompt`| An optional text description of undesired elements on an image (default: "")| STRING| No| -  
`pixverse_template`| An optional template to influence style of generation, created by the PixVerse Template node| CUSTOM| No| -  
  
**Note:** The `prompt` must contain at least 1 character. When 1080p quality is selected, the motion mode is automatically set to `normal` and the duration is limited to 5 seconds. For any duration other than 5 seconds, the motion mode is also automatically set to `normal`.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated video file| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTextToVideoNode/en.md)

* * *

**Source fingerprint (SHA-256):** `cb95579dc6c9afa17455b0216ec46571ad2c0455606cf3b9c725ca512c45f938`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/PixverseTextToVideoNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/PixverseTextToVideoNode)

[PixverseTemplateNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/PixverseTemplateNode)[PixverseTransitionVideoNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/PixverseTransitionVideoNode)

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
