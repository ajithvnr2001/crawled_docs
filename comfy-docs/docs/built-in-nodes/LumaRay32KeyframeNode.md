---
url: https://docs.comfy.org/built-in-nodes/LumaRay32KeyframeNode/
title: LumaRay32KeyframeNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:27.801028+00:00
---

# LumaRay32KeyframeNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LumaRay32KeyframeNode/

Luma

# LumaRay32KeyframeNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node anchors a guide image to a specific position on the Luma Ray 3.2 output video timeline.

Copy pageCopy page

This node anchors a guide image to a specific position on the Luma Ray 3.2 output video timeline. Connect this node to the “keyframes” input of the Luma Ray 3.2 Keyframes to Video node, and chain several keyframes together by connecting the optional “keyframes” input.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| Guide image to place at the chosen moment of the output video.| IMAGE| Yes| -  
`position`| How to place this image on the output video’s timeline.| DYNAMIC_COMBO| Yes| ”Fraction of duration (0.0-1.0)"  
"Absolute time (seconds)“  
`keyframes`| Optional earlier keyframes to chain with this one.| LUMA_RAY32_KEYFRAME| No| -  
  
### 

​

Fraction of duration (0.0-1.0) Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`fraction`| Where in the output video this image applies (0.0 = start, 1.0 = end). Default: 0.0.| FLOAT| Yes| 0.0 to 1.0 (step: 0.01)  
  
### 

​

Absolute time (seconds) Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`seconds`| Time in seconds from the start of the output video where this image applies. Default: 0.0.| FLOAT| Yes| 0.0 to 10.0 (step: 0.1)  
  
The `position` parameter determines which value is used to place the image on the timeline. Only the sub-parameter belonging to the selected option is shown and used: `fraction` for “Fraction of duration (0.0-1.0)” and `seconds` for “Absolute time (seconds)”.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`keyframes`| A keyframe chain that includes the new keyframe combined with any optional earlier keyframes.| LUMA_RAY32_KEYFRAME  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32KeyframeNode/en.md)

* * *

**Source fingerprint (SHA-256):** `b49d879888e6e83d6937068e799ea583ed5c90284e829ac496821eea330fe9c7`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LumaRay32KeyframeNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LumaRay32KeyframeNode)

[LumaRay32ImageToVideoNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LumaRay32ImageToVideoNode)[LumaRay32KeyframesToVideoNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LumaRay32KeyframesToVideoNode)

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
