---
url: https://docs.comfy.org/built-in-nodes/Vidu2StartEndToVideoNode/
title: Vidu2StartEndToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:19.701893+00:00
---

# Vidu2StartEndToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Vidu2StartEndToVideoNode/

Vidu

# Vidu2StartEndToVideoNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node generates a video by interpolating between a provided start frame and an end frame, guided by a text prompt.

Copy pageCopy page

This node generates a video by interpolating between a provided start frame and an end frame, guided by a text prompt. It uses a specified Vidu model to create a smooth transition between the two images over a set duration.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The Vidu model to use for video generation.| COMBO| Yes| `"viduq2-pro-fast"`  
`"viduq2-pro"`  
`"viduq2-turbo"`  
`first_frame`| The starting image for the video sequence. Only a single image is allowed.| IMAGE| Yes| -  
`end_frame`| The ending image for the video sequence. Only a single image is allowed.| IMAGE| Yes| -  
`prompt`| Prompt description (max 2000 characters).| STRING| Yes| -  
`duration`| The length of the generated video in seconds (default: 5).| INT| No| 2 to 8  
`seed`| A number used to initialize the random generation for reproducible results (default: 1).| INT| No| 0 to 2147483647  
`resolution`| The output resolution of the generated video.| COMBO| No| `"720p"`  
`"1080p"`  
`movement_amplitude`| The movement amplitude of objects in the frame.| COMBO| No| `"auto"`  
`"small"`  
`"medium"`  
`"large"`  
  
**Note:** The `first_frame` and `end_frame` images must have similar aspect ratios. The node validates that their aspect ratios are within a relative range of 0.8 to 1.25. Only one image is allowed for each input.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated video file.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu2StartEndToVideoNode/en.md)

* * *

**Source fingerprint (SHA-256):** `01316d15f95f264cadfb33978565fc320a9f42917693faa87c1367c0f31ca400`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Vidu2StartEndToVideoNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Vidu2StartEndToVideoNode)

[Vidu2ReferenceVideoNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Vidu2ReferenceVideoNode)[Vidu2TextToVideoNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Vidu2TextToVideoNode)

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
