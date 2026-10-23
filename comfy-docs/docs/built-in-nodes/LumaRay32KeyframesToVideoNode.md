---
url: https://docs.comfy.org/built-in-nodes/LumaRay32KeyframesToVideoNode/
title: LumaRay32KeyframesToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:28.119103+00:00
---

# LumaRay32KeyframesToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LumaRay32KeyframesToVideoNode/

Luma

# LumaRay32KeyframesToVideoNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node generates a video that interpolates through a sequence of guide images, each anchored to a specific position on the timeline, using Luma Ray 3.2.

Copy pageCopy page

This node generates a video that interpolates through a sequence of guide images, each anchored to a specific position on the timeline, using Luma Ray 3.2. Build the keyframe sequence using Luma Ray 3.2 Keyframe nodes, connecting at least 2 keyframes to define the animation.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Text prompt for the video generation (default: empty string).| STRING| Yes| 1 to 6000 characters  
`resolution`| The output resolution of the generated video (default: “720p”).| STRING| Yes| `"360p"`  
`"540p"`  
`"720p"`  
`"1080p"`  
`duration`| The duration of the generated video (default: “5s”).| STRING| Yes| `"5s"`  
`"10s"`  
`seed`| Seed for random number generation to control reproducibility.| INT| Yes| 0 to 4294967295  
`keyframes`| Keyframe sequence from Luma Ray 3.2 Keyframe nodes (at least 2).| LUMA_RAY32_KEYFRAME| Yes| 2 to 64 keyframes  
  
**Note:** The keyframe sequence must contain at least 2 keyframes and at most 64 keyframes. Each keyframe must have a distinct position on the timeline. Keyframe positions are resolved to output frame indices based on the selected duration (120 frames for 5s, 240 frames for 10s). Keyframe positions in seconds mode must not exceed the total video duration.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`video`| The generated video output.| VIDEO  
`generation_id`| The unique identifier for the generation request.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32KeyframesToVideoNode/en.md)

* * *

**Source fingerprint (SHA-256):** `28099e5990942860a20e23cfd5c71a36b23a6264b44097ca617f8bdd06e7857a`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LumaRay32KeyframesToVideoNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LumaRay32KeyframesToVideoNode)

[LumaRay32KeyframeNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LumaRay32KeyframeNode)[LumaRay32TextToVideoNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LumaRay32TextToVideoNode)

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
