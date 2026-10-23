---
url: https://docs.comfy.org/built-in-nodes/RunwayFirstLastFrameNode/
title: RunwayFirstLastFrameNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:53.551293+00:00
---

# RunwayFirstLastFrameNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/RunwayFirstLastFrameNode/

Runway

# RunwayFirstLastFrameNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Runway First-Last-Frame to Video node generates a video using a start frame, an end frame, and a text prompt.

Copy pageCopy page

The Runway First-Last-Frame to Video node generates a video using a start frame, an end frame, and a text prompt. It creates a smooth transition between the two provided keyframes using Runway’s gen3a_turbo model. It is especially useful for complex transitions where the end frame is completely different from the start frame.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Text prompt for the generation (default: empty string)| STRING| Yes| N/A  
`start_frame`| Start frame to be used for the video| IMAGE| Yes| N/A  
`end_frame`| End frame to be used for the video. Supported for gen3a_turbo only.| IMAGE| Yes| N/A  
`duration`| Duration of the generated video in seconds. The longer 10s duration gives the generation more time to smoothly transition between the start and end frames (default: “5”).| COMBO| Yes| `"5"`  
`"10"`  
`ratio`| Aspect ratio for the generated video (default: “768:1280”)| COMBO| Yes| `"768:1280"`  
`"1280:768"`  
`seed`| Random seed for generation (default: 0)| INT| Yes| 0 to 4294967295  
  
**Parameter Constraints:**

  * The `prompt` must contain at least 1 character
  * Both `start_frame` and `end_frame` must have maximum dimensions of 7999x7999 pixels
  * Both `start_frame` and `end_frame` must have aspect ratios between 0.5 and 2.0
  * The `end_frame` parameter is only supported when using the gen3a_turbo model

**Notes:**

  * The generation cost is based on the selected duration: USD 0.0715 per second (USD 0.3575 for 5 seconds, USD 0.715 for 10 seconds)
  * This node is marked as deprecated



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated video transitioning between the start and end frames| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayFirstLastFrameNode/en.md)

* * *

**Source fingerprint (SHA-256):** `1d8720aba833348583d2aa37e13a1ad43d9055b0201c9cb6ad9c95dada7e5056`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/RunwayFirstLastFrameNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/RunwayFirstLastFrameNode)

[RunwayAleph2VideoToVideoNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/RunwayAleph2VideoToVideoNode)[RunwayImageToVideoNodeGen3a - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/RunwayImageToVideoNodeGen3a)

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
