---
url: https://docs.comfy.org/built-in-nodes/RunwayImageToVideoNodeGen3a/
title: RunwayImageToVideoNodeGen3a - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:53.764810+00:00
---

# RunwayImageToVideoNodeGen3a - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/RunwayImageToVideoNodeGen3a/

Runway

# RunwayImageToVideoNodeGen3a - ComfyUI Built-in Node Documentation

Copy pageCopy page

Runway Image to Video (Gen3a Turbo) node generates a video from a single starting frame using Runway’s Gen3a Turbo model.

Copy pageCopy page

Runway Image to Video (Gen3a Turbo) node generates a video from a single starting frame using Runway’s Gen3a Turbo model. It takes a text prompt and an initial image frame, then creates a video sequence based on the specified duration and aspect ratio. The generation is processed remotely through Runway’s API. This node is marked as deprecated.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Text prompt for the generation (default: "")| STRING| Yes| N/A  
`start_frame`| Start frame to be used for the video| IMAGE| Yes| N/A  
`duration`| Duration of the generated video, in seconds (default: “5”)| COMBO| Yes| `"5"`  
`"10"`  
`ratio`| Aspect ratio of the generated video (default: “768:1280”)| COMBO| Yes| `"768:1280"`  
`"1280:768"`  
`seed`| Random seed for generation (default: 0)| INT| Yes| 0 to 4294967295  
  
**Parameter Constraints:**

  * The `prompt` must contain at least one character (it cannot be empty).
  * The `start_frame` accepts a single image (maximum of 1).
  * The `start_frame` must not exceed 7999 x 7999 pixels in dimensions.
  * The `start_frame` must have an aspect ratio between 1:2 and 2:1 (0.5 to 2.0).



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated video sequence| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayImageToVideoNodeGen3a/en.md)

* * *

**Source fingerprint (SHA-256):** `ff66cbdfa80aabeaf96d43e7822dd0c700ee027d13fb430a9dc2079e1a23f38e`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/RunwayImageToVideoNodeGen3a.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/RunwayImageToVideoNodeGen3a)

[RunwayFirstLastFrameNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/RunwayFirstLastFrameNode)[RunwayImageToVideoNodeGen4 - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/RunwayImageToVideoNodeGen4)

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
