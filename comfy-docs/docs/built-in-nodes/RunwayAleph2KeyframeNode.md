---
url: https://docs.comfy.org/built-in-nodes/RunwayAleph2KeyframeNode/
title: RunwayAleph2KeyframeNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:52.928472+00:00
---

# RunwayAleph2KeyframeNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/RunwayAleph2KeyframeNode/

Runway

# RunwayAleph2KeyframeNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Runway Aleph2 Keyframe node anchors a guidance image to a specific moment of your input video

Copy pageCopy page

Runway Aleph2 Keyframe node anchors a guidance image to a specific moment of your input video, so the Aleph2 model steers the edit at that point in your footage. Connect this node to the “keyframes” input of the Runway Aleph2 Video to Video node, and chain several together (up to 5) via the optional “keyframes” input.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The guidance image to apply at the chosen moment of the input video.| IMAGE| Yes| -  
`timing`| How to place this image on the input video’s timeline.| COMBO| Yes| ”Absolute seconds"  
"Fraction of duration”  
`keyframes`| Optional earlier keyframes to chain with this one.| KEYFRAME| No| -  
  
### 

​

Timing Parameter Details

The `timing` parameter has two modes:

  * **“Absolute seconds”** : When selected, a `seconds` sub-parameter appears. This specifies the time in seconds from the start of the input video where the image applies (default: 0.0, range: 0.0 to 30.0, step 0.1).
  * **“Fraction of duration”** : When selected, a `fraction` sub-parameter appears. This specifies where in the input video the image applies as a fraction of its duration, where 0.0 is the start and 1.0 is the end (default: 0.0, range: 0.0 to 1.0, step 0.01).



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`keyframes`| A chain of keyframes including this one and any previously connected keyframes.| KEYFRAME  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayAleph2KeyframeNode/en.md)

* * *

**Source fingerprint (SHA-256):** `b5ac6553166b7366fd35f97740861be163f91bc2353f5f83bdc2f04bf40f8478`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/RunwayAleph2KeyframeNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/RunwayAleph2KeyframeNode)

[PrunaTextToVideoNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/PrunaTextToVideoNode)[RunwayAleph2PromptImageNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/RunwayAleph2PromptImageNode)

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
