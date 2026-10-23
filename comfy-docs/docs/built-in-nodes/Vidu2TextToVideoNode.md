---
url: https://docs.comfy.org/built-in-nodes/Vidu2TextToVideoNode/
title: Vidu2TextToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:20.004255+00:00
---

# Vidu2TextToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Vidu2TextToVideoNode/

Vidu

# Vidu2TextToVideoNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Vidu2 Text-to-Video Generation node creates a video from a text description.

Copy pageCopy page

The Vidu2 Text-to-Video Generation node creates a video from a text description. It connects to an external API to generate video content based on your prompt, allowing you to control the video’s length, visual style, and format.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The AI model to use for video generation. Currently, only one model is available.| COMBO| Yes| `"viduq2"`  
`prompt`| A textual description for video generation, with a maximum length of 2000 characters.| STRING| Yes| -  
`duration`| The length of the generated video in seconds. The value can be adjusted using a slider (default: 5).| INT| No| 1 to 10  
`seed`| A number used to control the randomness of the generation, allowing for reproducible results. It can be controlled after generation (default: 1).| INT| No| 0 to 2147483647  
`aspect_ratio`| The proportional relationship between the video’s width and height.| COMBO| No| `"16:9"`  
`"9:16"`  
`"3:4"`  
`"4:3"`  
`"1:1"`  
`resolution`| The pixel dimensions of the generated video. This is an advanced parameter.| COMBO| No| `"720p"`  
`"1080p"`  
`background_music`| Whether to add background music to the generated video (default: False). This is an advanced parameter.| BOOLEAN| No| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated video file.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu2TextToVideoNode/en.md)

* * *

**Source fingerprint (SHA-256):** `27b7c05ae1b3b23d07e775f67474ecef1ffc0bd8240f4aa2219e15949d854f27`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Vidu2TextToVideoNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Vidu2TextToVideoNode)

[Vidu2StartEndToVideoNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Vidu2StartEndToVideoNode)[Vidu3ImageToVideoNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Vidu3ImageToVideoNode)

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
