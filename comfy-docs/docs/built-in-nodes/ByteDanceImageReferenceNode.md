---
url: https://docs.comfy.org/built-in-nodes/ByteDanceImageReferenceNode/
title: ByteDanceImageReferenceNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-18T12:01:27.562151+00:00
---

# ByteDanceImageReferenceNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ByteDanceImageReferenceNode/

Advanced

# ByteDanceImageReferenceNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ByteDance Image Reference Node generates videos using a text prompt and one to four reference images.

Copy pageCopy page

The ByteDance Image Reference Node generates videos using a text prompt and one to four reference images. It sends the images and prompt to an external API service that creates a video matching your description while incorporating the visual style and content from your reference images. The node provides various controls for video resolution, aspect ratio, duration, and other generation parameters.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The AI model to use for video generation (default: `"seedance-1-0-lite-i2v-250428"`).| STRING| Yes| `"seedance-1-0-pro-250528"`  
`"seedance-1-0-lite-i2v-250428"`  
`prompt`| The text prompt used to generate the video.| STRING| Yes| -  
`images`| One to four images. Each image must be between 300x300 and 6000x6000 pixels, with an aspect ratio between 0.4 and 2.5.| IMAGE| Yes| -  
`resolution`| The resolution of the output video.| STRING| Yes| `"480p"`  
`"720p"`  
`aspect_ratio`| The aspect ratio of the output video (default: `"adaptive"`).| STRING| Yes| `"adaptive"`  
`"16:9"`  
`"4:3"`  
`"1:1"`  
`"3:4"`  
`"9:16"`  
`"21:9"`  
`duration`| The duration of the output video in seconds (default: 5).| INT| Yes| 3 - 12  
`seed`| Seed to use for generation (default: 0).| INT| No| 0 - 2147483647  
`watermark`| Whether to add an “AI generated” watermark to the video (default: False).| BOOLEAN| No| -  
  
**Note:** The prompt text must not contain the following parameter strings: `--resolution`, `--ratio`, `--duration`, `--seed`, or `--watermark`. These values are controlled exclusively through their dedicated input widgets.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated video file based on the input prompt and reference images.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageReferenceNode/en.md)

* * *

**Source fingerprint (SHA-256):** `77a0f9aee920d07a1374eaec8489eed494a4505369246c16007765d67e52ef99`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ByteDanceImageReferenceNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ByteDanceImageReferenceNode)

[ByteDanceImageNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ByteDanceImageNode)[ComfyCloudFlux2TextToImageNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ComfyCloudFlux2TextToImageNode)

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
