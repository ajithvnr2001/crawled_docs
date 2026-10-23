---
url: https://docs.comfy.org/built-in-nodes/LumaRay32VideoReframeNode/
title: LumaRay32VideoReframeNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:28.281342+00:00
---

# LumaRay32VideoReframeNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LumaRay32VideoReframeNode/

Luma

# LumaRay32VideoReframeNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node changes the aspect ratio of an existing video using Luma Ray 3.2, which fills the newly exposed canvas areas with generated content.

Copy pageCopy page

This node changes the aspect ratio of an existing video using Luma Ray 3.2, which fills the newly exposed canvas areas with generated content. The source video can be up to 30 seconds long, and billing is per second of output.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`video`| Source video to reframe. Up to 30 seconds.| VIDEO| Yes| -  
`prompt`| Describes how the newly exposed canvas areas should be filled.| STRING| Yes| Min length: 1 character  
Max length: 6000 characters  
`aspect_ratio`| The target aspect ratio for the reframed video (default: “16:9”).| STRING| Yes| ”16:9"  
"9:16"  
"1:1"  
"4:3"  
"3:4"  
"21:9”  
`resolution`| The output resolution of the reframed video (default: “720p”).| STRING| Yes| ”360p"  
"540p"  
"720p"  
"1080p”  
`seed`| Seed for reproducible generation.| INT| Yes| -  
  
**Note:** The `1080p` resolution is not available for vertical aspect ratios (`9:16` and `3:4`) when reframing.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`video`| The reframed video with the new aspect ratio and filled canvas areas.| VIDEO  
`generation_id`| The unique identifier for the generation request.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32VideoReframeNode/en.md)

* * *

**Source fingerprint (SHA-256):** `d35ff5b63a850e4e44a40857188918ab5cde00b9159e3720a189a81807cfa7cb`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LumaRay32VideoReframeNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LumaRay32VideoReframeNode)

[LumaRay32VideoEditNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LumaRay32VideoEditNode)[LumaVideoNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LumaVideoNode)

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
