---
url: https://docs.comfy.org/built-in-nodes/PikaImageToVideoNode2_2/
title: PikaImageToVideoNode2_2 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:42.048112+00:00
---

# PikaImageToVideoNode2_2 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/PikaImageToVideoNode2_2/

Pika

# PikaImageToVideoNode2_2 - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Pika Image to Video node sends an image and text prompt to the Pika API version 2.2 to generate a video.

Copy pageCopy page

The Pika Image to Video node sends an image and text prompt to the Pika API version 2.2 to generate a video. It converts your input image into video format based on the provided description and settings. The node handles the API communication and returns the generated video as output.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The image to convert to video| IMAGE| Yes| -  
`prompt_text`| The text description guiding video generation| STRING| Yes| -  
`negative_prompt`| Text describing what to avoid in the video| STRING| Yes| -  
`seed`| Random seed value for reproducible results| INT| Yes| -  
`resolution`| Output video resolution setting| STRING| Yes| -  
`duration`| Length of the generated video in seconds| INT| Yes| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated video file| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaImageToVideoNode2_2/en.md)

* * *

**Source fingerprint (SHA-256):** `aaa8dc49b94f0fae2010a3b61a3fb41e212fa9d2946a934a1a7c651fdced81b3`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/PikaImageToVideoNode2_2.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/PikaImageToVideoNode2_2)

[Pikaffects - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Pikaffects)[PikaScenesV2_2 - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/PikaScenesV2_2)

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
