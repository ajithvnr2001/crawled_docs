---
url: https://docs.comfy.org/built-in-nodes/Vidu2ImageToVideoNode/
title: Vidu2ImageToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:20.085680+00:00
---

# Vidu2ImageToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Vidu2ImageToVideoNode/

Vidu

# Vidu2ImageToVideoNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Vidu2 Image-to-Video Generation node creates a video sequence starting from a single input image.

Copy pageCopy page

The Vidu2 Image-to-Video Generation node creates a video sequence starting from a single input image. It uses a specified Vidu2 model to animate the scene based on an optional text prompt, controlling the video’s length, resolution, and the intensity of motion.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The Vidu2 model to use for video generation. Different models offer varying speed and quality trade-offs.| COMBO| Yes| `"viduq2-pro-fast"`  
`"viduq2-pro"`  
`"viduq2-turbo"`  
`image`| An image to be used as the start frame of the generated video. Only one image is allowed.| IMAGE| Yes| -  
`prompt`| An optional text prompt for video generation (max 2000 characters). Default is an empty string.| STRING| No| -  
`duration`| The length of the generated video in seconds. Default is 5.| INT| Yes| 1 to 10  
`seed`| A seed value for random number generation to ensure reproducible results. Default is 1.| INT| No| 0 to 2147483647  
`resolution`| The output resolution of the generated video. This parameter is advanced.| COMBO| Yes| `"720p"`  
`"1080p"`  
`movement_amplitude`| The movement amplitude of objects in the frame. This parameter is advanced.| COMBO| Yes| `"auto"`  
`"small"`  
`"medium"`  
`"large"`  
  
**Constraints:**

  * The `image` input must contain exactly one image.
  * The input image’s aspect ratio must be between 1:4 and 4:1.
  * The `prompt` text is limited to a maximum of 2000 characters.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated video file.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu2ImageToVideoNode/en.md)

* * *

**Source fingerprint (SHA-256):** `4cf56654286561f3d211ce50d0dce141880fe0e0a63aa45ab41ae0ff5ab6ccc3`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Vidu2ImageToVideoNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Vidu2ImageToVideoNode)

[Veo3VideoGenerationNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Veo3VideoGenerationNode)[Vidu2ReferenceVideoNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Vidu2ReferenceVideoNode)

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
